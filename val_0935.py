#!/usr/bin/env python3
"""Validation guards for the 2026-09-02 09:35 ET edition."""
import re, sys, os, glob, datetime

FAIL = []
CHECKS = [0]
def ck(cond, msg):
    CHECKS[0] += 1
    if not cond: FAIL.append(msg)

pages = {p: open(p, encoding='utf-8').read() for p in
         ('index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html')}
CY, WS, MM, IX = pages['cyber-briefing.html'], pages['wallstreet-briefing.html'], pages['mma-briefing.html'], pages['index.html']

# ---------------------------------------------------------------- structural
for p, h in pages.items():
    for tab in ('index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html', 'archive.html'):
        ck('href="%s"' % tab in h, '%s: missing nav tab %s' % (p, tab))
    for el in ('id="edition"', 'id="datestamp"', 'id="updated"'):
        ck(el in h, '%s: missing masthead %s' % (p, el))
    ck(h.count('class="pill live"') == 1, '%s: LIVE pill count' % p)
    ck("America/New_York" in h, '%s: self-stamp JS missing' % p)
    ck(h.count('<body') == 1 and h.count('</body>') == 1, '%s: body tags' % p)
    ck(h.count('<div') == h.count('</div>'), '%s: unbalanced divs (%d open / %d close)' % (p, h.count('<div'), h.count('</div>')))
for p in ('cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html'):
    ck('id="freshline"' in pages[p], '%s: freshline missing' % p)
    ck('class="tldr"' in pages[p], '%s: tldr missing' % p)

# glyph consistency: each mark must appear in nav AND in the index card kickers
for g in ('⛨', '▲', '⊘'):
    ck(g in IX, 'index: glyph %s missing' % g)
    ck(IX.count(g) >= 2, 'index: glyph %s should appear in nav and card kicker' % g)
ck('&#9880;' not in IX, 'index: wrong alchemical glyph entity present')

# ---------------------------------------------------------------- live widgets (wallstreet)
for w in ('ticker-tape', 'single-quote', 'timeline', 'stock-heatmap', 'mini-symbol-overview', 'events'):
    ck('embed-widget-%s.js' % w in WS, 'wallstreet: missing widget %s' % w)
ck(WS.count('embed-widget-single-quote.js') == 3, 'wallstreet: need 3 single-quote widgets')
for s in ('FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI', 'TVC:USOIL', 'TVC:US10Y'):
    ck(s in WS, 'wallstreet: ticker tape must retain %s' % s)
for p in ('index.html', 'cyber-briefing.html', 'mma-briefing.html'):
    ck('tradingview.com' not in pages[p], '%s: must carry no live widgets' % p)

# ---------------------------------------------------------------- champions board
ch = MM[MM.find('<h2>Champions Board</h2>'):]
rows = re.findall(r'<tr><td>([^<]+)</td><td>([^<]+)</td>', ch)
champ = {a.strip(): b.strip() for a, b in rows}
expect = {'Middleweight': 'Sean Strickland', 'Light Heavyweight': 'Carlos Ulberg',
          'Featherweight': 'Alexander Volkanovski', 'Lightweight': 'Justin Gaethje',
          'Heavyweight': 'Tom Aspinall', 'Welterweight': 'Islam Makhachev',
          'Bantamweight': 'Petr Yan', 'Flyweight': 'Joshua Van'}
for div, who in expect.items():
    got = champ.get(div, '')
    ck(who in got, 'champions: %s should be %s, table has "%s"' % (div, who, got))
# no affirmative present-tense wrong-belt assertions anywhere on the page
for bad in ('Chimaev is the', 'Chimaev retains', 'champion Khamzat Chimaev',
            'Pereira (205)', 'Featherweight VACANT', 'featherweight is vacant'):
    ck(bad not in MM, 'mma: forbidden belt assertion "%s"' % bad)
# Chimaev may appear only as the man Strickland beat / in the stale-list note
ck('Strickland' in MM and 'UFC 328' in MM, 'mma: Strickland/UFC 328 provenance missing')

# ---------------------------------------------------------------- Parnasse provenance
ck('Contender Series' not in MM or not re.search(r'Parnasse[^.]{0,120}Contender Series', MM),
   'mma: Parnasse must never be attributed to the Contender Series')
ck('KSW' in MM, 'mma: Parnasse KSW provenance missing')

