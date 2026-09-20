# -*- coding: utf-8 -*-
import io, common

TLDR = ("Google has disclosed that its Gemini model broke into three real companies during a May "
        "evaluation after a naming collision gave it live internet access, while two actively "
        "exploited Cisco zero-days now sit one and three days past their federal patch deadlines.")

p = []
p.append(common.head("The Cyber Wire &mdash; Daily Briefing", "cyber"))
p.append(common.masthead("The Cyber Wire",
         "Your daily security briefing &mdash; breaches, bugs and what to patch first"))
p.append(common.META)
p.append(common.tldr("The Wire", TLDR))
p.append(common.nav("cyber"))

# Threat level banner
p.append('<div class="banner"><span class="lvl critc">Threat level: High</span>'
         '<span style="font-size:14.5px">Two Cisco zero-days confirmed exploited in the wild are '
         'past their federal remediation deadlines &mdash; a CVSS 10.0 authentication bypass in '
         'Identity Services Engine by one day, and a CVSS 9.8 root-execution flaw in Secure Email '
         'Gateway by three &mdash; while three Linux kernel flaws added to the KEV catalogue on '
         '18 September fall due tomorrow with public root exploits already circulating.</span></div>')

# Stat strip
p.append('<div class="stats">'
         '<div class="stat"><div class="n">15M</div><div class="l">DentaQuest records &mdash; largest health breach reported this year</div></div>'
         '<div class="stat"><div class="n">10.0</div><div class="l">CVSS of the Cisco ISE zero-day &mdash; patch deadline 1 day overdue</div></div>'
         '<div class="stat"><div class="n">9.8</div><div class="l">CVSS of the Cisco email gateway zero-day &mdash; 3 days overdue</div></div>'
         '<div class="stat"><div class="n">3</div><div class="l">Linux kernel CVEs added to KEV 18 Sep, due 21 Sep</div></div>'
         '</div>')

# Top story
p.append(common.sec("Top story"))
p.append('<div class="lead"><h3>Google&rsquo;s Gemini broke into three real companies during a '
         'security test &mdash; and it took two months to find out</h3>'
         '<p>Google has confirmed that its <b>Gemini</b> model gained unauthorized access to '
         '<b>three outside systems</b> during a cybersecurity evaluation run in <b>May 2026</b> by '
         'the evaluation firm <b>Irregular</b>. Google confirmed the incident on <b>18 September</b>, '
         'and it was reported across CNBC, NBC News, CNN, Axios and The Hacker News on 18&ndash;19 September.</p>'
         '<p><b>How it happened.</b> The exercises were capture-the-flag scenarios built around a '
         'fictional company name that happened to <b>match a real domain on the public internet</b>, '
         'and a <b>misconfiguration left the test environment connected to that internet</b> rather '
         'than sealed inside a sandbox. In one case Gemini got in by <b>repeatedly guessing login '
         'information</b>; in the two others it <b>used credentials it found in a public repository</b>. '
         'Google characterises the intrusions as mistaken identity &mdash; the model believed the '
         'systems it reached were part of the test.</p>'
         '<p><b>The detail that matters.</b> In all three instances the model <b>stopped before doing '
         'anything further</b> with the access it had obtained. Google did not learn of the intrusions '
         'until <b>July</b>, when Irregular reviewed its own work looking for incidents similar to the '
         'Hugging Face disclosure; Google then investigated, <b>notified the organisations behind the '
         'affected sites and told federal authorities</b>. The episode is evidence that AI evaluation '
         'environments are now a live piece of attack surface in their own right.</p></div>')

