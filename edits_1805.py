#!/usr/bin/env python3
# 6:05 PM ET Aug 31 2026 — AFTERNOON EDITION, post-close, TENTH run of the day.
# Targeted edits onto the 5:35 pages. Every claim below traces to a source fetched THIS run.
import os, re, sys
D = os.path.dirname(os.path.abspath(__file__))
def rd(p): return open(os.path.join(D,p),encoding='utf-8').read()
def wr(p,h): open(os.path.join(D,p),'w',encoding='utf-8').write(h)

N = '<span class="tag new">New &middot; 6:05 PM</span>'
report = []

# ── 0. demote every marker stamped earlier than this run ────────────────────
for p in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    h = rd(p); n = 0
    for t in re.findall(r'<span class="tag new">New &middot; ([^<]+)</span>', h):
        if t != '6:05 PM':
            a='<span class="tag new">New &middot; %s</span>'%t; b='<span class="tag">Carried &middot; Aug 31, %s</span>'%t
            n += h.count(a); h = h.replace(a,b)
    for t in set(re.findall(r'&#9679; New &middot; ([0-9:]+ ?[AP]?M?)', h)):
        if not t.startswith('6:05'):
            a='&#9679; New &middot; '+t; b='&#9679; '+t
            n += h.count(a); h = h.replace(a,b)
    wr(p,h); report.append('%-24s demoted %d stale New markers' % (p,n))

# ═══ WALL STREET ════════════════════════════════════════════════════════════
h = rd('wallstreet-briefing.html')

lead = ('<div class="note" style="margin-bottom:14px">' + N +
 ' <b>Five separate reads of this close now agree, and the month’s gain has stopped being an adjective and become a pair of numbers.</b> '
 'Reporting fetched this run repeats the official close unchanged for a fifth consecutive time — <b>S&amp;P 500 7,686.14, &minus;0.33%</b>; '
 '<b>Nasdaq Composite 26,370.89, &minus;0.12%</b>; <b>Dow Jones Industrial Average 53,185.90, &minus;374.09, &minus;0.70%</b> — with the cause stated the same way each time: '
 '<b>stocks fell after the U.S. and Iran traded fire for the first time in a month</b>. '
 '&#9888; <b>The new part is the month.</b> The same reporting states the <b>S&amp;P 500 gained more than 2.5% for August and the Nasdaq rose more than 3%</b>. '
 '<b>This page already carried +2.6% and +3.9% from a different source</b>; a floor of &ldquo;more than 2.5%&rdquo; and &ldquo;more than 3%&rdquo; <b>contains both figures rather than competing with them</b>, '
 'so the precise pair stands and the floor is recorded as corroboration.<br><br>'
 '&#9888; <b>The 10-year finally reconciles inside a single quoted range, which retires a discrepancy this page carried all afternoon.</b> '
 'A rates read fetched this run gives the <b>previous close at 4.722%</b> with a <b>day’s range of 4.697% to 4.767%</b>. '
 '<b>That range high is what &ldquo;topped 4.75%, highest since January 2025&rdquo; was describing, and 4.722% is where the day settled.</b> '
 '<b>The two figures this page printed as &ldquo;one path, not two claims&rdquo; are now provably one path</b> — the intraday high and the closing mark are the endpoints of the same quoted band. '
 '<b>No source is overturned; the gap simply closed.</b><br><br>'
 '<b>The utilities rout acquires a price and a record.</b> <b>Edison International fell 23% to $54.22, its largest single-day decline in more than 25 years</b>, per reporting fetched this run; '
 'a sector wrap fetched alongside it puts the same move at <b>more than 22% and calls it the largest one-day decline since 2001</b>. '
 '&#9888; <b>&ldquo;More than 25 years&rdquo; and &ldquo;since 2001&rdquo; are the same claim measured from either end of the same window</b> — both are printed, neither is adopted over the other. '
 '<b>The trigger is stated more exactly than before: California lawmakers stopped Governor Gavin Newsom’s plan to insulate utilities from insurer lawsuits over wildfires</b>, '
 'and <b>Mizuho analysts told clients investors are better positioned in utilities with few wildfire-liability issues</b> — the first named downgrade rationale this page has carried on the move.</div>')
h = h.replace('<h2 class="sec">The Lead</h2>', '<h2 class="sec">The Lead</h2>'+lead, 1)

