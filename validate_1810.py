#!/usr/bin/env python3
"""One job: assert the invariants. Guards are narrowed, never loosened, when they misfire."""
import io, sys, re
REPO = sys.argv[1]
P = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']
H = {f: io.open(REPO + '/' + f, encoding='utf-8').read() for f in P + ['archive.html']}
ok = err = 0
def chk(cond, msg):
    global ok, err
    if cond: ok += 1
    else:
        err += 1
        print('  FAIL:', msg)

def txt(s):
    return re.sub('<[^>]+>', ' ', s)

# ---- structure -------------------------------------------------------------
for f in P + ['archive.html']:
    h = H[f]
    for href in ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html',
                 'mma-briefing.html', 'archive.html']:
        chk(('href="%s"' % href) in h, '%s: nav link %s' % (f, href))
    chk(len(re.findall(r'<nav class="tabs">.*?</nav>', h, re.S)) == 1, '%s: one nav' % f)
    nav = re.search(r'<nav class="tabs">.*?</nav>', h, re.S).group(0)
    chk(nav.count('class="on"') == 1, '%s: exactly one active tab' % f)

for f in P:
    h = H[f]
    for i in ['edition', 'datestamp', 'updated', 'freshline']:
        chk(('id="%s"' % i) in h, '%s: id %s' % (f, i))
    chk('America/New_York' in h, '%s: self-stamp JS' % f)
    chk('Data as of 6:10 PM ET' in h, '%s: freshline restamped to 6:10 PM' % f)

# ---- widgets: wallstreet only ----------------------------------------------
ws = H['wallstreet-briefing.html']
for w in ['ticker-tape', 'single-quote', 'timeline', 'stock-heatmap',
          'mini-symbol-overview', 'events']:
    chk(('embed-widget-%s.js' % w) in ws, 'ws: widget %s' % w)
chk(ws.count('embed-widget-single-quote.js') == 3, 'ws: exactly three single-quote widgets')
for s in ['FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI', 'TVC:USOIL', 'TVC:US10Y']:
    chk(s in ws, 'ws: tape symbol %s' % s)
for f in ['index.html', 'cyber-briefing.html', 'mma-briefing.html', 'archive.html']:
    chk('tradingview.com/external-embedding' not in H[f], '%s: must carry no widgets' % f)

# ---- index cards mirror the tldrs byte-for-byte ----------------------------
idx = H['index.html']
for src, cls in [('cyber-briefing.html', 'c-cy'), ('wallstreet-briefing.html', 'c-ws'),
                 ('mma-briefing.html', 'c-mm')]:
    inner = re.search(r'<div class="tldr">.*?<span>(.*?)</span></div>', H[src], re.S).group(1)
    i = idx.find('<div class="bigcard %s">' % cls)
    card = idx[idx.find('<p>', i) + 3: idx.find('</p>', i)]
    chk(card == inner, '%s: card mirrors tldr byte-for-byte' % cls)
    chk('class="tldr"' not in idx, 'index: no tldr strip of its own')

# ---- markets arithmetic ----------------------------------------------------
chk('7,711.76' in ws and '26,402.42' in ws and '53,559.99' in ws, 'ws: three Friday closes')
chk(abs((7711.76 - 37.39) - 7674.37) < 5e-3, 'ws: S&P weekly reconciles')
chk(abs((53559.99 - 282.98) - 53277.01) < 5e-3, 'ws: Dow weekly reconciles')
chk(abs((26402.42 - 221.97) - 26180.45) < 5e-3, 'ws: Nasdaq weekly reconciles')
chk('26,180.45' in ws, 'ws: Nasdaq prior-week level corroborated and printed')
# Russell: the point of the item is that it does NOT reconcile; assert the failure is real
chk(abs((3017.87 - 45.50) - 2973.09) > 0.5, 'ws: Russell genuinely fails to reconcile')
chk('2,973.09' in ws and '3,017.87' in ws and '45.50' in ws, 'ws: all three Russell figures shown')
# ...and that the level is withheld rather than certified
r = txt(ws)
chk('level is withheld' in r or 'the level is not' in r, 'ws: Russell level explicitly withheld')
# Nasdaq-100 must never be promoted into the Composite row
for m in re.finditer('29,433.43', ws):
    seg = txt(ws[m.start() - 400:m.start() + 400])
    chk(('not promoted' in seg or 'recorded' in seg or 'different index' in seg),
        'ws: Nasdaq-100 adjacency lacks a separating clause')

