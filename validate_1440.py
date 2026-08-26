#!/usr/bin/env python3
"""Validation gate for the 2:44 p.m. ET Midday Edition, Wed Aug 26 2026."""
import re, sys, os, html

D = sys.argv[1] if len(sys.argv) > 1 else '.'
PAGES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']
S = {f: open(os.path.join(D, f), encoding='utf-8').read() for f in PAGES}
fails, checks = [], 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)

def norm(t):
    """Strip tags AND normalise entities before any text assertion."""
    t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = (t.replace('&nbsp;', ' ').replace('&mdash;', '-').replace('&ndash;', '-')
           .replace('&minus;', '-').replace('&plus;', '+').replace('&amp;', '&')
           .replace('&rsquo;', "'").replace('&lsquo;', "'").replace('&ldquo;', '"')
           .replace('&rdquo;', '"').replace('&middot;', '.').replace('&divide;', '/')
           .replace('&#9679;', '*').replace('&#9888;', '!'))
    return re.sub(r'\s+', ' ', t)

W, C, M, I = S['wallstreet-briefing.html'], S['cyber-briefing.html'], S['mma-briefing.html'], S['index.html']
w, c, m, i = norm(W), norm(C), norm(M), norm(I)

# ---------------------------------------------------------------- ARITHMETIC
def r2(x): return round(x + 1e-12, 2)

# (label, level, change, pct, prior_close) -- change signed
INDEX = [
    ('S&P 1:25',    7674.09,   -3.19,   -0.04, 7677.28),
    ('Dow 1:25',   53469.42, -107.98,   -0.20, 53577.40),
    ('Nasdaq 1:25',26101.79,  -49.51,   -0.19, 26151.30),
    ('VIX 1:25',      15.55,    0.10,    0.65, 15.45),
    ('Gold 12:05',  4655.50,  -39.00,   -0.83, 4694.50),
    ('WTI 12:05',     82.88,    0.52,    0.63, 82.36),
    ('ANF 2:40',     153.40,   44.50,   40.86, 108.90),
    ('XPON 2:40',      8.86,    3.59,   68.12, 5.27),
    ('INTU 2:40',    339.41,  -18.05,   -5.05, 357.46),
    ('CRE 2:40',       6.18,    3.61,  140.47, 2.57),
    ('META 2:40',    577.46,    7.41,    1.30, 570.05),
    ('NVDA 2:07',    209.99,   -3.06,   -1.44, 213.05),
    ('AMD 2:07',     483.88,    4.70,    0.98, 479.18),
    ('AAPL 2:07',    313.17,    3.27,    1.05, 309.90),
    ('MSFT 2:07',    494.72,    3.01,    0.61, 491.71),
    ('AMZN 2:07',    258.93,   -2.13,   -0.82, 261.06),
    ('GOOG 2:07',    338.26,   -5.08,   -1.48, 343.34),
    ('TSLA 2:07',    346.46,   -3.79,   -1.08, 350.25),
    ('BTC 12:05',  78100.48,-1052.82,   -1.33, 79153.30),
]
for lab, lvl, chg, pct, prior in INDEX:
    ck(r2(lvl - chg) == r2(prior), f'ARITH {lab}: {lvl} - ({chg}) != {prior}')
    raw = chg / prior * 100
    rounded = round(raw, 2)
    trunc = int(raw * 100 - (0 if raw >= 0 else 1) * 0) / 100 if raw >= 0 else -int(-raw * 100) / 100
    trunc = (int(raw * 100) / 100) if raw >= 0 else -(int(-raw * 100) / 100)
    ok_r = abs(rounded - pct) < 0.005
    ok_t = abs(trunc - pct) < 0.005
    ck(ok_r or ok_t, f'ARITH {lab}: {chg}/{prior} = {raw:.4f}%, page says {pct}%')
    if ok_t and not ok_r:
        ck('truncated rather than rounded' in w,
           f'ARITH {lab}: {pct}% is truncated, not rounded - the page must disclose that')
    # the level must actually appear on the Wall Street page
    ck(f'{lvl:,.2f}' in w, f'ARITH {lab}: level {lvl:,.2f} not printed on the page')

