#!/usr/bin/env python3
"""Programmatic gate for the 11:05 Midday Edition, Wednesday August 26 2026."""
import io, os, re, json, sys

D = os.path.dirname(os.path.abspath(__file__))
PAGES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']
S = {p: io.open(os.path.join(D, p), encoding='utf-8').read() for p in PAGES}
IX, CY, WS, MM = S['index.html'], S['cyber-briefing.html'], S['wallstreet-briefing.html'], S['mma-briefing.html']

fails, checks = [], 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)

def has(page, name, needle, n=None):
    c = S[page].count(needle) if page in S else page.count(needle)
    if n is None:
        ck(c >= 1, '%s: missing %r' % (name, needle[:80]))
    else:
        ck(c == n, '%s: expected %d of %r, found %d' % (name, n, needle[:80], c))

# ---------------------------------------------------------------- structure
for p in PAGES:
    s = S[p]
    for t in ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html', 'archive.html']:
        ck('href="%s"' % t in s, '%s: nav missing %s' % (p, t))
    for i in ['id="edition"', 'id="datestamp"', 'id="updated"', 'id="freshline"']:
        ck(s.count(i) == 1, '%s: %s count' % (p, i))
    ck('briefings refresh every 30 minutes' in s, '%s: freshness string' % p)
    ck(s.count('class="pill live"') == 1, '%s: live pill' % p)
    ck(s.count('<html') == 1 and s.count('</html>') == 1, '%s: html tags' % p)

# tldr: exactly one on each briefing, none on index
ck(IX.count('class="tldr"') == 0, 'index: must not carry a tldr')
for p, label in [('cyber-briefing.html', 'The Wire'),
                 ('wallstreet-briefing.html', 'The Tape'),
                 ('mma-briefing.html', 'Tale of the Tape')]:
    ck(S[p].count('class="tldr"') == 1, '%s: tldr count' % p)
    ck('<b>%s</b>' % label in S[p], '%s: tldr label %s' % (p, label))

# index cards carry each page's tldr verbatim
def tldr_body(s):
    i = s.find('<div class="tldr">')
    a = s.find('<span>', i) + len('<span>')
    return s[a:s.find('</span></div>', a)]

for cls, page in [('c-sec', 'cyber-briefing.html'), ('c-mkt', 'wallstreet-briefing.html'), ('c-mma', 'mma-briefing.html')]:
    m = re.search(r'<a class="bcard %s"[^>]*>(.*?)</a>' % cls, IX, re.S)
    ck(m is not None, 'index: card %s missing' % cls)
    if m:
        blk = m.group(1)
        ck(tldr_body(S[page]) in blk, 'index: card %s does not carry %s tldr verbatim' % (cls, page))
        h2 = re.search(r'<h2>(.*?)</h2>', blk, re.S)
        ck(h2 is not None and len(h2.group(1).strip()) > 20, 'index: card %s h2' % cls)
        ck('Read the briefing' in blk, 'index: card %s CTA' % cls)

# ------------------------------------------------- TradingView JSON parses
blocks = re.findall(r'embed-widget-[a-z\-]+\.js" async>(\{.*?\})</script>', WS, re.S)
ck(len(blocks) == 8, 'WS: expected 8 TradingView blocks, found %d' % len(blocks))
for b in blocks:
    try:
        json.loads(b)
        checks += 1
    except Exception as e:
        fails.append('WS: TradingView JSON parse failure: %s' % e)

tape = re.search(r'embed-widget-ticker-tape\.js" async>(\{.*?\})</script>', WS, re.S)
ck(tape is not None, 'WS: ticker tape block')
if tape:
    syms = [x['proName'] for x in json.loads(tape.group(1))['symbols']]
    for m_ in ['FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI', 'TVC:USOIL', 'TVC:US10Y']:
        ck(m_ in syms, 'WS tape: mandatory symbol %s missing' % m_)
    ck(len(syms) == len(set(syms)), 'WS tape: duplicate symbols')
    ck('NYSE:ANF' in syms, 'WS tape: ANF retained')
    ck('NASDAQ:SEDG' in syms, 'WS tape: SEDG added')
    ck('NYSE:BSX' not in syms, 'WS tape: BSX should be dropped')
    ck('NYSE:DKS' not in syms, 'WS tape: DKS must stay absent')

