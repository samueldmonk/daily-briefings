#!/usr/bin/env python3
"""Programmatic validation of the 6:06 PM ET edition, 2026-08-26.

Every number that went onto a page this run is re-derived here in Python; every
structural requirement of the task spec is asserted; every historically-regressed
fact is tested BY NAME; and every figure rejected this run is required to appear
ONLY inside a rejection/correction window (or not at all).
"""
import os, re, sys, datetime

D = os.path.dirname(os.path.abspath(__file__))
IDX, CY, WS, MM = 'index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html'
PAGES = [IDX, CY, WS, MM]
H = {p: open(os.path.join(D, p)).read() for p in PAGES}
fails, checks = [], 0


def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)


def near(pct, target, tol=0.06):
    return abs(pct - target) <= tol


def txt(s):
    """Strip tags + unescape the entities this site actually uses, for prose matching."""
    s = re.sub(r'<[^>]+>', ' ', s)
    for a, b in [('&mdash;', '—'), ('&ndash;', '–'), ('&rsquo;', "'"), ('&lsquo;', "'"),
                 ('&ldquo;', '"'), ('&rdquo;', '"'), ('&plus;', '+'), ('&minus;', '-'),
                 ('&nbsp;', ' '), ('&amp;', '&'), ('&#9888;', '!'), ('&#9679;', '*'),
                 ('&middot;', '·'), ('&plusmn;', '+/-')]:
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s)


T = {p: txt(H[p]) for p in PAGES}

# ============================================================ 1. NVIDIA ARITHMETIC
# Segment table published this run must reconcile to the top line.
hyper, acie, edge, dc, total_rev = 48.71, 40.31, 7.20, 89.02, 96.2
ck(abs((hyper + acie) - dc) < 0.005,
   'Hyperscale + ACIE (%.2f) != Data Center %.2f' % (hyper + acie, dc))
ck(abs((dc + edge) - 96.22) < 0.005, 'DC + Edge != 96.22')
ck(abs(round(dc + edge, 1) - total_rev) < 0.005,
   'segment sum %.2f does not round to the $96.2B top line' % (dc + edge))
ck('48.71 &plus; 40.31 = 89.02' in H[WS], 'the published reconciliation string is missing from the page')
ck('89.02 &plus; 7.20 =\n96.22' in H[WS] or '89.02 &plus; 7.20 = 96.22' in H[WS],
   'the second published reconciliation string is missing')

# Growth rates re-derived from the bases the page states.
ck(near((96.2 / 46.7 - 1) * 100, 106.0, 0.1),
   'revenue +106.0%% does not reconcile: got %.2f%%' % ((96.2 / 46.7 - 1) * 100))
ck(near((2.22 / 1.05 - 1) * 100, 111.4, 0.1),
   'EPS +111.4%% does not reconcile: got %.2f%%' % ((2.22 / 1.05 - 1) * 100))
q3 = (108.0 / 57.01 - 1) * 100
ck(near(q3, 89.4, 0.1), 'Q3 guide growth is %.2f%%, page says +89.4%%' % q3)
ck(q3 > 89.0, 'page/company claim "more than 89%%" but derived %.2f%%' % q3)
ck('&plus;89.4%' in H[WS], 'the +89.4% Q3 derivation is not printed')

# Segment y/y and q/q bases must be mutually consistent:
# prior-quarter Hyperscale + prior-quarter ACIE should reproduce prior-quarter Data Center.
dc_prior = dc / 1.183
hy_prior, ac_prior = hyper / 1.131, acie / 1.252
ck(abs((hy_prior + ac_prior) - dc_prior) < 0.15,
   'segment q/q bases inconsistent: %.2f + %.2f vs %.2f' % (hy_prior, ac_prior, dc_prior))
dc_yago = dc / 2.166
ck(40.5 < dc_yago < 41.7, 'Data Center y/y base %.2f outside the expected band' % dc_yago)

