#!/usr/bin/env python3
# Daily Briefings — 2026-08-27 ~9:06 AM ET, MORNING EDITION, third run of the day (PRE-OPEN).
# Targeted edits onto the 8:43 pages. Every replacement below traces to a source fetched this run.
import io, sys, re

D = "/sessions/hopeful-keen-bardeen/mnt/outputs/"
fails = []

def rw(path, pairs):
    p = D + path
    s = io.open(p, encoding="utf-8").read()
    for i, (old, new) in enumerate(pairs):
        if old not in s:
            fails.append("%s pair#%d NOT FOUND: %s" % (path, i, old[:90]))
            continue
        if s.count(old) != 1:
            fails.append("%s pair#%d NOT UNIQUE (%d): %s" % (path, i, s.count(old), old[:90]))
            continue
        s = s.replace(old, new)
    io.open(p, "w", encoding="utf-8").write(s)

# ───────────────────────── WALL STREET ─────────────────────────
ws = []

ws.append((
'<div class="tldr"><b>The Tape</b> <span>Nvidia is up roughly 7% before the bell on a $96.2 billion quarter and a $108 billion third-quarter guide, dragging the whole semiconductor complex higher and pushing all three US index futures into the green.</span></div>',
'<div class="tldr"><b>The Tape</b> <span>Nvidia, Salesforce and CrowdStrike are all sharply higher before the bell after their results, lifting Nasdaq futures roughly 0.9%, while the 8:30 jobless-claims print came in at 203,000 — a fresh sign of a steady labour market.</span></div>'))

ws.append((
'<span class="tag new">New · 8:40 AM ET</span><span class="tag acc">Pre-open</span>\n<h3>Nvidia\'s blowout quarter has all three index futures higher into the open</h3>',
'<span class="tag new">New · 9:05 AM ET</span><span class="tag acc">Pre-open</span>\n<h3>Three earnings beats and a 203,000 claims print carry the tape into the open</h3>'))

ws.append((
'<p style="margin:0 0 10px">As of roughly <b>8:40 AM ET</b>, ahead of Thursday\'s open, <b>all three major US index futures were higher</b>: <b>Dow futures +0.23%</b>, <b>S&amp;P 500 futures +0.38%</b> and <b>Nasdaq futures +0.53%</b>. That is a firmer picture than the earlier pre-market read, when Dow contracts were slipping while the tech complex rose. Bloomberg reported Nasdaq 100 contracts up about <b>1%</b> in early Thursday trade after CFO <b>Colette Kress</b> signalled strong sales growth into fiscal 2028.</p>',
'<p style="margin:0 0 10px">With about half an hour to the open, the tape is led by technology and the lead has narrowed rather than broadened. Yahoo Finance\'s Thursday-morning read has <b>Nasdaq 100 futures up 0.9%</b>, <b>S&amp;P 500 futures up 0.4%</b> and <b>Dow futures hovering near the flat line</b> — a step back from the <b>8:40 AM ET</b> read this page carried an hour ago, when all three were green and Dow contracts were up <b>0.23%</b>. Bloomberg separately reported S&amp;P 500 contracts up about <b>1%</b> in early Thursday trade after CFO <b>Colette Kress</b> signalled strong sales growth into fiscal 2028. The two headline ETF proxies tell the same story: <b>QQQ +1.04%</b> against <b>SPY +0.4%</b>.</p>\n<p style="margin:0 0 10px"><b>The 8:30 data is in, and it is good.</b> Initial jobless claims for the week ending <b>August 22</b> came in at <b>203,000</b>, down <b>4,000</b> from the prior week\'s upwardly revised <b>207,000</b> (first reported at 206,000). The four-week moving average rose <b>1,250</b> to <b>205,500</b>. Trading Economics notes the print extends a run of unusually low claims since a near-60-year low of <b>189,000</b> in mid-July. <span style="color:var(--mut)">This replaces the "no figure corroborated" line this page carried at 8:40 — and it is not the 232,000 number that circulated earlier, which traced to a 2022 report and was rejected.</span></p>'))

