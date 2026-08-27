#!/usr/bin/env python3
"""Edits for the 2026-08-27 ~8:40am ET Morning Edition (second run of the day)."""
import sys, io, re

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

def load(n):
    return io.open(OUT + '/' + n, encoding='utf-8').read()

def save(n, s):
    io.open(OUT + '/' + n, 'w', encoding='utf-8').write(s)

def rep(s, old, new, label):
    if old not in s:
        raise SystemExit('MISS: ' + label)
    if s.count(old) != 1:
        raise SystemExit('AMBIGUOUS (%d): %s' % (s.count(old), label))
    return s.replace(old, new)

# ============================ WALL STREET ============================
w = load('wallstreet-briefing.html')

w = rep(w,
 "<div class=\"tldr\"><b>The Tape</b> <span>Nvidia's $96.2 billion quarter and a $108 billion third-quarter forecast sent the chipmaker up sharply in premarket trade and lifted S&P 500 and Nasdaq 100 futures, while Dow futures slipped.</span></div>",
 "<div class=\"tldr\"><b>The Tape</b> <span>Nvidia is up roughly 7% before the bell on a $96.2 billion quarter and a $108 billion third-quarter guide, dragging the whole semiconductor complex higher and pushing all three US index futures into the green.</span></div>",
 'ws tldr')

w = rep(w,
 "<span class=\"tag new\">New · 8:06 AM ET</span><span class=\"tag acc\">Pre-open</span>\n<h3>Nvidia's blowout quarter puts a bid under tech futures before the open</h3>\n<p style=\"margin:0 0 10px\">As of roughly <b>8:06 AM ET</b>, ahead of Thursday's open, <b>S&amp;P 500 and Nasdaq 100 futures were higher while Dow futures slipped</b> after Nvidia's second-quarter report landed Wednesday evening. Bloomberg reported Nasdaq 100 contracts up about <b>1%</b> in early Thursday trade after CFO <b>Colette Kress</b> signalled strong sales growth into fiscal 2028.</p>",
 "<span class=\"tag new\">New · 8:40 AM ET</span><span class=\"tag acc\">Pre-open</span>\n<h3>Nvidia's blowout quarter has all three index futures higher into the open</h3>\n<p style=\"margin:0 0 10px\">As of roughly <b>8:40 AM ET</b>, ahead of Thursday's open, <b>all three major US index futures were higher</b>: <b>Dow futures +0.23%</b>, <b>S&amp;P 500 futures +0.38%</b> and <b>Nasdaq futures +0.53%</b>. That is a firmer picture than the earlier pre-market read, when Dow contracts were slipping while the tech complex rose. Bloomberg reported Nasdaq 100 contracts up about <b>1%</b> in early Thursday trade after CFO <b>Colette Kress</b> signalled strong sales growth into fiscal 2028.</p>",
 'ws lead p1')

w = rep(w,
 "<p style=\"margin:0\">That follows a flat-to-lower Wednesday session: the <b>S&amp;P 500 closed at 7,675.70, down 0.02%</b>, with the <b>Dow off 0.08%</b> and the <b>Nasdaq Composite down 0.16%</b>.</p>",
 "<p style=\"margin:0 0 10px\">The move is not confined to Nvidia. <b>Nvidia rose 7.4%</b> in pre-market trade, <b>Marvell Technology 5.8%</b> and <b>Micron 4.5%</b>, while the <b>VanEck Semiconductor ETF jumped 3.5%</b> and the <b>iShares Semiconductor ETF gained 3%</b>.</p>\n<p style=\"margin:0\">That follows a flat-to-lower Wednesday session: the <b>S&amp;P 500 closed at 7,675.70, down 0.02%</b>, with the <b>Dow off 0.08%</b> and the <b>Nasdaq Composite down 0.16%</b>.</p>",
 'ws lead p3')

