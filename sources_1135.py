import io
def R(P,old,new):
    s=io.open(P,encoding='utf-8').read()
    assert s.count(old)==1,('COUNT %d in %s'%(s.count(old),P))
    io.open(P,'w',encoding='utf-8').write(s.replace(old,new))

W='/sessions/optimistic-youthful-curie/mnt/outputs/wallstreet-briefing.html'
R(W,'<li><a href="https://stockmarketwatch.com/live/stock-market-today">StockMarketWatch — Tech and semis surge as Nvidia leads the premarket rally (QQQ +1.04%, SPY +0.4%)</a></li>',
  '<li><a href="https://stockmarketwatch.com/live/stock-market-today">StockMarketWatch — Tech and semis surge as Nvidia leads the premarket rally (QQQ +1.04%, SPY +0.4%)</a></li>'
  '<li><a href="https://finance.yahoo.com/markets/stocks/articles/stock-market-today-aug-27-144318504.html">Yahoo Finance — Stock Market Today (Aug. 27, 2026): S&amp;P 500 climbs after Nvidia earnings beat</a></li>'
  '<li><a href="https://www.cnbc.com/2026/08/18/treasury-yields-.html">CNBC — 30-year Treasury yield tops 5.33%, a new 19-year high, on inflation and spending concerns (Aug 18)</a></li>'
  '<li><a href="https://www.tipranks.com/news/the-fly/zscaler-price-target-raised-to-250-from-240-at-jpmorgan">TipRanks/The Fly — Zscaler price target raised at JPMorgan (one of three conflicting target reads; none published)</a></li>'
  '<li><a href="https://www.investing.com/news/analyst-ratings/jpmorgan-cuts-zscaler-stock-price-target-on-fy27-outlook-concerns-93CH-4712004">Investing.com — JPMorgan cuts Zscaler price target on FY27 outlook concerns (the conflicting third read)</a></li>'
  '<li><a href="https://www.marketbeat.com/stocks/NASDAQ/PLTR/forecast/">MarketBeat — Palantir Technologies (PLTR) forecast and price target</a></li>')

C='/sessions/optimistic-youthful-curie/mnt/outputs/cyber-briefing.html'
s=io.open(C,encoding='utf-8').read()
old='</ul>\n<div class="disc">'
assert s.count(old)==1, s.count(old)
add=('<li><a href="https://www.bleepingcomputer.com/news/security/cisa-hackers-now-exploiting-citrix-netscaler-rce-flaw-in-attacks/">BleepingComputer — CISA orders feds to patch Citrix NetScaler RCE flaw by Saturday (CVE-2026-8452, due Aug 29)</a></li>'
 '<li><a href="https://www.securityweek.com/recent-citrix-netscaler-vulnerability-exploited-in-the-wild/">SecurityWeek — Recent Citrix NetScaler vulnerability exploited in the wild (web shells, RCE as root per watchTowr)</a></li>'
 '<li><a href="https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog">CISA — Adds Six Known Exploited Vulnerabilities to Catalog (Aug 26)</a></li>'
 '<li><a href="https://www.cybersecuritydive.com/news/boston-scientific-cyberattack-disrupted-order-processing-shipping/828816/">Cybersecurity Dive — Boston Scientific says cyberattack disrupted order processing, shipping</a></li>'
 '<li><a href="https://www.medtechdive.com/news/boston-scientifics-ordering-shipping-disrupted-in-cyberattack/828814/">MedTech Dive — Boston Scientific’s ordering, shipping disrupted in cyberattack (Aug 25 intrusion, 8-K)</a></li>'
 '<li><a href="https://www.securityweek.com/adobe-and-nvidia-patch-dozens-of-vulnerabilities/">SecurityWeek — Adobe and Nvidia patch dozens of vulnerabilities (18 flaws in NemoClaw and OpenShell, two critical)</a></li>'
 '<li><a href="https://cybernews.com/news/boston-scientific-confirms-cyber-incident-knocked-systems-offline-disrupting-operations/">Cybernews — Boston Scientific confirms cyber incident knocked systems offline</a></li>')
io.open(C,'w',encoding='utf-8').write(s.replace(old,add+old))

M='/sessions/optimistic-youthful-curie/mnt/outputs/mma-briefing.html'
s=io.open(M,encoding='utf-8').read()
assert s.count(old)==1, s.count(old)
add=('<li><a href="https://www.ufc.com/news/ufc-returns-shanghai-pivotal-bantamweight-clash-between-3-umar-nurmagomedov-and-5-song-yadong">UFC.com — UFC returns to Shanghai: #3 Umar Nurmagomedov vs #5 Song Yadong (odds −500 / +380; records)</a></li>'
 '<li><a href="https://www.si.com/fannation/mma/news/dana-white-s-contender-series-2026-week-3-live-stream-results-highlights">Sports Illustrated — Dana White’s Contender Series 2026 Week 3 results (Aug 25, full card with methods)</a></li>'
 '<li><a href="https://www.ufc.com/news/ufc-and-meta-unveil-meta-ufc-rankings">UFC.com — UFC and Meta unveil Meta UFC Rankings (transition begun June 22, 2026)</a></li>'
 '<li><a href="https://bloodyelbow.com/2026/08/24/ufc-shanghai-preview-start-time-full-card-and-how-to-watch-umar-nurmagomedov-vs-song-yadong/">Bloody Elbow — UFC Shanghai preview: start time, full card, how to watch</a></li>'
 '<li><a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">ESPN — Current and all-time UFC champions (six belts re-verified this run)</a></li>')
io.open(M,'w',encoding='utf-8').write(s.replace(old,add+old))
print('sources added to all three')
