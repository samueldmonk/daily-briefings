#!/usr/bin/env python3
"""Programmatic validation for the 5:36 PM ET edition, Aug 26 2026."""
import io, os, re, sys, datetime

O = os.path.dirname(os.path.abspath(__file__))
P = {n: io.open(os.path.join(O, n), encoding='utf-8').read()
     for n in ('index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html')}
fails, checks = [], 0


def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)


def near(a, b, tol=0.05):
    return abs(a - b) <= tol


TODAY = datetime.date(2026, 8, 26)

# ------------------------------------------------ 1. ARITHMETIC, IN PYTHON
# ANF intraday price ladder against the common base the 2:40 strip confirms
base = 153.40 - 44.50
ck(near(base, 108.90, 0.001), 'ANF base 153.40-44.50 != 108.90')
ladder = [(121.47, 11.5), (144.81, 33.0), (153.40, 40.9)]
prev = 0
for px, pct in ladder:
    ck(near((px / base - 1) * 100, pct, 0.06), 'ANF ladder %% wrong for %s' % px)
    ck(px > prev, 'ANF ladder not monotonic at %s' % px)
    prev = px
ck(near(121.47 / 1.119, 108.55, 0.01), "StockStory 11.9%% implied base != 108.55")
ck(not near(144.81 / base - 1, 0.418, 0.005), 'StockStory 41.8% must NOT reconcile to 144.81')
ck(near((13.10 + 13.60) / 2, 13.35, 0.001), 'ANF FY guide midpoint != 13.35')
ck(near((296 / 170.3 - 1) * 100, 73.8, 0.1), 'ANF EBITDA beat != 73.8%')

# HP Inc
ck(near((15.7 / 14.34 - 1) * 100, 9.5, 0.05), 'HPQ revenue beat != 9.5%')
ck(near(0.83 - 0.66, 0.17, 0.001), 'HPQ 17-cent beat needs a 0.66 base')
ck(near((3.19 + 3.29) / 2, 3.24, 0.001), 'HPQ FY midpoint != 3.24')
ck(near(((3.19 + 3.29) / 2 / 3.04 - 1) * 100, 6.6, 0.05), 'HPQ midpoint vs consensus != 6.6%')

# Nutanix
ck(near(0.60 - 0.11, 0.49, 0.001), 'NTNX implied consensus != 0.49')

# Salesforce: the $5.90 figure must be demonstrably non-annualisable
ck(5.90 * 4 > 16.71, 'CRM $5.90 x4 must exceed the FY guide top for the flag to hold')
ck(near(5.90 * 4, 23.60, 0.001), 'CRM 5.90x4 != 23.60')

# Nvidia figures already on the page
ck(near(96.22 / 46.74, 2.06, 0.005), 'NVDA revenue not 2.06x year-ago')
ck(near(89.02 / 96.22 * 100, 92.5, 0.1), 'NVDA DC share != 92.5%')
ck(108.0 * 0.98 > 104.2, 'NVDA Q3 guide band bottom must sit above consensus')

# ------------------------------------------------ 2. THE NUMBERS APPEAR AS DERIVED
w = P['wallstreet-briefing.html']
for s in ('$121.47', '$144.81', '$153.40', '108.90', '&plus;11.5%', '&plus;33.0%', '&plus;40.9%',
          '$0.83', '$15.7&nbsp;billion', '$14.34&nbsp;billion', '$3.19&ndash;$3.29', '$3.24 midpoint',
          '$3.04 consensus', '9.5%', '6.6%', '$0.60', '$0.49', '$757.1&nbsp;million',
          '$3.91', '$2.48&nbsp;billion', '$5.90', '$23.60', '$1.96&nbsp;billion', '$2.10',
          '17.3%', '6.2%', '$296&nbsp;million', '$170.3&nbsp;million', '19.9%', '15.9%'):
    ck(s in w, 'WS missing figure %s' % s)

