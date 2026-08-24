#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MMA + index edits for the 2026-08-24 ~1:05pm ET Midday Edition run."""
import io
D = "/sessions/amazing-bold-curie/mnt/outputs/"
FAIL = []
def load(f): return io.open(D+f, encoding="utf-8").read()
def save(f, s): io.open(D+f, "w", encoding="utf-8").write(s)
def rep(s, old, new, label, count=1):
    n = s.count(old)
    if n != count:
        FAIL.append("MISS[%s] found %d expected %d" % (label, n, count)); return s
    return s.replace(old, new)

# ============================== MMA ==============================
m = load("mma-briefing.html")

m = rep(m,
 u'<div class="tldr"><b>Tale of the Tape</b> <span>Gregory Rodrigues outlasted Anthony Hernandez over five rounds in Sacramento for his fourth straight win and called out No.&nbsp;2-ranked Dricus du Plessis; the promotion now turns to Shanghai on Saturday, with the numbered calendar filled through the year &mdash; UFC&nbsp;333 in Abu Dhabi in October, Madison Square Garden in November and Las Vegas in December.</span></div>',
 u'<div class="tldr"><b>Tale of the Tape</b> <span>Gregory Rodrigues outlasted Anthony Hernandez over five rounds in Sacramento for his fourth straight win and called out No.&nbsp;2-ranked Dricus du Plessis; the promotion turns to Shanghai on Saturday, and UFC&nbsp;332 in Salt Lake City has quietly grown a championship fight &mdash; Valentina Shevchenko is reported to defend the women&rsquo;s flyweight title against Natália Silva, who has won eight straight in the UFC and beaten three former champions in her last three fights.</span></div>',
 "mma-tldr")

# --- UFC 332 card: add Shevchenko/Silva + the fuller bout list ---
m = rep(m,
 u'<div class="tags"><span class="tag">Main event TBA</span><span class="tag hot">RDA returns</span></div>\n<h3>UFC 332: Johnny Walker moves to heavyweight against Mick Parkin</h3>',
 u'<div class="tags"><span class="tag">Main event TBA</span><span class="tag hot">Title fight reported</span><span class="tag hot">RDA returns</span></div>\n<h3>UFC 332: a women&rsquo;s flyweight title fight is reported for the co-main, and the main event is still blank</h3>',
 "mma-332-head")

m = rep(m,
 u'<p><b>Added to this board this edition: Rafael dos Anjos returns against Alexander Hernandez.</b>',
 u'<p><b>Added to this board this edition: a championship bout.</b> A UFC women&rsquo;s flyweight title fight between reigning two-time champion <b>Valentina Shevchenko</b> and <b>Natália Silva</b> is reported to be set as the co-main event. The matchup was first reported by ESPN Brasil; the UFC has not made an official announcement, so it is carried here as reported rather than confirmed. Silva arrives on eight consecutive UFC wins, and her last three outings were unanimous decisions over three former champions &mdash; Rose Namajunas, Alexa Grasso and Jessica Andrade.</p>\n'
 u'<p><b>The rest of the announced card.</b> Alongside Walker vs Parkin, the bouts announced for October 3 include Deiveson Figueiredo vs Payton Talbott, Roman Kopylov vs Ateba Gautier, Damian Pinas vs Andrey Pulyaev, Marvin Vettori vs Ismail Naurdiev, Court McGee vs Eric Nolan and Imanol Rodríguez vs Alden Coria. The event is the promotion&rsquo;s fifth visit to Salt Lake City and its first since UFC 307 in October 2024.</p>\n'
 u'<p><b>Rafael dos Anjos returns against Alexander Hernandez.</b>',
 "mma-332-body")

m = rep(m,
 u'<p class="note">Odds: not stated in any source fetched this run. The dos Anjos booking was reported on August 21 and so predates the previous archived snapshot, which is why it carries no New tag.</p>',
 u'<p class="note">Odds: not stated in any source fetched this run. Both the Shevchenko&ndash;Silva report and the dos Anjos booking were reported on August 21 and so predate the previous archived snapshot, which is why neither carries a New tag. Sources for this card fetched this run: Heavy, Yahoo Sports, Bloody Elbow, MMA Sucka, Sports Illustrated and Wikipedia&rsquo;s UFC 332 page.</p>',
 "mma-332-note")