w = rep(w,
 "<h3>Nvidia (NVDA) — up sharply pre-market</h3><p>Two reads this morning, both printed and neither averaged: <b>CNBC has NVDA up 6%</b> in premarket trade, while <b>Benzinga has it up 7.32%</b>. Wednesday evening's first post-call read was \"more than 4%\" in extended trading. The driver is the $108 billion third-quarter guide and Huang's fiscal-2028 growth comment.</p></div>",
 "<h3>Nvidia (NVDA) — up sharply pre-market</h3><p>Three reads this morning, all printed and none averaged: <b>Reuters/AOL has NVDA up 7.4%</b>, <b>Benzinga has it up 7.32%</b> and <b>CNBC has it up 6%</b> in pre-market trade. Wednesday evening's first post-call read was \"more than 4%\" in extended trading. The driver is the $108 billion third-quarter guide and Huang's fiscal-2028 growth comment.</p></div>\n\n<div class=\"card\"><span class=\"tag new\">New</span><span class=\"tag acc\">Semis</span>\n<h3>The semiconductor complex follows Nvidia up</h3><p>The read-through hit the whole group before the bell: <b>Marvell Technology +5.8%</b> and <b>Micron +4.5%</b>, with the <b>VanEck Semiconductor ETF up 3.5%</b> and the <b>iShares Semiconductor ETF up 3%</b>. Reuters framed the reaction as evidence that \"the AI rally is far from over,\" with the companies at the centre of the AI build-out still posting strong growth as Big Tech ramps spending.</p></div>",
 'ws movers nvda + semis card')

w = rep(w,
 "<div class=\"note\">Pre-market activity leaned decisively toward technology and semiconductors on Thursday, on a resurgence in semiconductor demand. No numeric sector or breadth figure is asserted — none was stated in sources seen this run.</div>",
 "<div class=\"note\">Pre-market activity leaned decisively toward technology and semiconductors on Thursday. The two sector proxies that were quoted in sources this run — the VanEck Semiconductor ETF at <b>+3.5%</b> and the iShares Semiconductor ETF at <b>+3%</b> — are the only numeric sector reads printed here. No S&amp;P sector-level or breadth figure is asserted; none was stated in sources seen this run.</div>",
 'ws sector note')

w = rep(w,
 "<li><b>8:30 AM ET — second-quarter GDP (second estimate), weekly initial jobless claims and second-quarter corporate profits.</b> Consensus figures were not corroborated this run and are not printed.</li>",
 "<li><b>8:30 AM ET — second-quarter GDP (second estimate), weekly initial jobless claims and second-quarter corporate profits.</b> The release window has now passed, but <b>no figure from it was corroborated in sources fetched this run</b>, so none is printed. A widely-surfaced \"232,000 initial claims for the week ending August 27\" line traces to a <b>2022</b> report and is rejected — a Thursday claims report covers the week ending the previous Saturday, and cannot cover the day it is published.</li>",
 'ws radar 830')

w = rep(w,
 "<li><b>HP (HPQ)</b> joins Nvidia, Salesforce and CrowdStrike on this week's earnings watchlist.</li>",
 "<li><b>HP (HPQ)</b> joins Nvidia, Salesforce and CrowdStrike on this week's earnings watchlist.</li>\n<li><b>Vertiv Holdings (VRT)</b> was described in pre-market coverage as sharply higher after raising full-year 2026 revenue and adjusted-earnings guidance, with organic growth projected around <b>27%</b>. The figure comes from a pre-market movers feed rather than the company release, and is flagged as such.</li>",
 'ws radar vertiv')

# refresh the ticker tape to feature the day's movers, keeping the five mandatory symbols
w = rep(w,
 '{"proName":"NASDAQ:AMD","title":"AMD"}',
 '{"proName":"NASDAQ:MRVL","title":"Marvell"}',
 'ws tape amd->mrvl')

w = rep(w,
 "<li><a href=\"https://tradingeconomics.com/united-states/government-bond-yield\">Trading Economics — US 10 Year Treasury Note Yield</a></li>",
 "<li><a href=\"https://www.aol.com/articles/nasdaq-futures-lead-nvidia-forecast-095536000.html\">Reuters via AOL — Nasdaq futures take lead after Nvidia forecast refuels AI trade (NVDA +7.4%, MRVL +5.8%, MU +4.5%)</a></li><li><a href=\"https://www.cnbc.com/2026/08/27/nvidia-nvda-q2-earnings.html\">CNBC — Nvidia jumps 6% in premarket trading after blockbuster earnings boost AI confidence</a></li><li><a href=\"https://tradingeconomics.com/united-states/stock-market/news/508273\">Trading Economics — US Futures Rise as Nvidia Gains</a></li><li><a href=\"https://tradingeconomics.com/united-states/government-bond-yield\">Trading Economics — US 10 Year Treasury Note Yield</a></li>",
 'ws sources')