# Russell: deliberately published as one cent out; assert the page SAYS so.
ck(r2(3003.81 + 6.22) == 3010.03, 'Russell arithmetic sanity')
ck('one cent out' in w, 'Russell one-cent discrepancy must be disclosed on the page')

# Rejected / flagged figures must appear only inside an explicit rejection context.
for bad, why in [('41.8', 'StockStory percent'), ('30.68', 'DKS Tuesday move'),
                 ('7,677.24', 'Zacks S&P close')]:
    ck(bad in w, f'REJECT {why}: expected the figure to be present and flagged')
    seg = w[max(0, w.find(bad) - 700): w.find(bad) + 700]
    ck(any(k in seg for k in ('reject', 'does not reconcile', 'discrepancy', 'not published',
                              'not adopted', 'not asserted')),
       f'REJECT {why}: {bad} appears without a rejection window')

# Figures deliberately dropped must NOT be published as current.
bi = w.find('62.45')
ck(bi != -1 and 'is dropped' in w[max(0, bi-400):bi+400],
   'BAC must appear only inside an explicit drop window')

# ---------------------------------------------------------------- STRUCTURE
tv = 'tradingview.com/external-embedding/embed-widget-'
for name, n in [('ticker-tape', 1), ('single-quote', 3), ('timeline', 1),
                ('stock-heatmap', 1), ('mini-symbol-overview', 1), ('events', 1)]:
    ck(W.count(tv + name) == n, f'WIDGET {name}: expected {n}, got {W.count(tv+name)}')
ck('tradingview.com' not in I, 'index.html must carry no TradingView widget')

for sym in ['FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI', 'TVC:USOIL', 'TVC:US10Y']:
    ck(sym in W, f'TAPE: mandatory symbol {sym} missing')
tape = W[W.find(tv + 'ticker-tape'):]
tape = tape[:tape.find('</script>')]
syms = re.findall(r'"proName":"([^"]+)"', tape)
ck(len(syms) == len(set(syms)), f'TAPE: duplicate symbols {syms}')

# Chart of the Day must be scoped to the mini-overview block and be ANF.
mo = W[W.find(tv + 'mini-symbol-overview'):]
mo = mo[:mo.find('</script>')]
ck('"symbol":"NYSE:ANF"' in mo, f'CHART: expected NYSE:ANF, got {mo[:200]}')

# Nav: five links, right order, exactly one active per page.
NAV = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html',
       'mma-briefing.html', 'archive.html']
ACTIVE = dict(zip(PAGES, [0, 1, 2, 3]))
for f in PAGES:
    nav = re.search(r'<nav class="tabs">(.*?)</nav>', S[f], re.S)
    ck(nav is not None, f'NAV {f}: missing')
    if not nav:
        continue
    links = re.findall(r'<a href="([^"]+)"([^>]*)>', nav.group(1))
    ck([l[0] for l in links] == NAV, f'NAV {f}: order {[l[0] for l in links]}')
    on = [k for k, (href, attrs) in enumerate(links) if 'class="on"' in attrs]
    ck(on == [ACTIVE[f]], f'NAV {f}: active tab {on}, expected [{ACTIVE[f]}]')

# Masthead pills + freshness + per-page tldr label.
for f in PAGES:
    for el in ['id="edition"', 'id="datestamp"', 'id="updated"']:
        ck(el in S[f], f'MASTHEAD {f}: {el} missing')
for f, label in [('wallstreet-briefing.html', 'The Tape'), ('cyber-briefing.html', 'The Wire'),
                 ('mma-briefing.html', 'Tale of the Tape')]:
    ck(S[f].count('class="tldr"') == 1, f'TLDR {f}: expected exactly one')
    ck(f'<b>{label}</b>' in S[f], f'TLDR {f}: label "{label}" missing')
    ck('id="freshline"' in S[f], f'FRESHLINE {f}: missing')
ck('class="tldr"' not in I, 'index.html carries cards, not a tldr strip')
ck('id="ufccdn"' in M, 'MMA countdown target missing')

# Balance.
for f in PAGES:
    for tag in ['div', 'section', 'table', 'tr', 'ul', 'script']:
        o = len(re.findall(rf'<{tag}[\s>]', S[f]))
        cl = len(re.findall(rf'</{tag}>', S[f]))
        ck(o == cl, f'BALANCE {f}: <{tag}> {o} open vs {cl} close')

