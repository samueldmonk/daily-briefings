#!/usr/bin/env python3
"""Rewrite each page's sources footer to the links fetched this run."""
import io, re

SRC = {
'wallstreet-briefing.html': [
 ('TheStreet &mdash; Stock Market Today (Aug. 31, 2026): Russell 2000, S&amp;P 500 fall to start week',
  'https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-31-2026'),
 ('Washington Times &mdash; Oil prices rise and stocks fall after U.S. hits Iranian sites in the Strait of Hormuz (Aug 31)',
  'https://www.washingtontimes.com/news/2026/aug/31/oil-prices-increase-stocks-fall-us-hits-iranian-sites-strait-hormuz/'),
 ('Yahoo Finance &mdash; Bond markets face fresh selling as oil prices jump, stocks cautious',
  'https://finance.yahoo.com/markets/articles/shares-skid-asia-oil-yields-003835124.html'),
 ('Yahoo Finance &mdash; Energy stocks lead in subdued final trading day of August, utilities under pressure',
  'https://finance.yahoo.com/markets/article/energy-stocks-lead-in-subdued-final-trading-day-of-august-utilities-under-pressure-alphacheck-142014111.html'),
 ('Yahoo Finance &mdash; Dow, S&amp;P 500, Nasdaq futures fall as US strikes Iran, rate-hike bets jump',
  'https://finance.yahoo.com/markets/live/stock-market-today-monday-august-31-dow-sp-500-nasdaq-113851714.html'),
 ('CNBC &mdash; Stock futures fall after U.S. strikes Iran; Wall Street heads for winning month',
  'https://www.cnbc.com/2026/08/30/stock-market-today-live-updates.html'),
 ('Bloomberg &mdash; Latest Oil Market News and Analysis for Aug. 31',
  'https://www.bloomberg.com/news/articles/2026-08-30/latest-oil-market-news-and-analysis-for-aug-31'),
],
'cyber-briefing.html': [
 ('The Hacker News &mdash; front page (Silver Fox / ValleyRAT, Aurora, Fire Ant), fetched Aug 31 2026',
  'https://thehackernews.com/'),
 ('Security Affairs &mdash; Read, think, share (breach and malware reporting), fetched Aug 31 2026',
  'https://securityaffairs.com/'),
 ('SecurityWeek &mdash; Cybersecurity News, Insights and Analysis',
  'https://www.securityweek.com/'),
 ('The Hacker News &mdash; CISA Adds Six Exploited Flaws to KEV, Including NetScaler, Linux, and SQL Server Bugs',
  'https://thehackernews.com/2026/08/cisa-adds-six-exploited-flaws-to-kev.html'),
 ('CISA &mdash; Adds Six Known Exploited Vulnerabilities to Catalog (August 26, 2026)',
  'https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog'),
 ('CISA &mdash; Adds Two Known Exploited Vulnerabilities to Catalog (August 20, 2026)',
  'https://www.cisa.gov/news-events/alerts/2026/08/20/cisa-adds-two-known-exploited-vulnerabilities-catalog'),
 ('CISA &mdash; Adds Four Known Exploited Vulnerabilities to Catalog (August 18, 2026)',
  'https://www.cisa.gov/news-events/alerts/2026/08/18/cisa-adds-four-known-exploited-vulnerabilities-catalog'),
 ('CISA &mdash; Adds Three Known Exploited Vulnerabilities to Catalog (August 11, 2026)',
  'https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog'),
 ('CISA &mdash; Adds One Known Exploited Vulnerability to Catalog (August 7, 2026)',
  'https://www.cisa.gov/news-events/alerts/2026/08/07/cisa-adds-one-known-exploited-vulnerability-catalog'),
 ('CISA &mdash; Known Exploited Vulnerabilities Catalog',
  'https://www.cisa.gov/known-exploited-vulnerabilities-catalog'),
],
'mma-briefing.html': [
 ('ESPN &mdash; Current and all-time UFC champions',
  'https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions'),
 ('Fightomic &mdash; Newly Booked UFC Fights: Week Ending 30 August 2026',
  'https://fightomic.com/newly-booked-ufc-fights-week-ending-30-august-2026/'),
 ('Yahoo Sports &mdash; UFC Fight Night 287: Dan Hooker vs. Salahdine Parnasse odds, what to know',
  'https://sports.yahoo.com/articles/ufc-fight-night-287-dan-175030528.html'),
 ('Yahoo Sports &mdash; UFC Paris: How to watch Dan Hooker vs. Salahdine Parnasse, lineup, odds, more',
  'https://sports.yahoo.com/articles/ufc-paris-watch-dan-hooker-125027816.html'),
 ('UFC.com &mdash; UFC Fight Night: Hooker vs Parnasse (September 5, 2026)',
  'https://www.ufc.com/event/ufc-fight-night-september-05-2026'),
 ('Wikipedia &mdash; UFC Fight Night: Hooker vs. Parnasse',
  'https://en.wikipedia.org/wiki/UFC_Fight_Night:_Hooker_vs._Parnasse'),
 ('Wikipedia &mdash; 2026 in UFC',
  'https://en.wikipedia.org/wiki/2026_in_UFC'),
 ('MMA Mania &mdash; UFC Roster Watch Tracker: Cuts, Free Agent Acquisitions',
  'https://www.mmamania.com/ufc-roster-watch-cuts-tracker-free-agent-aquisitions-mma'),
],
}