cod = re.search(r'embed-widget-mini-symbol-overview\.js" async>(\{.*?\})</script>', WS, re.S)
ck(cod is not None and json.loads(cod.group(1))['symbol'] == 'NYSE:ANF', 'WS: Chart of the Day must be NYSE:ANF')

# --------------------------------------------------- markets arithmetic
# Tuesday closes as published
TUE = {'sp': 7677.28, 'dow': 53577.40, 'nas': 26151.30, 'rut': 3010.02}
# 11:06 S&P read
lvl, pts, pct = 7681.36, 4.08, 0.05
ck(round(lvl - pts, 2) == TUE['sp'], 'WS: 11:06 S&P level-points != Tuesday close')
ck(round(pts / TUE['sp'] * 100, 2) == pct, 'WS: 11:06 S&P percent does not reconcile')
has('wallstreet-briefing.html', 'WS', '7,681.36')
has('wallstreet-briefing.html', 'WS', '4.08')
has('wallstreet-briefing.html', 'WS', '11:06&nbsp;a.m.')
# 9:59 board still reconciles
for name, lv, pt, pc, key in [('S&P', 7686.64, 9.36, 0.12, 'sp'), ('Dow', 53594.69, 17.29, 0.03, 'dow'),
                              ('Nasdaq', 26173.36, 22.06, 0.08, 'nas'), ('Russell', 3007.66, -2.36, -0.08, 'rut')]:
    ck(round(lv - pt, 2) == TUE[key], 'WS 9:59 board: %s level-points mismatch' % name)
    ck(abs(pt / TUE[key] * 100 - pc) < 0.006, 'WS 9:59 board: %s percent mismatch' % name)
# INTU / ANF
ck(round(345.35 + 12.11, 2) == 357.46, 'WS: INTU arithmetic')
ck(abs(12.11 / 357.46 * 100 - 3.39) < 0.01, 'WS: INTU percent')
ck(round(142.50 - 33.59, 2) == 108.91, 'WS: ANF implied prior close')
i = WS.find('$108.91')
ck(i > 0 and 'implied' in WS[max(0, i - 300):i + 300], 'WS: $108.91 must sit near the word "implied"')

# no level published for Dow/Nasdaq at 11:06
seg = WS[WS.find('New at 11:05'):WS.find('New at 11:05') + 2200]
ck('Dow down about 0.2%' in seg.replace('&nbsp;', ' ').replace('<b>', '').replace('</b>', ''),
   'WS: Dow direction-only line')
ck('directions only' in seg, 'WS: must state Dow/Nasdaq are directions only')

for g in ['SolarEdge', '&plus;8.3%', '$42 from $36', 'Williams Companies', '&plus;5.6%',
          'Zoom Communications', '&minus;6.2%', 'Moderna', '&minus;5%', '&minus;9.2%',
          'slide as PCE inflation stays sticky', 'hold steady']:
    has('wallstreet-briefing.html', 'WS', g)
# carried figures still present
for g in ['+30.85%', '$142.50', '$4.17', '$1.98', '$1.27&nbsp;billion', '$13.10&ndash;$13.60',
          '$10.20&ndash;$11.00', '$500&nbsp;million', '3.7%', '3.3%', 'LSEG', 'Zaccarelli',
          'Northlight', 'Hathorn', 'Capital.com', '$81.52', '15.51', 'Rob Bonta', '29 states']:
    has('wallstreet-briefing.html', 'WS', g)

