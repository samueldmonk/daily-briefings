#!/usr/bin/env python3
"""Append THIS run's real source URLs to each page's footer, above the disclaimer."""
import sys, io, os
REPO = sys.argv[1]
rd = lambda f: io.open(os.path.join(REPO, f), encoding="utf-8").read()
wr = lambda f, s: io.open(os.path.join(REPO, f), "w", encoding="utf-8").write(s)

L = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a><br>' % (u, t)

SRC = {
 "wallstreet-briefing.html": (
   L("https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-31-2026",
     "TheStreet &mdash; Stock Market Today, Aug. 31, 2026 (Tesla +3.7% on Optimus production at Fremont; SAIC, GameStop)")
 + L("https://ca.finance.yahoo.com/news/energy-stocks-lead-in-subdued-final-trading-day-of-august-utilities-under-pressure-alphacheck-142014111.html",
     "Yahoo Finance / AlphaCheck &mdash; Energy leads final August session, utilities under pressure (EIX &minus;22.3%, PCG &minus;19.4%)")
 + L("https://www.tradingkey.com/news/market-movers/262142101-market-movers-pcg-20260831",
     "TradingKey &mdash; PG&amp;E (PCG) &minus;19.13% on Aug 31")
 + L("https://www.tradingkey.com/news/market-movers/262141945-market-movers-tsla-20260831",
     "TradingKey &mdash; Tesla (TSLA) +3.41% on Aug 31")
 + L("https://tradingeconomics.com/united-states/government-bond-yield",
     "TradingEconomics &mdash; US 10-Year Treasury yield 4.72% on Aug 31, 2026")
 + L("https://tradingeconomics.com/commodity/crude-oil",
     "TradingEconomics &mdash; WTI $85.54 (+2.57%) Aug 31; +6.48% over the month")
 + L("https://tradingeconomics.com/commodity/brent-crude-oil",
     "TradingEconomics &mdash; Brent $90.69 (+2.93%) Aug 31; +8.26% over the month")),
 "cyber-briefing.html": (
   L("https://www.helpnetsecurity.com/2026/08/31/papercut-attack-remote-access-tools/",
     "Help Net Security (Aug 31) &mdash; Attackers plant SimpleHelp and AnyDesk on compromised PaperCut servers")
 + L("https://www.bleepingcomputer.com/news/security/papercut-releases-second-emergency-patch-for-exploited-flaws/",
     "BleepingComputer &mdash; PaperCut releases a second emergency patch after fix bypasses")
 + L("https://securityaffairs.com/198107/uncategorized/hackers-are-probing-papercut-servers-and-47-still-have-no-patch.html",
     "Security Affairs &mdash; 47% of tracked PaperCut installations still unpatched")
 + L("https://cybersecuritynews.com/papercut-ng-mf-vulnerabilities-exploited/",
     "Cybersecurity News &mdash; CISA KEV additions CVE-2026-81578 / CVE-2026-82078, remediation due Sept 14, 2026")
 + L("https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/",
     "PaperCut &mdash; Urgent security bulletin, Aug 27, 2026 (restrict web access to trusted IPs)")
 + L("https://securityaffairs.com/198156/security/critical-givewp-flaw-lets-attackers-run-commands-on-wordpress-servers.html",
     "Security Affairs &mdash; GiveWP CVE-2026-82222 (CVSS 10.0), fixed in 4.16.7.2")
 + L("https://www.helpnetsecurity.com/2026/08/31/healthcare-company-mckesson-data-breach/",
     "Help Net Security (Aug 31) &mdash; McKesson / ShinyHunters: 284M records claimed, $55,236,150 demand, 72-hour window")),
 "mma-briefing.html": (
   L("https://www.ufcalendar.com/events/ufc-fight-night-2026-09-05",
     "UFCalendar &mdash; UFC Fight Night: Hooker vs Parnasse, Sep 5, 2026, Accor Arena (Parnasse &minus;600 / Hooker +430; 15 fights)")
 + L("https://sports.yahoo.com/articles/ufc-paris-watch-dan-hooker-125027816.html",
     "Yahoo Sports &mdash; UFC Paris viewing guide and lineup")
 + L("https://sports.yahoo.com/articles/sean-strickland-hints-next-opponent-031154872.html",
     "Yahoo Sports &mdash; Strickland &ldquo;once again the middleweight champion&rdquo;; first defense a rematch with Chimaev or Imavov")
 + L("https://bloodyelbow.com/2026/06/25/sean-strickland-reveals-date-for-first-title-defense-after-khamzat-chimaev-accused-him-of-running/",
     "Bloody Elbow &mdash; Strickland targets a December first title defense")
 + L("https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions",
     "ESPN &mdash; Current and all-time UFC champions")
 + L("https://www.ufc.com/news/ufc-fight-night-shanghai-2026-bonus-coverage",
     "UFC.com &mdash; UFC Shanghai bonus coverage (Aug 29, 2026)")
 + L("https://www.cbssports.com/ufc/news/2026-ufc-event-schedule-islam-makhachev-ian-machado-garry/",
     "CBS Sports &mdash; 2026 UFC event schedule")),
}

for f, extra in SRC.items():
    s = rd(f)
    i = s.rfind('<div class="disc">')
    assert i > 0, f
    s = s[:i] + extra + s[i:]
    wr(f, s)
print("sources_1705 applied")