ws.append((
'<p style="margin:0 0 10px">The move is not confined to Nvidia. <b>Nvidia rose 7.4%</b> in pre-market trade, <b>Marvell Technology 5.8%</b> and <b>Micron 4.5%</b>, while the <b>VanEck Semiconductor ETF jumped 3.5%</b> and the <b>iShares Semiconductor ETF gained 3%</b>.</p>',
'<p style="margin:0 0 10px">The move is not confined to Nvidia, and it is not confined to semiconductors. <b>Nvidia rose 7.4%</b> in pre-market trade, <b>Marvell Technology 5.8%</b> and <b>Micron 4.5%</b>, while the <b>VanEck Semiconductor ETF jumped 3.5%</b> and the <b>iShares Semiconductor ETF gained 3%</b>. Software and security joined in: <b>Salesforce climbed nearly 12%</b> and <b>CrowdStrike about 8.9%</b> pre-open on their own results, with <b>Okta</b> also among the morning\'s risers.</p>'))

ws.append((
'<h3>CrowdStrike (CRWD) — sharply higher after hours</h3><p>CrowdStrike closed Wednesday at <b>$189.18, up 2.05%</b>, then rose <b>10.49% to $209.02</b> in after-hours trading following its results. HP (HPQ) is also on the earnings watchlist this morning.</p></div>',
'<h3>CrowdStrike (CRWD) — the quarter now has numbers</h3><p>Fiscal second-quarter 2027 revenue, for the quarter ended <b>July 31</b>, rose <b>26%</b> year over year to <b>$1.47 billion</b>, ahead of a <b>$1.44 billion</b> consensus, with adjusted EPS of <b>$0.31</b> against <b>$0.29</b> expected. The company <b>raised its full-year outlook</b>. Shares were up about <b>8.9%</b> pre-open, having closed Wednesday at <b>$189.18, up 2.05%</b>, and traded <b>10.49% higher at $209.02</b> in the after-hours session. HP (HPQ) is also on the earnings watchlist this morning.</p></div>\n\n<div class="card"><span class="tag new">New</span><span class="tag acc">Identity</span>\n<h3>Okta (OKTA) — joins the earnings risers</h3><p>Okta appears alongside Nvidia, Salesforce and CrowdStrike in Thursday\'s biggest-movers coverage, with Yahoo Finance\'s earnings live blog describing Salesforce, CrowdStrike and Okta shares as surging as the AI boom lifted second-quarter results. <b>No pre-market percentage for Okta was stated in the sources seen this run, so none is printed.</b></p></div>'))

ws.append((
'<h3>Salesforce (CRM) — double-digit after-hours pop</h3><p>Revenue of <b>$11.35 billion</b>',
'<h3>Salesforce (CRM) — up nearly 12% pre-open</h3><p>Shares jumped <b>nearly 12%</b> in pre-market trade on Thursday. Revenue of <b>$11.35 billion</b>'))

ws.append((
'The stock traded to <b>$231.70</b> after hours, <b>+$26.08 / +12.68%</b>; a separate tally put the move at <b>+11.8%</b>.</p></div>',
'The stock traded to <b>$231.70</b> after hours, <b>+$26.08 / +12.68%</b>; a separate tally put the move at <b>+11.8%</b>. <span style="color:var(--mut)">An "adjusted EPS of $5.90 versus $3.27 expected" line has now appeared in pre-market coverage two runs running. It is still not published here: a beat of that magnitude is far more likely a mismatched consensus figure than a real result, and no company filing confirming it has been fetched.</span></p></div>'))

ws.append((
'<tr><td>US 10-year Treasury yield</td><td class="mono">4.66%</td><td>Thursday pre-market read (Benzinga). It sat at 4.64–4.65% around Aug 25, after a 20-month high of 4.75% on Aug 21 (Trading Economics).</td></tr>',
'<tr><td>US 10-year Treasury yield</td><td class="mono">4.64–4.66%</td><td>Trading Economics has the yield holding around <b>4.64%</b> midweek — after a drop of nearly 10 basis points in the prior session as falling oil eased inflation concerns — and edging to <b>4.65%</b> on fresh data; a Thursday pre-market read put it at <b>4.66%</b> (Benzinga). A 20-month high of 4.75% was set on Aug 21.</td></tr>'))

