# -*- coding: utf-8 -*-
import io, os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page
from common_1635 import S_CY, tldr, FRESH, srcblock

OUT = os.path.dirname(os.path.abspath(__file__))
ACC, ACC2 = "#22d3a8", "#36c6ff"
CSS = css(ACC, ACC2, "#080c0c", "#101817", "#1d2b29")

TODAY = datetime.date(2026, 9, 11)


def days_left(y, m, d):
    n = (datetime.date(y, m, d) - TODAY).days
    if n > 1:
        return '<span class="mut">(%d days left)</span>' % n
    if n == 1:
        return '<span class="mut">(1 day left)</span>'
    if n == 0:
        return '<span style="color:var(--crit)">(due today)</span>'
    return '<span style="color:var(--crit)">(overdue by %d days)</span>' % (-n)


SRC = [
 ("BleepingComputer - GitLab urges users to patch max severity path traversal flaw",
  "https://www.bleepingcomputer.com/news/security/gitlab-urges-users-to-patch-max-severity-path-traversal-flaw/"),
 ("The Hacker News - GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure",
  "https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html"),
 ("The Hacker News - CISA Flags Exploited Cisco, Citrix, Fortinet Flaws, Sets Sept. 12 Federal Patch Deadline",
  "https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html"),
 ("CISA - Adds Four Known Exploited Vulnerabilities to Catalog (Sept. 9, 2026)",
  "https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog"),
 ("CISA - Adds Two Known Exploited Vulnerabilities to Catalog (Sept. 10, 2026)",
  "https://www.cisa.gov/news-events/alerts/2026/09/10/cisa-adds-two-known-exploited-vulnerabilities-catalog"),
 ("GBHackers - CISA Adds Exploited MikroTik RouterOS Flaws to Security Alert",
  "https://gbhackers.com/cisa-adds-exploited-mikrotik-routeros-flaws/"),
 ("MikroTik - September 2026 vulnerability advisory",
  "https://mikrotik.com/supportsec/september-2026-vulnerability/"),
 ("BleepingComputer - Veradigm warns of patient data breach after ransomware gang claims attack",
  "https://www.bleepingcomputer.com/news/security/veradigm-discloses-patient-data-breach-after-gentlemen-gang-claims-attack/"),
 ("BleepingComputer - 220 million traveler records exposed in Vietnam-linked APIS leak",
  "https://www.bleepingcomputer.com/news/security/220-million-traveler-records-exposed-in-vietnam-linked-apis-leak/"),
 ("BleepingComputer - AdaptHealth confirms 4.1 million people exposed in July cyberattack",
  "https://www.bleepingcomputer.com/news/security/adapthealth-confirms-41-million-people-exposed-in-july-cyberattack/"),
 ("BleepingComputer - IDScan confirms breach tied to 153 million stolen driver's licenses",
  "https://www.bleepingcomputer.com/news/security/idscan-confirms-breach-tied-to-153-million-stolen-drivers-licenses/"),
 ("BleepingComputer - Trezor: 347,000 users targeted in phishing attacks after Brevo breach",
  "https://www.bleepingcomputer.com/news/security/trezor-347-000-users-targeted-in-phishing-attacks-after-brevo-breach/"),
 ("BleepingComputer - AI-powered attack exploited PaperCut flaws to hack 395 organizations",
  "https://www.bleepingcomputer.com/news/security/ai-powered-attack-exploited-papercut-flaws-to-hack-395-organizations/"),
 ("BleepingComputer - Cisco FMC flaws exploited by ransomware gang, state-sponsored hackers",
  "https://www.bleepingcomputer.com/news/security/cisco-fmc-flaws-exploited-by-ransomware-gang-state-sponsored-hackers/"),
 ("BleepingComputer - Microsoft September 2026 Patch Tuesday fixes 966 flaws, 2 zero-days",
  "https://www.bleepingcomputer.com/news/microsoft/microsoft-september-2026-patch-tuesday-fixes-966-flaws-2-zero-days/"),
 ("BleepingComputer - Conti ransomware gang member sentenced to 4 years in prison",
  "https://www.bleepingcomputer.com/news/security/conti-ransomware-gang-member-sentenced-to-four-years-in-prison/"),
 ("SecurityWeek - GitLab Vulnerability Exploited One Day After Disclosure",
  "https://www.securityweek.com/gitlab-vulnerability-exploited-one-day-after-disclosure/"),
]