# every new after-hours percentage present, with its source named
for name, pct in (('Okta', '&plus;17%'), ('Salesforce', '&plus;12%'), ('CrowdStrike', '&plus;10%'),
                  ('Nutanix', '&plus;5%'), ('Nvidia', '&minus;1%'), ('Synopsys', '&minus;6%'),
                  ('HP Inc', '&minus;11%')):
    ck(pct in w, 'WS missing roundup pct %s for %s' % (pct, name))
ck(w.count('Investing.com') >= 5, 'WS: Investing.com under-attributed')
ck('Kiplinger' in w, 'WS: Kiplinger read not attributed')

# ------------------------------------------------ 3. THE -1.59% GUARD (recurring bug class)
# -1.59% is NVDA's REGULAR-SESSION close. It may appear only in close or rejection context.
REJECT_VOCAB = ('reject', 'not published', 'reject', 'regular-session', 'REGULAR-SESSION',
                'on the session', 'went into the print red', 'relabel', 'declined to adopt',
                'Distinguish these from', 'remains rejected', 'closed')
for m in re.finditer(r'1\.59%', w):
    win = w[max(0, m.start() - 420): m.start() + 420]
    ck(any(v in win for v in REJECT_VOCAB),
       'WS: 1.59%% at %d lacks close/rejection context' % m.start())

# the new NVDA after-hours magnitudes must be present and distinguished from 1.59
ck('down about 1%' in w, 'WS: NVDA -1% after-hours magnitude missing')
ck('&minus;1.3%' in w, 'WS: NVDA -1.3% second read missing')
i = w.find('Distinguish these from')
ck(i > 0 and '1.59%' in w[i:i + 260], 'WS: the 1.59 distinction sentence lost its subject')

# ------------------------------------------------ 4. THE WSM/ANF RETRACTION IS REAL
ck('did NOT report after this bell' in w, 'WS: WSM/ANF retraction headline missing')
ck('SUPERSEDED at 5:36' in w, 'WS: old WSM placeholder not superseded')
ck('No results and no after-hours prices for either appeared' not in w,
   'WS: the retracted "still to be seen" claim survived verbatim')
i = w.find('did NOT report after this bell')
ck('BEFORE' in w[i:i + 900], 'WS: retraction does not say they reported before the open')

# ------------------------------------------------ 5. NO UNSOURCED ANF CLOSE
for bad in ('112.62', '97.69'):
    for m in re.finditer(re.escape(bad), w):
        win = w[max(0, m.start() - 500): m.start() + 320]
        ck(('NO ANF CLOSING PRICE IS ASSERTED' in win or 'mutually contradictory' in win
            or 'Nothing from either is published' in win or 'three weeks old' in win),
           'WS: %s appears outside its rejection window at %d' % (bad, m.start()))

# ------------------------------------------------ 6. CYBER: NEW MATERIAL, NO INVENTED IDs
c = P['cyber-briefing.html']
for s in ('CVE-2026-61979', 'CVE-2026-15981', 'miniOrange SAML 2.0 Single Sign On',
          '5.4.5', '10,000', 'Patchstack', 'DigitalOcean',
          'NemoClaw', 'OpenShell', '18 vulnerabilities', 'DGX Spark', 'Unified Fabric Manager',
          'Triton Inference Server', 'Cumulus Linux', 'NVOS',
          'Substance 3D Designer', 'Substance 3D Sampler', 'Substance 3D Painter',
          'Campaign Classic', 'Content Credentials SDK', 'priority rating of 1',
          'Nutex Health', 'ReliaQuest', 'ShinyHunters', 'Chrome 152', 'water systems'):
    ck(s in c, 'CY missing %s' % s)

# the Adobe/Nvidia block must NOT assert a CVE id, CVSS or fixed version
i = c.find('the advisories flagged but withheld at 5:06')
ck(i > 0, 'CY: Adobe/Nvidia block missing')
blk = c[i: c.find('</p>', i)]
ck('NO CVE IDENTIFIER, CVSS SCORE OR FIXED VERSION IS ASSERTED' in blk,
   'CY: Adobe/Nvidia block lost its no-identifier disclaimer')