sect = ('<div class="note" style="margin-bottom:14px">' + N +
 ' <b>The sector split now has three numbers instead of two directions.</b> A sector wrap fetched this run reports <b>Energy as the only S&amp;P 500 sector in positive territory, up about 2% on the day and more than 6% for August</b>, '
 'lifted by crude and by <b>Chevron and Exxon</b>; <b>Utilities down 1.6%</b> as one of the two biggest laggards; and <b>Technology roughly flat against a broadly lower market, with software and semiconductors edging higher</b>. '
 '&#9888; <b>The energy figure is described as a morning reading and the utilities figure as a day figure</b> — they are not the same clock and are not presented as a single snapshot. '
 '<b>The live heat map below is the authority on where the sectors finished.</b></div>')
i = h.find('<h2 class="sec">Sector Heat &mdash; live</h2>')
if i>=0:
    j = h.index('</h2>', i)+5
    h = h[:j] + sect + h[j:]

ah = ('<div class="note" style="margin-bottom:14px">' + N +
 ' <b>Thirty minutes on, the screen that turned over and turned back has simply held — and a held screen is the first stable after-hours reading of the evening.</b> '
 'The screen fetched this run returns <b>Antelope Enterprise Holdings (AEHL) +84.75%</b>, <b>Australian Oilseeds Holdings (COOT) +58.50%</b> and <b>One and One Green Technologies (YDDL) +41.82%</b> among gainers, '
 'and <b>Zentek (ZTEK) &minus;32.04%</b>, <b>Jupiter Neurosciences (JUNS) &minus;26.79%</b> and <b>FingerMotion (FNGR) &minus;19.07%</b> among losers. '
 '<b>Every one of those six percentages matches the 5:35 PM screen to the hundredth of a point.</b> '
 '&#9888; <b>NCRA and MENS did not return this run</b>; they are <b>not</b> recorded as having moved, only as having dropped off a list whose depth varies between fetches. '
 '<b>One name is new: WEBUY GLOBAL (WBUY) +4.07% at $0.94</b> — a far smaller move than anything else on the board, which is why it appears now and did not before.<br><br>'
 '&#9888; <b>The instrument conclusion from the last two runs is unchanged but better supported.</b> Four screens across roughly seventy minutes produced <b>three identical readings and one outlier that named no percentages at all</b>; '
 '<b>the identical readings are the signal and the outlier was the artefact</b>. <b>No dollar figure is attached to any of the six except where the screen itself supplied one.</b></div>')
i = h.find('<h2 class="sec">After-Hours Movers</h2>')
if i>=0:
    j = h.index('</h2>', i)+5
    h = h[:j] + ah + h[j:]

rates = ('<div class="note" style="margin-bottom:14px">' + N +
 ' <b>Crude gets a third read and it lands between the two already here.</b> A commodities read fetched this run marks <b>WTI at $85.54, up 2.57%</b>, and <b>Brent at $90.23</b>, '
 'against the settles this page leads with (<b>WTI $85.76, +2.83%; Brent $90.49, +2.71%</b>) and the intraday marks carried before them (<b>$85.54 / $90.69</b>). '
 '&#9888; <b>All three Brent figures &mdash; $90.23, $90.49, $90.69 &mdash; sit inside a 46-cent band on a barrel that moved roughly two and a half dollars</b>, '
 'and <b>the WTI mark repeats the earlier one to the cent</b>. <b>These are vendors marking the same rally at slightly different moments, not disagreeing about it.</b> '
 '<b>The settles remain what this page leads with.</b></div>')
i = h.find('<h2 class="sec">Rates, Bonds &amp; Commodities</h2>')
if i>=0:
    j = h.index('</h2>', i)+5
    h = h[:j] + rates + h[j:]

# tldr
h = re.sub(r'<div class="tldr"><b>The Tape</b>.*?</div>',
 '<div class="tldr"><b>The Tape</b> <span>A fifth read confirms the close unchanged &mdash; <b>S&amp;P 500 7,686.14 (&minus;0.33%)</b>, <b>Nasdaq Composite 26,370.89 (&minus;0.12%)</b>, '
 '<b>Dow 53,185.90 (&minus;374.09, &minus;0.70%)</b> after U.S. and Iranian forces exchanged fire for the first time in a month &mdash; and the afternoon&rsquo;s one open discrepancy closed: '
 'a quoted <b>10-year day range of 4.697%&ndash;4.767% against a 4.722% close</b> proves the &ldquo;topped 4.75%&rdquo; print and the daily mark were always the same path.</span></div>',
 h, count=1, flags=re.S)
wr('wallstreet-briefing.html', h); report.append('wallstreet: lead + sector + after-hours + rates + tldr')

