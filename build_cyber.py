# -*- coding: utf-8 -*-
import datetime, io, os
from common import head, masthead, nav, STAMP_JS, FOOT

OUT = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.date(2026, 9, 17)

PAL = """
:root{
  --bg:#080b0b; --panel:#111716; --line:#1e2a27;
  --accent:#22d3a8; --accent2:#36c6ff;
  --txt:#e9e6e2; --muted:#9aa0a6;
  --up:#22c55e; --down:#ef4444; --warn:#f0b429; --crit:#ef4444;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
"""

TLDR = ("Cisco shipped a firewall hardening release on 16 September carrying eight "
        "vulnerability classes up to CVSS 9.9 &mdash; two of them already exploited in the wild &mdash; "
        "while a separate Cisco email-gateway flaw hits its federal patch deadline today.")


def days_left(due):
    return (due - TODAY).days


KEV = [
    ("CVE-2026-76461", "Cisco Secure Email Gateway (AsyncOS)", datetime.date(2026, 9, 17),
     "Added 14 Sep, due 17 Sep &mdash; a three-day window under the risk-based directive. "
     "Pre-authentication SQL injection in email parsing leading to root-level command execution.", True),
    ("CVE-2026-76460", "Cisco Identity Services Engine", datetime.date(2026, 9, 19),
     "Added 16 Sep, due 19 Sep (a Saturday). CVSS 10.0 API authentication bypass; "
     "Cisco found it while working a TAC support case.", True),
    ("CVE-2026-87886", "Acronis Backup for cPanel &amp; WHM / Plesk (Linux)", datetime.date(2026, 9, 19),
     "Added 16 Sep, due 19 Sep. Insecure permissions allowing a low-privileged authenticated "
     "user to escalate without user interaction. No CVSS stated by the sources read this run.", True),
    ("CVE-2026-84869", "ConnectWise ScreenConnect", datetime.date(2026, 9, 14),
     "Due 14 Sep. Carried from this site&rsquo;s standing corrections ledger, not re-fetched this run.", False),
    ("CVE-2026-59310", "VMware vCenter Server (Syslog service)", datetime.date(2026, 8, 21),
     "Reported remediation date 21 Aug. Carried from this site&rsquo;s standing corrections ledger, "
     "not re-fetched this run; the date is attributed, not asserted.", False),
]

STATS = [
    ("9.9", "Highest CVSS in Cisco&rsquo;s 16 Sep ASA / FTD / FMC hardening release (CVE-2026-20329 and CVE-2026-20330)"),
    ("8", "CVEs in that release &mdash; one assigned per CWE grouping, not per bug"),
    ("680", "Revolut customer accounts in the breach behind a $3M ransom demand"),
    ("13", "Organisations across six countries confirmed compromised by Red Heron via Gitea"),
]

BREACHES = [
    ("Revolut: $3M demanded after five months of forged legal requests", True,
     ["Fintech", "Extortion"],
     "A threat actor using the moniker <b>IAmNotAVillain</b> publicly demanded <b>$3 million</b> from Revolut "
     "&mdash; <b>6,000 XMR</b>, worth about <b>$2.9 million</b> as of early Thursday &mdash; after siphoning data "
     "for roughly five months. The access came from an infostealer infection on a government employee&rsquo;s "
     "account, which was then used to send fraudulent legal requests to <b>Revolut Bank UAB</b>, the "
     "Lithuania-based subsidiary; obliged to answer law-enforcement requests, Revolut complied. At least "
     "<b>680 accounts</b> are affected, with passports, email addresses, phone numbers and financial information "
     "exposed. A public ransom demand is unusual and normally signals a target that has refused to engage."),
    ("Berlin: Rhysida publishes roughly 6TB after a refused demand", False,
     ["Ransomware", "Government"],
     "Berlin&rsquo;s state government is dealing with the fallout after the <b>Rhysida</b> extortion group published "
     "roughly <b>6 terabytes</b> of stolen data, reported at that volume by 11 September. The leak followed a refused "
     "demand of <b>30 bitcoin</b>, close to &euro;2 million at the time."),
    ("McKesson: attackers claim 284 million patient records", False,
     ["Healthcare", "ShinyHunters"],
     "The incident was discovered <b>25 August</b>; attackers claim <b>284 million</b> patient records including names, "
     "addresses, dates of birth and Social Security numbers. The figure is the attackers&rsquo; claim as reported, "
     "not a company-confirmed count."),
    ("Veradigm: breach traced to a third-party vendor", False,
     ["Healthcare", "Supply chain"],
     "The healthcare technology company disclosed a breach after a cybersecurity incident at one of its "
     "third-party vendors exposed patients&rsquo; personal data. No record count is stated by the sources read this run."),
]

