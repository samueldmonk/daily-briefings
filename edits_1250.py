#!/usr/bin/env python3
"""Incremental edits for the 12:50 ET Midday Edition, Wednesday 2026-08-26.
Every string inserted below traces to a source fetched or returned this run."""
import re, sys, io

FAIL = []
def rep(h, old, new, label, count=1):
    if old not in h:
        FAIL.append("MISSING ANCHOR: " + label)
        return h
    return h.replace(old, new, count)

# ---------------------------------------------------------------- WALL STREET
p = 'wallstreet-briefing.html'
h = open(p, encoding='utf-8').read()

# 1. demote prior-edition New tags
h = h.replace('<span class="tag new">New &middot; 11:05</span>',
              '<span class="tag">Carried &middot; 11:05 edition</span>')

# 2. TLDR
old_tldr = h[h.find('<div class="tldr"><b>The Tape</b>'):]
old_tldr = old_tldr[:old_tldr.find('</div>')+6]
new_tldr = ('<div class="tldr"><b>The Tape</b> <span>The S&amp;P&nbsp;500 has crossed into the red: '
            '<b>7,661.57, down 15.71 points or 0.20%</b>, in a read stamped <b>12:41:56&nbsp;p.m. EDT</b> '
            'that reconciles three ways against Tuesday&rsquo;s close &mdash; a second read two minutes '
            'earlier had it at <b>7,662.54, &minus;14.74, &minus;0.19%</b> &mdash; so the small opening gain '
            'is now fully surrendered with the <b>Nasdaq&nbsp;100 down 0.5%</b> on chip weakness, while '
            '<b>Summit Therapeutics &plus;12.49%</b> and <b>Kura Oncology &plus;10.5%</b> lead the gainers, '
            '<b>Abercrombie &amp; Fitch remains the day&rsquo;s outlier at &plus;30.85%</b>, and the whole tape '
            'waits on <b>Nvidia after the close</b>.</span></div>')
h = rep(h, old_tldr, new_tldr, 'ws tldr')

# 3. Lead headline + new top paragraph
h = rep(h,
    '<h2>The tape splits &mdash; the S&amp;P&nbsp;500 clings to green while the Dow and Nasdaq slip, as of <i>~11:06&nbsp;a.m. ET</i></h2>',
    '<h2>The S&amp;P&nbsp;500 gives it all back and turns red, as of <i>~12:42&nbsp;p.m. ET</i></h2>\n'
    '<p><b>&#9679; New at 12:50 &mdash; the freshest read on the tape, and the index has crossed the line.</b> '
    'A market summary returned this run states that <b>the S&amp;P&nbsp;500 stood at 7,661.57, down 15.71 points '
    'or 0.20%, as of 12:41:56&nbsp;p.m. EDT</b>. It passes this page&rsquo;s three-way test on its own: '
    '<b>7,661.57 &plus; 15.71 = 7,677.28</b>, exactly Tuesday&rsquo;s S&amp;P close as published in the Weekly '
    'Scorecard below, and <b>15.71 &divide; 7,677.28 = 0.205%</b>, which rounds to the stated 0.20%. '
    '<b>A second, independent summary read minutes earlier in the same run puts it at 7,662.54, &minus;14.74, '
    '&minus;0.19% as of 12:39&nbsp;p.m. EDT</b> &mdash; and that figure reconciles the same three ways against the '
    'same prior close. <b>Two separately returned reads, two minutes apart, both self-consistent and both agreeing '
    'on direction and magnitude.</b> Set against the 11:06 read of <b>7,681.36, &plus;4.08, &plus;0.05%</b> carried '
    'in the previous edition, the S&amp;P has given up the last of its opening gain and roughly twenty points more '
    'in the space of about ninety minutes.</p>\n'
    '<p><b>&#9679; The chip complex is where the weight is.</b> A market wrap returned this run describes US stocks '
    'as <b>mostly lower amid losses from heavyweight chip producers ahead of Nvidia&rsquo;s results</b>, with the '
    '<b>S&amp;P&nbsp;500 and the Dow inching below the flatline while the Nasdaq&nbsp;100 fell 0.5%</b>. '
    '<b>&#9888; That Nasdaq&nbsp;100 figure carries no level and no clock time on the page that returned it, so it is '
    'printed as a direction and a magnitude only.</b> A separate summary this run reports <b>Nvidia shares wavering '
    'ahead of the release</b> &mdash; the report is expected to signal the level of capital expenditure by the AI '
    'hyperscalers that has underwritten this market. <b>&#9888; A third source read this run, Trading Economics, '
    'quotes its US500 <i>contract-for-difference</i> tracker at <b>7,674, &minus;0.04%</b>. That is a CFD on the '
    'index, not the index, and it does not reconcile against Tuesday&rsquo;s cash close &mdash; it is noted and not '
    'used.</b></p>',
    'ws lead h2')