m = rep(m,
 u'<li>Yahoo Sports — UFC 332 adds several new bouts, including Johnny Walker&rsquo;s heavyweight debut</li>',
 u'<li>Heavy — Multiple Fights Announced for UFC 332 in Salt Lake City (Aug 2026) — https://heavy.com/sports/ufc/fights-ufc-332-salt-lake-city/</li>\n'
 u'<li>Bloody Elbow — UFC 332 reportedly adds title fight following main event speculation for Salt Lake City (Aug 21, 2026) — https://bloodyelbow.com/2026/08/21/ufc-322-reportedly-adds-title-fight-following-main-event-speculation-for-salt-lake-city/</li>\n'
 u'<li>MMA Sucka — Valentina Shevchenko vs. Natalia Silva title fight reportedly set for UFC 332 — https://mmasucka.com/news/valentina-shevchenko-vs-natalia-silva-title-fight-reportedly-set-for-ufc-332/</li>\n'
 u'<li>Wikipedia — UFC 332 (announced bout list, read this run) — https://en.wikipedia.org/wiki/UFC_332</li>\n'
 u'<li>ESPN — Current and all-time UFC champions (champions board cross-checked this run) — https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions</li>\n'
 u'<li>Yahoo Sports — UFC 332 adds several new bouts, including Johnny Walker&rsquo;s heavyweight debut</li>',
 "mma-sources")
save("mma-briefing.html", m)

# ============================== INDEX ==============================
x = load("index.html")

x = rep(x,
 u'<p>Iran-linked hackers took a British power plant offline for four days in the first cyberattack known to have halted a UK generating station &mdash; and the Treasury Secretary details the US sanctions response at 1 p.m. ET today &mdash; while CISA&rsquo;s remediation deadline for an actively exploited Zimbra command-injection flaw falls today and eight other Known Exploited Vulnerabilities entries tracked here are already past due.</p>',
 u'<p>Iran-linked hackers took a British power plant offline for four days in the first cyberattack known to have halted a UK generating station &mdash; the Treasury Secretary details the US sanctions response at 1 p.m. ET as this edition publishes &mdash; while CISA&rsquo;s remediation deadline for an actively exploited Zimbra command-injection flaw falls today, eight other Known Exploited Vulnerabilities entries tracked here are already past due, and a maximum-severity SAP Commerce Cloud flaw is drawing exploitation attempts against honeypots.</p>',
 "ix-cy")

x = rep(x,
 u'<h2>Washington may open Apple to Chinese memory &mdash; and the whole complex gapped down</h2>',
 u'<h2>Chips keep the Nasdaq red as Bessent takes the podium</h2>', "ix-ws-h2")
x = rep(x,
 u'<p>The chip slide now has a named cause &mdash; weekend reports that Washington may let Apple buy memory from China&rsquo;s CXMT and YMTC knocked SanDisk down 9% and Micron and Western Digital down 7% apiece &mdash; while the broad tape keeps grinding back, with CNBC reading the S&amp;P 500 off about 0.1%, the Nasdaq Composite off about 0.4% and the Dow up 161 points, and Treasury Secretary Scott Bessent&rsquo;s Iran sanctions press conference confirmed for 1 p.m. ET.</p>',
 u'<p>Chip and memory weakness is still setting the tone &mdash; the group gapped down on weekend reports Washington may let Apple buy memory from China&rsquo;s CXMT and YMTC &mdash; leaving the S&amp;P 500 off about 0.2%, the Nasdaq Composite off about 0.4% and the Dow up about 0.2% in early-afternoon trade, while Treasury Secretary Scott Bessent&rsquo;s Iran sanctions press conference begins at 1 p.m. ET and the bond market keeps refusing to reward his $1 trillion cash pile.</p>',
 "ix-ws-p")

x = rep(x,
 u'<h2>Rodrigues survives Sacramento; the calendar fills to year-end</h2>',
 u'<h2>Rodrigues survives Sacramento; UFC 332 grows a title fight</h2>', "ix-mma-h2")
x = rep(x,
 u'<p>Gregory Rodrigues outlasted Anthony Hernandez over five rounds in Sacramento for his fourth straight win and called out No.&nbsp;2-ranked Dricus du Plessis; the promotion now turns to Shanghai on Saturday, with the numbered calendar filled through the year &mdash; UFC&nbsp;333 in Abu Dhabi in October, Madison Square Garden in November and Las Vegas in December.</p>',
 u'<p>Gregory Rodrigues outlasted Anthony Hernandez over five rounds in Sacramento for his fourth straight win and called out No.&nbsp;2-ranked Dricus du Plessis; the promotion turns to Shanghai on Saturday, and UFC&nbsp;332 in Salt Lake City has quietly grown a championship fight &mdash; Valentina Shevchenko is reported to defend the women&rsquo;s flyweight title against Natália Silva, who has won eight straight in the UFC and beaten three former champions in her last three fights.</p>',
 "ix-mma-p")
save("index.html", x)

print("\n".join(FAIL) if FAIL else "ALL EDITS OK")
