# -*- coding: utf-8 -*-
import os,sys
sys.path.insert(0,'/tmp')
exec(open('/tmp/build_1710.py').read().split('# ============================================================ WALL STREET')[0])

CYCSS=css_for("#0a0f0e","#111a19","#1e2b29","#22d3a8","#36c6ff")

CY_TLDR=("CISA has given federal agencies until Friday to fix an actively exploited Sangoma Switchvox flaw now scored 9.3 and being used to "
 "drop reverse shells, while an MLflow credential-theft bug hits its federal deadline today and McKesson confirms a breach ShinyHunters says "
 "runs to 284 million patient records.")

cy=[]
cy.append('<div class="banner high"><span class="k">Threat Level &mdash; High</span>'
 'Two separate flaws are being exploited against internet-facing infrastructure right now &mdash; Sangoma Switchvox for reverse-shell access and '
 'MLflow for cloud credential theft &mdash; and the MLflow federal remediation deadline expires today.</div>')

cy.append('<div class="stats">'
 '<div class="stat"><div class="n">284M</div><div class="l">Patient records ShinyHunters claims to have stolen from McKesson</div></div>'
 '<div class="stat"><div class="n">$55M+</div><div class="l">Ransom demanded from McKesson, on a 72-hour deadline</div></div>'
 '<div class="stat"><div class="n">9.3</div><div class="l">CVSS 4.0 score newly published for the exploited Switchvox SQL injection</div></div>'
 '<div class="stat"><div class="n">3.7M</div><div class="l">Patients whose records were stolen in the CareCloud breach confirmed Aug 19</div></div>'
 '</div>')

cy.append('<h2 class="sec">Top Story</h2><div class="panel">'
 '<h3>The Switchvox flaw CISA flagged yesterday now has a severity score &mdash; and attackers are using it to plant reverse shells</h3>'
 '<p><b>CVE-2026-9586</b>, an unauthenticated SQL injection in <b>Sangoma Switchvox</b>, was added to CISA&rsquo;s Known Exploited '
 'Vulnerabilities catalog on <b>September 2</b> with a remediation deadline of <b>September 5</b>. This run is the first to source a severity '
 'score for it: <b>9.3, Critical, under CVSS 4.0</b>.</p>'
 '<p>The mechanism is now public in detail. The <code>/pa</code> endpoint processes XML beginning with <code>&lt;PolycomIPPhone&gt;</code> and '
 'concatenates the user-controlled <b>PhoneIP</b> value directly into PostgreSQL queries with no sanitisation or parameterisation. That gives an '
 'unauthenticated remote attacker arbitrary SQL against the backend database, and from there remote code execution. Reporting this run describes '
 'a threat actor actively targeting internet-exposed Switchvox instances and <b>deploying reverse shells</b>.</p>'
 '<p>The patch is not new: <b>Sangoma released Switchvox 8.4.0.2 on July 14, 2026</b>. Anything still exposed has been patchable for seven weeks '
 'and is now being hunted. Organisations running it are being told to check for signs of compromise rather than simply update.</p>'
 '</div>')

cy.append('<div class="callout crit"><div class="k">Patch Priority &mdash; today</div>'
 '<p><b>MLflow &mdash; CVE-2026-64849, CVSS 9.3, all versions before 3.15.0. KEV-added August 19; the federal remediation deadline is '
 '<u>today, September 2</u> &mdash; zero days left.</b></p>'
 '<p>This is an <b>unauthenticated server-side request forgery</b>: an attacker makes the MLflow server issue HTTP requests to internal '
 'endpoints, reaches cloud metadata services directly, and exfiltrates cloud credentials and secrets. In-the-wild exploitation began '
 '<b>within hours of CVE assignment</b>. It keeps this slot over higher-scored entries for one reason &mdash; it is the only item on the '
 'page whose sourced deadline is today. The Switchvox flaw above (9.3, exploited, reverse shells) is three days behind it at September 5, '
 'and the VMware vCenter entry carries a higher reported score but no sourced federal clock.</p></div>')

