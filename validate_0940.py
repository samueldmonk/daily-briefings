# -*- coding: utf-8 -*-
"""Validator for the Sat Aug 29 2026, 9:40 AM ET edition."""
import re, sys, io

PAGES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']
F = {p: io.open(p, encoding='utf-8').read() for p in PAGES}
ix, cy, ws, mm = F['index.html'], F['cyber-briefing.html'], F['wallstreet-briefing.html'], F['mma-briefing.html']
n = 0
fails = []

def chk(cond, msg):
    global n
    n += 1
    if not cond:
        fails.append(msg)

def txt(s):
    return re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', s)).strip()

STAMP = "9:40 AM"

# ── 1. structure: five-tab nav, one active tab, stamp pills, freshline, self-stamp
for p, s in F.items():
    for href in PAGES + ['archive.html']:
        chk('href="%s"' % href in s, "%s: nav missing %s" % (p, href))
    chk(s.count('class="on"') == 1, "%s: expected exactly one active tab, got %d" % (p, s.count('class="on"')))
    for pid in ['edition', 'datestamp', 'updated', 'freshline']:
        chk('id="%s"' % pid in s, "%s: missing id=%s" % (p, pid))
    chk('America/New_York' in s, "%s: missing self-stamp JS" % p)
    chk(s.rstrip().endswith('</html>'), "%s: malformed tail" % p)

# ── 2. tldr strips on the three briefings, absent from index; correct labels
for p, lab in [('cyber-briefing.html', 'The Wire'),
               ('wallstreet-briefing.html', 'The Tape'),
               ('mma-briefing.html', 'Tale of the Tape')]:
    chk('class="tldr"' in F[p], "%s: missing tldr" % p)
    chk('<b>%s</b>' % lab in F[p], "%s: wrong tldr label" % p)
chk('class="tldr"' not in ix, "index must not carry a tldr strip")

# ── 3. index cards byte-identical (whitespace-normalised) to each page's tldr
def tldr_of(s):
    m = re.search(r'<div class="tldr"><b>[^<]*</b>\s*<span>(.*?)</span></div>', s, re.S)
    return m.group(1) if m else None

for cls, src, lab in [('c-cy', cy, 'cyber'), ('c-ws', ws, 'markets'), ('c-mm', mm, 'mma')]:
    t = tldr_of(src)
    chk(t is not None, "%s: no tldr to compare" % lab)
    m = re.search(r'<div class="bigcard ' + cls + r'">.*?<p>(.*?)</p>', ix, re.S)
    chk(m is not None, "index: card %s not found" % cls)
    if m and t:
        chk(re.sub(r'\s+', ' ', m.group(1)).strip() == re.sub(r'\s+', ' ', t).strip(),
            "index card %s not identical to %s tldr" % (cls, lab))

# ── 4. edition-stamp freshness: every `tag new` carries this run's stamp; prior stamps gone
# A `tag new` now means: this item was sourced or materially changed IN THIS RUN.
# Exact per-page counts, so a carried item cannot quietly wear a fresh stamp.
EXPECT_FRESH = {'cyber-briefing.html': 2,   # CareCloud (new), Boston Scientific (updated)
                'wallstreet-briefing.html': 0,  # market closed; nothing can be new on the movers board
                'mma-briefing.html': 1}    # Noche UFC 4 (venue + headliner sourced this run)
for p, want in EXPECT_FRESH.items():
    tags = re.findall(r'<span class="tag new">([^<]*)</span>', F[p])
    chk(len(tags) == want, "%s: expected %d fresh tags, got %d %r" % (p, want, len(tags), tags))
    for t in tags:
        chk(STAMP in t, "%s: stale fresh tag %r" % (p, t))
    chk('<span class="tag new">New</span>' not in F[p], "%s: bare New tag" % p)
