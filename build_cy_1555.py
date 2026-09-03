# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, "/tmp/db_1788465063")
from shared import page, nav, META, sources
OUT = "/sessions/nifty-sweet-cannon/mnt/outputs"
CY = dict(accent="#22d3a8", accent2="#36c6ff", bg="#0b0f0e", panel="#121917", line="#1e2a27")
FRESH = '<p class="freshline" id="freshline">&nbsp;</p>'
S_CY  = ("A working privilege-escalation exploit for CrowdStrike's Falcon Sensor is now public with no "
         "vendor advisory or patch, while federal agencies have two days left to fix the two SonicWall "
         "SMA1000 zero-days and three other flaws CISA added to its exploited-vulnerability catalog.")

b = []
b.append(f'<header class="mast"><h1>The Cyber Wire</h1><p class="tag">Your daily security briefing &mdash; breaches, exploited bugs and what to patch first</p>{META}</header>')
b.append(f'<div class="tldr"><b>The Wire</b> <span>{S_CY}</span></div>')
b.append(FRESH)
b.append(nav("cyber", CY["accent"]))

b.append("""<div class="banner"><span class="lvl">Threat level: High</span>
<span class="why">Two SonicWall SMA1000 zero-days are being chained for unauthenticated remote code execution and
carry a federal fix-by date two days out, and a public proof-of-concept now claims local privilege escalation
against CrowdStrike's Falcon Sensor with no vendor advisory, CVE or patch.</span></div>""")

b.append('<div class="strip">'
 '<div class="stat"><div class="n">7</div><div class="l">CVEs added to CISA&rsquo;s exploited-vulnerability catalog on Sept 2</div></div>'
 '<div class="stat"><div class="n">10.0</div><div class="l">CVSS for SonicWall CVE-2026-83548, the top of the chain</div></div>'
 '<div class="stat"><div class="n">2 days</div><div class="l">until the Sept 5 federal remediation deadline</div></div>'
 '<div class="stat"><div class="n">11</div><div class="l">U.S. states named in the Thomson Reuters C-Track breach notice</div></div>'
 '</div>')

b.append('<h2 class="sec">Top Story</h2>')
b.append("""<div class="lead">
<h3>A public exploit for CrowdStrike&rsquo;s Falcon Sensor lands with no patch behind it</h3>
<p>A researcher operating as <strong>Nightmare-Eclipse</strong> (also known as Chaotic Eclipse and MSNightmare) has
publicly released <strong>FalconFlank</strong>, a proof-of-concept project claiming a local privilege escalation
vulnerability in CrowdStrike&rsquo;s Falcon Sensor.</p>
<p>The technique abuses Falcon&rsquo;s own automated remediation workflow for malicious Microsoft Office macros
&mdash; the built-in feature that inspects Office documents. The proof of concept is described as working on a fully
updated <strong>Windows 11 25H2</strong> machine or <strong>Windows Server 2025</strong> running Falcon; on success it
writes a file to <code>C:\\Windows\\System32\\MY_SNAKE_IS_SOLID.dll</code> with full permissions for the current user.</p>
<p><strong>What is not established:</strong> at the time of the reporting CrowdStrike had issued no public advisory,
no CVE identifier, no patch notice and no confirmation of the flaw. The FalconFlank README itself suggests Falcon
detections may already identify the released proof of concept. Treat this as an unconfirmed, unpatched local
escalation path on hosts where the agent runs &mdash; not as a remote entry point.</p>
</div>""")

b.append('<h2 class="sec">Patch Priority</h2>')
b.append("""<div class="callout crit"><h3>SonicWall SMA1000 &mdash; federal deadline Saturday, September 5 (2 days left)</h3>
<p><strong>CVE-2026-83548</strong> (CVSS <strong>10.0</strong>), a pre-authentication server-side request forgery in
the Appliance Work Place, is being chained with <strong>CVE-2026-83549</strong> (CVSS <strong>7.8</strong>), an OS
command injection in the Appliance Management Console, to reach unauthenticated remote code execution. Affected
appliances: <strong>SMA1000 6210, 7210 and 8200v</strong>. Fixed in hotfix <strong>12.4.3-03526</strong> and
<strong>12.5.0-02952</strong> and higher. <strong>There is no workaround.</strong> If you find indicators of
compromise, the guidance is to re-image the appliance, rotate all user and admin passwords, and reset TOTP tokens.</p></div>""")

