# -*- coding: utf-8 -*-
import io, common_r4 as C

OUT = "/sessions/youthful-bold-tesla/mnt/outputs/cyber-briefing.html"

TLDR = ("Federal agencies reach today&rsquo;s deadline on three actively exploited Linux kernel flaws, "
        "and Japan&rsquo;s Helpfeel has confirmed that an attacker who exploited its Gyazo image-upload "
        "server took 23.62 million user records.")

BANNER = ('<div class="banner" style="border-left:4px solid var(--crit)">'
 '<span class="lvl critc">Threat Level: High</span>'
 '<span style="font-size:14.5px">Three actively exploited Linux kernel flaws hit their federal remediation '
 'deadline <b>today</b> and require forensic triage, while two Cisco zero-days are already past theirs.</span></div>')

STATS = [("23.62M","Gyazo user records stolen"),
         ("490M","image metadata records exposed"),
         ("108","ClickFix ads in 48 hours from a hijacked verified account"),
         ("0 days","left on the Linux kernel KEV trio")]

TOP = ('<div class="lead"><h3>Helpfeel confirms a Gyazo breach: 23.62 million user records and metadata on '
 'hundreds of millions of images</h3>'
 '<p>Japanese software company <b>Helpfeel</b> has confirmed a data breach on its screenshot-sharing platform '
 '<b>Gyazo</b>, in which an attacker exploited a vulnerability in the image upload server to gain unauthorised '
 'access and run arbitrary commands. The company says the flaw was exploited on <b>11 September</b>; suspicious '
 'activity was detected that same evening, and by the early hours of <b>12 September</b> the access routes had been '
 'blocked and the attacker&rsquo;s connections cut off.</p>'
 '<p>The stolen user records &mdash; about <b>23.62 million</b> of them &mdash; include names, email addresses, '
 '<b>password hashes</b>, user IDs, device IDs, <b>login session IDs</b>, X integration tokens for connected '
 'accounts, Google SSO email addresses, profile information, language preferences, registration and login '
 'timestamps, subscription plans and billing status. Helpfeel says no payment information, including credit card '
 'numbers, was disclosed.</p>'
 '<p>The image metadata is larger in scope: approximately <b>490 million records</b>, tied mostly to images uploaded '
 'in or before <b>January 2019</b> &mdash; about <b>14.4%</b> of all image data on the platform. A further '
 '<b>2.4 million images</b> were separately pulled through specific filtering. That metadata included image IDs used '
 'to build image URLs, upload IP addresses, user agents, <b>EXIF location data</b> where present, <b>OCR text '
 'extracted from images</b>, image titles, source URLs and hashed passphrases protecting private images. The company '
 'has also confirmed the third party obtained <b>a list identifying private images</b> and cannot rule out that some '
 'were viewed.</p>'
 '<p>Helpfeel reported the incident to Japan&rsquo;s <b>Personal Information Protection Commission</b> on '
 '<b>15 September</b> and plans to notify affected users by email, and through the Gyazo web interface for anonymous '
 'accounts with no registered address. It found no sign data was taken from its other two services, Helpfeel and '
 'Cosense. <b>&ldquo;We ask all Gyazo users to change their passwords,&rdquo;</b> the notice reads, extending the '
 'same advice to any other account sharing the same or a similar password. At the time of writing Gyazo&rsquo;s '
 'homepage still showed a maintenance notice with no timeline for the service&rsquo;s return.</p></div>')

PATCH = ('<div class="callout crit"><h3 class="critc">Patch Priority &mdash; deadline is today</h3>'
 '<p>The single most urgent item for defenders today is <b>CVE-2025-39682</b>, a <b>CVSS 9.8</b> improper-condition '
 'check in the <b>Linux kernel&rsquo;s kTLS receive path</b>, in which a zero-length record retrieved from the '
 '<code>rx_list</code> bypasses intended <code>recvmsg()</code> record-type handling. CISA added it, together with '
 '<b>CVE-2026-53266</b> and <b>CVE-2025-39964</b>, on <b>18 September</b>; under BOD 26-04 the fixes are due '
 '<b>21 September &mdash; today</b>. All three are marked as requiring <b>forensic triage</b>, meaning affected '
 'agencies must investigate potentially exposed assets for evidence of compromise rather than treating patch '
 'installation as the only response. A vulnerability brief for today also lists <b>CVE-2026-76460</b> in Cisco '
 'Identity Services Engine among the CVEs under confirmed active exploitation; its federal deadline passed on '
 '19 September.</p></div>')

