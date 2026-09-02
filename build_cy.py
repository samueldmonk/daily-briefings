# -*- coding: utf-8 -*-
import shared, io

ACCENT = "#22d3a8"; ACCENT2 = "#36c6ff"
SUMMARY = ("Attackers are actively exploiting two chained zero-days in SonicWall SMA 1000 VPN appliances "
           "and a 9.8-rated unauthenticated root RCE in the Langflow AI framework, with federal agencies "
           "facing a CISA remediation deadline on Saturday, September 5.")

body = []
A = body.append

A('<header class="mast">')
A('<h1>&#9960; The Cyber Wire</h1>')
A('<p class="tag">Your daily cybersecurity briefing &mdash; breaches, exploited vulnerabilities &amp; federal deadlines</p>')
A(shared.META)
A('</header>')
A(f'<div class="tldr"><b>The Wire</b> <span>{SUMMARY}</span></div>')
A('<p class="freshline" id="freshline">&nbsp;</p>')
A(shared.nav("cyber", ACCENT))

# Threat level banner
A('<div class="banner">')
A('<span class="lvl">Threat level: High</span>')
A('<span class="why">Two separate unauthenticated remote-code-execution chains are under confirmed '
  'exploitation at once &mdash; SonicWall SMA 1000 (reported CVSS 10.0, no workarounds) and Langflow '
  'CVE-2026-0768 (CVSS 9.8, root) &mdash; and a CISA federal remediation deadline falls in three days.</span>')
A('</div>')

# By the numbers
A('<div class="strip">')
for n, l in [("360", "Langflow exploitation attempts logged by VulnCheck honeypots in the U.K., most traffic originating in Russia"),
             ("9.5M", "people affected by the Aesto Health breach of AWS-hosted patient data"),
             ("48%", "of all breaches now involve ransomware, though payouts are shrinking (2026 Verizon DBIR)"),
             ("31%", "of breaches now start with a software vulnerability &mdash; ahead of stolen passwords for the first time (2026 DBIR)")]:
    A(f'<div class="stat"><div class="n">{n}</div><div class="l">{l}</div></div>')
A('</div>')

# Top story
A('<h2 class="sec">Top Story</h2>')
A('<div class="lead">')
A('<h3>Hackers are draining OpenAI and AWS keys through a critical Langflow flaw &mdash; and honeypots '
  'have already logged 360 attempts</h3>')
A('<p>Threat actors are actively exploiting <b>CVE-2026-0768</b>, an unauthenticated remote-code-execution '
  'vulnerability in <b>Langflow</b>, the open-source framework for building AI applications, to steal '
  'credentials, tokens and keys. The flaw carries a <b>CVSS score of 9.8</b> and allows arbitrary code '
  'execution <b>as root, without authentication</b>.</p>')
A('<p>The defect sits in the code validator of Langflow\'s custom component editor: a user-supplied string '
  'passed to the <span class="mono">validate</span> endpoint\'s <span class="mono">code</span> parameter is '
  'not properly validated before it is used to execute Python. It affects <b>Langflow 1.4.2 and earlier</b>. '
  'It was reported through ZDI in July 2025 and publicly disclosed as a zero-day in January 2026.</p>')
A('<p>Security firm <b>VulnCheck</b> detected the attacks via honeypots in the United Kingdom, logging '
  '<b>360 exploitation attempts</b>, with the majority of attack traffic originating from Russia. Attackers '
  'are going straight for environment variables &mdash; querying files such as '
  '<span class="mono">/root/.cache/langflow/secret_key</span> and checking '
  '<span class="mono">.ssh</span> access and <span class="mono">.bash_history</span> &mdash; to harvest '
  'Langflow superuser credentials, AWS secrets and OpenAI API keys. Users are advised to upgrade to '
  '<b>version 1.11.6</b>, which patches all known vulnerabilities in the platform.</p>')
A('</div>')

# Patch priority
A('<h2 class="sec">Patch Priority</h2>')
A('<div class="callout crit">')
A('<h3>Patch SonicWall SMA 1000 today &mdash; hotfix 12.4.3-03526 / 12.5.0-02952, and there are no workarounds</h3>')
A('<p style="margin:0 0 9px;font-size:15px">SonicWall\'s SMA 1000 secure-access appliances are under attack '
  'through <b>two chained zero-days</b>. <b>CVE-2026-83548</b> is a pre-authentication <b>server-side request '
  'forgery</b> in the Appliance Work Place interface, carrying a <b>maximum CVSS v3 score of 10.0 (reported)</b>; '
  '<b>CVE-2026-83549</b> is a post-authentication <b>OS command injection</b> in the Appliance Management '
  'Console, <b>7.8 (reported)</b>, that an admin-privileged attacker can turn into remote code execution. '
  'SonicWall\'s PSIRT says it has observed exploitation of <i>both</i>, which indicates they are being '
  '<b>chained for unauthenticated RCE</b>.</p>')