save('wallstreet-briefing.html', w)

# ============================ CYBER ============================
c = load('cyber-briefing.html')

c = rep(c,
 "<span class=\"tag new\">New · 8:06</span><span class=\"tag crit\">Deadline today</span><span class=\"tag acc\">KEV</span>",
 "<span class=\"tag new\">New · 8:40</span><span class=\"tag crit\">Deadline today</span><span class=\"tag acc\">KEV</span>",
 'cy topstory tag')

# new incident card: Nutex Health
c = rep(c,
 "<div class=\"card\"><span class=\"tag warn\">Phishing</span><span class=\"tag\">Security vendor</span><span class=\"tag\">Carried</span>\n<h3>ReliaQuest employee phished</h3>",
 "<div class=\"card\"><span class=\"tag crit\">Data theft</span><span class=\"tag\">Healthcare</span><span class=\"tag new\">New</span>\n<h3>Nutex Health discloses data exfiltration in an 8-K</h3><p>Hospital operator <b>Nutex Health</b> — which runs <b>28 facilities across 12 US states</b> — told the SEC in a <b>Form 8-K filed August 24</b> that an unauthorised third party accessed its servers and exfiltrated data that \"may be private or confidential.\" The company is still assessing whether patient, employee, credentialed-provider, business, financial or intellectual-property data was taken. It has engaged external incident-response and forensic specialists, contained the intrusion and notified law enforcement, and says the incident has had <b>no material impact</b> on operations or financial reporting to date. <b>No threat actor has claimed responsibility.</b> <span style=\"color:var(--mut)\">(BleepingComputer, SecurityWeek, SC Media)</span></p></div>\n\n<div class=\"card\"><span class=\"tag warn\">Phishing</span><span class=\"tag\">Security vendor</span><span class=\"tag\">Carried</span>\n<h3>ReliaQuest employee phished</h3>",
 'cy nutex card')

# Kaltura CVE ids now known
c = rep(c,
 "<h3>Kaltura video player flaws disclosed unpatched</h3><p>CERT/CC disclosed two unpatched vulnerabilities in Kaltura's HTML5 video player library that let a remote, unauthenticated attacker read arbitrary files from a server and execute code on it. <span style=\"color:var(--mut)\">(The Hacker News / CERT/CC)</span></p></div>",
 "<h3>Kaltura video player flaws disclosed unpatched</h3><p>CERT/CC disclosed two unpatched vulnerabilities in Kaltura's HTML5 video player library — now identified as <span class=\"mono\">CVE-2026-19913</span> and <span class=\"mono\">CVE-2026-19912</span> — that let a remote, unauthenticated attacker read arbitrary files from a server and execute code on it. <span style=\"color:var(--mut)\">(The Hacker News / CERT/CC)</span></p></div>\n\n<div class=\"card\"><span class=\"tag crit\">Account takeover</span><span class=\"tag\">Identity</span><span class=\"tag new\">New</span>\n<h3>Keycloak patched for a 9.1 account-takeover flaw</h3><p>Red Hat and the Keycloak project shipped fixes for <span class=\"mono\">CVE-2026-18963</span>, <b>CVSS 9.1</b>, in the open-source identity and access management server. An unauthenticated remote attacker could take over <i>any</i> user account by forcing a password reset. <span style=\"color:var(--mut)\">(The Hacker News)</span></p></div>\n\n<div class=\"card\"><span class=\"tag warn\">AI agents</span><span class=\"tag\">Agent hijack</span><span class=\"tag new\">New</span>\n<h3>NVIDIA NemoClaw flaw can hijack an AI agent from a web page</h3><p>A critical vulnerability disclosed in <b>NVIDIA NemoClaw</b> could let an attacker hijack an AI agent after the victim simply visits a malicious website. <b>No CVE identifier or CVSS score was stated in the sources seen this run</b>, so none is printed. <span style=\"color:var(--mut)\">(The Hacker News)</span></p></div>",
 'cy kaltura + keycloak + nemoclaw')