# demote the previous lead's leading marker
h = rep(h, '<p><b>&#9679; New at 11:05 &mdash; the freshest read on the tape, and it does not match the 9:59 board.</b>',
        '<p><b>&#9679; Carried from the 11:05 edition &mdash; the previous read, now superseded.</b>',
        'ws lead demote')

# 4. New movers card
anchor = '<div class="lab">Movers &amp; drivers</div> <div class="cards">'
if anchor not in h:
    anchor = h[h.find('>Movers &amp; drivers</div>'):]
    anchor = anchor[:anchor.find('<div class="card">')]
    anchor = '>Movers &amp; drivers</div>' + anchor[len('>Movers &amp; drivers</div>'):]
newcard = ('<div class="card"> <div class="tags"><span class="tag new">New &middot; 12:50</span>'
           '<span class="tag">Gainers</span><span class="tag">Healthcare</span></div> '
           '<h3>Biotech and a CEO&rsquo;s own chequebook lead the gainers</h3> '
           '<p><b>Summit Therapeutics (SMMT) &plus;12.49%.</b> A StocksToTrade wire read this run attributes the move '
           'to the <b>Global HARMOni Phase&nbsp;III</b> readout, in which <b>ivonescimab plus chemotherapy delivered a '
           'statistically significant and clinically meaningful progression-free-survival gain over placebo plus '
           'chemotherapy</b> in EGFR-mutated non-small-cell lung cancer. <b>Kura Oncology (KURA) &plus;10.5%</b>, after '
           'president and chief executive <b>Troy Edward Wilson purchased 100,000 shares of common stock on August&nbsp;24 '
           'at a weighted-average price of $12.39</b>, per a regulatory filing &mdash; his second substantial open-market '
           'purchase in roughly a week &mdash; with <b>Jefferies reaffirming its Buy rating on August&nbsp;26</b>. Kura&rsquo;s '
           'second quarter had already beaten: an <b>adjusted loss of $0.77 a share against a $0.88 consensus</b>, on '
           '<b>revenue of $20.87&nbsp;million against $20.16&nbsp;million expected</b>.</p> '
           '<p><b>Also up, without a number attached.</b> <b>Meta</b> and <b>J.M. Smucker</b> are named among the early '
           'gainers; Smucker <b>beat on quarterly sales and profit and raised its fiscal-2027 sales and adjusted-EPS '
           'outlook</b>. <b>Jefferies Financial Group (JEF) &plus;5.5%</b> is attributed to a broader financial-sector '
           'rally on improving capital-markets activity. <b>&#9888; None of these carries a price level or a clock time '
           'on the pages that returned them, so each is published as a percentage move or a direction only, and none is '
           'reconciled against a prior close.</b></p></div> ')
h = rep(h, 'Movers &amp; drivers</div>\n<div class="cards">\n',
        'Movers &amp; drivers</div>\n<div class="cards">\n' + newcard,
        'ws movers insert')

# 5. Rates: Wednesday 10-year
h = rep(h,
    '<tr><td>10-year Treasury yield</td><td>4.629%</td><td class="down">more than 7 bp lower</td><td>Tue, Aug 25 (CNBC)</td></tr>',
    '<tr><td>10-year Treasury yield</td><td>4.65%</td><td class="down">eased</td><td>Wed, Aug 26 (Trading Economics)</td></tr>'
    '<tr><td>10-year Treasury yield</td><td>4.629%</td><td class="down">more than 7 bp lower</td><td>Tue, Aug 25 (CNBC)</td></tr>',
    'ws 10y row')