ws.append((
'<tr><td>WTI crude</td><td class="mono">$81.36</td><td>Down 1.06% from the previous day on Aug 27 (Trading Economics). Investing.com showed a WTI futures range of $81.44–$82.15.</td></tr>',
'<tr><td>WTI crude</td><td class="mono">$81.36</td><td>Down 1.06% from the previous day on Aug 27 (Trading Economics), with prices falling for a third consecutive session. Investing.com showed a WTI futures range of $81.44–$82.15.</td></tr>'))

ws.append((
'<li><b>8:30 AM ET — second-quarter GDP (second estimate), weekly initial jobless claims and second-quarter corporate profits.</b> The release window has now passed, but <b>no figure from it was corroborated in sources fetched this run</b>, so none is printed. A widely-surfaced "232,000 initial claims for the week ending August 27" line traces to a <b>2022</b> report and is rejected — a Thursday claims report covers the week ending the previous Saturday, and cannot cover the day it is published.</li>',
'<li><b>8:30 AM ET — jobless claims, now reported: 203,000.</b> Initial claims for the week ending <b>August 22</b> fell <b>4,000</b> from a revised <b>207,000</b>; the four-week average rose to <b>205,500</b>. <b>The second estimate of second-quarter GDP and second-quarter corporate profits were released in the same window, but no figure from either was corroborated this run and none is printed</b> — a "1.5% second estimate released August 26" line contradicts itself on the release date and no BEA release was fetched. The "232,000 claims for the week ending August 27" figure that circulated earlier remains rejected: it traces to a 2022 report, and a Thursday claims report covers the week ending the previous Saturday.</li>'))

ws.append((
'<li><b>Fed policy.</b> Chair <b>Kevin Warsh</b>\'s address at the Jackson Hole symposium was not expected to give clear guidance on the September decision; the target range currently stands at 3.50%–3.75%.</li>',
'<li><b>Fed policy.</b> The federal funds target range stands at <b>3.50%–3.75%</b>, left unchanged at the July meeting (Trading Economics). <span style="color:var(--mut)">A "Jackson Hole address" framing carried on this page earlier has been removed: it could not be re-confirmed for August 2026 in sources fetched this run, and the same phrasing appears in coverage from a prior year.</span></li>'))

ws.append((
'<li><a href="https://www.federalreserve.gov/releases/h15/">Federal Reserve — H.15 Selected Interest Rates (Daily), August 26, 2026</a></li>',
'<li><a href="https://www.federalreserve.gov/releases/h15/">Federal Reserve — H.15 Selected Interest Rates (Daily), August 26, 2026</a></li><li><a href="https://finance.yahoo.com/markets/live/stock-market-today-thursday-august-27-dow-sp-500-nasdaq-082144520.html">Yahoo Finance — Stock market today: Dow, S&amp;P 500, Nasdaq futures rise as Nvidia, Salesforce earnings boost tech (Thu Aug 27)</a></li><li><a href="https://www.dol.gov/ui/data.pdf">US Department of Labor — Unemployment Insurance Weekly Claims (week ending Aug 22, 2026: 203,000)</a></li><li><a href="https://tradingeconomics.com/united-states/jobless-claims">Trading Economics — United States Initial Jobless Claims</a></li><li><a href="https://www.cnbc.com/2026/08/27/stocks-making-the-biggest-moves-premarket-nvda-hp-crm-dg-p.html">CNBC — Stocks making the biggest moves premarket: Nvidia, HP, Salesforce, Dollar General and more</a></li><li><a href="https://www.investing.com/news/stock-market-news/crowdstrike-shares-jump-on-earnings-beat-raised-outlook-4877850">Investing.com — CrowdStrike shares jump 8% premarket after earnings beat, raised outlook</a></li><li><a href="https://www.investing.com/news/stock-market-news/premarket-movers-nvidia-salesforce-and-crowdstrike-rally-on-earnings-4878910">Investing.com — Premarket movers: Nvidia, Salesforce and CrowdStrike rally on earnings</a></li><li><a href="https://finance.yahoo.com/markets/live/earnings-live-updates-q2-nvidia-115314802.html">Yahoo Finance — Earnings live: Salesforce, CrowdStrike, Okta stocks surge as AI boom lifts Q2 results</a></li><li><a href="https://stockmarketwatch.com/live/stock-market-today">StockMarketWatch — Tech and semis surge as Nvidia leads the premarket rally (QQQ +1.04%, SPY +0.4%)</a></li>'))