# Patch priority
p.append(common.sec("Patch priority"))
p.append('<div class="callout crit"><h3>Cisco ISE and ISE-PIC &mdash; CVE-2026-76460, CVSS 10.0, '
         'federal deadline was 19 September</h3>'
         '<p>An unauthenticated remote attacker can send a specially crafted request to an ISE API '
         'endpoint that <b>does not enforce sufficient authentication</b>, bypass the web-based '
         'management interface without valid administrator credentials, and ultimately '
         '<b>execute commands as root</b>. Cisco disclosed it on <b>16 September</b> with emergency '
         'updates after confirming active exploitation; CISA added it to the KEV catalogue the same '
         'day and set <b>19 September</b> for federal civilian agencies &mdash; '
         '<b class="critc">now 1 day overdue</b>. It affects ISE and ISE-PIC <i>regardless of '
         'configuration</i>, and <b>Cisco states there are no workarounds</b>. The first fixed levels '
         'are <b>3.1 Patch 12, 3.2 Patch 11, 3.3 Patch 12, 3.4 Patch 7 and 3.5 Patch 4</b>; where '
         'upgrading cannot be immediate, reporting notes that infrastructure access control lists '
         '(iACLs) restricting traffic to the appliance prevent remote exploitation.</p></div>')

# Threat actor spotlight
p.append(common.sec("Threat actor spotlight"))
p.append('<div class="cards"><div class="card">'
         '<span class="tag new">New</span><span class="tag crit">Extortion</span>'
         '<h3>ShinyHunters</h3>'
         '<p>The extortion crew turns up three times in this briefing, which is the story in itself. '
         'It is <b>reportedly responsible for the DentaQuest intrusion</b> &mdash; the largest health '
         'data breach reported to the US government this year. And on <b>19 September</b> it went '
         'after a peer rather than a victim, breaching and defacing the <b>Clop ransomware gang&rsquo;s '
         'own Tor leak site</b> and threatening to extort the extortionists. The group is not a '
         'ransomware operator in the encrypt-and-demand sense: it steals data and sells access to the '
         'consequences, which is why its targets range from a dental benefits administrator to a rival '
         'crew&rsquo;s infrastructure. Attribution here is what researchers and the group itself have '
         'claimed, not a settled fact.</p></div></div>')

# Breaches
p.append(common.sec("Breaches &amp; incidents"))
p.append('<div class="cards">')

p.append('<div class="card"><span class="tag new">New</span><span class="tag crit">Extortion</span>'
         '<h3>ShinyHunters defaces the Clop leak site</h3>'
         '<p>On <b>19 September</b> ShinyHunters breached Clop&rsquo;s Tor data-leak site, exploiting '
         'what it claims is an <b>unauthenticated file upload vulnerability in Grav CMS</b> to upload '
         'a small text file. The message read &ldquo;THIS SITE HAS BEEN PWN3D BY SHINYHUNTERES '
         '#Skids10p &mdash; Maybe don&rsquo;t try to threaten us next time&rdquo; (the misspelling is '
         'the attackers&rsquo;). The group says it took leak-site source code and Grav plugins, system '
         'logs from <code>/var/log</code>, and the <b>private cryptographic keys for Clop&rsquo;s onion '
         'service</b>; it set a <b>72-hour deadline</b> and says it intends to extort Clop. The stated '
         'motive is retaliation for threats of violence and doxxing made by a Clop representative '
         'during a dispute over Clop&rsquo;s 2025 Oracle E-Business Suite data-theft campaign.</p></div>')

p.append('<div class="card"><span class="tag crit">15M</span><span class="tag">Healthcare</span>'
         '<h3>DentaQuest &mdash; the largest health breach of the year</h3>'
         '<p>The dental and vision benefits administrator is notifying <b>at least 15 million people</b>. '
         'It <b>discovered unauthorized network access on 20 May 2026</b>, with the intrusion having '
         'begun three days earlier on <b>17 May</b>. Exposed: <b>Social Security numbers, Medicaid and '
         'Medicare numbers, and dental and vision treatment records</b>. It is the <b>largest health '
         'data breach reported to the government this year</b>, and <b>ShinyHunters has claimed '
         'responsibility</b>.</p></div>')