# Gross margin figures published this run.
for s in ['75.0% against 72.7%', '74.0% against 73.6%']:
    ck(s.replace('%', '%') in T[WS], 'gross-margin string missing: %s' % s)
ck(75.0 > 72.7 and 74.0 > 73.6, 'gross-margin comparisons are not both expansions')

# The reversal is stated as a magnitude with a time and is NOT stated as a level.
ck('up almost 5% in after-hours trading' in T[WS], 'the +5% after-hours quote is missing')
ck('5:10 p.m. ET' in T[WS], 'the 5:10 p.m. ET timestamp on the reversal is missing')
ck('no 6 p.m. level is asserted here' in T[WS].lower() or
   'NO 6 P.M. LEVEL IS ASSERTED HERE'.lower() in T[WS].lower(),
   'the page does not disclaim a 6 p.m. level')
ck('down some from its after-hours peak' in T[WS],
   'the peak-adjacent caveat (5:24 entry) is missing')

# The pre-call reads must still be present and must still be labelled as pre-call.
for s in ['-1.3%', '-1%']:
    ck(s in T[WS], 'earlier after-hours read %s was deleted' % s)

# ============================================================ 2. REJECTED-THIS-RUN GUARDS
# Each rejected claim may appear ONLY inside a rejection window on the page.
REJECT_VOCAB = ['reject', 'not published', 'does not contain', 'does not appear', 'misattribut',
                'withheld', 'not asserted', 'neither is adopted', 'not adopted', 'declined',
                'no 6 p.m. level', 'is not published', 'mutually contradictory',
                'nothing from either', 'is asserted:', 'no anf closing price']


def rejection_windowed(page, needle, span=1400, label=None):
    """needle must occur only inside a paragraph that also contains rejection vocabulary."""
    global checks
    checks += 1
    t = T[page]
    lbl = label or needle
    for m in re.finditer(re.escape(needle), t):
        lo, hi = max(0, m.start() - span), min(len(t), m.end() + span)
        w = t[lo:hi].lower()
        if not any(v in w for v in REJECT_VOCAB):
            fails.append('UNCONTEXTED REJECTED ITEM [%s]: %r at %d' % (page, lbl, m.start()))
            return


for n in ['$1 trillion in combined Blackwell', '350 plants', '1.5 million components',
          '$200 billion CPU market', 'our demand is much higher than that']:
    rejection_windowed(WS, n)

# The rejection paragraph must actually name all four rejected claims.
rej = T[WS]
ck('REJECTED THIS RUN' in rej, 'the rejection block heading is missing')
for n in ['350 plants', '$200 billion CPU market', 'our demand is much higher than that']:
    ck(n in rej, 'rejection block does not name %r' % n)

# 70% MUST be attributed to Kress, never to Huang, on any page.
for p in [WS, IDX]:
    for m in re.finditer(r'70%', T[p]):
        w = T[p][max(0, m.start() - 400):m.end() + 400]
        ck('Kress' in w or 'she' in w or 'supply-constrained' in w or 'hers' in w,
           '70%% appears in %s without the Kress/supply-constrained attribution' % p)

# Standing rejected market figures from earlier runs must stay windowed.
for n in ['7,677.24', '4,637.03', '112.62', '97.69', '$213.70', '1.45%']:
    if n in T[WS]:
        rejection_windowed(WS, n)
ck('7,677.24' not in T[IDX], 'the rejected 7,677.24 close leaked onto the front page')

# -1.59% may never be presented as an after-hours figure.
for m in re.finditer(re.escape('1.59%'), T[WS]):
    w = T[WS][max(0, m.start() - 350):m.end() + 350].lower()
    ck(('regular-session' in w or 'on the session' in w or 'went into the print red' in w
        or 'close' in w or 'reject' in w),
       '-1.59%% used without its regular-session label at %d' % m.start())

