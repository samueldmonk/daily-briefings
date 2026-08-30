#!/usr/bin/env python3
"""Add this run's source URLs to each page footer, first-occurrence-wins dedupe."""
import re, sys, io, os
D = sys.argv[1]

NEW = {
 'wallstreet-briefing.html': [
   ('https://www.newyorkfed.org/research/calendars/i-sep26.html',
    'New York Fed &mdash; Economic Indicators Calendar, September 2026'),
   ('https://equityclock.com/2026/08/28/stock-market-outlook-for-august-31-2026/',
    'Equity Clock &mdash; Stock Market Outlook for August 31, 2026 (September seasonality)'),
   ('https://www.advisorperspectives.com/dshort/updates/2026/08/28/treasury-yields-snapshot-august-28-2026',
    'Advisor Perspectives &mdash; Treasury Yields Snapshot, August 28, 2026'),
   ('https://www.cnbc.com/2026/08/27/stock-market-today-live-updates.html',
    'CNBC &mdash; S&amp;P 500 falls Friday after Warsh highlights inflation worries'),
 ],
 'cyber-briefing.html': [
   ('https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog',
    'CISA &mdash; Adds Three Known Exploited Vulnerabilities to Catalog (Aug 27, 2026)'),
   ('https://www.tenable.com/blog/microsofts-august-2026-patch-tuesday-addresses-398-cves-cve-2026-68820',
    'Tenable &mdash; August 2026 Patch Tuesday addresses 398 CVEs (competing count)'),
   ('https://www.securityweek.com/august-2026-patch-tuesday-microsoft-fixes-421-cves-one-exploited-zero-day/',
    'SecurityWeek &mdash; August 2026 Patch Tuesday: 421 CVEs, one exploited zero-day'),
   ('https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html',
    'The Hacker News &mdash; Three CVSS 10.0 ServiceNow flaws'),
 ],
 'mma-briefing.html': [
   ('https://en.wikipedia.org/wiki/UFC_Fight_Night:_Hooker_vs._Parnasse',
    'UFC Fight Night: Hooker vs. Parnasse &mdash; card and odds'),
   ('https://www.ufc.com/news/ufc-fight-night-shanghai-2026-bonus-coverage',
    'UFC.com &mdash; UFC Shanghai bonus coverage'),
   ('https://sports.yahoo.com/articles/umar-nurmagomedov-releases-statement-following-161222125.html',
    'Yahoo Sports &mdash; Umar Nurmagomedov statement after UFC Shanghai'),
   ('https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions',
    'ESPN &mdash; Current and all-time UFC champions'),
   ('https://en.wikipedia.org/wiki/UFC_331',
    'UFC 331 &mdash; Van vs. Pantoja 2, Sept 19, Crypto.com Arena'),
 ],
}

for fn, links in NEW.items():
    p = os.path.join(D, fn)
    h = io.open(p, encoding='utf-8').read()
    fi = h.rfind('Sources')
    if fi == -1:
        print(f'{fn}: no Sources footer'); continue
    have = set(re.findall(r'href="(https?://[^"]+)"', h[fi:]))
    add = [(u, t) for u, t in links if u not in have]
    if not add:
        print(f'{fn}: no new sources'); continue
    # append inside the last <ul>/list in the footer, else before the footer's close
    ins = h.rfind('</ul>', fi)
    frag = ''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for u, t in add)
    if ins == -1:
        ins = h.rfind('</div>', fi)
        frag = ''.join(f'<a href="{u}" target="_blank" rel="noopener">{t}</a> &middot; ' for u, t in add)
    h = h[:ins] + frag + h[ins:]
    # first-occurrence-wins dedupe across the whole footer
    fi2 = h.rfind('Sources')
    seen, out, pos = set(), [], fi2
    def dedupe(seg):
        seen_local = set()
        def rm(m):
            u = m.group(1)
            if u in seen_local:
                return ''
            seen_local.add(u)
            return m.group(0)
        return re.sub(r'<li><a href="(https?://[^"]+)".*?</li>', rm, seg, flags=re.S)
    h = h[:fi2] + dedupe(h[fi2:])
    io.open(p, 'w', encoding='utf-8').write(h)
    print(f'{fn}: +{len(add)} sources')
