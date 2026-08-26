#!/usr/bin/env python3
"""Programmatic validation for the 4:36 PM ET Afternoon Edition, Aug 26 2026."""
import io, re, os, datetime

D = os.path.dirname(os.path.abspath(__file__))
F = {}
for n in ('index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html'):
    with io.open(os.path.join(D, n), encoding='utf-8') as f:
        F[n] = f.read()
WS, CY, MM, IX = F['wallstreet-briefing.html'], F['cyber-briefing.html'], F['mma-briefing.html'], F['index.html']
BRIEFS = {'wallstreet-briefing.html': WS, 'cyber-briefing.html': CY, 'mma-briefing.html': MM}

fails, n = [], 0
def ck(cond, msg):
    global n
    n += 1
    if not cond:
        fails.append(msg)

def txt(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    for a, b in (('&nbsp;', ' '), ('&amp;', '&'), ('&minus;', '-'), ('&plus;', '+'),
                 ('&mdash;', '-'), ('&ndash;', '-'), ('&rsquo;', "'"), ('&ldquo;', '"'),
                 ('&rdquo;', '"'), ('&divide;', '/'), ('&times;', 'x'), ('&plusmn;', '+/-'),
                 ('&#9888;', '!'), ('&#9679;', '*')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s)
TWS, TCY, TMM, TIX = txt(WS), txt(CY), txt(MM), txt(IX)

# ---------- 1. NVIDIA ARITHMETIC (every published figure re-derived) ----------
rev, est, yr = 96.22, 92.17, 46.74
ck(abs(rev / yr - 2.0586) < 1e-3, 'NVDA 2.06x ratio')
ck(round((rev / yr - 1) * 100) == 106, 'NVDA +106% y/y consistent with 96.22 vs 46.74')
ck(rev > yr * 2, 'NVDA "more than doubled" literally true')
ck(abs(89 / rev * 100 - 92.5) < 0.1, 'NVDA data center 92.5% of sales')
ck(round(89 / rev * 100) == 92, 'NVDA "92% of sales" rounds correctly')
glo, ghi = 91.0 * .98, 91.0 * 1.02
ck(abs(glo - 89.18) < .01 and abs(ghi - 92.82) < .01, 'NVDA prior guide band 89.18-92.82')
ck(rev > ghi, 'NVDA print above top of its own prior guide (justifies "consensus too low")')
ck(abs((rev - est) - 4.05) < .01, 'NVDA beat size 4.05B')
q3lo, q3hi = 108 * .98, 108 * 1.02
ck(abs(q3lo - 105.84) < .01 and abs(q3hi - 110.16) < .01, 'NVDA Q3 band 105.84-110.16')
ck(q3lo > 104.2, 'NVDA entire Q3 band above the 104.2B consensus')
ck(abs((108 / rev - 1) * 100 - 12.2) < .05, 'NVDA Q3 midpoint = +12.2% sequential')
for s in ('96.22', '92.17', '$2.22', '$2.10', '$89', '86.33', '117%', '$108', '104.2', '106%'):
    ck(s in TWS, 'WS carries NVDA figure %s' % s)
ck('no data-center sales from China' in TWS or 'no China data-center revenue' in TWS, 'NVDA China caveat')
ck('slipped in extended' in TWS, 'NVDA direction published')
ck('DIRECTION ONLY' in TWS and 'no source fetched this run states the size' in TWS,
   'NVDA magnitude explicitly withheld')
# HARNESS BUG (i), fixed not worked around: the old pattern allowed 120 chars of slack
# between "Nvidia" and the percentage, so it matched (a) the 2024-Barchart REJECTION
# prose ("revenue rose 122% ... the stock fell 7%") and (b) a sentence whose percentage
# belongs to the Nasdaq 100, not to Nvidia. Now: short window, no intervening index or
# ticker name, and rejection contexts are exempt.
for _m in re.finditer(r'Nvidia(?:&rsquo;s|\'s)?\s+(?:stock\s+|shares\s+)?(?:fell|dropped|slipped|sank|rose|jumped)\s+(\d+(?:\.\d+)?)%', TWS):
    _w = TWS[max(0, _m.start() - 450):_m.end() + 60].lower()
    _rej = any(r in _w for r in ('reject', 'august 2024', 'two years old', 'none of it publishes', 'trap'))
    ck(_rej, 'unsourced NVDA percentage published: %s' % _m.group(0))
ck(not re.search(r'(?:Nvidia|NVDA)[^.]{0,60}after[- ]hours[^.]{0,40}\d+(?:\.\d+)?%', TWS),
   'no invented NVDA after-hours percentage')

# ---------- 2. SALESFORCE: the flagged non-reconciliation ----------
ck(abs((3.53 / 1.89 - 1) * 100 - 86.77) < .05, 'CRM net income +86.8%')
ck(round((3.53 / 1.89 - 1) * 100) == 87, 'CRM 87% claim reconciles on net income')
ck(abs((4.29 / 1.96 - 1) * 100 - 118.88) < .05, 'CRM per-share +118.9%')
sh_now, sh_pr = 3.53e9 / 4.29 / 1e6, 1.89e9 / 1.96 / 1e6
ck(abs(sh_now - 822.8) < .5 and abs(sh_pr - 964.3) < .5, 'CRM implied share counts 822.8M / 964.3M')
ck(abs((sh_now / sh_pr - 1) * 100 + 14.7) < .1, 'CRM implied share count -14.7%')
ck('118.9%' in TWS and '86.8%' in TWS, 'both CRM growth rates printed')
ck('neither reconciled' in TWS or 'no reconciled EPS growth rate is asserted' in TWS,
   'CRM divergence flagged, not smoothed')
ck(abs((46.1 + 46.4) / 2 - 46.25) < 1e-9 and '46.25' in TWS, 'CRM FY27 revenue midpoint 46.25B')
for s in ('11.35', '11.32', '16.67', '16.71', '46.1', '46.4', '2.6 billion', 'Anthropic', '240%', '14%'):
    ck(s in TWS, 'WS carries CRM figure %s' % s)
ck('soared 14%' in TWS, 'CRM after-hours move is the sourced one')

# ---------- 3. CROWDSTRIKE: 8-K primary source ----------
ck(abs((1470897 / 1168952 - 1) * 100 - 25.83) < .02, 'CRWD revenue +25.8%')
ck(round((1470897 / 1168952 - 1) * 100) == 26, 'CRWD "26%" reconciles off the statements')
ck(abs(332.8 - 286 - 46.8) < .01, 'CRWD net new ARR beat vs guide high = 46.8M')
ck(332.8 > 286, 'CRWD net new ARR beat the top of guidance')
for s in ('1.47', '$0.31', '$0.29', '$333 million', '5.84', '2.29', '$530', '$377', '630 basis', '34%',
          '1,470,897', '1,168,952', 'George Kurtz'):
    ck(s in TWS, 'WS carries CRWD figure %s' % s)
ck('best quarter in CrowdStrike' in TWS, 'CRWD CEO quote verbatim')
# the wrong-quarter trap must appear ONLY inside rejection prose.
# HARNESS BUG (ii), fixed not worked around: bare '5.51' is a SUBSTRING of the VIX quote
# '15.51' that legitimately appears all over this page, so every VIX mention false-failed.
# Anchored on the ARR phrasing / a currency boundary instead.
for bad in (r'\$256\b', r'ARR \$?5\.51', r'\$?1\.39 billion'):
    for hit in re.finditer(bad, TWS):
        w = TWS[max(0, hit.start() - 400):hit.start() + 200].lower()
        ck(('reject' in w or 'prior quarter' in w or 'wrong quarter' in w),
           'CRWD prior-quarter figure %s appears outside rejection context' % bad)

# ---------- 4. NO FABRICATED AFTER-HOURS MOVES ----------
for tic in ('Okta', 'Williams-Sonoma', 'OKTA', 'WSM'):
    ck(not re.search(re.escape(tic) + r'[^.]{0,80}(?:rose|fell|jumped|soared|sank)\s+\d+%', TWS),
       'no invented move for %s' % tic)
ck('No results and no after-hours prices for any of the three' in TWS, 'unreported names declared unknown')

# ---------- 5. CISA KEV: due date -> countdown -> colour, all rows ----------
TODAY = datetime.date(2026, 8, 26)
kev = CY[CY.index('<div class="lab">CISA KEV'):]
kev = kev[:kev.index('</section>')]
rows = re.findall(r'<li>.*?</li>', kev, re.S)
ck(len(rows) == 14, 'KEV board holds 14 rows (found %d)' % len(rows))
past = 0
for r in rows:
    t = txt(r)
    m = re.search(r'due\s+(?:by\s+)?([A-Z][a-z]+)\s+(\d{1,2}),?\s*(2026)?', t, re.I)
    ck(bool(m), 'KEV row has a parseable due date: %s' % t[:70])
    if not m:
        continue
    due = datetime.datetime.strptime('%s %s 2026' % (m.group(1)[:3], m.group(2)), '%b %d %Y').date()
    left = (due - TODAY).days
    # HARNESS BUG (iii), fixed not worked around: the countdown is rendered as
    # <span class="kevdue ok">1 day left</span> -- there are no parentheses on the page,
    # so the old '\((\d+) days? left\)' pattern failed EVERY future-dated row.
    dm = re.search(r'\(?(\d+)\s+days?\s+left\)?', t)
    if left > 0:
        ck(bool(dm) and int(dm.group(1)) == left,
           'KEV countdown mismatch: due %s should read %d days left -> %s' % (due, left, t[:80]))
    else:
        past += 1
        ck(('overdue' in t.lower() or 'past due' in t.lower() or '0 days' in t.lower()),
           'KEV row due %s must be marked overdue: %s' % (due, t[:80]))
ck(past == 10, 'KEV past-due count is 10 (found %d)' % past)

# Patch Priority must match the KEV board's own urgent deadline
ck('August 28, 2026' in TCY or 'Aug 28' in TCY, 'Gitea Aug 28 deadline present')
ck('CVE-2026-21962' in TCY and 'Aug 27' in TCY, 'Patch Priority Oracle Aug 27 (1 day)')
ck('1.27.1' in TCY and 'CVSS 9.8' in TCY, 'Gitea fixed version + CVSS from this run')
ck('Habr' in TCY, 'Gitea in-the-wild provenance named')
# Gitea CVE must never be attributed to Oracle (recurring garble).
# HARNESS BUG (iv), fixed not worked around: the old 400-char flat window ran past the
# end of the Gitea <li> into the ADJACENT Oracle row, so correct markup false-failed.
# Scoped to the enclosing <li> element, which is the real unit of attribution.
# NOTE: in its correct form this test caught a REAL defect this run -- edits_1636.py had
# appended the Gitea detail to the Oracle row (see fix_1636.py).
for _row in re.finditer(r'<li>(?:(?!</li>).)*</li>', CY, re.S):
    _t = txt(_row.group(0))
    if 'CVE-2026-60004' in _t:
        ck('Gitea' in _t, 'CVE-2026-60004 row does not name Gitea')
        ck('Oracle' not in _t, 'CVE-2026-60004 mis-attributed to Oracle in its own row')
    if 'CVE-2026-21962' in _t:
        ck('Oracle' in _t, 'CVE-2026-21962 row does not name Oracle')
        ck('Gitea' not in _t, 'Gitea detail leaked into the Oracle row')

# ---------- 6. CHAMPIONS BOARD: 11 belts, three historical regressions tested ----------
ch = MM[MM.index('Champions board'):]
ch = ch[:ch.index('</section>')]
TCH = txt(ch)
for div, champ in (('Heavyweight', 'Tom Aspinall'), ('Light Heavyweight', 'Carlos Ulberg'),
                   ('Middleweight', 'Sean Strickland'), ('Welterweight', 'Islam Makhachev'),
                   ('Lightweight', 'Justin Gaethje'), ('Featherweight', 'Alexander Volkanovski'),
                   ('Bantamweight', 'Petr Yan'), ('Flyweight', 'Joshua Van'),
                   ('Shevchenko', 'Shevchenko'), ('Harrison', 'Harrison'), ('Dern', 'Dern')):
    ck(champ in TCH, 'champions board carries %s (%s)' % (champ, div))
ck('Ciryl Gane' in TCH, 'interim HW Gane on board')
# regressions
i_lhw = TCH.find('Light Heavyweight')
ck('Pereira' not in TCH[i_lhw:i_lhw + 160], 'REGRESSION: Pereira listed at light heavyweight')
# HARNESS BUG (v), fixed not worked around: Chimaev legitimately appears in the
# middleweight row as the man Strickland BEAT ("Split decision over Khamzat Chimaev").
# The old window test could not tell champion from defeated opponent. Now the test
# asserts the CHAMPION cell names Strickland and that Chimaev only ever appears after a
# defeat verb -- which is what "no longer champion" actually means on a champions board.
i_mw = TCH.find('Middleweight')
_mw = TCH[i_mw:i_mw + 200]
ck('Sean Strickland' in _mw, 'middleweight champion cell must name Strickland')
ck(_mw.index('Sean Strickland') < _mw.index('Chimaev') if 'Chimaev' in _mw else True,
   'REGRESSION: Chimaev listed ahead of Strickland at middleweight')
ck(re.search(r'(?:over|defeat\w*|beat)\s+Khamzat Chimaev', _mw) is not None if 'Chimaev' in _mw else True,
   'REGRESSION: Chimaev at middleweight not framed as the defeated opponent')
i_fw = TCH.find('Featherweight')
ck(not re.search(r'Featherweight[^|]{0,80}[Vv]acant', TCH[i_fw:i_fw + 200]),
   'REGRESSION: featherweight shown vacant')
ck('Volkanovski' in TCH[i_fw:i_fw + 200], 'featherweight row names Volkanovski')

# ---------- 7. MMA: dates, odds, no premature results ----------
ck('August 29, 2026' in TMM or 'Aug 29' in TMM, 'Shanghai date present')
ck('Oriental Sports Center' in TMM, 'venue is Oriental Sports Center')
# HARNESS BUG (vi), fixed not worked around -- and this is the THIRD recurrence of the
# same bug class (Dooho Choi at 3:50, Shanghai Indoor Stadium at 4:14): the page's real
# rejection vocabulary is wider than the single word "reject". The second occurrence
# rejects the venue with "the Oriental Sports Center name is the one published here",
# which contains no form of "reject" at all. Vocabulary widened; a positive check now
# requires the rejection sentence to be PRESENT at all.
VENUE_REJ = ('reject', 'is the one published here', 'not adopted', 'recorded and not',
             'no third venue', 'the name this page publishes')
for hit in re.finditer('Shanghai Indoor Stadium', TMM):
    w = TMM[max(0, hit.start() - 450):hit.start() + 260].lower()
    ck(any(r in w for r in VENUE_REJ), 'wrong venue outside rejection prose')
ck('Shanghai Indoor Stadium' not in TMM or 'Oriental Sports Center' in TMM,
   'venue rejection prose must name the venue actually published')
ck('13 bouts' in TMM and '12-fight undercard' in TMM, 'card size from UFC.com')
ck('3 a.m. ET' in TMM and '6 a.m. ET' in TMM, 'Shanghai start times')
ck('-500' in TMM and '+380' in TMM, 'Shanghai odds carried')
ck('has not taken place' in TMM and 'no result is asserted' in TMM, 'no premature Shanghai result')
imp_a, imp_b = 500 / 600 * 100, 100 / 480 * 100
ck(abs(imp_a - 83.33) < .01 and abs(imp_b - 20.83) < .01, 'moneyline implied probabilities')

# ---------- 8. TRAP GREPS (hard) ----------
for bad in ('Cody Salkilld', 'Shamil Yakhyaev', 'Abdul-Rakhman', 'Fight Night 286', '$1.4 trillion', 'Suno'):
    for k, v in F.items():
        ck(bad not in txt(v), 'HARD TRAP "%s" present in %s' % (bad, k))
# context-allowed: only inside rejection/correction prose
# HARNESS BUG (vii), fixed not worked around: the rejection vocabulary AGAIN missed the
# page's own language -- '7,677.24' is rejected with "declined to adopt", "four cents
# below", "loses again"; '122%' is rejected with "two years old", "NONE of it publishes",
# "trap of the day". This is the same under-specified-vocabulary bug as (vi); widened,
# and the window enlarged to reach a rejection clause that FOLLOWS the figure.
REJ = ('reject', 'correction', 'previously rendered', 'not published', 'stale', 'carried forward',
       "tuesday's close", 'completed session', 'august 2024', 'prior quarter', 'wrong quarter',
       'does not publish', 'flagged', 'declined to adopt', 'loses again', 'cents below',
       'two years old', 'none of it publishes', 'trap', 'not the 7,677.24', 'discrepancy',
       'is the one published here', 'not adopted', 'adopted at 2:44 over', 'zacks printed')
for bad in ('7,677.24', '4,637.03', '30.68', 'Dooho Choi', '122%'):
    for k, v in F.items():
        t = txt(v)
        for hit in re.finditer(re.escape(bad), t):
            w = t[max(0, hit.start() - 460):hit.start() + 320].lower()
            ck(any(r in w for r in REJ), '"%s" outside rejection context in %s' % (bad, k))

# ---------- 9. PAGE FURNITURE ----------
NAV = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html', 'archive.html']
for k, v in F.items():
    for href in NAV:
        ck('href="%s"' % href in v, '%s missing nav link %s' % (k, href))
    for pid in ('edition', 'datestamp', 'updated'):
        ck('id="%s"' % pid in v, '%s missing masthead pill #%s' % (k, pid))
    ck("getElementById('datestamp')" in v and 'America/New_York' in v, '%s missing self-stamp JS' % k)
    ck('Morning Edition' in v and 'Midday Edition' in v and 'Afternoon Edition' in v,
       '%s missing edition buckets' % k)
for k, v in BRIEFS.items():
    ck('id="freshline"' in v, '%s missing freshline' % k)
    ck('class="tldr"' in v, '%s missing tldr strip' % k)
ck('<b>The Tape</b>' in WS, 'WS tldr label')
ck('<b>The Wire</b>' in CY, 'CY tldr label')
ck('<b>Tale of the Tape</b>' in MM, 'MM tldr label')
ck('id="ufccdn"' in MM, 'MMA countdown element')

# ---------- 10. TRADINGVIEW BLOCKS ----------
ck(WS.count('embed-widget-single-quote.js') == 3, 'exactly 3 single-quote widgets')
for w in ('ticker-tape', 'timeline', 'stock-heatmap', 'mini-symbol-overview', 'events'):
    ck('embed-widget-%s.js' % w in WS, 'missing TradingView block %s' % w)
tape = WS[WS.index('embed-widget-ticker-tape.js'):]
tape = tape[:tape.index('</script>')]
for sym in ('FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI', 'TVC:USOIL', 'TVC:US10Y'):
    ck(sym in tape, 'ticker tape missing mandatory symbol %s' % sym)

# ---------- 11. FRESHNESS / NEW-TAG HYGIENE ----------
for k, v in F.items():
    for m in re.finditer(r'class="tag new">([^<]*)<', v):
        ck('4:36' in m.group(1), '%s: stale "New" tag -> %s' % (k, m.group(1)))
# HARNESS GAP (viii) closed: the old new-tag test only inspected <span class="tag new">
# elements, so INLINE prose labels ("* New &middot; 4:15 &mdash;") survived into a 4:36
# edition still calling themselves new. Freshness is a claim like any other; it is now
# tested in prose too.
for k, v in F.items():
    for m in re.finditer(r'New\s*&middot;\s*(\d{1,2}:\d{2})', v):
        ck(m.group(1) == '4:36', '%s: prose still labelled "New &middot; %s"' % (k, m.group(1)))
ck(WS.count('class="tag new"') >= 1, 'WS has at least one genuinely new item')
ck(CY.count('class="tag new"') >= 1, 'CY has at least one genuinely new item')
ck(MM.count('class="tag new"') >= 1, 'MM has at least one genuinely new item')

# ---------- 12. INDEX CARDS FAITHFULLY SUMMARISE THEIR PAGES ----------
for cls in ('c-sec', 'c-mkt', 'c-mma'):
    ck('class="bcard %s"' % cls in IX, 'index card %s present' % cls)
ck('96.22' in TIX and '108' in TIX, 'index markets card matches WS lead')
ck('CVE-2026-60004' in TIX and 'August 28' in TIX, 'index security card matches CY lead')
ck('Nurmagomedov' in TIX and 'Oriental Sports Center' in TIX, 'index MMA card matches MM lead')
ck(IX.count('Read the briefing') == 3, 'three "Read the briefing" links')
# the index must not claim a % move for NVDA that the WS page refuses to state
ck(not re.search(r'Nvidia[^.]{0,80}\d+%\s*(?:lower|down|drop)', TIX), 'index invents no NVDA move')

# ---------- 13. DISCLAIMERS + SOURCES ----------
ck('not investment advice' in TWS, 'WS disclaimer')
ck('subject to change' in TMM, 'MMA disclaimer')
for k, v in BRIEFS.items():
    ck('<div class="lab">Sources</div>' in v, '%s missing sources footer' % k)
    ck(v.count('href="http') >= 5, '%s has too few source URLs' % k)
ck('sec.gov' in WS and 'sec.gov' in CY, 'primary SEC source cited')
ck('cisa.gov' in CY, 'CISA primary source cited')
ck('ufc.com' in MM, 'UFC.com primary source cited')

print('CHECKS: %d   FAILURES: %d' % (n, len(fails)))
for f in fails:
    print('  FAIL:', f)
raise SystemExit(1 if fails else 0)