for p, srcs in SRC.items():
    h = io.open(p, encoding='utf-8').read()
    links = '<br>'.join(
        '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, l) for l, u in srcs)
    new = '<b>Sources checked this run &mdash; 1:41 PM:</b><br>' + links
    h2, n = re.subn(r'<b>Sources checked this run &mdash; [^<]*</b><br>.*?(?=</p>)',
                    lambda m: new, h, count=1, flags=re.S)
    assert n == 1, 'footer not found in ' + p
    io.open(p, 'w', encoding='utf-8').write(h2)
    print('footer rewritten', p, '(%d links)' % len(srcs))

# ---------------------------------------------------------------- index footer
IDXSRC = [
 ('TheStreet &mdash; Stock Market Today (Aug. 31, 2026)',
  'https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-31-2026'),
 ('Yahoo Finance &mdash; Energy stocks lead in subdued final trading day of August, utilities under pressure',
  'https://finance.yahoo.com/markets/article/energy-stocks-lead-in-subdued-final-trading-day-of-august-utilities-under-pressure-alphacheck-142014111.html'),
 ('Yahoo Finance &mdash; Bond markets face fresh selling as oil prices jump, stocks cautious',
  'https://finance.yahoo.com/markets/articles/shares-skid-asia-oil-yields-003835124.html'),
 ('The Hacker News &mdash; front page, fetched Aug 31 2026', 'https://thehackernews.com/'),
 ('Security Affairs &mdash; breach and malware reporting, fetched Aug 31 2026', 'https://securityaffairs.com/'),
 ('CISA &mdash; Known Exploited Vulnerabilities Catalog', 'https://www.cisa.gov/known-exploited-vulnerabilities-catalog'),
 ('ESPN &mdash; Current and all-time UFC champions', 'https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions'),
 ('Fightomic &mdash; Newly Booked UFC Fights: Week Ending 30 August 2026', 'https://fightomic.com/newly-booked-ufc-fights-week-ending-30-august-2026/'),
]
h = io.open('index.html', encoding='utf-8').read()
links = '<br>'.join('<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, l) for l, u in IDXSRC)
new = '<b>Primary sources for the three summaries above &mdash; fetched 1:41 PM ET:</b><br>' + links
h2, n = re.subn(r'<b>Primary sources for the three summaries above &mdash; fetched [^<]*</b><br>.*?(?=</div>)',
                lambda m: new, h, count=1, flags=re.S)
assert n == 1, 'index footer not found'
io.open('index.html', 'w', encoding='utf-8').write(h2)
print('footer rewritten index.html (%d links)' % len(IDXSRC))