b.append('<h2 class="sec">Threat Actor Spotlight</h2>')
b.append("""<div class="panel"><h3 style="margin:0 0 8px;font-size:17px">The Gentlemen &mdash; and a C2 framework called TukTuk</h3>
<p style="margin:0 0 10px;font-size:14.8px;color:#cfc9c2">Analysts at <strong>Oasis Security</strong> recovered a
complete, previously undocumented remote-control framework from an exposed server at <span class="mono">65.109.70.162</span>
on Hetzner Online infrastructure. The find links the tool to activity associated with the <strong>Gentlemen</strong>
ransomware operation, and was first reported on <strong>September 2, 2026</strong>.</p>
<p style="margin:0 0 10px;font-size:14.8px;color:#cfc9c2">The server held the full <strong>TukTuk v2.0</strong>
project &mdash; Windows and Linux agents, a backend server and an operator control panel. The panel offers server and
agent management, process control, screenshot galleries, credential listings, file upload, predefined command
shortcuts and arbitrary command execution. An operator can trigger a <strong>fake Windows Security prompt</strong>
that resembles the legitimate interface; whatever the user types is recorded.</p>
<p style="margin:0;font-size:14.8px;color:#cfc9c2">Sitting alongside the framework on the same host: a malicious
<strong>DLL sideloading set</strong>, <strong>EDR-disabling tools</strong>, and data believed taken from
<strong>two large organizations</strong>. That combination describes a staged environment able to run from initial
foothold through data theft to ransomware deployment &mdash; which is what makes containment hard and re-intrusion
likely.</p></div>""")

b.append('<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">')
b.append("""<div class="card"><div class="tags"><span class="t crit">Exploit</span><span class="t new">New</span></div>
<h3>FalconFlank proof of concept goes public</h3><p>A local privilege escalation against CrowdStrike Falcon Sensor,
abusing the product&rsquo;s Office macro remediation feature. No CVE, no advisory, no patch at the time of the
reporting.</p></div>""")
b.append("""<div class="card"><div class="tags"><span class="t crit">Ransomware</span><span class="t new">New</span></div>
<h3>The Gentlemen&rsquo;s tooling exposed on an open server</h3><p>The TukTuk v2.0 control framework, EDR-disabling
tools, a DLL sideloading set and data believed taken from two large organizations, all on one host at
65.109.70.162.</p></div>""")
b.append("""<div class="card"><div class="tags"><span class="t warn">Breach</span><span class="t">Courts</span></div>
<h3>Thomson Reuters &mdash; C-Track court case management</h3><p>An unauthorized party obtained files from C-Track,
sold by the West Publishing Corporation unit, in <strong>March 2026</strong>; the activity was not discovered until
<strong>June 30, 2026</strong>. The West Publishing notice names <strong>11 U.S. states, the U.S. Virgin Islands and
Ontario, Canada</strong>; a separate account says 12 states. Both are printed, neither adopted. Exposed data may
include names with Social Security numbers, driver&rsquo;s licence numbers, medical and health-insurance information,
and confidential, redacted or sealed court information. The intrusion was in Thomson Reuters&rsquo; own cloud
environment, not court networks; C-Track remains operational and 12 months of credit monitoring is offered.</p></div>""")
b.append("""<div class="card"><div class="tags"><span class="t warn">Ransomware</span><span class="t">Healthcare</span><span class="t new">New</span></div>
<h3>Five healthcare providers report ransomware-related breaches</h3><p>Alta Orthopaedics (California), Cornerstone
Behavioral Healthcare (Maine), Cameron Regional Medical Center (Missouri), Suntree Internal Medicine (Florida) and
Associated Endocrinologists (Michigan) have all confirmed data breaches stemming from ransomware. Cameron Regional, a
60-bed acute care hospital, announced in <strong>August 2026</strong> that it had been hit; the attack was detected on
<strong>June 18, 2026</strong>, when files on its network were encrypted.</p></div>""")
b.append('</div>')