# CVSS updates verified this run
c = rep(c,
 "<tr><td class=\"mono\">CVE-2026-68820</td><td class=\"mono\">Not confirmed</td><td>Windows Ancillary Function Driver for WinSock (afd.sys)</td><td>Use-after-free elevation of privilege to SYSTEM; the exploited zero-day in August Patch Tuesday. KEV due date <b>Aug 25 — lapsed</b>.</td></tr>",
 "<tr><td class=\"mono\">CVE-2026-68820</td><td class=\"mono\">7.0</td><td>Windows Ancillary Function Driver for WinSock (afd.sys)</td><td>Use-after-free elevation of privilege; the only August Patch Tuesday bug confirmed exploited in the wild. Score per Tenable. KEV due date <b>Aug 25 — lapsed</b>.</td></tr>",
 'cy cvss 68820')

c = rep(c,
 "<tr><td class=\"mono\">CVE-2026-60004</td><td class=\"mono\">Not confirmed</td><td>Gitea (fixed in 1.27.1)</td><td>Remote code execution; on the KEV board with a federal due date of <b>Aug 28</b>.</td></tr>",
 "<tr><td class=\"mono\">CVE-2026-60004</td><td class=\"mono\">9.8</td><td>Gitea (fixed in 1.27.1)</td><td>Remote code execution — an attacker with ordinary <i>write</i> access to a repository can run arbitrary shell commands. CISA has warned of active exploitation. Federal due date <b>Aug 28</b>.</td></tr>\n<tr><td class=\"mono\">CVE-2026-18963</td><td class=\"mono\">9.1</td><td>Keycloak (Red Hat / upstream)</td><td>Unauthenticated account takeover via forced password reset. Patched.</td></tr>\n<tr><td class=\"mono\">CVE-2026-19913 / CVE-2026-19912</td><td class=\"mono\">Not confirmed</td><td>Kaltura HTML5 video player library</td><td>Arbitrary file read and remote code execution. <b>Unpatched</b> as disclosed by CERT/CC.</td></tr>",
 'cy cvss 60004 + new rows')

c = rep(c,
 "<td>Critical remote code execution, disclosed Aug 20, 2026. Numeric CVSS not confirmed this run.</td>",
 "<td>Critical remote code execution, disclosed Aug 20, 2026. Numeric CVSS not confirmed for this identifier. A Hacker News headline this run reports Microsoft patching an Entra ID RCE at <b>CVSS 10.0</b>, but the article snippet did not name the CVE, so the score is not attached here.</td>",
 'cy entra note')

# KEV board: new Aug 26 and Aug 20 batches
c = rep(c,
 "<li><b>Aug 11 batch</b> — three vulnerabilities added: <span class=\"mono\">CVE-2026-20349</span> (Cisco Secure Firewall ASA / FTD), <span class=\"mono\">CVE-2026-68820</span> (Microsoft Windows) and <span class=\"mono\">CVE-2026-72898</span> (Metabase SQL injection).</li>",
 "<li><b>Aug 26 batch — new this run</b> — <b>six</b> vulnerabilities added: <span class=\"mono\">CVE-2015-3246</span>, <span class=\"mono\">CVE-2015-5287</span>, <span class=\"mono\">CVE-2019-1068</span>, <span class=\"mono\">CVE-2021-23758</span>, <span class=\"mono\">CVE-2022-0995</span> and <span class=\"mono\">CVE-2026-8452</span>. Five of the six are legacy CVEs from 2015&ndash;2022, a reminder that KEV additions are driven by observed exploitation, not by disclosure date. No due dates verified this run.</li>\n<li><b>Aug 20 batch — new this run</b> — <b>two</b> vulnerabilities added, both in <b>TrueConf Server</b>: <span class=\"mono\">CVE-2026-72529</span> and <span class=\"mono\">CVE-2026-72530</span>. No due dates verified this run.</li>\n<li><b>Aug 18 batch, now itemised</b> — <span class=\"mono\">CVE-2026-33824</span> (Microsoft IKE Service), <span class=\"mono\">CVE-2026-55040</span> (Microsoft SharePoint), <span class=\"mono\">CVE-2026-59310</span> (VMware vCenter) and <span class=\"mono\">CVE-2026-65400</span> (Apple macOS).</li>\n<li><b>Aug 11 batch</b> — three vulnerabilities added: <span class=\"mono\">CVE-2026-20349</span> (Cisco Secure Firewall ASA / FTD), <span class=\"mono\">CVE-2026-68820</span> (Microsoft Windows) and <span class=\"mono\">CVE-2026-72898</span> (Metabase SQL injection).</li>",
 'cy kev batches')