A('<p style="margin:0 0 9px;font-size:15px">Affected: physical and virtual models <b>6210, 7210 and 8200v</b>. '
  'Fixed in hotfixes <b>12.4.3-03526</b> and <b>12.5.0-02952</b> and later. <b>SonicWall notes there are no '
  'workarounds.</b> SMA 100 series and SonicWall firewalls are not affected. One outlet frames this as the '
  'second SMA1000 zero-day chain in seven weeks, following the same SSRF-to-injection pattern.</p>')
A('<p class="note" style="margin-top:0">Ranking note: the only KEV due dates re-sourced against CISA this run '
  'are <b>September 5</b> (CVE-2026-9586, Sangoma Switchvox &mdash; <b>3 days left</b>) and <b>September 16</b> '
  '(CVE-2026-48710 &mdash; 14 days left). The SonicWall KEV entry for CVE-2026-83549, due September 5, was '
  'sourced in the previous edition and is carried here, not re-fetched this run. SonicWall leads this box on '
  'severity, internet exposure, vendor-confirmed exploitation, chainability to unauthenticated RCE and the '
  'absence of any workaround &mdash; not on having the shortest verified clock.</p>')
A('</div>')

# Threat actor spotlight
A('<h2 class="sec">Threat Actor Spotlight</h2>')
A('<div class="card" style="border-left:3px solid var(--accent2)">')
A('<div class="tags"><span class="t new">New</span><span class="t warn">Iran-linked APT</span>'
  '<span class="t">Espionage</span></div>')
A('<h3>Mirage Kitten &mdash; fake LinkedIn coding tests, and a warning not to use AI</h3>')
A('<p>The Iran-linked group <b>Mirage Kitten</b> is delivering malware through spear-phishing messages on '
  '<b>LinkedIn and other job-search platforms</b>, sending candidates trojanized coding-challenge archives. '
  'In a detail that doubles as an admission, the operators <b>instructed candidates not to use AI tools</b> '
  'while reviewing the code they were sent &mdash; tools that could have spotted the malware.<br><br>'
  'The payloads, <b>NodeRabbit</b> and <b>PollCat</b>, are the first publicly documented use of Node.js- and '
  'JavaScript-based malware by this group. NodeRabbit hides inside a fake npm package bundled with the coding '
  'test; once run, it starts a background process and connects to infrastructure hosted on <b>Azure</b>, using '
  '<b>AES-256-GCM</b> to protect its communications. PollCat is a cross-platform RAT written in obfuscated '
  'JavaScript that can execute shell commands, move or delete files, collect system information and move files '
  'between the victim and its operators. Telemetry links the activity to <b>fintech, aviation and aerospace '
  'targets across the Middle East and Africa</b>.</p>')
A('</div>')

# Breaches
A('<h2 class="sec">Breaches &amp; Incidents</h2>')
A('<div class="cards">')

A('<div class="card"><div class="tags"><span class="t crit">Extortion</span><span class="t">Healthcare</span></div>'
  '<h3>McKesson &mdash; ShinyHunters, $55M demand</h3>'
  '<p>McKesson <b>confirmed the breach on August 28</b>, affecting customers in its <b>Oncology &amp; '
  'Multispecialty</b> and <b>Medical-Surgical</b> business units. ShinyHunters says it got in through '
  '<b>voice phishing against multiple employees</b>, then used compromised <b>Okta single-sign-on</b> accounts '
  'to reach <b>Salesforce and Snowflake</b> environments. It claims names, addresses, dates of birth, Social '
  'Security numbers, patient IDs, Medicaid numbers, medical record numbers, medication and allergy information '
  'and physician information, and demands <b>$55 million within 72 hours</b>. '
  '<b>Correction carried forward:</b> the widely-quoted <b>284 million</b> figure is a count of <b>data records, '
  'or lines &mdash; not unique individuals</b>; earlier editions of this briefing printed it unqualified.</p></div>')

A('<div class="card"><div class="tags"><span class="t new">New</span><span class="t crit">Ransomware</span>'
  '<span class="t">Healthcare</span></div>'
  '<h3>Nutex Health &mdash; attribution disputed three ways</h3>'
  '<p>The hospital operator confirms that <b>patient, employee, provider, business and financial information</b> '
  'was stolen in a cyberattack. <b>Who did it is genuinely unsettled.</b> Sources fetched this run name '
  '<b>The Gentlemen</b> ransomware group as the claimant; the same reporting notes <b>ShinyHunters</b> also '
  'posted an entry for the firm on its leak site claiming hundreds of millions of records; and a previous '
  'edition of this briefing sourced <b>Rhysida</b>. No record count, dwell time or attribution is asserted here, '
  'because the three claims cannot all be right.</p></div>')

