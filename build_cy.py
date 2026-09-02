# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp')
from css import BASE, STAMP, nav, meta
OUT="/sessions/amazing-determined-planck/mnt/outputs/"
ROOT=":root{--bg:#080d0c;--panel:#0f1716;--panel2:#14201e;--line:#1f2f2c;--fg:#e6f2ef;--muted:#6f8a85;--muted2:#a9c4be;--accent:#22d3a8;--accent2:#36c6ff;--up:#22d3a8;--crit:#ff5f6d;--warn:#f0b23c;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}\n"

h=[]
h.append('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Cyber Wire &mdash; Daily Security Briefing</title><style>'+ROOT+BASE+'</style></head><body><div class="wrap">')
h.append('<div class="masthead"><h1>The Cyber Wire</h1><p class="tag">Your daily security briefing &mdash; breaches, vulnerabilities &amp; federal deadlines</p>'+meta()+'</div>')
h.append('<div class="tldr"><b>The Wire</b> <span>SonicWall says <b>two SMA1000 zero-days it discovered internally</b> &mdash; one of them scored <b>CVSS 10</b> &mdash; are already being exploited and appear to have been chained for unauthenticated remote code execution, with hotfixes available, <b>no indicators of compromise published</b> and neither flaw yet in CISA&rsquo;s KEV catalog.</span></div>')
h.append('<div class="freshline" id="freshline">&nbsp;</div>')
h.append(nav("cyber-briefing.html"))

h.append('<div class="banner" style="border-color:var(--crit);background:rgba(255,95,109,.07)"><span class="lvl" style="color:var(--crit)">Threat Level: High</span><span class="why">A <b>CVSS 10</b> pre-authentication flaw in an internet-facing remote-access gateway is being exploited in the wild <i>today</i>, the vendor has published no IoCs, and the flaw is not yet KEV-listed &mdash; so there is no federal clock forcing the fix.</span></div>')

h.append('''<div class="stats">
<div class="stat"><div class="n">10.0</div><div class="l">CVSS &mdash; CVE-2026-83548 (SonicWall)</div></div>
<div class="stat"><div class="n">17</div><div class="l">SonicWall flaws already in CISA KEV</div></div>
<div class="stat"><div class="n">9.5M</div><div class="l">People impacted &mdash; Aesto Health</div></div>
<div class="stat"><div class="n">284M</div><div class="l">Records claimed &mdash; McKesson / ShinyHunters</div></div>
</div>''')

h.append('''<h2>Top Story</h2><div class="panel">
<h3 style="margin:0 0 9px;font-size:20px;line-height:1.3">SonicWall found two SMA1000 zero-days by looking at its own telemetry &mdash; and found them already being exploited</h3>
<p>SonicWall is urging customers of its <b>SMA1000 series</b> secure remote-access gateway and SSL-VPN appliance to patch <b>two zero-day vulnerabilities that have been exploited in the wild</b>. Per the advisory published Tuesday, <b>both the vulnerabilities and their exploitation were discovered internally</b> &mdash; the vendor found the attacks before anyone reported them.</p>
<p><b>CVE-2026-83548</b> carries a <b>CVSS score of 10</b> and is described as a <b>pre-authentication SSRF</b> issue in the <b>Appliance Work Place</b> interface. An attacker can exploit it remotely, without authentication, to reach sensitive functionality and conduct unauthorised operations. <b>CVE-2026-83549</b>, scored <b>7.8</b>, is an <b>OS command injection</b> issue in the <b>Appliance Management Console (AMC)</b> that an <i>authenticated</i> attacker can use to run arbitrary OS commands, potentially resulting in remote code execution.</p>
<p><b>SonicWall says it has observed exploitation of both, which SecurityWeek notes suggests they have been chained in attacks</b> &mdash; the pre-auth flaw supplying what the command-injection flaw needs. <b>That inference is the reporting&rsquo;s, and is printed as an inference rather than as a vendor statement.</b></p>
<p><b>Affected and not affected, precisely as the vendor scopes it:</b> SMA1000 models <b>6210, 7210 and 8200v</b> are affected. <b>SSL-VPN on SonicWall firewalls and the SMA100 series are not affected.</b> Hotfixes <b>12.4.3-03526</b> and <b>12.5.0-02952</b>, and higher versions, carry the patches.</p>
<p><b>What is missing is as operationally important as what is present.</b> No details appear to be available on the attacks, and <b>the public advisory does not include indicators of compromise</b> &mdash; defenders can patch but cannot easily hunt. CISA&rsquo;s KEV catalog currently includes <b>17 SonicWall product flaws</b>; <b>CVE-2026-83548 and CVE-2026-83549 have not yet been added</b>, so no federal remediation deadline attaches to either. SecurityWeek notes that SonicWall product vulnerabilities are regularly exploited in the wild, including in ransomware attacks, and that some have been exploited for weeks before a patch existed.</p>
</div>''')