STATS = [
 ("10.0", "GitLab&rsquo;s own CVSS for CVE-2026-85706, an unauthenticated arbitrary file read &mdash; already drawing in-the-wild probes"),
 ("220M+", "Passenger and crew records left reachable in an exposed Advance Passenger Information System database"),
 ("3.5M", "Patient records The Gentlemen claims to hold from the Veradigm third-party breach"),
 ("1 day", "Left on the federal remediation deadline for three exploited Cisco, Citrix and Fortinet edge flaws"),
]


def stats():
    return '<div class="stats">' + "".join(
        '<div class="stat"><div class="n">%s</div><div class="l">%s</div></div>' % (n, l) for n, l in STATS) + '</div>'


BREACH = [
 (['<span class="t new">New</span>', '<span class="t hot">healthcare</span>', '<span class="t">third party</span>'],
  "Veradigm: patient data taken through a vendor&rsquo;s API credentials",
  "The Chicago-based health-tech company, formerly Allscripts, told the SEC that an attacker obtained credentials from "
  "a <b>vendor&rsquo;s environment</b> for a Veradigm API reserved for customer services, then used that access to copy "
  "patient data including <b>Social Security numbers</b> for some individuals. Clinical and medical information was not "
  "affected, and Veradigm says the credentials gave access only through that limited interface &mdash; not to its "
  "broader network, servers or databases. <b>The Gentlemen</b> ransomware group claimed the intrusion on <b>5 "
  "September</b> and alleges it holds <b>3.5 million patient records</b>, threatening to leak them today if no ransom "
  "negotiation begins."),
 (['<span class="t new">New</span>', '<span class="t hot">exposure</span>', '<span class="t">aviation</span>'],
  "220 million traveler records sat exposed in an APIS database",
  "Kinry&#363; Labs found an Elasticsearch cluster carrying an <b>Advance Passenger Information System</b> dataset on "
  "<b>3 June</b> while surveying exposed databases, and disclosed it on <b>8 September</b>. Records span "
  "<b>January 2017 to April 2026</b> and include names, dates of birth, sex, nationality, <b>passport or "
  "travel-document numbers</b>, expiry dates and issuing countries, plus flight numbers and dates, airlines, departure, "
  "destination and transit airports, seat assignments and baggage references. The IP address traces to <b>Viettel</b>, "
  "Vietnam&rsquo;s state-owned telecoms provider; two misconfigurations were involved &mdash; a direct internet-facing "
  "endpoint and a separate cloud path that accepted <b>default credentials</b>."),
 (['<span class="t hot">healthcare</span>', '<span class="t">ShinyHunters</span>'],
  "AdaptHealth: 4.1 million people exposed",
  "The home-medical-equipment provider confirmed that data on <b>4.1 million</b> people was exposed in a cyberattack "
  "discovered in <b>July</b>, attributed to the <b>ShinyHunters</b> threat group."),
 (['<span class="t hot">identity</span>'],
  "IDScan confirms a breach tied to 153 million licence scans",
  "The identity-verification company confirmed hackers reached customer data in its cloud platform, days after reports "
  "linked it to a database holding more than <b>153 million driver&rsquo;s licence scans</b>."),
 (['<span class="t">phishing</span>', '<span class="t">supply chain</span>'],
  "Trezor: 347,000 addresses targeted, 2,500 users clicked",
  "After its third-party email provider <b>Brevo</b> was breached, phishing against Trezor customers reached "
  "<b>347,000</b> email addresses, and <b>2,500</b> users clicked an embedded malicious link."),
 (['<span class="t">AI-operated</span>', '<span class="t">education</span>'],
  "PaperCut: an AI-run campaign that hit 395 organisations",
  "A threat actor, likely Russian-speaking, used <b>hundreds of AI agents</b> to develop and launch a global "
  "exploitation campaign against vulnerable PaperCut NG/MF print servers, compromising <b>395 organisations</b>."),
]


