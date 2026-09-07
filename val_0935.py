#!/usr/bin/env python3
"""Run-specific validator, 2026-09-07 ~09:35 ET (fourth run of the day).
Adds checks for: this run's N-able additions, the provenance guard, duplication,
counter decay, structural placement, and the standing champions/regression bans."""
import io, re, sys, datetime, os

D = sys.argv[1] if len(sys.argv) > 1 else '.'
P = {n: io.open(os.path.join(D, n), encoding='utf-8').read()
     for n in ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']}
CY, WS, MM, IX = P['cyber-briefing.html'], P['wallstreet-briefing.html'], P['mma-briefing.html'], P['index.html']
TXT = {k: re.sub(r'<[^>]+>', ' ', v) for k, v in P.items()}

fails, n = [], 0
def chk(cond, msg):
    global n
    n += 1
    if not cond: fails.append(msg)

# ---------------- 1. N-able facts present exactly once where they matter -------------
for tok in ['CVE-2026-86218', 'CVE-2026-86206', 'CVE-2026-86207']:
    chk(tok in CY, 'missing ' + tok)
chk(CY.count('2026.3.1.14') >= 3, 'build string should appear in stat, row, patch priority and card; got %d' % CY.count('2026.3.1.14'))
chk('Hotfix 4' in CY, 'Hotfix 4 missing')
chk('5 September' in CY, 'fix date missing')

# no invented CVSS for the N-able CVEs
for bad in ['86218</td><td class="down"><b>9.', '86218</td><td class="down"><b>10']:
    chk(bad not in CY, 'a numeric CVSS was invented for CVE-2026-86218')
chk('no number published' in CY.lower(), 'the "no numeric score published" caveat is missing')

# the vendor contradiction must be printed, not resolved
chk('no confirmations that this vulnerability has been exploited' in CY, 'public advisory quote missing')
chk('has been observed being exploited in the wild' in CY, 'customer notice quote missing')
chk('contradict' in CY.lower(), 'the contradiction is not named')

# ---------------- 2. duplication guard (the 0917 defect) ----------------------------
for tok in ['N-able patches a pre-auth RCE in N-central',
            'if you run N-able N-central on-premises, apply Hotfix 4 now',
            'the N-able / N-central card below']:
    chk(CY.count(tok) == 1, 'duplicated or missing: %s (%d)' % (tok, CY.count(tok)))
for f, tok in [('cyber-briefing.html', '<div class="tldr">'),
               ('wallstreet-briefing.html', '<div class="tldr">'),
               ('mma-briefing.html', '<div class="tldr">')]:
    chk(P[f].count(tok) == 1, 'tldr count wrong in ' + f)

# ---------------- 3. provenance guard -----------------------------------------------
NEG = ('not requested', 'unreachable', 'carried', 'never', 'returned empty', 'not this one',
       'not consulted', 'no daily-cve aggregator', 'not fetched directly', 'not re-confirmed',
       'nor is any', 'none were', 'none was', 'no viewership', 'no other')
FETCHED_THIS_RUN = ('helpnetsecurity.com/2026/09/07/n-able', 'help net security')
for name, t in TXT.items():
    for m in re.finditer(r'[^.]{0,220}(?:fetch|retriev|request)[a-z]*[^.]{0,140}this run[^.]{0,90}\.', t, re.I):
        s = m.group(0).lower()
        ok = any(x in s for x in NEG) or any(x in s for x in FETCHED_THIS_RUN)
        chk(ok, 'unsupported "fetched this run" claim in %s: %s' % (name, m.group(0).strip()[:150]))

# stale edition-attributed fetches must not claim this run
chk('EnergyNow, fetched this run' not in WS, 'stale EnergyNow fetch claim')
chk('per EnergyNow, fetched directly this run' not in WS, 'stale OPEC+ fetch claim')
chk('fetched directly this run' not in CY.replace(
    'Help Net Security, fetched directly this run', '').replace(
    'was fetched directly this run', '').replace(
    '&mdash; fetched directly this run</a>', ''),
    'a cyber fetch claim other than Help Net Security asserts this run')

# ---------------- 4. counters decay --------------------------------------------------
chk('twenty-second consecutive run without one' in WS, 'VIX counter not advanced')
chk('twenty-first consecutive run without one' not in WS, 'old VIX counter still present')
chk('ninth consecutive run' in WS, 'closes counter not advanced')
chk('eighth consecutive run' not in WS, 'old closes counter still present')

# ---------------- 5. structural placement (the defect this run's read-through caught) -
i = WS.find('third reading arrived this run, landing just below it')
chk(i > 0, 'third WTI reading missing')
chk(WS.count('third reading arrived this run, landing just below it') == 1, 'third WTI reading duplicated')
if i > 0:
    row = WS[WS.rfind('<tr>', 0, i):i]
    chk('WTI' in row or '92.34' in row, 'third WTI reading is not inside the WTI table row')
    # the anchor it follows must be a COMPLETE clause, not a severed one (the orphan trap)
    chk('+48.3% on the year</b>, under its own headline' in row, 'the Trading Economics clause was severed again')
lead_end = WS.find('<h2 class="sec">Movers')
chk(lead_end < 0 or 'third reading arrived this run' not in WS[:lead_end], 'a copy survives in The Lead')
# every page must have balanced divs
for _n, _h in P.items():
    chk(_h.count('<div') - _h.count('</div>') == 0, 'unbalanced divs in ' + _n)

j = MM.find('a clean kick to the liver')
chk(j > 0, 'Paris finish mechanics missing')
chk(MM.count('a clean kick to the liver') == 1, 'finish mechanics duplicated')
chk('&mdash; inside a round. About halfway' not in MM, 'the broken mid-sentence interpolation survives')

# ---------------- 6. markets: verified numbers, and nothing invented -----------------
for tok in ['7,718.60', '26,506.99', '53,414.25', '271.86', '162,000', '53,000', '$91.48', '$96.28']:
    chk(tok in WS, 'verified markets figure missing: ' + tok)
chk('53,686.11 &minus; 271.86 = 53,414.25' in WS, 'Dow arithmetic assertion missing')
chk('$91.98' in WS, 'this run\'s WTI reading missing')
# The withdrawn 9.3% may survive ONLY inside the sentence that explains its withdrawal.
# A forbidden-token check must be scoped to where the token would be a defect (standing rule, 9:17 run).
_brent_i = WS.find('<td>Brent crude</td>')
_brent_row = WS[_brent_i:WS.find('</tr>', _brent_i)] if _brent_i > 0 else ''
chk('9.3%' not in _brent_row, '9.3% is back inside the Brent row')
for m in re.finditer(r'[^.]{0,240}9\.3%[^.]{0,160}\.', TXT['wallstreet-briefing.html']):
    s = m.group(0).lower()
    chk('withdraw' in s or 'comes off' in s or 'no longer' in s or 'none corroborates' in s,
        '9.3% appears outside its withdrawal sentence')
chk('Not asserted' in WS or 'not asserted' in WS, '10-year refusal language missing')
chk('after hours' not in TXT['wallstreet-briefing.html'].lower() or 'After-Hours Movers' not in WS,
    'an after-hours block exists on a day with no session')
# Labor Day framing
chk('Labor Day' in WS and '9:30 AM ET' in WS and 'Tuesday 8 September' in WS, 'Labor Day reopen framing missing')

# ---------------- 7. MMA champions board: the standing bans --------------------------
CHAMPS = [('Heavyweight', 'Tom Aspinall'), ('Interim Heavyweight', 'Ciryl Gane'),
          ('Light Heavyweight', 'Carlos Ulberg'), ('Middleweight', 'Sean Strickland'),
          ('Welterweight', 'Islam Makhachev'), ('Lightweight', 'Justin Gaethje'),
          ('Featherweight', 'Alexander Volkanovski'), ('Bantamweight', 'Petr Yan'),
          ('Flyweight', 'Joshua Van'), ('Shevchenko', 'Valentina Shevchenko'),
          ('Harrison', 'Kayla Harrison'), ('Dern', 'Mackenzie Dern')]
tbl_i = MM.find('<th>Division</th>')
tbl = MM[tbl_i:MM.find('</table>', tbl_i)] if tbl_i > 0 else ''
chk(tbl_i > 0, 'champions table not found')
chk(tbl.count('<tr>') == 12, 'champions table should have exactly 12 division rows, got %d' % tbl.count('<tr>'))
for _, name in CHAMPS:
    chk(name in tbl, 'champion missing from board: ' + name)
# the four known regressions must never sit in the champion column
for bad in ['<b>Alex Pereira</b>', '<b>Khamzat Chimaev</b>', '<b>Ilia Topuria</b>',
            '<b>Alexandre Pantoja</b>', '<b>Merab Dvalishvili</b>']:
    chk(bad not in tbl, 'REGRESSION: %s is in the champion column' % bad)
_champ_cells = re.findall(r'<td><b>(.*?)</b>', tbl)
chk(not any('vacant' in c.lower() for c in _champ_cells), 'a belt is listed vacant in the champion column')
chk(len(_champ_cells) == 12, 'expected 12 champion cells, got %d' % len(_champ_cells))
chk('Carried, not re-confirmed this run.</td>' not in MM, 'Shevchenko row was not upgraded')
chk('14 Sep 2024' in MM and '2 defences' in MM, 'Shevchenko detail missing')

# no ranking asserted for Hooker
chk('No ranking is asserted for Hooker' in MM, 'Hooker ranking refusal missing')
_mmt = TXT['mma-briefing.html']
for m in re.finditer(r'[^.]{0,180}Hooker[^.]{0,60}(?:No\.|#)\s*1[02]\b[^.]{0,120}\.', _mmt):
    s = m.group(0).lower()
    chk('disagree' in s or 'no longer asserted' in s or 'withdrawn' in s or 'neither' in s or 'not asserted' in s,
        'a Hooker ranking number is asserted outside the refusal: ' + m.group(0).strip()[:120])

# ---------------- 8. New-tag hygiene -------------------------------------------------
chk(CY.count('>New</span>') == 1, 'cyber should carry exactly 1 New tag, has %d' % CY.count('>New</span>'))
chk(WS.count('>New</span>') == 0, 'wall street should carry 0 New tags')
chk(MM.count('>New</span>') == 0, 'MMA should carry 0 New tags')
chk('Cyber carries 1 New tag this edition; Wall Street 0; MMA 0.' in CY, 'New-tag ledger line wrong')
prev = os.path.join(D, 'archive', 'cyber-2026-09-07-0917.html')
if os.path.exists(prev):
    p = io.open(prev, encoding='utf-8').read()
    for tok in ['N-able', 'N-central', '86218']:
        chk(tok not in p, 'New tag unjustified: %s already in the 0917 snapshot' % tok)

# ---------------- 9. KEV countdowns still arithmetically right -----------------------
today = datetime.date(2026, 9, 7)
for due, txt in [(datetime.date(2026, 9, 18), '11 days'), (datetime.date(2026, 9, 16), '9 days')]:
    chk((due - today).days == int(txt.split()[0]), 'countdown arithmetic wrong for %s' % due)
    chk(txt in CY, 'countdown text missing: ' + txt)
chk('no CISA addition exists for 5, 6 or 7 September' in CY or 'no 5, 6 or 7 September addition' in CY.replace('&nbsp;',' ')
    or 'no 5, 6 or 7\nSeptember addition exists' in CY, 'KEV no-addition statement missing')

# ---------------- 10. every page: chrome, nav, stamps, disclaimer --------------------
for name, h in P.items():
    for tab in ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html', 'archive.html']:
        chk('href="%s"' % tab in h, '%s missing nav link to %s' % (name, tab))
    for el in ['id="edition"', 'id="datestamp"', 'id="updated"', 'id="freshline"']:
        chk(el in h, '%s missing %s' % (name, el))
    chk('briefings refresh every 30 minutes' in h, '%s missing freshness script text' % name)
    chk('America/New_York' in h, '%s missing ET stamp script' % name)
for name in ['cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']:
    chk('<div class="disc">' in P[name], '%s missing disclaimer block' % name)
    chk('<h2 class="sec">Sources</h2>' in P[name], '%s missing sources footer' % name)
chk('Nothing here is investment advice' in WS, 'markets disclaimer text missing')
chk('subject to change' in MM, 'MMA disclaimer text missing')

# ---------------- 11. wall street live widgets -------------------------------------
for w in ['embed-widget-ticker-tape.js', 'embed-widget-single-quote.js', 'embed-widget-timeline.js',
          'embed-widget-stock-heatmap.js', 'embed-widget-mini-symbol-overview.js', 'embed-widget-events.js']:
    chk(w in WS, 'missing live widget: ' + w)
chk(WS.count('embed-widget-single-quote.js') == 3, 'should be exactly 3 single-quote widgets')
for sym in ['FOREXCOM:SPXUSD', 'FOREXCOM:NSXUSD', 'FOREXCOM:DJI', 'TVC:USOIL', 'TVC:US10Y']:
    chk(sym in WS, 'ticker tape missing ' + sym)
chk('id="ufccdn"' in MM, 'MMA countdown element missing')
chk(IX.count('tradingview.com') == 0, 'index must carry no live widgets')

# ---------------- 12. index cards mirror the three summaries ------------------------
def tldr(h):
    m = re.search(r'<div class="tldr"><b>[^<]*</b>\s*<span>(.*?)</span></div>', h, re.S)
    return m.group(1) if m else None
for h in [CY, WS, MM]:
    t = tldr(h)
    chk(t is not None, 'a briefing has no parseable tldr')
    if t: chk(t in IX, 'index card does not mirror a briefing summary: %s' % t[:70])

print('checks:', n)
if fails:
    print('FAILURES (%d):' % len(fails))
    for f in fails: print('  -', f)
    sys.exit(1)
print('ALL PASS')