h = rep(h,
    'The three Treasury rows are still Tuesday&rsquo;s, because no source fetched this run states a Wednesday yield.',
    '<b>&#9679; New at 12:50 &mdash; the ten-year now has a Wednesday print.</b> A Trading Economics report returned this '
    'run states the <b>10-year Treasury yield eased to 4.65% on Wednesday</b> as investors assessed the morning&rsquo;s '
    'data for the Fed&rsquo;s rate path; that row is added above Tuesday&rsquo;s and both are shown. <b>&#9888; The figure '
    'is quoted to two decimals with no basis-point change stated, so no move in basis points is asserted, and it is '
    '<i>higher</i> than Tuesday&rsquo;s 4.629% close rather than lower.</b> The 30-year and 2-year rows are still '
    'Tuesday&rsquo;s, because no source fetched this run states a Wednesday level for either.',
    'ws rates note')

# 6. On the radar addition
h = rep(h, 'On the radar</div>\n<div class="panel">\n<ul class="bul">\n',
        'On the radar</div>\n<div class="panel">\n<ul class="bul">\n'
        '<li><b>&#9679; New at 12:50 &mdash; the options market has put a number on tonight.</b> A TechStock&sup2; '
        'headline dated today reads <b>&ldquo;Nvidia Shares Gain 2.2% as Options Market Prices in $280 Billion Earnings '
        'Move.&rdquo;</b> <b>&#9888; That is a headline, not a page fetched in full, and the 2.2% carries no clock time '
        '&mdash; it is carried as the outlet states it and is not reconciled against the wrap above, which describes '
        'Nvidia shares as <i>wavering</i>. Both readings are printed; neither is merged into the other.</b></li> '
        '<li><b>&#9679; New at 12:50 &mdash; Friday&rsquo;s speech has a name attached.</b> A Trading Economics report '
        'read this run states that investors await <b>Fed Chair Kevin Warsh&rsquo;s speech at the annual Jackson Hole '
        'symposium on Friday</b>, where <b>he is not expected to provide clear guidance on the September decision</b>. '
        '<b>&#9888; That expectation is the outlet&rsquo;s characterisation, not a statement from the Federal Reserve.</b></li> ',
        'ws radar insert')

# 7. ticker tape swap SEDG -> SMMT
h = rep(h, '{"proName":"NASDAQ:SEDG","title":"SolarEdge"}', '{"proName":"NASDAQ:SMMT","title":"Summit Therapeutics"}', 'ws tape')