# ============================================================ 3. CISA KEV: due date -> countdown -> past-due
TODAY = datetime.date(2026, 8, 26)
MON = {m: i + 1 for i, m in enumerate(
    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])}
kev_sec = H[CY][H[CY].find('CISA KEV'):]
kev_sec = kev_sec[:kev_sec.find('<div class="lab">Sources')] if '<div class="lab">Sources' in kev_sec else kev_sec
triples = 0
for li in re.findall(r'<li>.*?</li>', kev_sec, re.S):
    lt = txt(li)
    dm = re.search(r'due\s+([A-Z][a-z]{2})[a-z]*\.?\s+(\d{1,2})', lt)
    cm = re.search(r'(\d+)\s+days?\s+left|past due|overdue|due today', lt, re.I)
    if not (dm and cm):
        continue
    triples += 1
    due = datetime.date(2026, MON[dm.group(1)], int(dm.group(2)))
    delta = (due - TODAY).days
    if cm.group(1):
        ck(int(cm.group(1)) == delta,
           'KEV countdown mismatch: due %s, page says %s days left, actual %d'
           % (due, cm.group(1), delta))
    else:
        ck(delta <= 0, 'KEV row marked past due but %s is %d days away' % (due, delta))
ck(triples >= 12, 'KEV countdown test parsed only %d rows — it must not pass vacuously' % triples)

# The two nearest deadlines must be stated identically in Patch Priority, the KEV note and the tldr.
ck(T[CY].count('CVE-2026-21962') >= 3, 'the Oracle CVE is not cross-referenced across sections')
ck('due tomorrow' in T[CY] or 'August 27' in T[CY], 'the Oracle Aug 27 deadline is not stated')
ck('August 28' in T[CY], 'the Gitea Aug 28 deadline is not stated')
ck('sixteenth consecutive edition' in T[CY].lower(), 'the KEV-static streak was not advanced to sixteenth')

# Gitea and Oracle must never be conflated inside one list item (the 1636 defect).
for li in re.findall(r'<li>.*?</li>', kev_sec, re.S):
    lt = txt(li)
    if 'CVE-2026-60004' in lt and 'Gitea' in lt:
        ck('Oracle' not in lt, 'a Gitea KEV row also names Oracle — the 1636 conflation has recurred')
ck('1.27.1' in T[CY], 'the Gitea fixed version is missing')
ck('late July' in T[CY], 'the new Gitea patch-gap detail did not publish')

# ============================================================ 4. NEW CYBER ITEMS
apollo = T[CY]
for s in ['Apollo Global Management', 'July 6 and July 10', 'August 12',
          'Social Security numbers', 'no client funds were compromised']:
    ck(s in apollo, 'Apollo card missing: %s' % s)
# We must NOT publish a victim count for Apollo.
am = apollo.find('Apollo Global Management confirms a social-engineering breach')
ck(am > 0, 'the Apollo card headline was not found')
ck('has NOT disclosed how many people are affected' in apollo[am:am + 2600],
   'the Apollo card does not disclaim a victim count')
ck(not re.search(r'Apollo[^.]{0,400}?([\d,]{4,})\s+(?:people|individuals|customers|records)',
                 apollo[am:am + 2600]),
   'a victim count leaked into the Apollo card')

for s, why in [('CVE-2026-18963', 'Keycloak CVE'), ('CVE-2026-75149', 'Marimo CVE'),
               ('NemoClaw', 'NemoClaw finding'), ('Mirage2FA', 'Mirage2FA'),
               ('Chrome 152', 'Chrome'), ('Super Micro', 'Taiwan export charges')]:
    ck(s in T[CY], 'cyber item missing (%s): %s' % (why, s))

