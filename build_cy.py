# -*- coding: utf-8 -*-
import shared, io, datetime

ACC, ACC2 = "#22d3a8", "#36c6ff"
css = shared.css(ACC, ACC2, "#0b0f0e", "#141a19", "#233230")

TODAY = datetime.date(2026, 9, 5)
DUE_CHROME = datetime.date(2026, 9, 18)
LEFT = (DUE_CHROME - TODAY).days   # 13

TLDR = ("A maximum-severity SonicWall SMA 1000 flaw is confirmed exploited in the wild and can be "
        "chained to remote code execution, while a Chromium V8 zero-day carries a September 18 federal "
        "patch deadline — and Unit 42 has published the anatomy of an AI-directed intrusion that took "
        "root in under ten hours.")

b = io.StringIO(); w = b.write
w(shared.masthead("The Cyber Wire", "Your daily security briefing — breaches, vulnerabilities &amp; the KEV clock"))
w(f'<div class="tldr"><b>The Wire</b> <span>{TLDR}</span></div>')
w('<div class="freshline" id="freshline">&nbsp;</div>')
w(shared.nav("cyber"))

w('<div class="banner"><span class="lvl">Threat level: High</span>'
  '<span style="font-size:14px">A CVSS 10.0 pre-authentication flaw in an internet-facing VPN appliance '
  '(SonicWall SMA 1000) is confirmed exploited in the wild and is being chained toward remote code '
  'execution, and a separately exploited browser zero-day is on the federal clock.</span></div>')

w('<div class="stats">')
w('<div class="stat"><div class="n">&lt; 10 hrs</div><div class="l">Time an AI-directed attacker needed to '
  'go from initial access to root, per Unit 42 — work researchers put at roughly two weeks for humans</div></div>')
w('<div class="stat"><div class="n">50+</div><div class="l">MITRE ATT&amp;CK techniques the agents executed '
  'inside that single intrusion</div></div>')
w('<div class="stat"><div class="n">10.0</div><div class="l">CVSS of CVE-2026-83548, the SonicWall SMA 1000 '
  'pre-auth SSRF, per the vendor advisory</div></div>')
w('<div class="stat"><div class="n">284M</div><div class="l">Records ShinyHunters claims it took from '
  'McKesson — the attackers’ figure, not a company-confirmed one</div></div>')
w('</div>')
w('<div class="note">Every figure in this strip comes from a primary or vendor source fetched this run. '
  'Aggregator “2026 cybersecurity statistics” pages are still refused: one returned mutually contradictory '
  'numbers inside a single response (global average breach cost given as both $4.88M and $4.44M).</div>')

w('<h2 class="sec">Top Story</h2>')
w('<div class="panel">')
w('<h3 style="margin:0 0 9px;font-size:21px">An attacker with frontier AI models compressed weeks of '
  'intrusion tradecraft into under ten hours — and left an 80-page audit behind</h3>')
w('<p>Unit 42, Palo Alto Networks’ threat-intelligence arm, published its investigation on September 2 '
  '(updated September 3 and September 4). A human attacker paired frontier AI models with attack-specific '
  '<strong>agentic AI frameworks</strong> and executed <strong>more than 50 MITRE ATT&amp;CK '
  'techniques in less than ten hours</strong> — work Unit 42 assesses at the scale of several coordinated '
  'red teams over roughly two weeks.</p>')
w('<p>After initial access, the agents mapped the internal architecture, combed source repositories for '
  'hard-coded secrets, seized the secrets manager and root credentials, triggered unauthorised CI/CD builds '
  'to exfiltrate cloud keys, and claimed master keys to the victim’s own cloud AI infrastructure — turning '
  'the target’s AI endpoints into post-compromise infrastructure. A Terraform backdoor attempt was stopped '
  'by branch protection. The attacker left behind an <strong>80-page report</strong> detailing dozens of '
  'exploited weaknesses.</p>')