# 8. sources
h = rep(h, '>Sources</div>\n<ul>\n',
        '>Sources</div>\n<ul>\n'
        '<li><b>&#9679; New at 12:50 &mdash; market summaries returned this run</b> across the '
        '<a href="https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-26-2026">TheStreet</a> and '
        '<a href="https://finance.yahoo.com/markets/live/stock-market-today-wednesday-august-26-dow-sp-500-nasdaq-081834782.html">Yahoo Finance</a> '
        'Wednesday coverage &mdash; the source for the <b>12:41:56&nbsp;p.m. EDT S&amp;P&nbsp;500 read of 7,661.57, '
        '&minus;15.71, &minus;0.20%</b>, the <b>12:39&nbsp;p.m. EDT read of 7,662.54, &minus;14.74, &minus;0.19%</b>, the '
        '<b>Nasdaq&nbsp;100 &minus;0.5%</b> line and the description of Nvidia shares wavering into the release.</li> '
        '<li><b>&#9679; <a href="https://tradingeconomics.com/united-states/stock-market">Trading Economics &mdash; United States Stock Market Index</a></b>, '
        '<b>fetched in full this run</b> &mdash; the source for the <b>US500 CFD read of 7,674, &minus;0.04%</b>, which is '
        'noted and not used, and, via its '
        '<a href="https://tradingeconomics.com/united-states/government-bond-yield">10-year yield page</a>, for the '
        '<b>Wednesday 10-year at 4.65%</b> and the <b>Kevin Warsh / Jackson Hole Friday</b> line.</li> '
        '<li><b>&#9679; <a href="https://stockstotrade.com/news/summit-therapeutics-inc-smmt-news-2026_08_26/">StocksToTrade &mdash; Summit Therapeutics (SMMT)</a></b> and '
        '<a href="https://www.investing.com/news/stock-market-news/why-is-kura-oncology-stock-surging-today-93CH-4875190">Investing.com &mdash; &ldquo;Why is Kura Oncology stock surging today?&rdquo;</a> '
        '&mdash; the source for <b>SMMT &plus;12.49%</b> and the HARMOni Phase&nbsp;III progression-free-survival result, and for '
        '<b>KURA &plus;10.5%</b>, the <b>100,000-share purchase at $12.39 on August&nbsp;24</b>, the <b>Jefferies Buy reaffirmation '
        'on August&nbsp;26</b> and the <b>$0.77 vs $0.88 / $20.87m vs $20.16m</b> quarter. Meta, J.M. Smucker and '
        '<b>JEF &plus;5.5%</b> come from the same movers cluster.</li> '
        '<li><b>&#9679; <a href="https://ts2.tech/en/stock-market-today-08-26-2026/">TechStock&sup2; &mdash; US Stock Market Today 08/26/2026</a></b>, '
        '<b>fetched in full this run</b> &mdash; the source for the headline <b>&ldquo;Nvidia Shares Gain 2.2% as Options Market '
        'Prices in $280 Billion Earnings Move.&rdquo;</b></li> ',
        'ws sources')

open(p, 'w', encoding='utf-8').write(h)

# ---------------------------------------------------------------------- CYBER
p = 'cyber-briefing.html'
h = open(p, encoding='utf-8').read()
h = h.replace('<span class="tag new">New &middot; 11:05</span>',
              '<span class="tag">Carried &middot; 11:05 edition</span>')

newcard = ('<div class="card"> <div class="tags"><span class="tag new">New &middot; 12:50</span>'
           '<span class="tag">Breach</span><span class="tag">SSN exposure</span></div> '
           '<h3>A Pizza Hut and Taco Bell franchise operator files a breach report exposing Social Security numbers</h3> '
           '<p><b>Hut American Group LLC</b> &mdash; a Pizza Hut franchisee operator within the <b>Flynn Group</b> portfolio, '
           'which also runs franchised locations for <b>Applebee&rsquo;s, Panera Bread, Taco Bell and Wendy&rsquo;s</b> &mdash; '
           '<b>filed a data-breach report with the Texas Attorney General on August&nbsp;21, 2026</b>, identifying '
           '<b>3,528 Texas residents</b> as affected. The categories of personal information stated as exposed are '
           '<b>addresses, Social Security numbers, driver&rsquo;s licence numbers, government-issued identification numbers '
           'such as passports and state ID cards, financial information including account and payment-card numbers, and '
           'dates of birth</b> &mdash; close to a full identity-theft set.</p> '
           '<p><b>It may not be the only one in that group.</b> Reporting read this run notes that <b>Apple American Group</b>, '
           'operator of the largest Applebee&rsquo;s franchise in the United States, <b>began reporting a data breach to state '
           'attorneys general from August&nbsp;18, 2026</b>. <b>&#9888; The reporting explicitly states it is unclear whether the '
           'two incidents are related, and no link between them is asserted here.</b> <b>&#9888; No threat actor, no ransomware '
           'family, no CVE, no intrusion vector and no national total is stated in the reporting read this run &mdash; the '
           '3,528 figure is the Texas filing only, not the size of the breach.</b> This is a state-regulator filing surfaced '
           'in a search summary, not a page fetched in full.</p></div> ')
h = rep(h, 'Breaches &amp; incidents</div>\n<div class="cards">\n',
        'Breaches &amp; incidents</div>\n<div class="cards">\n' + newcard,
        'cy breach insert')