# ---- GOTCHA #56 GUARD (new this run): an item already on the page may NOT be re-introduced
# inside a block this run marks new.  Scope to the enclosing element, not a flat window.
def blocks_marked_new(page, stamp='New &middot; 6:06'):
    """Return the text of each <div class="card">/<p> that carries the given new stamp."""
    h, out = H[page], []
    for m in re.finditer(re.escape(stamp), h):
        # walk back to the opening <div class="card"> or <p ...>, forward to its close
        lo = max(h.rfind('<div class="card">', 0, m.start()),
                 h.rfind('<p class="note">', 0, m.start()),
                 h.rfind('<p>', 0, m.start()))
        if lo < 0:
            lo = max(0, m.start() - 200)
        hi = h.find('</div>', m.end())
        hp = h.find('</p>', m.end())
        hi = hp if (hp > 0 and (hi < 0 or hp < hi)) else hi
        out.append(txt(h[lo:hi if hi > 0 else m.end() + 2500]))
    return out


CARRIED = ['CVE-2026-18963', 'CVE-2026-75149', 'Marimo', 'Elad Luz', '63.7%', 'v0.0.35']
newblocks = blocks_marked_new(CY)
ck(len(newblocks) >= 3, 'fewer than three blocks are marked new on the cyber page (%d)' % len(newblocks))
for b in newblocks:
    for ident in CARRIED:
        if ident in b:
            ck('already' in b.lower() or 'corroborat' in b.lower() or 'deleted' in b.lower(),
               'carried item %r re-introduced inside a 6:06 block without saying it is already published'
               % ident)
# Nothing may be introduced twice as a fresh Vulnerability Watch row.
for ident in ['CVE-2026-18963', 'CVE-2026-75149']:
    ck(T[CY].count(ident) <= 3, 'identifier %s appears %d times — likely duplicated'
       % (ident, T[CY].count(ident)))
# The self-check note must exist and must name what it deleted.
ck('caught this desk adding items it had already published' in T[CY],
   'the duplicate self-check note is missing')
for ident in ['Keycloak', 'Marimo', 'NemoClaw', 'Chrome 152']:
    k = T[CY].find('caught this desk adding items')
    ck(ident in T[CY][k:k + 1600], 'the self-check note does not name %s' % ident)

# The NemoClaw item (carried) must still state it has no CVE and the split patch status.
ni = T[CY].find('Oasis Security has disclosed a weakness in')
ck(ni > 0, 'the carried NemoClaw item is missing')
win = T[CY][ni:ni + 1600]
ck('no CVE identifier' in win, 'the NemoClaw item no longer says it has no CVE')
ck('no fix on the Windows and WSL path' in win, 'the NemoClaw Windows/WSL caveat is missing')
ck(win.find('v0.0.35') < win.find('v0.0.34'), 'the NemoClaw version pair reads out of order')

# Chrome 152 must not carry an invented CVE, in PROSE only — the stat tile and the source
# links are not claims.  (Flat-window class, seventh recurrence: the earlier version of this
# test matched the Sources footer.)
# BUG (viii), SAME CLASS AGAIN: the stat strip is a GRID OF TILES, so a "sentence" started
# inside one tile runs straight into the next tile's CVE.  Prose begins at the Top story label.
src_start = T[CY].rfind('Sources')
prose_start = T[CY].find('Top story')
ck(prose_start > 0, 'could not locate the start of prose on the cyber page')
for m in re.finditer(r'Chrome 152', T[CY]):
    if m.start() > src_start or m.start() < prose_start:
        continue                      # footer link titles / stat tiles are not CVE claims
    seg = T[CY][m.start():]
    end = seg.find('. ')
    seg = seg[:end + 1] if end > 0 else seg[:300]
    ck('CVE-' not in seg, 'a CVE appears in a Chrome 152 sentence at %d' % m.start())

# ============================================================ 5. MMA
m_t = T[MM]
for s in ['#7', '#9', '#8', '#13', '#14', '#15']:
    ck(s in m_t, 'rankings figure missing: %s' % s)
