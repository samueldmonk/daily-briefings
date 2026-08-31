#!/usr/bin/env python3
"""Restamp all four pages, refresh sources footers, mirror summaries onto index."""
import io, re

STAMP = '1:41 PM ET'
FRESH = 'Data as of 1:41 PM ET &middot; briefings refresh every 30 minutes, 8 AM&ndash;6 PM ET'
PAGES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']

for p in PAGES:
    h = io.open(p, encoding='utf-8').read()
    h = re.sub(r'(<span id="updated">)[^<]*(</span>)', r'\g<1>' + STAMP + r'\g<2>', h)
    h = re.sub(r'(<span class="pill" id="edition">)[^<]*(</span>)', r'\g<1>Midday Edition\g<2>', h)
    h = re.sub(r'(<span class="pill" id="datestamp">)[^<]*(</span>)',
               r'\g<1>Monday, August 31, 2026\g<2>', h)
    h = re.sub(r'(<div class="freshline" id="freshline">).*?(</div>)',
               r'\g<1>' + FRESH + r'\g<2>', h, flags=re.S)
    io.open(p, 'w', encoding='utf-8').write(h)
    print('restamped', p)

NEW_SRC = {
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
],
'cyber-briefing.html': [
 ('The Hacker News &mdash; front page (Silver Fox / ValleyRAT, Aurora, Fire Ant), fetched Aug 31 2026',
  'https://thehackernews.com/'),
 ('Security Affairs &mdash; Read, think, share (breach and malware reporting), fetched Aug 31 2026',
  'https://securityaffairs.com/'),
 ('The Hacker News &mdash; CISA Adds Six Exploited Flaws to KEV, Including NetScaler, Linux, and SQL Server Bugs',
  'https://thehackernews.com/2026/08/cisa-adds-six-exploited-flaws-to-kev.html'),
 ('CISA &mdash; Adds Six Known Exploited Vulnerabilities to Catalog (August 26, 2026)',
  'https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog'),
 ('CISA &mdash; Adds Two Known Exploited Vulnerabilities to Catalog (August 20, 2026)',
  'https://www.cisa.gov/news-events/alerts/2026/08/20/cisa-adds-two-known-exploited-vulnerabilities-catalog'),
 ('CISA &mdash; Adds Four Known Exploited Vulnerabilities to Catalog (August 18, 2026)',
  'https://www.cisa.gov/news-events/alerts/2026/08/18/cisa-adds-four-known-exploited-vulnerabilities-catalog'),
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
 ('Wikipedia &mdash; 2026 in UFC',
  'https://en.wikipedia.org/wiki/2026_in_UFC'),
],
}

for p, srcs in NEW_SRC.items():
    h = io.open(p, encoding='utf-8').read()
    m = re.search(r'(<ul class="srclist">)(.*?)(</ul>)', h, re.S)
    if not m:
        print('  !! no srclist in', p); continue
    existing = m.group(2)
    add = ''
    for label, url in srcs:
        if url in existing:
            continue
        add += '<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (url, label)
    if add:
        h = h[:m.start(2)] + add + existing + h[m.end(2):]
        io.open(p, 'w', encoding='utf-8').write(h)
    print('sources refreshed', p, '(+%d)' % add.count('<li>'))

# ------------------------------------------------------------------ index mirror
h = io.open('index.html', encoding='utf-8').read()

CY = ('<p><b>Three new actors, and none of them needed a new vulnerability.</b> <b>Fire Ant</b>, a '
'<b>China-nexus espionage actor</b>, has expanded onto <b>Cisco IOS XR routers, TACACS servers and Linux '
'management hosts</b> &mdash; the three places network access is <i>granted</i> rather than used, and none of them '
'where endpoint detection lives. <b>Silver Fox</b> is shipping the <b>ValleyRAT</b> backdoor inside a signed '
'Chinese adware application built around <b>QN Wallpaper, a genuine product</b> (Kaspersky). <b>Aurora</b> '
'ransomware operators are reported by <b>CloudSEK</b> and <b>Gambit Security</b> using the AI coding assistant '
'<b>Cursor</b> to break into networks &mdash; &#9888; <b>published with its vendor attribution struck</b>, '
'unsourced. <b>KEV twenty-fifth check: nothing later than August 27.</b></p>')

WS = ('<p><b>The first live reading of the day that states its own clock.</b> As of about <b>1:31 PM EDT</b>, the '
'<b>Dow slipped 0.5%</b>, the <b>S&amp;P 500 declined 0.4%</b> and the <b>Nasdaq Composite fell 0.3%</b> &mdash; '
'<b>inverting the running order</b>, with tech now the shallowest decline. It arrived in the same return as the '
'mis-shelved recap, <b>refused for a fifth and sixth time</b>, proving a return is not clean or dirty as a whole. '
'&#9888; <b>A live two-year and ten-year yield cleared the bar for the first time</b> &mdash; <b>4.35% and 4.76%</b>, '
'each naming <b>Friday&rsquo;s 4.34% and 4.73%</b> as its baseline, which is exactly what this page carries. '
'<b>PG&amp;E &minus;20.0%</b> joins <b>Edison International</b> on the California wildfire bill.</p>')

MM = ('<p><b>September 26 finally has a venue and a card.</b> A newly-booked-fights tracker for the week ending '
'<b>August 30</b> lists it as the <b>TUF 34 Bantamweight Finale</b> at the <b>Meta APEX</b>, with '
'<b>Osmanli vs Akylbek Uulu</b>, <b>Rodolfo Vieira vs Robert Bryczek</b> and <b>Brady Hiestand vs Rinya Nakamura</b> '
'&mdash; &#9888; <b>corroboration, not reconciliation</b>; the three competing event names stay apart. A '
'<b>nineteenth champions cross-check</b> returned <b>six men&rsquo;s divisions from ESPN and matched all six</b>; the '
'women&rsquo;s and smaller men&rsquo;s classes did not return, and <b>an omission is not evidence against a row</b>. '
'<b>Board unchanged &mdash; seventy-sixth consecutive edition.</b></p>')

for cls, body in (('c-cy', CY), ('c-ws', WS), ('c-mm', MM)):
    pat = re.compile(r'(<div class="bigcard %s">.*?<div class="sub">[^<]*</div>\s*)<p>.*?</p>' % cls, re.S)
    h2 = pat.sub(lambda m: m.group(1) + body, h, count=1)
    assert h2 != h, 'index card %s not replaced' % cls
    h = h2

io.open('index.html', 'w', encoding='utf-8').write(h)
print('index mirrored')
