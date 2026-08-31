#!/usr/bin/env python3
"""Restamp all four pages, refresh sources footers, mirror summaries onto index."""
import io, re

STAMP = '1:12 PM ET'
FRESH = 'Data as of 1:12 PM ET &middot; briefings refresh every 30 minutes, 8 AM&ndash;6 PM ET'
PAGES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']

# ---------------------------------------------------------------- restamp
for p in PAGES:
    h = io.open(p, encoding='utf-8').read()
    h = re.sub(r'(<span id="updated">)[^<]*(</span>)', r'\g<1>' + STAMP + r'\g<2>', h)
    h = re.sub(r'(<span class="pill" id="edition">)[^<]*(</span>)',
               r'\g<1>Midday Edition\g<2>', h)
    h = re.sub(r'(<span class="pill" id="datestamp">)[^<]*(</span>)',
               r'\g<1>Monday, August 31, 2026\g<2>', h)
    h = re.sub(r'(<div class="freshline" id="freshline">).*?(</div>)', r'\g<1>' + FRESH + r'\g<2>',
               h, flags=re.S)
    io.open(p, 'w', encoding='utf-8').write(h)
    print('restamped', p)

# ---------------------------------------------------------- sources footers
SRC = {
'wallstreet-briefing.html': [
 ('TheStreet &mdash; Stock Market Today, Aug. 31, 2026',
  'https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-31-2026'),
 ('Bloomberg &mdash; S&amp;P 500 Falls Amid Oil Spike as Middle East Conflict Intensifies (Aug 31)',
  'https://www.bloomberg.com/news/articles/2026-08-31/s-p-500-falls-amid-oil-spike-as-middle-east-conflict-intensifies'),
 ('Yahoo Finance &mdash; Energy stocks lead in subdued final trading day of August, utilities under pressure',
  'https://finance.yahoo.com/markets/article/energy-stocks-lead-in-subdued-final-trading-day-of-august-utilities-under-pressure-alphacheck-142014111.html'),
 ('Yahoo Finance &mdash; Dow, S&amp;P 500, Nasdaq futures fall as US strikes Iran, rate-hike bets jump',
  'https://finance.yahoo.com/markets/live/stock-market-today-monday-august-31-dow-sp-500-nasdaq-113851714.html'),
 ('CNBC &mdash; Stock futures fall after U.S. strikes Iran; Wall Street heads for winning month',
  'https://www.cnbc.com/2026/08/30/stock-market-today-live-updates.html'),
 ('CNBC &mdash; 10-year Treasury yield rises as oil prices gain',
  'https://www.cnbc.com/2026/08/10/us-treasury-yields-investors-eye-key-inflation-data-.html'),
],
'cyber-briefing.html': [
 ('Security Affairs &mdash; Extortion group FulcrumSec claims 86GB Manchester Airports Group data theft',
  'https://securityaffairs.com/198143/cyber-crime/extortion-group-fulcrumsec-claims-86gb-manchester-airports-group-data-theft.html'),
 ('TechNadu &mdash; FulcrumSec claims Manchester Airports hack via exposed Iterable API credentials',
  'https://www.technadu.com/manchester-airports-group-data-breach-fulcrumsec-claims-the-theft-of-86-gb-via-exposed-iterable-api-credentials/634395/'),
 ('BleepingComputer &mdash; Berlin confirms data theft after Rhysida ransomware attack claims',
  'https://www.bleepingcomputer.com/news/security/berlin-confirms-data-theft-after-rhysida-ransomware-attack-claims/'),
 ('Security Affairs &mdash; Rhysida ransomware group targets Berlin government ahead of vote',
  'https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html'),
 ('Security Affairs &mdash; Critical GiveWP flaw lets attackers run commands on WordPress servers',
  'https://securityaffairs.com/198156/security/critical-givewp-flaw-lets-attackers-run-commands-on-wordpress-servers.html'),
 ('Patchstack &mdash; Unauthenticated PHP object injection to RCE on GiveWP',
  'https://patchstack.com/articles/unauthenticated-php-object-injection-to-remote-code-execution-on-givewp/'),
 ('CISA &mdash; Adds Three Known Exploited Vulnerabilities to Catalog (August 27, 2026)',
  'https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog'),
 ('CISA &mdash; Adds Six Known Exploited Vulnerabilities to Catalog (August 26, 2026)',
  'https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog'),
 ('CISA &mdash; Known Exploited Vulnerabilities Catalog',
  'https://www.cisa.gov/known-exploited-vulnerabilities-catalog'),
],
'mma-briefing.html': [
 ('ESPN &mdash; Current and all-time UFC champions',
  'https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions'),
 ('Rogers Place &mdash; UFC Fight Night, October 17, 2026',
  'https://www.rogersplace.com/ufc-fight-night-october-17-2026/'),
 ('Daily Hive &mdash; UFC reveals full fight card for Edmonton event',
  'https://dailyhive.com/edmonton/ufc-reveals-fight-card-edmonton'),
 ('Wikipedia &mdash; UFC Fight Night: Buckley vs. Malott',
  'https://en.wikipedia.org/wiki/UFC_Fight_Night:_Buckley_vs._Malott'),
 ('Fightomic &mdash; Newly booked UFC fights, week ending 30 August 2026',
  'https://fightomic.com/newly-booked-ufc-fights-week-ending-30-august-2026/'),
 ('Wikipedia &mdash; 2026 in UFC',
  'https://en.wikipedia.org/wiki/2026_in_UFC'),
],
}