rw("wallstreet-briefing.html", ws)

# ───────────────────────── CYBER ─────────────────────────
cy = []

cy.append((
'<div class="stat"><div class="n">28</div><div class="l">Nutex Health facilities across 12 US states hit by the newly disclosed data exfiltration (BleepingComputer)</div></div>',
'<div class="stat"><div class="n">3.7M</div><div class="l">People affected by the CareCloud breach — now the fifth-largest health-data theft of 2026 (TechCrunch, SecurityWeek)</div></div>'))

cy.append((
'<h3>Nutex Health discloses data exfiltration in an 8-K</h3>',
'<h3>Nutex Health discloses data exfiltration in an 8-K</h3>'))

cy.append((
'<div class="card"><span class="tag warn">Phishing</span><span class="tag">Security vendor</span><span class="tag">Carried</span>\n<h3>ReliaQuest employee phished</h3>',
'''<div class="card" style="grid-column:1/-1"><span class="tag crit">Data theft</span><span class="tag">Healthcare</span><span class="tag new">New</span>
<h3>CareCloud breach confirmed at 3.7 million people — ten times the original estimate</h3><p>Digital health company <b>CareCloud</b> has confirmed that more than <b>3.7 million</b> people were affected by a breach it first believed had hit roughly <b>350,000</b>; the far larger figure appears on the HHS breach tracker. The company disclosed in early July that it had detected a network intrusion in <b>mid-March</b>, with the attackers inside one of its <b>AWS environments between March 10 and March 16</b>. Stolen data includes <b>names, addresses, Social Security numbers, driver's licence numbers, dates of birth, health-insurance information and medical records</b>, and for a very limited subset, <b>full payment-card information</b>. No cybercrime group has publicly claimed the hack and it is unclear whether a ransom was paid. It now ranks as the <b>fifth-largest theft of health data in 2026</b>. <span style="color:var(--mut)">(TechCrunch, SecurityWeek, HIPAA Journal, Malwarebytes)</span><br><br><span style="color:var(--mut);font-size:13.4px"><b>Note on an earlier omission:</b> this page previously saw a "3,750,000 affected individuals, filed with HHS" figure with no covered entity attached, and dropped it rather than publish an anonymous statistic. It belonged to CareCloud. It is published now that the entity is named.</span></p></div>

<div class="card"><span class="tag crit">Ransomware</span><span class="tag">Healthcare</span><span class="tag new">New</span>
<h3>Hospital for Sick Children hit, employee data stolen</h3><p>Canada's <b>Hospital for Sick Children</b> was attacked on <b>August 21, 2026</b>, with <b>employee data stolen</b>. <span style="color:var(--mut)">(Tech.co 2026 breach tracker)</span></p></div>

<div class="card"><span class="tag warn">Outage</span><span class="tag">Education</span><span class="tag new">New</span>
<h3>University of Texas at San Antonio takes systems offline</h3><p>The university was forced to take systems offline following a cyberattack on <b>August 18, 2026</b>. <span style="color:var(--mut)">(Tech.co 2026 breach tracker)</span></p></div>

<div class="card"><span class="tag crit">Critical infrastructure</span><span class="tag">FBI</span><span class="tag new">New</span>
<h3>Water utilities in at least seven states report incidents to the FBI</h3><p>Since <b>July 27, 2026</b>, Water and Wastewater Sector utilities in <b>at least seven US states</b> have reported incidents to the FBI, with <b>some of the activity degrading water operations</b>. <span style="color:var(--mut)">(FBI cyber alerts, 2026)</span></p></div>

<div class="card"><span class="tag warn">Phishing</span><span class="tag">Security vendor</span><span class="tag">Carried</span>
<h3>ReliaQuest employee phished</h3>'''))