# and no page may claim novelty in prose for something it does not tag as new
chk('genuinely new item this run' not in ws, "ws: stale novelty claim in the Lead")
chk('What is new this run' not in cy, "cyber: stale novelty claim in the Top Story")
chk('New this run &mdash; the exploitation' not in cy, "cyber: stale novelty claim in Patch Priority")
chk('resolved after the previous edition went out' not in mm, "mma: stale temporal claim")
chk('a fourth read' not in ws, "ws: miscounted Salesforce reads")
chk(ws.count('22.6%') >= 1 and '11.2%' in ws and '22.87%' in ws, "ws: Salesforce read set incomplete")
chk('six reads' in ws.lower() or 'Six different percentages' in ws, "ws: Salesforce count not stated as six")
# Scoped to EDITION STAMPS ONLY (inside tag spans / freshline), so that a real
# event start time such as the Contender Series "7:00 PM ET" is not mistaken for one.
for p, s in F.items():
    stamp_zones = re.findall(r'<span class="tag[^"]*">([^<]*)</span>', s) + \
                  re.findall(r'id="freshline"[^>]*>([^<]*)<', s)
    for z in stamp_zones:
        for old in ['9:15 AM', '8:46 AM', '8:44 AM', '8:40 AM', '8:19 AM']:
            chk(old not in z, "%s: prior edition stamp %s survived in tag %r" % (p, old, z))
    chk(STAMP in s, "%s: current stamp missing" % p)

# ── 5. TradingView live blocks: Wall Street only
for w in ['ticker-tape', 'single-quote', 'timeline', 'stock-heatmap', 'mini-symbol-overview', 'events']:
    chk('embed-widget-%s.js' % w in ws, "ws: missing widget %s" % w)
chk(ws.count('embed-widget-single-quote.js') == 3, "ws: need exactly 3 single-quote widgets")
chk(ws.count('s3.tradingview.com/external-embedding') == 8, "ws: expected 8 TradingView scripts, got %d"
    % ws.count('s3.tradingview.com/external-embedding'))
for sym in ['FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI', 'TVC:USOIL', 'TVC:US10Y']:
    chk(sym in ws, "ws: tape missing %s" % sym)
chk('NASDAQ:PYPL' in ws, "ws: Chart of the Day must be NASDAQ:PYPL")
chk('class="livebar"' in ws, "ws: missing livebar")
for p in ['index.html', 'cyber-briefing.html', 'mma-briefing.html']:
    chk('tradingview' not in F[p].lower(), "%s: must not carry live widgets" % p)

# ── 6. markets: closed-market discipline, reconciliation arithmetic, rejected figures stay out
chk('as of ~' not in ws, "ws: intraday 'as of ~' marker on a closed-market page")
chk('Monday, August 31' in ws, "ws: must say when the tape reopens")
chk('7,673.04' not in ws, "ws: rejected Thursday close 7,673.04 reappeared")
chk('After-Hours' not in ws and 'After Hours' not in ws, "ws: After-Hours section must be absent (market closed)")
chk('7,711.76' in ws and '26,402.42' in ws and '53,559.99' in ws, "ws: Friday closes missing")
chk('7,730.99' in ws and '26,541.35' in ws and '53,569.44' in ws, "ws: Thursday closes missing")
# arithmetic guards, strict to the precision the prose claims
chk(abs((53569.44 - 9.45) - 53559.99) < 0.005, "ws: Dow points/level reconciliation fails")
chk(abs((7711.76 / 7730.99 - 1) * 100 - (-0.25)) < 0.005, "ws: S&P percent reconciliation fails")
chk(abs((26402.42 / 26541.35 - 1) * 100 - (-0.52)) < 0.005, "ws: Nasdaq percent reconciliation fails")
# the superseded Fed pricing must be shown as superseded, not asserted as current
chk('superseded' in ws.lower(), "ws: Fed pricing change must be labelled superseded")
chk('48%' in ws and 'Kalshi' in ws, "ws: new Kalshi pricing missing")
chk('nearly 70%' in ws, "ws: prior no-change reading must be shown alongside")
chk('carried from the previous edition' in ws.lower(), "ws: December odds must be labelled carried")
# 1.82% may only appear inside its own rejection text
for m in re.finditer(r'1\.82%', ws):
    w = ws[max(0, m.start() - 400):m.end() + 400].lower()
    chk('not' in w or 'reject' in w or 'unpublish' in w, "ws: 1.82% appears outside a rejection window")