# ------------------------------------------------------------------- cyber
for g in ['CVE-2026-15981', 'CVE-2026-61979', 'miniOrange', 'Xecurify', 'Patchstack',
          'DigitalOcean', 'Ravie Lakshmanan', '17.0.5', '17.0.6', 'openssl_verify',
          'mo_saml_validate_signature', 'wp_set_auth_cookie', '207.211.214.41', '64.225.25.188',
          'opportunistic scanning rather than a targeted campaign',
          'CoreRAT', 'Core Werewolf', 'BI.ZONE', 'UltraVNC', 'Telegram',
          'nothing seen this run', 'CVE-2026-21962 is the Oracle', '1.27.1',
          '5.03%', '$46.90', '20-day low', 'CVE-2026-71362', 'APSB26-92', 'Sansec']:
    has('cyber-briefing.html', 'CY', g)
_na = [m.start() for m in re.finditer('nothing added', CY)]
ck(len(_na) == 2, 'CY: expected exactly 2 contextual "nothing added" occurrences, got %d' % len(_na))
for _i in _na:
    _ctx = CY[max(0, _i-200):_i+200]
    ck(('That was wrong' in _ctx) or ('never as' in _ctx),
       'CY: "nothing added" used as a claim, not a correction/wording rule')
ck(CY.count('fourth consecutive edition') == 1, 'CY: fourth consecutive edition')
# CVSS split published correctly, never both at 9.8
ck(re.search(r'CVE-2026-15981[^<]{0,40}\(CVSS&nbsp;9\.8\)', CY) is not None
   or 'CVE-2026-15981 (CVSS&nbsp;9.8)' in CY, 'CY: 15981 must be 9.8')
ck('CVE-2026-61979 (CVSS&nbsp;8.1)' in CY or re.search(r'CVE-2026-61979[^<]{0,40}\(CVSS&nbsp;8\.1\)', CY),
   'CY: 61979 must be 8.1')
ck('CVE-2026-61979</td><td>8.1</td>' in CY, 'CY: vuln table 61979 = 8.1')
ck('CVE-2026-15981</td><td>9.8</td>' in CY, 'CY: vuln table 15981 = 9.8')

# KEV countdown spans still consistent
spans = re.findall(r'<span class="kevdue ([a-z]+)">([^<]*)</span>', CY)
spans = [c + ' ' + t for c, t in spans]
ck(len(spans) == 14, 'CY: expected 14 kevdue spans, found %d' % len(spans))
overdue = sum(1 for x in spans if 'past due' in x.lower())
today = sum(1 for x in spans if 'due today' in x.lower())
ahead = sum(1 for x in spans if 'left' in x.lower())
ck(overdue + today + ahead == len(spans), 'CY: kevdue spans not fully classified')
for _c, _t in re.findall(r'<span class="kevdue ([a-z]+)">([^<]*)</span>', CY):
    ck((_c == 'crit') == ('past due' in _t or 'due today' in _t),
       'CY: kevdue colour/text disagreement: %s / %s' % (_c, _t))
ck(overdue == 10, 'CY: expected 10 overdue, got %d' % overdue)
ck(today == 0, 'CY: expected 0 due today, got %d' % today)
ck(ahead == 4, 'CY: expected 4 ahead, got %d' % ahead)
ck('August&nbsp;27' in CY, 'CY: Oracle Aug 27 deadline')
ck('August&nbsp;28' in CY, 'CY: Gitea Aug 28 deadline')

# ---------------------------------------------------------------------- mma
CHAMPS = ['Tom Aspinall', 'Ciryl Gane', 'Carlos Ulberg', 'Sean Strickland', 'Islam Makhachev',
          'Justin Gaethje', 'Alexander Volkanovski', 'Petr Yan', 'Joshua Van',
          'Valentina Shevchenko', 'Kayla Harrison', 'Mackenzie Dern']