cy.append((
'<li><b>Aug 11 batch</b> — three vulnerabilities added: <span class="mono">CVE-2026-20349</span> (Cisco Secure Firewall ASA / FTD), <span class="mono">CVE-2026-68820</span> (Microsoft Windows) and <span class="mono">CVE-2026-72898</span> (Metabase SQL injection).</li>',
'<li><b>Aug 11 batch</b> — three vulnerabilities added: <span class="mono">CVE-2026-20349</span> (Cisco Secure Firewall ASA / FTD), <span class="mono">CVE-2026-68820</span> (Microsoft Windows) and <span class="mono">CVE-2026-72898</span> (Metabase SQL injection).</li>\n<li><b>Aug 7</b> — <span class="mono">CVE-2026-8037</span>, a <b>Progress LoadMaster</b> command-injection flaw. No due date verified this run.</li>\n<li><b>On the directive itself:</b> a source seen this run reported that agencies had until <b>August 21</b> to remediate the August 18 batch. That is a three-day window, not the old three-week one, and it is consistent with <b>BOD 26-04, "Prioritizing Security Updates Based on Risk,"</b> which now sets FCEB remediation requirements per-CVE. Because the date came from a summary rather than the CISA alert page itself, <b>it is reported here rather than asserted as the deadline</b>, and no due date is inferred for the Aug 26, Aug 21, Aug 20, Aug 11 or Aug 7 additions.</li>'))

cy.append((
'<h3>Nimbus Manticore infrastructure surfaces</h3>',
'<h3>Nimbus Manticore infrastructure surfaces</h3>'))

cy.append((
'<h3>NVIDIA NemoClaw flaw can hijack an AI agent from a web page</h3><p>A critical vulnerability disclosed in <b>NVIDIA NemoClaw</b> could let an attacker hijack an AI agent after the victim simply visits a malicious website. <b>No CVE identifier or CVSS score was stated in the sources seen this run</b>, so none is printed. <span style="color:var(--mut)">(The Hacker News)</span></p></div>',
'<h3>NVIDIA NemoClaw flaw can hijack an AI agent from a web page</h3><p>A critical vulnerability disclosed in <b>NVIDIA NemoClaw</b> could let an attacker hijack an AI agent after the victim simply visits a malicious website. <b>No CVE identifier or CVSS score was stated in the sources seen this run</b>, so none is printed. <span style="color:var(--mut)">(The Hacker News)</span></p></div>\n\n<div class="card"><span class="tag crit">Ransomware-as-a-service</span><span class="tag">CISA advisory</span><span class="tag new">New</span>\n<h3>CISA and the FBI detail Gunra ransomware</h3><p>CISA released a <b>#StopRansomware</b> advisory (<span class="mono">AA26-222A</span>) on <b>August 10, 2026</b> covering <b>Gunra</b> ransomware, first observed by the FBI in <b>April 2025</b>. As of <b>January 2026</b> Gunra had launched a formal <b>ransomware-as-a-service affiliate programme</b> on dark-web forums, giving affiliates a management panel and a configurable ransomware builder. Ransom demands run through a customised <b>Tor-based negotiation portal</b>, with exfiltrated data published to a dedicated leak site if victims do not pay. <span style="color:var(--mut)">(CISA advisory AA26-222A)</span></p></div>'))

cy.append((
'<li><a href="https://cybersecuritynews.com/cyber-security-newsletter-bulletin-august/">Cybersecurity News — Weekly bulletin (ReliaQuest phishing, Entra ID CVE-2026-69836)</a></li>',
'<li><a href="https://cybersecuritynews.com/cyber-security-newsletter-bulletin-august/">Cybersecurity News — Weekly bulletin (ReliaQuest phishing, Entra ID CVE-2026-69836)</a></li><li><a href="https://techcrunch.com/2026/08/19/carecloud-confirms-3-7m-patients-had-their-medical-records-stolen-in-data-breach/">TechCrunch — CareCloud confirms 3.7M patients had their medical records stolen in data breach</a></li><li><a href="https://www.securityweek.com/carecloud-data-breach-impact-grows-to-3-7-million-individuals/">SecurityWeek — CareCloud Data Breach Impact Grows to 3.7 Million Individuals</a></li><li><a href="https://www.hipaajournal.com/carecloud-data-breach/">HIPAA Journal — CareCloud Data Breach</a></li><li><a href="https://www.malwarebytes.com/blog/news/2026/08/medical-records-ssns-and-bank-details-exposed-in-carecloud-data-breach">Malwarebytes — Medical records, SSNs and bank details exposed in CareCloud data breach</a></li><li><a href="https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a">CISA — #StopRansomware: Gunra Ransomware (AA26-222A)</a></li><li><a href="https://www.fbi.gov/investigate/cyber/alerts/2026">FBI — Cyber alerts, 2026 (Water and Wastewater Sector incidents)</a></li><li><a href="https://tech.co/news/data-breaches-updated-list">Tech.co — Data breaches that have happened this year (2026 update)</a></li><li><a href="https://www.cisa.gov/news-events/alerts/2026/08/07/cisa-adds-one-known-exploited-vulnerability-catalog">CISA — Adds One Known Exploited Vulnerability to Catalog (Aug 7, 2026 — Progress LoadMaster)</a></li>'))