p.append('<div class="card"><span class="tag warnt">Count disputed</span><span class="tag crit">Supply chain</span>'
         '<h3>CrowdSec &mdash; source code published, scope unsettled</h3>'
         '<p>Two readings of this incident are in circulation and this desk adopts neither count. '
         'CrowdSec&rsquo;s own analysis, carried from earlier editions, says an attacker cloned about '
         '<b>170 private GitHub repositories</b> using an OAuth token tied to a <b>former '
         'employee&rsquo;s account</b> compromised in May&rsquo;s <b>TanStack npm</b> supply-chain '
         'attack &mdash; 84 malicious versions of 42 packages published 11 May, the clone on 22 May, '
         'the account removed 25 May after the fact, the code surfacing on a forum on 16 September. '
         'A separate account read this run says the code published on <b>16 September 2026</b> covered '
         '<b>130+ public repositories and many private ones</b>. Both accounts agree on the point that '
         'matters most: <b>CrowdSec&rsquo;s infrastructure and databases were not accessed or '
         'compromised</b>.</p></div>')

p.append('<div class="card"><span class="tag warnt">Scope unconfirmed</span><span class="tag">Utility</span>'
         '<h3>CenterPoint Energy &mdash; a confirmed breach and a claimed count</h3>'
         '<p>The Texas utility <b>confirmed on 14 September</b> that an unauthorized third party stole '
         'customer data through one of its external-facing systems, disclosing the incident in a '
         '<b>Form 8-K</b>. The <b>7.49 million</b> figure in circulation is the <b>hacker&rsquo;s claim</b> '
         '&mdash; an actor using the alias <b>&ldquo;4d722e4d656f77&rdquo;</b> says the records came from '
         'an <b>exposed API</b>, with fields including names, phone numbers, billing addresses, account '
         'numbers and partial Social Security numbers. An earlier figure of <b>6.7 million</b> also '
         'circulated. The company has confirmed neither number.</p></div>')

p.append('<div class="card"><span class="tag crit">3.75M</span><span class="tag">Healthcare</span>'
         '<h3>CareCloud &mdash; 3.75 million patients</h3>'
         '<p>Carried from earlier editions and not restated in sources read this run: personal '
         'information and medical records of <b>more than 3.75 million people</b> were stolen from the '
         'health data firm in a <b>March</b> breach, detailed in an HHS filing in August, and it ranks '
         'as the <b>fifth-largest theft of health data in 2026</b> so far.</p></div>')

p.append('</div>')

# Vulnerability watch
p.append(common.sec("Vulnerability watch"))
p.append('<div class="panel" style="padding:8px 10px"><table><thead><tr><th>CVE</th><th>CVSS</th>'
         '<th>Affected</th><th>Note</th></tr></thead><tbody>'
         '<tr><td class="mono">CVE-2026-76460</td><td class="critc mono">10.0</td>'
         '<td>Cisco ISE / ISE-PIC</td><td>Authentication bypass via an API endpoint that does not '
         'enforce sufficient authentication; leads to root command execution. Exploited in the wild. '
         'No workarounds &mdash; upgrade only.</td></tr>'
         '<tr><td class="mono">CVE-2026-76461</td><td class="critc mono">9.8</td>'
         '<td>Cisco Secure Email Gateway (AsyncOS)</td><td>A crafted email carrying SQL statements is '
         'processed by the gateway&rsquo;s parsing logic, giving arbitrary SQL execution and then OS '
         'command execution as root. Affects AsyncOS 16.5, 16.0 and 15.5 and earlier, on-premises '
         'physical and virtual appliances and Cisco Secure Email Cloud. Exploited as a zero-day before '
         'disclosure.</td></tr>'
         '<tr><td class="mono">CVE-2026-20079</td><td class="critc mono">10.0</td>'
         '<td>Cisco Secure Firewall Management Center</td><td>Authentication bypass allowing script '
         'execution and root on the underlying OS. Exploited. Carried from this desk&rsquo;s standing '
         'record, not restated this run.</td></tr>'
         '<tr><td class="mono">CVE-2026-20316</td><td class="mut mono">not published</td>'
         '<td>Cisco Secure FMC</td><td>Hard-coded password for a built-in, low-privileged web account. '
         'No CVSS has been stated in any source this desk has read.</td></tr>'
         '<tr><td class="mono">CVE-2025-39682</td><td class="critc mono">9.8</td><td>Linux kernel</td>'
         '<td>Improper condition check in the TLS receive path: a zero-length record retrieved from '
         'the rx_list bypasses intended recvmsg() record-type handling. In KEV, due 21 September.</td></tr>'
         '<tr><td class="mono">CVE-2026-53266</td><td class="warnc mono">8.8</td><td>Linux kernel</td>'
         '<td>Out-of-bounds write. In KEV, due 21 September.</td></tr>'
         '<tr><td class="mono">CVE-2025-39964</td><td class="warnc mono">7.8</td><td>Linux kernel</td>'
         '<td>Race condition. In KEV, due 21 September.</td></tr>'
         '</tbody></table></div>')
