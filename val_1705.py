# -*- coding: utf-8 -*-
"""Validator, Sunday 6 Sep 2026 Afternoon Edition (~5:05pm ET research, stamp 1711)."""
import re, sys, datetime, html as H

F = {n: open(n).read() for n in
     ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}
PREV = {k: open('archive/%s-2026-09-06-1641.html' % k).read() for k in ('cyber','wallstreet','mma')}

fails, checks = [], 0
def ck(cond, msg):
    global checks
    checks += 1
    if not cond: fails.append(msg)

def txt(h):
    h = re.sub(r'<script.*?</script>', ' ', h, flags=re.S)
    h = re.sub(r'<style.*?</style>', ' ', h, flags=re.S)
    return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', h)))

T = {k: txt(v) for k, v in F.items()}
TODAY = datetime.date(2026, 9, 6)

# ── 1. structural: nav, masthead, stamp JS, summary strips ──────────────
for n, h in F.items():
    for tab in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        ck('href="%s"' % tab in h, "%s: nav missing %s" % (n, tab))
    for i in ('edition','datestamp','updated','freshline'):
        ck('id="%s"' % i in h, "%s: missing #%s" % (n, i))
    ck("America/New_York" in h, "%s: stamp JS missing" % n)
    ck(h.count('<nav class="tabs">') == 1, "%s: nav count" % n)

for n, lab in [('cyber-briefing.html','The Wire'),
               ('wallstreet-briefing.html','The Tape'),
               ('mma-briefing.html','Tale of the Tape')]:
    m = re.search(r'<div class="tldr"><b>([^<]*)</b>', F[n])
    ck(m and m.group(1).strip() == lab, "%s: tldr label != %s" % (n, lab))

# ── 2. index cards must match each tldr VERBATIM ────────────────────────
tld = {}
for k, n in [('cy','cyber-briefing.html'), ('ws','wallstreet-briefing.html'), ('mma','mma-briefing.html')]:
    tld[k] = re.search(r'<div class="tldr"><b>[^<]*</b>\s*<span>(.*?)</span></div>', F[n], re.S).group(1)
    ck(tld[k] in F['index.html'], "index: card does not match %s tldr verbatim" % k)
ck(len(re.findall(r'<p>.*?</p>\n<a class="read"', F['index.html'], re.S)) == 3, "index: not 3 cards")
ck('livebar' not in F['index.html'] and 'tradingview' not in F['index.html'].lower(),
   "index: must carry no live widgets")

# ── 3. Wall Street live widget blocks A-F ───────────────────────────────
w = F['wallstreet-briefing.html']
for frag, lab in [('embed-widget-ticker-tape.js','A ticker tape'),
                  ('embed-widget-single-quote.js','B single quotes'),
                  ('embed-widget-timeline.js','C timeline'),
                  ('embed-widget-stock-heatmap.js','D heatmap'),
                  ('embed-widget-mini-symbol-overview.js','E chart of the day'),
                  ('embed-widget-events.js','F calendar')]:
    ck(frag in w, "WS: missing block %s" % lab)
ck(w.count('embed-widget-single-quote.js') == 3, "WS: need exactly 3 single-quote widgets")
for s in ('FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y'):
    ck(s in w, "WS: ticker tape missing %s" % s)
ck('livebar' in w and 'LIVE QUOTES' in w, "WS: livebar wrapper")

# ── 4. MARKETS facts ────────────────────────────────────────────────────
tw = T['wallstreet-briefing.html']
for f in ['7,718.60','26,506.99','53,414.25','271.86','162,000','53,000']:
    ck(f in tw, "WS: missing verified figure %s" % f)
ck(abs((53686.11 - 271.86) - 53414.25) < 1e-9, "WS: Dow arithmetic")
ck('53,686.11' in tw, "WS: Dow prior close absent")

# the 10-year level must NOT be asserted this run
ck('4.79%' not in tw.replace('carried <b>4.79%</b>', '') or 'Not asserted' in tw,
   "WS: 10Y level still asserted")
m10 = re.search(r'US 10-year Treasury yield\s*(\S+)', tw)
ck(m10 and m10.group(1).startswith('Not'), "WS: 10Y row must read 'Not asserted'")
for f in ['4.76','4.74','4.81']:
    ck(f in tw, "WS: 10Y conflict missing %s" % f)
ck('November 2023' in tw and 'three-year highs' in tw, "WS: 10Y superlative conflict not printed")

# standing refusals
for phrase, lab in [('Brent crude','Brent row'), ('Fed funds target range','Fed funds row'),
                    ('2-year / 30-year yields','2Y/30Y row')]:
    ck(phrase in tw, "WS: missing %s" % lab)
ck('VIX' in tw and 'No VIX level is published' in tw, "WS: VIX refusal must persist")
ck('After-Hours' not in tw and 'after-hours session' in tw.lower(),
   "WS: weekend must have no after-hours section but must say so")

# Waller block (this run's New item)
for f in ['Waller','would be inclined','nearly 65%','50-50','John Williams','Purtell',
          'Neuberger','knife edge','Vance','3.7%','0.2% from June to July','11 September']:
    ck(f in tw, "WS: Waller block missing %s" % f)