def breaches():
    out = ['<div class="cards">']
    for tags, h, p in BREACH:
        out.append('<div class="card"><div class="tags">%s</div><h3>%s</h3><p>%s</p></div>' % ("".join(tags), h, p))
    out.append('</div>')
    return "".join(out)


CVES = [
 ("CVE-2026-85706", "10.0 (GitLab)", "GitLab CE &amp; EE",
  "Path traversal in the repository commits API lets an <b>unauthenticated</b> user read arbitrary files off the "
  "server &mdash; configuration, credentials, source and CI/CD secrets. Affects 18.7 through 19.1.7, 19.2 before "
  "19.2.6 and 19.3 before 19.3.2; fixed in <b>19.1.8, 19.2.6 and 19.3.2</b>. In-the-wild probing observed from "
  "<b>06:00 UTC on 11 September</b>, a day after disclosure."),
 ("CVE-2026-20079", "10.0", "Cisco Secure Firewall Management Center",
  "Authentication bypass leading to script execution and root access. Cisco says it became aware of exploitation in "
  "<b>August 2026</b> and names three post-compromise clusters &mdash; UAT-12197, UAT-11823 and UAT-11988 &mdash; "
  "linked to ransomware and state-sponsored activity. <b>KEV due 12 September.</b>"),
 ("CVE-2026-19490", "9.3", "Citrix NetScaler ADC / Gateway",
  "Authentication bypass when the appliance is configured as an AAA virtual server or Gateway. Previdian honeypots "
  "logged <b>56 exploitation attempts since 3 September</b>, <b>36 of them on 8 September</b> alone. "
  "<b>KEV due 12 September.</b>"),
 ("CVE-2025-25249", "7.3", "Fortinet FortiOS / FortiSwitchManager / FortiSASE",
  "Heap overflow leading to unauthenticated remote code execution. Added to KEV on 9 September alongside the Cisco and "
  "Citrix flaws. <b>KEV due 12 September.</b>"),
 ("CVE-2026-67277", "Not stated", "MikroTik RouterOS",
  "Missing authentication for a critical function (<b>CWE-306</b>) in the bandwidth-test (<code>btest</code>) service, "
  "allowing kernel-memory disclosure and denial of service. Fixed 3 September in <b>6.49.21</b> and <b>7.23.4</b> "
  "(long-term) and <b>7.24.2</b> (stable). <b>KEV due 13 September.</b>"),
 ("CVE-2026-86060", "Not stated", "MikroTik RouterOS",
  "Improper neutralisation of argument delimiters (<b>CWE-88</b>) allowing manipulation of the trusted RouterOS policy "
  "mask and privilege escalation. CISA has designated it as requiring <b>forensic triage under BOD 26-04</b>. Same "
  "fixed builds. <b>KEV due 13 September.</b>"),
]


def cverows():
    return "".join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td></tr>' % c for c in CVES)