board = MM[MM.find('<div class="lab">Champions board</div>'):]
board = board[:board.find('</table>')]
rows = re.findall(r'<tr>(.*?)</tr>', board, re.S)
ck(len(rows) == 12, 'MMA champions: expected 12 <tr> incl header, got %d' % len(rows))
champ_col = ' '.join(re.findall(r'<td>(.*?)</td>', r, re.S)[1] for r in rows[1:] if len(re.findall(r'<td>(.*?)</td>', r, re.S)) > 1)
for stale in ['Pereira', 'Chimaev', 'Topuria', 'Dvalishvili', 'Pantoja', 'Jandiroba', 'Pe&ntilde;a', 'Procházka']:
    ck(stale not in champ_col, 'MMA champions: stale name %s in champion column' % stale)
ck('vacant' not in champ_col.lower(), 'MMA champions: no belt may be vacant')
for c in CHAMPS:
    ck(c in board, 'MMA champions: %s missing' % c)

for g in ['&minus;470', '+360', '&minus;700', '+500', '+385', '&minus;500 / +375',
          'Shanghai Oriental Sports Center', 'Umar Nurmagomedov', 'Song Yadong',
          '20-1', '23-9-1', '6:00&nbsp;a.m. EDT', 'Denise Gomes',
          'Andrew Schleimer', 'Mark Shapiro', '$30&nbsp;million', '$60&nbsp;million']:
    has('mma-briefing.html', 'MMA', g)
cdn = re.search(r"2026-08-29T06:00:00-04:00", MM)
ck(cdn is not None, 'MMA: countdown target must be 2026-08-29T06:00:00-04:00')
ck('2026-08-29T00:00' not in MM, 'MMA: countdown must not be midnight')
ck(MM.count('id="ufccdn"') == 1, 'MMA: ufccdn element')

# ----------------------------------------------------- New-tag hygiene
counts = {'wallstreet-briefing.html': 1, 'cyber-briefing.html': 1, 'mma-briefing.html': 1, 'index.html': 0}
for p, n in counts.items():
    ck(S[p].count('class="tag new"') == n, '%s: expected %d New tag(s), got %d' % (p, n, S[p].count('class="tag new"')))
    for t in re.findall(r'<span class="tag new">(.*?)</span>', S[p]):
        ck(t == 'New &middot; 11:05', '%s: bad New tag text %r' % (p, t))
    ck('New &middot; 10:45' not in S[p], '%s: undemoted 10:45 New tag' % p)
    ck('New &middot; 10:20' not in S[p], '%s: undemoted 10:20 New tag' % p)
    ck('New &middot; 9:40' not in S[p], '%s: undemoted 9:40 New tag' % p)

# ------------------------------------------------------------- trap greps
TRAPS = ['Cody Salkilld', 'Abdul-Rakhman', 'Shamil Yakhyaev', 'title challenger Beneil',
         'Shanghai Indoor Stadium&rdquo;' if False else 'Pereira retains', 'Featherweight vacant',
         'markets closed higher today', '@@T@@', 'UFC Fight Night 286', 'Fight Night 286',
         'UFC 336', 'UFC 335', 'no source fetched at 8:44', 'is not printing a number yet',
         '&minus;500 / +380', 'Figueiro&nbsp;', 'U.S. markets are still not open',
         'session has not opened', 'Suno', '$1.4 trillion', 'slipped 0.12%',
         'No opening level for any index',
         'largest single-name move any source fetched this run puts a number on is Intuit']
for p in PAGES:
    for t in TRAPS:
        ck(t not in S[p], 'TRAP %r found in %s' % (t, p))

# forward dates still in the future
for d in ['Aug 29', 'Sep 19', 'August&nbsp;27', 'August&nbsp;28']:
    pass
ck('Sat, Aug 29' in MM, 'MMA: Aug 29 card still upcoming')

print('%d checks, %d failures' % (checks, len(fails)))
for f in fails:
    print('  FAIL:', f)
sys.exit(1 if fails else 0)
