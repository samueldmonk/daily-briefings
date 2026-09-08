# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))
ACC, ACC2 = "#22d3a8", "#36c6ff"
CSS = css(ACC, ACC2, "#0b0f0e", "#121a18", "#1e2c29")

SRC = [
 ("The Hacker News — Google releases Chrome update to patch actively exploited V8 zero-day", "https://thehackernews.com/2026/09/google-releases-chrome-update-to-patch.html"),
 ("SharkStriker — Top data breaches of September 2026 (updated daily)", "https://sharkstriker.com/blog/september-2026-data-breaches/"),
 ("CISA — Adds Seven Known Exploited Vulnerabilities to Catalog (2 Sep 2026)", "https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog"),
 ("CISA — Known Exploited Vulnerabilities Catalog", "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
 ("CISA — Adds Two Known Exploited Vulnerabilities to Catalog (31 Aug 2026)", "https://www.cisa.gov/news-events/alerts/2026/08/31/cisa-adds-two-known-exploited-vulnerabilities-catalog"),
 ("securityonline.info — Weekly CVE report: 10 exploited vulnerabilities hit CISA KEV", "https://securityonline.info/weekly-cve-report-10-exploited-vulnerabilities-hit-cisa-kev/"),
 ("securityonline.info — September 2026 SAP Security Patch Day fixes critical flaws", "https://securityonline.info/september-2026-sap-security-patch-day/"),
 ("cyberpress.org — SAP Security Patch Day fixes 19 new vulnerabilities across NetWeaver, S/4HANA and cloud products", "https://cyberpress.org/sap-security-patch-day-fixes-19-new-vulnerabilities/"),
 ("gbhackers — SAP September 2026 security update fixes 4 critical vulnerabilities and 15 other flaws", "https://gbhackers.com/sap-september-2026-security-update/"),
 ("Onapsis — SAP Security Notes: September 2026 Patch Day", "https://onapsis.com/blog/sap-security-patch-day-september-2026/"),
 ("Black Kite — 2026 Ransomware Report: 7,551 victims, up 24.9%", "https://blackkite.com/reports/2026-ransomware-report"),
 ("Industrial Cyber — Ransomware reaches elevated 'new normal' as attack volumes hold steady into 2026", "https://industrialcyber.co/reports/ransomware-reaches-elevated-new-normal-as-attack-volumes-hold-steady-into-2026-reshape-baseline-risk-expectations/"),
 ("CISA — #StopRansomware: Gunra Ransomware (AA26-222A)", "https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a"),
 ("Senserva — Patch Tuesday September 2026: date, live coverage, what to expect", "https://senserva.com/patch-tuesday-2026-09.html"),
 ("Malwarebytes — August 2026 Patch Tuesday: 421 flaws, including three zero-days", "https://www.malwarebytes.com/blog/bugs/2026/08/patch-tuesday-update-now-to-fix-421-flaws-including-three-zero-days"),
 ("UpGuard — Biggest data breaches in telecommunications (updated September 2026)", "https://www.upguard.com/blog/biggest-data-breaches-in-telecommunications"),
 ("Trinetri — Microsoft Patch Tuesday September 2026", "https://trinetriops.com/resources/patch-tuesday/september-2026"),
]

def srcblock():
    return "".join('<div style="margin-bottom:7px">%s &mdash; <a href="%s">%s</a></div>' % (t, u, u) for t, u in SRC)

BODY = """
%s
<div class="tldr"><b>The Wire</b> <span>Adobe&#39;s maximum-severity Magento flaw CVE-2026-75650 remains the day&#39;s defining incident with exploitation running since 4 September, and SAP has just patched a second CVSS 10.0 flaw of its own &mdash; while three federal remediation deadlines stay open, the nearest in six days.</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
%s

<div class="banner">
<span class="lvl">Threat Level: High</span>
<span style="font-size:14px">Two separate CVSS 10.0 flaws are in play at once &mdash; one in Adobe Commerce, confirmed exploited in the wild since 4 September; one in SAP Extended Passport Processing, patched today &mdash; with three CISA remediation deadlines still open.</span>
</div>

<div class="stats">
<div class="stat"><div class="n">10.0</div><div class="l">CVSS of CVE-2026-75650, the actively exploited Adobe Commerce / Magento flaw (Adobe APSB26-146)</div></div>
<div class="stat"><div class="n">19 + 1</div><div class="l">New SAP security notes plus one update to a previously issued note, released on today&#39;s SAP Security Patch Day</div></div>
<div class="stat"><div class="n">10</div><div class="l">CVEs under active exploitation in the most recent weekly KEV tally, including SonicWall SMA1000, JFrog Artifactory and PaperCut</div></div>
<div class="stat"><div class="n">7,551</div><div class="l">Ransomware victims counted in Black Kite&#39;s 2026 report, up 24.9%%</div></div>
</div>

<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 8px;font-size:19px">StyleSmuggler: Adobe&#39;s CVSS 10.0 Magento zero-day is patched, but patching does not clean a compromised store</h3>
<p style="margin:0 0 10px">Adobe released security patches for a maximum-severity flaw affecting Adobe Commerce and Magento Open Source that has come under active exploitation in the wild, tracked as <b>CVE-2026-75650</b> with a <b>CVSS score of 10.0</b>. The bulletin is <b>APSB26-146</b>, published 7 September with Adobe&#39;s priority rating 1. Sansec, which discovered the zero-day and named it <b>StyleSmuggler</b>, dates exploitation to <b>4 September 2026</b>.</p>
<p style="margin:0 0 10px">The mechanism is PHP code injection through Magento&#39;s template system, triggered when a &ldquo;Payment Transaction Failed Reminder&rdquo; email is generated. Sansec reproduced the full unauthenticated chain on clean Magento Open Source 2.4.7, 2.4.8 and 2.4.9; the internal reference is <b>VULN-39341</b>, and every version from 2.4.4 through 2.4.9 is affected. Fixed patch levels are <b>2.4.4-p18, 2.4.5-p17, 2.4.6-p15, 2.4.7-p10, 2.4.8-p5 and 2.4.9</b>, with the remedy for older branches shipping as a composer hotfix rather than a release. Observed payloads: a Rust-based Linux backdoor beaconing to an external server, and a PHP dropper that writes an arbitrary-PHP web shell.</p>
<p style="margin:0">The operational point worth repeating: applying the patch closes the door but does not evict anyone already inside. A storefront that was exposed on or after 4 September needs a compromise assessment, not just an update.</p>
</div>

<div class="callout crit">
<h3>Patch Priority</h3>
<p style="margin:0 0 8px"><b>CVE-2026-75650 &mdash; Adobe Commerce / Magento Open Source.</b> Maximum severity, confirmed exploited in the wild, patch available. This box is crit-rated because a CVSS 10.0 flaw is being used against internet-facing storefronts right now &mdash; <b>not</b> because of a deadline: <span class="mut">no federal remediation deadline for this CVE was confirmed in anything read this run.</span></p>
<p style="margin:0"><b>Nearest open federal deadline:</b> PaperCut NG/MF, <b>14 September</b> &mdash; <b>6 days left</b>. That is the same date used in the KEV section below.</p>
</div>

<h2 class="sec">Threat Actor Spotlight</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t hot">Ransomware</span></div>
<h3>Qilin &mdash; one in every five to six victims</h3>
<p>Ransomware-tracking research read this run puts <b>Qilin</b> alone at roughly one in every five to six victims in the dataset, having grown from <b>250 victims to 1,358</b> and operating across <b>more than 50 countries</b>. The broader pattern in the same research: threat actors are increasingly abandoning encryption-based attacks in favour of data theft and extortion-only operations, which cuts operational complexity while keeping pressure on victims through the threat of exposure.</p>
</div>
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t">Runner-up</span></div>
<h3>The Gentlemen, and a newcomer</h3>
<p><b>The Gentlemen</b>, which appeared in August 2025, expanded from <b>35 victims in the fourth quarter of 2025 to 182 in the first quarter of 2026</b> &mdash; the second most active group in the same dataset. Separately, an operation branding itself <b>Majinahanashi</b> has claimed <b>18 victims across 12 countries</b> since first activity in early July 2026, using a double-extortion model and a <code>.majin</code> encryption extension.</p>
</div>
<div class="card">
<div class="tags"><span class="t">CISA advisory</span></div>
<h3>Gunra: a RaaS that recruits its own access brokers</h3>
<p>Per CISA&#39;s <b>#StopRansomware: Gunra</b> advisory (<b>AA26-222A</b>), the FBI first observed Gunra ransomware in <b>April 2025</b>, and as of <b>January 2026</b> the group launched a formal ransomware-as-a-service affiliate programme on dark-web forums. It has commercialised further since by actively recruiting penetration testers and ethical hackers to serve as initial access brokers.</p>
</div>
</div>

<h2 class="sec">Breaches &amp; Incidents</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t">Supply chain</span></div>
<h3>Trezor: another 67,000 US customers hit through its shipping provider</h3>
<p>Trezor disclosed that a further <b>67,000 customers from the U.S.</b> were affected by a breach at its shipping provider <b>ShipMonk</b>. The exposed information includes customer names, email addresses, phone numbers, shipping addresses and order numbers, covering orders placed between <b>November 2019 and August 2021</b>.</p>
</div>
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t gold">Vendor patch</span></div>
<h3>Broadcom patches a critical VMware desktop flaw</h3>
<p>Broadcom released security updates for two flaws affecting <b>VMware Workstation and Fusion</b>, including a critical bug tracked as <b>CVE-2026-59346</b> with a <b>CVSS score of 9.3</b>. It is an integer-overflow vulnerability that a <b>local attacker with elevated privileges</b> can exploit to run arbitrary code &mdash; that privilege requirement is why this is a patch-soon item rather than an emergency.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Expanded</span><span class="t hot">Education</span></div>
<h3>The PaperCut campaign keeps running against schools</h3>
<p>The chain behind the nearest KEV deadline &mdash; <b>CVE-2026-81578</b> (authentication bypass) plus <b>CVE-2026-82078</b> (remote code execution) &mdash; has been used against targets from K-12 through major universities, most cases in the U.S. plus Denmark and Ireland, with post-exploitation using registry-hive collection tooling and Metasploit/Meterpreter Java payloads. Detection advice keys on interpreters spawned by <code>pc-app.exe</code>. PaperCut has issued emergency patches.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Sector context</span></div>
<h3>Telecoms remain the standing exposure</h3>
<p>A telecommunications breach tracker updated for September 2026 counts the <b>32 largest telecom data breaches</b> to date, with Salt Typhoon and AT&amp;T among them. Carried here as sector context, not as a new incident.</p>
</div>
</div>

<h2 class="sec">Vulnerability Watch</h2>
<div class="panel">
<table>
<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>
<tr><td>CVE-2026-75650</td><td class="down">10.0</td><td>Adobe Commerce / Magento Open Source 2.4.4&ndash;2.4.9</td><td>&ldquo;StyleSmuggler&rdquo;. Unauthenticated RCE via the template system. Exploited in the wild from 4 Sep; APSB26-146, priority rating 1.</td></tr>
<tr><td>CVE-2026-44756</td><td class="down">10.0</td><td>SAP Extended Passport Processing &mdash; KERNEL 7.22, 7.53, 7.54, 7.77, 7.89, 7.93, 8.04 and 9.16 through 9.20</td><td>Memory corruption; the most severe item on today&#39;s SAP Patch Day. SAP Note 3747649. No exploitation reported in anything read this run.</td></tr>
<tr><td>CVE-2026-83548</td><td class="down">10.0</td><td>SonicWall SMA1000 appliances</td><td>Pre-authentication SSRF. Chains with the command-injection bug CVE-2026-83549 to reach unauthenticated remote code execution. In the 2 September KEV batch.</td></tr>
<tr><td>CVE-2026-58240</td><td class="down">9.8</td><td>SAP NetWeaver Message Server</td><td>Missing authentication check. SAP Note 3759472.</td></tr>
<tr><td>CVE-2026-76969</td><td class="down">9.4</td><td>SAP Cloud Application Programming Model &mdash; library <code>sap/cds-mtxs</code>, versions up to 1.18.3, 2.7.6, 3.9.6 and 4.0.2</td><td>Credential disclosure in multitenant applications.</td></tr>
<tr><td>CVE-2026-59346</td><td class="down">9.3</td><td>VMware Workstation and Fusion</td><td>Integer overflow; arbitrary code execution by a local attacker with elevated privileges.</td></tr>
<tr><td>CVE-2026-85046</td><td class="mut">Not stated in any return read this run</td><td>Google Chrome (V8 engine)</td><td>Actively exploited zero-day; Chrome update released. Added to KEV 4 September, remediation due 18 September.</td></tr>
</table>
<p class="note">A CVSS figure is printed here only where a source read this run states it, and vendor or CISA figures are preferred over third-party summaries. A breach round-up read in an earlier edition attributed StyleSmuggler to a different identifier and a 9.8 score, contradicting both Adobe and the discoverer on identifier, score and mechanism; that attribution is refused and is used nowhere on this page.</p>
</div>

<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>
<div class="panel">
<ul class="bul">
<li><b>PaperCut NG/MF &mdash; CVE-2026-81578 and CVE-2026-82078</b>, added to KEV on <b>31 August</b>. Remediation due <b>14 September</b> &mdash; <b class="down">6 days left</b>. The nearest open deadline; PaperCut has shipped emergency patches.</li>
<li><b>The 2 September batch of seven.</b> CISA added seven vulnerabilities on evidence of active exploitation, covering <b>Sangoma Switchvox, Kludex Starlette, Kestra OSS, BerriAI LiteLLM, JFrog Artifactory and SonicWall SMA1000 appliances</b> &mdash; the SonicWall pair being CVE-2026-83548 and CVE-2026-83549. Due <b>16 September</b> &mdash; <b style="color:var(--warn)">8 days left</b>.</li>
<li><b>Google Chrome V8 &mdash; CVE-2026-85046</b>, added to KEV on <b>4 September</b>, requiring Federal Civilian Executive Branch agencies to apply patches by <b>18 September 2026</b> &mdash; <b style="color:var(--warn)">10 days left</b>.</li>
<li><b>Nothing newer surfaced.</b> No KEV addition dated after 4 September appeared in any return read this run, so no fourth countdown is published here.</li>
</ul>
<p class="note"><b>On the governing directive.</b> The shorthand that a KEV deadline falls three weeks from the add date is <b>not</b> the text of BOD 22-01 and should not be used to derive dates. <b>BOD 26-04</b> (issued 10 June 2026), &ldquo;Prioritizing Security Updates Based on Risk&rdquo;, establishes vulnerability management requirements for Federal Civilian Executive Branch agencies, with five remediation tiers and windows of 3, 14 or 60 calendar days. Every countdown above is measured from today, 8 September, to a due date stated by a source &mdash; never inferred from an interval.</p>
</div>

<h2 class="sec">Also Landing Today</h2>
<div class="panel">
<ul class="bul">
<li><b>SAP Security Patch Day, 8 September.</b> SAP released <b>19 new security notes and one update</b> to a previously issued note, spanning SAP NetWeaver, Extended Passport Processing, the Cloud Application Programming Model, S/4HANA, Integration Suite and Commerce Cloud. A second tally read this run frames the same release as four critical flaws plus fifteen others. Priority attention goes to internet-facing SAP services and NetWeaver Message Server instances.</li>
<li><b>Microsoft&#39;s September Patch Tuesday has not landed yet as this edition publishes.</b> The release is scheduled for <b>today at 10:00 AM PT / 1:00 PM ET / 6:00 PM UTC</b>. <span class="mut">Two pre-publication pages read this run give sharply different expected volumes &mdash; one says nine CVEs, another says 150 to 300 or more &mdash; so no count is printed here.</span> For scale: August 2026 delivered <b>421 vulnerabilities</b>, the highest monthly total in Microsoft&#39;s patching history, <b>42</b> of them classified critical, and included three zero-days.</li>
</ul>
</div>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
%s
</div>
<p class="disc">Compiled automatically from public reporting gathered during this run. Every figure above traces to a source listed here or to a standing sourced correction; items that could not be confirmed this run were dropped rather than carried. No source was fetched first-hand this run &mdash; everything came from search returns. CVSS scores, patch levels and remediation deadlines should be confirmed against the vendor advisory or the CISA catalogue before you act on them. This briefing is informational and is not security advice for any specific environment.</p>
""" % (masthead("The Cyber Wire", "Your daily cybersecurity briefing &mdash; breaches, exploits &amp; federal deadlines"), nav("cyber"), srcblock())

html = page("The Cyber Wire &mdash; Daily Briefings", CSS, BODY)
io.open(os.path.join(OUT, "cyber-briefing.html"), "w", encoding="utf-8").write(html)
print("cyber ok", len(html))
