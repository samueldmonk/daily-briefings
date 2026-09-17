# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))
ACC, ACC2 = "#22d3a8", "#36c6ff"
EXTRA = """
.banner .lvl{border-color:var(--crit);color:var(--crit)}
.cve td:first-child{font-family:var(--mono);font-size:12.5px;white-space:nowrap}
.cvss{font-family:var(--mono);font-size:13px}
.kevdays{font-family:var(--mono);font-size:11.5px}
.kevdays.crit{color:var(--crit)}
"""
CSS = css(ACC, ACC2, "#080c0d", "#101617", "#1e2a2b", EXTRA)

SRC = [
 ("Cybernews - Gyazo data breach exposes 23.6M user records, 490M metadata records", "https://cybernews.com/security/helpfeel-gyazo-data-breach-exposed-millions-records/"),
 ("The Hacker News - Gyazo Breach Exposes 23.62 Million User Records and 490 Million Image Metadata Records", "https://thehackernews.com/2026/09/gyazo-breach-exposes-2362-million-user.html"),
 ("DataBreaches.Net - Gyazo Breach Exposes 23.62 Million User Records and 490 Million Image Metadata Records", "https://databreaches.net/2026/09/17/gyazo-breach-exposes-23-62-million-user-records-and-490-million-image-metadata-records/"),
 ("SOC Prime - CVE-2026-76461: Critical Cisco Secure Email Gateway Zero-Day Enables Root RCE", "https://socprime.com/blog/cve-2026-76461-critical-cisco-secure-email-gateway-zero-day-enables-root-rce/"),
 ("Help Net Security - Cisco patches actively exploited email gateway zero-day (CVE-2026-76461)", "https://www.helpnetsecurity.com/2026/09/15/cve-2026-76461-cisco-email-gateway-zero-day-exploited/"),
 ("eSecurity Planet - Cisco Secure Email Gateway Zero-Day Exploited for Root Command Execution", "https://www.esecurityplanet.com/threats/news-cisco-secure-email-gateway-cve-2026-76461/"),
 ("Rapid7 - CVE-2026-76461: Critical Cisco Secure Email Gateway Vulnerability Exploited in the Wild", "https://www.rapid7.com/blog/post/etr-cve-2026-76461-critical-cisco-secure-email-gateway-vulnerability-exploited-in-the-wild/"),
 ("BleepingComputer - Cisco patches Secure Email Gateway zero-day exploited in attacks", "https://www.bleepingcomputer.com/news/security/new-cisco-secure-email-zero-day-exploited-to-execute-commands-as-root/"),
 ("The Hacker News - Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks", "https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html"),
 ("SecurityWeek - Active Exploitation Triggers Emergency Patch for Cisco ISE Zero-Day", "https://www.securityweek.com/active-exploitation-triggers-emergency-patch-for-cisco-ise-zero-day/"),
 ("The Hacker News - China-Linked Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy GRIMWEDGE", "https://thehackernews.com/2026/09/china-linked-hackers-exploit-chrome.html"),
 ("SOC Prime - Chinese Threat Actors Chain Chrome and Windows Zero-Days", "https://socprime.com/active-threats/chinese-threat-actors-chain-browser-and-windows-zero-days/"),
 ("CISA - Adds Four Known Exploited Vulnerabilities to Catalog (September 8, 2026)", "https://www.cisa.gov/news-events/alerts/2026/09/08/cisa-adds-four-known-exploited-vulnerabilities-catalog"),
 ("CISA - Adds Two Known Exploited Vulnerabilities to Catalog (September 10, 2026)", "https://www.cisa.gov/news-events/alerts/2026/09/10/cisa-adds-two-known-exploited-vulnerabilities-catalog"),
 ("CISA - Known Exploited Vulnerabilities Catalog", "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
 ("BleepingComputer via SecOpsNews - CISA: Critical VMware RCE flaw now exploited by ransomware gangs", "https://github.com/SecOpsNews/news/issues/73979"),
 ("Petri - Ransomware Operators are Exploiting a Critical VMware vCenter Flaw", "https://petri.com/vmware-vcenter-flaw-ransomware-groups/"),
 ("Bitdefender - Threat Debrief, September 2026", "https://www.bitdefender.com/en-us/blog/businessinsights/bitdefender-ransomware-threat-debrief-september-2026"),
 ("Help Net Security - Ransomware in 2026: More groups, more victims, no slowdown", "https://www.helpnetsecurity.com/2026/07/24/ransomware-attack-trends-2026-report/"),
 ("Black Kite - 2026 Ransomware Report: 7,551 Victims, Up 24.9%", "https://blackkite.com/reports/2026-ransomware-report"),
 ("Cybernews - Latest Security News", "https://cybernews.com/security/"),
 ("hendryadrian.com - Cybersecurity News Daily Recap", "https://www.hendryadrian.com/cybersecurity-news-daily-recap-15-sep-2026/"),
]

def srcblock():
    return "".join('<div style="margin-bottom:7px">%s &mdash; <a href="%s">%s</a></div>' % (t, u, u) for t, u in SRC)

TLDR = ("A Japanese screenshot service lost 23.62 million user records and 490 million image "
        "metadata entries, while two actively exploited Cisco flaws &mdash; one of them a CVSS 10.0 "
        "authentication bypass &mdash; sit on federal patch deadlines that expire today and on Saturday.")

BODY = """@@MAST@@
<div class="tldr"><b>The Wire</b> <span>@@TLDR@@</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
@@NAV@@

<div class="banner">
<span class="lvl">Threat level: High</span>
<span style="flex:1;min-width:240px;font-size:14px">Two Cisco flaws are under active exploitation at once &mdash; a CVSS 10.0 authentication bypass in Identity Services Engine and a CVSS 9.8 email-gateway zero-day that runs commands as root &mdash; and their federal remediation deadlines fall today and on Saturday the 19th.</span>
</div>

<div class="stats">
<div class="stat"><div class="n">23.62M</div><div class="l">Gyazo user records exposed, alongside 490M image metadata records (Cybernews, The Hacker News)</div></div>
<div class="stat"><div class="n">10.0</div><div class="l">CVSS for CVE-2026-76460, the Cisco ISE authentication bypass exploited in the wild</div></div>
<div class="stat"><div class="n">361</div><div class="l">Compromised IPs across 47 countries tied to the VMware vCenter flaw CVE-2026-59310</div></div>
<div class="stat"><div class="n">146</div><div class="l">Active ransomware groups counted by June 2026, after 61 new entrants in twelve months</div></div>
</div>

<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 9px;font-size:19px">A screenshot tool leaked 23.62 million accounts &mdash; and half a billion pointers to private images</h3>
<p style="margin:0 0 10px">Helpfeel, the Japanese operator of the screenshot-sharing service <b>Gyazo</b>, disclosed a breach exposing <b>23.62 million user records</b> and roughly <b>490 million image metadata records</b>. Cybernews and The Hacker News both report the intrusion dates to <b>11 September</b>, and that attackers exploited a bug in Gyazo&#39;s <b>image upload server</b> that let them execute arbitrary commands.</p>
<p style="margin:0 0 10px">The user records include <b>names, email addresses, password hashes, device IDs, login sessions and some connected-account tokens</b>. The metadata set is the more unusual half: it covers images mostly dated <b>January 2019 or earlier</b> and includes the IDs that make up Gyazo image links &mdash; which is why the company has <b>temporarily disabled viewing of certain images</b>, since that metadata could help an attacker reach pictures their owners believed were private.</p>
<p style="margin:0" class="note">Gyazo will require password changes and is advising users to change reused passwords elsewhere. Neither source fetched this run names a threat actor, states a ransom demand, or gives a figure for how many of the 490 million metadata rows map to images still hosted &mdash; so none of those is printed here.</p>
</div>

<h2 class="sec">Patch Priority</h2>
<div class="callout crit">
<h3>Today &middot; CVE-2026-76461 &middot; Cisco Secure Email Gateway</h3>
<p style="margin:0 0 9px">The single most urgent item for defenders today is <b>CVE-2026-76461</b> in <b>Cisco Secure Email Gateway</b>. CISA&#39;s remediation deadline for federal civilian agencies is <b>17 September 2026 &mdash; that is today, <span class="kevdays crit">@@D1@@</span></b>.</p>
<p style="margin:0 0 9px">Newly sourced this run: the flaw carries a <b>CVSS of 9.8</b>. It lives in the email-parsing logic of Cisco AsyncOS, where insufficient validation lets a <b>specially crafted email</b> carry SQL statements that the gateway processes &mdash; ending in arbitrary SQL execution and then operating-system command execution <b>as root</b>, with no authentication. Cisco PSIRT says it became aware of attacks exploiting the flaw in September 2026.</p>
<p style="margin:0">Affected: AsyncOS <b>16.5, 16.0, and 15.5 and earlier</b>, on on-premises physical and virtual appliances. Fixed releases: <b>15.5.5-014, 16.0.4-302, 16.5.0-780</b>. Immediately behind it sits the CVSS 10.0 Cisco ISE bypass, <b>CVE-2026-76460</b>, due <b>19 September (<span class="kevdays">@@D2@@</span>)</b>.</p>
</div>

<h2 class="sec">Threat Actor Spotlight</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t hot">Ransomware</span><span class="t">Critical infrastructure</span></div>
<h3>Medusa: 67 claimed victims, and an EDR killer in the toolkit</h3>
<p>Active since <b>mid-2022</b>, Medusa has hit hundreds of critical-infrastructure organisations and claims <b>67 victims</b> as of 2026, concentrated in <b>government, retail and manufacturing</b>. Its tradecraft leans on exploiting remote-access services and deploying <b>EDR killers</b>, and it stages <b>Rclone inside Windows Defender exclusion paths</b> so that exfiltration does not trip detection.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Espionage</span></div>
<h3>UTA0560 chained three zero-days to drop GRIMWEDGE</h3>
<p>Volexity attributes a spear-phishing campaign against multiple <b>NGOs on 1 September 2026</b> to a China-linked cluster it tracks as <b>UTA0560</b>, delivering a JavaScript backdoor called <b>GRIMWEDGE</b>. The chain runs <b>CVE-2026-85046</b> for arbitrary read/write inside the V8 sandbox, <b>CVE-2026-87491</b> to escape the browser sandbox, then <b>CVE-2026-85880</b> to inject into the Chrome process. A second cluster, <b>JungleBamboo</b>, uses SUPERSTOMP to install the LONGTALE extension.</p>
</div>
</div>

<h2 class="sec">Breaches &amp; Incidents</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t">Utilities</span></div>
<h3>CenterPoint Energy data posted to the dark web</h3>
<p>CenterPoint Energy has experienced a data breach with details posted on the dark web. Nothing fetched this run states a record count, a data type, or a claiming group, so none is given.</p>
</div>
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t">Supply chain</span></div>
<h3>Valve says Steam customer data was not exposed in the CEVA attack</h3>
<p>Valve states that customer data was <b>not</b> exposed in the CEVA cyberattack, a relief for Steam shoppers. The scope of the underlying CEVA intrusion is not stated by anything fetched this run.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Ransomware</span><span class="t hot">Exploited</span></div>
<h3>Ransomware gangs join the VMware vCenter attacks</h3>
<p>CISA warned on <b>15 September</b> that ransomware operators have joined ongoing attacks on <b>CVE-2026-59310</b>, a directory-traversal flaw in vCenter&#39;s Syslog server patched by Broadcom in <b>July</b>. A DFIR firm found <b>361 compromised IPs across 47 countries</b> tied to a suspected APT deploying reverse SSH tooling.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Web</span><span class="t">Credentials</span></div>
<h3>WordPress plugins, exposed Vite servers and Telegram Desktop</h3>
<p>Attackers targeted WooCommerce and WordPress through a third-party plugin, abused <b>exposed Vite dev servers</b> to harvest AWS and Azure secrets, and leveraged a <b>Telegram Desktop HTML-export flaw</b> to exfiltrate messages. No CVE identifiers were attached to these in anything fetched this run, so none are tabled below.</p>
</div>
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t">Policy</span></div>
<h3>Norway opens an investigation into Telenor</h3>
<p>Norway is investigating <b>Telenor</b> over an alleged role in military surveillance. No findings, charges or timeline are stated by anything fetched this run.</p>
</div>
</div>

<h2 class="sec">Vulnerability Watch</h2>
<div class="panel" style="padding:6px 10px">
<table class="cve">
<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>
<tr><td>CVE-2026-76460</td><td class="cvss">10.0</td><td>Cisco ISE and ISE&#8209;PIC</td><td>Authentication bypass from insufficient authentication control on an API endpoint; a crafted request bypasses the web management interface, <b>regardless of device configuration</b>. Cisco confirms active exploitation. Fixed in <b>3.1 P12, 3.2 P11, 3.3 P12, 3.4 P7, 3.5 P4</b>. No workaround; iACLs limit remote reachability.</td></tr>
<tr><td>CVE-2026-76461</td><td class="cvss">9.8</td><td>Cisco Secure Email Gateway (AsyncOS 16.5, 16.0, 15.5 and earlier)</td><td>Unauthenticated remote code execution <b>as root</b> triggered by a crafted email reaching the parsing logic. Fixed in <b>15.5.5-014, 16.0.4-302, 16.5.0-780</b>. KEV deadline is today.</td></tr>
<tr><td>CVE-2026-59310</td><td class="cvss">9.8</td><td>VMware vCenter (Syslog server)</td><td>Directory traversal allowing unauthenticated remote code execution. Patched by Broadcom in July; ransomware operators joined the attacks per CISA on 15 September.</td></tr>
<tr><td>CVE-2026-84869</td><td class="cvss">9.9</td><td>ConnectWise ScreenConnect</td><td>Patched in <b>26.6.5</b>. Added to KEV 11 September with a 14 September deadline that has now passed.</td></tr>
<tr><td>CVE-2026-85880</td><td class="cvss mut">not stated in sources fetched this run</td><td>Microsoft Windows (heap-based buffer overflow)</td><td>Added to KEV on 8 September; used as the final link of the GRIMWEDGE chain to inject code into the Chrome browser process.</td></tr>
<tr><td>CVE-2026-85046 / CVE-2026-87491</td><td class="cvss mut">not stated in sources fetched this run</td><td>Google Chrome</td><td>The first two links of the same chain: arbitrary read/write inside the V8 sandbox, then escape from the browser sandbox.</td></tr>
</table>
</div>
<p class="note">Two CVSS cells are deliberately empty: nothing fetched this run assigns a score to CVE-2026-85880 or to the two Chrome flaws, and a score is not inferred from severity language. The WooCommerce, Vite and Telegram Desktop issues above are described rather than tabled because no source fetched this run attaches a CVE identifier to them.</p>

<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>
<div class="panel">
<ul class="bul">
<li><b>CVE-2026-76461</b> (Cisco Secure Email Gateway) &mdash; added 14 September, due <b>17 September 2026</b> <span class="kevdays crit">(@@D1@@)</span>. This is the deadline that expires today, and it is why this CVE holds the Patch Priority slot rather than the higher-scoring ISE bypass.</li>
<li><b>CVE-2026-76460</b> (Cisco ISE / ISE-PIC, CVSS 10.0) &mdash; added <b>16 September</b>, due <b>19 September 2026</b> <span class="kevdays">(@@D2@@)</span>.</li>
<li><b>CVE-2026-84869</b> (ConnectWise ScreenConnect, CVSS 9.9) &mdash; added 11 September, due 14 September <span class="kevdays crit">(@@D3@@)</span>.</li>
<li><b>10 September additions:</b> <b>CVE-2026-67277</b> (MikroTik RouterOS, missing authentication for a critical function) and <b>CVE-2026-86060</b> (MikroTik RouterOS, improper neutralisation of argument delimiters in a command).</li>
<li><b>8 September additions:</b> <b>CVE-2026-75650</b> (Adobe Commerce and Magento), <b>CVE-2026-81963</b> (Windows link following), <b>CVE-2026-85880</b> (Windows heap-based buffer overflow) and <b>CVE-2026-86218</b> (N-able N-central static code injection).</li>
<li><b>2 September additions</b> included the SonicWall pair <b>CVE-2026-83548</b> &mdash; a pre-authentication SSRF rated a maximum <b>10.0</b> &mdash; and <b>CVE-2026-83549</b>, a command injection; chained, they reach unauthenticated remote code execution, and SonicWall confirmed real-world attacks. That deadline was 5 September and has passed.</li>
</ul>
<p class="note" style="margin-top:12px">Countdowns are computed at build time from today&#39;s date against the due dates above, not copied from a previous edition. Where a deadline has passed, the overdue count is shown rather than the item being dropped.</p>
</div>

<h2 class="sec">By the Numbers &mdash; the ransomware baseline</h2>
<div class="panel">
<ul class="bul">
<li><b>61 new ransomware groups</b> entered the market between April 2025 and March 2026 &mdash; more than one a week &mdash; taking the count of active groups to <b>146 by June 2026</b>.</li>
<li>Black Kite&#39;s 2026 report counts <b>7,551 victims, up 24.9%</b> year over year.</li>
<li>Bitdefender&#39;s September debrief records <b>August 2026</b> as the month with the highest number of active reported ransomware groups in its window, and the second-largest number of claimed victims in the past year.</li>
<li><b>Clop</b> has been exploiting <b>CVE-2026-12569</b> for unauthenticated access to Windchill servers, dropping JSP web shells to complete execution and exfiltration.</li>
</ul>
</div>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
@@SRCS@@
</div>
<p class="disc">Compiled automatically from public reporting gathered during this run; nothing was fetched first-hand. Every CVE identifier, CVSS score, fixed version and KEV deadline above traces to a source listed here or to a standing sourced correction, and cells with no sourced figure are marked as such rather than filled in. This is a summary of reporting, not a security advisory; verify against your vendor&#39;s own bulletin before acting.</p>
"""

import datetime
TODAY = datetime.date(2026, 9, 17)
def days(y, m, d):
    n = (datetime.date(y, m, d) - TODAY).days
    if n > 0:
        return "%d day%s left" % (n, "" if n == 1 else "s")
    if n == 0:
        return "0 days left"
    return "%d day%s overdue" % (-n, "" if -n == 1 else "s")

D1, D2, D3 = days(2026, 9, 17), days(2026, 9, 19), days(2026, 9, 14)

BODY = (BODY.replace("@@MAST@@", masthead("The Cyber Wire", "Breaches, exploited vulnerabilities and federal patch deadlines &mdash; refreshed every 30 minutes"))
            .replace("@@NAV@@", nav("cyber"))
            .replace("@@TLDR@@", TLDR)
            .replace("@@SRCS@@", srcblock())
            .replace("@@D1@@", D1).replace("@@D2@@", D2).replace("@@D3@@", D3))

html = page("The Cyber Wire &mdash; Daily Briefing", CSS, BODY)
io.open(os.path.join(OUT, "cyber-briefing.html"), "w", encoding="utf-8").write(html)
print("cyber ok", len(html), "|", D1, "|", D2, "|", D3)
print("TLDR::" + TLDR)
