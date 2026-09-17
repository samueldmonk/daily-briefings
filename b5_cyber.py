# -*- coding: utf-8 -*-
import io, os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.date(2026, 9, 17)

def countdown(y, m, d):
    due = datetime.date(y, m, d)
    n = (due - TODAY).days
    if n > 1:
        return '<span class="mut">(%d days left)</span>' % n, due
    if n == 1:
        return '<span class="mut">(1 day left)</span>', due
    if n == 0:
        return '<span style="color:var(--crit)">(0 days left &mdash; today)</span>', due
    return '<span style="color:var(--crit)">(overdue by %d days)</span>', due

def cd(y, m, d):
    due = datetime.date(y, m, d)
    n = (due - TODAY).days
    label = due.strftime("%-d %B %Y") if hasattr(due, "strftime") else str(due)
    if n > 1:
        tag = '<span class="mut">(%d days left)</span>' % n
    elif n == 1:
        tag = '<span class="mut">(1 day left)</span>'
    elif n == 0:
        tag = '<span style="color:var(--crit)">(0 days left &mdash; due today)</span>'
    else:
        tag = '<span style="color:var(--crit)">(overdue by %d days)</span>' % (-n)
    return label, tag

D_CISCO_EMAIL = cd(2026, 9, 17)
D_SCREEN      = cd(2026, 9, 14)
D_ISE         = cd(2026, 9, 19)
D_ACRONIS     = cd(2026, 9, 19)
D_VCENTER     = cd(2026, 8, 21)
SAT19 = datetime.date(2026, 9, 19).strftime("%A")

EXTRA = """
.banner .lvl{border-color:var(--crit);color:var(--crit)}
"""
CSS = css("#22d3a8", "#36c6ff", "#080b0b", "#111716", "#1e2a27", EXTRA)

TLDR = ("CISA says ransomware crews have now joined the attacks on a critical VMware vCenter flaw, "
        "while the federal remediation deadline for an actively exploited Cisco email-gateway zero-day "
        "that hands an attacker root expires today.")