c = rep(c,
 "<li><b>Aug 18 batch</b> — four vulnerabilities added spanning <b>Apple macOS, Microsoft SharePoint, VMware vCenter and Windows</b>. No due dates verified this run.</li>\n",
 "",
 'cy kev drop old aug18 line')

c = rep(c,
 "<div class=\"stat\"><div class=\"n\">7 mo</div><div class=\"l\">Between Oracle's January patch and CISA spotting exploitation (The Stack)</div></div>",
 "<div class=\"stat\"><div class=\"n\">7 mo</div><div class=\"l\">Between Oracle's January patch and CISA spotting exploitation (The Stack)</div></div>\n<div class=\"stat\"><div class=\"n\">28</div><div class=\"l\">Nutex Health facilities across 12 US states hit by the newly disclosed data exfiltration (BleepingComputer)</div></div>",
 'cy stat strip')

c = rep(c,
 "<li><a href=\"https://cybersecuritynews.com/cyber-security-newsletter-bulletin-august/\">Cybersecurity News — Weekly bulletin (ReliaQuest phishing, Entra ID CVE-2026-69836)</a></li>",
 "<li><a href=\"https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog\">CISA — Adds Six Known Exploited Vulnerabilities to Catalog (Aug 26, 2026)</a></li><li><a href=\"https://www.cisa.gov/news-events/alerts/2026/08/20/cisa-adds-two-known-exploited-vulnerabilities-catalog\">CISA — Adds Two Known Exploited Vulnerabilities to Catalog (Aug 20, 2026 — TrueConf Server)</a></li><li><a href=\"https://www.cisa.gov/news-events/alerts/2026/08/18/cisa-adds-four-known-exploited-vulnerabilities-catalog\">CISA — Adds Four Known Exploited Vulnerabilities to Catalog (Aug 18, 2026)</a></li><li><a href=\"https://www.bleepingcomputer.com/news/security/hospital-operator-nutex-health-says-data-stolen-in-cyberattack/\">BleepingComputer — Hospital operator Nutex Health says data stolen in cyberattack</a></li><li><a href=\"https://www.securityweek.com/sensitive-information-exposed-in-nutex-health-data-breach/\">SecurityWeek — Sensitive Information Exposed in Nutex Health Data Breach</a></li><li><a href=\"https://www.scworld.com/brief/nutex-investigating-data-breach-after-unauthorized-access-to-servers\">SC Media — Nutex investigating data breach after unauthorized access to servers</a></li><li><a href=\"https://www.tenable.com/blog/microsofts-august-2026-patch-tuesday-addresses-398-cves-cve-2026-68820\">Tenable — August 2026 Microsoft Patch Tuesday (CVE-2026-68820, CVSS 7.0)</a></li><li><a href=\"https://thehackernews.com/search/label/Vulnerability\">The Hacker News — Vulnerability feed (Gitea CVE-2026-60004, Keycloak CVE-2026-18963, Kaltura CVE-2026-19913/19912, NVIDIA NemoClaw)</a></li><li><a href=\"https://thehackernews.com/2026/08/microsoft-entra-id-flaw-cvss-100.html\">The Hacker News — Microsoft Patches Severe Entra ID Flaw (CVSS 10.0) Allowing Remote Code Execution</a></li><li><a href=\"https://cybersecuritynews.com/cyber-security-newsletter-bulletin-august/\">Cybersecurity News — Weekly bulletin (ReliaQuest phishing, Entra ID CVE-2026-69836)</a></li>",
 'cy sources')

save('cyber-briefing.html', c)

# ============================ MMA ============================
m = load('mma-briefing.html')