_ref = re.search(r'Two readings are refused\.(.*?)predate Thursday', tw, re.S)
ck(_ref is not None, "WS: refusal paragraph missing")
ck(tw.count('4.76% in February') == 1 and '4.76% in February' in (_ref.group(1) if _ref else ''),
   "WS: 4.76/3.05 pair must appear only inside the printed refusal")
ck('3.05' in (_ref.group(1) if _ref else ''), "WS: 3.05 must sit inside the refusal")
ck(tw.count('66.1%') == 1, "WS: 66.1% should appear once, as a superseded figure")
ck(re.search(r'supersedes the week-old 66\.1% reading', tw) is not None,
   "WS: 66.1% must be marked superseded, not presented as current")

# ── 5. CYBER facts ──────────────────────────────────────────────────────
tc = T['cyber-briefing.html']
for f in ['StyleSmuggler','Sansec','2.4.9','ProxiBlue','Graycore','Lucas van Staden','Bouma',
          'eComscan','1,728','1.9 MB','Rust','CVE-2026-32475','9.8','MikroTrick','CERT Polska']:
    ck(f in tc, "CY: missing %s" % f)
ck('Store A' in tc and '2.4.8' in tc and '2.4.7-p2' in tc, "CY: store versions")
ck('26 distinct source addresses' in tc, "CY: 26 addresses")
ck('no CVE' in tc or 'no CVE identifier' in tc, "CY: StyleSmuggler must stay CVE-less")

# KEV: verified adds and countdowns computed from today
for cve, due, days in [('CVE-2026-85046', datetime.date(2026,9,18), 12)]:
    ck((due - TODAY).days == days, "CY: %s countdown arithmetic" % cve)
    ck(cve in tc, "CY: missing %s" % cve)
ck((datetime.date(2026,9,16) - TODAY).days == 10, "CY: 16 Sep = 10 days")
ck((TODAY - datetime.date(2026,9,5)).days == 1, "CY: 5 Sep group overdue by 1")
for f in ['18 September','16 September','5 September']:
    ck(f in tc, "CY: KEV date %s missing" % f)
ck('CVE-2026-83548' in tc and 'CVE-2026-49869' in tc, "CY: CVSS 10.0 KEV pair")
# no KEV additions found for 5-6 Sep this run
ck('7 September' not in tc or 'Labor Day' not in tc, "CY: stray date")

# Patch Priority severity border
mpp = re.search(r'Patch Priority.{0,400}', F['cyber-briefing.html'], re.S)
ck('var(--crit)' in F['cyber-briefing.html'], "CY: patch priority crit border")

# ── 6. MMA facts ────────────────────────────────────────────────────────
tm = T['mma-briefing.html']
CHAMPS = ['Tom Aspinall','Ciryl Gane','Carlos Ulberg','Sean Strickland','Islam Makhachev',
          'Justin Gaethje','Alexander Volkanovski','Petr Yan','Joshua Van',
          'Valentina Shevchenko','Kayla Harrison','Mackenzie Dern']
rows = re.findall(r'<tr><td>([^<]+)</td><td><b>([^<]+)</b></td>', F['mma-briefing.html'])
board = [(d, c) for d, c in rows if d in
         ['Heavyweight','Interim Heavyweight','Light Heavyweight','Middleweight','Welterweight',
          'Lightweight','Featherweight','Bantamweight','Flyweight','Women&rsquo;s Flyweight',
          'Women&rsquo;s Bantamweight','Women&rsquo;s Strawweight']]
ck(len(board) == 12, "MMA: champions board has %d rows, expected 12" % len(board))
got = [H.unescape(c).strip() for _, c in board]
ck(got == CHAMPS, "MMA: champions board mismatch -> %s" % got)
# forbidden regressions in the champion column ONLY
for bad in ['Pereira','Chimaev','Topuria','Pantoja','Dvalishvili']:
    ck(not any(bad in c for c in got), "MMA: REGRESSION - %s in champion column" % bad)

# stoppage-time refusal
ck('2:25' in tm and '2:35' in tm, "MMA: both stoppage times must be shown")
ck('2026-09-05T18:40:35' in tm, "MMA: modified_time evidence absent")
ck('eighth consecutive edition' in tm, "MMA: refusal counter not incremented")
ck('five consecutive runs' in tm, "MMA: byte-identical counter not incremented")
ck('not asserted' in tm.lower(), "MMA: stoppage refusal wording")

# verified-this-run UFC.com figures
for f in ['$4,365,335','15,687','Accor Arena history','Parnasse','Axel Sola','Losene Keita','Mario Pinto']:
    ck(f in tm, "MMA: missing verified %s" % f)
ck('Fight of the Night' in tm and 'no Fight of the Night' in tm, "MMA: FOTN absence")
ck('re-fetched directly this run' in tm, "MMA: bonus re-fetch note")
for f in ['Menifield','Baraniewski','UFC 227']:
    ck(f in tm, "MMA: UFC 331 addition %s missing" % f)