h.append('''<div class="callout crit"><h3>Patch Priority &mdash; today</h3>
<p><b>SonicWall SMA1000 &mdash; CVE-2026-83548 (CVSS 10, pre-auth SSRF) and CVE-2026-83549 (CVSS 7.8, OS command injection).</b> Apply hotfix <b>12.4.3-03526</b> or <b>12.5.0-02952</b> or higher to models <b>6210, 7210, 8200v</b>. <b>This ranks first because it is the only item on this page that is simultaneously maximum-severity, internet-facing, pre-authentication and confirmed exploited by the vendor itself.</b> <b>It carries no CISA deadline &mdash; it is not KEV-listed &mdash; so the standing rule that an elapsed or imminent federal deadline outranks a live advisory does not reach it.</b> The nearest actual federal clocks are in the KEV section below. Firewall SSL-VPN and SMA100 customers are out of scope.</p></div>''')

h.append('''<h2>Threat Actor Spotlight</h2><div class="cards">
<div class="card"><div class="tags"><span class="tag t-c">Extortion</span><span class="tag t-a">Carried forward</span></div>
<h3>ShinyHunters</h3><p>The extortion group has claimed the theft of <b>284 million records</b> from McKesson&rsquo;s systems. <b>McKesson has confirmed a breach</b>, saying data was exfiltrated for <b>a subset of its Oncology &amp; Multispecialty and Medical-Surgical customers</b>. <b>The confirmed scope and the claimed scope are different quantities and this page does not reconcile them</b> &mdash; the 284 million figure is the attacker&rsquo;s, and is printed as the attacker&rsquo;s.</p></div>
</div>''')

h.append('''<h2>Breaches &amp; Incidents</h2><div class="note">&ldquo;New&rdquo; tags mark stories absent from the <b>9:53 AM</b> edition of this page.</div><div class="cards">
<div class="card"><div class="tags"><span class="tag t-new">New this run</span><span class="tag t-c">Healthcare</span><span class="tag t-a">Cloud</span></div>
<h3>Aesto Health &mdash; 9.5 million impacted</h3><p>Hackers stole <b>personal and health information</b> from the healthcare technology company&rsquo;s <b>AWS infrastructure</b>, with <b>9.5 million people</b> impacted. <b>That headcount and that infrastructure detail are the whole of what is sourced here</b>; no threat actor, intrusion date or ransom demand is published because none was fetched.</p></div>
<div class="card"><div class="tags"><span class="tag t-new">New this run</span><span class="tag t-c">Ransomware</span><span class="tag t-a">SEC filing</span></div>
<h3>Nutex Health &mdash; ransomware gang claims a breach</h3><p>A ransomware gang has claimed a breach at Nutex Health. <b>The company has notified the SEC</b> that hackers accessed <b>patient, employee, provider, business and financial information</b>. <b>No record count, gang name or demand is published here</b> &mdash; the claim and the SEC notification are what is sourced.</p></div>
<div class="card"><div class="tags"><span class="tag t-a">Carried forward</span><span class="tag t-c">Ransomware</span><span class="tag t-a">Government</span></div>
<h3>Berlin &mdash; Rhysida claims 5TB, city refuses to pay</h3><p>The <b>Rhysida</b> ransomware group has claimed the exfiltration of <b>over 5TB of data</b> from Berlin, including personal information and credentials. <b>Berlin will not pay the extortion demand.</b> <b>Every quantity in this item is the attacker&rsquo;s claim and is printed as one</b> &mdash; no independent corroboration of the volume has been fetched.</p></div>
<div class="card"><div class="tags"><span class="tag t-a">Carried forward</span><span class="tag t-c">Extortion</span><span class="tag t-a">Deadline</span></div>
<h3>McKesson &mdash; breach confirmed as an attacker deadline runs</h3><p>McKesson has <b>confirmed</b> a data breach while ShinyHunters&rsquo; extortion deadline looms. The company confirms exfiltration for <b>a subset of Oncology &amp; Multispecialty and Medical-Surgical customers</b>; the group claims <b>284 million records</b>. <b>An attacker&rsquo;s deadline is not a regulatory one and is not counted down on this page.</b></p></div>
<div class="card"><div class="tags"><span class="tag t-a">Law enforcement</span><span class="tag t-a">Aug 27</span></div>
<h3>Australia arrests two alleged TeamPCP hackers</h3><p>Australian and U.S. authorities collaborated to identify and charge the alleged cybercriminals, <b>who face many years in prison</b>. <b>Dated Aug 27 and labelled as such</b> &mdash; it is carried for context, not presented as breaking.</p></div>
<div class="card"><div class="tags"><span class="tag t-new">New this run</span><span class="tag t-a">Takedown</span></div>
<h3>A 23-year-old P2P botnet is disrupted</h3><p>The long-running <b>Sality</b> peer-to-peer botnet has been disrupted. The shutdown operation involved <b>peer-list manipulation</b> and a <b>takedown of Sality payload URLs</b>. <b>No attribution, victim count or law-enforcement agency is published</b> because none was fetched this run.</p></div>
</div>''')

