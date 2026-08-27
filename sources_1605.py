import sys
def add(P,anchor,items):
    h=open(P).read()
    if anchor not in h: print("!! anchor missing in",P); sys.exit(1)
    h=h.replace(anchor,anchor+items,1)
    open(P,'w').write(h); print("sources added:",P)

add('wallstreet-briefing.html','<footer><b style="color:var(--ink)">Sources</b><ul class="bul">',
 '<li><b>Fetched 4:05 PM ET</b> — The Motley Fool, <a href="https://www.fool.com/investing/2026/08/27/nvidia-delivers-and-the-nasdaq-jumps-13/">Nvidia Delivers and the Nasdaq Jumps 1.3%</a> — Nasdaq Composite +1.31%, S&amp;P 500 +0.66%, Dow +0.33%; NVDA +8.4% and a $461bn market-value gain; CRM +19%, CRWD +9%; 156 of 503 S&amp;P stocks higher, 23 of 30 Dow components lower. Not treated here as an official close.</li>'
 '<li><b>Fetched 4:05 PM ET</b> — Trading Economics, <a href="https://tradingeconomics.com/united-states/stock-market">United States Stock Market Index</a> — S&amp;P 500 at 7,727, +0.67%; untimed, reconciles against Wednesday&rsquo;s 7,675.70 close.</li>'
 '<li><b>Fetched 4:05 PM ET</b> — Bloomberg, <a href="https://www.bloomberg.com/news/articles/2026-08-27/us-stock-futures-climb-as-nvidia-s-outlook-lifts-tech-sector">S&amp;P 500 Rises as Nvidia Spurs Tech Rally, All Other Sectors Down</a> — corroborates the one-sector shape of the session.</li>'
 '<li><b>Fetched 4:05 PM ET</b> — Yahoo Finance, <a href="https://finance.yahoo.com/markets/live/stock-market-today-thursday-august-27-dow-sp-500-nasdaq-082144520.html">Dow, S&amp;P 500, Nasdaq rally as Nvidia earnings revive AI optimism, software stocks roar back</a> — Nasdaq +1.5%, NVDA +8%, Jackson Hole still ahead.</li>'
 '<li><b>Fetched 4:05 PM ET, NOT PUBLISHED</b> — an aggregator page offering August 27 &ldquo;closes&rdquo; of 7,673.04 / 53,195.36 / 26,168.46 and, separately, S&amp;P +0.24% / Dow −0.19% / Nasdaq +0.83%. Rejected: internally inconsistent and below Wednesday&rsquo;s verified close while labelled a gain.</li>')