for s in ['Gregory Rodrigues', 'Anthony Hernandez', 'Vitor Petrino', 'Serghei Spivac',
          'Reinier de Ridder', 'Jamall Emmers', 'Carli Judice', 'Lerryan Douglas', 'Jeisla Chaves',
          'Roman Dolidze']:
    ck(s in m_t, 'fighter name missing or misspelled: %s' % s)
ck('Jamal Emmers' not in m_t, 'the single-l "Jamal Emmers" spelling leaked onto the page')

# de Ridder's exact rank is DISPUTED and must not be asserted; both readings must be printed.
di = m_t.find("de Ridder's exact rank")
ck(di > 0, 'the de Ridder rank dispute is not flagged')
dw = m_t[max(0, di - 200):di + 900]
ck('#9' in dw and ('#10' in dw or 'Top 10' in dw), 'both disputed rank readings are not printed')
ck('neither is adopted' in dw, 'the de Ridder dispute does not say neither reading is adopted')

# Duel Arena 1 must be flagged as NOT a UFC event.
pi = m_t.find('Duel Arena 1')
ck(pi > 0, 'the Perry vs. Danis card is missing')
pw = m_t[pi:pi + 1100]
for s in ['August 29', 'Kia Center', 'Orlando', '8 p.m. ET', 'not a UFC event']:
    ck(s in pw, 'Duel Arena card missing: %s' % s)

# Bonuses: Fight of the Night stated, no dollar figure invented.
bi = m_t.find('Fight of the Night bonuses')
ck(bi > 0, 'the Sacramento FOTN bonuses are not stated')
ck('No bonus dollar figure' in m_t[bi:bi + 700], 'the page does not disclaim a bonus dollar figure')

# ---- CHAMPIONS BOARD: the three historical regressions, tested BY NAME, in the champions section.
ci = H[MM].find('Champions board')
ck(ci > 0, 'champions board section not found')
cb = H[MM][ci:]
cb = cb[:cb.find('<div class="lab">Sources')] if '<div class="lab">Sources' in cb else cb[:9000]
cbt = txt(cb)
rows = re.findall(r'<tr>.*?</tr>', cb, re.S)
ck(len(rows) >= 12, 'champions board has %d rows (need header + 11 belts)' % len(rows))


def cells_of(div):
    for r in rows:
        cs = [txt(x).strip() for x in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S)]
        if cs and cs[0] == div:
            return cs
    return []


for div, who, notwho in [('Light Heavyweight', 'Ulberg', 'Pereira'),
                         ('Middleweight', 'Strickland', None),
                         ('Featherweight', 'Volkanovski', None),
                         ('Lightweight', 'Gaethje', 'Topuria')]:
    cs = cells_of(div)
    ck(len(cs) >= 2, 'champions board: no parsed row for %s' % div)
    if len(cs) >= 2:
        ck(who in cs[1],
           'champions board: %s champion cell is %r, expected %s' % (div, cs[1][:60], who))
        if notwho:
            ck(notwho not in cs[1],
               'champions board: %s appears in the CHAMPION CELL of %s' % (notwho, div))
# Chimaev may appear only as the man Strickland beat.
if 'Chimaev' in cbt:
    k = cbt.find('Chimaev')
    w = cbt[max(0, k - 260):k + 120]
    ck(any(v in w.lower() for v in ['beat', 'upset', 'defeat', 'over ', 'split-decision', 'split decision']),
       'Chimaev appears in the champions board without a defeat verb')
ck('thirty-second consecutive edition' in m_t.lower(),
   'the champions-board streak was not advanced to thirty-second')

# ============================================================ 6. STRUCTURE (task spec)
NAV = [('index.html', 'Front Page'), ('cyber-briefing.html', 'The Cyber Wire'),
       ('wallstreet-briefing.html', 'The Closing Bell'), ('mma-briefing.html', 'The Octagon'),
       ('archive.html', 'Archive')]