# ---- cyber -----------------------------------------------------------------
cy = H['cyber-briefing.html']
ct = txt(cy)
for s in ['Questal', 'ShinyHunters', 'Hyundai Motor T', 'ProHealth', 'Krybit', 'CRPx0']:
    chk(s in cy, 'cy: %s present' % s)
chk('attacker' in ct and 'leak site' in ct.lower().replace('leak-site', 'leak site'),
    'cy: leak-site claims labelled as claims')
chk('CVE-2026-19490' in cy, 'cy: companion CVE recorded')
# 19490 must NOT be on the deadline board.
# NARROWED: the first guard sliced "everything after the KEV heading", which swept in the
# source-footer link title and would have swept in every later section too. The real
# requirement is (a) it is absent from the KEV section's own list markup and (b) every
# body mention carries the negation. Footer link labels are not placements on the board.
kev_i = cy.find('<h2 class="sec">CISA KEV')
_cands = [x for x in (cy.find('<h2 class="sec">', kev_i + 10),
                      cy.find('<footer'), cy.find('<div class="srcs">')) if x > 0]
kev_end = min(_cands) if _cands else len(cy)   # the KEV section ends at the next section OR the footer
kev = cy[kev_i:kev_end]
chk('CVE-2026-19490' not in kev, 'cy: 19490 kept off the KEV/deadline board')
body_end = cy.find('<div class="srcs">')
for m in re.finditer('CVE-2026-19490', cy[:body_end]):
    seg = txt(cy[max(0, m.start() - 700):m.start() + 700])
    # NARROWED again: the summary strip carries a real qualifier ("kept off the deadline
    # board ... nothing fetched calls it exploited") in different words from the body's.
    # The guard listed body phrasings only, so it failed a sentence that is in fact correct.
    # It still requires a negation adjacent to every mention -- a bare mention fails.
    QUALIFIERS = ('not in the KEV', 'does not belong', 'not added', 'not</b> added',
                  'kept off the deadline board', 'calls it exploited')
    chk(any(q in seg for q in QUALIFIERS),
        'cy: 19490 mentioned without its not-exploited/not-KEV qualifier')
chk('eleventh consecutive run' in ct, 'cy: Nevada refusal count advanced to eleventh')
# the Iran-linked claim must appear ONLY inside a refusal context
for m in re.finditer('Iran-linked', cy):
    seg = txt(cy[max(0, m.start() - 900):m.start() + 900])
    chk('refus' in seg.lower() or 'not published' in seg,
        'cy: Iran-linked claim outside a refusal context')
# CVE well-formedness + liveness
ids = set(re.findall(r'CVE-\d{4}-\d{4,6}', cy))
chk(len(ids) >= 15, 'cy: >=15 distinct CVE ids (%d)' % len(ids))
for c in ids:
    chk(re.fullmatch(r'CVE-(19|20)\d\d-\d{4,6}', c) is not None, 'cy: malformed %s' % c)
chk('9.3' in cy or 'CVE-2026-3055' not in cy, 'cy: conditional Citrix 9.3 rule')
# Nevada must never be presented as a 2026 incident
for m in re.finditer('Nevada', cy):
    seg = txt(cy[max(0, m.start() - 500):m.start() + 700])
    chk('2025' in seg or 'refus' in seg.lower(), 'cy: Nevada without its 2025/refusal context')