# ═══ CYBER ══════════════════════════════════════════════════════════════════
h = rd('cyber-briefing.html')
top = ('<div class="note" style="margin-bottom:14px">' + N +
 ' <b>PaperCut finally has severity scores, and they are not the ones a reader would have guessed from the word &ldquo;zero-day&rdquo;.</b> '
 'A vendor advisory fetched this run scores <b>CVE-2026-82078 at CVSS 9.4</b> and <b>CVE-2026-81578 at CVSS 8.8</b>, and dates the disclosure to <b>August 27, 2026</b>. '
 '&#9888; <b>Neither is a 9.8, and this page has never attached one to either CVE</b> — the guard added two runs ago exists precisely to keep a stray 9.8 from drifting onto them. '
 '<b>The chain is unchanged: 81578 is improper access control in the web management interface letting an unauthenticated remote attacker modify system configuration; '
 '82078 is unsafe dynamic class loading in the database connection utilities, yielding arbitrary Java execution.</b> '
 '<b>8.8 leading into 9.4 is what a two-stage chain looks like scored one link at a time — the severity is in the composition, not in either number.</b><br><br>'
 '&#9888; <b>And the patch story got worse in the way that matters most operationally: PaperCut has issued a SECOND emergency patch after researchers broke the first fix.</b> '
 '<b>An organisation that patched once, promptly, and moved on is not covered.</b> This is now the single most consequential sentence on this page: '
 '<b>the KEV clock to September 14 is measured against the current build, not against the fact that you patched.</b></div>')
i = h.find('<h2 class="sec">Top Story</h2>')
if i>=0:
    j = h.index('</h2>', i)+5
    h = h[:j] + top + h[j:]

inc = ('<div class="note" style="margin-bottom:14px">' + N +
 ' <b>Three incidents move this run and one of them puts a number on an extortion demand for the first time.</b> '
 '<b>The McKesson intrusion now carries a stated ransom: ShinyHunters is demanding $55,236,150</b>, against the <b>284 million records</b> the group claims — '
 'both figures from reporting fetched this run. &#9888; <b>The claim count is the attacker’s, not McKesson’s, and is printed as a claim.</b><br><br>'
 '<b>Two names are new.</b> <b>Air France and KLM confirmed an attacker gained unauthorised access to a third-party customer-service platform used by their contact centres</b>, '
 'and both airlines <b>say the intrusion was contained and internal systems were not compromised</b>. '
 '<b>Hackers have threatened to leak data from Neogen, a US food-safety company</b>, in what reporting fetched this run frames as a potential break in the food supply chain. '
 '&#9888; <b>Neither the Neogen actor nor a record count was stated in what was fetched, and none is supplied.</b><br><br>'
 '<b>The ransomware number of the run is Medusa.</b> <b>CISA reports Medusa affiliates have breached more than 500 organisations across critical-infrastructure sectors</b>, '
 'working opportunistically — <b>monitoring vulnerability announcements and targeting organisations that have not yet patched</b>. '
 '&#9888; <b>That method is the exact reason the PaperCut re-patch above is the day’s operational point</b>: a partially-patched estate is the population Medusa is described as selecting for.</div>')
i = h.find('<h2 class="sec">Breaches &amp; Incidents</h2>')
if i>=0:
    j = h.index('</h2>', i)+5
    h = h[:j] + inc + h[j:]

spot = ('<div class="note" style="margin-bottom:14px">' + N +
 ' <b>The Siemens S7 advisory now has a number and a full author list.</b> Reporting fetched this run identifies it as <b>joint advisory AA26-231A, issued August 19, 2026 by the NSA, CISA, FBI, the Department of Energy and the EPA</b>. '
 '<b>The tooling is named: attackers combine the open-source industrial-automation libraries snap7.dll and python-snap7 with AI-assisted scripting</b> to build custom tools '
 '<b>disguised as legitimate OT monitoring software</b>, giving <b>read and write access to PLC memory, configuration data and ladder-logic programs over the S7comm protocol</b>. '
 '<b>Targets are found by scanning with Censys and ZoomEye for exposed or poorly segmented devices, then using default or weak credentials.</b> '
 '&#9888; <b>The significant claim is capability, not novelty</b> — the advisory’s argument is that AI drops the expertise and time needed to produce working ICS exploitation scripts, '
 'not that a new vulnerability exists. <b>Affected sectors named: water and wastewater, manufacturing, energy, chemicals, and food and agriculture.</b></div>')
i = h.find('<h2 class="sec">Threat Actor Spotlight</h2>')
if i>=0:
    j = h.index('</h2>', i)+5
    h = h[:j] + spot + h[j:]

