# -*- coding: utf-8 -*-
import io
def add(f,items):
    s=io.open(f,encoding='utf-8').read()
    a=u'<footer><b style="color:var(--ink)">Sources</b><ul class="bul">'
    assert s.count(a)==1
    new=u''.join(u'<li><b>Fetched 12:38 PM ET</b> — %s, <a href="%s">%s</a> — %s</li>'%(pub,url,title,note) for pub,url,title,note in items)
    s=s.replace(a,a+new)
    io.open(f,'w',encoding='utf-8').write(s); print('sources added',f,len(items))

add('wallstreet-briefing.html',[
 (u'Yahoo Finance',u'https://finance.yahoo.com/markets/stocks/articles/stock-market-today-aug-27-144318504.html',
  u'Stock Market Today (Aug. 27, 2026): S&amp;P 500 climbs after Nvidia earnings beat',
  u'Nasdaq +400.29 (+1.53%), Dow +208.48 (+0.39%), S&amp;P 500 +0.4%; NVDA +9.48%, CRM +21.04%, CRWD +17.93%; jobless claims 203,000; bond yields stabilised.'),
 (u'Bloomberg',u'https://www.bloomberg.com/news/articles/2026-08-27/us-stock-futures-climb-as-nvidia-s-outlook-lifts-tech-sector',
  u'US Stock Futures Climb as Nvidia&rsquo;s Outlook Lifts Tech Sector',
  u'S&amp;P futures +0.4% at 8:15 a.m. NY, Nasdaq 100 futures +1%; Micron, Marvell, SanDisk, Palo Alto and GE Vernova adding between 6% and 3%; Salesforce among top performers on its revenue outlook and deepened Anthropic partnership.'),
 (u'Seeking Alpha',u'https://seekingalpha.com/news/4637151-salesforce-leaps-on-q2-financial-results-reveals-partnership-with-anthropic',
  u'Salesforce leaps on Q2 financial results; reveals partnership with Anthropic',
  u'Shares "surged more than 10%" after the fiscal Q2 2027 report released post-market Wednesday, Aug 26.'),
 (u'Trading Economics',u'https://tradingeconomics.com/united-states/government-bond-yield',
  u'US 10 Year Treasury Note Yield',
  u'10-year eased to 4.65% from the 20-month high of 4.75% set Aug 21; September rate-<i>rise</i> odds near 52%, down from 67% a week earlier.'),
])

add('cyber-briefing.html',[
 (u'The Hacker News',u'https://thehackernews.com/2026/08/cisa-adds-six-exploited-flaws-to-kev.html',
  u'CISA Adds Six Exploited Flaws to KEV, Including NetScaler, Linux, and SQL Server Bugs',
  u'Aug 26 batch: CVE-2019-1068 and CVE-2026-8452 due Aug 29; the remaining four due Sept 9, under BOD 26-04.'),
 (u'BleepingComputer',u'https://www.bleepingcomputer.com/news/security/atf-confirms-major-incident-after-recent-qilin-breach-claims/',
  u'ATF confirms &ldquo;major incident&rdquo; after recent Qilin breach claims',
  u'Standalone system breached; DOJ investigating; no indication the enterprise network or eForms was affected.'),
 (u'Cybernews',u'https://cybernews.com/news/qilin-ransomware-bureau-alcohol-tobacco-firearms-atf-cyberattack/',
  u'Qilin ransomware gang claims US firearms agency ATF, provides no details',
  u'Qilin claimed the attack Aug 26; group first detected 2022, roughly 1,900 victims over 18 months.'),
 (u'BleepingComputer',u'https://www.bleepingcomputer.com/news/security/hospital-operator-nutex-health-says-data-stolen-in-cyberattack/',
  u'Hospital operator Nutex Health says data stolen in cyberattack',
  u'28 facilities across 12 US states; 8-K filed Aug 24, 2026; data accessed and exfiltrated; no group has claimed it.'),
 (u'TechTimes',u'https://www.techtimes.com/articles/325583/20260826/oracle-proxy-flaw-cve-2026-21962-fueled-china-linked-attacks-100-governments.htm',
  u'Oracle Proxy Flaw CVE-2026-21962 Fueled China-Linked Attacks on 100+ Governments',
  u'SNOWLIGHT downloader across 100+ countries (SOCRadar, July); CloudSEK honeypots logged 140,000+ attempts from 21 countries over 12 days.'),
])

add('mma-briefing.html',[
 (u'Yahoo Sports',u'https://sports.yahoo.com/articles/ufc-sacramento-salaries-gregory-rodrigues-045215953.html',
  u'UFC Sacramento salaries: Gregory Rodrigues leads all fighters after main event win',
  u'$340,000 payday &mdash; $170,000 to show plus a $170,000 win bonus.'),
 (u'ESPN',u'https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions',
  u'Current and all-time UFC champions',
  u'Re-verified 12:38 &mdash; Aspinall, Ulberg, Strickland, Makhachev, Gaethje and Volkanovski returned with matching dates and methods.'),
 (u'Bloody Elbow',u'https://bloodyelbow.com/2026/08/21/ex-ufc-title-challenger-survives-trend-of-surprise-roster-removals-by-signing-new-8-fight-deal/',
  u'Ex-UFC title challenger survives trend of surprise roster removals by signing new 8-fight deal',
  u'Curtis Blaydes, No. 10 heavyweight and one-time interim heavyweight title challenger; revealed to James Lynch for Ozoon; last fight a loss to Josh Hokit at UFC 327.'),
 (u'Wikipedia',u'https://en.wikipedia.org/wiki/UFC_331',
  u'UFC 331',
  u'Sept 19, 2026, Crypto.com Arena, Los Angeles; Van vs. Pantoja 2; Tsarukyan (No. 2) vs. Ruffy (No. 10); Moicano vs. Ortega rematch; 13 fights.'),
])