BODY = """@@MAST@@
@@TLDR@@
@@FRESH@@
@@NAV@@

<div class="banner">
<span class="lvl">Threat level: High</span>
<span>A maximum-severity GitLab file-read flaw is being probed in the wild the day after disclosure, while three
already-exploited edge-device bugs hit their federal remediation deadline tomorrow and two more follow on Sunday.</span>
</div>

@@STATS@@

<h2 class="sec">Top Story</h2>
<div class="panel">
<h3 style="margin:0 0 9px;font-size:20px">GitLab&rsquo;s CVSS 10.0 file-read bug went from advisory to in-the-wild probing in a day</h3>
<p style="margin:0 0 11px">GitLab urged users on Thursday to patch immediately against
<b>CVE-2026-85706</b>, a path traversal in the <b>repository commits API</b> of GitLab CE and EE that lets an
<b>unauthenticated</b> user read arbitrary files from the server. GitLab assigned it a CVSS of <b>10.0</b>. The root
cause is improper path confinement combined with missing authentication enforcement on the affected endpoint, which
means an attacker outside the intended repository path can pull configuration files, credentials, source code and
CI/CD secrets.</p>
<p style="margin:0 0 11px">Affected releases run from <b>18.7 through 19.1.7</b>, <b>19.2 before 19.2.6</b> and
<b>19.3 before 19.3.2</b>; the fixes are <b>19.1.8, 19.2.6 and 19.3.2</b>. Opportunistic scanning began almost
immediately &mdash; in-the-wild probes were observed from <b>06:00 UTC on 11 September</b>, one day after
disclosure.</p>
<p style="margin:0">The reason this matters more than a typical read primitive: a self-hosted GitLab instance is
usually the single richest credential store in an engineering organisation. A file read there is rarely the end of the
intrusion &mdash; it is the step that supplies the keys for the next one.</p>
</div>

<div class="callout crit">
<h3>Patch Priority</h3>
<p style="margin:0">If you run <b>Cisco Secure Firewall Management Center</b>, the maximum-severity authentication
bypass <b>CVE-2026-20079</b> carries a CISA remediation deadline of <b>12 September 2026</b> @@D12@@ &mdash; and Cisco
has confirmed exploitation dating to August by three separate clusters tied to ransomware and state-sponsored
activity. Patch it today. Immediately behind it: the Citrix NetScaler and Fortinet flaws on the same deadline, the two
MikroTik RouterOS bugs due <b>13 September</b> @@D13@@, and the GitLab upgrade above, which has no federal deadline but
is already being probed.</p>
</div>

<h2 class="sec">Threat Actor Spotlight</h2>
<div class="panel">
<div class="tags"><span class="t new">New</span><span class="t hot">ransomware</span><span class="t">double extortion</span></div>
<h3 style="margin:0 0 9px;font-size:19px">The Gentlemen</h3>
<p style="margin:0 0 11px">The group behind this week&rsquo;s Veradigm claim emerged around <b>mid-2025</b> and runs a
<b>double-extortion</b> model, pairing data theft with encryption across <b>Windows, Linux, NAS, BSD and ESXi</b>
systems. Its leak site lists more than <b>800 victims from 86 countries</b> spanning manufacturing, technology,
healthcare, transportation and financial services &mdash; a spread that reads as opportunistic targeting driven by
whatever access is available rather than by sector.</p>
<p style="margin:0">Two tooling notes from this year: in <b>April 2026</b> Check Point tied a <b>SystemBC</b> proxy
botnet of more than <b>1,500 hosts</b> to a Gentlemen affiliate, and in <b>June 2026</b> ESET reported the group using
a purpose-built EDR killer called <b>GentleKiller</b>. Defenders should assume endpoint protection is a target of the
intrusion, not a backstop against it.</p>
</div>

<h2 class="sec">Breaches &amp; Incidents</h2>
@@BREACH@@

<h2 class="sec">Vulnerability Watch</h2>
<div class="panel" style="padding:6px 10px">
<table><thead><tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr></thead>
<tbody>@@CVES@@</tbody></table>
</div>
<p class="note">Where a CVSS is shown as &ldquo;Not stated&rdquo;, no score for that CVE appeared in any source read
this run, and none is inferred. Where a vendor and a third party disagree, the vendor&rsquo;s figure is the one
printed.</p>

<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>
<div class="panel">
<ul class="bul">
<li><b>Due 12 September 2026</b> @@D12@@ &mdash; <b>CVE-2026-20079</b> (Cisco Secure Firewall Management Center),
<b>CVE-2026-19490</b> (Citrix NetScaler ADC/Gateway) and <b>CVE-2025-25249</b> (Fortinet FortiOS, FortiSwitchManager
and FortiSASE), all added on <b>9 September</b>.</li>
<li><b>Due 13 September 2026</b> @@D13@@ &mdash; <b>CVE-2026-67277</b> and <b>CVE-2026-86060</b> (MikroTik RouterOS),
added on <b>10 September</b>. CISA has flagged CVE-2026-86060 as requiring <b>forensic triage under BOD 26-04</b>.</li>
<li><b>Added 8 September, no due date published in any source read this run:</b> <b>CVE-2026-75650</b> (Adobe Commerce
/ Magento template-engine injection), <b>CVE-2026-81963</b> and <b>CVE-2026-85880</b> (the two exploited Windows
zero-days from this month&rsquo;s Patch Tuesday) and <b>CVE-2026-86218</b> (N-able N-central). The date is left blank
rather than inferred.</li>
<li><b>Earlier September batches carried forward:</b> the 2 September additions run on two separate clocks &mdash;
CVE-2026-83548, CVE-2026-83549, CVE-2026-9586, CVE-2026-82329 and CVE-2026-49869 were due <b>5 September</b>
@@D05@@, while CVE-2026-48710 and CVE-2026-59822 are due <b>16 September</b> @@D16@@.</li>
<li><b>Deadlines are assigned per CVE under BOD 26-04.</b> Two vulnerabilities added on the same day can carry very
different clocks, as the 12 and 13 September dates above show &mdash; read the catalogue entry, not a rule of
thumb.</li>
</ul>
</div>

<h2 class="sec">Also This Week</h2>
<div class="panel">
<ul class="bul">
<li><b>Patch Tuesday was the largest on record.</b> BleepingComputer counts <b>966</b> flaws and two zero-days;
SecurityWeek and Security Affairs both say <b>974</b>. The count is printed as a range because the outlets have not
reconciled.</li>
<li><b>Artifactory flaws chained to a Rust backdoor.</b> Attackers are chaining critical and high-severity JFrog
Artifactory bugs to bypass authentication, gain admin privileges and deploy a Rust backdoor on self-hosted
servers.</li>
<li><b>A Conti member got four years.</b> A Ukrainian national was sentenced for his role in Conti ransomware attacks
between 2021 and 2022.</li>
<li><b>WatchGuard Firebox is now in ransomware use.</b> CISA confirmed ransomware crews are exploiting the critical
Firebox flaw it flagged as actively exploited in December.</li>
<li><b>Housekeeping hazards:</b> September&rsquo;s Windows Server updates are breaking <b>Remote Desktop Services</b>
on Server 2019, 2022 and 2025, and the Excel <b>KB5002914</b> update is breaking copy-and-paste and formula dragging
for some users.</li>
</ul>
</div>

<h2 class="sec">Sources</h2>
<div class="panel"><div class="srcs">@@SRC@@</div></div>

<p class="disc">The Cyber Wire summarises public reporting for awareness only and is not incident-response advice.
Severity scores, affected versions and remediation deadlines should be confirmed against the vendor advisory or the
CISA catalogue entry before you act on them.</p>
"""

body = (BODY.replace("@@MAST@@", masthead("The Cyber Wire", "Breaches, exploited vulnerabilities and the federal patch clock"))
            .replace("@@TLDR@@", tldr("The Wire", S_CY))
            .replace("@@FRESH@@", FRESH)
            .replace("@@NAV@@", nav("cyber"))
            .replace("@@STATS@@", stats())
            .replace("@@BREACH@@", breaches())
            .replace("@@CVES@@", cverows())
            .replace("@@D12@@", days_left(2026, 9, 12))
            .replace("@@D13@@", days_left(2026, 9, 13))
            .replace("@@D05@@", days_left(2026, 9, 5))
            .replace("@@D16@@", days_left(2026, 9, 16))
            .replace("@@SRC@@", srcblock(SRC)))

html = page("The Cyber Wire &mdash; Daily Briefings", CSS, body)
io.open(os.path.join(OUT, "cyber-briefing.html"), "w", encoding="utf-8").write(html)
print("cy ok", len(html))