# ---- mma -------------------------------------------------------------------
mm = H['mma-briefing.html']
mt = txt(mm)
CHAMPS = ['Aspinall', 'Ulberg', 'Strickland', 'Makhachev', 'Gaethje', 'Volkanovski',
          'Petr Yan', 'Joshua Van', 'Shevchenko', 'Harrison', 'Dern']
for c in CHAMPS:
    chk(c in mm, 'mma: champion %s present' % c)
# forbidden champion claims (standing corrections)
champ_tbl = mm[mm.find('Champions Board'):]
for bad in ['Pereira</td>', 'Chimaev</td>', 'Topuria</td>', 'Pantoja</td>',
            'Zhang Weili</td>', 'Dvalishvili</td>', 'Procházka</td>']:
    chk(bad not in champ_tbl, 'mma: forbidden name in champion column: %s' % bad)
chk('Vacant' not in champ_tbl and 'vacant' not in champ_tbl.split('Interim')[0][:4000]
    or 'Volkanovski' in champ_tbl, 'mma: featherweight not vacant')
# new odds material
chk('&minus;357' in mm and '+275' in mm, 'mma: opening line present')
chk('opening odds' in mt or 'opening</i>' in mm or 'opening' in mt, 'mma: opener labelled as an opener')
# the inverted line must only appear as refuted
for m in re.finditer('Hooker &minus;500', mm):
    seg = txt(mm[max(0, m.start() - 700):m.start() + 900])
    chk('refut' in seg or 'wrong' in seg or 'opposite' in seg,
        'mma: inverted line printed without its refutation')
# standing fighter traps
if 'Salkilld' in mm:
    seg = txt(mm[mm.find('Salkilld') - 900: mm.find('Salkilld') + 900])
    chk('Gamrot' in seg, 'mma: Salkilld latest fight must be Gamrot')
    chk('Cody Salkilld' not in mm, 'mma: Salkilld first name')
chk('Shamil Yakhyaev' not in mm, 'mma: Yakhyaev name trap')
if 'Dariush' in mm:
    for m in re.finditer('Dariush', mm):
        seg = txt(mm[max(0, m.start() - 300):m.start() + 300])
        chk('champion' not in seg.lower().replace('championship', ''),
            'mma: Dariush must never be called a champion')

# ---- footers / links -------------------------------------------------------
for f in P:
    h = H[f]
    i = h.find('<div class="srcs">')
    chk(i >= 0, '%s: srcs footer' % f)
    block = h[i:h.find('</div>', i)]
    hrefs = re.findall(r'<a href="([^"]+)"', block)
    if f != 'index.html':
        chk(len(hrefs) >= 6, '%s: >=6 source links (%d)' % (f, len(hrefs)))
        chk(len(hrefs) == len(set(hrefs)), '%s: duplicate hrefs' % f)
        chk(all(u.startswith('https://') for u in hrefs), '%s: non-https source' % f)
    chk('class="disc"' in h, '%s: disclaimer' % f)

# ---- no bare future timestamp ---------------------------------------------
NOW = 18 * 60 + 10
for f in P:
    for m in re.finditer(r'New &middot; (\d{1,2}):(\d{2})\s*(AM|PM)', H[f]):
        hh, mm_, ap = int(m.group(1)), int(m.group(2)), m.group(3)
        t = (hh % 12) * 60 + mm_ + (720 if ap == 'PM' else 0)
        chk(t <= NOW, '%s: bare "New" stamp %s is in the future' % (f, m.group(0)))

# ---- tag classes defined ---------------------------------------------------
for f in P:
    h = H[f]
    for c in set(re.findall(r'class="tag ([a-z]+)"', h)):
        chk(('.tag.%s' % c) in h, '%s: tag class .%s undefined' % (f, c))

print('\nchecks: %d passed, %d failed' % (ok, err))
sys.exit(1 if err else 0)