w('<div class="callout" style="border-left-color:var(--accent2);margin-top:14px">'
  '<h3 style="color:var(--accent2)">Framing check — the secondary coverage is wrong</h3>'
  '<p style="margin:0">Secondary coverage keeps calling this ransomware. DataBreaches.net headlines it '
  '“Agentic Ransomware Took Down Enterprise in Ten Hours”; CSO Online writes of AI agents compressing a '
  'ransomware intrusion to under 10 hours; this desk’s log records The Register using the same framing. '
  '<strong>Unit 42’s own page carries a correction, dated September 3 at '
  '5:25 a.m. PT, stating the incident “was an intrusion, and not a ransomware attack.”</strong> This desk '
  'follows the primary source and names the discrepancy rather than papering over it. Ransom negotiations '
  'did occur — that is how the tooling was learned — but the victim is unnamed and no ransom figure was '
  'reported. Unit 42’s own emphasis: what made this notable was AI-assisted operational efficiency, '
  '<em>not</em> a novel zero-day or elite tradecraft.</p></div>')
w('</div>')

w('<h2 class="sec">Patch Priority</h2>')
w('<div class="callout crit">')
w('<h3>Do this first — CVE-2026-83548, SonicWall SMA 1000</h3>')
w('<p><strong>CVE-2026-83548 (CVSS 10.0)</strong> is a <strong>pre-authentication server-side request '
  'forgery</strong> in the Appliance Work Place interface of SonicWall SMA 1000 series appliances, reachable '
  'by a remote unauthenticated attacker. SonicWall says it has “investigated a case indicating the active '
  'exploitation of the vulnerabilities,” and believes attackers are <strong>chaining</strong> it with '
  '<strong>CVE-2026-83549 (CVSS 7.8)</strong>, a post-authentication OS command injection in the Appliance '
  'Management Console, to reach arbitrary code execution.</p>')
w('<p><strong>Affected:</strong> SMA 1000 models 6210, 7210 and 8200v on 12.4.3-03453 (platform-hotfix) and '
  'older, and 12.5.0-02835 (platform-hotfix) and older. <strong>Fixed builds:</strong> 12.4.3-03526 and '
  '12.5.0-02952. SonicWall also advises reviewing for indicators of compromise and, if any are found, '
  're-imaging or re-deploying the appliance, changing all user and administrator passwords, and resetting TOTP.</p>')
w('<p><strong>Why this box is red, and not amber:</strong> the desk’s rule turns the border red when a '
  'deadline is today or overdue <em>or</em> a maximum-severity flaw is actively exploited. CVE-2026-83548 is '
  '<strong>CVSS 10.0 and confirmed exploited</strong> — squarely the second branch. It is red on severity, '
  'not on a clock.</p>')
w('<p><strong>Deadline honesty:</strong> reporting on the September 2 KEV batch states a '
  '<strong>September 5, 2026</strong> remediation due date for both SonicWall CVEs — which would be today, '
  'and far shorter than BOD 22-01’s usual three weeks. <strong>CISA’s own alert page returned empty on '
  'fetch for a third consecutive run</strong>, so this desk does <em>not</em> assert that date. The only '
  'KEV deadline this edition publishes at all is the Chromium one below — and even that is attributed to '
  'reporting rather than read off CISA directly.</p>')
w('</div>')

w('<h2 class="sec">Threat Actor Spotlight</h2>')
w('<div class="panel">')
w('<div class="tags"><span class="t hot">Extortion</span><span class="t">Vishing</span><span class="t">SaaS abuse</span></div>')
w('<h3 style="margin:0 0 8px;font-size:19px">ShinyHunters / “Scattered LAPSUS$ Hunters”</h3>')
w('<p>A joint operation run with Scattered Spider and LAPSUS$ through a public Telegram channel. Vendor '
  'records put <strong>40+ claimed breaches in 2026 as of July</strong>. Claimed victims include '
  'Canvas/Instructure (~275 million student records), Carnival, ADT (~5.5 million), Charter, Kemper, '
  'McGraw-Hill, Rockstar Games, Telus and the European Commission. The crew ran an “AuraInspector” campaign '
  'against roughly 400 organisations via Salesforce Experience Cloud misconfigurations, and used stolen '
  'Anodot tokens to reach Google BigQuery. Every item here is a <strong>claim</strong> recorded by vendors, '
  'not an independently confirmed count.</p>')