for p, links in SRC.items():
    h = io.open(p, encoding='utf-8').read()
    m = re.search(r'<footer>', h)
    assert m, p
    block = ('<p><b>Sources checked this run &mdash; 1:12 PM:</b><br>'
             + '<br>'.join('<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)
                           for t, u in links)
             + '</p>')
    h = h[:m.end()] + block + h[m.end():]
    io.open(p, 'w', encoding='utf-8').write(h)
    print('sources appended', p, len(links), 'links')

# ------------------------------------------------------ index card mirroring
CARDS = {
'c-cy': ('<b>The Manchester Airports breach now has an attacker and a method.</b> '
 'The extortion group <b>FulcrumSec</b> claims <b>86 GB</b> from <b>Manchester Airports Group</b>, '
 'saying it found <b>Iterable API credentials inside client-side JavaScript</b> &mdash; readable by '
 'anyone with browser developer tools. Samples shared with reporters include a <b>21.5 GB Manchester '
 'export</b> and <b>nearly 200,000 records</b> for travel booked across the rest of 2026, against the '
 '<b>8.7 million customers</b> MAG itself disclosed. &#9888; <b>The volumes are the attacker&rsquo;s; '
 'the 8.7 million is the company&rsquo;s.</b> Also: <b>Berlin confirms data theft</b> after '
 '<b>Rhysida</b> claimed <b>5.79 TB</b> three weeks before a September 20 state election and says it '
 'will not pay; <b>CVE-2026-82222</b> in <b>GiveWP</b> is rated <b>10.0</b>, fixed in <b>4.16.7.2</b>. '
 '<b>KEV twenty-fourth check: nothing later than August 27.</b>'),
'c-ws': ('<b>The mis-shelved recap was refused a fourth time, and this pass it labelled itself.</b> '
 'Asked for today&rsquo;s levels at <b>around 1 PM ET</b>, the wrap dated <b>August 31</b> returned '
 '<b>S&amp;P 500 7,711.76</b>, <b>Nasdaq 26,402.42</b> and <b>Dow 53,885.10 (&minus;464 pts)</b> as '
 '<b>&ldquo;closing values&rdquo;</b>, noting the market &ldquo;had already closed&rdquo; &mdash; '
 'six hours early, with two levels being Friday&rsquo;s verified closes. '
 '<b>Refused in full.</b> The live tape gives an eighth rendering: <b>Dow &minus;315 points, '
 '&minus;0.6%</b>, <b>S&amp;P 500 off about half a percent</b>, <b>energy the only sector higher</b> on '
 'the Strait of Hormuz escalation and <b>utilities &minus;1.6%</b>. '
 '<b>No index level published for the live session.</b>'),
'c-mm': ('<b>Eighteenth champions cross-check, and the first complete one this page has recorded &mdash; '
 'all eleven divisions returned, all eleven matched.</b> The ESPN-sourced sweep reached the '
 '<b>women&rsquo;s divisions and both smaller men&rsquo;s classes</b> that the last four checks missed, '
 'confirming <b>Yan</b>, <b>Van</b>, <b>Harrison</b>, <b>Shevchenko</b> and <b>Dern</b> alongside the '
 'usual six. <b>Board unchanged &mdash; seventy-fifth consecutive edition</b>, with <b>no row carried '
 'unverified</b> for the first time in weeks. <b>UFC Edmonton</b> is fully booked for <b>October 17 at '
 'Rogers Place</b>: <b>Joaquin Buckley vs Mike Malott</b>, co-main <b>Erin Blanchfield vs Jasmine '
 'Jasudavicius</b>. <b>UFC Paris is Saturday</b> &mdash; <b>Parnasse &minus;550, Hooker +400</b>.'),
}

h = io.open('index.html', encoding='utf-8').read()
for cls, text in CARDS.items():
    m = re.search(r'(<div class="bigcard %s">.*?<div class="sub">[^<]*</div>\s*<p>)(.*?)(</p>)'
                  % cls, h, flags=re.S)
    assert m, cls
    h = h[:m.start(2)] + text + h[m.end(2):]
    print('index card updated', cls)

# index sources footer — REPLACE the stale block, do not stack a second one
ALL = []
for links in SRC.values():
    ALL.extend(links)
blk = ('<div class="srcs"><b>Primary sources for the three summaries above '
       '&mdash; fetched 1:12 PM ET:</b><br>'
       + '<br>'.join('<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)
                     for t, u in ALL) + '</div>')
m = re.search(r'<footer><div class="srcs">.*?</div>', h, flags=re.S)
assert m, 'index srcs block'
h = h[:m.start()] + '<footer>' + blk + h[m.end():]
io.open('index.html', 'w', encoding='utf-8').write(h)
print('index sources:', len(ALL), 'links')