# TrueConf CVSS discrepancy note in the KEV section
h = rep(h,
    '<li><b>CVE-2026-72530</b> &mdash; TrueConf Server, code injection / sandbox breakout (CVSS 9.5). Added Aug 20, due <b>Sep 3</b>.',
    '<li><b>CVE-2026-72530</b> &mdash; TrueConf Server, code injection / sandbox breakout (CVSS 9.5; <b>&#9888; a SecurityWeek-sourced '
    'summary read this run gives 9.0 for this CVE &mdash; both renderings are printed, neither is merged, and the lower figure is '
    'not substituted without a vendor or CISA page confirming it</b>). Added Aug 20, due <b>Sep 3</b>.',
    'cy 72530 cvss')

h = rep(h,
    '<div class="note"><b>Corrected this run:</b> the 8:46 edition left this line reading',
    '<div class="note"><b>&#9679; New at 12:50 &mdash; the TrueConf pair got independent confirmation, and one detail is added.</b> '
    'A fresh catalogue search this run re-confirms both TrueConf entries and states that <b>CISA ordered federal agencies to patch '
    'both by September&nbsp;3, 2026</b>, with the missing-authentication flaw carrying a <b>three-day</b> window and the '
    'code-injection flaw a <b>two-week</b> one &mdash; consistent with the per-CVE risk-based assignment under BOD&nbsp;26-04 already '
    'described above. <b>CVE-2026-72529</b> is described as reachable by <b>a remote attacker who can reach TrueConf Server over '
    'TCP port 4307</b> to invoke an undocumented function and run an arbitrary script <b>without authentication</b>. On attribution: '
    '<b>Kaspersky says the Head Mare group has been exploiting both flaws since at least July&nbsp;2026</b>, replacing client '
    'installers with malicious versions that deploy backdoor malware. <b>&#9888; Kaspersky&rsquo;s attribution is carried as that '
    'vendor states it; no victim, sector or count is stated and none is asserted.</b> <b>&#9888; KEV additions dated August&nbsp;26: '
    'nothing seen this run</b> &mdash; the fifth consecutive edition in which a catalogue search returned no alert page later than '
    'August&nbsp;25. <b>Corrected this run:</b> the 8:46 edition left this line reading',
    'cy kev note')

h = rep(h, '>Sources</div>\n<ul>\n',
        '>Sources</div>\n<ul>\n'
        '<li><b>&#9679; New at 12:50 &mdash; <a href="https://www.claimdepot.com/data-breach/hut-8-mining-corp-2026">Hut American Group data-breach report</a></b> '
        '&mdash; the source for the <b>Texas Attorney General filing of August&nbsp;21, 2026</b>, the <b>3,528 Texas residents</b> '
        'figure, the exposed-data categories, the <b>Flynn Group</b> affiliation and the <b>Apple American Group</b> August&nbsp;18 '
        'reporting. Search summary, not fetched in full.</li> '
        '<li><b>&#9679; New at 12:50 &mdash; TrueConf KEV cluster:</b> '
        '<a href="https://www.cisa.gov/news-events/alerts/2026/08/20/cisa-adds-two-known-exploited-vulnerabilities-catalog">CISA &mdash; &ldquo;CISA Adds Two Known Exploited Vulnerabilities to Catalog&rdquo; (August&nbsp;20)</a>, '
        '<a href="https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-trueconf-server-flaws/">BleepingComputer</a> and '
        '<a href="https://www.securityweek.com/cisa-urges-immediate-patching-of-exploited-trueconf-vulnerabilities/">SecurityWeek</a> '
        '&mdash; the source for the <b>September&nbsp;3, 2026</b> deadline, the three-day / two-week window split, the '
        '<b>TCP port 4307</b> mechanic, the competing <b>9.0</b> CVSS rendering for CVE-2026-72530, and the '
        '<b>Kaspersky / Head Mare</b> attribution.</li> '
        '<li><b>&#9679; <a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">CISA Known Exploited Vulnerabilities Catalog</a></b> '
        '&mdash; the standing reference for every deadline on the board above.</li> ',
        'cy sources')
