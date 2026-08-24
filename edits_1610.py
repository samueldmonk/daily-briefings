#!/usr/bin/env python3
"""Afternoon (post-close) edition edits — 2026-08-24 ~4:10pm ET."""
import io, sys, re

def rw(p, pairs):
    h = io.open(p, encoding='utf-8').read()
    for i, (old, new) in enumerate(pairs):
        if old not in h:
            print('  !! MISS #%d in %s: %r' % (i, p, old[:90])); sys.exit(1)
        if h.count(old) != 1:
            print('  !! NOT UNIQUE #%d in %s (%d): %r' % (i, p, h.count(old), old[:90])); sys.exit(1)
        h = h.replace(old, new)
    io.open(p, 'w', encoding='utf-8').write(h)
    print('  ok %s (%d edits)' % (p, len(pairs)))

# ───────────────────────── WALL STREET ─────────────────────────
WS_TLDR = ('The session is over and the split held to the bell: the Dow closed higher for the day while the '
    'S&amp;P&nbsp;500 and the Nasdaq Composite finished lower, dragged by a memory-chip selloff set off by weekend '
    'reports that Washington may let Apple buy Chinese DRAM and NAND &mdash; the Nasdaq Composite ended at '
    '<b>25,980.19, down 0.76%</b>, the S&amp;P&nbsp;500 fell about <b>0.28%</b> and the Dow rose about '
    '<b>0.26%</b> on roughly 140 points, with Treasury&rsquo;s &ldquo;Operation Economic Outcast&rdquo; sanctions '
    'on Iran and a 50% tariff threat against Canadian autos framing a week that still has July PCE and Nvidia&rsquo;s '
    'results on Wednesday and Kevin Warsh at Jackson Hole on Friday.')

WS_LEAD_H2 = ('The bell finally settles it: the Dow up, the S&amp;P 500 and Nasdaq down, and memory chips the reason')