A('<div class="card"><div class="tags"><span class="t">Healthcare</span><span class="t">Cloud</span></div>'
  '<h3>Aesto Health &mdash; 9.5 million people</h3>'
  '<p>Roughly <b>9.5 million individuals</b> had personal and health information stolen after attackers reached '
  'the health-technology company\'s <b>AWS infrastructure</b>; the incident has been formally reported to HHS. '
  'Carried from the previous edition and not re-sourced this run: exfiltration ran <b>December 2&ndash;18</b>, '
  'was determined on <b>May 26, 2026</b>, and spans roughly <b>two dozen provider clients</b> across several '
  'states, with SSNs, licences, financial accounts and taxpayer IDs among the data.</p></div>')

A('<div class="card"><div class="tags"><span class="t new">New</span><span class="t warn">AI supply chain</span></div>'
  '<h3>Langflow credential theft &mdash; and Rails alongside it</h3>'
  '<p>The Langflow campaign in today\'s top story is being reported as part of a broader credential-harvesting '
  'wave: security press this run pairs the <b>Langflow</b> exploitation with <b>critical Ruby on Rails flaws</b> '
  'in the same attacks. Beyond the pairing itself, no Rails CVE identifier, score or affected version was stated '
  'in anything fetched this run, so none is printed.</p></div>')
A('</div>')

# Vulnerability watch
A('<h2 class="sec">Vulnerability Watch</h2>')
A('<div class="panel" style="padding:6px 8px"><table>')
A('<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>')
rows = [
 ("CVE-2026-0768", "9.8", "Langflow &le; 1.4.2",
  "Unauthenticated RCE as root via the <span class='mono'>validate</span> endpoint's code parameter. "
  "<b>Actively exploited.</b> Fixed in 1.11.6."),
 ("CVE-2026-83548", "10.0 (reported)", "SonicWall SMA 1000 &mdash; Appliance Work Place",
  "Pre-authentication SSRF. Chained with CVE-2026-83549 for unauthenticated RCE. <b>Exploited.</b> No workarounds."),
 ("CVE-2026-83549", "7.8 (reported)", "SonicWall SMA 1000 &mdash; Appliance Management Console",
  "Post-authentication OS command injection &rarr; RCE for an admin-privileged attacker. <b>Exploited; in KEV.</b>"),
 ("CVE-2026-9586", "9.3 (CVSS 4.0)", "Sangoma Switchvox &lt; 8.4.0.2",
  "Unauthenticated SQL injection through the <span class='mono'>/pa</span> endpoint &rarr; RCE. "
  "<b>KEV, due September 5.</b> Patched July 14, 2026."),
 ("CVE-2026-62911", "8.0 (Microsoft) / 8.1 (ZDI)", "Microsoft Exchange",
  "Authentication bypass via divergent MRSProxy paths abused through WCF &rarr; ASPX webshell &rarr; SYSTEM. "
  "Patched August 11, 2026. Carried, not re-sourced this run."),
]
for c, s, a, n in rows:
    A(f'<tr><td class="mono">{c}</td><td class="mono">{s}</td><td>{a}</td><td>{n}</td></tr>')
A('</table></div>')
A('<p class="note">The SonicWall <b>10.0</b> and <b>7.8</b> are printed as <b>reported</b>, not adopted: they '
  'come from security-press summaries of SonicWall advisory SNWLID-2026-0016, and no vendor advisory page was '
  'fetched directly this run. This follows the same rule that kept a blog\'s 9.8 off a Citrix entry the vendor '
  'scored 9.3.</p>')

# KEV
A('<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>')
A('<div class="panel">')
A('<ul class="bul">')
A('<li><b>CVE-2026-9586</b> (Sangoma Switchvox) &mdash; added <b>September 2, 2026</b>, due '
  '<b>September 5, 2026</b> <span class="mono" style="color:var(--crit)">(3 days left)</span>. CISA flags it as '
  'requiring forensic triage per BOD-26-04. <i>Note: September 5, 2026 is a Saturday.</i></li>')
A('<li><b>CVE-2026-48710</b> &mdash; added <b>September 2, 2026</b>, due <b>September 16, 2026</b> '
  '<span class="mono" style="color:var(--warn)">(14 days left)</span>; does not require forensic triage per '
  'BOD-26-04. No affected product was stated in anything fetched this run, so none is named here.</li>')
