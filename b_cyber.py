# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))
ACC, ACC2 = "#22d3a8", "#36c6ff"
CSS = css(ACC, ACC2, "#080d0c", "#0f1716", "#1d2c2a")

SRC = [
 ("Help Net Security - Hackers exploit RouterOS flaws to hijack MikroTik devices without authentication", "https://www.helpnetsecurity.com/2026/09/07/mikrotik-routeros-ssh-vulnerabilities-exploited/"),
 ("BleepingComputer - Hackers exploit new MikroTik RouterOS flaws to hijack routers", "https://www.bleepingcomputer.com/news/security/hackers-exploit-new-mikrotik-routeros-flaws-to-hijack-routers/"),
 ("SOC Prime - CVE-2026-67276: MikroTik RouterOS SSH Zero-Day", "https://socprime.com/blog/cve-2026-67276-mikrotik-routeros-ssh-zero-day/"),
 ("SecurityOnline - MikroTrick PoC: RouterOS Admin Rights Exploited In Wild", "https://securityonline.info/mikrotik-routeros-mikrotrick-cve-2026-67276/"),
 ("Help Net Security - Mathspace breach exposes data on over a million students and parents", "https://www.helpnetsecurity.com/2026/09/08/mathspace-data-breach-metabase-vulnerability/"),
 ("BleepingComputer - Mathspace discloses data breach affecting over 1 million people", "https://www.bleepingcomputer.com/news/security/mathspace-discloses-data-breach-affecting-over-1-million-people/"),
 ("The Hacker News - CISA Adds Seven Exploited Flaws as Attackers Deploy Reverse Shells and Crypto Miners", "https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html"),
 ("CISA - Adds Seven Known Exploited Vulnerabilities to Catalog (2 September 2026)", "https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog"),
 ("CISA - Adds One Known Exploited Vulnerability to Catalog (4 September 2026)", "https://www.cisa.gov/news-events/alerts/2026/09/04/cisa-adds-one-known-exploited-vulnerability-catalog"),
 ("CISA - Adds Two Known Exploited Vulnerabilities to Catalog (31 August 2026)", "https://www.cisa.gov/news-events/alerts/2026/08/31/cisa-adds-two-known-exploited-vulnerabilities-catalog"),
 ("CISA - Known Exploited Vulnerabilities Catalog", "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
 ("CVE Brief - September 8, 2026", "https://cvebrief.com/archive/2026/09/08/"),
 ("SecurityWeek - August 2026 Patch Tuesday: Microsoft Fixes 421 CVEs, One Exploited Zero-Day", "https://www.securityweek.com/august-2026-patch-tuesday-microsoft-fixes-421-cves-one-exploited-zero-day/"),
 ("BleepingComputer - Microsoft August 2026 Patch Tuesday fixes 400 flaws, 3 zero-days", "https://www.bleepingcomputer.com/news/microsoft/microsoft-august-2026-patch-tuesday-fixes-400-flaws-3-zero-days/"),
 ("The Hacker News - Microsoft Patches 398 Flaws Including a Windows Driver Zero-Day Under Active Attack", "https://thehackernews.com/2026/08/microsoft-patches-398-flaws-including.html"),
 ("Unit 42 (Palo Alto Networks) - No Manners Here: The Ruthless Rise of The Gentlemen Ransomware", "https://unit42.paloaltonetworks.com/the-gentlemen-ransomware/"),
 ("Silent Push - Following a Serial Ransomware Affiliate from LockBit, Black Basta, and Qilin to The Gentlemen", "https://www.silentpush.com/blog/gentlemen-ransomware/"),
 ("Halcyon - Threat Assessment: The Gentlemen Ransomware Group Is Scaling Faster Than Any Other Group on Record", "https://www.halcyon.ai/ransomware-research-reports/threat-assessment-the-gentlemen-ransomware-group"),
 ("Becker's Hospital Review - Healthcare ransomware attacks up 14%: 5 things to know", "https://www.beckershospitalreview.com/healthcare-information-technology/cybersecurity/healthcare-ransomware-attacks-up-14-5-things-to-know/"),
 ("Help Net Security - Cybersecurity News and Expert Analysis", "https://www.helpnetsecurity.com/"),
]

def srcblock():
    return "".join('<div style="margin-bottom:7px">%s &mdash; <a href="%s">%s</a></div>' % (t, u, u) for t, u in SRC)

BODY = """@@MAST@@
<div class="tldr"><b>The Wire</b> <span>An SSH authentication bypass in MikroTik RouterOS, chained for full administrative takeover and exploited in the wild since 2 September, is now the most urgent unpatched exposure on the internet-facing edge, with more than 122,000 devices showing exposed SSH interfaces.</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
@@NAV@@

<div class="banner">
<span class="lvl">Threat Level: High</span>
<span>Eight CVEs are under confirmed active exploitation as of today, an actively exploited router auth-bypass chain has more than 122,000 candidate targets, and three federal remediation deadlines fall inside the next ten days.</span>
</div>

<div class="stats">
<div class="stat"><div class="n">122,000+</div><div class="l">MikroTik devices with exposed SSH interfaces, the candidate target set for the MikroTrick chain</div></div>
<div class="stat"><div class="n">8</div><div class="l">CVEs showing confirmed active exploitation as of 8 September, including Kestra, Sangoma Switchvox, LiteLLM and Starlette</div></div>
<div class="stat"><div class="n">1,079,819</div><div class="l">People exposed in the Mathspace breach, all in Australia and New Zealand</div></div>
<div class="stat"><div class="n">410</div><div class="l">Ransomware incidents against U.S. healthcare organisations in H1 2026, up 14%</div></div>
</div>

<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 8px;font-size:20px">&ldquo;MikroTrick&rdquo;: attackers are taking full administrative control of MikroTik routers over SSH, and they started before the patch shipped</h3>
<p style="margin:0 0 10px"><b>CVE-2026-67276</b> is an SSH authentication bypass in MikroTik RouterOS caused by <b>incomplete validation of RSA public keys</b>. An attacker who knows a username and the public modulus of that user&#39;s key can craft a different key and log in <b>without the legitimate private key</b>. On its own that is an unauthenticated foothold; chained with <b>CVE-2026-86060</b>, an SSH privilege-escalation flaw triggered by a specially crafted username, it yields <b>full administrative privileges</b> on the device.</p>
<p style="margin:0 0 10px">Poland&#39;s CERT Polska named the chain <b>MikroTrick</b> and warned it is being actively exploited. The timeline is the uncomfortable part: <b>exploitation began as early as 2 September</b>, one day <i>before</i> MikroTik released patched builds on <b>3 September</b>. Observed attacks created an <b>&ldquo;ops&rdquo; account</b> from <b>82.192.72.4</b>, with the SSH username <b>&ldquo;-2&rdquo;</b> as an indicator of compromise. <span class="mut">Those three indicators are carried from this briefing&#39;s standing sourced record of the CERT Polska advisory; the sources read this run describe the chain and its exploitation but do not restate the IOCs.</span></p>
<p style="margin:0"><b>Fixed builds:</b> RouterOS <b>7.25beta3, 7.24.2, 7.23.4 and 6.49.21</b>, all released 3 September. The updates add a compromise-detection mechanism that checks at startup for known signs of unauthorised configuration change, disables malicious entries and logs a critical warning &mdash; which means patching also gives you a detection you did not previously have. <b>Over 122,000 devices have exposed SSH interfaces.</b> <span class="mut">No CVSS was stated for CVE-2026-86060 in anything read this run, so none is printed. Neither CVE is in the CISA KEV catalog.</span></p>
</div>

<h2 class="sec">Patch Priority</h2>
<div class="callout crit">
<h3>Do this first</h3>
<p style="margin:0 0 9px"><b>The nearest federal deadline: PaperCut.</b> <b>CVE-2026-81578</b> and <b>CVE-2026-82078</b> entered the CISA KEV catalog on <b>31 August</b> and carry a remediation due date of <b>14 September &mdash; six days from today</b>. That is the tightest verified clock on this page and it matches the KEV section below exactly.</p>
<p style="margin:0 0 9px"><b>The most urgent item without a deadline: MikroTik RouterOS.</b> The MikroTrick chain above is confirmed exploited in the wild against internet-exposed routers, the patches have been available since 3 September, and the exposed population is over 122,000. It is not in KEV, so no federal clock applies &mdash; which makes it easier to defer and no less dangerous. Upgrade to 7.25beta3 / 7.24.2 / 7.23.4 / 6.49.21 and hunt for an <b>&ldquo;ops&rdquo;</b> account and the SSH username <b>&ldquo;-2&rdquo;</b>.</p>
<p style="margin:0"><b>The highest severity currently exploited: SonicWall SMA1000.</b> <b>CVE-2026-83548</b>, a pre-authentication server-side request forgery at <b>CVSS 10.0</b>, chains to <b>CVE-2026-83549</b> for unauthenticated remote code execution. SonicWall has said it investigated a case indicating active exploitation of both. KEV due <b>16 September &mdash; eight days from today</b>.</p>
</div>

<h2 class="sec">Threat Actor Spotlight</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t">Expanded</span><span class="t hot">Ransomware</span></div>
<h3>The Gentlemen &mdash; and the Qilin affiliate it broke away from</h3>
<p><b>The Gentlemen</b> (also tracked as <i>hastalamuerte</i>) is a double-extortion operation <b>first observed in July 2025</b>, assessed as a mature RaaS platform or a rebranded actor with ties to the DevMan and Qilin ecosystems. Its operators were likely active earlier as a Qilin RaaS affiliate known as <b>ArmCorp</b>, and the group appears to have <b>formed following a payment dispute with Qilin</b>. Since mid-2025 it has claimed <b>nearly 300 organisations across more than 66 countries and 20 industry verticals</b>, making it one of the fastest-scaling ransomware threats on record; it <b>surged to 269 victims and overtook Qilin during June 2026</b>. By July, <b>Qilin and The Gentlemen each accounted for roughly 14%</b> of publicly reported ransomware victim postings tracked by Check Point &mdash; and Qilin itself had published <b>more than 2,000 victim listings</b> on its leak site as of July 2026. <span class="mut">An earlier edition of this briefing dated The Gentlemen&#39;s appearance to August 2025; this run&#39;s reads give July 2025, and the conflict is stated rather than resolved.</span></p>
</div>
</div>

<h2 class="sec">Breaches &amp; Incidents</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t">Expanded</span><span class="t hot">Education</span></div>
<h3>Mathspace: 1,079,819 students, parents and staff</h3>
<p>The maths-learning platform confirmed on <b>3 September</b> that unauthorised parties accessed an internal reporting system and downloaded information on students, their parents or guardians and school staff. <b>1,079,819 people</b> were affected, <b>all in Australia and New Zealand</b>. The entry point was an <b>unpatched Metabase flaw</b>; access dates back to <b>10 August</b>, with data confirmed downloaded from the Australian reporting database on <b>27 August</b>. Exposed: usernames, first and last names, email addresses, country, time zone, user type, email-verification status, last-active and last-login dates and date joined. <b>Not exposed:</b> academic records, assessment results, passwords, authentication tokens or API credentials. The reporting system has been taken offline; Mathspace began emailing school contacts on <b>4 September</b>.</p>
</div>
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t">Pattern</span></div>
<h3>Self-hosted Metabase is the common thread</h3>
<p>Mathspace is the fourth company named in this pattern. <b>Framework, Tally and Kilo Code</b> all disclosed similar breaches in <b>August 2026</b> after attackers exploited the <b>same SQL injection flaw in their Metabase instances</b>, and this run&#39;s reporting places the Mathspace incident in that same trend. If you run Metabase yourself, the exposed asset is your internal analytics database, and the entry point in every named case was an instance that had not been patched. <span class="mut">The reporting groups these four; it does not claim they are the complete set of victims, and no such claim is made here.</span></p>
</div>
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t hot">Healthcare</span></div>
<h3>Healthcare ransomware up 14% in the first half</h3>
<p><b>410 incidents</b> hit U.S. hospitals, clinics and healthcare businesses in <b>H1 2026</b>, up <b>14%</b>. <b>Qilin</b> and <b>The Gentlemen</b> were the most active strains against healthcare providers; four of Qilin&#39;s confirmed U.S. attacks hit <b>Rocky Mountain Care, FMRS Health Systems, Orthopaedic Specialists of Massachusetts</b> and <b>Aroostook Mental Health Services</b>. Median ransom demands: <b>$310,000</b> for healthcare providers and <b>$300,000</b> for healthcare businesses globally.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t hot">Router</span></div>
<h3>MikroTik: exploitation confirmed in the wild</h3>
<p>Carried and re-confirmed this run from two further sources: hackers are exploiting the new RouterOS flaws to hijack devices <b>without authentication</b>, with the exploitation window opening before the fix shipped. Full detail in the Top Story above.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t">AI</span></div>
<h3>An AI-agent-run intrusion, start to finish in under ten hours</h3>
<p>A human operator using frontier models and agentic frameworks breached an enterprise network in <b>under ten hours</b>, against roughly two weeks for human operators, and left the victim an <b>80-page security audit</b> (2 September). Carried from the previous edition; nothing this run refreshed it.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t">Supply chain</span></div>
<h3>Trezor, via a shipping provider</h3>
<p>A further <b>67,000 U.S. customers</b> exposed through shipping provider <b>ShipMonk</b>, covering orders placed <b>November 2019 to August 2021</b>. Carried from the previous edition.</p>
</div>
</div>

<h2 class="sec">Vulnerability Watch</h2>
<div class="panel">
<table>
<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>
<tr><td>CVE-2026-67276</td><td>9.2</td><td>MikroTik RouterOS</td><td>SSH auth bypass via incomplete RSA public-key validation. <b>Exploited in the wild from 2 September.</b> Fixed 3 September.</td></tr>
<tr><td>CVE-2026-86060</td><td class="mut">not stated</td><td>MikroTik RouterOS</td><td>SSH privilege escalation via crafted username; chains with the above for full admin. <span class="mut">No CVSS appeared in any source read this run.</span></td></tr>
<tr><td>CVE-2026-83548</td><td>10.0</td><td>SonicWall SMA1000</td><td>Pre-auth server-side request forgery. In KEV; SonicWall investigated a case indicating active exploitation.</td></tr>
<tr><td>CVE-2026-83549</td><td class="mut">not stated</td><td>SonicWall SMA1000</td><td>OS command injection; chains with CVE-2026-83548 for unauthenticated RCE. In KEV.</td></tr>
<tr><td>CVE-2026-59822</td><td>8.8</td><td>BerriAI LiteLLM</td><td>Improper authentication on the MCP Streamable HTTP endpoint &mdash; an unauthenticated attacker can establish an authenticated MCP session with an arbitrary Bearer token. In KEV.</td></tr>
<tr><td>CVE-2026-9586</td><td class="mut">not stated</td><td>Sangoma Switchvox</td><td>SQL injection. Weaponised alongside CVE-2026-82329 to deploy reverse shells and mint admin tokens for follow-on enumeration of users, groups, credential sets and federated access topologies. In KEV.</td></tr>
<tr><td>CVE-2026-82329</td><td class="mut">not stated</td><td>JFrog Artifactory</td><td>Improper authentication. See above. In KEV.</td></tr>
<tr><td>CVE-2026-48710</td><td class="mut">not stated</td><td>Kludex Starlette</td><td>HTTP request/response smuggling. In KEV.</td></tr>
<tr><td>CVE-2026-49869</td><td class="mut">not stated</td><td>Kestra OSS</td><td>OS command injection. In KEV.</td></tr>
<tr><td>CVE-2026-85046</td><td class="mut">not stated</td><td>Google Chromium V8</td><td>Type confusion. Added to KEV 4 September.</td></tr>
<tr><td>CVE-2026-75650</td><td>10.0</td><td>Adobe Commerce (APSB26-146)</td><td>&ldquo;StyleSmuggler&rdquo;. Exploited from 4 September. Carried and re-confirmed as one of the maximum-severity items of the past week.</td></tr>
<tr><td>CVE-2026-44756</td><td>10.0</td><td>SAP Extended Passport Processing</td><td>Memory corruption; SAP Note 3747649. From SAP Security Patch Day, 8 September.</td></tr>
<tr><td>CVE-2026-58240</td><td>9.8</td><td>SAP NetWeaver Message Server</td><td>Missing authentication check; SAP Note 3759472.</td></tr>
<tr><td>CVE-2026-76969</td><td>9.4</td><td>SAP <code>sap/cds-mtxs</code></td><td>Credential disclosure up to 1.18.3 / 2.7.6 / 3.9.6 / 4.0.2.</td></tr>
<tr><td>CVE-2026-66768</td><td>9.0</td><td>SAP GUI for Java</td><td>Improper access control.</td></tr>
<tr><td>CVE-2026-59346</td><td>9.3</td><td>VMware Workstation / Fusion</td><td>Integer overflow. <b>Requires a local attacker with elevated privileges</b> &mdash; stated so the 9.3 is not read as an emergency.</td></tr>
<tr><td>CVE-2026-68820</td><td class="mut">not stated</td><td>Windows afd.sys (WinSock)</td><td>Use-after-free; the one exploited zero-day in Microsoft&#39;s August release.</td></tr>
</table>
<p class="note">Where a source read this run did not state a CVSS score, none is printed. Vendor and CISA scores are preferred over figures quoted in blog coverage.</p>
</div>

<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>
<div class="panel">
<ul class="bul">
<li><b>PaperCut &mdash; CVE-2026-81578 and CVE-2026-82078.</b> Added to KEV <b>31 August</b>; remediation due <b>14 September</b>. <b class="down">(6 days left)</b></li>
<li><b>The 2 September batch of seven.</b> Sangoma Switchvox (CVE-2026-9586), Kludex Starlette (CVE-2026-48710), Kestra OSS (CVE-2026-49869), BerriAI LiteLLM (CVE-2026-59822), JFrog Artifactory (CVE-2026-82329) and the SonicWall SMA1000 pair (CVE-2026-83548, CVE-2026-83549). Remediation due <b>16 September</b>. <b class="down">(8 days left)</b></li>
<li><b>Google Chromium V8 &mdash; CVE-2026-85046.</b> Added to KEV <b>4 September</b>; remediation due <b>18 September</b>, a date stated outright by a source rather than inferred. <b class="down">(10 days left)</b></li>
<li><b>No KEV addition after 4 September surfaced in anything read this run</b>, so no fourth countdown has been invented. The three above are the complete set of live federal clocks on this page, and the same three dates appear in the Patch Priority box.</li>
<li><span class="mut"><b>Two conflicting deadline claims were refused this run.</b> A source stated a <b>5 September</b> federal deadline for the SonicWall flaws and a <b>9 September</b> deadline for &ldquo;the rest&rdquo; of a batch. Neither is reconcilable with the 2 September add date and the 16 September due date verified above, and a date that has already passed cannot be presented as a live clock, so both were dropped rather than picked between.</span></li>
<li><span class="mut">Federal remediation timing runs under <b>BOD 26-04: Prioritizing Security Updates Based on Risk</b>, which sets vulnerability-management requirements for Federal Civilian Executive Branch agencies. The older three-week shorthand from BOD 22-01 is <b>not</b> what produced the dates above; each due date here comes from the catalog entry or from a source stating it.</span></li>
</ul>
</div>

<h2 class="sec">Patch Tuesday</h2>
<div class="panel">
<p style="margin:0 0 10px"><b>Microsoft&#39;s September 2026 release ships today, 8 September, at 1:00 PM ET</b> &mdash; effectively at the moment of this edition. <b>No September CVE count or zero-day detail had appeared in anything read this run, so none is printed here.</b> A count will appear in a later edition once the release is actually documented.</p>
<p style="margin:0"><b>The August baseline is itself disputed, and the spread has widened this run.</b> Four sources give four tallies for the same release: <b>421 CVEs</b> (two sources, and the figure this desk carries), <b>400 flaws</b>, <b>398 flaws</b>, and <b>751 CVEs across 67 updates with 108 critical</b>. The critical count remains dropped rather than picked between &mdash; earlier editions carried 42, a later source gave 62, and this run adds 108 on a different denominator. What is agreed: the release contained an exploited zero-day, <b>CVE-2026-68820</b>, a use-after-free in the Ancillary Function Driver for WinSock (afd.sys), alongside publicly disclosed zero-days.</p>
</div>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
@@SRCS@@
</div>
<p class="disc">Compiled automatically from public reporting gathered during this run; nothing was fetched first-hand. Every CVE, CVSS score, deadline and figure above traces to a source listed here or to a standing sourced correction; where a score or date was not stated in a source read this run, it is marked as not stated rather than estimated. Countdowns are computed from today&#39;s date to the verified due date. This is a summary for awareness, not a substitute for your vendor&#39;s advisory or your own risk assessment.</p>
"""

BODY = (BODY.replace("@@MAST@@", masthead("The Cyber Wire", "Your daily security briefing &mdash; breaches, CVEs, KEV deadlines &amp; threat actors"))
            .replace("@@NAV@@", nav("cyber"))
            .replace("@@SRCS@@", srcblock()))

html = page("The Cyber Wire &mdash; Daily Briefings", CSS, BODY)
io.open(os.path.join(OUT, "cyber-briefing.html"), "w", encoding="utf-8").write(html)
print("cyber ok", len(html))