w('</div>')

w('<h2 class="sec">Breaches &amp; Incidents</h2>')
w('<div class="cards">')
w('<div class="card"><div class="tags"><span class="t new">New</span><span class="t hot">Healthcare</span>'
  '<span class="t">Extortion</span></div>'
  '<h3>McKesson confirms a breach — in an SEC filing</h3>'
  '<p>The distributor <strong>discovered the incident on August 25, 2026</strong> and has now '
  '<strong>confirmed it in a filing with the U.S. Securities and Exchange Commission</strong> — a material '
  'change from the last edition, which could only report the attackers’ side. McKesson says the incident '
  'involved unauthorised access to <strong>third-party applications</strong> and data theft, affecting a '
  'subset of customers within its <strong>Oncology &amp; Multispecialty</strong> and '
  '<strong>Medical-Surgical</strong> business units. Its investigation is early; it says it does not '
  'currently believe customers need to act, that initial containment appears successful, and that no further '
  'unauthorised activity has been detected. ShinyHunters claims Snowflake and Salesforce access obtained by '
  '<strong>voice-phishing multiple employees</strong>, roughly <strong>1 TB</strong> taken August 21–25, and '
  '<strong>284 million patient records</strong> — an attacker claim, and reporting notes it does not imply '
  '284 million distinct patients. The demand was <strong>$55,236,150</strong> on a 72-hour clock; per '
  'ShinyHunters, McKesson did not respond or negotiate.</p></div>')
w('<div class="card"><div class="tags"><span class="t">Legal sector</span><span class="t">Long dwell</span></div>'
  '<h3>Thomson Reuters C-Track court software</h3>'
  '<p>Files were taken in <strong>March 2026</strong> and discovered on <strong>June 30, 2026</strong> — '
  'roughly four months undetected. <strong>Sealed and redacted court material may be affected.</strong> '
  'A count discrepancy is printed rather than resolved: this run’s reporting says “at least 12 US states” '
  'plus the U.S. Virgin Islands and Canada, while this desk’s log records body text naming '
  '<strong>eleven</strong> — Alabama, Pennsylvania, Kentucky, Montana, Nevada, North Dakota, South Carolina, '
  'Tennessee, Ohio, New Hampshire and Wyoming — plus USVI and Ontario. Twelve months of Experian '
  'IdentityWorks is on offer, enrolment open until December 31, 2026.</p></div>')
w('<div class="card"><div class="tags"><span class="t gold">June 2026 — not new</span><span class="t">Supply chain</span></div>'
  '<h3>Klue, labelled with its real date</h3>'
  '<p>The Klue supply-chain breach keeps surfacing in September-scoped searches. <strong>TechCrunch dates '
  'it June 22 and June 25, 2026.</strong> Roughly 200 customers were reached via an unrotated 2022 OAuth '
  'credential by an extortion crew calling itself “Icarus”; named downstream organisations include LastPass, '
  'BeyondTrust, Jamf, HackerOne, Recorded Future, Snyk, Tanium and Huntress. It is carried here '
  '<strong>explicitly labelled June 2026</strong> so the next edition does not import it as fresh.</p></div>')
w('<div class="card"><div class="tags"><span class="t">Refused</span></div>'
  '<h3>Refusals held again</h3>'
  '<p>Three stories were re-surfaced by 2026-scoped searches and refused on sight: <strong>Nevada</strong> '
  '(August <strong>2025</strong>), <strong>Kido International</strong> (September <strong>2025</strong>), and '
  'a “Boeing and Airbus supplier” item that resolves to a <strong>March 2026</strong> LISI Group piece. The '
  'IDScan.net 153-million figure remains unpublished for want of a primary source.</p></div>')
w('</div>')