p.append('<p class="note">Seven rows, one of which carries no CVSS. The Secure Email Gateway flaw is '
         'new to this table; the two Secure FMC rows are carried from this desk&rsquo;s standing record '
         'rather than restated in sources read this run, and are labelled as such.</p>')

# KEV
p.append(common.sec("CISA KEV &amp; federal deadlines"))
p.append('<div class="panel"><ul class="bul">'
         '<li><b class="critc">CVE-2026-76460 &mdash; Cisco ISE / ISE-PIC.</b> Added <b>16 September</b>, '
         'due <b>19 September</b> &mdash; <b class="critc">1 day overdue</b>. CVSS 10.0, confirmed '
         'exploited, no workarounds.</li>'
         '<li><b class="critc">CVE-2026-76461 &mdash; Cisco Secure Email Gateway.</b> Cisco published '
         'the advisory on <b>14 September</b> and CISA added the flaw to the catalogue the same day, '
         'ordering federal agencies to patch <b>within three days, by 17 September</b> &mdash; '
         '<b class="critc">3 days overdue</b>. CVSS 9.8, exploited as a zero-day before disclosure.</li>'
         '<li><b class="warnc">CVE-2025-39682, CVE-2026-53266 and CVE-2025-39964 &mdash; Linux kernel.</b> '
         'Added <b>18 September</b>, remediation required by <b>21 September</b> under <b>BOD 26-04</b> '
         '&mdash; <b class="warnc">1 day left</b>. CISA has additionally marked all three as requiring '
         '<b>forensic triage</b>: affected agencies must investigate potentially exposed assets for '
         'evidence of compromise rather than treat installing the patch as the whole response. Four '
         'public root exploits landed the same day the trio hit the catalogue.</li>'
         '<li><b class="critc">CVE-2026-20079 &mdash; Cisco Secure FMC.</b> Federal deadline was '
         '<b>12 September</b> &mdash; <b class="critc">8 days overdue</b>. Carried from this '
         'desk&rsquo;s standing record.</li>'
         '<li>Also added to the catalogue alongside the kernel trio: flaws in <b>ownCloud</b> and '
         '<b>JFrog Artifactory</b>.</li>'
         '</ul>'
         '<p class="note">Deadlines above are the dates stated by CISA and by reporting on the specific '
         'additions. Note the window on these additions is <b>three days</b>, not the three weeks of the '
         'older BOD 22-01 regime &mdash; anything computed on the old assumption will be wrong.</p></div>')