ck(not re.search(r'CVE-\d{4}-\d+', blk), 'CY: a CVE id was invented inside the Adobe/Nvidia block')
ck(not re.search(r'CVSS[^.]{0,20}\d\.\d', blk), 'CY: a CVSS score was invented in the Adobe/Nvidia block')
ck('exploited in the wild' in blk or 'none of these have been exploited' in blk,
   'CY: Adobe non-exploitation statement missing')

# BUG (vi), the real defect: the MiniOrange CVEs were ALREADY in Patch Priority
# with numeric CVSS scores, so a table row saying "no numeric score is asserted"
# put the page in contradiction with itself. The row is gone; assert it stays gone.
ck('<tr><td>CVE-2026-61979 and CVE-2026-15981' not in c,
   'CY: the duplicate MiniOrange CVE row is back')
ck(c.count('CVE-2026-15981') >= 1 and c.count('CVE-2026-61979') >= 1,
   'CY: the MiniOrange CVEs vanished entirely')

# the Gitea/Oracle conflation guard, scoped to <li> rows
for m in re.finditer(r'<li>.*?</li>', c, re.S):
    li = m.group(0)
    if 'CVE-2026-60004' in li:
        ck('Gitea' in li, 'CY: a KEV row names CVE-2026-60004 without Gitea')
        ck('Oracle WebLogic' not in li,
           'CY: CVE-2026-60004 row names Oracle WebLogic (the recurring conflation)')
    if 'CVE-2026-21962' in li:
        ck('Oracle' in li, 'CY: the CVE-2026-21962 row lost Oracle')
        ck('Gitea' not in li, 'CY: Gitea detail leaked into the Oracle row')

# ------------------------------------------------ 7. KEV COUNTDOWNS FROM PRINTED DUE DATES
i = c.find('CISA KEV &amp; federal deadlines')
kev = c[i: c.find('<div class="lab">Sources</div>', i)]
rows = re.findall(r'<li>.*?</li>', kev, re.S)
ck(len(rows) >= 10, 'CY: KEV board has only %d rows' % len(rows))
MON = {m: k + 1 for k, m in enumerate(
    ['January', 'February', 'March', 'April', 'May', 'June', 'July',
     'August', 'September', 'October', 'November', 'December'])}
triples = 0
past_due = 0
for li in rows:
    dm = re.search(r'due\s*(?:<b>)?\s*([A-Z][a-z]{2})[a-z]*\.?(?:&nbsp;|\s)(\d{1,2})(?:,?\s*(\d{4}))?', li)
    if not dm:
        continue
    mon = [k for k in MON if k.startswith(dm.group(1))]
    if not mon:
        continue
    due = datetime.date(int(dm.group(3) or 2026), MON[mon[0]], int(dm.group(2)))
    left = (due - TODAY).days
    txt = re.sub(r'<[^>]+>', ' ', li)
    if left <= 0:
        past_due += 1
        ck(('past due' in txt.lower() or 'overdue' in txt.lower() or '0 days' in txt.lower()),
           'CY: KEV row due %s is past due but not marked' % due)
    else:
        want = '%d day%s left' % (left, '' if left == 1 else 's')
        ck(want in txt, 'CY: KEV row due %s should read "%s"' % (due, want))
    triples += 1
ck(triples >= 10, 'CY: only %d KEV due-date triples parsed' % triples)
ck(past_due >= 1, 'CY: no past-due KEV rows found')

# Patch Priority must name the same CVE and deadline as its KEV row
ck('CVE-2026-21962' in c, 'CY: Patch Priority CVE missing')
i = c.find('Patch priority')
pp = c[i: c.find('<div class="lab">', i + 10)]
ck('CVE-2026-15981' in pp and 'CVE-2026-61979' in pp,
   'CY: Patch Priority box does not name the miniOrange CVEs it leads on')
ck('miniOrange' in pp or 'MiniOrange' in pp, 'CY: Patch Priority box lost the product name')
ck('5.4.5' in pp and '17.0.5' in pp,
   'CY: Patch Priority box must carry BOTH edition fix versions')
ck('free edition' in pp and 'Standard edition' in pp,
   'CY: the two version schemes are not distinguished, so they read as a contradiction')