h.append('''<h2>Vulnerability Watch</h2><table>
<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>
<tr><td>CVE-2026-83548</td><td><b class="down">10</b></td><td>SonicWall SMA1000 (6210, 7210, 8200v)</td><td>Pre-auth SSRF in Appliance Work Place. <b>Exploited in the wild</b>, discovered internally by the vendor. Fix: hotfix 12.4.3-03526 / 12.5.0-02952 or higher. <b>Not in KEV.</b></td></tr>
<tr><td>CVE-2026-83549</td><td>7.8</td><td>SonicWall SMA1000 Appliance Management Console</td><td>Authenticated OS command injection &rarr; possible RCE. <b>Exploited in the wild</b>; reportedly chained with 83548. <b>Not in KEV.</b></td></tr>
<tr><td>CVE-2026-82329</td><td class="flat">not sourced this run</td><td>JFrog Artifactory (self-hosted)</td><td>Critical <b>authentication bypass</b>; exploitation began <b>just days after public disclosure</b>. <b>Not the KEV item</b> &mdash; see the disambiguation note below.</td></tr>
<tr><td>CVE-2026-0768</td><td class="flat">not sourced this run</td><td>Langflow</td><td>Allows <b>unauthenticated attackers to execute arbitrary Python code remotely</b>. <b>Hackers have started exploiting it.</b></td></tr>
<tr><td>CVE-2026-82078</td><td class="flat">not sourced this run</td><td>PaperCut NG/MF</td><td>Unsafe reflection. <b>Added to CISA KEV</b>; exploitation escalated to active intrusions. Due date below.</td></tr>
<tr><td>CVE-2026-81578</td><td class="flat">not sourced this run</td><td>PaperCut NG/MF</td><td>Missing authentication for a critical function. <b>Added to CISA KEV</b> alongside 82078.</td></tr>
<tr><td>CVE-2026-66384</td><td class="flat">not sourced this run</td><td>JFrog Artifactory</td><td>Path traversal. <b>This</b> is the KEV-listed JFrog flaw. Due date below.</td></tr>
</table><div class="note"><b>CVSS scores appear only where a vendor or advisory this desk fetched states them.</b> The SonicWall pair is sourced to SonicWall&rsquo;s own advisory via SecurityWeek; for the rest, no authoritative score was fetched this run, so the column says so rather than borrowing a number from a blog. Also patched this week and not scored here: <b>Chrome and Firefox</b> shipped fixes for dozens of flaws including use-after-free, sandbox-escape and privilege-escalation bugs, and <b>WatchGuard</b> patched three critical issues in the Fireware OS <code>iked</code> process that could allow unauthenticated remote code execution.</div>''')

