# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------------- summaries (must be byte-identical on index cards) ----------------
S_CY = ("Microsoft shipped the largest Patch Tuesday on record &mdash; about 974 CVEs &mdash; including two Windows "
        "privilege-escalation flaws already exploited as zero-days and twenty bugs that could be classed as wormable, "
        "while the maximum-severity N-able N-central flaw reaches its federal remediation deadline today.")
S_WS = ("Wall Street is snapping a four-day losing streak, with all three major indexes up around 1.1% on reads through "
        "2:18 PM ET as oil retreats and an in-line August CPI leaves a Fed hike next Wednesday all but priced &mdash; "
        "even as Treasury yields set fresh 52-week highs across the curve.")
S_MMA = ("Every fighter on the thirteen-bout Noche UFC card made weight in Glendale, where Jean Silva headlines against "
         "short-notice replacement Jose Miguel Delgado on Saturday, a week after Salahdine Parnasse&rsquo;s first-round TKO "
         "of Dan Hooker topped the highest-grossing event in Accor Arena history.")

def tldr(label, text, ):
    return '<div class="tldr"><b>%s</b> <span>%s</span></div>' % (label, text)

FRESH = '<div class="freshline" id="freshline">&nbsp;</div>'

def srcblock(items):
    return "".join('<div style="margin-bottom:7px">%s &mdash; <a href="%s">%s</a></div>' % (t, u, u) for t, u in items)

# =================================================================== CYBER
CY_ACC, CY_ACC2 = "#22d3a8", "#36c6ff"
CY_CSS = css(CY_ACC, CY_ACC2, "#080d0c", "#0f1716", "#1d2b29")

