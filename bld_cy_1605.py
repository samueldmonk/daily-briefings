# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page
from common_1605 import S_CY, tldr, FRESH, srcblock

OUT = os.path.dirname(os.path.abspath(__file__))
ACC, ACC2 = "#22d3a8", "#36c6ff"
CSS = css(ACC, ACC2, "#080d0c", "#0f1716", "#1d2b29")

SRC = [
 ("The Hacker News - CISA Flags Exploited Cisco, Citrix, Fortinet Flaws, Sets Sept. 12 Federal Patch Deadline",
  "https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html"),
 ("CISA - CISA Adds Four Known Exploited Vulnerabilities to Catalog (Sept 9, 2026)",
  "https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog"),
 ("CISA - CISA Adds Four Known Exploited Vulnerabilities to Catalog (Sept 8, 2026)",
  "https://www.cisa.gov/news-events/alerts/2026/09/08/cisa-adds-four-known-exploited-vulnerabilities-catalog"),
 ("CISA - CISA Adds Seven Known Exploited Vulnerabilities to Catalog (Sept 2, 2026)",
  "https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog"),
 ("CISA - Known Exploited Vulnerabilities Catalog",
  "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
 ("Cisco - Security Advisory: On-Prem FMC authentication bypass (cisco-sa-onprem-fmc-authbypass-5JPp45V2)",
  "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2"),
 ("Fortinet FortiGuard PSIRT - FG-IR-25-084 (CVE-2025-25249)",
  "https://fortiguard.fortinet.com/psirt/FG-IR-25-084"),
 ("SOCRadar - CVE-2025-25249 and the PivotC2 FortiGate RAT campaign",
  "https://socradar.io/blog/cve-2025-25249-pivotc2-fortigate-rat/"),
 ("BleepingComputer - AI-powered attack exploited PaperCut flaws to hack 395 organizations",
  "https://www.bleepingcomputer.com/news/security/ai-powered-attack-exploited-papercut-flaws-to-hack-395-organizations/"),
 ("BleepingComputer - IDScan confirms breach tied to 153 million stolen driver's licenses",
  "https://www.bleepingcomputer.com/news/security/idscan-confirms-breach-tied-to-153-million-stolen-drivers-licenses/"),
 ("BleepingComputer - AdaptHealth confirms 4.1 million people exposed in July cyberattack",
  "https://www.bleepingcomputer.com/news/security/adapthealth-confirms-41-million-people-exposed-in-july-cyberattack/"),
 ("BleepingComputer - Trezor: 347,000 users targeted in phishing attacks after Brevo breach",
  "https://www.bleepingcomputer.com/news/security/trezor-347-000-users-targeted-in-phishing-attacks-after-brevo-breach/"),
 ("BleepingComputer - Surfshark VPN says hackers breached internal testing, proxy servers",
  "https://www.bleepingcomputer.com/news/security/surfshark-vpn-says-hackers-breached-internal-testing-proxy-servers/"),
 ("BleepingComputer - Cisco FMC flaws exploited by ransomware gang, state-sponsored hackers",
  "https://www.bleepingcomputer.com/news/security/cisco-fmc-flaws-exploited-by-ransomware-gang-state-sponsored-hackers/"),
 ("BleepingComputer - Conti ransomware gang member sentenced to 4 years in prison",
  "https://www.bleepingcomputer.com/news/security/conti-ransomware-gang-member-sentenced-to-four-years-in-prison/"),
 ("BleepingComputer - GitLab urges users to patch max severity path traversal flaw",
  "https://www.bleepingcomputer.com/news/security/gitlab-urges-users-to-patch-max-severity-path-traversal-flaw/"),
 ("BleepingComputer - Microsoft September 2026 Patch Tuesday fixes 966 flaws, 2 zero-days",
  "https://www.bleepingcomputer.com/news/microsoft/microsoft-september-2026-patch-tuesday-fixes-966-flaws-2-zero-days/"),
 ("BleepingComputer - New Microsoft Defender 'ShieldCrash' zero-day grants SYSTEM access",
  "https://www.bleepingcomputer.com/news/security/new-microsoft-defender-shieldcrash-zero-day-grants-system-access/"),
 ("BleepingComputer - September Windows Server updates break Remote Desktop Services",
  "https://www.bleepingcomputer.com/news/microsoft/september-windows-server-updates-break-remote-desktop-services/"),
 ("BleepingComputer - Over 36,000 exposed Plex servers vulnerable to recent flaws",
  "https://www.bleepingcomputer.com/news/security/over-36-000-plex-servers-unpatched-against-recently-disclosed-flaws/"),
 ("BleepingComputer - CISA: WatchGuard RCE flaw now exploited in ransomware attacks",
  "https://www.bleepingcomputer.com/news/security/cisa-watchguard-rce-flaw-now-exploited-in-ransomware-attacks/"),
 ("BleepingComputer - New 'BlueMoon' kit exploited Windows and Chrome zero-day flaws",
  "https://www.bleepingcomputer.com/news/security/new-bluemoon-kit-exploited-windows-and-chrome-zero-day-flaws/"),
 ("The Hacker News - CISA Adds Seven Exploited Flaws as Attackers Deploy Reverse Shells and Crypto Miners",
  "https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html"),
 ("The Hacker News - N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw",
  "https://thehackernews.com/2026/09/n-able-issues-fourth-n-central-hotfix.html"),
 ("Help Net Security - September 2026 Patch Tuesday: Record patch count, 2 zero-days, and a SigRed successor",
  "https://www.helpnetsecurity.com/2026/09/09/september-2026-patch-tuesday-zero-days-sigred-successor/"),
 ("SecurityWeek - Microsoft Patches Record 974 Vulnerabilities, Including Two Exploited Zero-Days",
  "https://www.securityweek.com/microsoft-patches-record-974-vulnerabilities-including-two-exploited-zero-days/"),
]

CVES = [
 ("CVE-2026-20079", "10.0", "Cisco Secure Firewall Management Center (on-prem)",
  "Authentication bypass in the web interface: an unauthenticated remote attacker can execute script files and obtain "
  "root on the underlying OS. Cisco updated its advisory to say it became aware of active exploitation in August 2026."),
 ("CVE-2026-19490", "9.3", "Citrix NetScaler ADC and NetScaler Gateway",
  "Authentication bypass when the appliance is configured as an AAA virtual server or as a Gateway (SSL VPN, ICA Proxy, "
  "CVPN or RDP Proxy). Previdian logged 56 exploitation attempts against its honeypots since 3 September, 36 of them on "
  "8 September alone."),
 ("CVE-2025-25249", "7.3", "Fortinet FortiOS, FortiSwitchManager, FortiSASE",
  "Heap-based buffer overflow allowing a remote unauthenticated attacker to run arbitrary code or commands via crafted "
  "requests. Weaponised to deliver the PivotC2 RAT (see Threat Actor Spotlight)."),
 ("CVE-2026-59822", "8.8", "BerriAI LiteLLM (MCP Streamable HTTP endpoint)",
  "Improper authentication: an unauthenticated attacker can establish an authenticated MCP session using an arbitrary "
  "Bearer token."),
 ("CVE-2026-48710", "6.5", "Kludex Starlette",
  "HTTP request/response smuggling. An attacker can inject paths into the host part, leading to authentication bypass "
  "among other effects."),
 ("CVE-2026-85706", '<span class="mut">Not stated</span>', "GitLab",
  "Described by GitLab as a maximum-severity path traversal flaw; the company urged users on Thursday to patch their "
  "servers immediately. No numeric CVSS appeared in the reads for this one, so none is printed."),
 ("CVE-2026-81963", '<span class="mut">Not stated</span>', "Microsoft Windows Update Stack (Windows 11, Server 2025)",
  "Link-following privilege escalation to SYSTEM, shipped in the September Patch Tuesday as an exploited zero-day; "
  "reported by MSTIC. CISA added it to the KEV catalog on 8 September."),
 ("CVE-2026-85880", '<span class="mut">Not stated</span>', "Microsoft Windows ALPC (Windows 10, Server 2012&ndash;2022)",
  "Heap-based buffer overflow privilege escalation to SYSTEM, the second exploited zero-day in the September release; "
  "reported by Proofpoint. Also added to the KEV catalog on 8 September."),
 ("CVE-2026-69414", '<span class="mut">Not stated</span>', "Microsoft Defender (&ldquo;ShieldBreak&rdquo;)",
  "Patched by Microsoft, but the new &ldquo;ShieldCrash&rdquo; proof-of-concept bypasses the fix to read arbitrary files "
  "as SYSTEM on fully patched Windows 10, Windows 11 and Windows Server. No write access, per the researcher."),
]


def cverows():
    out = []
    for cve, cvss, aff, note in CVES:
        out.append("<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td></tr>" % (cve, cvss, aff, note))
    return "".join(out)


CARDS = [
 (['<span class="t hot">exploited</span>', '<span class="t new">New</span>', '<span class="t">education</span>'],
  "Hundreds of AI agents drove a PaperCut campaign that hit 395 organisations",
  "A threat actor BleepingComputer describes as likely Russian-speaking used hundreds of AI agents to develop and launch "
  "a global exploitation campaign against vulnerable PaperCut NG/MF print-management servers, reaching <b>395 "
  "organisations</b>. Arctic Wolf had previously traced the same flaw pair against education targets from K-12 schools "
  "to major universities in the U.S. and Europe."),
 (['<span class="t hot">breach</span>', '<span class="t new">New</span>', '<span class="t">identity</span>'],
  "IDScan confirms a breach behind 153 million stolen driver&rsquo;s licences",
  "The identity-verification company has confirmed that hackers accessed customer data stored in its cloud platform, "
  "days after reports linked it to a database holding more than <b>153 million driver&rsquo;s licence scans</b>."),
 (['<span class="t hot">breach</span>', '<span class="t new">New</span>', '<span class="t">healthcare</span>'],
  "AdaptHealth: 4.1 million people exposed in a July attack",
  "The home-medical-equipment provider has confirmed that <b>4.1 million people</b> had data exposed in a cyberattack "
  "that took place in July."),
 (['<span class="t">phishing</span>', '<span class="t new">New</span>', '<span class="t">supply chain</span>'],
  "Trezor: 347,000 addresses targeted after its email provider was breached",
  "Trezor says the phishing wave that followed the breach of its third-party email provider Brevo targeted "
  "<b>347,000 email addresses</b> and affected <b>2,500 users</b> who clicked an embedded malicious link."),
 (['<span class="t hot">exploited</span>', '<span class="t">ransomware</span>'],
  "Cisco Talos: three clusters, ransomware and state-sponsored, on Secure FMC",
  "Talos says two recently patched Secure Firewall Management Center vulnerabilities have been exploited by three "
  "separate threat clusters tied to ransomware and state-sponsored operations. Cisco names them <b>UAT-12197</b>, "
  "<b>UAT-11823</b> and <b>UAT-11988</b>, deploying web shells and malware post-compromise."),
 (['<span class="t">breach</span>', '<span class="t">misconfiguration</span>'],
  "Surfshark says an exposed internal test server was breached",
  "The VPN provider disclosed that attackers reached one of its internal test servers after a configuration error "
  "exposed it to the internet, affecting internal testing and proxy infrastructure."),
 (['<span class="t pro">enforcement</span>', '<span class="t new">New</span>'],
  "Conti member sentenced to four years",
  "A Ukrainian national has been sentenced to <b>four years in prison</b> for his role in Conti ransomware attacks "
  "carried out between 2021 and 2022."),
 (['<span class="t">patch quality</span>', '<span class="t">windows</span>'],
  "September&rsquo;s updates are breaking Remote Desktop and Excel",
  "Windows admins report the September 2026 security updates are causing Remote Desktop Services failures on "
  "<b>Windows Server 2019, 2022 and 2025</b>, in some cases requiring a hard reset. Separately, the "
  "<b>KB5002914</b> Office update is breaking copy-and-paste and formula dragging in Excel for some users."),
]


def cards():
    out = ['<div class="cards">']
    for tags, h, p in CARDS:
        out.append('<div class="card"><div class="tags">%s</div><h3>%s</h3><p>%s</p></div>'
                   % ("".join(tags), h, p))
    out.append('</div>')
    return "".join(out)


BODY = """@@MAST@@
@@TLDR@@
@@FRESH@@
@@NAV@@

<div class="banner">
<span class="lvl">Threat level: High</span>
<span>A <b>CVSS 10.0</b> authentication bypass in Cisco Secure Firewall Management Center is being exploited by three
post-compromise clusters linked to ransomware and state-sponsored activity &mdash; and its federal remediation deadline
falls <b>tomorrow</b>.</span>
</div>

<div class="stats">
<div class="stat"><div class="n">966</div><div class="l">Flaws in September&rsquo;s record Patch Tuesday, per BleepingComputer; SecurityWeek and Security Affairs both say 974</div></div>
<div class="stat"><div class="n">153M</div><div class="l">Driver&rsquo;s licence scans in the database linked to the IDScan breach</div></div>
<div class="stat"><div class="n">395</div><div class="l">Organisations hit in the AI-agent-driven PaperCut campaign</div></div>
<div class="stat"><div class="n">178</div><div class="l">Devices infected with the PivotC2 RAT out of 3,000+ IP addresses targeted</div></div>
</div>

<h2 class="sec">Top Story</h2>
<div class="panel">
<h3 style="margin:0 0 9px;font-size:19px">Three exploited edge-device flaws, one deadline: federal agencies must patch Cisco, Citrix and Fortinet by 12 September</h3>
<p style="margin:0 0 11px">CISA added the trio to its Known Exploited Vulnerabilities catalog on Wednesday and set a
remediation deadline of <b>12 September 2026</b> for Federal Civilian Executive Branch agencies &mdash; one day from
today. All three sit on the network perimeter, and all three are already being used.</p>
<p style="margin:0 0 11px">The most severe is <b>CVE-2026-20079</b> (CVSS <b>10.0</b>), an authentication bypass in the
web interface of Cisco Secure Firewall Management Center that lets an unauthenticated remote attacker execute script
files and take root on the underlying operating system. Cisco has updated its advisory to say it became aware of
exploitation efforts in <b>August 2026</b>, and identified three clusters of post-compromise activity on FMC instances
&mdash; <b>UAT-12197</b>, <b>UAT-11823</b> and <b>UAT-11988</b> &mdash; dropping web shells and malware.</p>
<p style="margin:0 0 11px"><b>CVE-2026-19490</b> (CVSS <b>9.3</b>) is an authentication bypass in Citrix NetScaler ADC
and NetScaler Gateway that applies when the appliance is configured as an AAA virtual server or as a Gateway. Previdian
has logged <b>56 exploitation attempts</b> against its honeypots since 3 September, <b>36 of them on 8 September</b>
alone. <b>CVE-2025-25249</b> (CVSS <b>7.3</b>) is a heap-based buffer overflow in Fortinet FortiOS, FortiSwitchManager
and FortiSASE that yields unauthenticated remote code execution.</p>
<p style="margin:0">Two of the Windows zero-days from this week&rsquo;s record Patch Tuesday were added to the same
catalog a day earlier, on <b>8 September</b>, alongside an Adobe Commerce and Magento template-engine flaw and an
N-able N-central static code injection bug.</p>
</div>

<h2 class="sec">Patch Priority</h2>
<div class="callout crit">
<h3>Patch this first &mdash; deadline tomorrow</h3>
<p style="margin:0"><b>CVE-2026-20079 &mdash; Cisco Secure Firewall Management Center (on-prem).</b> CVSS <b>10.0</b>,
unauthenticated to root, confirmed exploited by three named post-compromise clusters. The CISA KEV remediation date is
<b>12 September 2026 &mdash; 1 day left</b>. Citrix <b>CVE-2026-19490</b> and Fortinet <b>CVE-2025-25249</b> share the
same deadline. If an FMC, NetScaler or FortiGate is internet-facing and unpatched, treat it as the day&rsquo;s only
priority; hunt for web shells and rotate credentials on anything already exposed.</p>
</div>

<h2 class="sec">Threat Actor Spotlight</h2>
<div class="cards"><div class="card">
<div class="tags"><span class="t hot">financially motivated</span><span class="t">edge devices</span><span class="t">fortinet</span></div>
<h3>The PivotC2 operator &mdash; a Russian-speaking crew farming FortiGate appliances</h3>
<p>SOCRadar attributes the campaign behind <b>CVE-2025-25249</b> to a <b>Russian-speaking threat actor driven by
financial gain</b>, with the earliest evidence of exploitation dating to <b>July 2026</b>. More than <b>3,000 IP
addresses</b> are estimated to have been targeted, resulting in <b>178 devices</b> infected with a Node.js remote access
trojan codenamed <b>PivotC2</b> &mdash; the majority of compromises concentrated in the United States.<br><br>
The chain starts with a shell script carrying an exploit binary against a vulnerable FortiGate instance, which
establishes a reverse shell and runs a single-line JavaScript command via Node.js; that pulls a second-stage payload
which is decrypted and executed. PivotC2 then holds a persistent outbound TLS connection to its command-and-control
server and offers interactive shells, file transfers, SOCKS5 and HTTP proxy tunnelling, local and remote port
forwarding, CIDR-range scanning, and FortiGate-specific configuration harvesting and credential decryption. An
<b>auto-mode flag</b> runs a predefined command sequence autonomously on initial infection.</p>
</div></div>

<h2 class="sec">Breaches &amp; Incidents</h2>
@@CARDS@@

<h2 class="sec">Vulnerability Watch</h2>
<div class="panel" style="padding:6px 10px">
<table><thead><tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr></thead>
<tbody>@@CVES@@</tbody></table>
</div>
<p class="note">CVSS values are taken from the vendor or CISA listing wherever one was published. Where no numeric score
appeared in the sources read for this edition, the cell says so rather than carrying a figure from elsewhere.</p>

<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>
<div class="panel">
<ul class="bul">
<li><b>12 September 2026 &mdash; <span style="color:var(--crit)">1 day left</span>.</b>
<b>CVE-2026-20079</b> (Cisco Secure Firewall Management Center), <b>CVE-2026-19490</b> (Citrix NetScaler ADC and
Gateway) and <b>CVE-2025-25249</b> (Fortinet FortiOS, FortiSwitchManager, FortiSASE). Added Wednesday; all three
confirmed exploited.</li>
<li><b>16 September 2026 &mdash; 5 days left.</b> <b>CVE-2026-48710</b> (Kludex Starlette, CVSS 6.5) and
<b>CVE-2026-59822</b> (BerriAI LiteLLM, CVSS 8.8), both from the 2 September batch.</li>
<li><b>5 September 2026 &mdash; <span style="color:var(--crit)">overdue by 6 days</span>.</b> The rest of the
2 September batch: <b>CVE-2026-83548</b> and <b>CVE-2026-83549</b> (SonicWall SMA 1000), <b>CVE-2026-9586</b>,
<b>CVE-2026-82329</b> and <b>CVE-2026-49869</b> (Kestra).</li>
<li><b>Added 8 September 2026, no due date read this run.</b> <b>CVE-2026-75650</b> (Adobe Commerce and Magento,
template-engine injection), <b>CVE-2026-81963</b> and <b>CVE-2026-85880</b> (the two exploited Windows zero-days) and
<b>CVE-2026-86218</b> (N-able N-central, static code injection). No remediation date appeared in the sources read for
this edition, so none is asserted here.</li>
<li><span class="mut">Deadlines are assigned per CVE under <b>BOD 26-04</b>, which prioritises remediation by risk. Two
vulnerabilities added in the same week can carry very different clocks &mdash; the 12 and 16 September dates above are
four days apart for batches added a week apart.</span></li>
</ul>
</div>

<h2 class="sec">Also Moving</h2>
<div class="panel">
<ul class="bul">
<li><b>A Defender zero-day dropped the day Patch Tuesday shipped.</b> The anonymous researcher known as <b>Nightmare
Eclipse</b> released <b>ShieldCrash</b>, a bypass for the ShieldBreak privilege-escalation flaw
(<b>CVE-2026-69414</b>) that Microsoft had just patched. The proof-of-concept demonstrates an arbitrary file read as
SYSTEM on fully patched Windows 10, Windows 11 and Windows Server; the researcher says it does not grant write access.
ShieldBreak itself bypassed RoguePlanet, disclosed in June and patched in July.</li>
<li><b>GitLab is urging immediate patching</b> of <b>CVE-2026-85706</b>, which it classes as a maximum-severity path
traversal flaw.</li>
<li><b>More than 36,000 exposed Plex servers</b> remain unpatched against recently disclosed flaws.</li>
<li><b>CISA has confirmed ransomware crews are now exploiting</b> a critical WatchGuard Firebox firewall vulnerability
it first flagged as actively exploited in December.</li>
<li><b>A new exploit kit called BlueMoon</b> was deployed by multiple cyber-espionage groups, leveraging zero-days in
both Microsoft Windows and Google Chrome.</li>
<li><b>N-able has issued a fourth N-central hotfix in five weeks</b> for an unauthenticated RCE flaw, and a separate
N-central static code injection bug went into the KEV catalog on 8 September.</li>
</ul>
</div>

<h2 class="sec">What is not on this page</h2>
<div class="panel">
<p style="margin:0" class="srcs">Two items were refused this edition. The <b>Nevada statewide ransomware</b> incident
keeps surfacing in &ldquo;2026 breach&rdquo; round-ups but is an <b>August 2025</b> event, per Nevada&rsquo;s own
after-action report; it is excluded on sight. And no CVSS figure is printed for the two exploited Windows zero-days,
the GitLab flaw or the Defender bug, because none of the sources read this edition states one &mdash; the cells say
&ldquo;Not stated&rdquo; instead of importing a number from a secondary blog.</p>
</div>

<h2 class="sec">Sources</h2>
<div class="panel"><div class="srcs">@@SRC@@</div></div>

<p class="disc">The Cyber Wire is assembled from public reporting and vendor advisories and is intended as a briefing,
not as security advice for any specific environment. Severity scores, affected-version lists and remediation deadlines
should be confirmed against the vendor bulletin or the CISA catalog before you act on them.</p>
"""

body = (BODY.replace("@@MAST@@", masthead("The Cyber Wire", "Breaches, exploited vulnerabilities and federal deadlines &mdash; refreshed through the day"))
            .replace("@@TLDR@@", tldr("The Wire", S_CY))
            .replace("@@FRESH@@", FRESH)
            .replace("@@NAV@@", nav("cyber"))
            .replace("@@CARDS@@", cards())
            .replace("@@CVES@@", cverows())
            .replace("@@SRC@@", srcblock(SRC)))

html = page("The Cyber Wire &mdash; Daily Briefings", CSS, body)
io.open(os.path.join(OUT, "cyber-briefing.html"), "w", encoding="utf-8").write(html)
print("cyber ok", len(html))