rw("cyber-briefing.html", cy)

# ───────────────────────── MMA ─────────────────────────
mm = []

mm.append((
'<b>Song Yadong "The Kung Fu Kid" (23-9-1</b>, fighting out of Heilongjiang, China<b>)</b> makes his sixth main-event appearance following a submission win over former UFC flyweight champion <b>Deiveson Figueiredo</b> at UFC Fight Night Macau in May. The two came face to face on Wednesday at media day.</p>',
'<b>Song Yadong "The Kung Fu Kid" (23-9-1</b>, fighting out of Heilongjiang, China<b>)</b> makes his sixth main-event appearance following a submission win over former UFC flyweight champion <b>Deiveson Figueiredo</b> at UFC Fight Night Macau in May. The two have had their first fight-week faceoff.</p>\n<p style="margin:0 0 10px">The stakes are spelled out on both sides. Nurmagomedov is working his way back toward a title shot after <b>losing to Merab Dvalishvili at UFC 311</b>; Song is <b>China\'s highest-ranked male UFC contender</b>, and a win over Nurmagomedov would be the biggest of his career. A decisive result either way carries title-shot implications at 135 pounds.</p>'))

mm.append((
'<p>Flyweight title rematch between champion <b>Joshua Van</b> and former champion <b>Alexandre Pantoja</b>, whom Van beat by TKO 26 seconds into round one at UFC 323 after Pantoja suffered an arm injury. Co-main: <b>Arman Tsarukyan vs. Mauricio Ruffy</b> over five rounds. Also booked: <b>Marlon Vera vs. Charles Jourdain</b>. Thirteen fights; the UFC\'s first Los Angeles event since UFC 227 in August 2018.<br><span style="color:var(--mut)">No odds stated in sources seen this run.</span></p></div>',
'<p>Flyweight title rematch between champion <b>Joshua Van</b> and former champion <b>Alexandre Pantoja</b>, whom Van beat by TKO 26 seconds into round one at UFC 323 after Pantoja suffered an arm injury — a result that ended Pantoja\'s <b>four-defence reign</b>. Van carries a <b>seven-fight winning streak</b> into the rematch. The co-main, <b>Arman Tsarukyan vs. Mauricio Ruffy</b> over five rounds, is billed as a <b>lightweight title eliminator</b>, with the winner expected to challenge champion Justin Gaethje next. Also booked: <b>Marlon Vera vs. Charles Jourdain</b>. Thirteen fights; the UFC\'s first Los Angeles event since UFC 227 in August 2018. Main card <b>9 p.m. ET / 6 p.m. PT</b> on Paramount+.<br><span style="color:var(--mut)">No odds stated in sources seen this run.</span></p></div>'))

rw("mma-briefing.html", mm)

# ───────────────────────── INDEX ─────────────────────────
ix = []
ix.append((
'<h3>Nvidia\'s blowout quarter has all three index futures higher</h3>',
'<h3>Earnings beats and a 203,000 claims print lead the tape into the open</h3>'))
ix.append((
'Nvidia is up roughly 7% before the bell on a $96.2 billion quarter and a $108 billion third-quarter guide, dragging the whole semiconductor complex higher and pushing all three US index futures into the green.',
'Nvidia, Salesforce and CrowdStrike are all sharply higher before the bell after their results, lifting Nasdaq futures roughly 0.9%, while the 8:30 jobless-claims print came in at 203,000 — a fresh sign of a steady labour market.'))
rw("index.html", ix)

if fails:
    print("FAILURES:")
    for f in fails:
        print("  " + f)
    sys.exit(1)
print("All edits applied cleanly.")