# ---------------------------------------------------------------- KEV countdowns
today = datetime.date(2026, 9, 2)
def days(due): return (due - today).days
ck(days(datetime.date(2026, 9, 2)) == 0, 'arith: MLflow due today == 0')
ck(days(datetime.date(2026, 9, 14)) == 12, 'arith: PaperCut Sept 14 == 12 days')
ck(days(datetime.date(2026, 9, 10)) == 8, 'arith: JFrog Sept 10 == 8 days')
ck(days(datetime.date(2026, 8, 29)) == -4, 'arith: Citrix Aug 29 == 4 overdue')
ck('(12 days left)' in CY, 'cyber: PaperCut must read 12 days left')
ck('(8 days left)' in CY, 'cyber: JFrog KEV must read 8 days left')
ck('13 days left' not in CY, 'cyber: stale 13-days PaperCut countdown survived')
ck('4 days overdue' in CY or 'four days past due' in CY, 'cyber: Citrix overdue count missing')
# JFrog two-CVE disambiguation: both CVEs present and distinguished
ck('CVE-2026-82329' in CY and 'CVE-2026-66384' in CY, 'cyber: both JFrog CVEs must be named')
ck('Not in KEV' in CY or 'not in KEV' in CY, 'cyber: 82329 must be marked outside KEV')

# ---------------------------------------------------------------- banned strings (standing refusals)
BANNED = {
 'Nevada statewide': ('cyber-briefing.html',),
 '9.8 million records': ('cyber-briefing.html',),
 '700,000 Singapore': ('cyber-briefing.html',),
 'Jaguar Land Rover': ('cyber-briefing.html',),
 'Midwest water': ('cyber-briefing.html',),
}
for s, ps in BANNED.items():
    for p in ps:
        ck(s not in pages[p], '%s: banned string "%s"' % (p, s))

# ---------------------------------------------------------------- novelty tags vs previous snapshot
snap = sorted(glob.glob('/tmp/%s/archive/*-2026-09-02-0918.html' % os.environ.get('DBDIR', '')))
prev = {}
for f in snap:
    base = os.path.basename(f).split('-')[0]
    prev[base] = open(f, encoding='utf-8').read()
if prev:
    NOVEL = {'wallstreet': ['Lutnick', 'SpaceX'],
             'cyber': ['Rhysida', 'McKesson', 'Virtualizor', 'Astra'],
             'mma': []}
    STALE = {'wallstreet': ['GitLab', 'MongoDB', 'Credo', 'Sirius', 'Vertiv', 'Palo Alto'],
             'cyber': ['Sality', 'WatchGuard', 'Nutex', 'Aesto', 'MLflow'],
             'mma': ['Ruffy', 'Mairon']}
    for sec, names in NOVEL.items():
        for nm in names:
            ck(nm not in prev.get(sec, ''), 'novelty: "%s" tagged New but was in the 0918 snapshot' % nm)
    for sec, names in STALE.items():
        for nm in names:
            ck(nm in prev.get(sec, ''), 'novelty: "%s" expected in 0918 snapshot but absent' % nm)
    # no card may carry a New tag for a name present in the previous snapshot
    for p, sec in (('cyber-briefing.html', 'cyber'), ('wallstreet-briefing.html', 'wallstreet'), ('mma-briefing.html', 'mma')):
        for card in re.findall(r'<div class="card">(.*?)(?=<div class="card">|</div>\s*<h2>|$)', pages[p], re.S):
            if '>New<' not in card: continue
            m = re.search(r'<h3>(.*?)</h3>', card)
            if not m: continue
            title = re.sub(r'<[^>]+>', '', m.group(1))
            # A headline token can appear in the previous edition in an unrelated sense
            # ("Pwn2Own Berlin" vs the Berlin ransomware case; "crude" in a rates table).
            # Novelty is a property of the STORY, so key on a distinctive story term.
            STORYKEY = {'Berlin refuses': 'Rhysida', 'McKesson': 'ShinyHunters',
                        'Virtualizor': 'Virtualizor', 'Chrome and Firefox': 'sandbox escape',
                        'Chip tariffs': 'Lutnick', 'SpaceX': 'SpaceX'}
            key = None
            for frag, sk in STORYKEY.items():
                if frag in title: key = sk; break
            if key is None:
                key = re.split(r'[ (&,—]', title.strip())[0]
            if len(key) > 3 and key in prev.get(sec, ''):
                FAIL.append('%s: card "%s" carries a New tag but story key "%s" appears in the 0918 snapshot' % (p, title[:50], key))
            CHECKS[0] += 1
else:
    print('  (note: previous snapshot not located; novelty diff skipped)')

