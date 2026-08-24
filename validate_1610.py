#!/usr/bin/env python3
"""Programmatic validation — 2026-08-24 post-close Afternoon Edition."""
import io, re, json, sys
from html.parser import HTMLParser

PAGES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']
H = {p: io.open(p, encoding='utf-8').read() for p in PAGES}
fails, checks = [], [0]

def ck(cond, msg):
    checks[0] += 1
    if not cond:
        fails.append(msg)

VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
class Bal(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True); self.st=[]; self.stray=0
    def handle_starttag(self,t,a):
        if t not in VOID: self.st.append(t)
    def handle_endtag(self,t):
        if t in VOID: return
        if t in self.st:
            while self.st and self.st.pop()!=t: pass
        else: self.stray+=1

# ── 1. structure ───────────────────────────────────────────────
for p in PAGES:
    b = Bal(); b.feed(H[p])
    ck(not b.st, '%s: %d unclosed tags %s' % (p, len(b.st), b.st[:6]))
    ck(b.stray == 0, '%s: %d stray end tags' % (p, b.stray))
    nav = re.search(r'<nav class="tabs">(.*?)</nav>', H[p], re.S)
    ck(nav is not None, '%s: no <nav class="tabs">' % p)
    if nav:
        links = re.findall(r'<a href="([^"]+)"([^>]*)>', nav.group(1))
        ck(len(links) == 5, '%s: nav has %d tabs, want 5' % (p, len(links)))
        ck([l[0] for l in links] == ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html'],
           '%s: nav targets wrong' % p)
        on = [l for l in links if 'class="on"' in l[1]]
        ck(len(on) == 1, '%s: %d active tabs, want 1' % (p, len(on)))
        ck(on and on[0][0] == p, '%s: active tab is %s' % (p, on[0][0] if on else '?'))
    for i in ('edition','datestamp','updated','freshline'):
        ck(('id="%s"' % i) in H[p], '%s: missing id=%s' % (p, i))
    ck('Intl.DateTimeFormat' in H[p], '%s: missing self-stamp JS' % p)
    ck("America/New_York" in H[p], '%s: stamp not Eastern' % p)

# ── 2. tldr strips ─────────────────────────────────────────────
LABELS = {'cyber-briefing.html':'The Wire','wallstreet-briefing.html':'The Tape','mma-briefing.html':'Tale of the Tape'}
TLDR = {}
for p, lab in LABELS.items():
    m = re.search(r'<div class="tldr"><b>([^<]+)</b>\s*<span>(.*?)</span></div>', H[p], re.S)
    ck(m is not None, '%s: no .tldr' % p)
    if m:
        ck(m.group(1).strip() == lab, '%s: tldr label %r want %r' % (p, m.group(1), lab))
        TLDR[p] = m.group(2)
    ck(H[p].count('class="tldr"') == 1, '%s: %d tldr blocks' % (p, H[p].count('class="tldr"')))
ck('class="tldr"' not in H['index.html'], 'index.html must not carry a .tldr')

# each index card carries its page's tldr verbatim
for p in LABELS:
    ck(TLDR.get(p, '\x00') in H['index.html'], 'index.html missing verbatim tldr of %s' % p)

# ── 3. TradingView widget JSON ─────────────────────────────────
blocks = re.findall(r'embed-widget-[a-z\-]+\.js"\s+async>(\{.*?\})</script>', H['wallstreet-briefing.html'], re.S)
ck(len(blocks) == 8, 'wallstreet: %d widget blocks, want 8' % len(blocks))
for i, b in enumerate(blocks):
    try: json.loads(b)
    except Exception as e: ck(False, 'widget block %d bad JSON: %s' % (i, e))
tape = re.search(r'embed-widget-ticker-tape\.js"\s+async>(\{.*?\})</script>', H['wallstreet-briefing.html'], re.S)
ck(tape is not None, 'no ticker-tape block')
if tape:
    syms = [s['proName'] for s in json.loads(tape.group(1))['symbols']]
    for req in ('FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y'):
        ck(req in syms, 'ticker tape missing %s' % req)
