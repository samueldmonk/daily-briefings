# -*- coding: utf-8 -*-
import io
O="/sessions/tender-hopeful-newton/mnt/outputs/"
ADD={
"cyber-briefing.html":[
 ("https://www.bleepingcomputer.com/news/security/critical-avada-wordpress-theme-flaw-enables-zero-click-rce/","BleepingComputer &mdash; Critical Avada WordPress theme flaw enables zero-click RCE (Aug 26, 2026)"),
 ("https://www.wordfence.com/blog/2026/08/wordfence-argus-finds-complex-6-step-critical-rce-in-avada-theme-with-1-million-sales/","Wordfence &mdash; Argus finds complex 6-step critical RCE in Avada theme"),
 ("https://www.bleepingcomputer.com/news/security/atf-confirms-major-incident-after-recent-qilin-breach-claims/","BleepingComputer &mdash; ATF confirms &ldquo;major incident&rdquo; after Qilin breach claims"),
 ("https://www.securityweek.com/atf-confirms-cyber-incident-after-ransomware-group-claims-attack/","SecurityWeek &mdash; ATF confirms cyber incident after ransomware group claims attack"),
 ("https://cybernews.com/news/qilin-ransomware-bureau-alcohol-tobacco-firearms-atf-cyberattack/","Cybernews &mdash; ATF confirms cyberattack; Qilin claims it"),
 ("https://www.bleepingcomputer.com/news/security/mckesson-discloses-breach-after-shinyhunters-claims-patient-data-theft/","BleepingComputer &mdash; McKesson discloses breach after ShinyHunters claims patient data theft"),
 ("https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog","CISA &mdash; Adds Six Known Exploited Vulnerabilities to Catalog (Aug 26, 2026)"),
],
"wallstreet-briefing.html":[
 ("https://www.schaeffersresearch.com/content/news/2026/08/27/the-week-ahead-august-jobs-report-takes-center-stage","Schaeffer&rsquo;s &mdash; The Week Ahead: August jobs report takes center stage"),
 ("https://www.capitaleconomics.com/publication-group/us-employment-report-preview","Capital Economics &mdash; US Employment Report Preview (+90,000 August forecast)"),
 ("https://tradingeconomics.com/united-states/non-farm-payrolls","Trading Economics &mdash; US non-farm payrolls (July &minus;23K; June revised to +20K)"),
 ("https://finance.yahoo.com/markets/stocks/articles/jobs-report-broadcom-results-pose-100141778.html","Yahoo Finance &mdash; Jobs report, Broadcom results pose next hurdles"),
 ("https://www.cnbc.com/2026/08/27/stock-market-today-live-updates.html","CNBC &mdash; Stock market news for Aug. 28, 2026 (Friday closes)"),
],
"mma-briefing.html":[
 ("https://www.forbes.com/sites/brianmazique/2026/08/29/ufc-fight-night-shanghai-results-bonuses-and-highlights/","Forbes &mdash; UFC Shanghai results, bonuses and highlights ($400K in bonuses)"),
 ("https://www.sherdog.com/news/news/Yadong-Song-crushes-Umar-Nurmagomedov-in-big-upset-at-UFC-Shanghai-202570","Sherdog &mdash; Yadong Song crushes Umar Nurmagomedov in big upset"),
 ("https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions","ESPN &mdash; Current and all-time UFC champions (re-checked 11:05 AM)"),
],
}
for fn,items in ADD.items():
    s=io.open(O+fn,encoding='utf-8').read()
    added=0
    ins=[]
    for url,label in items:
        if url in s: continue
        ins.append('<a href="%s">%s</a>'%(url,label)); added+=1
    if ins:
        anchor='</div><div class="disc">'
        if anchor in s:
            s=s.replace(anchor,''.join(ins)+anchor,1)
        else:
            print("  !! no footer anchor in",fn); continue
    io.open(O+fn,'w',encoding='utf-8').write(s)
    print("%s: %d source links added"%(fn,added))