# ------------------------------------------------------------ NEW-TAG HYGIENE
for f in PAGES:
    for tag in re.findall(r'<span class="tag new">([^<]*)</span>', S[f]):
        ck('2:44' in tag, f'NEWTAG {f}: stale "New" tag "{norm(tag)}"')
    for mm2 in re.findall(r'\* New at ([0-9:]+)', norm(S[f])):
        ck(mm2 == '2:44', f'NEWTAG {f}: stale "New at {mm2}" marker')

# ---------------------------------------------------------------- CYBER GATES
kl = C.find('CISA KEV &amp; federal deadlines</div>')
ck(kl != -1, 'KEV: section label not found')
kev = C[kl:C.find('Sources</div>', kl)]
cds = re.findall(r'<span class="kevdue[^"]*"[^>]*>(.*?)</span>', kev, re.S)
ck(len(cds) == 14, f'KEV: expected 14 countdown spans, got {len(cds)}')
crit = re.findall(r'<span class="kevdue crit"[^>]*>', kev)
okc = re.findall(r'<span class="kevdue ok"[^>]*>', kev)
ck(len(crit) == 10, f'KEV: expected 10 past-due (crit) spans, got {len(crit)}')
ck(len(okc) == 4, f'KEV: expected 4 in-window (ok) spans, got {len(okc)}')
ck('14 rows, 10 of them past due' in norm(C), 'KEV: board size statement missing')

# Every countdown must agree, in Python, with the due date printed beside it,
# and its colour must agree with its own text.
from datetime import date
TODAY = date(2026, 8, 26)
MON = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,
       'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
pairs = re.findall(r'due\s+([A-Z][a-z]{2})[&nbsp;\s]+(\d{1,2})\s*</b>?\s*\.?\s*'
                   r'</?[^>]*>?\s*<span class="kevdue ([^"]+)"[^>]*>(.*?)</span>', kev, re.S)
if not pairs:
    pairs = []
    for mm3 in re.finditer(r'<span class="kevdue ([^"]+)"[^>]*>(.*?)</span>', kev, re.S):
        before = norm(kev[max(0, mm3.start() - 260): mm3.start()])
        dm = re.findall(r'due ([A-Z][a-z]{2}) (\d{1,2})', before)
        if dm:
            pairs.append((dm[-1][0], dm[-1][1], mm3.group(1), mm3.group(2)))
ck(len(pairs) == 14, f'KEV: matched {len(pairs)} date/countdown pairs, expected 14')
for mon, day, cls, text in pairs:
    yr = 2026
    due = date(yr, MON[mon], int(day))
    delta = (due - TODAY).days
    tn = norm(text).strip().lower()
    if delta < 0:
        ck('overdue' in tn or 'past due' in tn,
           f'KEV: {mon} {day} is {abs(delta)}d past due but reads "{tn}"')
        ck(cls.strip() == 'crit', f'KEV: {mon} {day} overdue but coloured "{cls}"')
    elif delta == 0:
        ck('today' in tn or 'due today' in tn or '0 day' in tn,
           f'KEV: {mon} {day} is due today but reads "{tn}"')
        ck(cls.strip() == 'crit', f'KEV: {mon} {day} due today but coloured "{cls}"')
    else:
        want = f'{delta} day left' if delta == 1 else f'{delta} days left'
        ck(want in tn, f'KEV: {mon} {day} is {delta}d away but reads "{tn}"')
        ck(cls.strip() == 'ok', f'KEV: {mon} {day} in window but coloured "{cls}"')