# GOTCHA #4 — scope Chart-of-the-Day to the mini-symbol-overview block only
mini = re.search(r'embed-widget-mini-symbol-overview\.js"\s+async>(\{.*?\})</script>', H['wallstreet-briefing.html'], re.S)
ck(mini is not None, 'no mini-symbol-overview block')
if mini:
    ck(json.loads(mini.group(1))['symbol'] == 'NASDAQ:SNDK', 'Chart of the Day symbol is %r, want NASDAQ:SNDK' % json.loads(mini.group(1))['symbol'])
    ck('NASDAQ:AAOI' not in mini.group(1), 'Chart of the Day still AAOI')
ck('Chart of the day — SanDisk (SNDK)' in H['wallstreet-briefing.html'], 'chart label not updated')

# ── 4. KEV countdowns (GOTCHA #7) ──────────────────────────────
kev = re.findall(r'<span class="kevdue[^"]*">(.*?)</span>', H['cyber-briefing.html'], re.S)
ck(len(kev) == 12, 'cyber: %d kevdue spans, want 12' % len(kev))
past = sum(1 for k in kev if 'PAST DUE' in k)
today = sum(1 for k in kev if 'DUE TODAY' in k)
ahead = sum(1 for k in kev if 'left' in k and 'DUE TODAY' not in k and 'PAST DUE' not in k)
ck((past, today, ahead) == (8, 1, 3), 'KEV split is %s, want (8,1,3)' % ((past, today, ahead),))

# ── 5. champions board — CHAMPION COLUMN ONLY ──────────────────
sec = re.search(r'Champions board.*?</table>', H['mma-briefing.html'], re.S)
ck(sec is not None, 'no champions board')
if sec:
    rows = re.findall(r'<tr>(?!\s*<th)(.*?)</tr>', sec.group(0), re.S)
    champs = []
    for r in rows:
        tds = re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)
        if len(tds) >= 2: champs.append(re.sub('<[^>]+>', '', tds[1]).strip())
    ck(len(champs) == 11, 'champions board has %d rows, want 11' % len(champs))
    col = ' | '.join(champs)
    for name in ('Aspinall','Ulberg','Strickland','Makhachev','Gaethje','Volkanovski','Yan','Dern'):
        ck(name in col, 'champion column missing %s' % name)
    for bad in ('Pereira','Chimaev','Topuria','Vacant','vacant'):
        ck(bad not in col, 'champion column contains stale/blank %r' % bad)

# ── 6. markets: fresh present, stale absent ────────────────────
W = H['wallstreet-briefing.html']
lead = re.search(r'<div class="lead">.*?</div>\s*</section>', W, re.S)
ck(lead is not None, 'no lead block')
LEAD = lead.group(0) if lead else ''
FRESH_WS = ['25,980.19','&minus;200.27','7,652.96','7,652.86','53,416.99','53,417.16','139.98','140.15',
            '1.14-to-1','1.38-to-1','62 new highs','16 new 52-week highs','2.64%','$1,458.29','$897.86',
            '$429.49','$154.48','$53.62','572%','239%','Lynx Equity Research','Philadelphia SE Semiconductor',
            'Questar','50% starting January 1','Coterra','Expedia','Booking Holdings','eighth time',
            'StockAnalysis.com','After-hours movers'.lower()]
for s in FRESH_WS:
    ck(s.lower() in W.lower(), 'wallstreet missing fresh string %r' % s)
# GOTCHA #5 generalised: a Friday close may appear in the lead ONLY inside prose that
# labels it as Friday's. Test the CONTEXT, not mere presence — blacklisting the string
# itself would flag the deliberate reconciliation sentence as an error.
for bad in ('7,674.37','53,277.01','26,180.46'):
    for m in re.finditer(re.escape(bad), LEAD):
        win = LEAD[max(0, m.start()-260):m.start()+160]
        ck('Friday' in win, 'Friday close %r appears in the lead without being labelled Friday' % bad)
# the cached 12:59 board figures are NOT quoted in the lead at all
for bad in ('7,659.82','53,392.55','26,067.27','79,032.63'):
    ck(bad not in LEAD, 'CACHED 12:59 figure %r leaked into the lead block' % bad)
