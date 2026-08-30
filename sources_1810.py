#!/usr/bin/env python3
"""One job: append this run's source URLs to each page footer, then de-duplicate by href."""
import io, sys, re
REPO = sys.argv[1]

ADD = {
 'wallstreet-briefing.html': [
   ('https://wtop.com/national/2026/08/how-major-us-stock-indexes-fared-friday-8-28-2026/',
    'WTOP &mdash; How major US stock indexes fared Friday 8/28/2026 (weekly changes; Russell 2000)'),
   ('https://www.schwab.com/learn/story/weekly-traders-outlook',
    'Charles Schwab &mdash; Weekly Trader&rsquo;s Stock Market Outlook'),
   ('https://finance.yahoo.com/markets/live/stock-market-today-friday-august-28-dow-sp-500-nasdaq-dip-fed-warsh-jackson-hole-speech-081514091.html',
    'Yahoo Finance &mdash; Dow, S&amp;P 500, Nasdaq end week on down note as rate-hike bets jump'),
   ('https://www.cnbc.com/2026/08/27/stock-market-today-live-updates.html',
    'CNBC &mdash; Stock market news for Aug. 28, 2026'),
 ],
 'cyber-briefing.html': [
   ('https://sharkstriker.com/blog/august-2026-data-breaches/',
    'SharkStriker &mdash; Top data breaches of August 2026 (leak-site listings: Questal, Hyundai Motor T&uuml;rkiye, ProHealth)'),
   ('https://www.helpnetsecurity.com/2026/08/27/netscaler-adc-gateway-cve-2026-8452/',
    'Help Net Security &mdash; NetScaler ADC/Gateway CVE-2026-8452 (fixed builds; companion CVE-2026-19490)'),
   ('https://www.securityweek.com/recent-citrix-netscaler-vulnerability-exploited-in-the-wild/',
    'SecurityWeek &mdash; Recent Citrix NetScaler vulnerability exploited in the wild'),
   ('https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog',
    'CISA &mdash; Adds six known exploited vulnerabilities to catalog (Aug 26, 2026)'),
   ('https://labs.cloudsecurityalliance.org/research/ciso-daily-briefing-20260828/',
    'CSA Lab Space &mdash; CISO Daily Briefing, Aug 28 2026 (source of the Iran-linked claim refused above)'),
 ],
 'mma-briefing.html': [
   ('https://sports.yahoo.com/articles/ufc-fight-night-287-dan-175030528.html',
    'Yahoo Sports &mdash; UFC Fight Night 287: Hooker vs. Parnasse odds (BetWay: Parnasse &minus;400 / Hooker +300)'),
   ('https://x.com/FightOdds_io/status/2085561916059947238',
    'FightOdds.io &mdash; UFC Fight Night 287 opening odds (Parnasse &minus;357 / Hooker +275)'),
   ('https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions',
    'ESPN &mdash; Current and all-time UFC champions (twelfth cross-check; eight cells returned)'),
   ('https://www.ufc.com/event/ufc-fight-night-september-05-2026',
    'UFC.com &mdash; UFC Fight Night: Hooker vs Parnasse (UFC Paris, Sept 5)'),
   ('https://www.cbssports.com/ufc/event/31001542/ufc-fight-night-hooker-vs-parnasse-september-05-2026/',
    'CBS Sports &mdash; UFC Fight Night: Hooker vs. Parnasse fight card'),
 ],
}

for f, links in ADD.items():
    p = REPO + '/' + f
    h = io.open(p, encoding='utf-8').read()
    i = h.find('<div class="srcs">')
    assert i >= 0, f
    j = i + len('<div class="srcs">')
    new = ''.join('<a href="%s">%s</a><br>' % (u, t) for u, t in links)
    h = h[:j] + new + h[j:]
    # de-duplicate by href, keeping first occurrence
    k = h.find('<div class="srcs">')
    e = h.find('</div>', k)
    block = h[k + len('<div class="srcs">'):e]
    parts = re.findall(r'<a href="([^"]+)">.*?</a>', block)
    seen, out, dropped = set(), [], 0
    for m in re.finditer(r'<a href="([^"]+)">.*?</a>(?:<br>)?', block):
        href = m.group(1)
        if href in seen:
            dropped += 1
            continue
        seen.add(href)
        a = re.match(r'<a href="[^"]+">.*?</a>', m.group(0)).group(0)
        out.append(a)
    rest = re.sub(r'<a href="[^"]+">.*?</a>(?:<br>)?', '', block).strip()
    h = h[:k] + '<div class="srcs">' + '<br>'.join(out) + ('<br>' + rest if rest else '') + h[e:]
    assert all(u.startswith('https://') for u in seen), f
    io.open(p, 'w', encoding='utf-8').write(h)
    print('%-26s +%d links, %d dupes dropped, %d unique' % (f, len(links), dropped, len(seen)))