WS_LEAD_P1 = ('<p><b>At the closing bell, roughly 4:10&nbsp;p.m. ET.</b> After twelve consecutive editions of '
    'withholding index levels because every quote board this desk checked was stale, the close is finally '
    'available and it is <b>corroborated</b>. Two independent post-close prints fetched this run agree on the '
    'shape and on the arithmetic: the <b>Nasdaq Composite closed at 25,980.19, down 200.27 points or 0.76%</b>; '
    'the <b>S&amp;P 500 fell about 0.28%</b>; and the <b>Dow Jones Industrial Average rose about 0.26%</b> on a '
    'gain of roughly 140 points. Each of those changes reconciles <em>exactly</em> against Friday&rsquo;s verified '
    'closes of 7,674.37, 53,277.01 and 26,180.46, which is the arithmetic test this desk applies before publishing '
    'anything. The Nasdaq level is carried here because both prints give it identically. The S&amp;P 500 and Dow '
    'levels are <b>not</b> asserted to the cent: one print closes the S&amp;P at 7,652.96 on a 21.41-point loss and '
    'the Dow at 53,416.99 on a 139.98-point gain, the other at 7,652.86 and 53,417.16 on a 140.15-point gain. Both '
    'are internally consistent, they differ by about a dime, and until a single figure is corroborated this page '
    'publishes the percentage move and shows the spread rather than picking a winner. <b>Direction, magnitude and '
    'cause are not in doubt; the last decimal place is.</b> The move deepened into the close &mdash; Reuters had the '
    'Nasdaq off 0.38% at 11:55&nbsp;a.m. ET and 0.57% at 2:02&nbsp;p.m., against 0.76% at the bell &mdash; so the '
    'selling did not exhaust itself in the morning. <b>The Friday-close trap fired for a twelfth consecutive run</b>: '
    'a search summary this run again returned Friday&rsquo;s 7,674.37 / 53,277.01 / 26,180.46 as though they were '
    'Monday&rsquo;s close. They are not, and they remain confined to the Weekly Scorecard. <b>Yahoo Finance served a '
    'cached page for an eighth time</b>, its strip reading &ldquo;U.S. markets open in 5h 6m&rdquo; &mdash; the open '
    'anchor, 9:30 minus 5h06m, dating it to about 4:24&nbsp;a.m. ET &mdash; alongside pre-open futures and a trending '
    'rail still carrying Friday&rsquo;s Alibaba decline. Nothing from it is published here.</p>\n'
    '<p><b>The cause was memory, and it had a name attached.</b> 24/7&nbsp;Wall&nbsp;St. reported at 11:29&nbsp;a.m. ET '
    'that the group sold off on weekend reports Washington may permit Apple to source DRAM from China&rsquo;s '
    'ChangXin Memory Technologies (CXMT) and NAND flash from Yangtze Memory Technologies (YMTC), described as a '
    'possible diplomatic gesture ahead of President Xi Jinping&rsquo;s planned US visit, expected on or around '
    'September&nbsp;24. <b>No policy decision has been announced</b>, and Commerce Secretary Howard Lutnick told the '
    '<em>Wall Street Journal</em> on August 17 that &ldquo;it&rsquo;s not great American companies using Chinese '
    'memory.&rdquo; Both CXMT and YMTC remain on the Pentagon&rsquo;s Section 1260H list. The tape traded it anyway: '
    '<b>SanDisk fell 9% to $1,458.29</b> in the morning and was put at roughly 10% down in an afternoon summary, '
    '<b>Micron 7% to $897.86</b>, <b>Western Digital 7% to $429.49</b> and <b>SK hynix 5% to $154.48</b>, with the '
    'Roundhill Memory ETF off 7% at $53.62 &mdash; a uniformity that says traders were not sorting NAND exposure from '
    'DRAM exposure. KC Rajkumar of Lynx Equity Research called it &ldquo;an overreaction,&rdquo; finding CXMT '
    'qualified for only one low-volume Mac product and not for iPhones at all, and YMTC not qualified by Apple for any '
    'product and allocating its latest NAND to domestic customers. Context for the size of the gap: SanDisk was up '
    '572% year to date through Friday&rsquo;s close and Micron up 239%. Reuters put the Philadelphia SE Semiconductor '
    'index down <b>2.64%</b> to a three-week low, with <b>Nvidia &minus;2.03%</b>, <b>Micron &minus;5.76%</b> and '
    '<b>Broadcom &minus;1.74%</b> at 11:55&nbsp;a.m. ET, while <b>financials rose 1.19%</b> &mdash; JPMorgan '
    '+1.49%, Visa +2.64% &mdash; and kept the Dow afloat. That is the whole session in one line: one sector down hard, '
    'one sector up, and the index you looked at decided what kind of day you thought it was.</p>')

WS_MOVERS_LAB = 'Movers &amp; drivers — at the closing bell'