cy.append('<h2 class="sec">Threat Actor Spotlight &mdash; ShinyHunters</h2><div class="panel">'
 '<h3>A voice call, an SSO account, and 284 million records</h3>'
 '<p>ShinyHunters compromised McKesson by <b>voice phishing employees into handing over Okta single sign-on access</b>, then pivoting into the '
 'company&rsquo;s cloud environments. Exfiltration ran <b>August 21 to 25</b>; McKesson discovered the incident on <b>August 25</b> and has now '
 'confirmed it. The group claims more than <b>284 million records</b> and has demanded <b>over $55 million</b> on a 72-hour deadline.</p>'
 '<p>The data is said to include patient identifiers, Social Security numbers, diagnoses, medications and doctor&ndash;patient messages. '
 'Nothing in the chain required a software vulnerability: the entry point was a phone call, and the escalation was an identity provider trusted '
 'by everything downstream of it.</p></div>')

cy.append('<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards two">'
 '<div class="card"><div class="k">Healthcare &mdash; McKesson</div><h4>Breach confirmed; 284M records claimed</h4>'
 '<span class="tag c">Extortion</span><span class="tag a">Healthcare</span>'
 '<p>McKesson has confirmed a cybersecurity incident discovered August 25 after ShinyHunters claimed the theft of patient data. Vector: '
 'vishing into Okta SSO, then cloud environments; exfiltration August 21&ndash;25. Ransom demand exceeds $55 million.</p></div>'
 '<div class="card"><div class="k">Medical devices &mdash; Boston Scientific</div><h4>Ongoing intrusion; remote cardiac monitoring degraded</h4>'
 '<span class="tag c">Ongoing</span><span class="tag w">Attribution disputed</span>'
 '<p>An August 25 compromise of on-premises IT disrupted global operations. <b>Pacemakers and other heart devices implanted after the breach '
 'cannot provide remote monitoring and data transmission as intended.</b> The company has repeatedly declined to say whether it was ransomware '
 'or who is responsible; this run&rsquo;s sources state <b>no group has claimed it</b>, while an earlier edition recorded a claim by '
 '&ldquo;Server Killers.&rdquo; Both are printed; neither is adopted.</p></div>'
 '<div class="card"><div class="k">Healthcare IT &mdash; CareCloud</div><h4>3.7 million patients&rsquo; medical records stolen</h4>'
 '<span class="tag a">Healthcare</span><p>CareCloud confirmed on August 19 that 3.7 million patients had medical records stolen in a data '
 'breach &mdash; the third healthcare-sector incident on this page, and the pattern of the month.</p></div>'
 '<div class="card"><div class="k">Ransomware ecosystem &mdash; The Gentlemen</div><h4>A 90% affiliate cut, and it is working</h4>'
 '<span class="tag new">New</span><span class="tag w">RaaS</span>'
 '<p>First observed in September 2025, The Gentlemen has become one of the most active extortion brands by handing affiliates a <b>90% cut</b>, '
 'and ranks second among 2026 ransomware gangs by victim count. Its leak site had claimed more than <b>320 victims, 240 of them in 2026</b> '
 '&mdash; a count stated <b>as of April 2026</b>, so it is published with that as-of date rather than as a current total.</p></div>'
 '</div>'
 '<div class="note"><b>Standing refusals.</b> The Nevada statewide ransomware incident is permanently excluded &mdash; it is <b>August 2025</b>, '
 'and any &ldquo;2026 breaches&rdquo; listing that surfaces it is mis-shelving last year&rsquo;s event; refused on sight. IDMerit, Panera and '
 'Vanderbilt remain refused from earlier runs. New this run and also refused: a breach-tracker listing dated September 1 offering '
 '&ldquo;laboral.com.ar, 6.8 million records&rdquo; alongside a 9.8-million-record Panera entry &mdash; the Panera figure is already refused, '
 'and the tracker gives no incident date, disclosure source or victim confirmation for either.</div>')