w('<h2 class="sec">Vulnerability Watch</h2>')
w('<div class="panel"><table>')
w('<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>')
w('<tr><td>CVE-2026-83548</td><td class="down"><strong>10.0</strong></td><td>SonicWall SMA 1000 (6210, 7210, 8200v)</td>'
  '<td>Pre-auth SSRF in the Appliance Work Place. <strong>Exploited in the wild</strong>; added to CISA KEV '
  'September 2. Fixed in 12.4.3-03526 / 12.5.0-02952.</td></tr>')
w('<tr><td>CVE-2026-83549</td><td>7.8</td><td>SonicWall SMA 1000 — Appliance Management Console</td>'
  '<td>Post-auth OS command injection; SonicWall believes it is being chained with 83548 for RCE. Both were '
  'found internally by SonicWall’s William Perry and Adam Babis.</td></tr>')
w('<tr><td>CVE-2026-85046</td><td>8.8</td><td>Chromium V8 (Chrome, Edge, Opera and other Chromium browsers)</td>'
  '<td>Type confusion allowing code execution inside the sandbox via a crafted HTML page. Google confirms '
  'active exploitation. Fixed in Chrome <strong>152.0.7977.82/.83</strong> (Windows, macOS) and '
  '<strong>152.0.7977.82</strong> (Linux), released September 3. Coverage dated September 5 calls it '
  'Chrome’s <strong>sixth zero-day of 2026</strong>.</td></tr>')
w('<tr><td>CVE-2026-9586</td><td class="mut">—</td><td>Sangoma Switchvox</td>'
  '<td>SQL injection; KEV September 2. Reporting says actors weaponised it to deploy reverse shells. No CVSS '
  'was confirmed this run, so none is printed.</td></tr>')
w('<tr><td>CVE-2026-82329</td><td class="mut">—</td><td>JFrog Artifactory</td>'
  '<td>Improper authentication; KEV September 2. Reported to have been used to mint admin tokens for '
  'follow-on enumeration. No CVSS confirmed this run.</td></tr>')
w('<tr><td>CVE-2026-18885 / -18886 / -74820</td><td class="down"><strong>10.0</strong> each</td>'
  '<td>ServiceNow AI Platform</td>'
  '<td>Unauthenticated code and SQL execution. Hosted instances were patched by the vendor; self-hosted '
  'deployments need hotfixes. A fourth issue, <strong>CVE-2026-6876 (8.7)</strong>, is a sandbox escape.</td></tr>')
w('</table>')
w('<div class="note">CVSS values above are taken from the vendor advisory or CISA, never from a blog '
  'figure. Where no authoritative score was confirmed this run, the cell is an em-dash rather than a guess.</div>')
w('</div>')

w('<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>')
w('<div class="panel"><ul class="bul">')
w(f'<li><strong>CVE-2026-85046 (Chromium V8) — added September 4, due September 18, 2026 '
  f'<span class="up">({LEFT} days left)</span>.</strong> The single addition of that day. September 18, 2026 '
  'is a Friday; the count is measured from today, September 5. <strong>Caveat, third consecutive run:</strong> '
  'the CISA alert page itself returned <em>empty</em> on fetch, so this date is published as reported rather '
  'than read off CISA directly — the same wording this desk used in the last two editions.</li>')
w('<li><strong>September 2 batch — seven vulnerabilities added.</strong> CVE-2026-9586 (Sangoma Switchvox, '
  'SQL injection), CVE-2026-48710 (Kludex Starlette, HTTP request/response smuggling), CVE-2026-49869 '
  '(Kestra OSS, OS command injection), CVE-2026-59822 (BerriAI LiteLLM, improper authentication), '
  'CVE-2026-82329 (JFrog Artifactory, improper authentication), CVE-2026-83548 (SonicWall SMA 1000, SSRF) and '
  'CVE-2026-83549 (SonicWall SMA 1000, OS command injection).</li>')
w('<li><strong>No due date is asserted for the September 2 batch.</strong> Reporting gives September 5, 2026 '
  'for the two SonicWall entries; CISA’s own page returned empty, so the desk declines to state it as '
  'verified. The Patch Priority box above says exactly the same thing, in the same terms.</li>')