WS_NEW_CARD = '''<div class="card">
<div class="tags"><span class="tag">Closing bell</span><span class="tag down">Breadth negative</span><span class="tag new">New</span></div>
<h3>Under the flat headline, more stocks fell than rose &mdash; and the auto tariff hit the tape hard</h3>
<p><b>New this edition.</b> The index numbers make Monday look like a non-event. The internals do not. Reuters reported that <b>declining issues outnumbered advancers by 1.14-to-1 on the NYSE and by 1.38-to-1 on the Nasdaq</b>, and the new-highs/new-lows split tells the same story from the other end: the S&amp;P 500 posted <b>16 new 52-week highs against six new lows</b>, but the Nasdaq Composite posted <b>62 new highs against 70 new lows</b> &mdash; more names making twelve-month lows than highs on a day the composite fell less than a percent. A late-session sector board from Stock Market Watch had <b>consumer staples +1.30%</b>, <b>communication services +0.99%</b> and <b>financials +0.96%</b> against <b>technology &minus;1.47%</b> with semiconductors <b>&minus;2.23%</b>, and <b>energy the worst sector at &minus;1.00%</b> on softer crude &mdash; a defensive rotation rather than a broad bid. The second driver was trade. President Trump warned that tariffs on cars, trucks and automotive parts from Canada would rise to <b>50% starting January 1</b> after talks collapsed over the weekend, and the affected names moved on it: Reuters had <b>Ford &minus;3.9%</b> and <b>General Motors &minus;1.9%</b>, with 24/7&nbsp;Wall&nbsp;St. reporting Ford and Stellantis both down about 4%, and trucking took it worse still &mdash; <b>J.B. Hunt Transport slipped about 5.4%</b> on Reuters&rsquo; read and finished on 24/7&rsquo;s losers board at &minus;6.55% ($257.42). Elsewhere on that board: <b>Coterra Energy &minus;8.62%</b> ($32.56), <b>Seagate Technology &minus;6.79%</b> ($792.30) and <b>Western Digital &minus;6.45%</b> ($429.82); the gainers were <b>Expedia +4.45%</b> ($335.93), <b>Altria +3.98%</b> ($68.72), <b>Verisign +3.40%</b> ($291.39) and <b>GoDaddy +3.03%</b> ($100.01). An afternoon summary separately put <b>Monster Beverage +2.3%</b> after record second-quarter 2026 results and <b>Booking Holdings +2.24%</b>, and 24/7 reported <b>Moderna &minus;7%</b> on profit-taking against a 392% year-to-date run, with BioNTech off 4%. One caution carried forward: the Stock Market Watch board has now repeated a byte-identical table across several runs and is treated here as frozen, so its sector percentages are read as a late-session snapshot rather than a certified closing print.</p>
</div>

'''

WS_CHART_LAB = 'Chart of the day — SanDisk (SNDK)'
WS_CHART_SYM = '{"symbol":"NASDAQ:SNDK","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}'
WS_CHART_NOTE = ('The chart moves to <b>SanDisk</b> for the closing edition, because it is the single name that best '
    'explains the day. It led the memory complex lower on the Apple/China sourcing reports &mdash; 24/7&nbsp;Wall&nbsp;St. '
    'put it <b>down 9% at $1,458.29</b> at 11:29&nbsp;a.m. ET and an afternoon summary put it at roughly <b>10%</b> down '
    '&mdash; and it is the mechanism by which a policy rumour about an iPhone bill of materials became a drag on the '
    'Nasdaq Composite. It is also the clearest illustration of why the move was violent: SanDisk was <b>up 572% year to '
    'date through Friday&rsquo;s close</b>, so a headline that merely raises the possibility of a new low-cost supplier '
    'lands on a position with a very long way to fall. Applied Optoelectronics, which held this slot at the previous '
    'edition on an 11% morning drop after a $600&nbsp;million equity offering, remains a real decline but a company-specific '
    'one; SanDisk is the sector story. Note the arithmetic honestly: the &minus;9% and &minus;10% readings are from '
    'different moments of the session, not a contradiction, and no closing print for the name was corroborated this run.')

WS_SCORE_ADD = '''<div class="lab">Monday&rsquo;s close — August 24</div>
<div class="panel" style="padding:6px 8px">
<table>
<tr><th>Index</th><th>Close</th><th>Change</th><th>%</th></tr>
<tr><td>Nasdaq Composite</td><td>25,980.19</td><td class="down">&minus;200.27</td><td class="down">&minus;0.76%</td></tr>
<tr><td>S&amp;P 500</td><td>7,652.96 / 7,652.86 <span class="tag">two prints</span></td><td class="down">&minus;21.41</td><td class="down">&minus;0.28%</td></tr>
<tr><td>Dow Jones Industrial Average</td><td>53,416.99 / 53,417.16 <span class="tag">two prints</span></td><td class="up">+139.98 / +140.15</td><td class="up">+0.26%</td></tr>
</table>
</div>
<div class="note"><b>How to read this table.</b> Monday&rsquo;s close is now official and is published here for the first time. The Nasdaq Composite level is asserted because two independent post-close prints fetched this run give it identically. The S&amp;P 500 and Dow levels are shown as a pair because those same two prints differ by about a dime; each pair is internally consistent &mdash; every level plus or minus its stated point change returns Friday&rsquo;s verified close exactly &mdash; so this is a vendor rounding or settlement-print difference, not a stale figure. The percentage moves are agreed by both and are what the editorial above relies on. A third, earlier reading fetched this run had the S&amp;P &minus;0.24%, the Dow +0.25% and the Nasdaq &minus;0.55%; it is treated as a late-session rather than a closing print, since the two closing prints agree with each other and it does not agree with either.</div>
</section>

<section>
'''