h.append('''<h2>CISA KEV &amp; Federal Deadlines</h2>
<div class="callout"><h3>Disambiguation: there are two JFrog Artifactory stories this week, and only one of them has a federal clock</h3>
<p><b>CVE-2026-82329</b> is the critical <b>authentication bypass</b>, reportedly exploited in the wild days after disclosure, self-hosted Artifactory only. <b>It is NOT in KEV and has no deadline.</b> <b>CVE-2026-66384</b> is the <b>path traversal</b>, and it <i>is</i> the KEV item, with the due date below. <b>Same vendor, same product, same week, opposite compliance status</b> &mdash; merged, they read as one escalation and the federal clock gets attached to the wrong flaw.</p></div>
<ul class="bul">
<li><b>CVE-2026-82078 &mdash; PaperCut NG/MF, unsafe reflection.</b> Federal remediation due <b>September 14, 2026</b> <span id="kev1" class="up"></span>. Added alongside CVE-2026-81578 on evidence of active exploitation; SecurityWeek reports PaperCut exploitation has <b>escalated to active intrusions</b>.</li>
<li><b>CVE-2026-81578 &mdash; PaperCut NG/MF, missing authentication for a critical function.</b> Added to KEV in the same action. <b>No due date for this CVE was fetched this run, so none is stated and no countdown is shown</b> &mdash; treat it as governed by the same action until CISA&rsquo;s own entry is read.</li>
<li><b>CVE-2026-66384 &mdash; JFrog Artifactory, path traversal.</b> Federal remediation due <b>September 10, 2026</b> <span id="kev2" class="up"></span>.</li>
<li><b>CVE-2026-83548 / CVE-2026-83549 &mdash; SonicWall SMA1000.</b> <b>Not in KEV as of the vendor advisory read this run, therefore no deadline.</b> Seventeen other SonicWall flaws already are. <b>The absence of a deadline is not an absence of urgency</b> &mdash; this is the page&rsquo;s Patch Priority precisely because the exploitation is confirmed and the clock is not.</li>
</ul>
<div class="note"><b>CISA KEV due dates are assigned per-CVE and are risk-based under BOD 26-04</b> &mdash; the old flat &ldquo;three weeks from the add date&rdquo; heuristic of BOD 22-01 is superseded and is not used to infer any deadline on this page. Every date above is a date a source states. <b>A mid-August KEV batch (CVE-2026-65400, CVE-2026-55040, CVE-2026-59310, CVE-2026-33824) that a search framed as an early-September addition was refused again this run: those were added Aug 18 with an Aug 21 deadline, and are not new.</b></div>''')

h.append('''<h2>Around the Industry</h2><ul class="bul">
<li><b>Palo Alto Networks has acquired AI agent platform Console</b>, announced alongside quarterly results showing a <b>34% increase in revenue</b> and strong growth in next-generation security ARR.</li>
<li><b>The U.S. Coast Guard has established an Office of Maritime Cybersecurity Policy</b>, which will serve as the central authority for cybersecurity policy covering U.S. ports, vessels and maritime facilities.</li>
<li><b>Forescout researchers ported a remote-code-execution exploit between WAGO PLC models using AI</b>, and report it took <b>hours and hundreds of dollars</b>. The relevance to defenders is the cost curve, not the specific PLC.</li>
<li><b>Five Venezuelans have pleaded guilty in U.S. court to ATM jackpotting.</b> The defendants <b>unsuccessfully</b> attempted to physically install malware on ATMs to force them to dispense cash.</li>
<li><b>OpenAI&rsquo;s Astra</b> has been designated as crossing a &ldquo;critical&rdquo; cybersecurity threshold &mdash; a tier that applies when a model can independently find and exploit zero-day vulnerabilities across many well-defended systems. <b>This is a vendor grading its own product against its own framework;</b> nothing here claims that no other organisation&rsquo;s model is comparable.</li>
</ul>''')