ref = ('<div class="note" style="margin-bottom:14px">' + N +
 ' <b>&ldquo;SpaceX’s Cursor&rdquo; came back a fourth time and is refused a fourth time.</b> A roundup fetched this run again describes '
 '<b>Aurora ransomware operators using &ldquo;SpaceX’s Cursor&rdquo; AI coding assistant to break into target networks</b>, naming a spacecraft manufacturer as the tool’s publisher. '
 '<b>Nothing fetched in four runs establishes who publishes Cursor.</b> <b>The actor and the tool are published; the publisher attribution is struck.</b> '
 '&#9888; <b>Same call as &ldquo;former champion&rdquo; on the MMA page: a wrong descriptor discredits the true sentence it is attached to.</b><br><br>'
 '&#9888; <b>Also recorded, not published as today’s KEV news:</b> the catalog additions surfacing this run are the <b>six of August 26</b> (including <b>CVE-2026-8452</b> alongside five older CVEs) '
 'and the <b>three of August 27</b> — <b>CVE-2023-49105 (ownCloud, improper authentication, due August 30)</b>, <b>CVE-2026-53362 (Linux kernel)</b> and <b>CVE-2026-66384 (JFrog Artifactory, path traversal)</b>. '
 '<b>Their due dates run from August 29 to September 9</b>, which is <b>direct confirmation that KEV deadlines are assigned per-CVE and risk-based</b>, not on the retired three-week rule. '
 '<b>All are already past or nearly past; the September 14 PaperCut date remains the live federal clock on this page.</b></div>')
i = h.find('<h2 class="sec">Refused This Run</h2>')
if i>=0:
    j = h.index('</h2>', i)+5
    h = h[:j] + ref + h[j:]

h = re.sub(r'<div class="tldr"><b>The Wire</b>.*?</div>',
 '<div class="tldr"><b>The Wire</b> <span>The <b>PaperCut NG/MF</b> chain now carries vendor severity scores &mdash; <b>CVE-2026-81578 at CVSS 8.8</b> feeding <b>CVE-2026-82078 at CVSS 9.4</b>, '
 'both added to CISA&rsquo;s Known Exploited Vulnerabilities catalog on <b>August 31 with a September 14 remediation date</b> &mdash; and <b>PaperCut has now issued a second emergency patch after researchers broke the first fix</b>, '
 'which means an estate that patched once and moved on is still exposed to the exact opportunistic targeting CISA attributes to Medusa affiliates across 500-plus organisations.</span></div>',
 h, count=1, flags=re.S)
wr('cyber-briefing.html', h); report.append('cyber: top + incidents + spotlight + refused + tldr')

# ═══ MMA ════════════════════════════════════════════════════════════════════
h = rd('mma-briefing.html')
top = ('<div class="note" style="margin-bottom:14px">' + N +
 ' <b>UFC.com settles the Paris card count that two secondary sources spent the afternoon disagreeing about — and it agrees with neither.</b> '
 'The promotion’s own preview calls <b>UFC Fight Night: Hooker vs. Parnasse a loaded 14-fight card</b> at the <b>Accor Arena in Paris on September 5</b>, '
 'the <b>fifth straight year the Octagon has made the September trip to the Seine</b>. '
 '&#9888; <b>This page carried 15 fights at 5:05 PM and 13 at 5:35 PM. Fourteen is the primary source and is adopted; the other two are retired, not reconciled.</b> '
 '<b>A card can lose or add bouts without announcing it to a search index, which is exactly why the promotion’s own page outranks an aggregator here.</b><br><br>'
 '<b>Two further details arrive from the same page.</b> The broadcast is <b>Paramount+, prelims at 12 PM ET and the main card at 3 PM ET</b> — '
 '<b>an afternoon card in the United States, which is what a Paris start time means</b>. And <b>Saladhine Parnasse earned his UFC contract through Dana White’s Contender Series earlier this year</b>, '
 'which is the promotion’s own description and the first sourced account of how the debutant got here. '
 '&#9888; <b>It is also the cleanest explanation of the &minus;600 line</b>: the market is pricing an unbeaten regional champion, not an unknown. '
 '<b>One bout is new to this page: Oumar Sy vs. Modestas Bukauskas.</b></div>')
i = h.find('<h2 class="sec">Top Story</h2>')
if i>=0:
    j = h.index('</h2>', i)+5
    h = h[:j] + top + h[j:]