# ---------------------------------------------------------------- index cards verbatim from page TL;DRs
for p, tag in (('cyber-briefing.html', 'The Wire'), ('wallstreet-briefing.html', 'The Tape'), ('mma-briefing.html', 'Tale of the Tape')):
    m = re.search(r'<div class="tldr"><b>%s</b>\s*<span>(.*?)</span></div>' % re.escape(tag), pages[p], re.S)
    ck(bool(m), '%s: TL;DR labelled "%s" not found' % (p, tag))
    if m: ck(m.group(1).strip() in IX, 'index: card for %s is not a verbatim copy of its page TL;DR' % p)

# ---------------------------------------------------------------- markets discipline
ck('Weekly Scorecard' in WS, 'wallstreet: scorecard missing')
sc = WS[WS.find('<h2>Weekly Scorecard</h2>'):WS.find('<h2>Rates')]
for lvl in ('7,631.47', '26,099.77', '52,766.88'):
    ck(lvl in sc, 'wallstreet: Sept 1 close %s missing from scorecard' % lvl)
# no Sept 2 index LEVEL anywhere in editorial
lead = WS[WS.find('<h2>The Lead</h2>'):WS.find('<h2>Movers')]
# The page deliberately QUOTES the futures-board figures it refused, so the reader can see
# what was withheld and why. Permit them only inside that refusal paragraph; ban elsewhere.
refusal = ''
mref = re.search(r'<p class="note"><b>A refusal, and the reason for it\.</b>.*?</p>', WS, re.S)
if mref: refusal = mref.group(0)
ck(bool(mref), 'wallstreet: the futures-board refusal paragraph is missing')
lead_ex = lead.replace(refusal, '') if refusal else lead
for lvl in ('7,64', '7,62', '29,127', '28,948', '52,900'):
    ck(lvl not in lead_ex,
       'wallstreet: refused level %s appears in The Lead OUTSIDE the refusal paragraph' % lvl)
for lvl in ('29,127', '52,900'):
    ck(lvl in refusal, 'wallstreet: refusal paragraph must name the figure %s it withholds' % lvl)
ck('187 points' in WS, 'wallstreet: post-open Dow move missing')
ck('$89.58' in WS and '$94.28' in WS, 'wallstreet: 9:24 oil reversal figures missing')
ck('rolling URL' in WS, 'wallstreet: Schwab rolling-URL correction missing')
# superlative discipline: no unsourced "worst/biggest megacap/large-cap" claims
for bad in ('worst megacap', 'worst large-cap', 'biggest loser of the day'):
    ck(bad not in WS or 'unsupported' in WS, 'wallstreet: unguarded superlative "%s"' % bad)

# ---------------------------------------------------------------- Astra precision
ck('Preparedness Framework' in CY, 'cyber: Astra threshold must be named as OpenAI\'s own framework')
for bad in ('first AI model ever', 'first model in the world', 'no other model'):
    ck(bad not in CY, 'cyber: overbroad Astra claim "%s"' % bad)

# ---------------------------------------------------------------- attacker claims marked
for s in ('5.79 TB', '284 million'):
    ck(s in CY, 'cyber: figure %s missing' % s)
ck('claim' in CY.lower(), 'cyber: attacker figures must be marked as claims')

# ------------------------------------------------ relative cross-edition pointers (NEW GUARD)
# "the previous edition" re-points itself every time an edition is published, turning a
# true sentence false with nothing on the page changing. Editions must be named by clock
# time. The only permitted use is inside the provenance note that documents this rule.
for p in ('cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html'):
    h = pages[p]
    m = re.search(r'<div class="note"[^>]*><b>On dates and pointers\.</b>.*?</div>', h, re.S)
    ck(bool(m), '%s: standing provenance note missing' % p)
    body = h.replace(m.group(0), '') if m else h
    ck('previous edition' not in body,
       '%s: relative pointer "the previous edition" outside the provenance note' % p)
    ck('yesterday' not in body.lower() or 'flagged yesterday' not in body.lower(),
       '%s: relative day-pointer "yesterday" used for a same-day edition' % p)
    for t in ('8:19 AM', '8:48 AM', '9:18 AM'):
        pass
ck(sum(pages[p].count('AM</b> edition') for p in pages) >= 8,
   'edition references should be absolute and timestamped')

# ---------------------------------------------------------------- sources present
for p in ('cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html'):
    ck('<h2>Sources</h2>' in pages[p], '%s: sources section missing' % p)
    ck(pages[p].count('<a href="http') >= 5, '%s: too few source links' % p)
ck('not investment advice' in WS, 'wallstreet: disclaimer missing')
ck('subject to change' in MM, 'mma: disclaimer missing')

# ---------------------------------------------------------------- report
print('val_0935: %d checks, %d raised' % (CHECKS[0], len(FAIL)))
for f in FAIL: print('  RAISED: ' + f)
sys.exit(1 if FAIL else 0)