cy.append('<h2 class="sec">Vulnerability Watch</h2><div class="tblwrap"><table>'
 '<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>'
 '<tr><td><b>CVE-2026-9586</b></td><td class="down">9.3</td><td>Sangoma Switchvox</td>'
 '<td>Unauthenticated SQL injection at <code>/pa</code> via the PhoneIP value, extending to RCE. Score is CVSS 4.0, newly sourced this run. '
 'Patched in <b>8.4.0.2, released July 14, 2026</b>. Actively exploited; reverse shells observed. KEV due Sept 5.</td></tr>'
 '<tr><td><b>CVE-2026-64849</b></td><td class="down">9.3</td><td>MLflow, all versions before 3.15.0</td>'
 '<td>Unauthenticated SSRF reaching cloud metadata services; used to steal cloud credentials and secrets. Exploited within hours of CVE '
 'assignment. <b>KEV deadline today.</b></td></tr>'
 '<tr><td><b>CVE-2026-59310</b></td><td class="down">9.8 (reported)</td><td>VMware vCenter</td>'
 '<td>Directory traversal in the Syslog server leading to arbitrary code execution. Disclosed <b>July 29</b> when Broadcom patched it alongside '
 'four other VMware defects; a suspected APT began exploiting it <b>August 3</b>, using a reverse shell for persistent access. '
 '<b>The 9.8 is attributed, not adopted</b> &mdash; it comes from security press, not a vendor advisory fetched this run, and this desk has '
 'twice been burned by inflated 9.8s (Citrix&rsquo;s official 9.3, Progress&rsquo;s official 9.6).</td></tr>'
 '<tr><td><b>CVE-2026-82078</b></td><td class="down">9.4</td><td>PaperCut NG/MF</td>'
 '<td>Vendor score, from PaperCut&rsquo;s August 27 advisory. The vendor calls it unsafe dynamic class loading; CISA words it &ldquo;unsafe '
 'reflection.&rdquo; Both descriptors stand. KEV-added Aug 31.</td></tr>'
 '<tr><td><b>CVE-2026-81578</b></td><td class="down">8.8</td><td>PaperCut NG/MF</td>'
 '<td>Authentication bypass; CISA words it &ldquo;missing authentication for critical function.&rdquo; Advisory published while PaperCut was '
 'investigating active exploitation with confirmed customer incidents. KEV-added Aug 31.</td></tr>'
 '<tr><td><b>CVE-2026-69836</b></td><td>&mdash;</td><td>Microsoft Entra ID</td>'
 '<td><b>Corrected this run.</b> A previous edition of this page listed this critical RCE as an exploited zero-day. <b>Microsoft has since '
 'changed the exploitation status to &ldquo;no&rdquo; and confirmed it was not exploited in the wild.</b> It is patched; it is not an active '
 'threat. No CVSS was sourced, so none is printed.</td></tr>'
 '</table></div>')

cy.append('<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2><div class="panel"><ul class="b">'
 '<li><b>CVE-2026-64849 &mdash; MLflow.</b> Added August 19. Due <b>today, September 2</b> &mdash; <span class="down"><b>0 days left</b></span>.</li>'
 '<li><b>CVE-2026-9586 &mdash; Sangoma Switchvox.</b> Added <b>September 2</b>. Due <b>September 5</b> &mdash; <b>3 days left</b>.</li>'
 '<li><b>CVE-2026-48710.</b> Added <b>September 2</b>. Due <b>September 16</b> &mdash; <b>14 days left</b>. CISA&rsquo;s entry describes an '
 'open-source component used across multiple products and <b>names no product, so this page names none</b>.</li>'
 '<li><b>CVE-2026-81578 and CVE-2026-82078 &mdash; PaperCut NG/MF.</b> Added <b>August 31</b>, confirmed against CISA&rsquo;s own alert page '
 'this run. <b>No per-CVE due date was sourced this run, so no countdown is printed for them.</b></li>'
 '<li><b>An Oracle entry</b> carried in this desk&rsquo;s verified record passed its deadline on August 27 &mdash; '
 '<span class="down"><b>6 days overdue</b></span>. It is listed without a CVE identifier because none was re-sourced this run.</li>'
 '</ul>'
 '<div class="note"><b>No deadline on this page is inferred.</b> CISA&rsquo;s remediation windows are now risk-based and assigned per CVE under '
 '<b>BOD 26-04</b> &mdash; cited in CISA&rsquo;s own KEV entries as &ldquo;Prioritizing Security Updates Based on Risk&rdquo; &mdash; so the old '
 'BOD 22-01 flat three-week heuristic is superseded and is not applied here. Every countdown above is arithmetic from September 2 to a published '
 'due date; where no due date was published to a source fetched this run, no countdown appears.</div></div>')