BODY = """@@MAST@@
<div class="tldr"><b>The Wire</b> <span>@@TLDR@@</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
@@NAV@@

<div class="banner">
<span class="lvl">Threat level: High</span>
<span style="font-size:14px">Two separate CVSS 9.8 flaws are under active attack at once &mdash; one with a federal patch deadline expiring today, the other now being used by ransomware crews.</span>
</div>

<div class="stats">
<div class="stat"><div class="n">9.8</div><div class="l">CVSS of the Cisco Secure Email Gateway zero-day whose federal deadline is <strong>today</strong></div></div>
<div class="stat"><div class="n">153M+</div><div class="l">Driver's licence scans advertised on a dark-web marketplace after the IDScan.net intrusion</div></div>
<div class="stat"><div class="n">450+</div><div class="l">VMware vCenter servers exposed online, per Shadowserver, as ransomware joins the vCenter attacks</div></div>
<div class="stat"><div class="n">110</div><div class="l">Vulnerabilities fixed in Google's September Pixel patches, one an exploited zero-day</div></div>
</div>

<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 9px;font-size:21px">Ransomware gangs have joined the attacks on VMware vCenter</h3>
<p style="margin:0 0 10px">CISA has updated its Known Exploited Vulnerabilities entry for <strong>CVE-2026-59310</strong> to flag the flaw as actively abused in <strong>ransomware campaigns</strong> &mdash; a confirmation dated <strong>15 September 2026</strong>. The bug is a <strong>critical directory-traversal flaw in the VMware vCenter Server Syslog service</strong>, carrying a <strong>CVSS of 9.8</strong>, that lets an unauthenticated attacker with network access execute arbitrary code on the affected server.</p>
<p style="margin:0 0 10px">The escalation follows two earlier waves: exploitation by a suspected <strong>China-nexus actor</strong> deploying reverse SSH tooling for persistent access, and a separate campaign linked to <strong>Babuk-derived ransomware</strong> deployed on ESXi hosts. vCenter is a management plane &mdash; an attacker who owns it owns the hypervisors underneath it, which is precisely why ransomware operators find it worth the effort.</p>
<p style="margin:0 0 10px"><strong>Broadcom released fixes on 29 July 2026</strong>, and the vulnerability was added to the KEV catalog on <strong>18 August</strong>. Seven weeks after the fix shipped, <strong>Shadowserver still reports more than 450 vCenter servers exposed online</strong>; no data is published on how many of those are patched against this specific flaw. If you run vCenter and have not confirmed the July fix is applied, that is the job for this afternoon.</p>
<p style="margin:0" class="note">One caution on the deadline: the reporting this run states a remediation date of <strong>21 August 2026</strong> under <strong>BOD 26-04</strong> &mdash; three days from the KEV listing rather than the standard three-week window. That is a secondary characterisation, so it is attributed rather than asserted. Either way the date is long past; what is new today is the ransomware flag, not the clock.</p>
</div>

<h2 class="sec">Patch Priority</h2>
<div class="callout crit">
<h3>Do this first &mdash; deadline expires today</h3>
<p style="margin:0 0 8px"><strong>CVE-2026-76461 &mdash; Cisco Secure Email Gateway.</strong> A <strong>CVSS 9.8</strong> zero-day in the email-parsing logic of <strong>Cisco AsyncOS</strong>: insufficient validation lets a specially crafted email carry SQL statements that the gateway processes, ending in arbitrary command execution <strong>as root</strong>, unauthenticated. An attacker needs only to send mail to a vulnerable device. Cisco PSIRT confirmed attacks in the wild in September.</p>
<p style="margin:0 0 8px"><strong>Affected:</strong> AsyncOS <strong>16.5, 16.0, and 15.5 and earlier</strong>, on on-premises physical and virtual Secure Email Gateway appliances. <strong>Fixed releases:</strong> <strong>15.5.5-014</strong>, <strong>16.0.4-302</strong>, or <strong>16.5.0-780</strong> (Cisco prefers the last).</p>
<p style="margin:0"><strong>Federal deadline: @@D_CISCO_EMAIL_L@@ @@D_CISCO_EMAIL_T@@.</strong> This is the same date carried in the KEV section below.</p>
</div>

<h2 class="sec">Threat Actor Spotlight</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t hot">State-linked</span><span class="t">Iran</span></div>
<h3>CHOSEN BRICK and the targeting of dissidents</h3>
<p>Government agencies have warned that <strong>Iranian state-linked hackers</strong> are using a Windows malware strain named <strong>CHOSEN BRICK</strong> to target <strong>dissidents, activists and journalists worldwide</strong>. This is surveillance tooling aimed at people rather than balance sheets, and it belongs in an enterprise briefing because the same operators reuse infrastructure and initial-access tradecraft against commercial targets.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Banking crime</span><span class="t">Browser</span></div>
<h3>KREMLIN: credential theft through browser extensions</h3>
<p>A banking-malware operation active since <strong>mid-2025</strong> has been using a toolkit named <strong>KREMLIN</strong> to install malicious <strong>Chrome and Edge extensions</strong> that steal credentials, session tokens and other sensitive data. Session tokens are the part that matters: they sidestep multi-factor authentication entirely, so extension inventory and enterprise extension allow-listing are the controls that actually bite here.</p>
</div>
</div>

<h2 class="sec">Breaches &amp; Incidents</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t hot">Identity</span><span class="t">153M+</span></div>
<h3>IDScan.net confirms the driver's-licence breach</h3>
<p>The Louisiana-based identity-verification firm, whose technology underpins age and ID checks for retailers, bars and Fortune 500 clients, has <strong>confirmed a breach</strong> after a criminal marketplace began advertising more than <strong>153 million driver's licences</strong> from the United States and Canada. The company detected unauthorised access <strong>on or around 1 September 2026</strong>. Exposed data includes full names and driver's-licence numbers alongside identity numbers from other government documents such as passports; the marketplace claimed a searchable trove of <strong>front and back images plus infrared and ultraviolet scans</strong>. It surfaced through reporting by <strong>Brian Krebs</strong>, alerted on <strong>31 August</strong> to a new identity-theft service called <strong>&ldquo;Nexus&rdquo;</strong> advertised on the Russian-language forum Exploit. IDScan says it secured its systems, engaged third-party forensics and is cooperating with federal law enforcement.</p>
</div>
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t">Insurance</span></div>
<h3>An Argentine insurer loses 3.66 million customer records</h3>
<p>A breach at an <strong>Argentine insurance company</strong> resulted in the leak of <strong>3,659,226 lines</strong> of customer information, disclosed on <strong>16 September 2026</strong>. The figure comes from a breach tracker rather than a company statement, and no attribution or ransom demand is stated, so nothing further is asserted here.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Government</span><span class="t">Japan</span></div>
<h3>Japan's Digital Agency exposes employee records</h3>
<p>Japan's <strong>Digital Agency</strong> has discovered a data breach that may have exposed around <strong>246,000 record rows</strong> containing personal information of government employees. Scope and cause beyond that are not stated in the reporting fetched this run.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Social</span><span class="t">ClickFix</span></div>
<h3>HBO Max's Reddit account hijacked to push ClickFix</h3>
<p>Attackers compromised <strong>HBO Max's official Reddit account</strong> and used it to push <strong>malicious ads</strong> that launched <strong>ClickFix</strong> attacks, infecting <strong>Windows and macOS</strong> devices with information-stealing malware. A brand's verified social account is an access path, and ClickFix works by persuading the victim to paste a command themselves &mdash; no exploit required.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Public sector</span><span class="t">Florida</span></div>
<h3>ShinyHunters claims a Florida DMV breach</h3>
<p>A data breach involving the <strong>State of Florida DMV</strong> was disclosed by <strong>ShinyHunters</strong> on <strong>16 September 2026</strong>. No record count, confirmation from the agency, or ransom figure is stated in the sources fetched this run, so none is printed.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Utility</span><span class="t">US</span></div>
<h3>CenterPoint Energy confirms customer data taken</h3>
<p><strong>CenterPoint Energy</strong> has disclosed a breach compromising some customers' personal information, after an attacker leaked data allegedly stolen from the utility. No record count and no attribution are stated.</p>
</div>
</div>

<h2 class="sec">Vulnerability Watch</h2>
<div class="panel" style="padding:4px 0">
<table>
<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>
<tr><td>CVE-2026-76460</td><td><span class="down">10.0</span></td><td>Cisco Identity Services Engine</td><td>Incorrect use of privileged APIs / inadequate authorisation checks on an API endpoint. KEV, added 16 Sep.</td></tr>
<tr><td>CVE-2026-75650</td><td><span class="down">10.0</span></td><td>Adobe Commerce</td><td>Template-engine injection, exploited in the wild.</td></tr>
<tr><td>CVE-2026-84869</td><td><span class="down">9.9</span></td><td>ConnectWise ScreenConnect</td><td>Improper privilege management / missing authorisation. Fixed in <strong>26.6.5</strong>. KEV deadline already passed.</td></tr>
<tr><td>CVE-2026-76461</td><td><span class="down">9.8</span></td><td>Cisco Secure Email Gateway (AsyncOS 16.5 / 16.0 / 15.5 and earlier)</td><td>SQL injection in email parsing &rarr; unauthenticated root RCE. Zero-day, exploited. Fixed: 15.5.5-014, 16.0.4-302, 16.5.0-780.</td></tr>
<tr><td>CVE-2026-59310</td><td><span class="down">9.8</span></td><td>VMware vCenter Server (Syslog service)</td><td>Directory traversal &rarr; unauthenticated RCE. Broadcom fixed 29 Jul. <strong>Now exploited by ransomware.</strong></td></tr>
<tr><td>CVE-2026-87886</td><td><span class="mut">not stated</span></td><td>Acronis Backup plugin for cPanel &amp; WHM / Plesk extension</td><td>Incorrect default permissions. KEV, added 16 Sep. No CVSS stated by any source fetched this run.</td></tr>
<tr><td>CVE-2026-58704</td><td><span class="mut">not stated</span></td><td>Google Pixel</td><td>Privilege escalation, exploited in targeted attacks; patched 15 Sep in a release fixing 110 Pixel flaws in total.</td></tr>
</table>
</div>
<p class="note">Scores are the vendor or CISA figure where one exists. Where a CVSS was not stated by a source fetched this run, the cell says so rather than borrowing a number from a blog.</p>

<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>
<div class="panel">
<ul class="bul">
<li><strong>CVE-2026-76461</strong> &mdash; Cisco Secure Email Gateway, CVSS 9.8. Added 14 Sep, due <strong>@@D_CISCO_EMAIL_L@@</strong> @@D_CISCO_EMAIL_T@@. This is the clock that governs today's Patch Priority.</li>
<li><strong>CVE-2026-84869</strong> &mdash; ConnectWise ScreenConnect, CVSS 9.9. Added 11 Sep, due <strong>@@D_SCREEN_L@@</strong> @@D_SCREEN_T@@.</li>
<li><strong>CVE-2026-76460</strong> &mdash; Cisco Identity Services Engine, CVSS 10.0. Added 16 Sep, due <strong>@@D_ISE_L@@</strong> @@D_ISE_T@@ &mdash; a @@SAT19@@.</li>
<li><strong>CVE-2026-87886</strong> &mdash; Acronis Backup plugin for cPanel &amp; WHM / Plesk. Added 16 Sep, due <strong>@@D_ACRONIS_L@@</strong> @@D_ACRONIS_T@@.</li>
<li><strong>CVE-2026-59310</strong> &mdash; VMware vCenter Server, CVSS 9.8. Added 18 Aug, remediation date reported as <strong>@@D_VCENTER_L@@</strong> @@D_VCENTER_T@@. Re-listed as ransomware-exploited on 15 Sep.</li>
<li>CISA's own 16 September alert is titled <em>CISA Adds Two Known Exploited Vulnerabilities to Catalog</em> and lists only the Cisco ISE and Acronis entries. One vendor headline this run bundled a <strong>Google Pixel</strong> flaw into the same batch; it is not attached to that alert on CISA's page, so it is not counted here.</li>
</ul>
</div>
<p class="note">Every countdown on this page is computed from today's date against the stated due date, not written by hand.</p>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
<a href="https://www.bleepingcomputer.com/news/security/cisa-critical-vmware-vcenter-rce-flaw-now-exploited-by-ransomware-gangs/">BleepingComputer &mdash; vCenter flaw now exploited by ransomware</a> &middot;
<a href="https://www.bleepingcomputer.com/news/security/critical-vmware-vcenter-rce-flaw-exploited-for-reverse-ssh-access/">BleepingComputer &mdash; vCenter exploited for reverse SSH access</a> &middot;
<a href="https://nflo.tech/knowledge-base/2026-08-18-cve-2026-59310-en/">nFlo on CVE-2026-59310 and its KEV date</a> &middot;
<a href="https://www.helpnetsecurity.com/2026/09/15/cve-2026-76461-cisco-email-gateway-zero-day-exploited/">Help Net Security &mdash; Cisco email gateway zero-day</a> &middot;
<a href="https://www.bleepingcomputer.com/news/security/new-cisco-secure-email-zero-day-exploited-to-execute-commands-as-root/">BleepingComputer &mdash; Cisco Secure Email zero-day</a> &middot;
<a href="https://www.rapid7.com/blog/post/etr-cve-2026-76461-critical-cisco-secure-email-gateway-vulnerability-exploited-in-the-wild/">Rapid7 on CVE-2026-76461</a> &middot;
<a href="https://securityaffairs.com/199137/hacking/cisco-warns-of-ongoing-exploitation-of-critical-email-gateway-zero-day.html">Security Affairs &mdash; ongoing exploitation</a> &middot;
<a href="https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-two-known-exploited-vulnerabilities-catalog">CISA alert, 16 September 2026</a> &middot;
<a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">CISA KEV catalog</a> &middot;
<a href="https://techcrunch.com/2026/09/10/id-verification-giant-idscan-confirms-data-breach-with-more-than-150-million-drivers-licenses-stolen/">TechCrunch on IDScan.net</a> &middot;
<a href="https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/">Krebs on Security &mdash; the &ldquo;Nexus&rdquo; service</a> &middot;
<a href="https://cyberinsider.com/idscan-confirms-breach-linked-to-massive-drivers-license-leak/">CyberInsider on the IDScan confirmation</a> &middot;
<a href="https://www.wbay.com/video/2026/09/17/data-breach-id-verification-company-may-have-exposed-millions-drivers-license-images/">WBAY, 17 September</a> &middot;
<a href="https://www.brightdefense.com/resources/recent-data-breaches/">Bright Defense breach tracker (Argentine insurer, Florida DMV)</a> &middot;
<a href="https://www.bleepingcomputer.com/news/security/">BleepingComputer security feed (HBO Max, CenterPoint, Japan Digital Agency, Pixel, CHOSEN BRICK, KREMLIN)</a> &middot;
<a href="https://www.securityweek.com/">SecurityWeek</a> &middot;
<a href="https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html">The Hacker News on recent KEV batches</a>
</div>

<div class="disc">Compiled from public reporting gathered during this run. Severity scores and remediation deadlines are the ones the vendor or CISA stated; where a figure was not stated, the page says so rather than estimating. Countdowns are computed at build time and are accurate to the day, not the hour. This is a news summary, not a substitute for your own vulnerability management process.</div>
"""