ck('7,674.37' in W, 'Friday close must still appear in the Weekly Scorecard')
# and Monday's close must NOT be confused with Friday's anywhere
ck('closed at 7,674.37' not in W and 'close at 7,674.37' not in W, 'Friday level presented as a close without qualification')
# stale editorial strings gone
for s in ('Twenty minutes from the bell','twelfth consecutive run of withholding',
          'No After-Hours Movers section appears in this edition',
          'the freshest reading available is forty minutes old'):
    ck(s not in W, 'stale wallstreet string still present: %r' % s)
# GOTCHA #6 — anchored hour
ck(re.search(r'(?<!1)2:59', W) is None, 'bare 2:59 stamp present (should be 12:59 only)')
# GOTCHA #5 — after-hours SECTION LABEL must now be PRESENT (session is over)
ck(re.search(r'<div class="lab">After-hours movers</div>', W) is not None, 'after-hours SECTION LABEL missing after the close')
ck('Monday&rsquo;s close — August 24' in W, 'Monday close table label missing')

# ── 7. cyber fresh/stale ───────────────────────────────────────
C = H['cyber-briefing.html']
for s in ('CVE-2026-76604','CVE-2026-76605','CVE-2026-76606','CVE-2026-76607','CVE-2026-77992',
          'CVE-2026-76571','CVE-2026-76602','CVE-2026-77946','CVE-2026-78050','CVE-2026-77945',
          'Fabrik','TRENDnet','Comfast','cvebrief.com'):
    ck(s in C, 'cyber missing fresh string %r' % s)
ck('CVE-2026-73570' in C and 'due Aug 24' in C.replace('&nbsp;',' ') or 'August 24' in C, 'Zimbra deadline missing')
ck('researchers have named two fresh loaders' not in C, 'stale cyber tldr tail still present')
# the misdated Entra reversal must NOT be published as Aug 24
ck('changed the exploitation status to' not in C or 'August 21' in C, 'Entra reversal date unverified')

# ── 8. New-tag accounting: WS 1 / CY 1 / MMA 0 ─────────────────
counts = {p: H[p].count('class="tag new"') for p in PAGES}
ck(counts['wallstreet-briefing.html'] == 1, 'WS New tags = %d, want 1' % counts['wallstreet-briefing.html'])
ck(counts['cyber-briefing.html'] == 1, 'CY New tags = %d, want 1' % counts['cyber-briefing.html'])
ck(counts['mma-briefing.html'] == 0, 'MMA New tags = %d, want 0' % counts['mma-briefing.html'])
ck(counts['index.html'] == 0, 'index New tags = %d, want 0' % counts['index.html'])
# the New tag must sit on the card the footnote names
m = re.search(r'<span class="tag new">New</span>.*?<h3>(.*?)</h3>', W, re.S)
ck(m is not None and 'Under the flat headline' in m.group(1), 'WS New tag is not on the closing-bell card')
ck('Under the flat headline' in W and '<b>New this edition.</b>' in W, 'WS New card missing its "New this edition" marker')
m2 = re.search(r'<span class="tag new">New</span>', C)
ck(m2 is not None, 'CY New tag missing')
ck(C.count('<b>New this edition.</b>') == 1, 'CY has %d "New this edition" markers, want 1' % C.count('<b>New this edition.</b>'))
# dropped tags really gone
ck('<span class="tag">Iran</span><span class="tag down">Hormuz risk</span><span class="tag new">New</span>' not in W, 'previous Iran New tag not dropped')

# ── 9. trap greps ──────────────────────────────────────────────
TRAPS = ['Cody Salkilld','Abdul-Rakhman','Shamil Yakhyaev','title challenger Beneil',
         'Shanghai Indoor Stadium','mid-August 2025']
for p in PAGES:
    for t in TRAPS:
        ck(t not in H[p], 'TRAP %r found in %s' % (t, p))

# ── 10. hygiene ────────────────────────────────────────────────
for p in PAGES:
    for junk in ('<!--OLD','%%WS','%%CY','%%IDX','OLDLEAD'):
        ck(junk not in H[p], '%s: leftover scaffolding %r' % (p, junk))
    ck('<div class="lab">Sources</div>' in H[p] or p == 'index.html', '%s: no Sources footer' % p)

print('checks: %d   failures: %d' % (checks[0], len(fails)))
for f in fails: print('  FAIL:', f)
sys.exit(1 if fails else 0)
