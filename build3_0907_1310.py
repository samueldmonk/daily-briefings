# -*- coding: utf-8 -*-
import re, os
R="/tmp/db_1788800764"; PAGES=["index","cyber-briefing","wallstreet-briefing","mma-briefing"]
S={p:open(os.path.join(R,p+".html"),encoding="utf-8").read() for p in PAGES}
log=[]
def sub1(page,old,new,why):
    n=S[page].count(old); assert n==1,"GOT %d :: %s :: %s"%(n,page,why)
    S[page]=S[page].replace(old,new); log.append("%-20s %s"%(page,why))

CY_SRC = ('<h2 class="sec">Sources</h2><div class="panel srcs">'
 '<b>Search return, 1:05 PM ET edition</b> &mdash; Nozomi Networks, <a href="https://www.nozominetworks.com/blog/tengu-a-modernized-mirai-that-doesnt-want-to-leave">Tengu: A Modernized Mirai That Doesn&rsquo;t Want to Leave</a> &mdash; the originating research. &nbsp;&middot;&nbsp; '
 '<b>Search return, 1:05 PM ET edition</b> &mdash; Help Net Security, <a href="https://www.helpnetsecurity.com/2026/07/29/tengu-mirai-iot-botnet-linux/">Tengu botnet reboots Linux devices to survive removal</a> (29 Jul 2026). &nbsp;&middot;&nbsp; '
 '<b>Search return, 1:05 PM ET edition</b> &mdash; The Hacker News, <a href="https://thehackernews.com/2026/07/tengu-botnet-reboots-compromised-linux.html">Tengu Botnet Reboots Compromised Linux Devices When Defenders Kill Its Process</a>. &nbsp;&middot;&nbsp; '
 '<b>Search return, 1:05 PM ET edition</b> &mdash; GBHackers, <a href="https://gbhackers.com/tengu-mirai-style-linux-bot/">Tengu Mirai-Style Linux Bot Hides as Kernel Worker to Launch DDoS and Proxy Attacks</a> &mdash; the 7 September static analysis (464 functions, <code>kworker/%d:%d</code> masquerade, 60-second guardian process). &nbsp;&middot;&nbsp; '
 '<b>Search return, 1:05 PM ET edition</b> &mdash; CISA, <a href="https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog">CISA Adds Seven Known Exploited Vulnerabilities to Catalog</a> (2 Sep 2026) and <a href="https://www.cisa.gov/news-events/alerts/2026/09/04/cisa-adds-one-known-exploited-vulnerability-catalog">CISA Adds One Known Exploited Vulnerability to Catalog</a> (4 Sep 2026) &mdash; the KEV set below re-confirmed by title this edition; neither alert page was fetched. &nbsp;&middot;&nbsp; ')
sub1("cyber-briefing", '<h2 class="sec">Sources</h2><div class="panel srcs">', CY_SRC, "appended Tengu + KEV sources to footer")

WS_SRC = ('<h2 class="sec">Sources</h2><div class="panel srcs">'
 '<b>Search return, 1:05 PM ET edition</b> &mdash; oil market coverage for 7 September &mdash; Brent ~$97.50 at ~2:34 a.m. ET, up ~1.7%, intraday high near $97.93; WTI above $92; last week Brent +7.6% and WTI ~+10%; tanker traffic through the Strait of Hormuz at its lowest since May. &nbsp;&middot;&nbsp; '
 '<b>Search return, 1:05 PM ET edition</b> &mdash; <a href="https://www.benzinga.com/markets/equities/26/09/61646501/is-stock-market-open-today-labor-day-2026-september-7">Is the stock market open today on Labor Day 2026?</a> &mdash; NYSE and Nasdaq closed all day 7 September; normal 9:30 AM&ndash;4:00 PM ET session resumes Tuesday 8 September. Re-confirmed this edition. &nbsp;&middot;&nbsp; '
 '<b>Search return, 1:05 PM ET edition</b> &mdash; <a href="https://www.washingtonpost.com/business/2026/09/04/stock-market-dow-nasdaq-jobs/b9e994e6-a89f-11f1-9e38-f705d048bd5a_story.html">How major US stock indexes fared Friday 9/4/2026</a> and <a href="https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-04-2026">TheStreet &mdash; Yields jump, stocks fall after jobs report surprises to upside</a> &mdash; Friday&rsquo;s closes and the 162,000 payroll print re-confirmed this edition. &nbsp;&middot;&nbsp; ')
sub1("wallstreet-briefing", '<h2 class="sec">Sources</h2><div class="panel srcs">', WS_SRC, "appended this-edition oil / Labor Day / Friday-close sources to footer")

MM_SRC = ('<h2 class="sec">Sources</h2><div class="panel srcs">'
 '<b>Search return, 1:05 PM ET edition</b> &mdash; <a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">ESPN &mdash; Current and all-time UFC champions</a> &mdash; champions board cross-checked again this edition: Aspinall (HW), Ulberg (LHW, 11 Apr 2026), Strickland (MW, 9 May 2026), Makhachev (WW, 15 Nov 2025), Gaethje (LW, 14 Jun 2026), Volkanovski (FW, 12 Apr 2025) &mdash; six of six match. &nbsp;&middot;&nbsp; '
 '<b>Search return, 1:05 PM ET edition</b> &mdash; <a href="https://www.ufc.com/event/ufc-332">UFC 332: Silva vs Wang</a> and <a href="https://www.ufc.com/event/ufc-fight-night-september-12-2026">Noche UFC: Silva vs Delgado</a> &mdash; both cards re-confirmed unchanged; Silva &minus;425 / Delgado +355 re-stated by a Yahoo Sports return. &nbsp;&middot;&nbsp; '
 '<b>Search return, 1:05 PM ET edition</b> &mdash; <a href="https://www.ufc.com/news/bonus-coverage-ufc-fight-night-paris-2026">UFC &mdash; Bonus Coverage, UFC Paris</a> &mdash; the four $100,000 and four $25,000 bonuses already on this page re-confirmed. &nbsp;&middot;&nbsp; ')
sub1("mma-briefing", '<h2 class="sec">Sources</h2><div class="panel srcs">', MM_SRC, "appended this-edition re-verification sources to footer")

for p in PAGES: open(os.path.join(R,p+".html"),"w",encoding="utf-8").write(S[p])
print("\n".join(log))