open(p, 'w', encoding='utf-8').write(h)

# ------------------------------------------------------------------------ MMA
p = 'mma-briefing.html'
h = open(p, encoding='utf-8').read()
h = h.replace('<span class="tag new">New &middot; 11:05</span>',
              '<span class="tag">Carried &middot; 11:05 edition</span>')

h = rep(h, 'Rankings &amp; business</div>\n<div class="panel">\n<p><b>Rankings movement.</b>',
        'Rankings &amp; business</div>\n<div class="panel">\n'
        '<p><span class="tag new">New &middot; 12:50</span> <b>The official rankings have moved on Sacramento, and five '
        'names changed position.</b> Reporting read this run gives the post-event board: <b>Gregory Rodrigues climbed three '
        'places to #7 at middleweight</b> after the headline unanimous decision, putting him on a <b>four-fight winning '
        'streak</b> and <b>7-1 in his last eight Octagon appearances</b>; <b>Anthony Hernandez fell two places to #9</b> and '
        'is now on a <b>two-fight skid</b>, his eight-fight win streak having been ended by <b>Sean Strickland</b> in '
        'February. Elsewhere on the same card, <b>Vitor Petrino entered the heavyweight top&nbsp;15</b> after beating '
        '<b>Serghei Spivac</b> in the co-main, <b>Carli Judice joined the women&rsquo;s flyweight top&nbsp;15</b> after a '
        'first-round stoppage of <b>Jeisla Chaves</b>, and <b>Reinier de Ridder broke into the light-heavyweight top&nbsp;10</b>. '
        '<b>&#9888; The Rodrigues and Hernandez placements are given as <i>Meta</i> rankings by the outlet that states them; '
        'the de Ridder, Petrino and Judice entries come from separate write-ups and no exact rank number is stated for any of '
        'the three, so none is printed.</b></p> <p><b>Rankings movement.</b>',
        'mma rankings')

h = rep(h, 'Around the sport</div>\n<div class="panel">\n<ul class="bul">\n',
        'Around the sport</div>\n<div class="panel">\n<ul class="bul">\n'
        '<li><span class="tag new">New &middot; 12:50</span> <b>Saturday is not only a UFC night.</b> <b>Mike Perry</b> and '
        '<b>Dillon Danis</b> headline the inaugural <b>Duel Arena 1</b> at <b>Orlando&rsquo;s Kia Center on August&nbsp;29</b> '
        '&mdash; a <b>professional mixed martial arts bout</b> on a <b>hybrid card of MMA, boxing and kickboxing</b>, with every '
        'bout contested <b>in a ring rather than a cage</b>. Perry, an Orlando resident, holds <b>Bare Knuckle Fighting '
        'Championship&rsquo;s &ldquo;King of Violence&rdquo; title</b> and <b>returned to MMA rules in May for the first time '
        'since 2021</b>. <b>&#9888; This is not a UFC event and neither man is on the UFC roster; it is carried because it '
        'shares the date with UFC Shanghai.</b></li> ',
        'mma around')

