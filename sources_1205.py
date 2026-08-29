#!/usr/bin/env python3
"""Add this run's newly fetched sources to each footer, skipping any href already present."""
import io, re

ADDS = {
 'mma-briefing.html': [
   ("https://www.si.com/fannation/mma/news/ufc-fans-justin-gaethje-fight-news-major-update-manager",
    "SI/FanNation &mdash; Justin Gaethje fight news: major update from his manager"),
   ("https://sports.yahoo.com/articles/justin-gaethje-says-fight-lightweight-195855780.html",
    "Yahoo Sports &mdash; Justin Gaethje says who should fight for the lightweight title next"),
   ("https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions",
    "ESPN &mdash; Current and all-time UFC champions (checked again 12:05 PM)"),
 ],
 'cyber-briefing.html': [
   ("https://www.itsecurityguru.org/2026/08/28/manchester-airports-group-cyberattack/",
    "IT Security Guru &mdash; Manchester Airports Group cyberattack exposes data of 8.7 million customers"),
   ("https://www.bleepingcomputer.com/news/security/mckesson-discloses-breach-after-shinyhunters-claims-patient-data-theft/",
    "BleepingComputer &mdash; McKesson discloses breach after ShinyHunters claims patient data theft"),
 ],
 'wallstreet-briefing.html': [
   ("https://finance.yahoo.com/markets/live/stock-market-today-friday-august-28-dow-sp-500-nasdaq-dip-fed-warsh-jackson-hole-speech-081514091.html",
    "Yahoo Finance &mdash; Stock market today, Friday August 28: Dow, S&amp;P 500, Nasdaq and the Warsh speech"),
   ("https://www.cnbc.com/2026/08/27/stock-market-today-live-updates.html",
    "CNBC &mdash; Stock market news for Aug. 28, 2026 (week-ahead: pre-speech odds, Kalshi 48%)"),
 ],
}

for path, items in ADDS.items():
    h = io.open(path, encoding='utf-8').read()
    m = re.search(r'<div class="srcs">.*?</div>', h, re.S)
    if not m:
        print('NO FOOTER', path); continue
    block = m.group(0)
    added = []
    ins = ''
    for href, label in items:
        if href in h:
            continue
        ins += '<br><a href="%s">%s</a>' % (href, label)
        added.append(href)
    if ins:
        newblock = block[:-len('</div>')] + ins + '</div>'
        h = h.replace(block, newblock, 1)
        io.open(path, 'w', encoding='utf-8').write(h)
    hrefs = re.findall(r'<a href="([^"]+)"', re.search(r'<div class="srcs">.*?</div>', h, re.S).group(0))
    dupes = [x for x in set(hrefs) if hrefs.count(x) > 1]
    print('%-26s added=%d links=%d dupes=%s' % (path, len(added), len(hrefs), dupes or 'none'))
