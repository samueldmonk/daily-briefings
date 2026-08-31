#!/usr/bin/env python3
import os, re
D = os.path.dirname(os.path.abspath(__file__))
ADD = {
 'wallstreet-briefing.html': [
  ('https://finance.yahoo.com/markets/live/stock-market-today-monday-august-31-dow-sp-500-nasdaq-113851714.html','Yahoo Finance &mdash; Aug 31 close (S&amp;P 7,686.14 &minus;0.33%; Nasdaq 26,370.89 &minus;0.12%; Dow 53,185.90 &minus;374.09 &minus;0.70%; S&amp;P +2.5%/Nasdaq +3% for August)'),
  ('https://finance.yahoo.com/markets/stocks/articles/pg-e-sinks-18-edison-163921802.html','Yahoo Finance &mdash; Edison International &minus;23% to $54.22, largest one-day drop in 25+ years; Mizuho downgrade rationale'),
  ('https://finance.yahoo.com/markets/article/energy-stocks-lead-in-subdued-final-trading-day-of-august-utilities-under-pressure-alphacheck-142014111.html','Yahoo/AlphaCheck &mdash; sector split (Energy only positive sector ~+2% day, +6% month; Utilities &minus;1.6%; EIX largest one-day decline since 2001)'),
  ('https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield','Investing.com &mdash; US 10-year yield (previous close 4.722%, day range 4.697%&ndash;4.767%)'),
  ('https://stockanalysis.com/markets/afterhours/','StockAnalysis &mdash; after-hours movers screen (AEHL +84.75%, COOT +58.50%, YDDL +41.82%; ZTEK &minus;32.04%, JUNS &minus;26.79%, FNGR &minus;19.07%; WBUY +4.07% at $0.94)'),
  ('https://tradingeconomics.com/commodity/crude-oil','Trading Economics &mdash; WTI $85.54 (+2.57%) and Brent $90.23, Aug 31'),
 ],
 'cyber-briefing.html': [
  ('https://www.esentire.com/security-advisories/apercut-discloses-zero-day-vulnerabilities-cve-2026-82078-and-cve-2026-81578','eSentire &mdash; PaperCut zero-days disclosed Aug 27 2026: CVE-2026-82078 CVSS 9.4, CVE-2026-81578 CVSS 8.8; KEV addition Aug 31'),
  ('https://thecyberexpress.com/papercut-issues-second-emergency-patch/','The Cyber Express &mdash; PaperCut issues a second emergency patch after researchers broke the first fix'),
  ('https://cybernews.com/security/','Cybernews &mdash; McKesson/ShinyHunters $55,236,150 ransom demand, 284M records claimed; Neogen extortion threat; Air France/KLM third-party platform intrusion'),
  ('https://xage.com/blog/cyber-attack-news-risk-roundup-top-stories-for-august-2026/','Xage roundup &mdash; CISA on Medusa affiliates breaching 500+ critical-infrastructure organisations (publisher of &ldquo;Cursor&rdquo; refused)'),
  ('https://media.defense.gov/2026/Aug/18/2003983494/-1/-1/0/CSA_Active_Threat_to_Siemens_S7_Series_PLCs.PDF','NSA/CISA/FBI/DOE/EPA &mdash; joint advisory AA26-231A, active threat to Siemens S7 Series PLCs (snap7/python-snap7, S7comm, Censys/ZoomEye)'),
  ('https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog','CISA &mdash; three KEV additions Aug 27 (CVE-2023-49105 ownCloud due Aug 30; CVE-2026-53362 Linux kernel; CVE-2026-66384 JFrog Artifactory)'),
  ('https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog','CISA &mdash; six KEV additions Aug 26 (incl. CVE-2026-8452; due dates Aug 29 to Sept 9 &mdash; risk-based, per-CVE)'),
 ],
 'mma-briefing.html': [
  ('https://www.ufc.com/news/fight-by-fight-preview-ufc-paris-hooker-vs-parnasse','UFC.com &mdash; UFC Paris fight-by-fight preview: 14-fight card, Accor Arena Sept 5, fifth straight September in Paris; Parnasse via Contender Series; Sy vs Bukauskas'),
  ('https://en.wikipedia.org/wiki/UFC_Fight_Night:_Hooker_vs._Parnasse','UFC Fight Night: Hooker vs. Parnasse &mdash; card and broadcast (Paramount+, prelims 12 PM ET / main card 3 PM ET)'),
  ('https://bloodyelbow.com/2026/08/29/umar-nurmagomedov-vs-song-yadong-ufc-shanghai-result-khabibs-cousin-knocked-out-cold/','Bloody Elbow &mdash; Song Yadong KO2 (1:48) Umar Nurmagomedov; Song to 24-9-1, Nurmagomedov to 20-1; title-shot callout'),
  ('https://www.ufc.com/event/ufc-fight-night-september-12-2026','UFC.com &mdash; Noche UFC: Silva vs. Delgado, Sept 12, Desert Diamond Arena, Glendale AZ; main card 2 PM PT Paramount+'),
  ('https://www.espn.com/mma/ufc/story/_/id/48728368/strickland-stuns-chimaev-ufc-middleweight-title','ESPN &mdash; Strickland stuns Chimaev for the middleweight title, UFC 328, May 9 2026 (split decision 48&ndash;47 &times;2; 4-to-1 underdog)'),
  ('https://www.ufc.com/event/ufc-328','UFC.com &mdash; UFC 328: Chimaev vs Strickland, Prudential Center, Newark (official event page)'),
 ],
}
for p, links in ADD.items():
    fp = os.path.join(D,p); h = open(fp,encoding='utf-8').read()
    i = h.rfind('<div class="srcs">'); j = h.index('>', i)+1
    block = ''.join('<a href="%s">%s</a><br>' % (u,t) for u,t in links if u not in h)
    h = h[:j] + block + h[j:]
    open(fp,'w',encoding='utf-8').write(h)
    print('%-24s +%d source links' % (p, block.count('<a href')))