# ── 7. cyber: CVE whitelist, KEV countdowns, directive naming
CVE_OK = {'CVE-2026-8452', 'CVE-2019-1068', 'CVE-2022-0995', 'CVE-2021-23758',
          'CVE-2015-5287', 'CVE-2015-3246', 'CVE-2026-53362', 'CVE-2023-49105',
          'CVE-2026-66384', 'CVE-2026-81578', 'CVE-2026-82078', 'CVE-2026-69836',
          'CVE-2026-21962', 'CVE-2026-20253'}
found = set(re.findall(r'CVE-\d{4}-\d{4,}', cy))
chk(found <= CVE_OK, "cyber: unwhitelisted CVE id(s): %s" % (found - CVE_OK))
chk(len(found) >= 12, "cyber: whitelist liveness — only %d CVEs on page" % len(found))
chk('9.8' not in cy, "cyber: rejected CVSS 9.8 reappeared")
chk('8.8' in cy and '9.4' in cy, "cyber: PaperCut CVSS pair missing")
chk('10.0' in cy, "cyber: Entra ID CVSS 10.0 missing")
for days, label in [('0 days', 'today'), ('1 day', 'Aug 30'), ('11 days', 'Sept 9'), ('12 days', 'Sept 10')]:
    chk(days in cy, "cyber: KEV countdown %s (%s) missing" % (days, label))
chk('BOD 26-04' in cy, "cyber: BOD 26-04 must be named")
for m in re.finditer(r'BOD 22-01', cy):
    w = cy[max(0, m.start() - 300):m.end() + 300].lower()
    chk('supersed' in w or 'no longer' in w or 'old' in w, "cyber: BOD 22-01 named without the superseded caveat")
chk('14.1-73.32' in cy and '14.1-72.61' in cy, "cyber: both Citrix build sets must be printed")
chk('CTX696604' in cy, "cyber: Citrix advisory id missing")
# new this run
chk('3,756,469' in cy, "cyber: CareCloud filed victim count missing")
chk('March 10' in cy and 'March 16' in cy, "cyber: CareCloud access window missing")
chk('350,000' in cy and '3.7 million' in cy, "cyber: CareCloud amendment history must be shown")
chk('700 basis points' in cy, "cyber: Boston Scientific revenue-hit figure missing")
chk('August 26' in cy, "cyber: Boston Scientific Ireland WFH date missing")
# signatory count split: all four reported forms present, none adopted as the count
for form in ['116', 'nearly 130', 'more than 130', '100-plus']:
    chk(form in cy, "cyber: signatory-count form %r missing" % form)
chk('no single' in cy.lower() or 'not agreed' in cy.lower(), "cyber: signatory split must be flagged")

# ── 8. mma: champions board parsed as real cells; regressions absent from champion cells only
seg = mm[mm.find('Champions Board'):]
rows = re.findall(r'<tr>(.*?)</tr>', seg, re.S)
cells = [re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S) for r in rows]
champ = [c for c in cells if len(c) >= 2 and txt(c[0])]
chk(len(champ) >= 11, "mma: champions board has %d rows, expected >=11" % len(champ))

def champ_for(div_kw):
    for c in champ:
        if div_kw.lower() in txt(c[0]).lower():
            return txt(c[1])
    return None

EXPECT = {'Heavyweight': 'Aspinall', 'Light Heavyweight': 'Ulberg', 'Middleweight': 'Strickland',
          'Welterweight': 'Makhachev', 'Lightweight': 'Gaethje', 'Featherweight': 'Volkanovski',
          'Bantamweight': 'Yan', 'Flyweight': 'Van'}
for div, who in EXPECT.items():
    cell = champ_for(div)
    chk(cell is not None, "mma: no champions row for %s" % div)
    if cell is not None:
        chk(who in cell, "mma: %s champion cell is %r, expected %s" % (div, cell, who))

champ_cells = " || ".join(txt(c[1]) for c in champ)
for bad in ['Pereira', 'Chimaev', 'Topuria', 'Vacant', 'vacant']:
    chk(bad not in champ_cells, "mma: REGRESSION — %r appears in a champion cell" % bad)