WS_AFTERHOURS = '''<section>
<div class="lab">After-hours movers</div>
<div class="panel" style="padding:12px 15px">
<p style="margin:0;font-size:14.5px;line-height:1.6"><b>No after-hours moves are published this edition, because none could be sourced.</b> The extended session opened at 4:00&nbsp;p.m. ET and this edition was built from roughly 4:05&nbsp;p.m., so the window is minutes old. The dedicated after-hours board this desk checked (StockAnalysis.com&rsquo;s 4:00&nbsp;p.m.&ndash;8:00&nbsp;p.m. movers page) was fetched this run and was still serving <b>August 21</b> data &mdash; its own heading read &ldquo;Stock Indexes &mdash; Aug 21, 2026 &mdash; After-hours&rdquo; and both its gainers and losers tables were stamped &ldquo;Updated Aug 21, 2026&rdquo; &mdash; so it had not yet rolled over to Monday. Publishing Friday&rsquo;s extended-hours names as tonight&rsquo;s would be exactly the cached-board error this page has spent the day refusing to make, so nothing from it is carried. There is also little reason to expect much: no large-capitalisation earnings were scheduled for Monday evening. <b>The event this desk is waiting on is Wednesday</b> &mdash; Nvidia reports fiscal Q2 after the bell, with July PCE the same morning &mdash; and Marvell follows on Thursday. Verified after-hours moves, if any develop, will be carried at the next edition.</p>
</div>
</section>

'''

rw('wallstreet-briefing.html', [
 # 1. tldr
 ('<div class="tldr"><b>The Tape</b> <span>With about twenty minutes of regular trading left the shape of the session has not changed',
  '<div class="tldr"><b>The Tape</b> <span>%%WSTLDR%%<!--x'),
 ('with The Motley Fool frozen for a fifth consecutive run and Yahoo Finance cached for a seventh; the one thing that did move is the Iran story, where Treasury named the shadow-fleet network it is sanctioning and Tehran&rsquo;s new security chief answered with a threat to the tanker lanes.</span></div>',
  'x--></span></div>'),
 # 2. lead headline
 ('<h2>Twenty minutes from the bell, the tape is unchanged &mdash; and the freshest reading available is forty minutes old</h2>',
  '<h2>' + WS_LEAD_H2 + '</h2>'),
 # 3. lead paragraph 1 (replace opener through the AAOI sentence end)
 ('<p><b>As of roughly 3:38 p.m. ET.</b> With about twenty minutes of regular trading left',
  WS_LEAD_P1 + '\n<!--OLDLEAD <p>x'),
 ('after the company announced a $600&nbsp;million equity offering.</p>\n<p>The event risk has come off the podium.',
  'OLDLEAD-->\n<p>The event risk has come off the podium.'),
 # 4. movers label
 ('<div class="lab">Movers &amp; drivers — the overnight tape and the late morning</div>\n<div class="cards">\n\n',
  '<div class="lab">' + WS_MOVERS_LAB + '</div>\n<div class="cards">\n\n' + WS_NEW_CARD),
 # 5. drop previous New tag (Iran card)
 ('<span class="tag">Iran</span><span class="tag down">Hormuz risk</span><span class="tag new">New</span>',
  '<span class="tag">Iran</span><span class="tag down">Hormuz risk</span>'),
 ('<h3>The sanctions package now has names attached &mdash; and Tehran has answered with a threat to the tanker lanes</h3>\n<p><b>New this edition.</b> NPR',
  '<h3>The sanctions package now has names attached &mdash; and Tehran has answered with a threat to the tanker lanes</h3>\n<p><b>Carried from the previous edition.</b> NPR'),
 # 6. chart of the day
 ('<div class="lab">Chart of the day — Applied Optoelectronics (AAOI)</div>',
  '<div class="lab">' + WS_CHART_LAB + '</div>'),
 ('{"symbol":"NASDAQ:AAOI","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}',
  WS_CHART_SYM),
 ('<div class="note">The chart moves back to Applied Optoelectronics this edition, and this time with a live source and a named cause.',
  '<div class="note">%%WSCHART%%<!--y'),
 ('after a $500&nbsp;million raise in April and a $600&nbsp;million ATM programme in May.</div>',
  'y--></div>'),
 # 7. weekly scorecard: prepend Monday close block
 ('<div class="lab">Weekly scorecard — official closes, Friday August 21</div>',
  WS_SCORE_ADD + '<div class="lab">Weekly scorecard — official closes, Friday August 21</div>'),
 (' No After-Hours Movers section appears in this edition &mdash; the regular session is under way, not finished.</div>',
  ' Monday&rsquo;s official close now appears in its own table above.</div>'),
 # 8. after-hours section, inserted before Weekly scorecard section wrapper
 ('<section>\n<div class="lab">Monday&rsquo;s close — August 24</div>',
  WS_AFTERHOURS + '<section>\n<div class="lab">Monday&rsquo;s close — August 24</div>'),
])

