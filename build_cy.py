# -*- coding: utf-8 -*-
import css as C

ACCENT, ACCENT2 = "#22d3a8", "#36c6ff"
CSS = C.base_css(ACCENT, ACCENT2, "#0a0f0e", "#111917", "#1f2c29")

TLDR = ("CISA added two more exploited flaws to the KEV catalog today, one of them an unauthenticated "
        "SQL-injection-to-RCE bug in Sangoma Switchvox carrying a three-day federal deadline of "
        "September 5 — while the MLflow credential-theft flaw added on August 19 runs out of clock today.")

SOURCES = [
    ("CISA — Known Exploited Vulnerabilities Catalog",
     "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
    ("CISA — Adds Six Known Exploited Vulnerabilities to Catalog (Aug 26, 2026)",
     "https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog"),
    ("CISA — Adds Four Known Exploited Vulnerabilities to Catalog (Aug 18, 2026)",
     "https://www.cisa.gov/news-events/alerts/2026/08/18/cisa-adds-four-known-exploited-vulnerabilities-catalog"),
    ("Horizon3.ai — CVE-2026-9586: Sangoma Switchvox RCE",
     "https://horizon3.ai/attack-research/disclosures/cve-2026-9586-sangoma-switchvox-rce/"),
    ("Rapid7 — PaperCut NG/MF Critical Zero-Day Exploited in the Wild",
     "https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/"),
    ("SecurityWeek — Microsoft Patches Exploited Entra ID Vulnerability",
     "https://www.securityweek.com/microsoft-rolls-out-22-fresh-security-patches/"),
    ("SecurityWeek — Critical VMware vCenter Vulnerability in Attackers' Crosshairs",
     "https://www.securityweek.com/critical-vmware-vcenter-vulnerability-in-attackers-crosshairs/"),
    ("HIPAA Journal — ShinyHunters Claims Theft of 284M Records from McKesson",
     "https://www.hipaajournal.com/mckesson-data-breach/"),
    ("HIPAA Journal — Boston Scientific Cyberattack Impacting Operations",
     "https://www.hipaajournal.com/boston-scientific-cyberattack/"),
    ("Cybernews — Boston Scientific confirms cyber incident knocked systems offline",
     "https://cybernews.com/news/boston-scientific-confirms-cyber-incident-knocked-systems-offline-disrupting-operations/"),
    ("The Register — Healthcare cyberattacks hit pacemakers and millions of patient records",
     "https://www.theregister.com/cyber-crime/2026/08/31/healthcare-cyberattacks-hit-pacemakers-and-millions-of-patient-records/5293537"),
    ("Senserva — Microsoft CVE List / Open Source Patch Tracker (September 2026)",
     "https://senserva.com/open-source-patch-tracker.html"),
    ("Cyber Security News — daily coverage",
     "https://cybersecuritynews.com/"),
]

STATS = [
    ("2", "New CVEs added to the CISA KEV catalog today, September 2 — due September 5 and September 16"),
    ("1,687", "CVEs confirmed exploited in the wild across ~12,000 Microsoft and CISA KEV entries tracked "
              "as of September 2 (Senserva)"),
    ("671", "Of those tracked entries rated Critical severity (Senserva, September 2)"),
    ("284M", "Patient records ShinyHunters claims to have taken from McKesson, with a ransom demand "
             "above $55 million"),
]

CVES = [
    ("CVE-2026-9586", "—", "Sangoma Switchvox",
     "Unauthenticated remote SQL injection against the backend PostgreSQL database via a single crafted "
     "request, extending to remote code execution. Added to KEV today, September 2; federal due date "
     "September 5. No CVSS was stated by any source fetched this run, so none is printed."),
    ("CVE-2026-83548", "10.0", "SonicWall SMA1000 (6210 / 7210 / 8200v)",
     "Pre-authentication SSRF in the Appliance Workplace, confirmed exploited. Advisory SNWLID-2026-0016, "
     "published September 1. Affects 12.4.3-03453 and earlier and 12.5.0-02835 and earlier; fixed in "
     "12.4.3-03526 / 12.5.0-02952 and above."),
    ("CVE-2026-83549", "7.8", "SonicWall SMA1000 AMC",
     "Authenticated OS command injection, same advisory. Distinct from the July pair (SNWLID-2026-0008, "
     "CVE-2026-15409 / 15410) — the different scores are different CVEs, not a contradiction."),
    ("CVE-2026-64849", "9.3", "MLflow, all versions before 3.15.0",
     "Unauthenticated SSRF that reaches cloud metadata endpoints and exfiltrates live AWS, GCP and Azure "
     "credentials. KEV-added August 19; federal deadline is today."),
    ("CVE-2026-21962", "10.0", "Oracle HTTP Server / WebLogic Server Proxy Plug-in",
     "Improper access control, unauthenticated over HTTP. Patched by Oracle in January 2026. KEV-added "
     "August 24 with a federal deadline of August 27 — already overdue."),
    ("CVE-2026-82078", "9.4", "PaperCut NG / PaperCut MF",
     "Unsafe dynamic class loading, per the vendor advisory of August 27; CISA's catalog entry words it as "
     "unsafe reflection. Same flaw, two descriptors — both printed."),
    ("CVE-2026-81578", "8.8", "PaperCut NG / PaperCut MF",
     "Authentication bypass, per the vendor; CISA words it as missing authentication for a critical "
     "function. PaperCut confirmed customer incidents when it published on August 27."),
    ("CVE-2026-69836", "—", "Microsoft Entra ID",
     "A zero-day exploited in attacks, permitting remote code execution, fixed among 22 security updates "
     "Microsoft rolled out. No CVSS was stated in what was fetched this run."),
    ("CVE-2026-59310", "9.8 (reported)", "VMware vCenter",
     "Directory traversal in the Syslog server leading to remote code execution, now being exploited "
     "following patching. ⚠ The 9.8 is SecurityWeek's figure and was NOT confirmed against a vendor "
     "advisory this run — this desk has been burned twice by inflated 9.8s (Citrix 9.3, Progress 9.6), "
     "so it is attributed, not adopted."),
]

KEV = [
    ("crit", "<b>CVE-2026-21962</b> — Oracle HTTP Server / WebLogic Server Proxy Plug-in, CVSS 10.0. "
             "Added August 24, due <b>August 27</b> — <b>overdue by 6 days</b>."),
    ("crit", "<b>CVE-2026-64849</b> — MLflow SSRF, CVSS 9.3. Added August 19, due <b>today, "
             "September 2</b> — <b>0 days left</b>."),
    ("warn", "<b>CVE-2026-9586</b> — Sangoma Switchvox SQL injection. Added <b>today</b>, due "
             "<b>September 5</b> — <b>3 days left</b>."),
    ("", "<b>CVE-2021-23758</b> — due <b>September 9</b> — <b>7 days left</b>. The product is still not "
         "named by anything fetched, and is printed unnamed rather than guessed."),
    ("", "<b>CVE-2026-66384</b> — due <b>September 10</b> — <b>8 days left</b>. Printed unnamed: one "
         "earlier edition recorded this as JFrog Artifactory, while a vulnerability tracker instead assigns "
         "JFrog Artifactory to CVE-2026-82329. The conflict is unresolved and is not decided here."),
    ("", "<b>CVE-2026-81578</b> — PaperCut NG/MF, due <b>September 14</b> — <b>12 days left</b>."),
    ("", "<b>CVE-2026-82078</b> — PaperCut NG/MF, due <b>September 14</b> — <b>12 days left</b>."),
    ("", "<b>CVE-2026-48710</b> — added <b>today</b>, due <b>September 16</b> — <b>14 days left</b>. "
         "CISA's entry describes an open-source component, third-party library, protocol or proprietary "
         "implementation used across different products; no specific product was named, so none is printed."),
    ("", "<b>CVE-2026-8452</b> (Citrix) — <b>no countdown is published, for the fifth consecutive run.</b> "
         "The August 26 add date and August 29 due date recorded for this CVE cannot be reconciled by "
         "anything fetched, and a deadline this desk cannot verify is one it will not print."),
]

BREACHES = [
    ("McKesson", ["ransomware", "extortion", "healthcare"], "new",
     "ShinyHunters claims to have stolen <b>284 million patient records</b> and has demanded a ransom of "
     "more than <b>$55 million</b> against a 72-hour deadline. The group used voice phishing to compromise "
     "employee Okta single sign-on accounts and then pivoted into McKesson's cloud environments; "
     "exfiltration ran August 21–25. The data is reported to include patient identifiers, Social Security "
     "numbers, diagnoses, medications and doctor-patient messages. The 284-million figure is new this run; "
     "earlier editions carried the $55.2M demand without a record count."),
    ("Boston Scientific", ["disruption", "medical devices", "unattributed"], "",
     "An <b>August 25</b> attack hit on-premises IT, disrupting manufacturing, order processing and shipping, "
     "and some cardiac monitor remote activations — pacemakers and other heart devices implanted after "
     "August 25 cannot deliver remote monitoring as intended. Cloud systems and applications are unaffected. "
     "CrowdStrike and other third parties are assisting. ⚠ <b>An attribution conflict is left open:</b> the "
     "sources fetched this run state that no cybercrime group has claimed responsibility, while an earlier "
     "edition of this page recorded a claim by a pro-Russian group calling itself \"Server Killers.\" Both "
     "are printed; neither is adopted. Boston Scientific has not said whether ransomware was involved, how "
     "access occurred, or whether data was taken."),
    ("Berlin city government", ["Rhysida", "ransomware", "government"], "",
     "Rhysida claims <b>5.79 TB</b> — contracts, emails, phone numbers, passwords and material described as "
     "classified — against a demand of 30 BTC, roughly $2.3 million. Berlin publicly refused to pay in a "
     "joint statement with Interior Senator Iris Spranger reported by Reuters on August 28, weeks before "
     "the September 20 state election; election infrastructure is said to be unaffected. Carried from an "
     "earlier edition's fetch and corroborated this run at the \"more than 5 TB\" level."),
    ("Aesto Health", ["healthcare", "disclosure", "AWS"], "",
     "<b>9,540,683 individuals</b> notified to HHS after personal and health data — Social Security numbers, "
     "driver's licences, financial accounts, medical and taxpayer identifiers — was taken from the company's "
     "AWS infrastructure. ⚠ This is a recent <b>disclosure</b>, not a new intrusion: the incident was "
     "discovered on December 18, 2025."),
    ("Nutex Health", ["ransomware claim", "SEC filing"], "",
     "An <b>8-K filed August 31, 2026</b> discloses exfiltration of patient, employee, provider, business and "
     "financial data. A ransomware gang has claimed the breach; the actor is not named by the sources "
     "fetched, and is not named here."),
]

REFUSALS = (
    "<b>Three incidents remain refused, and the reason is the same each time: they were real, but "
    "not recent.</b> No new laundered incident surfaced on the cyber side this run, but the standing "
    "refusals are republished because the defect recurs — an aggregator's \"recent breaches\" page "
    "turned into a \"today\" list by a summariser, caught three times so far. Refused on these grounds: "
    "IDMerit (a February 2026 disclosure of a November 2025 finding), Panera Bread (January 2026, and with "
    "three irreconcilable record counts), and Vanderbilt University Medical Center / Meow (a 2023 leak-site "
    "listing plus a July 2026 disclosure of a March 2026 email compromise). The countermeasure that works "
    "is not scepticism — it is dating every incident before it is allowed onto the page. The standing "
    "permanent exclusion also holds: the Nevada statewide ransomware incident is <b>August 2025</b> and is "
    "refused on sight whenever a \"biggest breaches of 2026\" listing surfaces it."
)


def build():
    p = []
    p.append(C.head("The Cyber Wire — Daily Briefings", CSS))
    p.append('<div class="masthead"><h1>&#9960; The Cyber Wire</h1>'
             '<p class="tag">Your daily cybersecurity briefing — breaches, vulnerabilities &amp; federal deadlines</p>'
             + C.meta_row() + "</div>")
    p.append('<div class="tldr"><b>The Wire</b> <span>%s</span></div>' % TLDR)
    p.append('<div class="freshline" id="freshline">&nbsp;</div>')
    p.append(C.nav("cyber"))

    p.append('<div class="banner high"><span class="k">Threat Level — High</span>'
             'Two exploited flaws entered the KEV catalog today, one of them with a three-day federal '
             'clock; a CVSS 10.0 pre-authentication SonicWall SSRF is under active exploitation with no '
             'federal deadline attached; and a CVSS 10.0 Oracle flaw is six days past its remediation '
             'date.</div>')

    p.append('<div class="stats">' + "".join(
        '<div class="stat"><div class="n">%s</div><div class="l">%s</div></div>' % s for s in STATS
    ) + "</div>")

    # TOP STORY
    p.append('<h2 class="sec">Top Story</h2>')
    p.append('<div class="panel"><h3>CISA adds two exploited flaws to KEV, and gives federal agencies '
             'three days on the Sangoma one</h3>'
             '<p>Two vulnerabilities entered the Known Exploited Vulnerabilities catalog on '
             '<b>September 2</b>. The more urgent of the two is <b>CVE-2026-9586</b>, a SQL injection '
             'in <b>Sangoma Switchvox</b> that lets an unauthenticated remote attacker run arbitrary SQL '
             'against the backend PostgreSQL database from a single crafted request — including database '
             'operations and, from there, remote code execution. Its federal remediation date is '
             '<b>September 5</b>, three days out.</p>'
             '<p>The second addition, <b>CVE-2026-48710</b>, carries a September 16 date. CISA\'s entry '
             'describes it as affecting an open-source component, third-party library, protocol or '
             'proprietary implementation that could be used across different products; no specific product '
             'is named in anything fetched, so this page names none.</p>'
             '<p>Both entries direct organisations to apply vendor mitigations in line with <b>BOD 26-04, '
             '"Prioritizing Security Updates Based on Risk."</b> That is worth recording: this desk worked '
             'from BOD 22-01\'s flat three-week window for a long time, and has watched deadlines of three '
             'days, two weeks and three weeks all appear since. The directive number now appears in CISA\'s '
             'own guidance language rather than only in third-party reporting — but no window is assumed '
             'here regardless. <b>Every deadline on this page is a per-CVE published date, never one '
             'computed from a rule.</b></p></div>')

    # PATCH PRIORITY
    p.append('<h2 class="sec">Patch Priority</h2>')
    p.append('<div class="callout crit"><div class="k">Do this first — clock expires today</div>'
             '<p><b>CVE-2026-64849 — MLflow SSRF, CVSS 9.3, all versions before 3.15.0.</b> '
             'Unauthenticated, reaches cloud metadata endpoints, and steals live AWS, GCP and Azure '
             'credentials — with confirmed downstream resource enumeration, cryptominers and attacker-created '
             'IAM users and roles. It was added to KEV on <b>August 19</b> and its federal remediation date '
             'is <b>today, September 2 — zero days left</b>. Upgrade to 3.15.0 or later and rotate any '
             'credential the instance could reach.</p>'
             '<p>Two CVSS 10.0 entries sit above it on severity and neither outranks it on urgency. The '
             '<b>SonicWall SMA1000</b> pre-authentication SSRF is '
             'CVSS 10.0 and confirmed exploited, but no federal clock has been sourced for it. The '
             '<b>Oracle CVE-2026-21962</b> is also CVSS 10.0 and its deadline has already passed — six days '
             'ago — which makes it urgent but no longer a countdown. The newest clock, Sangoma\'s '
             '<b>CVE-2026-9586</b>, runs to <b>September 5</b>. These are the same dates given in the '
             'deadlines section below.</p></div>')

    # THREAT ACTOR
    p.append('<h2 class="sec">Threat Actor Spotlight</h2>')
    p.append('<div class="card"><div class="k">ShinyHunters</div>'
             '<h4>Vishing the help desk, then walking into the cloud</h4>'
             '<p>The group\'s McKesson intrusion is a clean illustration of the pattern that has dominated '
             'this year\'s large healthcare breaches, and it never touches a vulnerability. Operators phoned '
             'employees, talked them out of their <b>Okta single sign-on</b> credentials, and used that access '
             'to pivot into cloud environments — exfiltrating over <b>August 21–25</b> before surfacing a '
             'ransom demand above <b>$55 million</b> with a 72-hour deadline, and a claim of '
             '<b>284 million patient records</b>. It is the same shape as the "Spring Ring" campaign this '
             'page profiled earlier: Teams-based voice phishing, external tenants named things like '
             '"ITProtectionDepartment," email bombing to manufacture a help-desk call, Quick Assist for the '
             'foothold, then lateral movement over WinRM. <b>The control that stops both is a help desk that '
             'will not reset an MFA factor on the strength of a phone call.</b></p></div>')

    # BREACHES
    p.append('<h2 class="sec">Breaches &amp; Incidents</h2>')
    cards = []
    for name, tags, isnew, body in BREACHES:
        t = '<span class="tag new">New</span>' if isnew == "new" else ""
        tg = "".join('<span class="tag a">%s</span>' % x for x in tags)
        cards.append('<div class="card"><h4>%s</h4>%s%s<p>%s</p></div>' % (name, t, tg, body))
    p.append('<div class="cards">' + "".join(cards) + "</div>")
    p.append('<div class="note">%s</div>' % REFUSALS)

    # VULN WATCH
    p.append('<h2 class="sec">Vulnerability Watch</h2>')
    rows = "".join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td></tr>' % c for c in CVES)
    p.append('<div class="tblwrap"><table>'
             '<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>' + rows + "</table></div>")

    # KEV
    p.append('<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>')
    lis = []
    for cls, txt in KEV:
        style = ""
        if cls == "crit":
            style = ' style="color:#ef4444"'
        elif cls == "warn":
            style = ' style="color:#f0a132"'
        lis.append("<li%s>%s</li>" % (style, txt))
    p.append('<div class="panel"><ul class="b">' + "".join(lis) + "</ul>"
             '<div class="note">Countdowns are computed from today, September 2, to each CVE\'s '
             '<em>published</em> due date. A direct fetch of the CISA KEV catalog page has returned an empty '
             'body on recent runs, so these dates come from CISA alert pages surfaced in search plus vendor '
             'security reporting that cites them; that limitation is disclosed rather than papered over. '
             'Additional context sourced this run: PaperCut published its advisory on August 27 while '
             'investigating active exploitation with confirmed customer incidents, and roughly 22,000 '
             'Microsoft Exchange servers remain exposed as an exploit has gone public.</div></div>')

    p.append(C.sources(SOURCES))
    p.append('<div class="disc">This briefing summarises publicly reported security incidents and '
             'vulnerabilities. Verify every CVE, CVSS score, fixed version and remediation deadline against '
             'the vendor advisory and the CISA KEV catalog before acting on it. Nothing here is a substitute '
             'for your own incident response process.</div></footer>')
    p.append(C.STAMP_JS)
    p.append("</div></body></html>")
    return "".join(p)


if __name__ == "__main__":
    open("cyber-briefing.html", "w").write(build())
    print("cyber ok")