# ── 9. mma: name traps, spelling splits, result integrity
for trap in ['Shamil Yakhyaev', 'Cody Salkilld', 'Abdul-Rakhman']:
    chk(trap not in mm, "mma: name trap %r present" % trap)
for pair in ['Aoriqileng', 'Qileng Aori', 'Sumudaerji', 'Su Mudaerji']:
    chk(pair in mm, "mma: spelling form %r missing" % pair)
chk('Undecided' not in mm, "mma: an Undecided row survived a completed card")
chk('(prelim)</td>' not in mm, "mma: a results row shipped without a division label")
chk('tag warn">Live now' not in mm, "mma: stale live-now marker")
chk('live now' not in mm.lower(), "mma: stale in-progress language")
chk('Marc Goddard' in mm, "mma: referee not printed")
chk('1:48' in mm, "mma: main event finish time missing")
chk('2026-08-28T14:03' in mm, "mma: UFC.com lag timestamp must be printed as provenance")
chk('fifth' in mm.lower(), "mma: fifth-fetch provenance claim missing")
chk('forty-eighth consecutive edition' in mm, "mma: champions-board counter not advanced")
chk('seventh consecutive edition' in mm, "mma: ESPN-agreement counter not advanced")
chk('empty body' in mm, "mma: the weaker ESPN provenance this run must be disclosed")
chk('no title bout' in mm, "mma: must state no belt could move on this card")
# Noche UFC dual naming: both forms present, neither adopted
chk('Silva vs. Delgado' in mm and 'Rodriguez vs. Silva' in mm, "mma: Noche UFC dual naming incomplete")
chk('Desert Diamond Arena' in mm, "mma: Noche UFC venue missing")
chk('Delgado' in mm and 'withdrew' in mm, "mma: Rodriguez withdrawal not stated")
# bonuses: still none announced, and the page must say so rather than print a figure
chk('no bonuses' in mm.lower() or 'Still no bonuses' in mm, "mma: bonus status not stated")
chk("reporter" in mm.lower(), "mma: the POTN assessment must be labelled as an assessment")
# fresh prospect tags
chk(mm.count('tag pros') == 4, "mma: expected 4 prospect tags, got %d" % mm.count('tag pros'))

# ── 10. cross-page: date coherence and disclaimers
chk(sum('August 29' in s or 'Aug 29' in s or 'Aug. 29' in s for s in F.values()) >= 3,
    "the run's date must appear on at least three pages")
for p in ['cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html', 'index.html']:
    chk('class="disc"' in F[p], "%s: missing disclaimer" % p)
chk('not investment advice' in ws.lower() or 'not investment advice' in ix.lower(),
    "ws: investment-advice disclaimer missing")
chk('subject to change' in mm.lower(), "mma: cards-subject-to-change disclaimer missing")
for p in ['cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']:
    chk('Sources checked this run' in F[p], "%s: sources footer missing" % p)
    chk(F[p].count('https://') >= 8, "%s: too few source URLs" % p)

# ── 11. guards written against THIS run's read-through findings, so they cannot recur
chk('has not been resulted' not in mm, "mma: stale 'main event unresulted' claim survives a completed card")
chk('Two fighters missed weight' not in mm, "mma: weight-miss count contradicts itself (two vs three)")
chk('Three of thirteen fighters' not in mm, "mma: bout count used as a fighter count")
chk('115-pound strawweight limit' not in mm, "mma: unsourced weight limit asserted")
chk('three different ways' not in cy, "cyber: signatory-count adjective contradicts the four counts listed")
chk('four different counts' in cy, "cyber: signatory-count framing missing")
# no duplicate source links on any page
for p in ['cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']:
    hrefs = re.findall(r'<a href="(https?://[^"]+)"', F[p])
    chk(len(hrefs) == len(set(hrefs)), "%s: duplicate source links (%d links, %d unique)"
        % (p, len(hrefs), len(set(hrefs))))
# no sentence may claim novelty while its own card is tagged carried
chk(cy.count('First published in the 8:46 edition and carried unchanged.') == 1,
    "cyber: provenance sentence duplicated")

print("validate_0940: %d checks, %d failures" % (n, len(fails)))
for f in fails:
    print("  FAIL: " + f)
sys.exit(1 if fails else 0)