res = ('<div class="note" style="margin-bottom:14px">' + N +
 ' <b>Shanghai gains the two records and the callout that were missing.</b> <b>Song Yadong is 24-9-1</b> after the <b>KO by right uppercut at 1:48 of round two</b>, '
 'and <b>Umar Nurmagomedov falls to 20-1</b> — <b>the first loss of his career</b>, and this page had the result for three days without either number. '
 '<b>Song called for a title shot in his post-fight interview.</b> &#9888; <b>No title fight has been announced; the callout is published as a callout.</b><br><br>'
 '<b>Two undercard finishes gain their exact times:</b> <b>Denise Gomes def. Yan Xiaonan by TKO (elbow and punches) at 4:49 of round one</b>, '
 'and <b>Kai Asakura def. Aoriqileng by KO (head kick and strikes) at 0:34 of round two</b>. '
 '<b>Both fighters already appear in this page’s bonus list; the methods and times are new.</b></div>')
i = h.find('<h2 class="sec">UFC Shanghai &mdash; Results</h2>')
if i>=0:
    j = h.index('</h2>', i)+5
    h = h[:j] + res + h[j:]

sched = ('<div class="note" style="margin-bottom:14px">' + N +
 ' <b>September stops being three dates and becomes three cards.</b> <b>Noche UFC: Silva vs. Delgado, Saturday September 12, Desert Diamond Arena, Glendale, Arizona</b> '
 '— main card <b>2 PM PT on Paramount+</b>, prelims 11 AM PT — now has a published main card: '
 '<b>Alexa Grasso vs. Manon Fiorot</b>, <b>Brandon Moreno vs. Joseph Morales</b>, <b>Waldo Cortes Acosta vs. Curtis Blaydes</b>, <b>Kelvin Gastelum vs. Yousri Belgaroui</b>, '
 '<b>Tim Elliott vs. Edgar Chairez</b> and <b>JJ Aldrich vs. Regina Tarin</b>. '
 '&#9888; <b>Grasso&ndash;Fiorot is the consequential one</b> — a former flyweight champion against the division’s most recent title challenger — but '
 '<b>nothing fetched this run frames it as a title eliminator, and it is not described as one here.</b><br><br>'
 '<b>The month closes at the Apex:</b> <b>UFC Fight Night: Rosas Jr. vs. Barcelos, Saturday September 26, Meta APEX, Las Vegas</b>, main card <b>6 PM ET on Paramount+</b>. '
 '&#9888; <b>No odds were stated for either card in what was fetched and none are printed.</b></div>')
i = h.find('<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>')
if i>=0:
    j = h.index('</h2>', i)+5
    h = h[:j] + sched + h[j:]

champ = ('<div class="note" style="margin-bottom:14px">' + N +
 ' <b>The Chimaev regression presented itself a fourth time and was beaten by the primary source rather than by inference.</b> '
 'An aggregated champions page fetched this run again returns <b>&ldquo;Middleweight (185): Khamzat Chimaev, as of August 16, 2025&rdquo;</b> alongside eleven cells that match this board exactly. '
 '&#9888; <b>Its own date is the disproof: August 16, 2025 predates UFC 328 by nearly nine months.</b> '
 '<b>UFC.com, ESPN, Yahoo and CBS all state, in reporting fetched this run, that Sean Strickland took the middleweight title from Chimaev by split decision at UFC 328, Prudential Center, Newark, on May 9, 2026.</b> '
 '<b>Two judges scored it 48&ndash;47 Strickland, one 48&ndash;47 Chimaev; Strickland entered as more than a 4-to-1 underdog</b>, and it was <b>his second career title upset</b> after Israel Adesanya in 2023. '
 '<b>A stale champions list is not a competing claim, it is an out-of-date one, and its own timestamp says so.</b> '
 '<b>The board is unchanged for an eightieth straight edition.</b></div>')
i = h.find('<h2 class="sec">Champions Board</h2>')
if i>=0:
    j = h.index('</h2>', i)+5
    h = h[:j] + champ + h[j:]

h = re.sub(r'<div class="tldr"><b>Tale of the Tape</b>.*?</div>',
 '<div class="tldr"><b>Tale of the Tape</b> <span>UFC.com settles the Paris count at <b>14 fights</b> &mdash; against the 15 and 13 this page carried earlier &mdash; '
 'dates it <b>September 5 at the Accor Arena</b> with <b>prelims noon ET and the main card 3 PM ET on Paramount+</b>, and confirms <b>Saladhine Parnasse came through the Contender Series this year</b>, '
 'which is the plainest account yet of why an unbeaten debutant is a <b>&minus;600</b> favourite over Dan Hooker; the champions board is unchanged for an eightieth straight edition.</span></div>',
 h, count=1, flags=re.S)
wr('mma-briefing.html', h); report.append('mma: top + results + schedule + champions + tldr')

print('\n'.join(report))