h.append('''<h2>Sources</h2><div class="panel srcs">
<a href="https://www.securityweek.com/sonicwall-warns-of-two-sma1000-zero-days-exploited-in-attacks/">SecurityWeek &mdash; SonicWall Warns of Two SMA1000 Zero-Days Exploited in Attacks (Sept 2, 2026, 1:04 AM ET)</a><br>
<a href="https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016">SonicWall PSIRT &mdash; advisory SNWLID-2026-0016</a><br>
<a href="https://www.securityweek.com/9-5-million-impacted-by-aesto-health-data-breach/">SecurityWeek &mdash; 9.5 Million Impacted by Aesto Health Data Breach</a><br>
<a href="https://www.securityweek.com/ransomware-gang-claims-nutex-health-data-breach/">SecurityWeek &mdash; Ransomware Gang Claims Nutex Health Data Breach</a><br>
<a href="https://www.securityweek.com/papercut-exploitation-escalates-to-active-intrusions/">SecurityWeek &mdash; PaperCut Exploitation Escalates to Active Intrusions</a><br>
<a href="https://www.securityweek.com/critical-jfrog-artifactory-vulnerability-reportedly-exploited-in-the-wild/">SecurityWeek &mdash; Critical JFrog Artifactory Vulnerability Reportedly Exploited in the Wild</a><br>
<a href="https://www.securityweek.com/hackers-start-exploiting-critical-langflow-vulnerability/">SecurityWeek &mdash; Hackers Start Exploiting Critical Langflow Vulnerability</a><br>
<a href="https://www.securityweek.com/mckesson-confirms-data-breach-as-attacker-deadline-looms/">SecurityWeek &mdash; McKesson Confirms Data Breach as Attacker Deadline Looms</a><br>
<a href="https://www.securityweek.com/berlin-wont-pay-extortion-group-claiming-data-theft/">SecurityWeek &mdash; Berlin Won&rsquo;t Pay Extortion Group Claiming Data Theft</a><br>
<a href="https://www.securityweek.com/23-year-old-sality-p2p-botnet-disrupted/">SecurityWeek &mdash; 23-Year-Old Sality P2P Botnet Disrupted</a><br>
<a href="https://www.securityweek.com/chrome-and-firefox-updates-patch-dozens-of-vulnerabilities/">SecurityWeek &mdash; Chrome and Firefox Updates Patch Dozens of Vulnerabilities</a><br>
<a href="https://www.securityweek.com/watchguard-patches-critical-vulnerabilities/">SecurityWeek &mdash; WatchGuard Patches Critical Vulnerabilities</a><br>
<a href="https://www.securityweek.com/openais-astra-becomes-first-model-to-cross-critical-cybersecurity-threshold/">SecurityWeek &mdash; OpenAI&rsquo;s Astra Becomes First Model to Cross Critical Cybersecurity Threshold</a><br>
<a href="https://www.cisa.gov/news-events/alerts/2026/08/31/cisa-adds-two-known-exploited-vulnerabilities-catalog">CISA &mdash; Adds Two Known Exploited Vulnerabilities to Catalog (Aug 31, 2026)</a><br>
<a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">CISA &mdash; Known Exploited Vulnerabilities Catalog</a>
</div>
<div class="disc"><b>Operational guidance is summarised, not substituted for the vendor advisory.</b> Patch only from the vendor bulletin linked above. CVSS scores, fixed versions and federal due dates on this page appear only where a source fetched this run states them; where a figure was not sourced, the page says so rather than estimating.</div>''')

CDN = """<script>(function(){function d(id,due){var el=document.getElementById(id);if(!el)return;var n=new Date();var t=new Date(due+'T23:59:59-04:00');var days=Math.ceil((t-n)/86400000);if(days>0){el.textContent='('+days+' day'+(days==1?'':'s')+' left)';}else{el.textContent=days===0?'(due today)':'(overdue by '+(-days)+' day'+(days==-1?'':'s')+')';el.className='down';}}d('kev1','2026-09-14');d('kev2','2026-09-10');})();</script>"""
h.append('</div>'+CDN+STAMP+'</body></html>')
open(OUT+"cyber-briefing.html","w").write("".join(h))
print("cy ok", sum(len(x) for x in h))