w('<li><strong>Also in KEV on exploitation evidence:</strong> two PaperCut flaws — CVE-2026-81578 (missing '
  'authentication for a critical function) and CVE-2026-82078 (unsafe reflection). Reporting describes them '
  'being chained to execute code without authentication.</li>')
w('</ul></div>')

w('<h2 class="sec">Sources</h2>')
w('<div class="panel srcs">')
w('Fetched or returned this run: '
  '<a href="https://unit42.paloaltonetworks.com/ai-assisted-cyber-attack-inside-a-unit-42-investigation/">Unit 42 — An AI-Assisted Cyber Attack: Inside a Unit 42 Investigation</a> (primary; carries the “intrusion, not ransomware” correction) · '
  '<a href="https://www.csoonline.com/article/4217976/ai-agents-help-compress-ransomware-intrusion-to-under-10-hours-raising-stakes-for-cisos.html">CSO Online</a> · '
  '<a href="https://cybermagazine.com/news/unit-42-how-ai-agents-breached-a-network-in-10-hours">Cyber Magazine</a> · '
  '<a href="https://databreaches.net/2026/09/03/agentic-ransomware-took-down-enterprise-in-ten-hours-ai-left-80-page-audit/">DataBreaches.net</a> · '
  '<a href="https://thehackernews.com/2026/09/attackers-exploit-two-sonicwall-sma.html">The Hacker News — Attackers Exploit Two SonicWall SMA 1000 Zero-Days</a> · '
  '<a href="https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016">SonicWall PSIRT SNWLID-2026-0016</a> · '
  '<a href="https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog">CISA — Adds Seven Known Exploited Vulnerabilities (returned EMPTY on fetch)</a> · '
  '<a href="https://www.cisa.gov/news-events/alerts/2026/09/04/cisa-adds-one-known-exploited-vulnerability-catalog">CISA — Adds One Known Exploited Vulnerability, Sept 4</a> · '
  '<a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">CISA KEV catalog</a> · '
  '<a href="https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html">The Hacker News — CISA Adds Seven Exploited Flaws</a> · '
  '<a href="https://www.techtimes.com/articles/326749/20260905/chrome-patches-sixth-zero-day-2026-v8-compiler-exploit-hits-wild.htm">TechTimes — Chrome patches sixth zero-day of 2026</a> · '
  '<a href="https://vulnerability.circl.lu/vuln/CVE-2026-85046">CIRCL Vulnerability-Lookup — CVE-2026-85046</a> · '
  '<a href="https://www.securityweek.com/mckesson-confirms-data-breach-as-attacker-deadline-looms/">SecurityWeek — McKesson Confirms Data Breach</a> · '
  '<a href="https://www.bleepingcomputer.com/news/security/mckesson-discloses-breach-after-shinyhunters-claims-patient-data-theft/">BleepingComputer — McKesson discloses breach</a> · '
  '<a href="https://www.helpnetsecurity.com/2026/08/31/healthcare-company-mckesson-data-breach/">Help Net Security</a> · '
  '<a href="https://cybernews.com/news/mckesson-breached-shinyhunters-claims-284m-records/">Cybernews</a> · '
  '<a href="https://techcrunch.com/2026/07/07/the-worst-hacks-and-breaches-of-2026-so-far/">TechCrunch — worst hacks and breaches of 2026 so far</a>.')
w('</div>')

w('<div class="disc"><strong>Method:</strong> every claim above traces to a source fetched this run or to a '
  'sourced entry in this desk’s standing corrections file. Attacker claims are labelled as claims. Where a '
  'primary source and its secondary coverage disagree, both are shown and the primary is followed. This page '
  'is a news summary for general awareness, not security advice or an authoritative advisory — always act on '
  'the vendor bulletin and the CISA KEV catalog directly.</div>')

html = shared.page("The Cyber Wire — Daily Security Briefing", css, b.getvalue())
open("/tmp/build_1788656196/out/cyber-briefing.html","w",encoding="utf-8").write(html)
print("cy bytes", len(html), "days left", LEFT)