m = rep(m,
 "<span class=\"tag\">Carried</span><span class=\"tag acc\">Fight week</span><span class=\"tag\">Bantamweight</span>",
 "<span class=\"tag new\">Updated</span><span class=\"tag acc\">Fight week</span><span class=\"tag\">Bantamweight</span>",
 'mma topstory tag')

m = rep(m,
 "<b>Deiveson Figueiredo</b> at UFC Fight Night Macau in May. The two came face to face on Wednesday at media day.</p>",
 "<b>Deiveson Figueiredo</b> at UFC Fight Night Macau in May. The two came face to face on Wednesday at media day.</p>\n<p style=\"margin:0 0 10px\">The <b>co-main event</b> is a women's strawweight bout between <b>Yan Xiaonan</b>, China's first female UFC athlete and a former strawweight title challenger, ranked <b>No. 4</b>, and the surging <b>No. 13 Denise Gomes</b>. Because of the time difference, the card runs in the American morning: <b>prelims at 3 a.m. ET</b>, <b>main card at 6 a.m. ET</b>. Official weights were released for the Oriental Sports Center athletes on <b>August 28</b>.</p>",
 'mma comain')

m = rep(m,
 "<p>Bantamweight main event with title-eliminator stakes; Paramount+ exclusive in the US.<br><b>Odds:</b> Nurmagomedov −500 / Song +380 consensus (roughly 80% / 20% implied); DraftKings opened the fight at −470 / +360.</p></div>",
 "<p>Bantamweight main event with title-eliminator stakes; Paramount+ exclusive in the US. Co-main: <b>Yan Xiaonan vs. Denise Gomes</b> at women's strawweight. Prelims 3 a.m. ET, main card 6 a.m. ET.<br><b>Odds:</b> Nurmagomedov −500 / Song +380 consensus (roughly 80% / 20% implied); DraftKings opened the fight at −470 / +360.</p></div>",
 'mma card1')

m = rep(m,
 "<p>Ten weekly episodes running August through October 2026, airing Tuesday nights exclusively on Paramount+. Week 3's main event paired <b>Bella Mir</b> — daughter of former UFC heavyweight champion Frank Mir — with <b>Alex Apodaca</b> at women's bantamweight.</p></div>",
 "<p>Ten weekly episodes running August through October 2026, airing Tuesday nights exclusively on Paramount+. <b>Week 3 (Tuesday, August 25, Meta APEX)</b> handed out a contract to every one of its five winners — including the biggest upset in the show's history.</p></div>",
 'mma dwcs card')

m = rep(m,
 "<div class=\"card\"><span class=\"tag new\" style=\"color:var(--up);border-color:var(--up)\">prospect</span><span class=\"tag\">Carried</span>\n<h3>Bella Mir headlines week 3</h3><p>The daughter of former UFC heavyweight champion <b>Frank Mir</b> met <b>Alex Apodaca</b> in the women's bantamweight main event of the season's third episode. No result is asserted here — none was stated in sources seen this run.</p></div>",
 "<div class=\"card\"><span class=\"tag new\" style=\"color:var(--up);border-color:var(--up)\">prospect</span><span class=\"tag new\">New</span>\n<h3>Week 3 — five fights, five contracts, and a record upset</h3><p>All five winners on <b>August 25</b> left with UFC deals. In the featured bout, bantamweight <b>Alex Apodaca</b> beat <b>Bella Mir</b> — daughter of former UFC heavyweight champion Frank Mir — by unanimous decision, <b>29-28 on all three cards</b>. Mir had been a <b>−6000</b> favourite and Apodaca a <b>+1200</b> underdog, described as the <b>biggest upset in Contender Series history</b>. Joining her on the roster: <b>Ronald Humphrey</b> (first-round submission of Alexis Miranda), <b>Sean Clancy Jr.</b>, <b>Nick Galanti</b> and <b>Guilherme Uriel</b>, the quartet all winning by finish.</p></div>",
 'mma dwcs wk3 prospect card')