# splice the long strings (avoids quoting collisions above)
h = io.open('wallstreet-briefing.html', encoding='utf-8').read()
h = re.sub(r'%%WSTLDR%%<!--x.*?x-->', WS_TLDR, h, flags=re.S)
h = re.sub(r'%%WSCHART%%<!--y.*?y-->', WS_CHART_NOTE, h, flags=re.S)
h = re.sub(r'<!--OLDLEAD <p>x.*?OLDLEAD-->\n', '', h, flags=re.S)
io.open('wallstreet-briefing.html', 'w', encoding='utf-8').write(h)
print('  ok wallstreet splices')

# ───────────────────────── CYBER ─────────────────────────
CY_TLDR_TAIL = ('&mdash; while CISA&rsquo;s remediation deadline for an actively exploited Zimbra command-injection '
  'flaw falls today with Shadowserver already counting more than 270 compromised servers, eight other Known '
  'Exploited Vulnerabilities entries tracked here are already past due, and a single Joomla extension has just '
  'produced six of the weekend&rsquo;s twelve critical CVEs &mdash; four of them scored a maximum 10.0, all '
  'unauthenticated, and none with a patch listed at disclosure.</span></div>')

CY_ROWS = '''<tr><td>CVE-2026-76604 <span class="tag new">New</span><br>CVE-2026-76605<br>CVE-2026-76606<br>CVE-2026-76607</td><td>10.0<br>(each)</td><td>Fabrik extension for Joomla &mdash; <b>no patch information was available at disclosure</b></td><td><b>New this edition.</b> Four maximum-severity flaws in a single Joomla extension, all disclosed August 22, 2026 and all rated <b>CVSS 10.0</b> with the same worst-case profile: <b>network reachable, no privileges, no user interaction</b>. CVE-2026-76604 is unauthenticated remote code execution through improper control of code generation in the PHP form element; CVE-2026-76605 is remote code execution through the image element; CVE-2026-76606 is a path traversal in the image element allowing unauthenticated file access or manipulation; CVE-2026-76607 is a missing access-control check in the download element. Fabrik accounts for <b>six of the twelve critical (CVSS 9.0+) CVEs published that day</b>, and the wider cluster adds CVE-2026-77992 (9.5, code injection via a heredoc terminator breakout in the calc element plus a missing access control on the <code>onUpdateComment</code> endpoint), CVE-2026-76571 and CVE-2026-76602 (9.3 each, unauthenticated SQL injection in the list filter condition and list model order parameters) and four further access-control and cross-site-scripting issues at 8.6&ndash;8.7. <b>Patch availability across the disclosed set was recorded as 0% at collection time</b>, so the practical control is exposure reduction: audit Joomla installations for the Fabrik extension, restrict administrative interfaces to trusted networks and raise logging on the affected endpoints until the vendor ships a fix. <b>None of these is a KEV entry and none carries a federal deadline</b>, and no in-the-wild exploitation has been reported &mdash; but an unauthenticated 10.0 in a widely deployed CMS extension is the profile that historically reaches the KEV catalogue quickly.</td></tr>

<tr><td>CVE-2026-77946<br>CVE-2026-78050</td><td>10.0<br>9.9</td><td>TRENDnet TEW-821DAP access point; Comfast CF-N1-S</td><td>Two internet-facing SOHO network devices disclosed the same day. CVE-2026-77946 is a stack-based buffer overflow in the TRENDnet TEW-821DAP NTP Timezone Configuration Handler, reachable by unauthenticated remote attackers via crafted NTP server configuration parameters, and is rated <b>10.0</b>; CVE-2026-78050 is a stack-based buffer overflow in the Comfast CF-N1-S web management interface via the <code>timestr</code> or <code>ntp_client_enabled</code> arguments, rated <b>9.9</b> and requiring only low privileges. A related TRENDnet issue, CVE-2026-77945 (7.4), allows authenticated command injection via the <code>ssi</code> interface. No patch information was listed at disclosure for the critical pair. Neither is a KEV entry. The pattern is the point: alongside the Joomla cluster, the weekend&rsquo;s critical set was dominated by web application components and edge hardware &mdash; the two categories that favour unauthenticated remote access as the primary attack path.</td></tr>

'''