VULNS = [
    ("CVE-2026-76461", "9.8", "Cisco Secure Email Gateway &mdash; AsyncOS",
     "Pre-auth SQL injection in email-parsing logic &rarr; arbitrary SQL and root command execution. "
     "Fixed in AsyncOS 15.5.5-014, 16.0.4-302 and 16.5.0-780; Cisco recommends 16.5.0-780. No workaround."),
    ("CVE-2026-76460", "10.0", "Cisco Identity Services Engine",
     "Inadequate authentication checks on a specific API endpoint; an unauthenticated remote attacker "
     "can reach the web management interface with a crafted request."),
    ("CVE-2026-20329", "9.9", "Cisco ASA / FTD / FMC",
     "CWE-703 &mdash; improper handling of exceptional conditions (uncaught exceptions, reachable assertions). "
     "Addressed in the 16 Sep hardening release; no workarounds."),
    ("CVE-2026-20330", "9.9", "Cisco ASA / FTD / FMC",
     "CWE-707 &mdash; structured messages or data not verified as well-formed before being read from or "
     "sent to another component."),
    ("CVE-2026-20332", "9.0", "Cisco ASA / FTD / FMC",
     "CWE-284 improper access control. Cisco&rsquo;s advisory attaches its &ldquo;actively exploited&rdquo; "
     "footnote to <b>this</b> class, covered by the FMC Static Credential and FMC Authentication Bypass advisories."),
    ("CVE-2026-60004", "9.8", "Gitea 1.17 through 1.27.0",
     "Remote code execution, patched in 1.27.1 on 27 July 2026. Weaponised within days of disclosure by Red Heron."),
    ("CVE-2026-87886", "not stated", "Acronis Backup for cPanel &amp; WHM / Plesk (Linux)",
     "Insecure permissions allowing a low-privileged authenticated attacker to elevate privileges "
     "without user interaction. No CVSS appears in the sources read this run."),
]

SOURCES = [
    ("Cisco Security Advisory &mdash; ASA / FTD / FMC Software Hardening Release, September 2026",
     "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-asaftdfmc-uvpPROhN"),
    ("Cisco &mdash; Secure Firewall Management Center Static Credential Vulnerability",
     "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-static-cred-BET3Cjh"),
    ("SOCRadar &mdash; CVE-2026-76461: Cisco Email Gateway flaw exploited",
     "https://socradar.io/blog/cve-2026-76461-cisco-email-gateway-flaw/"),
    ("Qualys ThreatPROTECT &mdash; Cisco Secure Email Gateway vulnerability exploited in attacks",
     "https://threatprotect.qualys.com/2026/09/15/cisco-secure-email-gateway-vulnerability-exploited-in-attacks-cve-2026-76461/"),
    ("Security Affairs &mdash; CISA adds Acronis Backup, Cisco ISE and Google Pixel flaws to KEV",
     "https://securityaffairs.com/199239/security/u-s-cisa-adds-acronis-backup-cisco-ise-and-google-pixel-flaws-to-its-known-exploited-vulnerabilities-catalog.html"),
    ("CISA &mdash; Adds Two Known Exploited Vulnerabilities to Catalog (16 September 2026)",
     "https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-two-known-exploited-vulnerabilities-catalog"),
    ("SecurityWeek &mdash; Revolut Data Breach: 5 Months, 680 High-Profile Accounts, $3M Ransom",
     "https://www.securityweek.com/revolut-data-breach-5-months-680-high-profile-accounts-3m-ransom/"),
    ("PYMNTS &mdash; Revolut hackers issue $3 million ransom for customer data",
     "https://www.pymnts.com/cybersecurity/2026/revolut-hackers-issue-3-million-ransom-for-customer-data"),
    ("The Irish Times &mdash; Hackers demand Revolut hand over $3m ransom amid data breach (17 Sep 2026)",
     "https://www.irishtimes.com/business/2026/09/17/hackers-demand-revolut-hand-over-3m-ransom-amid-data-breach/"),
    ("Acronis Threat Research Unit &mdash; Red Heron exploits Gitea n-day flaw, exposing new Linux rootkit",
     "https://www.acronis.com/en/tru/posts/red-heron-exploits-gitea-n-day-flaw-in-multinational-campaign-exposing-new-linux-rootkit/"),
    ("The Hacker News &mdash; Red Heron Exploits Gitea RCE to Compromise 13 Organizations Across Six Countries",
     "https://thehackernews.com/2026/09/red-heron-exploits-gitea-rce-to.html"),
    ("SecurityWeek &mdash; front page (breach and incident roundup)", "https://www.securityweek.com/"),
    ("securityonline.info &mdash; Cisco patches 18 Secure Firewall flaws",
     "https://securityonline.info/cisco-secure-firewall-vulnerabilities-september-2026/"),
]