A('<li><b>CVE-2026-83549</b> (SonicWall SMA 1000) &mdash; recorded in the previous edition as added September 2 '
  'and due September 5. <b>Carried, not re-fetched this run</b>, so it is listed without an independent '
  'countdown.</li>')
A('<li><b>CVE-2026-81578</b> and <b>CVE-2026-82078</b> (PaperCut) &mdash; added <b>August 31, 2026</b> per CISA\'s '
  'own alert page. <b>No per-CVE due date has ever been sourced, so no countdown is printed</b> rather than one '
  'being inferred from the three-week BOD 22-01 window.</li>')
A('</ul>')
A('<p class="note">The September 2 KEV additions returned by search <b>disagree between runs</b>: this run\'s '
  'query returns CVE-2026-9586 and CVE-2026-48710; the previous edition\'s returned CVE-2026-83549 and '
  'CVE-2026-59822 (BerriAI LiteLLM, improper authentication, CVSS 3.1 = 8.2 / CVSS 4.0 = 8.8, fixed in 1.84.0, '
  'no due date sourced). <b>Neither pair is treated as the complete list for the day.</b> Under BOD 22-01 the '
  'standard remediation window is three weeks from the add date; the September 5 dates above are shorter because '
  'CISA set them explicitly.</p>')
A('</div>')

A(shared.sources([
 ("BleepingComputer &mdash; Critical Langflow flaw exploited to steal OpenAI and AWS keys",
  "https://www.bleepingcomputer.com/news/security/critical-langflow-flaw-exploited-to-steal-openai-and-aws-keys/"),
 ("SecurityWeek &mdash; Hackers Start Exploiting Critical Langflow Vulnerability",
  "https://www.securityweek.com/hackers-start-exploiting-critical-langflow-vulnerability/"),
 ("Security Affairs &mdash; Hackers Target Langflow in CVE-2026-0768 Attacks",
  "https://securityaffairs.com/198270/hacking/hackers-target-langflow-in-cve-2026-0768-attacks.html"),
 ("Help Net Security &mdash; SonicWall SMA 1000 appliances under attack via zero-day flaws",
  "https://www.helpnetsecurity.com/2026/09/02/sonicwall-sma-1000-cve-2026-83548-cve-2026-83549-zero-day-attacks/"),
 ("BleepingComputer &mdash; SonicWall warns of actively exploited SMA1000 zero-day flaws",
  "https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-actively-exploited-sma1000-zero-day-flaws/"),
 ("The Hacker News &mdash; Attackers Exploit Two SonicWall SMA 1000 Zero-Days That May Form a Chain",
  "https://thehackernews.com/2026/09/attackers-exploit-two-sonicwall-sma.html"),
 ("Securelist (Kaspersky) &mdash; Mirage Kitten switches to Node.js and JavaScript malware",
  "https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/"),
 ("Security Affairs &mdash; Iran-linked APT Mirage Kitten Uses Fake Job Tests to Spread Malware",
  "https://securityaffairs.com/198289/apt/iran-linked-apt-mirage-kitten-uses-fake-job-tests-to-spread-malware.html"),
 ("BleepingComputer &mdash; McKesson discloses breach after ShinyHunters claims patient data theft",
  "https://www.bleepingcomputer.com/news/security/mckesson-discloses-breach-after-shinyhunters-claims-patient-data-theft/"),
 ("SecurityWeek &mdash; Ransomware Gang Claims Nutex Health Data Breach",
  "https://www.securityweek.com/ransomware-gang-claims-nutex-health-data-breach/"),
 ("Infosecurity Magazine &mdash; Nutex Health Says Patient Data Stolen, Hackers Threaten Leak",
  "https://www.infosecurity-magazine.com/news/nutex-patient-data-stolen/"),
 ("CISA &mdash; Known Exploited Vulnerabilities Catalog",
  "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
 ("CISA &mdash; Adds Two Known Exploited Vulnerabilities to Catalog (Aug 31, 2026)",
  "https://www.cisa.gov/news-events/alerts/2026/08/31/cisa-adds-two-known-exploited-vulnerabilities-catalog"),
 ("Verizon &mdash; 2026 Data Breach Investigations Report",
  "https://www.verizon.com/business/resources/reports/dbir/"),
]))
A('<p class="disc">This briefing is compiled from public reporting and is provided for information only. '
  'Vulnerability scores, exploitation status and remediation deadlines change; verify against the vendor '
  'advisory and the CISA KEV catalog before acting.</p>')
A('</footer>')

html = shared.page("The Cyber Wire &mdash; Daily Briefings", ACCENT, ACCENT2,
                   "#0b1110", "#121a19", "#1e2b29", "\n".join(body))
io.open("cyber-briefing.html", "w", encoding="utf-8").write(html)
print("cyber ok", len(html))