rw('cyber-briefing.html', [
 ('eight other Known Exploited Vulnerabilities entries tracked here are already past due, and researchers have named two fresh loaders, WordlistLoader and SynkLoader, that look built to sell access on to ransomware crews.</span></div>',
  '%%CYTAIL%%'),
 ('<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>\n\n<tr><td>CVE-2026-58231</td>',
  '<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>\n\n' + CY_ROWS + '<tr><td>CVE-2026-58231</td>'),
])
h = io.open('cyber-briefing.html', encoding='utf-8').read()
h = h.replace('%%CYTAIL%%', CY_TLDR_TAIL)
io.open('cyber-briefing.html', 'w', encoding='utf-8').write(h)
print('  ok cyber splices')

# ───────────────────────── INDEX ─────────────────────────
IDX_MKT_H2 = 'The bell settles it &mdash; Dow up, S&amp;P and Nasdaq down, memory chips the reason'
IDX_SEC_H2 = 'Iran-linked hackers took a UK power plant offline for four days'

rw('index.html', [
 ('<h2>Quiet indexes, restless risk gauges &mdash; and a sixth cached page</h2>\n<p>With about twenty minutes of regular trading left the shape of the session has not changed &mdash; the Dow higher, the S&amp;P 500 and the Nasdaq Composite lower on semiconductor weakness &mdash; and no source fetched this run carried a reading newer than roughly 3&nbsp;p.m. ET, with The Motley Fool frozen for a fifth consecutive run and Yahoo Finance cached for a seventh; the one thing that did move is the Iran story, where Treasury named the shadow-fleet network it is sanctioning and Tehran&rsquo;s new security chief answered with a threat to the tanker lanes.</p>',
  '<h2>' + IDX_MKT_H2 + '</h2>\n<p>%%IDXWS%%</p>'),
 ('eight other Known Exploited Vulnerabilities entries tracked here are already past due, and researchers have named two fresh loaders, WordlistLoader and SynkLoader, that look built to sell access on to ransomware crews.</p>',
  '%%IDXCY%%</p>'),
])
h = io.open('index.html', encoding='utf-8').read()
h = h.replace('%%IDXWS%%', WS_TLDR)
h = h.replace('%%IDXCY%%', CY_TLDR_TAIL.replace('</span></div>', ''))
io.open('index.html', 'w', encoding='utf-8').write(h)
print('  ok index splices')
print('DONE')
