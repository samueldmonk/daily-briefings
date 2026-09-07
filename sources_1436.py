# -*- coding: utf-8 -*-
"""Edition 2026-09-07-1436: append this run's sources into each page's srcs panel."""
import sys, os
REPO = sys.argv[1]
P = lambda n: os.path.join(REPO, n)
rep = []

ED = "2:36 PM ET edition"
SEP = " &nbsp;&middot;&nbsp; "

SRC = {
 "wallstreet-briefing.html": [
   ("KuCoin", "https://www.kucoin.com/news/flash/u-s-markets-closed-on-sept-7-for-labor-day-futures-trading-ends-early",
    "U.S. markets closed on September 7 for Labor Day; futures trading ends early",
    "the relayed CME and ICE holiday halt times (01:00, 01:30 and 02:30 UTC+8 on 8 September)."),
   ("Trading Economics", "https://tradingeconomics.com/commodity/brent-crude-oil",
    "Brent Crude Oil &mdash; price, chart, historical data, news",
    "the eighth Brent reading, $97.68 up 1.45%, alongside the $97.39 up 1.15% already carried."),
 ],
 "cyber-briefing.html": [
   ("The Hacker News", "https://thehackernews.com/2026/09/extradited-russian-hacker-faces-charges.html",
    "Extradited Russian Hacker Faces Charges Over Excel Malware Campaign That Infected Thousands", ""),
   ("BleepingComputer", "https://www.bleepingcomputer.com/news/security/us-charges-russian-for-infecting-80-000-freelancers-with-malware/",
    "US charges Russian for infecting 80,000 freelancers with malware", ""),
   ("Help Net Security", "https://www.helpnetsecurity.com/2026/09/03/russian-national-indicted-freelance-platform-malware/",
    "Russian man indicted for spreading malware to 80,000 freelancers", "(3 Sep 2026)."),
   ("Infosecurity Magazine", "https://www.infosecurity-magazine.com/news/russian-man-extradited-malware/",
    "Russian Man Extradited Over Malware Campaign Targeting Freelancers",
    "&mdash; the arrest, extradition and court-appearance dates."),
 ],
 "mma-briefing.html": [
   ("Bloody Elbow", "https://bloodyelbow.com/2026/09/04/roberto-soldic-signs-ufc-snap-up-former-two-weight-champion-who-knocked-out-dricus-du-plessis/",
    "Roberto Soldic signs: UFC snap up former two-weight champion", "(4 Sep 2026)."),
   ("Yahoo Sports", "https://ca.sports.yahoo.com/news/former-ksw-champ-roberto-soldic-202728245.html",
    "Former KSW champ Roberto Soldic signs for UFC 332 octagon debut",
    "&mdash; the Khaos Williams pairing, the Delta Center date and the 1&ndash;1 Du Plessis series."),
   ("Bloody Elbow", "https://bloodyelbow.com/2026/09/03/ufc-334-gets-its-first-fight-as-11-1-former-mma-champion-books-return-at-madison-square-garden/",
    "UFC 334 gets its first fight at Madison Square Garden", "(3 Sep 2026)."),
   ("Sports Illustrated", "https://www.si.com/fannation/mma/news/first-fight-booked-ufc-334-card-madison-square-garden",
    "First Fight Booked for UFC 334 Card at Madison Square Garden", ""),
 ],
}

for f, items in SRC.items():
    h = open(P(f), encoding="utf-8").read()
    i = h.find('<div class="panel srcs">')
    if i < 0:
        rep.append("MISS  " + f); continue
    j = i + len('<div class="panel srcs">')
    add = ""
    n = 0
    for pub, url, title, tail in items:
        if url in h:
            continue
        add += ('<b>Search return, %s</b> &mdash; %s, <a href="%s">%s</a>%s%s'
                % (ED, pub, url, title, (" " + tail) if tail else ".", SEP))
        n += 1
    h = h[:j] + add + h[j:]
    open(P(f), "w", encoding="utf-8").write(h)
    rep.append("ok    sources %s (+%d)" % (f, n))

print("\n".join(rep))