def build():
    o = io.StringIO()
    o.write(head("The Cyber Wire &mdash; Daily Security Briefing", PAL))
    o.write(masthead("The Cyber Wire",
                     "Your daily security briefing &mdash; breaches, exploited bugs and the deadlines that matter"))
    o.write('<div class="tldr"><b>The Wire</b> <span>%s</span></div>\n' % TLDR)
    o.write('<div class="freshline" id="freshline">&nbsp;</div>\n')
    o.write(nav("cyber"))

    # Threat level banner
    o.write('<div class="banner"><span class="lvl">Threat level: High</span>'
            '<span style="flex:1;min-width:240px">A CVSS 9.8 unauthenticated root-RCE in Cisco&rsquo;s email gateway '
            'reaches its federal patch deadline <b>today</b>, and Cisco&rsquo;s firewall hardening release of '
            '16 September contains two flaws already exploited in the wild.</span></div>\n')

    # Stats
    o.write('<div class="stats">')
    for n, l in STATS:
        o.write('<div class="stat"><div class="n">%s</div><div class="l">%s</div></div>' % (n, l))
    o.write("</div>\n")

    # Top story
    o.write('<h2 class="sec">Top Story</h2>\n')
    o.write('<div class="panel">'
            '<div class="tags"><span class="t new">New</span><span class="t hot">Exploited</span>'
            '<span class="t">Network edge</span></div>'
            '<h3 style="margin:0 0 9px;font-size:20px">Cisco hardens its firewall line &mdash; and two of the flaws '
            'are already being used</h3>'
            '<p style="margin:0 0 10px">Cisco published a <b>software hardening release for Secure Firewall ASA, '
            'Threat Defense and Management Center</b> on <b>16 September 2026 at 16:00 GMT</b>, rated Critical. '
            'Rather than one CVE per bug, Cisco grouped the findings by vulnerability class and assigned a single '
            'CVE to each CWE grouping &mdash; eight in all, from <b>CVSS 9.9</b> down to 7.5. The two highest are '
            '<b>CVE-2026-20329</b> (CWE-703, improper handling of exceptional conditions) and <b>CVE-2026-20330</b> '
            '(CWE-707, structured data not verified as well-formed).</p>'
            '<p style="margin:0 0 10px">The advisory states that <b>two of the vulnerabilities are known to be '
            'actively exploited</b>, and attaches that footnote to the <b>CWE-284 improper-access-control</b> class '
            '&mdash; <b>CVE-2026-20332, CVSS 9.0</b> &mdash; pointing to the separate <i>FMC Static Credential</i> and '
            '<i>FMC Authentication Bypass</i> advisories. A search-level summary read this run instead asserted that '
            'CVE-2026-20329 and CVE-2026-20330 were the exploited pair; <b>that reading is refused</b> and the vendor '
            'advisory is followed.</p>'
            '<p style="margin:0 0 10px">There are <b>no workarounds</b>. Fixed ASA releases are 9.16.4.103, 9.18.4.94, '
            '9.20.4.49, 9.22.3.26, 9.23.1.47 and 9.24.1.26; fixed FTD/FMC releases are 7.0.10, 7.2.12, 7.4.8, 7.6.6, '
            '7.7.13, 10.0.2 and 10.1.0. Snort rules 67121&ndash;67122 are published.</p>'
            '<p style="margin:0" class="mut">One detail worth noting from the advisory&rsquo;s own Source section: the '
            'flaws were found during internal security testing &ldquo;using existing testing processes as well as '
            'frontier AI models.&rdquo;</p>'
            "</div>\n")

    # Patch priority
    d = days_left(datetime.date(2026, 9, 17))
    o.write('<div class="callout crit"><h3>Patch Priority</h3>'
            '<p style="margin:0"><b>CVE-2026-76461 &mdash; Cisco Secure Email Gateway (AsyncOS), CVSS 9.8.</b> '
            'A crafted email carrying SQL statements is enough: pre-authentication SQL injection in the email-parsing '
            'logic leads to arbitrary SQL execution and then command execution as <b>root</b> on the underlying OS. '
            'Cisco PSIRT learned of exploitation while resolving a TAC support case and disclosed on 14 September; '
            'CISA added it to KEV the same day with a remediation date of <b>17 September 2026 &mdash; that is today, '
            '%d days left</b>, and a requirement for forensic investigation. There is no workaround. Upgrade to '
            'AsyncOS <b>15.5.5-014</b>, <b>16.0.4-302</b> or <b>16.5.0-780</b>; Cisco recommends 16.5.0-780.</p>'
            "</div>\n" % d)

    # Spotlight
    o.write('<h2 class="sec">Threat Actor Spotlight</h2>\n')
    o.write('<div class="panel">'
            '<div class="tags"><span class="t hot">Espionage</span><span class="t">PRC-linked</span>'
            '<span class="t">Moderate confidence</span></div>'
            '<h3 style="margin:0 0 8px;font-size:18px">Red Heron</h3>'
            '<p style="margin:0 0 10px">A suspected PRC-linked, Chinese-speaking actor that turned a public '
            'proof-of-concept into an automated intrusion framework within days of disclosure. The target was '
            '<b>CVE-2026-60004</b>, a <b>CVSS 9.8</b> flaw in <b>Gitea</b> affecting versions 1.17 through 1.27.0 and '
            'patched in 1.27.1 on 27 July 2026. The tooling registered accounts, exploited vulnerable servers, stole '
            'repositories and removed selected traces.</p>'
            '<p style="margin:0 0 10px">Acronis&rsquo; Threat Research Unit counts <b>1,386 Gitea instances scanned '
            'across seven countries</b>, plus a separate dataset of <b>477 Taiwan-based systems</b>, and <b>13 '
            'confirmed compromises across six countries</b>: Taiwan (4), the United States (4), Canada (2), Argentina '
            '(1), Qatar (1) and Sri Lanka (1). Targets were labelled in Simplified Chinese and span defence, election, '
            'energy, aerospace, telecommunications, government, public safety and research.</p>'
            '<p style="margin:0">The intrusions ran on from source-code theft to persistent access, credential '
            'collection and lateral movement, including root on a three-node Proxmox cluster, and are linked to a '
            'newly documented Linux implant called <b>JITTERLY</b> carrying an embedded LD_PRELOAD rootkit named '
            '<b>SIXZUT</b>. Attribution is stated at <b>moderate confidence</b>.</p>'
            "</div>\n")

    # Breaches
    o.write('<h2 class="sec">Breaches &amp; Incidents</h2>\n<div class="cards">')
    for title, is_new, tags, body in BREACHES:
        t = "".join('<span class="t">%s</span>' % x for x in tags)
        if is_new:
            t = '<span class="t new">New</span>' + t
        o.write('<div class="card"><div class="tags">%s</div><h3>%s</h3><p>%s</p></div>' % (t, title, body))
    o.write("</div>\n")

    # Vulnerability watch
    o.write('<h2 class="sec">Vulnerability Watch</h2>\n<div class="panel" style="padding:6px 10px">')
    o.write("<table><tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>")
    for c, s, a, n in VULNS:
        o.write("<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td></tr>" % (c, s, a, n))
    o.write("</table></div>\n")

    # KEV
    o.write('<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>\n<div class="panel"><ul class="bul">')
    for cve, prod, due, note, fresh in KEV:
        dl = days_left(due)
        if dl <= 0:
            lab = '<span class="down"><b>%s</b></span>' % (
                "due today &mdash; 0 days left" if dl == 0 else "overdue by %d days" % abs(dl))
        else:
            lab = '<b>%d days left</b>' % dl
        o.write("<li><b>%s</b> &mdash; %s. Due <b>%s</b> (%s). %s</li>"
                % (cve, prod, due.strftime("%-d %B %Y"), lab, note))
    o.write("</ul>"
            '<p class="note">Deadlines are assigned per CVE under the risk-based directive that replaced the old flat '
            'three-week window, so a three-day window is normal and is not &ldquo;corrected&rdquo; here. '
            '<b>cisa.gov returned empty on direct fetch again this run</b>, so the catalog itself was not read; '
            'the 16 September dates come from Security Affairs&rsquo; report of the alert. One discrepancy is worth '
            'stating plainly: that report&rsquo;s headline names a <b>Google Pixel</b> flaw alongside the Cisco ISE and '
            'Acronis entries, while CISA&rsquo;s own alert for 16 September is titled as adding <b>two</b> '
            'vulnerabilities. The Pixel flaw is therefore not attached to that alert here.</p>'
            "</div>\n")

    # Sources
    o.write('<h2 class="sec">Sources</h2>\n<div class="panel srcs">')
    o.write("<br>".join('<a href="%s">%s</a>' % (u, t) for t, u in SOURCES))
    o.write("</div>\n")

    o.write('<p class="disc">The Cyber Wire is compiled from public reporting and vendor advisories gathered at the '
            'time of publication. CVSS scores are taken from the vendor or CISA in preference to secondary coverage. '
            'Nothing here is a substitute for your own vulnerability management process.</p>\n')

    o.write(FOOT % STAMP_JS)
    return o.getvalue()


if __name__ == "__main__":
    html = build()
    with open(os.path.join(OUT, "cyber-briefing.html"), "w") as f:
        f.write(html)
    print("cyber ok", len(html))
