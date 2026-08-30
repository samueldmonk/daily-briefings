#!/usr/bin/env python3
# Append this run's real source URLs to each page footer; de-duplicate anchors.
import re, sys, io
REPO = sys.argv[1]
def rd(f): return io.open(REPO+'/'+f, encoding='utf-8').read()
def wr(f,s): io.open(REPO+'/'+f,'w',encoding='utf-8').write(s)

NEW = {
 'cyber-briefing.html': [
  ("https://cyberinsider.com/questel-confirms-microsoft-365-breach-after-shinyhunters-leaks-data/",
   "CyberInsider &mdash; Questel confirms Microsoft 365 breach after ShinyHunters leaks data"),
  ("https://breachnews.com/breaches/shinyhunters-lists-questel-alcon-and-lumenis-on-leak-site-with-new-extortion-claims/",
   "BreachNews &mdash; ShinyHunters lists Questel, Alcon and Lumenis (Aug 2 listing, Aug 4 deadline)"),
  ("https://sqmagazine.co.uk/questel-confirms-vishing-breach-shinyhunters-leak/",
   "SQ Magazine &mdash; Questel confirms vishing breach after ShinyHunters leak"),
  ("https://www.dexpose.io/shinyhunters-breach-alcon-inc/",
   "DeXpose &mdash; ShinyHunters breach claim against Alcon Inc. (25M+ Salesforce records)"),
  ("https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html",
   "The Hacker News &mdash; three CVSS 10.0 ServiceNow flaws (low attack complexity; four records)"),
  ("https://www.securityweek.com/august-2026-patch-tuesday-microsoft-fixes-421-cves-one-exploited-zero-day/",
   "SecurityWeek &mdash; August 2026 Patch Tuesday (CVE-2026-62893, CVE-2026-62818)"),
  ("https://www.cisa.gov/news-events/alerts/2026/08/18/cisa-adds-four-known-exploited-vulnerabilities-catalog",
   "CISA &mdash; four KEV additions, August 18 2026 (federal deadline August 21)"),
  ("https://www.cisa.gov/news-events/alerts/2026/08/20/cisa-adds-two-known-exploited-vulnerabilities-catalog",
   "CISA &mdash; two KEV additions, August 20 2026 (TrueConf Server)"),
  ("https://www.cisa.gov/known-exploited-vulnerabilities-catalog",
   "CISA &mdash; Known Exploited Vulnerabilities Catalog"),
 ],
 'wallstreet-briefing.html': [
  ("https://www.bloomberg.com/news/articles/2026-08-30/stock-market-today-dow-s-p-live-updates",
   "Bloomberg &mdash; Stock market today, Aug 30 2026 (Strait of Hormuz strike; crude +2% at the open; S&amp;P futures lower)"),
  ("https://finance.yahoo.com/markets/live/stock-market-today-friday-august-28-dow-sp-500-nasdaq-dip-fed-warsh-jackson-hole-speech-081514091.html",
   "Yahoo Finance &mdash; Friday August 28 closes and weekly changes (hike bets to 57%)"),
  ("https://www.stocktitan.net/news/AVGO/broadcom-inc-to-announce-third-quarter-fiscal-year-2026-financial-dkaqc3d1n73a.html",
   "StockTitan &mdash; Broadcom sets Q3 FY2026 earnings date, Sept 2 2026 (call 2:00 PM PT)"),
  ("https://www.bls.gov/schedule/2026/08_sched.htm",
   "BLS &mdash; release schedule (Employment Situation, Friday September 4, 8:30 AM ET)"),
  ("https://tradingeconomics.com/united-states/government-bond-yield",
   "Trading Economics &mdash; US Treasury yield curve snapshot (undated &ldquo;late August&rdquo;; recorded, not promoted)"),
  ("https://www.federalreserve.gov/releases/h15/",
   "Federal Reserve &mdash; H.15 Selected Interest Rates, August 28 2026"),
 ],
 'mma-briefing.html': [
  ("https://en.wikipedia.org/wiki/UFC_Fight_Night:_Hooker_vs._Parnasse",
   "UFC Fight Night: Hooker vs. Parnasse &mdash; event page (Sept 5, Accor Arena, UFC Fight Night 287)"),
  ("https://www.ufc.com/event/ufc-fight-night-september-05-2026",
   "UFC.com &mdash; UFC Fight Night: Hooker vs Parnasse, UFC Paris (official listing)"),
  ("https://sports.yahoo.com/articles/ufc-fight-night-287-dan-175030528.html",
   "Yahoo Sports &mdash; UFC Fight Night 287 odds (BetWay Parnasse &minus;400 / Hooker +300)"),
  ("https://www.mmamania.com/ufc-fight-cards/460921/ufc-paris-fight-card-start-time-date-and-location-hooker-vs-parnasse",
   "MMA Mania &mdash; UFC Paris card, start time, date and location"),
  ("https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions",
   "ESPN &mdash; Current and all-time UFC champions (thirteenth cross-check; two stale cells)"),
  ("https://sports.yahoo.com/articles/ufc-331-fight-card-start-140351479.html",
   "Yahoo Sports &mdash; UFC 331 card, Crypto.com Arena (&ldquo;current champion Joshua Van&rdquo;, &ldquo;former champion Alexandre Pantoja&rdquo;)"),
  ("https://www.aljazeera.com/sports/2026/8/6/ufc-331-van-pantoja-rematch-tsarukyan-returns-and-full-fight-card",
   "Al Jazeera &mdash; UFC 331: Van&ndash;Pantoja rematch, Tsarukyan returns, full card"),
  ("https://www.ufc.com/news/ufc-fight-night-shanghai-2026-bonus-coverage",
   "UFC.com &mdash; UFC Shanghai bonus coverage"),
  ("https://sports.yahoo.com/articles/ufc-shanghai-bonuses-yadong-song-150010453.html",
   "Yahoo Sports &mdash; UFC Shanghai bonuses ($100K x4 plus five stated $25K awards)"),
  ("https://bloodyelbow.com/2026/07/14/sean-omalley-sets-petr-yan-deadline-to-defend-ufc-title-before-hell-claim-to-be-champion-instead/",
   "Bloody Elbow &mdash; Petr Yan as reigning bantamweight champion (defence pressure)"),
 ],
}

for f, items in NEW.items():
    h = rd(f)
    m = re.search(r'<div class="srcs">', h)
    assert m, f
    add = ''.join('<a href="%s">%s</a><br>' % (u, t) for u, t in items)
    h = h[:m.end()] + add + h[m.end():]
    # de-duplicate anchors by href, keeping the first occurrence
    seen = set(); out = []; pos = 0
    for a in re.finditer(r'<a href="([^"]+)"[^>]*>.*?</a>', h, re.S):
        href = a.group(1)
        if href in seen:
            out.append(h[pos:a.start()]); pos = a.end()
        else:
            seen.add(href)
    out.append(h[pos:]); h2 = ''.join(out)
    dup = len(re.findall(r'<a href=', h)) - len(re.findall(r'<a href=', h2))
    hrefs = re.findall(r'<div class="srcs">(.*?)</div>', h2, re.S)
    n = len(re.findall(r'<a href="https://', hrefs[0])) if hrefs else 0
    assert n >= 6, (f, n)
    assert 'http://' not in h2.replace('https://', ''), f
    wr(f, h2)
    print(f, 'footer links:', n, '| dupes removed:', dup)