# chronology: nothing "upcoming" that has passed
for d, lab in [(datetime.date(2026,9,12),'Noche UFC'), (datetime.date(2026,9,19),'UFC 331')]:
    ck(d > TODAY, "MMA: %s is not in the future" % lab)

# ── 7. New tags: earned by absence from the 1641 snapshot ───────────────
NEW = {'cyber-briefing.html': [('ProxiBlue','cyber'), ('Graycore','cyber'),
                               ('Bouma','cyber'), ('eComscan','cyber')],
       'wallstreet-briefing.html': [('Waller','wallstreet'), ('Purtell','wallstreet'),
                                    ('Neuberger','wallstreet'), ('50-50','wallstreet')]}
for page, toks in NEW.items():
    for tok, arch in toks:
        ck(tok in F[page], "NEW: %s absent from %s" % (tok, page))
        ck(tok not in PREV[arch], "NEW: %s was ALREADY in the 1641 snapshot - tag not earned" % tok)

ck(F['cyber-briefing.html'].count('class="t new"') == 2,
   "CY: expected exactly 2 New tags, got %d" % F['cyber-briefing.html'].count('class="t new"'))
ck(F['wallstreet-briefing.html'].count('class="t new"') == 2,
   "WS: expected 2 New markers (mover + rate call), got %d" % F['wallstreet-briefing.html'].count('class="t new"'))
ck(F['mma-briefing.html'].count('class="t new"') == 0,
   "MMA: expected 0 New tags, got %d" % F['mma-briefing.html'].count('class="t new"'))
ck('Cyber carries 2 New tags' in T['cyber-briefing.html'], "CY: New-tag tally not updated")
# every New marker uses the site-wide class
for n, h in F.items():
    ck('class="t hot">New<' not in h, "%s: New tag uses wrong class" % n)

# ── 8. weekday guard: every "<Day> <DD> <Month>" string must be real ────
DAYS = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
MON = {m: i+1 for i, m in enumerate(
    ['January','February','March','April','May','June','July','August',
     'September','October','November','December'])}
bad = []
for n, t in T.items():
    for dn, dd, mo in re.findall(r'\b(%s)\s+(\d{1,2})\s+(%s)\b' % ('|'.join(DAYS), '|'.join(MON)), t):
        try: d = datetime.date(2026, MON[mo], int(dd))
        except ValueError: bad.append((n, dn, dd, mo)); continue
        if d.weekday() != DAYS[dn]: bad.append((n, dn, dd, mo))
    for dn, mo, dd in re.findall(r'\b(%s),?\s+(%s)\s+(\d{1,2})\b' % ('|'.join(DAYS), '|'.join(MON)), t):
        try: d = datetime.date(2026, MON[mo], int(dd))
        except ValueError: bad.append((n, dn, mo, dd)); continue
        if d.weekday() != DAYS[dn]:
            ctx = t[max(0, t.find('%s, %s %s' % (dn, mo, dd)) - 200):]
            quoted = ('one return dated the release' in ctx[:400]
                      or 'is a Friday' in ctx[:400])
            if not quoted: bad.append((n, dn, mo, dd))
ck('11 September 2026 is a Friday' in T['wallstreet-briefing.html'],
   "WS: the mis-dated-CPI correction must be printed")
ck(not bad, "weekday guard failures: %s" % bad)
ck(datetime.date(2026,9,11).weekday() == 4, "11 Sep 2026 must be a Friday")
ck(datetime.date(2026,9,7).weekday() == 0, "7 Sep 2026 must be a Monday")

# ── 9. sources + disclaimers ────────────────────────────────────────────
for n in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    ck('Sources' in T[n], "%s: no sources footer" % n)
    ck(len(re.findall(r'https?://', F[n])) >= 10, "%s: too few source URLs" % n)
ck('Nothing here is investment advice' in T['wallstreet-briefing.html'], "WS: disclaimer")
ck('subject to change' in T['mma-briefing.html'], "MMA: disclaimer")
ck('pbs.org' in F['wallstreet-briefing.html'], "WS: PBS/AP source URL missing")

# ── 10. no unresolved entities / broken markup ──────────────────────────
for n, h in F.items():
    ck('&&' not in h and '&nbsp,' not in h, "%s: entity damage" % n)
    ck(h.count('<div') - h.count('</div>') == 0, "%s: unbalanced divs (%d/%d)" % (n, h.count('<div'), h.count('</div>')))
    ck('TODO' not in h and 'XXX' not in h, "%s: placeholder text" % n)
    orphan = re.findall(r'(?<!&)\b(mdash|rsquo|ldquo|rdquo|ndash|minus|nbsp|amp)\;', h)
    ck(not orphan, "%s: orphaned entity fragments %s (sed '&' damage?)" % (n, set(orphan)))
    dup = re.findall(r'<h3[^>]*>([^<]{25,})\1', h)
    ck(not dup, "%s: duplicated headline text %s" % (n, dup))

print("checks run: %d" % checks)
if fails:
    print("FAILURES (%d):" % len(fails))
    for f in fails: print("  -", f)
    sys.exit(1)
print("ALL CLEAR")