ck('Neither CVE is in KEV' in pp or 'not in KEV' in pp or 'Neither CVE is in CISA KEV' in pp,
   'CY: Patch Priority box does not state KEV status')
# the box must not silently contradict itself on severity
ck(not ('no numeric score is asserted' in pp and 'CVSS&nbsp;9.8' in pp),
   'CY: Patch Priority both asserts and disclaims a CVSS for the same CVEs')
# and no MiniOrange row may have been left in the CVE table duplicating it
ck('<tr><td>CVE-2026-61979 and CVE-2026-15981' not in c,
   'CY: duplicate MiniOrange table row survived')

# ------------------------------------------------ 8. MMA: CHAMPIONS BOARD, ELEVEN BELTS
m = P['mma-briefing.html']
CHAMPS = [('Heavyweight', 'Tom Aspinall'), ('Light Heavyweight', 'Carlos Ulberg'),
          ('Middleweight', 'Sean Strickland'), ('Welterweight', 'Islam Makhachev'),
          ('Lightweight', 'Justin Gaethje'), ('Featherweight', 'Alexander Volkanovski'),
          ('Bantamweight', 'Petr Yan'), ('Flyweight', 'Joshua Van'),
          ('Shevchenko', 'Valentina Shevchenko'), ('Harrison', 'Kayla Harrison'),
          ('Dern', 'Mackenzie Dern')]
for _, name in CHAMPS:
    ck(name in m, 'MMA: champion %s missing from the page' % name)
# the three historical regressions, by name
ck('Ciryl Gane' in m, 'MMA: interim HW champion missing')
ck(not re.search(r'Light Heavyweight[^<]{0,120}Pereira', m),
   'MMA: Pereira listed as light-heavyweight champion (known regression)')
ci = m.find('Champions board')
ck(ci > 0, 'MMA: champions board section missing')
board = m[ci: ci + 9000]
mi = board.find('Middleweight')
ck(mi > 0 and 'Strickland' in board[mi:mi + 400],
   'MMA: champions-board MW row does not name Strickland')
ck('over Khamzat Chimaev' in board or 'Split decision over Khamzat Chimaev' in board,
   'MMA: Chimaev must appear as the DEFEATED opponent, not the champion')
li = board.find('Light Heavyweight')
ck(li > 0 and 'Ulberg' in board[li:li + 400], 'MMA: champions-board LHW row does not name Ulberg')
ck('featherweight is not vacant' in m.lower() or 'not vacant' in m.lower(),
   'MMA: the featherweight not-vacant note is missing')
ck(not re.search(r'[Ff]eatherweight(?![^<]{0,80}not vacant)[^<]{0,60}\bvacant\b', m),
   'MMA: featherweight described as vacant (known regression)')

# calendar sanity: nothing "upcoming" that has already happened
ck('August&nbsp;29' in m or 'August 29' in m or 'Aug. 29' in m, 'MMA: next card date missing')
ck('Oriental Sports Center' in m, 'MMA: venue missing')
ck('Nurmagomedov' in m and 'Song Yadong' in m, 'MMA: headliner missing')
ck('&minus;500' in m and '&plus;380' in m, 'MMA: headliner odds missing')
ck('thirty-first consecutive edition' in m, 'MMA: champions-board counter not advanced')
# Salkilld trap: correct given name and method
ck('Cody Salkilld' not in m, 'MMA: "Cody Salkilld" trap present')

# ------------------------------------------------ 9. STRUCTURE ON ALL FOUR PAGES
TABS = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html',
        'mma-briefing.html', 'archive.html']
for n, h in P.items():
    for t in TABS:
        ck('href="%s"' % t in h, '%s: nav missing %s' % (n, t))
    for pid in ('edition', 'datestamp', 'updated'):
        ck('id="%s"' % pid in h, '%s: masthead pill %s missing' % (n, pid))
    ck("getElementById('datestamp')" in h, '%s: self-stamp JS missing' % n)
    ck("America/New_York" in h, '%s: self-stamp not Eastern' % n)
    ck('Morning Edition' in h and 'Afternoon Edition' in h, '%s: edition buckets missing' % n)
    if n != 'index.html':
        ck('id="freshline"' in h, '%s: freshline missing' % n)
        ck('class="tldr"' in h, '%s: tldr strip missing' % n)
    # no stale "New" markers from a previous edition
    for stale in ('5:06', '4:36', '4:15', '3:50', '2:44'):
        ck('New &middot; %s' % stale not in h, '%s: stale New marker for %s' % (n, stale))