SPOT = ('<div class="cards"><div class="card" style="border-left:3px solid var(--acc)">'
 '<span class="tag acc">Threat actor</span><h3>The PasteSwitch operators</h3>'
 '<p>The crew behind the HBO Max Reddit hijack runs what Hudson Rock and ADAMnetworks describe as a <b>cross-platform '
 'delivery operation</b> spanning MacSync, AMOS, Amatera, fake wallet apps and contract-controlled cryptocurrency '
 'clippers. Visitors are <b>fingerprinted before anything malicious is shown</b> &mdash; depending on browser, screen '
 'and device signals, some get the lure and a malicious command while others see a blank page, a redirect to a '
 'legitimate vendor site, or unrelated content, which keeps automated scanning from catching the pattern '
 'consistently. Their clippers, <b>AnimateClipper</b> and <b>ZigClipper</b>, store the attacker&rsquo;s wallet '
 'address <b>inside smart contracts on the Binance Smart Chain</b> rather than at a fixed C2 domain; between '
 '<b>March and July 2026</b> researchers observed <b>36 mainnet changes</b> executed by the same controller address, '
 'letting the operators rotate burned domains without registering new ones. &ldquo;The threat actors squeezed as much '
 'value as possible out of the verified account&rsquo;s status, pivoting quickly when domains were burned,&rdquo; '
 'Hudson Rock said.</p></div></div>')

INCIDENTS = [
 ("HBO Max&rsquo;s verified Reddit account pushed 108 malware ads", "acc", "Malvertising",
  "Attackers compromised <b>u/hbomax</b>, the verified official HBO Max Reddit account, and used its trusted "
  "advertising status for a ClickFix campaign against macOS and Windows. Over <b>48 hours</b> the account pushed "
  "<b>108 distinct ads</b>: <b>46</b> used an HBO Max lure, <b>36</b> posed as OpenAI Codex, <b>15</b> advertised a "
  "fake macOS disk utility and <b>11</b> other developer tools. On macOS the commands piped <code>curl</code> output "
  "into <code>zsh</code>, delivering <b>MacSync</b> (browser credentials, Gecko profiles, Telegram data, Apple Notes "
  "and macOS passwords, staged in a hidden zip), <b>AMOS Helper</b> (persistent background process disguised as a "
  "system service) and fake <b>Ledger, Trezor Suite and Exodus</b> apps built to harvest 12- and 24-word BIP39 "
  "recovery phrases. Windows visitors went through <code>mshta</code> and PowerShell to an in-memory loader that "
  "installed <b>Amatera</b>. Reddit has paused the ads and secured the account."),
 ("AnMed closes dozens of medical offices after a weekend attack", "crit", "Healthcare",
  "<b>AnMed</b>, a nonprofit health system serving upstate South Carolina and northeast Georgia, temporarily closed "
  "dozens of its medical offices and other care facilities while responding to a weekend attack, per a "
  "<b>18 September</b> entry in the ransomware tracking listings read this run. No ransomware family, patient-record "
  "count or restoration timeline is stated in anything read this run, so none is printed here."),
 ("A Settra cluster hit three North American firms on the same day", "warnt", "Ransomware",
  "The <b>Settra</b> group is listed as having hit <b>Hansler Smith Limited</b> and <b>Teletek Structures Inc.</b>, "
  "both Canadian, and <b>MedEvolve</b>, a U.S. medical billing company, all on <b>4 September 2026</b>, with threats "
  "to leak data unless demands are met. Separate 4 September entries name <b>Engefitas</b> (Brazil, Vexy ransomware) "
  "and <b>Petrocare Construction</b> (Canada, Storm). These are victim-listing entries, not company confirmations, "
  "and are presented as such."),
 ("Plugin4Shell: zero-click RCE in four AI coding agents, two still unpatched", "acc", "Supply chain",
  "A zero-click remote-code-execution flaw hit four major AI coding agents, and <b>two remain unpatched</b> &mdash; "
  "the framing in a Help Net Security headline still carried on the site today. From this desk&rsquo;s standing "
  "ledger: the technique is pinned-commit plugin substitution; <b>Claude Code 2.1.179</b> and <b>Codex 0.146.0</b> "
  "are patched, <b>GitHub Copilot</b> has no fix, and <b>Gemini CLI will not be patched</b> because it is being "
  "retired. Those version details are carried, not restated this run."),
]