b.append('<h2 class="sec">Vulnerability Watch</h2><div class="panel"><table>'
 '<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>'
 '<tr><td class="mono">CVE-2026-83548</td><td class="mono crit" style="color:var(--crit)">10.0</td><td>SonicWall SMA1000 &mdash; Appliance Work Place</td><td>Pre-auth SSRF, head of the RCE chain. In KEV, due Sept 5.</td></tr>'
 '<tr><td class="mono">CVE-2026-83549</td><td class="mono">7.8</td><td>SonicWall SMA1000 &mdash; Appliance Management Console</td><td>OS command injection, authenticated admin; chained with 83548. In KEV, due Sept 5.</td></tr>'
 '<tr><td class="mono">CVE-2026-49869</td><td class="mono" style="color:var(--crit)">10.0</td><td>Kestra OSS</td><td>OS command injection. Microsoft reporting: likely exploited in late June 2026 for a reverse shell, Docker container discovery, defense evasion, a cryptocurrency miner and data harvesting. In KEV, due Sept 5.</td></tr>'
 '<tr><td class="mono">CVE-2026-82329</td><td class="mono">9.8</td><td>JFrog Artifactory</td><td>Improper authentication. In KEV, due Sept 5.</td></tr>'
 '<tr><td class="mono">CVE-2026-9586</td><td class="mono">9.3</td><td>Sangoma Switchvox</td><td>SQL injection. In KEV, due Sept 5.</td></tr>'
 '<tr><td class="mono">CVE-2026-59822</td><td class="mono">8.8</td><td>BerriAI LiteLLM</td><td>Improper authentication. In KEV, due Sept 16.</td></tr>'
 '<tr><td class="mono">CVE-2026-48710</td><td class="mono">6.5</td><td>Kludex Starlette</td><td>HTTP request/response smuggling. In KEV, due Sept 16.</td></tr>'
 '<tr><td class="mono">FalconFlank</td><td class="mono">&mdash;</td><td>CrowdStrike Falcon Sensor</td><td>No CVE assigned and no vendor advisory. Public PoC only; <strong>not</strong> in KEV.</td></tr>'
 '</table></div>')

b.append('<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2><div class="panel"><ul class="bul">'
 '<li><strong>Saturday, September 5 &mdash; <span style="color:var(--crit)">2 days left</span>.</strong> Five of the '
 'seven CVEs added on September 2: <span class="mono">CVE-2026-83548</span> and <span class="mono">CVE-2026-83549</span> '
 '(SonicWall SMA1000), plus three others &mdash; <span class="mono">CVE-2026-9586</span> (Sangoma Switchvox), '
 '<span class="mono">CVE-2026-82329</span> (JFrog Artifactory) and <span class="mono">CVE-2026-49869</span> (Kestra OSS).</li>'
 '<li><strong>Wednesday, September 16 &mdash; 13 days left.</strong> The remaining two: '
 '<span class="mono">CVE-2026-48710</span> (Kludex Starlette) and <span class="mono">CVE-2026-59822</span> (BerriAI LiteLLM).</li>'
 '<li>The directive cited on the September 2 addition is <strong>BOD 26-04, &ldquo;Prioritizing Security Updates Based '
 'on Risk&rdquo;</strong> &mdash; recorded as CISA states it.</li>'
 '<li>The Kestra entry was driven by a Microsoft report describing exploitation in <strong>late June 2026</strong> to '
 'establish a reverse shell, enumerate a Docker container environment, evade defenses, deploy a cryptocurrency miner '
 'and harvest data.</li>'
 '</ul></div>')

b.append(sources([
 ("The Register &mdash; Prolific Microsoft 0-day hunter drops CrowdStrike Falcon exploit PoC", "https://www.theregister.com/security/2026/09/03/prolific-microsoft-0-day-hunter-drops-crowdstrike-falcon-exploit-poc/5294318"),
 ("The Hacker News &mdash; Researcher Releases FalconFlank PoC", "https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html"),
 ("Security Affairs &mdash; Chaotic Eclipse releases CrowdStrike Falcon zero-day FalconFlank", "https://securityaffairs.com/198342/hacking/chaotic-eclipse-releases-crowdstrike-falcon-zeroday-falconflank.html"),
 ("Cyber Security News &mdash; Ransomware hackers use new TukTuk malware", "https://cybersecuritynews.com/new-tuktuk-malware/"),
 ("GBHackers &mdash; The Gentlemen ransomware hackers use TukTuk C2", "https://gbhackers.com/tuktuk-c2-framework/"),
 ("CISA &mdash; CISA Adds Seven Known Exploited Vulnerabilities to Catalog (Sept 2, 2026)", "https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog"),
 ("The Hacker News &mdash; CISA adds seven exploited flaws as attackers deploy reverse shells", "https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html"),
 ("The Hacker News &mdash; Thomson Reuters court software breach", "https://thehackernews.com/2026/09/thomson-reuters-court-software-breach.html"),
 ("HIPAA Journal &mdash; Five healthcare providers report ransomware-related data breaches", "https://www.hipaajournal.com/ransomware-healthcare-providers-ca-ma-mo-fl-mi/"),
]))
b.append('<p class="disc">The Cyber Wire is an automated summary of published security reporting. Severity scores and '
 'remediation deadlines are quoted from vendor and CISA sources where available. Verify against your own vendor '
 'advisories before acting.</p></footer>')

H = page("The Cyber Wire &mdash; Daily Briefings", CY["accent"], CY["accent2"], CY["bg"], CY["panel"], CY["line"], "\n".join(b))
open(os.path.join(OUT, "cyber-briefing.html"), "w").write(H)
print("cyber ok", len(H))
