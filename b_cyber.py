# -*- coding: utf-8 -*-
import io, os, sys
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))
TODAY = date(2026, 9, 17)

def left(due):
    d = (date(*due) - TODAY).days
    if d > 0:
        return ('%d day%s left' % (d, '' if d == 1 else 's'), False)
    if d == 0:
        return ('due today &mdash; 0 days left', True)
    return ('OVERDUE by %d day%s' % (-d, '' if -d == 1 else 's'), True)

K1, K1c = left((2026, 9, 17))   # Cisco Secure Email Gateway
K2, K2c = left((2026, 9, 14))   # ScreenConnect
K3, K3c = left((2026, 9, 19))   # Cisco ISE
K4, K4c = left((2026, 9, 19))   # Acronis
SAT19 = date(2026, 9, 19).strftime('%A')   # computed, not written

CSS = css("#22d3a8", "#36c6ff", "#0a0f0e", "#121a19", "#1e2b29")

TLDR = ("Cisco's actively exploited email-gateway flaw hits its federal patch deadline today, "
        "while a ConnectWise ScreenConnect bug is already three days overdue and Gyazo confirms "
        "the loss of 23.62 million user records.")

BODY = """@@MAST@@
<div class="tldr"><b>The Wire</b> <span>@@TLDR@@</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
@@NAV@@

<div class="banner">
<span class="lvl">Threat Level &middot; High</span>
<span>An unauthenticated, CVSS&nbsp;9.8 path to <em>root</em> on Cisco Secure Email Gateway is being exploited in the wild and its CISA deadline expires today &mdash; with a second Cisco flaw scored 10.0 and a ScreenConnect bug already past due.</span>
</div>

<div class="stats">
<div class="stat"><div class="n">9.8</div><div class="l">CVSS, Cisco Secure Email Gateway zero-day (CVE-2026-76461) &mdash; unauthenticated root RCE</div></div>
<div class="stat"><div class="n">10.0</div><div class="l">CVSS, Cisco Identity Services Engine auth bypass (CVE-2026-76460), KEV-listed 16 Sep</div></div>
<div class="stat"><div class="n">23.62M</div><div class="l">Gyazo user records exposed, plus roughly 490M image-metadata records</div></div>
<div class="stat"><div class="n">1,183</div><div class="l">New ransomware incidents in the first seven months of 2026, a 40% rise on the same period of 2025</div></div>
</div>

<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 9px;font-size:20px">A screenshot tool loses 23.62 million accounts &mdash; and half a billion image records with them</h3>
<p style="margin:0 0 10px">Helpfeel's <strong>Gyazo</strong>, the screen-capture and image-sharing service, has disclosed the loss of <strong>23.62 million user records</strong> and roughly <strong>490 million image metadata records</strong>. The intrusion is dated <strong>11 September</strong>; attackers exploited a bug in the <strong>image upload server</strong> that allowed arbitrary command execution.</p>
<p style="margin:0 0 10px">The user records include names, email addresses, password hashes, device identifiers, login sessions and some connected-account tokens. The metadata covers images <strong>mostly from January 2019 or earlier</strong> and includes the identifiers embedded in Gyazo image links &mdash; which is why viewing of certain images was <strong>temporarily disabled</strong>: the leaked data could be used to reach and view images users had shared.</p>
<p style="margin:0" class="note">Deliberately not printed here: any named threat actor, any ransom demand, and any figure for how many metadata rows map to images that are still live. No source fetched this run states them.</p>
</div>

<h2 class="sec">Patch Priority</h2>
<div class="callout crit">
<h3>Do this first</h3>
<p style="margin:0 0 9px"><strong>CVE-2026-76461 &mdash; Cisco Secure Email Gateway (AsyncOS). CVSS 9.8. CISA deadline is <em>today</em>.</strong></p>
<p style="margin:0 0 9px">The flaw is an SQL injection (CWE-89) in the <strong>email-parsing logic of Cisco AsyncOS</strong>: insufficient validation lets a <strong>crafted email carry SQL statements</strong> that the gateway executes, leading to arbitrary SQL execution and ultimately <strong>command execution as root</strong> on the underlying OS &mdash; unauthenticated, remote, and triggered by a message arriving in the normal course of business.</p>
<p style="margin:0 0 9px">Cisco disclosed it on <strong>14 September</strong> after PSIRT became aware of exploitation; CISA added it to the Known Exploited Vulnerabilities catalog the <strong>same day</strong> and set a <strong>17 September</strong> remediation date for federal civilian agencies. Affected: AsyncOS <strong>16.5, 16.0, and 15.5 and earlier</strong>. Fixed in <strong>15.5.5-014, 16.0.4-302 and 16.5.0-780</strong>; Cisco recommends migrating to 16.5.0-780 where possible.</p>
<p style="margin:0" class="note">This holds the top slot over the higher-scoring Cisco ISE bypass (10.0) purely on clock: the ISE deadline is 19 September, this one is today.</p>
</div>

<h2 class="sec">Threat Actor Spotlight</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t hot">Ransomware</span><span class="t">Manufacturing</span></div>
<h3>The Gentlemen</h3>
<p>First noticed by Black Kite in <strong>September 2025</strong>. In SecurityWeek's reporting on the manufacturing surge the group accounts for <strong>12% of this year's attacks</strong> and had claimed <strong>142 manufacturing victims by mid-2026</strong> &mdash; the percentage is quoted as that research framed it, not as a share of all ransomware everywhere. The group sits inside a broader shift: attacks on manufacturers rose <strong>40%</strong> in early 2026 as crews learned that an operational shutdown propagates through a supply chain and raises the price of saying no.</p>
</div>
<div class="card">
<div class="tags"><span class="t hot">State-linked</span><span class="t">Critical infrastructure</span></div>
<h3>IRGC Cyber-Electronic Command</h3>
<p>The State Department's Rewards for Justice programme is offering up to <strong>$10 million</strong> for information identifying or locating <strong>Amir Yaryab</strong>, head of the cyber operations division of Iran's IRGC Cyber-Electronic Command. Yaryab is said to oversee <strong>CyberAv3ngers</strong>, <strong>Dadeh Afzar Arman</strong> and <strong>Mehrsam Andisheh Saz Nik</strong>, groups tied to operations against defence, shipping, energy, telecoms and financial targets in the US, Europe and the Middle East.</p>
</div>
</div>

<h2 class="sec">Breaches &amp; Incidents</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t hot">Identity documents</span><span class="t">FBI</span></div>
<h3>IDScan.net &mdash; 153 million licence scans</h3>
<p>The ID-verification provider confirmed unauthorised access, detected on or around <strong>1 September</strong>, linked to more than <strong>153 million driver's-licence scans</strong> offered on a dark-web marketplace. Exposed data may include full names, driver's-licence numbers and numbers from other government-issued documents; the marketplace claimed ID scans of over <strong>170 million</strong> people in North America. The <strong>FBI's New Orleans field office</strong> has opened a formal inquiry.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Utilities</span><span class="t hot">Dark web</span></div>
<h3>CenterPoint Energy</h3>
<p>Data from a CenterPoint Energy breach has been posted on the dark web. No record count, no attribution and no ransom figure appeared in anything fetched this run, so none is given here.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Supply chain</span><span class="t pro">Contained</span></div>
<h3>Valve says CEVA attack did not reach customers</h3>
<p>Valve has stated that customer data was <strong>not</strong> exposed in the CEVA cyberattack &mdash; a third-party incident touching its logistics chain rather than its own systems.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Web</span><span class="t">Cloud</span></div>
<h3>Three quieter campaigns worth a config check</h3>
<p>Attackers are planting web shells through <strong>WooCommerce Wholesale Lead Capture</strong>, a premium WordPress plugin; harvesting <strong>AWS and Azure secrets</strong> from exposed <strong>Vite dev servers</strong>; and abusing a <strong>Telegram Desktop HTML export</strong> flaw to exfiltrate messages. None of the three needs a new CVE on your part &mdash; they need something turned off that should never have been on.</p>
</div>
</div>

<h2 class="sec">Vulnerability Watch</h2>
<div class="panel" style="padding:4px 0">
<table>
<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>
<tr><td><strong>CVE-2026-76461</strong></td><td class="down">9.8</td><td>Cisco Secure Email Gateway (AsyncOS 16.5, 16.0, 15.5 and earlier)</td><td>SQL injection in email parsing &rarr; arbitrary SQL &rarr; root command execution, unauthenticated. Exploited in the wild. Fixed 15.5.5-014 / 16.0.4-302 / 16.5.0-780.</td></tr>
<tr><td><strong>CVE-2026-76460</strong></td><td class="down">10.0</td><td>Cisco Identity Services Engine</td><td>Inadequate authentication checks on an API endpoint let an unauthenticated remote attacker reach the web management interface with a crafted request. KEV-listed 16 Sep.</td></tr>
<tr><td><strong>CVE-2026-84869</strong></td><td class="down">9.9</td><td>ConnectWise ScreenConnect (fixed in 26.6.5)</td><td>Improper privilege management / missing authorisation: files can be transferred to a device and executed mid-session without host confirmation. Huntress documented VBScript payloads pushed to newly connected systems; more than 1,000 exposed instances remain unpatched.</td></tr>
<tr><td><strong>CVE-2026-87886</strong></td><td class="mut">not stated this run</td><td>Acronis Backup plugin for cPanel &amp; WHM; extension for Plesk</td><td>Incorrect default permissions allowing privilege escalation. KEV-listed 16 Sep. No CVSS appeared in anything fetched this run.</td></tr>
<tr><td><strong>CVE-2026-69730</strong></td><td class="down">9.8</td><td>Windows DNS Server</td><td>Use-after-free reachable by a crafted packet from an unauthenticated remote attacker &rarr; RCE. Rated Critical in the September Patch Tuesday. The total CVE count for that release is <em>not</em> settled across sources read this run &mdash; 964, 972, 974 and 1,169 all appear &mdash; so no single figure is asserted; what they agree on is 113 critical and two zero-days already under exploitation (CVE-2026-85880 in Windows ALPC and CVE-2026-81963 in the Windows Update stack).</td></tr>
</table>
</div>
<p class="note">CVSS figures here are the vendor's or CISA's, not a blog's. Where a score was not stated by a source fetched this run, the cell says so rather than guessing.</p>

<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>
<div class="panel">
<ul class="bul">
<li><strong>CVE-2026-76461</strong> &mdash; Cisco Secure Email Gateway. Added <strong>14 September</strong>, due <strong>17 September</strong>. <span class="@@C1@@"><strong>@@K1@@</strong></span></li>
<li><strong>CVE-2026-84869</strong> &mdash; ConnectWise ScreenConnect. Added <strong>11 September</strong>, due <strong>14 September</strong>. <span class="@@C2@@"><strong>@@K2@@</strong></span></li>
<li><strong>CVE-2026-76460</strong> &mdash; Cisco Identity Services Engine. Added <strong>16 September</strong>, due <strong>19 September</strong> (a @@SAT@@). <span class="mut"><strong>@@K3@@</strong></span></li>
<li><strong>CVE-2026-87886</strong> &mdash; Acronis Backup plugin for cPanel &amp; WHM and extension for Plesk. Added <strong>16 September</strong>, due <strong>19 September</strong>. <span class="mut"><strong>@@K4@@</strong></span></li>
</ul>
<p class="note">Countdowns are computed from today's date, not written by hand, and the weekday of 19 September is derived the same way. Earlier September additions &mdash; seven on 2 September (Sangoma Switchvox, Starlette, Kestra OSS, LiteLLM, JFrog Artifactory, SonicWall SMA1000) and four on 9 September (Fortinet, Citrix NetScaler, Cisco Firewall Management Center, Chromium V8) &mdash; are past due and not counted down here. The directive cited on these entries is <strong>BOD 26-04</strong>.</p>
</div>

<h2 class="sec">What this edition would not print</h2>
<div class="panel">
<ul class="bul">
<li>No item on this page carries a <em>New</em> tag. Every story here appears in at least one earlier archived snapshot; a thirty-minute refresh that tagged them anyway would be describing the archive rather than checking it.</li>
<li>A search summary paired a Google Pixel flaw with the 16 September KEV additions. CISA's own alert for that date lists <strong>two</strong> entries &mdash; Cisco ISE and Acronis Backup &mdash; so the Pixel item is not attached to that batch here.</li>
<li>No dollar figure, victim count or attribution is given for the CenterPoint Energy posting, because none was stated.</li>
</ul>
</div>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
<a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">CISA KEV catalog</a> &middot;
<a href="https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-two-known-exploited-vulnerabilities-catalog">CISA alert, 16 Sep</a> &middot;
<a href="https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog">CISA alert, 9 Sep</a> &middot;
<a href="https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog">CISA alert, 2 Sep</a> &middot;
<a href="https://www.rapid7.com/blog/post/etr-cve-2026-76461-critical-cisco-secure-email-gateway-vulnerability-exploited-in-the-wild/">Rapid7 on CVE-2026-76461</a> &middot;
<a href="https://socprime.com/blog/cve-2026-76461-critical-cisco-secure-email-gateway-zero-day-enables-root-rce/">SOC Prime</a> &middot;
<a href="https://thehackernews.com/2026/09/cisco-secure-email-gateway-flaw.html">The Hacker News</a> &middot;
<a href="https://www.esecurityplanet.com/threats/news-cisco-secure-email-gateway-cve-2026-76461/">eSecurity Planet</a> &middot;
<a href="https://securityaffairs.com/199239/security/u-s-cisa-adds-acronis-backup-cisco-ise-and-google-pixel-flaws-to-its-known-exploited-vulnerabilities-catalog.html">Security Affairs</a> &middot;
<a href="https://www.bleepingcomputer.com/news/security/cisa-warns-of-hackers-exploiting-critical-screenconnect-flaw/">BleepingComputer on ScreenConnect</a> &middot;
<a href="https://arcticwolf.com/resources/blog-uk/cve-2026-84869-connectwise-screenconnect-client-vulnerability-critical-remote-session-file-transfer-exploitation-risk/">Arctic Wolf</a> &middot;
<a href="https://www.tenable.com/blog/microsofts-september-2026-patch-tuesday-addresses-964-cves-cve-2026-81963-cve-2026-85880">Tenable, September Patch Tuesday</a> &middot;
<a href="https://cybersecuritynews.com/idscan-confirms-data-breach/">Cyber Security News on IDScan</a> &middot;
<a href="https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/">Krebs on Security</a> &middot;
<a href="https://time.com/article/2026/09/03/fbi-probes-reported-dark-web-drivers-license-breach/">TIME</a> &middot;
<a href="https://www.securityweek.com/ransomware-attacks-on-manufacturers-surge-as-supply-chain-risk-grows/">SecurityWeek on manufacturing ransomware</a> &middot;
<a href="https://therecord.media/us-reward-amir-yaryab-iran-irgc-cyberattacks">The Record on the Yaryab reward</a> &middot;
<a href="https://www.hendryadrian.com/cybersecurity-news-daily-recap-15-sep-2026/">Daily recap, 15 Sep</a>
</div>

<div class="disc">Compiled from public reporting gathered during this run. Severity scores and fixed versions are quoted from vendor or CISA advisories where available. Nothing here is a substitute for your own vendor bulletins, and remediation deadlines apply to US federal civilian agencies under the cited directive, not to private organisations.</div>
"""

BODY = (BODY.replace("@@MAST@@", masthead("The Cyber Wire", "Your daily security briefing &mdash; breaches, exploited vulnerabilities and what to patch first"))
            .replace("@@NAV@@", nav("cyber"))
            .replace("@@TLDR@@", TLDR)
            .replace("@@K1@@", K1).replace("@@K2@@", K2).replace("@@K3@@", K3).replace("@@K4@@", K4)
            .replace("@@C1@@", "down" if K1c else "mut").replace("@@C2@@", "down" if K2c else "mut")
            .replace("@@SAT@@", SAT19))

html = page("The Cyber Wire &mdash; Daily Briefing", CSS, BODY)
io.open(os.path.join(OUT, "cyber-briefing.html"), "w", encoding="utf-8").write(html)
print("cyber ok", len(html), "| KEV:", K1, "/", K2, "/", K3, "/", K4, "| 19 Sep =", SAT19)