m = rep(m,
 "<li><b>Roster churn.</b> Bloody Elbow reported on August 21 that a former UFC title challenger has survived a run of surprise roster removals by signing a new <b>eight-fight deal</b>. No name is asserted here — none appeared in the source text seen this run.</li>",
 "<li><b>Roster churn — the eight-fight deal now has a name.</b> Bloody Elbow reported on August 21 that a former UFC title challenger had survived a run of surprise roster removals by signing a new <b>eight-fight deal</b>; coverage seen this run identifies him as UFC heavyweight <b>Curtis Blaydes</b>. The \"title challenger\" descriptor is Bloody Elbow's headline wording, reported as such.</li>",
 'mma blaydes')

m = rep(m,
 "<li><b>Broadcast.</b> Both UFC Shanghai and Contender Series season 10 stream exclusively on <b>Paramount+</b> in the United States.</li>",
 "<li><b>Broadcast.</b> Both UFC Shanghai and Contender Series season 10 stream exclusively on <b>Paramount+</b> in the United States. Shanghai's start times are set by the time difference: prelims <b>3 a.m. ET</b>, main card <b>6 a.m. ET</b>.</li>\n<li><b>Contender Series is converting at a high rate.</b> Across the three episodes verified so far, season 10 has produced <b>fifteen</b> UFC contracts — four in week 1, six in week 2 and five in week 3.</li>",
 'mma around')

m = rep(m,
 "<li><a href=\"https://en.wikipedia.org/wiki/Dana_White's_Contender_Series_season_10\">Wikipedia — Dana White's Contender Series season 10</a></li>",
 "<li><a href=\"https://www.ufc.com/news/dana-whites-contender-series-season-10-week-3-results\">UFC.com — Week 3 Results + Scorecards | Dana White's Contender Series Season 10</a></li><li><a href=\"https://cagesidepress.com/2026/08/25/dana-whites-contender-series-season-10-week-3-results/\">Cageside Press — Dana White's Contender Series Season 10, Week 3 Results</a></li><li><a href=\"https://dknetwork.draftkings.com/2026/08/25/dana-whites-contender-series-season-10-week-3-live-results-round-by-round-updates-highlights-and-winner-august-25-2026-2/\">DraftKings Network — DWCS Season 10, Week 3 live results (Apodaca +1200 over Mir −6000)</a></li><li><a href=\"https://athlonsports.com/mma/ufc-shanghai-umar-nurmagomedov-song-yadong-date-time-how-to-watch\">Athlon Sports — UFC Shanghai: date, time, how to watch (start times, co-main)</a></li><li><a href=\"https://www.si.com/fannation/mma/news/ufc-introduces-eight-fighters-removes-four\">Sports Illustrated / FanNation MMA — UFC roster moves (Curtis Blaydes eight-fight deal)</a></li><li><a href=\"https://en.wikipedia.org/wiki/Dana_White's_Contender_Series_season_10\">Wikipedia — Dana White's Contender Series season 10</a></li>",
 'mma sources')

save('mma-briefing.html', m)

# ============================ INDEX ============================
i = load('index.html')

i = rep(i,
 "<h3>Nvidia's $96.2bn quarter lifts tech futures before the open</h3>\n<p>Nvidia's $96.2 billion quarter and a $108 billion third-quarter forecast sent the chipmaker up sharply in premarket trade and lifted S&P 500 and Nasdaq 100 futures, while Dow futures slipped.</p>",
 "<h3>Nvidia's blowout quarter has all three index futures higher</h3>\n<p>Nvidia is up roughly 7% before the bell on a $96.2 billion quarter and a $108 billion third-quarter guide, dragging the whole semiconductor complex higher and pushing all three US index futures into the green.</p>",
 'idx ws card')

i = rep(i,
 "<h3>Shanghai fight week: Nurmagomedov vs. Song for the next title shot</h3>\n<p>It is fight week in Shanghai: bantamweight contenders Umar Nurmagomedov and Song Yadong headline Saturday's card at the Oriental Sports Center, with Nurmagomedov roughly a −500 favourite.</p>",
 "<h3>Shanghai fight week: Nurmagomedov vs. Song for the next title shot</h3>\n<p>It is fight week in Shanghai: bantamweight contenders Umar Nurmagomedov and Song Yadong headline Saturday's card at the Oriental Sports Center, with Nurmagomedov roughly a −500 favourite and Yan Xiaonan vs. Denise Gomes in the co-main.</p>",
 'idx mma card')

save('index.html', i)

print('ALL EDITS APPLIED OK')
