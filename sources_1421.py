# -*- coding: utf-8 -*-
D='/tmp/db_1787854887/'
def load(f): return open(D+f,encoding='utf-8').read()
def save(f,s): open(D+f,'w',encoding='utf-8').write(s)
def rep(s,old,new,n=1):
    c=s.count(old); assert c==n,"count %d want %d :: %s"%(c,n,old[:100]); return s.replace(old,new)

FOOT='<footer><b style="color:var(--ink)">Sources</b><ul class="bul">'

# ---------- MMA tldr + sources ----------
m=load('mma-briefing.html')
m=rep(m,"It is fight week in Shanghai: bantamweight contenders Umar Nurmagomedov and Song Yadong headline Saturday's card at the Oriental Sports Center, with Nurmagomedov a &minus;500 favourite on two of the three lines seen this run and &minus;470 on the third &mdash; and ESPN's champions page returned the correct board this time, after serving a stale one earlier today."
 if "&minus;500 favourite on two of the three lines seen this run" in m else
 "It is fight week in Shanghai: bantamweight contenders Umar Nurmagomedov and Song Yadong headline Saturday's card at the Oriental Sports Center, with Nurmagomedov a −500 favourite on two of the three lines seen this run and −470 on the third — and ESPN's champions page returned the correct board this time, after serving a stale one earlier today.",
 "It is fight week in Shanghai: bantamweight contenders Umar Nurmagomedov and Song Yadong headline Saturday's card at the Oriental Sports Center, with Nurmagomedov at −500 on two of the three lines seen today and −470 on the third — and September's reshuffled Noche UFC headliner now has a venue, Desert Diamond Arena in Glendale, Arizona, after Yair Rodríguez withdrew injured.")
m=rep(m,FOOT, FOOT+
 '<li><b>Fetched 2:21 PM ET</b> — Cageside Press, <a href="https://cagesidepress.com/2026/08/22/jean-silva-vs-jose-miguel-delgado-announced-as-new-noche-ufc-main-event/">Jean Silva vs. Jose Miguel Delgado Announced as New Noche UFC Main Event</a> — replacement headliner for Sept 12.</li>'
 '<li><b>Fetched 2:21 PM ET</b> — Wikipedia, <a href="https://en.wikipedia.org/wiki/UFC_Fight_Night:_Rodr%C3%ADguez_vs._Silva">UFC Fight Night: Rodríguez vs. Silva</a> — Noche UFC: Silva vs. Delgado, also UFC Fight Night 288 / Noche UFC 4, Sept 12 2026, Desert Diamond Arena, Glendale, Arizona; Rodríguez withdrew injured, replaced by Delgado.</li>'
 '<li><b>Fetched 2:21 PM ET</b> — UFC, <a href="https://www.ufc.com/event/ufc-fight-night-september-12-2026">Noche UFC: Silva vs Delgado</a> — official event page.</li>'
 '<li><b>Fetched 2:21 PM ET</b> — CBS Sports, <a href="https://www.cbssports.com/ufc/news/dana-whites-contender-series-2026-week-1-results-winners-contracts-anthony-wint-bilal-hasan/">DWCS 2026 Week 1 results: Anthony Wint, Bilal Hasan earn UFC contracts</a> — Hasan finished Mridul Saikia under a minute; Wint stopped Matt Adams in 34 seconds.</li>'
 '<li><b>Fetched 2:21 PM ET</b> — Bloody Elbow, <a href="https://bloodyelbow.com/2026/08/26/undefeated-dana-whites-contender-series-winner-sean-clancy-jr-tipped-to-become-ufc-champion/">Undefeated DWCS winner Sean Clancy Jr. tipped to become UFC champion</a> — second-round stoppage of Gary Balletto, Aug 25.</li>')
save('mma-briefing.html',m); print("mma ok")

# ---------- Cyber sources ----------
c=load('cyber-briefing.html')
c=rep(c,FOOT, FOOT+
 '<li><b>Fetched 2:21 PM ET</b> — The Hacker News, <a href="https://thehackernews.com/">front page, Aug 27 2026</a> — Amazon Kiro agentic IDE: data exfiltration via prompt injection and Kiro Powers; Kaltura CVE-2026-19912 / CVE-2026-19913 unpatched; CISA urging agencies to patch CVE-2026-8452.</li>'
 '<li><b>Fetched 2:21 PM ET</b> — Vici Tech Solutions, <a href="https://www.vicisecurity.com/blog/critical-flaws-exploited-within-days-august-2026-patch-window/">Critical Flaws Exploited Within Days: The August 2026 Patch Window</a> — CVE-2026-45659 SharePoint deserialization exploited by ransomware since early July; SAP Commerce Cloud CVE-2026-58231 exploited within 72 hours of disclosure.</li>'
 '<li><b>Fetched 2:21 PM ET</b> — SharkStriker, <a href="https://sharkstriker.com/blog/august-2026-data-breaches/">Top data breaches of August 2026</a> — Identity Theft Resource Center: 471.2M victim notices in H1 2026 against 297.5M for all of 2025, a 58% rise.</li>'
 '<li><b>Fetched 2:21 PM ET</b> — CISA, <a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">Known Exploited Vulnerabilities Catalog</a> — KEV additions re-checked this run.</li>')
save('cyber-briefing.html',c); print("cy ok")

# ---------- WS sources ----------
w=load('wallstreet-briefing.html')
w=rep(w,FOOT, FOOT+
 '<li><b>Fetched 2:21 PM ET</b> — TheStreet, <a href="https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-27-2026">Stock Market Today (Aug. 27, 2026): S&amp;P 500 climbs after Nvidia earnings beat</a> — Dow +0.4%, S&amp;P 500 +0.8%, Nasdaq Composite +1.5%; jobless claims 203,000.</li>'
 '<li><b>Fetched 2:21 PM ET</b> — Bloomberg, <a href="https://www.bloomberg.com/news/articles/2026-08-26/nasdaq-futures-rise-on-bullish-nvidia-sales-growth-markets-wrap">Stock Market Today: Dow, S&amp;P Live Updates for August 27</a> — technology the only advancing S&amp;P 500 sector, index +0.8% at 1:25 p.m. New York; Nvidia +7%; Micron, Marvell, Sandisk, Palo Alto and GE Vernova +6% to +3%.</li>'
 '<li><b>Fetched 2:21 PM ET</b> — Seeking Alpha / movers roundup, <a href="https://seekingalpha.com/news/4080339-biggest-stock-movers-today-goog-four-and-more">Biggest stock movers today</a> — Okta +17.4%, Salesforce +10.4%, Nvidia +9%, CrowdStrike +9%; software ETF +6.5%.</li>'
 '<li><b>Fetched 2:21 PM ET</b> — Trading Economics, <a href="https://tradingeconomics.com/united-states/government-bond-yield">US 10 Year Treasury Note Yield</a> — 10-year around 4.64–4.65%; July PCE +0.2% m/m against 0.1% expected, 3.7% y/y against 3.6% forecast.</li>'
 '<li><b>Fetched 2:21 PM ET</b> — ConvexTrade, <a href="https://convextrade.com/today/oil-price">WTI Crude Oil Price Today: $82.86 -0.08% (August 27, 2026)</a>.</li>'
 '<li><b>Fetched 2:21 PM ET</b> — Eastern Herald, <a href="https://easternherald.com/2026/08/27/crude-oil-price-today-august-27-2026/">Crude Oil Price Today, August 27, 2026: Brent at $87.65</a>.</li>')
save('wallstreet-briefing.html',w); print("ws ok")