CY_SRC = [
 ("Help Net Security - September 2026 Patch Tuesday: Record patch count, 2 zero-days, and a SigRed successor",
  "https://www.helpnetsecurity.com/2026/09/09/september-2026-patch-tuesday-zero-days-sigred-successor/"),
 ("SecurityWeek - Microsoft Patches Record 974 Vulnerabilities, Including Two Exploited Zero-Days",
  "https://www.securityweek.com/microsoft-patches-record-974-vulnerabilities-including-two-exploited-zero-days/"),
 ("Security Affairs - Microsoft's Biggest Patch Tuesday: 974 CVEs, 2 Zero-Days and 20 Wormable Bugs",
  "https://securityaffairs.com/198705/security/microsofts-biggest-patch-tuesday-974-cves-2-zero-days-and-20-wormable-bugs.html"),
 ("CrowdStrike - September 2026 Patch Tuesday: Updates and Analysis",
  "https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-september-2026/"),
 ("Zero Day Initiative - The September 2026 Security Update Review",
  "https://www.zerodayinitiative.com/blog/2026/9/8/the-september-2026-security-update-review"),
 ("The Hacker News - Attackers Exploit PaperCut Flaws to Steal Credentials From Schools and Universities",
  "https://thehackernews.com/2026/09/attackers-exploit-papercut-flaws-to.html"),
 ("Arctic Wolf Adversary Research - PaperCut CVE exploitation alert pack",
  "https://github.com/rtkwlf/wolf-tools/tree/main/pack_alerts/202609-papercut-cve-exploitation"),
 ("The Hacker News - CISA Adds Seven Exploited Flaws as Attackers Deploy Reverse Shells and Crypto Miners",
  "https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html"),
 ("CISA - CISA Adds Seven Known Exploited Vulnerabilities to Catalog (Sept 2, 2026)",
  "https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog"),
 ("Microsoft Security Blog - When AI infrastructure becomes a target: securing gateways and control points",
  "https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/"),
 ("Wiz - AI infrastructure honeypot research",
  "https://www.wiz.io/blog/ai-infrastructure-honeypot"),
 ("The Hacker News - N-able N-central Pre-Auth RCE Flaw Exploited in the Wild",
  "https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html"),
 ("Help Net Security - Cisco FMC bugs exploited by nation-state and ransomware actors (CVE-2026-20079, CVE-2026-20316)",
  "https://www.helpnetsecurity.com/2026/09/10/cisco-fmc-exploited-cve-2026-20079-cve-2026-20316/"),
 ("The Hacker News - Google Releases Chrome Update to Patch Actively Exploited V8 Zero-Day",
  "https://thehackernews.com/2026/09/google-releases-chrome-update-to-patch.html"),
 ("CISA - Known Exploited Vulnerabilities Catalog",
  "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
 ("Senserva - CISA KEV Additions This Week: 11 New Exploited CVEs (September 2026)",
  "https://senserva.com/exploited-this-week.html"),
]

CY_BODY = """@@MAST@@
@@TLDR@@
@@FRESH@@
@@NAV@@

<div class="banner">
<span class="lvl">Threat level: High</span>
<span>Two Windows privilege-escalation flaws are being exploited as zero-days in the same release that fixes a record number of CVEs, and a maximum-severity N-able N-central bug already under attack reaches its federal remediation deadline <b>today</b>.</span>
</div>

<div class="stats">
<div class="stat"><div class="n">~974</div><div class="l">CVEs in Microsoft&rsquo;s September Patch Tuesday, the largest on record (SecurityWeek, Security Affairs; other tallies 966&ndash;973)</div></div>
<div class="stat"><div class="n">20</div><div class="l">Windows bugs ZDI classes as potentially wormable &mdash; remote, unauthenticated, no user interaction</div></div>
<div class="stat"><div class="n">2</div><div class="l">Windows privilege-escalation flaws in that release already exploited as zero-days</div></div>
<div class="stat"><div class="n">0 days</div><div class="l">Left on the N-able N-central KEV deadline &mdash; FCEB agencies must remediate by today, 11 September</div></div>
</div>

<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<div class="tags"><span class="t new">New</span><span class="t hot">Zero-day</span><span class="t">Patch Tuesday</span></div>
<h3 style="font-size:20px;margin:0 0 9px">Microsoft&rsquo;s Record Patch Tuesday Carries Two Exploited Windows Zero-Days &mdash; and Twenty Bugs ZDI Calls Wormable</h3>
<p>September 2026 Patch Tuesday was, in Help Net Security&rsquo;s words, &ldquo;another record-breaking number of patches.&rdquo; <b>SecurityWeek and Security Affairs both put the count at 974 CVEs</b>, the largest single Patch Tuesday on record; other outlets tallied between 966 and 973, so the figure is printed as approximate rather than reconciled. <b>Two of the flaws were already being exploited as zero-days</b>, and both are privilege escalations to SYSTEM.</p>
<p><b>CVE-2026-81963</b> sits in the <b>Windows Update Stack</b>, the component used to install Windows updates. It is caused by improper link resolution before file access combined with improper access control, and it lets an <b>authenticated attacker with low privileges gain SYSTEM</b>. It affects various Windows 11 versions and <b>Windows Server 2025</b>, and was reported by <b>Microsoft&rsquo;s Threat Intelligence Centre (MSTIC)</b>. Tenable&rsquo;s <b>Satnam Narang</b> notes there have been seven privilege-escalation flaws in the Windows Update Stack since 2022, but this is <b>the first zero-day and the first to be exploited</b>. ZDI&rsquo;s <b>Dustin Childs</b> doubts the automatic update process itself is compromised, and reads it as more likely being combined with a code-execution bug to spread malware or ransomware.</p>
<p><b>CVE-2026-85880</b> is a privilege escalation to SYSTEM in the <b>Windows Advanced Local Procedure Call</b> &mdash; described in coverage of the release as a heap buffer overflow. It affects <b>Windows 10 and the older Windows Server builds (2012, 2016, 2019 and 2022)</b>, and was reported by <b>Proofpoint</b> researchers. CrowdStrike observes that this class of flaw &ldquo;has historically appeared in post-compromise tooling used by both commodity malware and targeted intrusion operators as a reliable final step from user-mode to kernel-mode control.&rdquo; <span class="mut">Neither zero-day carries a CVSS score in any source read this run, so none is printed for either.</span></p>
<p style="margin-bottom:0">Beyond the two, Childs tells organisations to prioritise <b>a cluster of 20 bugs affecting most supported Windows versions that could be classified as wormable</b> &mdash; &ldquo;a remote, unauthenticated attacker could get arbitrary code execution on affected systems with no user interaction.&rdquo; He singles out a DNS flaw, <b>CVE-2026-69730</b>, as <b>&ldquo;the spiritual successor to SigRed&rdquo;</b>, the 2020 wormable DNS bug. Also flagged: <b>CVE-2026-69676</b>, a Kerberos authentication bypass leading to RCE and rated Exploitation More Likely &mdash; &ldquo;one phished workstation account, one crafted request, code execution on the DC. That&rsquo;s a domain-compromise primitive&rdquo; &mdash; and <b>CVE-2026-80093</b> in the Windows Cloud Files Mini Filter Driver, where technical details are already public via Talos (TALOS-2026-2445) though exploitation requires winning a race condition. Outside Windows, Childs advises prioritising <b>Microsoft Exchange Server</b> for <b>CVE-2026-55007</b>, an RCE triggered when Exchange processes an email carrying a malicious Visio attachment, plus a set of SharePoint Server fixes. Within hours of the release, the anonymous researcher <b>Nightmare Eclipse</b> published <b>ShieldCrash</b>, a proof-of-concept that ostensibly bypasses the patch for <b>CVE-2026-69414</b> (&ldquo;ShieldBreak&rdquo;), a privilege-escalation bug in the Microsoft Malware Protection Engine.</p>
</div>

<h2 class="sec">Patch Priority</h2>
<div class="callout crit">
<h3>Due today &mdash; CVE-2026-86218, N-able N-central (CVSS 10.0)</h3>
<p style="margin:0 0 9px"><b>The single most urgent item for defenders today is CVE-2026-86218</b>, a maximum-severity static code injection flaw in <b>N-able N-central</b> that is <b>exploited in the wild</b>. CISA added it to the Known Exploited Vulnerabilities catalog with an <b>FCEB remediation deadline of 11 September 2026 &mdash; that is today, 0 days left</b>. The fix is <b>N-central 2026.3 Hotfix 4</b>, released <b>5 September 2026</b>.</p>
<p style="margin:0">N-central is used by MSPs, MSSPs and large IT organisations to manage entire customer and corporate estates, which makes it strategically valuable to ransomware crews in particular: one compromised console reaches every managed environment behind it. <b>Tomorrow&rsquo;s deadline &mdash; 12 September, 1 day left &mdash; covers the Cisco Secure FMC, Citrix NetScaler and Fortinet trio</b> listed in the KEV section below; this callout, that section and the countdowns all carry the same verified dates.</p>
</div>

<h2 class="sec">Threat Actor Spotlight</h2>
<div class="card">
<div class="tags"><span class="t hot">Ransomware</span><span class="t">Qilin / Agenda</span></div>
<h4>Qilin is turning up on both ends of the AI-infrastructure problem</h4>
<p><b>Qilin</b> (also tracked as <b>Agenda</b>) appears in two separate strands of this week&rsquo;s reporting. Google-owned <b>Wiz</b> links threat actors associated with Qilin to active exploitation of the <b>Berri LiteLLM</b> chain &mdash; <b>CVE-2026-42271</b> (CVSS 8.7) chained with <b>CVE-2026-48710</b> to bypass authentication and reach remote code execution against exposed LiteLLM deployments. Separately, in Cisco Talos&rsquo;s account of the Secure Firewall Management Center intrusions carried below, one of the three activity clusters is <b>a suspected Qilin ransomware operator</b> using the static hard-coded credentials of <b>CVE-2026-20316</b>, deploying antivirus killers and then ransomware. <span class="mut">The common thread is not a technique but a target class: management and gateway planes that sit above many downstream systems at once.</span></p>
</div>

<h2 class="sec">Breaches &amp; Incidents</h2>
<div class="cards">

<div class="card">
<div class="tags"><span class="t new">New</span><span class="t hot">Education</span><span class="t">Credential theft</span></div>
<h4>PaperCut servers are being chained for credential theft across schools and universities</h4>
<p>The <b>Arctic Wolf Adversary Research Team</b> reports attackers exploiting the newly disclosed PaperCut pair &mdash; <b>CVE-2026-81578</b> (authentication bypass) and <b>CVE-2026-82078</b> (remote code execution) &mdash; as a chain for command execution, reconnaissance and privileged account creation. Arctic Wolf told The Hacker News the activity has hit vulnerable PaperCut servers <b>across the education sector, from K-12 schools to major universities in the U.S. and Europe</b>.</p>
<p style="margin:9px 0 0">Observed behaviour includes discovery commands (<code>uname</code>, <code>whoami</code>, <code>ver</code>, <code>tasklist</code>), creation of a privileged account named <b>&ldquo;Administrator17&rdquo;</b>, and delivery of credential-harvesting tools (<code>lsa_collect.exe</code>, <code>lsa_collect_small.exe</code>, <code>save_hives.exe</code>) via <code>certutil.exe</code> from <b>45.142.193[.]132</b>, with Meterpreter Java payloads retrieved from <b>194.180.48[.]134</b>. Attackers ran <code>findstr</code> across PaperCut <code>*.config</code> files for &ldquo;password&rdquo;, &ldquo;secret&rdquo;, &ldquo;ldap&rdquo;, &ldquo;bind&rdquo; and &ldquo;token&rdquo;. In a sandbox, <code>lsa_collect.exe</code> extracted registry keys to reconstruct the system <b>BootKey</b>, which grants access to the SAM database. Arctic Wolf&rsquo;s advice: keep PaperCut servers off the internet, and alert on <code>cmd.exe</code> or <code>powershell.exe</code> with <b>pc-app.exe as the parent process</b>.</p>
</div>

<div class="card">
<div class="tags"><span class="t new">New</span><span class="t hot">AI infrastructure</span><span class="t">Cryptojacking</span></div>
<h4>Microsoft and Wiz: AI gateways are now a routine intrusion target</h4>
<p>Microsoft&rsquo;s research describes a <b>Kestra</b> compromise via <b>CVE-2026-49869</b> (CVSS 10.0) in which an actor established a reverse shell, enumerated the Docker container environment, evaded defences, deployed a cryptocurrency miner and harvested data. Microsoft identifies <b>four impact paths</b>: shell execution through the workflow engine, container-environment exposure through Docker socket access, host resource hijacking through miner deployment, and follow-on collection through workflow task execution.</p>
<p style="margin:9px 0 0">In a parallel campaign, attackers broke into <b>LiteLLM</b> gateways using <b>CVE-2026-42271</b> and <b>CVE-2026-48710</b> to deliver an <b>XMRig</b> miner as an ELF binary, fingerprinting the host and killing competing mining processes first. They then reached the LiteLLM-backed <b>PostgreSQL</b> tier, targeting <code>LiteLLM_ProxyModelTable</code> and <code>LiteLLM_VerificationToken</code> to harvest model configuration, <b>upstream provider key material</b>, provider endpoints and proxy-issued virtual keys, with persistence added through <code>~/.ssh/authorized_keys</code>. Microsoft also suspects exposed <b>RAGFlow</b> instances are being exploited through CVE-2026-45312, CVE-2026-28797, CVE-2026-24770, CVE-2025-68700 and CVE-2025-69286 to steal LLM provider keys. Microsoft&rsquo;s conclusion: &ldquo;Defenders should monitor AI workloads according to their control-plane role, not only as isolated applications.&rdquo;</p>
</div>

<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t hot">CVSS 10.0</span></div>
<h4>Cisco Secure FMC: Sandworm and a suspected Qilin operator, still on tomorrow&rsquo;s clock</h4>
<p>Cisco Talos confirmed two Secure Firewall Management Center flaws under attack: <b>CVE-2026-20079</b> (CVSS 10.0), an authentication bypass from an improper boot-time system process giving unauthenticated <b>root</b> RCE via crafted HTTP, and <b>CVE-2026-20316</b>, static hard-coded credentials for a low-privileged account. Three clusters were identified &mdash; a web shell in the CSM Tomcat webroot followed by a malicious JAR; <b>Sandworm</b>, using a malicious <code>license.tmp</code> to open a reverse shell, harvest managed-firewall configurations and install a credential and packet-sniffing implant; and a suspected <b>Qilin</b> operator. Cisco became aware of exploitation in <b>August 2026</b>; the hardening release is due <b>the week of 16 September</b>, with hotfixes available now. <span class="mut">No CVSS appears for CVE-2026-20316 in any source read this run, so none is printed.</span></p>
</div>

<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t hot">Chrome</span></div>
<h4>The Chrome V8 zero-day runs to a different clock</h4>
<p>Google&rsquo;s Stable Channel release fixed <b>230</b> flaws including <b>CVE-2026-87491</b>, an out-of-bounds write in <b>V8</b>. NVD&rsquo;s wording: the bug &ldquo;allowed a remote attacker to execute arbitrary code <b>inside the sandbox</b> via a crafted HTML page.&rdquo; Google says it is aware an exploit exists in the wild but has withheld attribution. It was reported on <b>6 August 2026</b> by <b>Jihyeon Jeong</b> of the Compsec Lab at Seoul National University for a <b>$2,500</b> bounty, and is the <b>seventh</b> actively exploited Chrome zero-day of 2026. Fixed builds are <b>153.0.8010.36/.37</b> on Windows and macOS and <b>153.0.8010.36</b> on Linux. CISA added it on <b>9 September</b> with a deadline of <b>23 September 2026</b> &mdash; a longer clock than the 12 September trio added the same day. <span class="mut">The Hacker News records its CVSS as &ldquo;N/A&rdquo;, so none is printed.</span></p>
</div>

<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t hot">Ransomware</span></div>
<h4>WatchGuard Firebox: a KEV entry that escalated into ransomware</h4>
<p>CISA confirmed on <b>9 September</b> that <b>CVE-2025-14733</b> &mdash; an out-of-bounds write giving unauthenticated RCE at low attack complexity, affecting Fireware 11.x (including 11.12.4_Update1), 12.x (including 12.11.5) and 2025.1&ndash;2025.1.3 &mdash; is now being used in <b>ransomware campaigns</b>. It has been in KEV since December, when Shadowserver counted <b>115,000+</b> exposed devices; <b>nearly 9,000 remain unsecured</b> nine months on. Only <b>IKEv2 VPN</b> configurations are exploitable, but a device can remain compromised after the configuration is deleted if a <b>branch-office VPN to a static gateway peer</b> is still present. <span class="mut">No CVSS is printed &mdash; none appears in the reads this run.</span></p>
</div>

<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t gold">Availability</span></div>
<h4>September Windows Server updates are still breaking Remote Desktop</h4>
<p><b>KB5122876</b> (Server 2019), <b>KB5122882</b> (2022) and <b>KB5122871</b> (2025) break Remote Desktop Services hours after installation or on logout. One administrator traced the fault to a mutual block between the RD service and <b>LSM</b>. There is still <b>no Microsoft fix and no confirmed cause</b>; rolling the update back restores RDS but gives up that month&rsquo;s security fixes &mdash; an unwelcome trade in a month this size.</p>
</div>

</div>

<h2 class="sec">Vulnerability Watch</h2>
<div class="panel">
<table>
<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>
<tr><td><b>CVE-2026-86218</b></td><td class="down">10.0</td><td>N-able N-central</td><td>Static code injection; exploited in the wild. Fixed in N-central 2026.3 Hotfix 4 (5 Sep 2026). <b>KEV deadline today.</b></td></tr>
<tr><td><b>CVE-2026-20079</b></td><td class="down">10.0</td><td>Cisco Secure Firewall Management Center</td><td>Auth bypass &rarr; unauthenticated root RCE via crafted HTTP. Sandworm and a suspected Qilin operator observed.</td></tr>
<tr><td><b>CVE-2026-49869</b></td><td class="down">10.0</td><td>Kestra OSS</td><td>OS command injection; unauthenticated attacker can create and execute arbitrary workflows. Miner deployment observed.</td></tr>
<tr><td><b>CVE-2026-83548</b></td><td class="down">10.0</td><td>SonicWall SMA 1000 Appliances</td><td>Unauthenticated SSRF; chains with CVE-2026-83549 toward RCE.</td></tr>
<tr><td><b>CVE-2026-82329</b></td><td class="down">9.8</td><td>JFrog Artifactory</td><td>Improper authentication; under default configuration an unauthenticated attacker can obtain administrative privileges.</td></tr>
<tr><td><b>CVE-2026-9586</b></td><td class="down">9.3</td><td>Sangoma Switchvox</td><td>Unauthenticated SQL injection against the backend PostgreSQL database via a single crafted request; reverse shells observed.</td></tr>
<tr><td><b>CVE-2026-19490</b></td><td class="down">9.3</td><td>Citrix NetScaler ADC / Gateway</td><td>KEV deadline 12 September. Previdian honeypots logged 56 attempts since 3 September, 36 on 8 September alone.</td></tr>
<tr><td><b>CVE-2026-59822</b></td><td>8.8</td><td>Berri LiteLLM (MCP Streamable HTTP)</td><td>Improper authentication; an unauthenticated attacker can establish an authenticated MCP session with an arbitrary Bearer token.</td></tr>
<tr><td><b>CVE-2026-42271</b></td><td>8.7</td><td>Berri LiteLLM</td><td>Chains with CVE-2026-48710 to bypass auth and reach RCE; Qilin-associated actors linked by Wiz.</td></tr>
<tr><td><b>CVE-2026-83549</b></td><td>7.8</td><td>SonicWall SMA 1000 Appliances</td><td>Post-authentication OS command injection as administrator &rarr; RCE.</td></tr>
<tr><td><b>CVE-2025-25249</b></td><td>7.3</td><td>Fortinet FortiOS / FortiSwitchManager / FortiSASE</td><td>KEV deadline 12 September. SOCRadar ties it to the PivotC2 Node.js RAT: 3,000+ IPs targeted, 178 devices infected.</td></tr>
<tr><td><b>CVE-2026-48710</b></td><td>6.5</td><td>Kludex Starlette</td><td>HTTP request/response smuggling; path injection into the host part can bypass URL-path-dependent authentication.</td></tr>
<tr><td><b>CVE-2026-81963</b></td><td class="mut">not stated</td><td>Windows Update Stack (Win 11, Server 2025)</td><td>Exploited zero-day. Improper link resolution + improper access control &rarr; SYSTEM. Reported by MSTIC.</td></tr>
<tr><td><b>CVE-2026-85880</b></td><td class="mut">not stated</td><td>Windows ALPC (Win 10, Server 2012&ndash;2022)</td><td>Exploited zero-day. Privilege escalation to SYSTEM. Reported by Proofpoint.</td></tr>
<tr><td><b>CVE-2026-69730</b></td><td class="mut">not stated</td><td>Windows DNS</td><td>Among the 20 wormable bugs; ZDI calls it &ldquo;the spiritual successor to SigRed&rdquo;.</td></tr>
<tr><td><b>CVE-2026-69676</b></td><td class="mut">not stated</td><td>Windows Kerberos</td><td>Auth bypass &rarr; RCE on a domain controller. Rated Exploitation More Likely.</td></tr>
<tr><td><b>CVE-2026-87491</b></td><td class="mut">not stated</td><td>Google Chrome (V8)</td><td>Out-of-bounds write, exploited in the wild. Fixed in 153.0.8010.36/.37. KEV deadline 23 September.</td></tr>
<tr><td><b>CVE-2026-20316</b></td><td class="mut">not stated</td><td>Cisco Secure FMC</td><td>Static hard-coded credentials for a low-privileged account. Disclosed and fixed 29 July; KEV the same day.</td></tr>
<tr><td><b>CVE-2025-14733</b></td><td class="mut">not stated</td><td>WatchGuard Fireware (IKEv2 VPN)</td><td>Out-of-bounds write &rarr; unauthenticated RCE; now used in ransomware campaigns.</td></tr>
</table>
<p class="note">A CVSS is printed only where a vendor, CISA or NVD figure appeared in a source read this run. Where a score was absent the cell reads &ldquo;not stated&rdquo; rather than carrying a number from a secondary write-up.</p>
</div>

<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>
<div class="panel">
<ul class="bul">
<li><b>CVE-2026-86218 &mdash; N-able N-central (10.0).</b> FCEB remediation due <b>11 September 2026</b> &mdash; <b class="down">0 days left (due today)</b>.</li>
<li><b>CVE-2026-20079 (Cisco Secure FMC, 10.0), CVE-2026-19490 (Citrix NetScaler ADC/Gateway, 9.3) and CVE-2025-25249 (Fortinet FortiOS/FortiSwitchManager/FortiSASE, 7.3).</b> Added 9 September; due <b>12 September 2026</b> &mdash; <b class="down">1 day left</b>.</li>
<li><b>CVE-2026-48710 (Starlette, 6.5) and CVE-2026-59822 (Berri LiteLLM, 8.8).</b> From the 2 September batch; due <b>16 September 2026</b> &mdash; <b>5 days left</b>.</li>
<li><b>CVE-2026-87491 &mdash; Chrome V8.</b> Added 9 September; due <b>23 September 2026</b> &mdash; <b>12 days left</b>. A different clock from the trio added the same day.</li>
<li><b>The rest of the 2 September batch &mdash; CVE-2026-83548, CVE-2026-83549, CVE-2026-9586, CVE-2026-82329 and CVE-2026-49869 &mdash;</b> carried a due date of <b>5 September 2026</b> and is now <b class="down">overdue by 6 days</b> for any agency that has not remediated.</li>
<li><b>MikroTik: still no countdown.</b> For a fourth consecutive edition, no source read this run states a KEV due date for <b>CVE-2026-67277</b> or <b>CVE-2026-86060</b>, so <b>no deadline and no countdown are asserted</b>. Fixes are 6.49.21 / 7.23.4 / 7.24.2 / 7.25beta3.</li>
</ul>
<p class="note">Deadlines are assigned per CVE under <b>BOD 26-04</b>, which is risk-based: two CVEs added on the same day can carry very different clocks, as the 12 and 23 September dates above show. No fixed remediation window is assumed anywhere on this page &mdash; each countdown is computed from today, 11 September 2026, to the due date CISA itself states for that individual CVE.</p>
</div>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
@@SRCS@@
</div>
<p class="disc">Compiled automatically from public reporting gathered during this run. Every claim above traces to a source listed here or to a standing sourced correction; where a CVSS, deadline or attribution was not stated by a primary source, this page says so rather than supplying one. This is a news summary, not security advice &mdash; verify against your own vendor advisories before acting.</p>
"""

CY_BODY = (CY_BODY.replace("@@MAST@@", masthead("The Cyber Wire", "Your daily cybersecurity briefing &mdash; breaches, exploited flaws &amp; federal deadlines"))
                  .replace("@@TLDR@@", tldr("The Wire", S_CY))
                  .replace("@@FRESH@@", FRESH)
                  .replace("@@NAV@@", nav("cyber"))
                  .replace("@@SRCS@@", srcblock(CY_SRC)))
io.open(os.path.join(OUT, "cyber-briefing.html"), "w", encoding="utf-8").write(
    page("The Cyber Wire &mdash; Daily Briefings", CY_CSS, CY_BODY))
print("cyber ok")