BODY = (BODY.replace("@@MAST@@", masthead("The Cyber Wire", "Your daily security briefing &mdash; breaches, exploited bugs and the deadlines that matter"))
            .replace("@@NAV@@", nav("cyber"))
            .replace("@@TLDR@@", TLDR)
            .replace("@@D_CISCO_EMAIL_L@@", D_CISCO_EMAIL[0]).replace("@@D_CISCO_EMAIL_T@@", D_CISCO_EMAIL[1])
            .replace("@@D_SCREEN_L@@", D_SCREEN[0]).replace("@@D_SCREEN_T@@", D_SCREEN[1])
            .replace("@@D_ISE_L@@", D_ISE[0]).replace("@@D_ISE_T@@", D_ISE[1])
            .replace("@@D_ACRONIS_L@@", D_ACRONIS[0]).replace("@@D_ACRONIS_T@@", D_ACRONIS[1])
            .replace("@@D_VCENTER_L@@", D_VCENTER[0]).replace("@@D_VCENTER_T@@", D_VCENTER[1])
            .replace("@@SAT19@@", SAT19))

html = page("The Cyber Wire &mdash; Daily Security Briefing", CSS, BODY)
io.open(os.path.join(OUT, "cyber-briefing.html"), "w", encoding="utf-8").write(html)
print("cyber ok", len(html))