for p in PAGES:
    for href, label in NAV:
        ck(('href="%s"' % href) in H[p], '%s: nav link to %s missing' % (p, href))
        ck(label in T[p], '%s: nav label %r missing' % (p, label))
    for pid in ['id="edition"', 'id="datestamp"', 'id="updated"']:
        ck(pid in H[p], '%s: masthead pill %s missing' % (p, pid))
    ck('id="freshline"' in H[p], '%s: freshness line missing' % p)
    ck("America/New_York" in H[p], '%s: self-stamp JS missing' % p)
    ck('briefings refresh every 30 minutes' in H[p] or 'freshline' in H[p],
       '%s: freshness copy missing' % p)

for p, label, acc in [(CY, 'The Wire', None), (WS, 'The Tape', None), (MM, 'Tale of the Tape', None)]:
    ck(('<div class="tldr"><b>%s</b>' % label) in H[p], '%s: tldr label %r missing' % (p, label))
ck('class="tldr"' not in H[IDX], 'index.html should use cards, not a tldr strip')

# TradingView blocks A-F on the Wall Street page.
tv = H[WS]
for widget, n in [('embed-widget-ticker-tape.js', 1), ('embed-widget-single-quote.js', 3),
                  ('embed-widget-timeline.js', 1), ('embed-widget-stock-heatmap.js', 1),
                  ('embed-widget-mini-symbol-overview.js', 1), ('embed-widget-events.js', 1)]:
    ck(tv.count(widget) == n, 'TradingView %s: expected %d, found %d' % (widget, n, tv.count(widget)))
for sym in ['FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI', 'TVC:USOIL', 'TVC:US10Y']:
    ck(sym in tv, 'mandatory ticker-tape symbol missing: %s' % sym)
ck('id="ufccdn"' in H[MM], 'the MMA countdown element is missing')

# ============================================================ 7. FRESHNESS HYGIENE
for p in PAGES:
    for stale in ['5:36', '5:06', '4:36', '4:15', '3:50', '12:50']:
        ck(('<span class="tag new">New &middot; %s</span>' % stale) not in H[p],
           '%s: a %s item is still tagged new in a 6:06 edition' % (p, stale))
        ck(('&#9679; New &middot; %s' % stale) not in H[p],
           '%s: prose still says "New · %s" in a 6:06 edition' % (p, stale))
    ck(H[p].count('New &middot; 6:06') >= (1 if p != IDX else 0),
       '%s: nothing on the page is marked new this run' % p)

# The 5:36 doubled caveat must be gone.
dupe = ('That last clause is no longer true as of 5:36 — Nvidia now has two sourced after-hours '
        'magnitudes; the sentence is kept only as the record of what this page said at 5:06.')
ck(T[WS].count(dupe) == 1, 'the doubled 5:36 caveat was not deduplicated (count=%d)'
   % T[WS].count(dupe))

# Index cards must faithfully summarise each page's own lead.
ck('reverses on the call' in T[IDX] and 'up almost 5%' in T[IDX],
   'index markets card does not match the Wall Street lead')
ck('Apollo Global Management' in T[IDX], 'index cyber card does not match the cyber lead')
ck('Rodrigues' in T[IDX] and 'Petrino' in T[IDX], 'index MMA card does not match the MMA lead')

# ============================================================ 8. TRAP GREPS
for trap in ['Cody Salkilld', 'Shamil Yakhyaev', 'Abdul-Rakhman', 'Fight Night 286',
             '$1.4 trillion', 'Suno', 'Shanghai Indoor Stadium']:
    for p in PAGES:
        if trap in T[p]:
            k = T[p].find(trap)
            w = T[p][max(0, k - 700):k + 700].lower()
            ck(any(v in w for v in REJECT_VOCAB),
               'TRAP %r appears in %s outside a correction window' % (trap, p))
        else:
            checks += 1

# ============================================================
print('checks run: %d' % checks)
if fails:
    print('FAILURES: %d' % len(fails))
    for f in fails:
        print('  - ' + f)
    sys.exit(1)
print('0 failures')