VULNS = [
 ("CVE-2025-39682","9.8","Linux kernel (kTLS receive path)","KEV 18 Sep &middot; due <b>21 Sep &mdash; today</b> &middot; forensic triage. Zero-length rx_list record bypasses recvmsg() record-type handling."),
 ("CVE-2026-53266","8.8","Linux kernel (netfilter bridge ebtables SNAT)","KEV 18 Sep &middot; due <b>21 Sep &mdash; today</b> &middot; out-of-bounds write."),
 ("CVE-2025-39964","7.8","Linux kernel (AF_ALG socket)","KEV 18 Sep &middot; due <b>21 Sep &mdash; today</b> &middot; race condition on concurrent writes; crash or corrupted cryptographic results."),
 ("CVE-2026-76460","10.0","Cisco Identity Services Engine / ISE-PIC","KEV 16 Sep &middot; due 19 Sep &mdash; <b class=\"critc\">2 days overdue</b>. Listed again today among CVEs under confirmed active exploitation. Score and fixed versions carried from the standing ledger."),
 ("CVE-2026-76461","9.8","Cisco Secure Email Gateway","KEV 14 Sep &middot; due 17 Sep &mdash; <b class=\"critc\">4 days overdue</b>. <span class=\"mut\">Carried from the standing ledger; not restated in anything read this run.</span>"),
 ("CVE-2026-94097","10.0","Netcore NBR200V2 router","One of five critical Netcore entries in today&rsquo;s disclosure brief. No exploitation claimed."),
 ("CVE-2026-55366","9.8","Google Android","Today&rsquo;s disclosure brief. No exploitation claimed."),
 ("CVE-2026-86462","9.1","Apache Airflow FAB provider","Today&rsquo;s disclosure brief; the authentication layer is the exposed component."),
 ("CVE-2026-58704","not stated","Google Pixel","Named today among six CVEs carrying confirmed active exploitation. No CVSS appears in anything read this run, so none is printed."),
]

KEV = [
 "<b>Linux kernel trio &mdash; due today, 0 days left.</b> <b>CVE-2025-39682</b>, <b>CVE-2026-53266</b> and "
 "<b>CVE-2025-39964</b> were added on <b>18 September</b> with remediation required by <b>21 September</b> under "
 "<b>BOD 26-04: Prioritizing Security Updates Based on Risk</b>. All three are marked as requiring forensic triage.",
 "<b>Cisco Identity Services Engine &mdash; CVE-2026-76460, 2 days overdue.</b> Added 16 September, due "
 "<b>19 September</b>. Today&rsquo;s vulnerability brief still lists it among the CVEs under confirmed active "
 "exploitation.",
 "<b>Cisco Secure Email Gateway &mdash; CVE-2026-76461, 4 days overdue.</b> Added 14 September, due "
 "<b>17 September</b>. Carried from this desk&rsquo;s standing ledger; not restated in anything read this run.",
 "<b>September&rsquo;s KEV cadence, verified this run.</b> <b>2 Sep</b>: seven added, including Sangoma Switchvox, "
 "Kludex Starlette, Kestra OSS, BerriAI LiteLLM, JFrog Artifactory and SonicWall SMA1000. <b>9 Sep</b>: four, "
 "including Fortinet, Citrix NetScaler, Google Chromium V8 and Cisco Firewall Management Center. <b>11 Sep</b>: one, "
 "<b>CVE-2026-85706</b> in GitLab. <b>16 Sep</b>: two, in Cisco Identity Services Engine and Acronis Backup.",
 "<b>Neither Acronis Backup&rsquo;s CVE nor today&rsquo;s brief-only CVEs carry a federal deadline here.</b> No due "
 "date for the Acronis entry appears in anything read this run, so none is asserted; the Netcore, Android, Airflow "
 "and Pixel entries above are disclosure-brief items and are not stated to be in KEV.",
]