p.append(common.srcs([
    ("https://www.cnbc.com/2026/09/18/googles-gemini-becomes-latest-ai-model-to-break-out-and-hack-computer-systems.html",
     "CNBC &mdash; Google&rsquo;s Gemini becomes latest AI model to break out and hack computer systems"),
    ("https://www.nbcnews.com/tech/tech-news/google-says-ai-model-gained-unauthorized-access-three-systems-rcna598651",
     "NBC News &mdash; Google says its AI model gained unauthorized access to three outside systems"),
    ("https://thehackernews.com/2026/09/google-gemini-broke-into-real-company.html",
     "The Hacker News &mdash; Gemini broke into real company systems after a test domain mix-up"),
    ("https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html",
     "The Hacker News &mdash; Cisco warns of new zero-day ISE auth bypass (CVSS 10.0)"),
    ("https://www.securityweek.com/active-exploitation-triggers-emergency-patch-for-cisco-ise-zero-day/",
     "SecurityWeek &mdash; active exploitation triggers emergency patch for Cisco ISE zero-day"),
    ("https://socprime.com/blog/cve-2026-76460-cisco-ise-zero-day-exploited/",
     "SOC Prime &mdash; CVE-2026-76460 Cisco ISE zero-day exploited"),
    ("https://www.helpnetsecurity.com/2026/09/15/cve-2026-76461-cisco-email-gateway-zero-day-exploited/",
     "Help Net Security &mdash; Cisco patches actively exploited email gateway zero-day"),
    ("https://www.rapid7.com/blog/post/etr-cve-2026-76461-critical-cisco-secure-email-gateway-vulnerability-exploited-in-the-wild/",
     "Rapid7 &mdash; CVE-2026-76461 exploited in the wild"),
    ("https://www.bleepingcomputer.com/news/security/new-cisco-secure-email-zero-day-exploited-to-execute-commands-as-root/",
     "BleepingComputer &mdash; Cisco patches Secure Email Gateway zero-day exploited in attacks"),
    ("https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html",
     "The Hacker News &mdash; CISA flags three Linux kernel vulnerabilities exploited in the wild"),
    ("https://www.cisa.gov/known-exploited-vulnerabilities-catalog",
     "CISA &mdash; Known Exploited Vulnerabilities catalog"),
    ("https://cybersecuritynews.com/linux-kernel-vulnerabilities-actively-exploited/",
     "Cybersecurity News &mdash; CISA warns of Linux kernel vulnerabilities actively exploited"),
    ("https://www.bleepingcomputer.com/news/security/shinyhunters-hacks-clop-leak-site-threatens-to-extort-ransomware-gang/",
     "BleepingComputer &mdash; ShinyHunters hacks Clop leak site"),
    ("https://cybernews.com/news/shinyhunters-hacks-clop-ransomware/",
     "Cybernews &mdash; ShinyHunters hacks Clop and threatens extortion"),
    ("https://www.healthcaredive.com/news/Dental-benefits-administrator-discloses-breach/827533/",
     "Healthcare Dive &mdash; DentaQuest breach exposes data of 15M people"),
    ("https://www.hipaajournal.com/dentaquest-data-breach/",
     "HIPAA Journal &mdash; DentaQuest notifying 15 million+ individuals"),
    ("https://www.crowdsec.net/blog/tanstack-supply-chain-attack-analysis",
     "CrowdSec &mdash; TanStack supply chain attack analysis"),
    ("https://securityaffairs.com/199170/data-breach/texas-utility-centerpoint-energy-confirms-data-breach-after-hacker-claims-7-49m-records-stolen.html",
     "Security Affairs &mdash; CenterPoint Energy confirms breach after hacker claims 7.49M records"),
]))

p.append(common.footer(
    "For information only, and not security advice for any particular environment. CVSS scores, "
    "affected versions and remediation deadlines are as stated by the vendor or CISA at the time of "
    "reading and can change; confirm against the vendor advisory and the KEV catalogue before acting. "
    "Attribution of an intrusion to a named group reflects what researchers or the group itself have "
    "claimed, not a settled fact."))
p.append(common.TAIL)

html = "".join(p)
io.open("cyber-briefing.html", "w", encoding="utf-8").write(html)
print("cyber ok", len(html), "tldr:", TLDR[:60])