ck('The Tape' in P['wallstreet-briefing.html'], 'WS: tldr label wrong')
ck('The Wire' in P['cyber-briefing.html'], 'CY: tldr label wrong')
ck('Tale of the Tape' in P['mma-briefing.html'], 'MMA: tldr label wrong')

# ------------------------------------------------ 10. TRADINGVIEW BLOCKS
ck(w.count('embed-widget-single-quote.js') == 3, 'WS: single-quote widget count != 3')
for widget in ('ticker-tape', 'timeline', 'stock-heatmap', 'mini-symbol-overview', 'events'):
    ck('embed-widget-%s.js' % widget in w, 'WS: %s widget missing' % widget)
for sym in ('FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI', 'TVC:USOIL', 'TVC:US10Y'):
    ck(sym in w, 'WS: mandatory tape symbol %s missing' % sym)
ck('id="ufccdn"' in m, 'MMA: countdown element missing')
ck('embed-widget' not in P['index.html'], 'index: live widget present (spec says none)')

# ------------------------------------------------ 11. INDEX CARDS MATCH THEIR PAGES
x = P['index.html']
for cls in ('bcard c-sec', 'bcard c-mkt', 'bcard c-mma'):
    ck(cls in x, 'index: card class %s missing' % cls)
i = x.find('bcard c-sec')
sec = x[i:x.find('</a>', i)]
ck('NVIDIA' in sec and 'Adobe' in sec and 'Nutex Health' in sec and 'ReliaQuest' in sec,
   'index: security card does not match the cyber lead')
ck('cyber-briefing.html' in sec, 'index: security card links elsewhere')
i = x.find('bcard c-mkt')
mkt = x[i:x.find('</a>', i)]
ck('HP Inc' in mkt and '&minus;11%' in mkt, 'index: markets card does not match the WS lead')
ck('wallstreet-briefing.html' in mkt, 'index: markets card links elsewhere')
i = x.find('bcard c-mma')
mma = x[i:x.find('</a>', i)]
ck('Nurmagomedov' in mma, 'index: MMA card does not match the MMA lead')
ck('mma-briefing.html' in mma, 'index: MMA card links elsewhere')

# ------------------------------------------------ 12. TRAP GREPS
HARD = ['Cody Salkilld', 'Shamil Yakhyaev', 'Abdul-Rakhman', 'Fight Night 286',
        '$1.4 trillion', 'Suno']
for n, h in P.items():
    for t in HARD:
        ck(t not in h, '%s: HARD trap "%s" present' % (n, t))

# window-scoped traps: only legal inside their own rejection prose
CTX = {'7,677.24': ('declined to adopt', 'adopted at 2:44', 'four cents below', 'Zacks'),
       '4,637.03': ('reject', 'not published', 'derivation'),
       '30.68': ('reject', 'Tuesday', 'carried forward', 'completed session', 'cache'),
       '122%': ('two years old', 'NONE of it publishes', 'reject', '2024'),
       'Shanghai Indoor Stadium': ('Oriental Sports Center', 'reject', 'primary source',
                                   'the name published here'),
       'Dooho Choi': ('previously rendered', 'correction')}
for n, h in P.items():
    for trap, vocab in CTX.items():
        for mm in re.finditer(re.escape(trap), h):
            win = h[max(0, mm.start() - 600): mm.start() + 600]
            ck(any(v in win for v in vocab),
               '%s: context-only trap "%s" at %d outside its window' % (n, trap, mm.start()))

# ------------------------------------------------ REPORT
print('checks: %d' % checks)
if fails:
    print('FAILURES: %d' % len(fails))
    for f in fails:
        print('  -', f)
    sys.exit(1)
print('0 failures')