h = rep(h, '>Sources</div>\n<ul>\n',
        '>Sources</div>\n<ul>\n'
        '<li><b>&#9679; New at 12:50 &mdash; post-Sacramento rankings:</b> '
        '<a href="https://www.si.com/fannation/mma/news/ufc-rankings-update-several-new-fighters-debut-ufc-sacramento-wins">Sports Illustrated / FanNation</a>, '
        '<a href="https://www.sherdog.com/news/rankings/4/UFC-Sacramento-shakes-up-rankings-as-Rodrigues-De-Ridder-surge-202500">Sherdog</a> and '
        '<a href="https://www.mmamania.com/ufc-mma-rankings/467315/top-10-reinier-de-ridder-crashes-light-heavyweight-rankings-ufc-sacramento">MMA Mania</a> '
        '&mdash; the source for <b>Rodrigues to #7</b>, <b>Hernandez to #9</b>, <b>Petrino</b> into the heavyweight top&nbsp;15, '
        '<b>Judice</b> into the women&rsquo;s flyweight top&nbsp;15 and <b>de Ridder</b> into the light-heavyweight top&nbsp;10.</li> '
        '<li><b>&#9679; New at 12:50 &mdash; <a href="https://www.wftv.com/news/local/mike-perry-dillon-danis-headline-inaugural-duel-arena-event-orlando/VCIHPGS2KZAUBC2AOVWZYSQUEE/">WFTV &mdash; &ldquo;Mike Perry and Dillon Danis to headline inaugural Duel Arena event in Orlando&rdquo;</a></b> '
        'and <a href="https://www.tapology.com/fightcenter/bouts/1162938-duel-arena-1-platinum-mike-perry-vs-dillon-el-jefe-danis">Tapology</a> '
        '&mdash; the source for <b>Duel Arena 1</b>, the <b>Kia Center</b>, the <b>August&nbsp;29</b> date, the hybrid-card format '
        'and Perry&rsquo;s BKFC title and May return to MMA rules.</li> '
        '<li><b>&#9679; <a href="https://www.mmamania.com/daily_mania_ufc_mma/467355/open-thread-august-26-2026-self-defense-and-a-bunch-of-new-trailers">MMA Mania &mdash; open thread, August&nbsp;26, 2026</a></b> '
        '&mdash; read this run for same-day coverage; the source for the rankings-update and Perry&ndash;Danis threads being live today.</li> ',
        'mma sources')
open(p, 'w', encoding='utf-8').write(h)

# ---------------------------------------------------------------------- INDEX
p = 'index.html'
h = open(p, encoding='utf-8').read()
h = rep(h,
    '<h2>The tape splits at midday: the S&amp;P clings to green, the Dow and Nasdaq slide</h2>',
    '<h2>The S&amp;P&nbsp;500 gives back its opening gain and turns red before Nvidia</h2>', 'idx mkt h2')
old = h[h.find('<h2>The S&amp;P&nbsp;500 gives back its opening gain and turns red before Nvidia</h2>'):]
old_p = old[old.find('<p>'):old.find('</p>')+4]
new_p = ('<p>The S&amp;P&nbsp;500 has crossed into the red: <b>7,661.57, down 15.71 points or 0.20%</b>, in a read stamped '
         '<b>12:41:56&nbsp;p.m. EDT</b> that reconciles three ways against Tuesday&rsquo;s close &mdash; a second read two '
         'minutes earlier had it at <b>7,662.54, &minus;14.74, &minus;0.19%</b> &mdash; so the small opening gain is now fully '
         'surrendered with the <b>Nasdaq&nbsp;100 down 0.5%</b> on chip weakness, while <b>Summit Therapeutics &plus;12.49%</b> '
         'and <b>Kura Oncology &plus;10.5%</b> lead the gainers, <b>Abercrombie &amp; Fitch remains the day&rsquo;s outlier at '
         '&plus;30.85%</b>, and the whole tape waits on <b>Nvidia after the close</b>.</p>')
h = rep(h, old_p, new_p, 'idx mkt p')

# cyber card: keep the miniOrange lead, append the new franchise breach
h = rep(h, 'with the Oracle CVSS&nbsp;10.0 flaw due tomorrow.</p>',
        'with the Oracle CVSS&nbsp;10.0 flaw due tomorrow and a <b>Pizza Hut and Taco Bell franchise operator</b> newly on '
        'record with the Texas Attorney General over a breach exposing <b>Social Security numbers</b>.</p>', 'idx cy p')

# mma card: append rankings movement
h = rep(h, 'the White House card lost about <b>$30&nbsp;million</b> on roughly <b>$60&nbsp;million</b> of production.</p>',
        'the White House card lost about <b>$30&nbsp;million</b> on roughly <b>$60&nbsp;million</b> of production &mdash; and '
        'the official rankings have now moved on Sacramento, with <b>Gregory Rodrigues up three to #7 at middleweight</b>.</p>',
        'idx mma p')
open(p, 'w', encoding='utf-8').write(h)

if FAIL:
    print("FAILURES:"); [print(" -", f) for f in FAIL]; sys.exit(1)
print("edits_1250 applied cleanly")