SRC = [
 ("https://www.helpnetsecurity.com/2026/09/21/helpfeel-gyazo-data-breach/",
  "Help Net Security &mdash; Hackers exploit Gyazo server flaw to steal 23.6 million user records (21 Sep, fetched in full)"),
 ("https://corp.helpfeel.com/en/news/news-20260916", "Helpfeel &mdash; incident notice"),
 ("https://www.helpnetsecurity.com/2026/09/15/hbo-max-reddit-account-clickfix-infostealer-malware/",
  "Help Net Security &mdash; Attackers hijack HBO Max&rsquo;s Reddit account for a 48-hour malvertising blitz (fetched in full)"),
 ("https://www.hudsonrock.com/blog/hbo-max-ads-on-a-compromised-reddit-account-exposed-a-massive-pasteswitch-clickfix-operation",
  "Hudson Rock &mdash; PasteSwitch ClickFix operation"),
 ("https://adamnet.works/blog/hbo-max-ads-exposed-the-pasteswitch-clickfix-operation/",
  "ADAMnetworks &mdash; following the copied command"),
 ("https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html",
  "The Hacker News &mdash; CISA flags three Linux kernel vulnerabilities exploited in the wild"),
 ("https://www.cisa.gov/known-exploited-vulnerabilities-catalog", "CISA &mdash; Known Exploited Vulnerabilities Catalog"),
 ("https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-two-known-exploited-vulnerabilities-catalog",
  "CISA &mdash; adds two KEVs, 16 September"),
 ("https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog",
  "CISA &mdash; adds seven KEVs, 2 September"),
 ("https://cvebrief.com/archive/2026/09/21/", "CVE Brief &mdash; 21 September 2026"),
 ("https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/",
  "Help Net Security &mdash; Plugin4Shell in four AI coding agents"),
 ("https://www.ransomware.live/", "Ransomware.live &mdash; victim listings"),
]

b = []
b.append(C.head("The Cyber Wire &mdash; Daily Cybersecurity Briefing", "cyber"))
b.append(C.masthead("The Cyber Wire", "Your daily cybersecurity briefing &mdash; breaches, bugs and the people behind them"))
b.append(C.META)
b.append(C.tldr("The Wire", TLDR))
b.append(C.nav("cyber"))
b.append(BANNER)
b.append('<div class="stats">')
for n, l in STATS:
    b.append('<div class="stat"><div class="n">%s</div><div class="l">%s</div></div>' % (n, l))
b.append('</div>')
b.append(C.sec("Top Story"))
b.append(TOP)
b.append(C.sec("Patch Priority"))
b.append(PATCH)
b.append(C.sec("Threat Actor Spotlight"))
b.append(SPOT)
b.append(C.sec("Breaches &amp; Incidents"))
b.append('<div class="cards">')
for title, tag, tagtxt, body in INCIDENTS:
    newtag = '<span class="tag new">New</span>' if title.startswith(("AnMed", "A Settra")) else ''
    b.append('<div class="card">%s<span class="tag %s">%s</span><h3>%s</h3><p>%s</p></div>'
             % (newtag, tag, tagtxt, title, body))
b.append('</div>')
b.append('<p class="note">Only the two items tagged New were absent from the previous archived edition; the HBO Max '
         'and Plugin4Shell cards carried over and are not tagged.</p>')
b.append(C.sec("Vulnerability Watch"))
b.append('<div class="panel"><table><tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>')
for cve, score, aff, note in VULNS:
    b.append('<tr><td class="mono">%s</td><td class="mono">%s</td><td>%s</td><td class="mut">%s</td></tr>'
             % (cve, score, aff, note))
b.append('</table><p class="note">Today&rsquo;s disclosure brief records <b>87 total disclosures</b>, of which '
         '<b>15</b> are critical, <b>72</b> high priority and <b>6</b> carry confirmed active exploitation. Its page '
         'returned empty on direct fetch, so the figures above are taken from the brief&rsquo;s own summary text as '
         'read this run.</p></div>')
b.append(C.sec("CISA KEV &amp; Federal Deadlines"))
b.append('<div class="panel"><ul class="bul">')
for k in KEV:
    b.append('<li>%s</li>' % k)
b.append('</ul></div>')
b.append(C.srcs(SRC))
b.append(C.footer("Deadlines and CVSS scores should be verified against your own vendor advisories and the CISA KEV "
                  "catalog before you act on them. Where a score, a fixed version or a due date was not stated in a "
                  "source read this run, this page says so rather than supplying one."))
b.append(C.TAIL)

io.open(OUT, "w", encoding="utf-8").write("".join(b))
print("wrote", OUT)