# Patch Priority deadlines must match the KEV board after month-abbreviation
# AND entity normalisation (the two sections spell the month differently).
def dates(t):
    t = norm(t).replace('August', 'Aug').replace('September', 'Sep')
    return set(re.findall(r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}\b', t))
pp = C[C.find('Patch priority'):C.find('Threat actor spotlight')]
for d in ['Aug 27', 'Aug 28']:
    ck(d in dates(pp), f'PATCH PRIORITY: deadline "{d}" missing')
    ck(d in dates(kev), f'KEV BOARD: deadline "{d}" missing (must match Patch Priority)')

# New CVE row present, with vendor-grade score and no exploitation claim.
ck('CVE-2026-19490' in C, 'CYBER: new CVE row missing')
row = re.search(r'<tr><td>CVE-2026-19490.*?</tr>', C, re.S)
ck(row is not None, 'CVE-2026-19490: table row not found')
seg = norm(row.group(0)) if row else ''
ck('9.3' in seg, 'CVE-2026-19490: CVSS 9.3 missing')
ck('had not observed in-the-wild exploitation' in seg, 'CVE-2026-19490: must state no ITW exploitation')
ck('CVE-2026-3055' in seg, 'CVE-2026-19490: must be distinguished from CVE-2026-3055')
ck('Not in KEV' in seg, 'CVE-2026-19490: must state it carries no federal deadline')

# ------------------------------------------------------------------ MMA GATES
board = M[M.find('Champions board'):M.find('Sources</div>', M.find('Champions board'))]
ck(board.count('<tr') == 12, f'CHAMPIONS: expected 12 <tr> incl. header, got {board.count("<tr")}')
tbl = board[board.find('<table'):board.find('</table>')]
champ_col = []
for r in re.findall(r'<tr.*?</tr>', tbl, re.S)[1:]:
    cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S)
    ck(len(cells) == 4, f'CHAMPIONS: row has {len(cells)} cells, expected 4')
    champ_col.append(norm(cells[1]))
ck(len(champ_col) == 11, f'CHAMPIONS: expected 11 incumbents, got {len(champ_col)}')
joined = ' | '.join(champ_col)
for stale in ['Pereira', 'Chimaev', 'Topuria', 'vacant', 'Vacant']:
    ck(stale not in joined, f'CHAMPIONS: stale name/state "{stale}" in the champion column')
nb = norm(board)
for champ in ['Aspinall', 'Ulberg', 'Strickland', 'Makhachev', 'Gaethje',
              'Volkanovski', 'Yan', 'Van', 'Shevchenko', 'Harrison', 'Dern']:
    ck(champ in joined, f'CHAMPIONS: incumbent "{champ}" missing from the champion column')
ck('Oriental Sports Center' in m, 'MMA: venue missing')
si = m.find('Shanghai Indoor Stadium')
while si != -1:
    seg = m[max(0, si - 900): si + 400]
    ck('reject' in seg, 'MMA: "Shanghai Indoor Stadium" outside a rejection window')
    si = m.find('Shanghai Indoor Stadium', si + 1)

# ------------------------------------------------------------------ TRAP GREPS
TRAPS = ['Cody Salkilld', 'Shamil Yakhyaev', 'Abdul-Rakhman',
         'Fight Night 286', '$1.4 trillion', 'Suno', 'No opening level for any index',
         'former champion Umar', 'title challenger Beneil']
for f in PAGES:
    for t in TRAPS:
        ck(t not in norm(S[f]), f'TRAP {f}: "{t}" present')

# Chronology: nothing "upcoming" that already happened.
ck('Aug 29' in m or 'August 29' in m, 'MMA: next card date missing')

# "slipped 0.12%" is a documented rejected figure; it may appear only in that window.
si = w.find('slipped 0.12%')
while si != -1:
    ck('rejected' in w[max(0, si-600):si+900],
       'TRAP ws: "slipped 0.12%" outside its rejection window')
    si = w.find('slipped 0.12%', si + 1)

# Index cards must mirror each page's own verified lead.
ck('40.86' in i and '40.86' in w, 'INDEX CARD: markets summary not supported by the page')
ck('CVE-2026-19490' in i and 'CVE-2026-19490' in c, 'INDEX CARD: cyber summary not supported')
ck('Oriental Sports Center' in i and 'Oriental Sports Center' in m, 'INDEX CARD: MMA summary not supported')
ck('twenty-fourth' in i and 'twenty-fourth' in m, 'INDEX CARD: champions streak mismatch')

# ------------------------------------------------------------------- REPORT
print(f'{checks} checks, {len(fails)} failures')
for f in fails:
    print('  FAIL:', f)
sys.exit(1 if fails else 0)