cy.append(srcs([
 ("https://www.helpnetsecurity.com/2026/09/02/exploitation-of-sangoma-switchvox-flaw-underway-cve-2026-9586/","Help Net Security &mdash; Exploitation of Sangoma Switchvox flaw is underway (CVE-2026-9586), Sept 2 2026"),
 ("https://thehackernews.com/2026/09/attackers-exploit-critical-switchvox-flaw.html","The Hacker News &mdash; Attackers exploit critical Switchvox flaw to deploy reverse shells"),
 ("https://www.sentinelone.com/vulnerability-database/cve-2026-9586/","SentinelOne vulnerability database &mdash; CVE-2026-9586 (CVSS 4.0 score 9.3)"),
 ("https://vulnerability.circl.lu/vuln/cve-2026-9586","CIRCL Vulnerability-Lookup &mdash; CVE-2026-9586"),
 ("https://www.cisa.gov/known-exploited-vulnerabilities-catalog","CISA &mdash; Known Exploited Vulnerabilities Catalog"),
 ("https://www.cisa.gov/news-events/alerts/2026/08/31/cisa-adds-two-known-exploited-vulnerabilities-catalog","CISA &mdash; Adds two KEVs (PaperCut CVE-2026-81578, CVE-2026-82078), Aug 31 2026"),
 ("https://www.securityweek.com/mlflow-vulnerability-exploited-for-cloud-credential-theft/","SecurityWeek &mdash; MLflow vulnerability exploited for cloud credential theft"),
 ("https://www.securityweek.com/critical-vmware-vcenter-vulnerability-in-attackers-crosshairs/","SecurityWeek &mdash; Critical VMware vCenter vulnerability in attackers&rsquo; crosshairs"),
 ("https://www.infosecurity-magazine.com/news/vcenter-cve-2026-59310-exploited/","Infosecurity Magazine &mdash; vCenter CVE-2026-59310 exploited five days after disclosure"),
 ("https://www.helpnetsecurity.com/2026/08/21/microsoft-entra-id-vulnerability-cve-2026-69836/","Help Net Security &mdash; Microsoft patches critical Entra ID vulnerability CVE-2026-69836 [exploitation status later changed to &ldquo;no&rdquo;]"),
 ("https://www.bleepingcomputer.com/news/security/mckesson-discloses-breach-after-shinyhunters-claims-patient-data-theft/","BleepingComputer &mdash; McKesson discloses breach after ShinyHunters claims patient data theft"),
 ("https://cybernews.com/news/mckesson-breached-shinyhunters-claims-284m-records/","Cybernews &mdash; McKesson breach: ShinyHunters claims 284m patient records"),
 ("https://www.theregister.com/cyber-crime/2026/08/31/healthcare-cyberattacks-hit-pacemakers-and-millions-of-patient-records/5293537","The Register &mdash; Healthcare cyberattacks hit pacemakers and millions of patient records"),
 ("https://techcrunch.com/2026/08/19/carecloud-confirms-3-7m-patients-had-their-medical-records-stolen-in-data-breach/","TechCrunch &mdash; CareCloud confirms 3.7M patients had medical records stolen"),
 ("https://tech-insider.org/the-gentlemen-ransomware-2026/","Tech Insider &mdash; The Gentlemen ransomware: victim count and affiliate terms [as of April 2026]"),
])+'<div class="disc">Defensive information only. Vulnerability details are summarised from public advisories and reporting; verify against your '
 'vendor&rsquo;s own bulletin before acting. Remediation deadlines apply to U.S. federal civilian agencies under CISA&rsquo;s binding operational '
 'directives and are published here as a severity signal for everyone else.</div></footer>')

open(os.path.join(OUT,'cyber-briefing.html'),'w').write(page(
 "The Cyber Wire — Daily Briefings",CYCSS,
 mast("The Cyber Wire","Your daily cybersecurity briefing &mdash; breaches, vulnerabilities &amp; the threat landscape","The Wire",CY_TLDR),
 ''.join(cy),"cyber-briefing.html"))
print("cyber ok")
