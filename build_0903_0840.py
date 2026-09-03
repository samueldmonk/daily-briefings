# -*- coding: utf-8 -*-
"""Daily Briefings — Thursday, September 3, 2026 · Morning Edition (~8:40 AM ET, pre-open)."""
import io, os, css

OUT = "/sessions/dreamy-focused-cerf/mnt/outputs"

TV = "https://s3.tradingview.com/external-embedding/embed-widget-%s.js"

def w(name, cfg):
    return '<script src="%s" async>%s</script>' % (TV % name, cfg)

def write(fn, s):
    with io.open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        f.write(s)
    print("wrote", fn, len(s))

# ---------------------------------------------------------------- summaries
SUM_WS = ("Futures are narrowly mixed before the bell &mdash; Dow contracts up about 0.2%, Nasdaq 100 "
          "contracts just below flat &mdash; as Iran's overnight strikes on Jordan, the UAE and Kuwait "
          "keep a war premium in oil and Snowflake holds a pre-market gain of more than 24%.")
SUM_CY = ("A Russian national extradited from Cyprus has been indicted in San Francisco over a campaign "
          "that pushed malware-laced Excel attachments to roughly 80,000 users of a freelance-work "
          "platform, while five of the seven flaws CISA added to its KEV catalog on September 2 come "
          "due for federal agencies on Saturday.")
SUM_MMA = ("UFC 332 still has no announced main event after Valentina Shevchenko withdrew injured, with an "
           "interim women's flyweight title fight between Natalia Silva and Wang Cong reported as the "
           "target &mdash; a pairing coverage says would let Silva avenge a 2015 kickboxing loss.")

FRESH = '<div class="freshline" id="freshline">&nbsp;</div>'

# ================================================================ INDEX
def build_index():
    c = css.base_css("#c9a84c", "#e0c877", "#0d0f12", "#15181d", "#242830")
    extra = """
.hero{display:grid;gap:14px;margin-top:6px}
@media(min-width:820px){.hero{grid-template-columns:repeat(3,1fr)}}
.hcard{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:19px 21px;
  display:flex;flex-direction:column;transition:.18s;border-top:3px solid var(--line)}
.hcard:hover{transform:translateY(-3px);box-shadow:0 10px 26px rgba(0,0,0,.35)}
.hcard .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;margin-bottom:8px}
.hcard h3{font-size:21px;margin:0 0 4px;letter-spacing:-.3px}
.hcard .sub{font-size:12.5px;color:var(--muted);font-family:var(--mono);letter-spacing:.08em;
  text-transform:uppercase;margin-bottom:11px}
.hcard p{font-size:14.5px;color:#cfcdc9;flex:1;margin:0 0 15px}
.hcard a.go{font-family:var(--mono);font-size:11.5px;letter-spacing:.12em;text-transform:uppercase}
.hcard.cy{border-top-color:#22d3a8} .hcard.cy .k,.hcard.cy a.go{color:#22d3a8}
.hcard.cy:hover{border-color:#22d3a8}
.hcard.ws{border-top-color:#caa64a} .hcard.ws .k,.hcard.ws a.go{color:#caa64a}
.hcard.ws:hover{border-color:#caa64a} .hcard.ws h3{font-family:Georgia,'Times New Roman',serif}
.hcard.mm{border-top-color:#e84545} .hcard.mm .k,.hcard.mm a.go{color:#ff8a5c}
.hcard.mm:hover{border-color:#e84545}
"""
    b = []
    b.append(css.head("Daily Briefings", c + extra))
    b.append('<header class="masthead"><h1>Daily Briefings</h1>'
             '<p class="tag">Security, markets and mixed martial arts &mdash; rebuilt from live sources '
             'every 30 minutes, 8 AM&ndash;6 PM ET.</p>' + css.meta_row() + '</header>')
    b.append(FRESH)
    b.append(css.nav("index"))
    b.append('<div class="hero">')
    b.append('<div class="hcard cy"><div class="k">&#9960; The Cyber Wire</div>'
             '<h3>The Cyber Wire</h3><div class="sub">The Wire</div>'
             '<p>%s</p><a class="go" href="cyber-briefing.html">Read the briefing &rarr;</a></div>' % SUM_CY)
    b.append('<div class="hcard ws"><div class="k">&#9650; The Closing Bell</div>'
             '<h3>The Closing Bell</h3><div class="sub">The Tape</div>'
             '<p>%s</p><a class="go" href="wallstreet-briefing.html">Read the briefing &rarr;</a></div>' % SUM_WS)
    b.append('<div class="hcard mm"><div class="k">&#8856; The Octagon</div>'
             '<h3>The Octagon</h3><div class="sub">Tale of the Tape</div>'
             '<p>%s</p><a class="go" href="mma-briefing.html">Read the briefing &rarr;</a></div>' % SUM_MMA)
    b.append('</div>')
    b.append('<div class="note" style="margin-top:22px">Every edition is rebuilt from searches run at '
             'publication time. Figures appear only where a source fetched in that run states them; '
             'disputed readings are printed with their provenance rather than resolved silently. '
             'Point-in-time snapshots of past editions live in the <a href="archive.html">Archive</a>.</div>')
    b.append('<footer><h5>About</h5><ul>'
             '<li>Automated briefing desk &mdash; built and published by a scheduled agent run.</li>'
             '<li>Source lists live at the foot of each individual briefing.</li></ul>'
             '<div class="disc">Information only. Nothing here is investment, security or wagering advice.</div>'
             '</footer>')
    b.append('</div>' + css.STAMP_JS + '</body></html>')
    write("index.html", "\n".join(b))

# ================================================================ CYBER
def build_cyber():
    c = css.base_css("#22d3a8", "#36c6ff", "#0b0f0e", "#121817", "#1f2b28")
    b = []
    b.append(css.head("The Cyber Wire &mdash; Daily Briefing", c))
    b.append('<header class="masthead"><h1>The Cyber Wire</h1>'
             '<p class="tag">&#9960; Your daily cybersecurity briefing &mdash; breaches, exploited bugs '
             'and federal deadlines.</p>' + css.meta_row() + '</header>')
    b.append('<div class="tldr"><b>The Wire</b> <span>%s</span></div>' % SUM_CY)
    b.append(FRESH)
    b.append(css.nav("cyber"))

    b.append('<div class="banner high"><span class="k">Threat level &middot; High</span>'
             'Five actively exploited flaws &mdash; two of them scored CVSS 10.0 &mdash; carry a federal '
             'remediation deadline two days out, a second federal deadline lands eleven days out, and a '
             'critical WordPress upload bug has a public proof of concept.</div>')

    b.append('<div class="stats">'
             '<div class="stat"><div class="n">80,000</div><div class="l">Freelance-platform users sent '
             'malware-laced Excel files in the charged campaign (DOJ)</div></div>'
             '<div class="stat"><div class="n">7</div><div class="l">Flaws added to CISA KEV on Sept 2, '
             'per the CISA alert page</div></div>'
             '<div class="stat"><div class="n">2 days</div><div class="l">Until the Sept 5 federal '
             'deadline for five of the seven</div></div>'
             '<div class="stat"><div class="n">9.0</div><div class="l">CVSS v3.1 of the Elementor Pro '
             'upload flaw CVE-2026-32475</div></div>'
             '</div>')

    b.append('<h2 class="sec">Top Story</h2>')
    b.append('<div class="callout crit"><div class="k">Charged &middot; Northern District of California</div>'
             '<h3>Extradited Russian national indicted over an Excel-macro campaign aimed at 80,000 freelancers</h3>'
             '<p>Federal prosecutors in San Francisco have indicted <b>Searzhudin Tamirlanovich '
             'Aktulaev</b>, 40, over a campaign that the Justice Department says ran from at least June '
             '2016 through November 2017. Aktulaev and co-conspirators allegedly built around <b>255 fake '
             'accounts</b> on a well-known freelance-work platform headquartered in Northern California '
             'and used its messaging system to contact roughly <b>80,000 users</b>, posing as prospective '
             'clients and attaching malicious Microsoft Excel files that prompted the recipient to enable '
             'a macro, which then pulled malware down from the internet.</p>'
             '<p>Two malware families were used: a variant of <b>TVRAT</b> &mdash; also called TVSPY or TeamSpy '
             '&mdash; which abuses TeamViewer for remote control, and <b>DarkVNC</b>, which does the same '
             'through VNC. Both shipped stolen data to a command-and-control server. Roughly half the '
             'victims were in the United States. Aktulaev was arrested in Cyprus in May 2025 and '
             'extradited in August 2026; he faces conspiracy, transmission of a program or code to damage '
             'a protected computer, and aggravated identity theft counts carrying a maximum of <b>20 '
             'years</b>. He is in federal custody with a court appearance set for October 5.</p>'
             '<p class="note">The charged conduct dates to 2016 and 2017. The delivery route has not aged: a '
             'macro-enabled attachment arriving inside a trusted platform\'s own messaging, from an '
             'account that looks like a paying client.</p></div>')

    b.append('<h2 class="sec">Also Leading</h2>')
    b.append('<div class="callout"><div class="k">Seven at once &middot; 2 days left</div>'
             '<h3>Attackers are dropping reverse shells and miners through the newly listed flaws</h3>'
             '<p>CISA added seven security flaws to its Known Exploited Vulnerabilities catalog on '
             'Wednesday, September 2, covering SonicWall, JFrog Artifactory, Sangoma Switchvox, '
             'Starlette, Kestra and LiteLLM. The Hacker News reports attackers weaponising the Switchvox '
             'and Artifactory flaws for administrative access and remote code execution, while Kestra OSS '
             'and LiteLLM are being abused for reverse shells, persistence, credential theft and '
             'cryptocurrency mining.</p>'
             '<p>Federal agencies must remediate Kestra, Artifactory, Switchvox and both SonicWall entries '
             'by <b>September 5, 2026</b>; Starlette and LiteLLM carry a <b>September 16, 2026</b> due '
             'date. That split is consistent with the risk-based assignment CISA has been applying per '
             'CVE rather than a flat three-week window.</p></div>')

    b.append('<h2 class="sec">Patch Priority</h2>')
    b.append('<div class="callout crit"><div class="k">Do this first &middot; 2 days left</div>'
             '<h3>SonicWall SMA1000 &mdash; CVE-2026-83548 (CVSS 10.0), due Saturday, September 5</h3>'
             '<p>An unauthenticated server-side request forgery in the Appliance Work Place interface, '
             'chained with the authenticated OS command-injection flaw CVE-2026-83549 (CVSS 7.8) for '
             'unauthenticated remote code execution. SonicWall says both are exploited in the wild; '
             'Rapid7 MDR discovered the chain. Affected models 6210, 7210 and 8200v; hotfixes '
             '12.4.3-03526 and 12.5.0-02952 and later.</p>'
             '<p>The same September 5 deadline covers JFrog Artifactory (CVE-2026-82329), Sangoma '
             'Switchvox (CVE-2026-9586) and Kestra OSS (CVE-2026-49869) &mdash; the last of which also '
             'carries a CVSS of 10.0 and has been used to plant a cryptocurrency miner. If you triage by '
             'blast radius rather than by score, Artifactory is the one that sits in the software supply '
             'chain.</p>'
             '<p>Behind it, the PaperCut NG/MF pair returns to the board: CVE-2026-81578 and '
             'CVE-2026-82078 were added to KEV on August 31 with a <b>September 14</b> due date, eleven '
             'days out. They chain to let an unauthenticated attacker alter server configuration and '
             'execute Java bytecode as the PaperCut server process.</p></div>')

    b.append('<h2 class="sec">Threat Actor Spotlight</h2>')
    b.append('<div class="cards"><div class="card">'
             '<span class="tag c">Ransomware</span><span class="tag a">New tooling</span>'
             '<h4>The Gentlemen &mdash; and a framework called TukTuk</h4>'
             '<p>Ransomware operators are running a previously undocumented remote-control framework '
             'named TukTuk to steal credentials, watch compromised machines and weaken defences. Cyber '
             'Security News reports the tooling was recovered from a server that also held a malicious '
             'DLL side-loading set, EDR-disabling utilities and data believed taken from two large '
             'organisations, and links the activity to the Gentlemen ransomware operation. The pattern on display is one '
             'intrusion combining access theft, surveillance and defence evasion rather than a '
             'smash-and-grab.</p></div></div>')

    b.append('<h2 class="sec">Breaches &amp; Incidents</h2>')
    b.append('<div class="cards two">')
    b.append('<div class="card"><span class="tag new">New</span><span class="tag c">Zero-day</span>'
             '<h4>PaperCut is on its third emergency patch</h4>'
             '<p>PaperCut Software published an urgent advisory on August 27 saying it was investigating '
             'active exploitation of PaperCut NG and PaperCut MF, and has since shipped emergency patches '
             'for versions 24, 25 and 26. A third version of the emergency patch had been released by '
             'September 1 &mdash; earlier fixes were bypassed. CISA added the two chained flaws to KEV on '
             'August 31 with a September 14 federal deadline.</p></div>')
    b.append('<div class="card"><span class="tag c">Mobile</span>'
             '<h4>StreamRat Android trojan pushed through Meta ads</h4>'
             '<p>ThreatFabric published its analysis on September 2: a fake television-streaming campaign '
             'aimed at Spanish-speaking users delivered StreamRat, which abuses Accessibility Services and '
             'MediaProjection for near-complete device control &mdash; VNC and hidden-screen control, '
             'UI-tree collection, keylogging, credential-stealing overlays and internet or screen '
             'blocking. One advertising push reached 570,000 Meta users between 11 June and 3 July 2026, '
             'mainly in Spain.</p></div>')
    b.append('<div class="card"><span class="tag w">Unconfirmed claim</span>'
             '<h4>"FalconFlank" PoC claims local privilege escalation in CrowdStrike Falcon</h4>'
             '<p>A researcher going by Nightmare-Eclipse (also Chaotic Eclipse) released a proof of concept '
             'claiming SYSTEM-level access by abusing Falcon Sensor\'s remediation workflow for malicious '
             'Microsoft Office macros, said to run on fully updated Windows 11 25H2 and Windows Server '
             '2025 with Phase 3 Optimal Protection active. At the time of reporting CrowdStrike had issued '
             'no advisory, CVE or patch. Treat this as a researcher claim, not a confirmed vulnerability.</p></div>')
    b.append('<div class="card"><span class="tag a">Supply chain</span>'
             '<h4>JFrog Artifactory exploited to mint administrator tokens</h4>'
             '<p>watchTowr honeypots observed attackers forging administrator tokens and enumerating users, '
             'groups, credential sets and federated access topologies. Public exploitation of '
             'CVE-2026-82329 has been seen since September 1; JFrog shipped the patch on August 28 and '
             'CISA added the flaw to KEV on September 2. Self-hosted instances only &mdash; JFrog SaaS is '
             'not affected.</p></div>')
    b.append('<div class="card"><span class="tag m">Ongoing</span>'
             '<h4>McKesson breach investigation</h4>'
             '<p>Infosecurity reports McKesson is investigating unauthorised access to certain third-party '
             'applications and the exfiltration of data associated with a subset of customers in its '
             'Oncology &amp; Multispecialty and Medical-Surgical business units. ShinyHunters has claimed '
             '284 million records. That figure describes claimed data records or lines, not unique '
             'individuals, and no individual count is asserted here.</p></div>')
    b.append('</div>')
    b.append('<div class="note"><b>Refused this run:</b> a search return surfaced the INC Ransom attack on '
             'the Pennsylvania Attorney General\'s Office alongside September 2026 material. The '
             'underlying coverage is dated September 2025, so the item was not published as current news. '
             'This is the same mis-shelving pattern that has repeatedly surfaced last year\'s Nevada '
             'statewide ransomware incident as a 2026 breach.</div>')

    b.append('<h2 class="sec">Vulnerability Watch</h2>')
    rows = [
        ("CVE-2026-83548", "10.0", "SonicWall SMA1000 (6210, 7210, 8200v)",
         "Pre-auth SSRF in the Appliance Work Place; chained with CVE-2026-83549 for unauthenticated RCE. Exploited in the wild; hotfixes 12.4.3-03526 / 12.5.0-02952 and later."),
        ("CVE-2026-49869", "10.0", "Kestra OSS &lt; 1.0.45 and 1.1.0&ndash;1.3.20",
         "Unauthenticated workflow creation and execution via an unsafe suffix match on paths ending in /configs; RCE as root inside the worker container. Exploited from late June 2026 to plant a cryptocurrency miner."),
        ("CVE-2026-82329", "9.8", "JFrog Artifactory (self-hosted)",
         "Improper authentication in the default configuration lets an unauthenticated attacker obtain administrative privileges and forge admin tokens. Patched August 28."),
        ("CVE-2026-9586", "9.3 (CVSS v4.0)", "Sangoma Switchvox SMB 8.3",
         "Unauthenticated SQL injection at the /pa endpoint &mdash; PhoneIP concatenated into PostgreSQL queries unsanitised &mdash; chainable to RCE. Fixed in 8.4.0.2; Horizon3.ai saw valid exploitation attempts on August 30."),
        ("CVE-2026-32475", "9.0 (CVSS v3.1)", "Elementor Pro for WordPress &le; 4.2.1",
         "Unrestricted file upload in the Forms module: extension validation and the file-move step run in separate loops, so submitting two file parts for one upload field bypasses the extension blocklist and writes a PHP file into wp-content/uploads/elementor/forms/. Fixed in 4.2.2. A public proof of concept exists; see the note below on exploitation status."),
        ("CVE-2026-83549", "7.8", "SonicWall SMA1000",
         "Post-authentication OS command injection in the Appliance Management Console; the second half of the SonicWall chain."),
        ("CVE-2026-48710", "Not stated in sources fetched", "Starlette &lt; 1.0.1 (and FastAPI, vLLM, LiteLLM)",
         '"BadHost" &mdash; the HTTP Host header is not validated before request.url is reconstructed, letting an unauthenticated attacker bypass path-based middleware with a single malformed character. Fixed in 1.0.1.'),
    ]
    b.append('<div class="tblwrap"><table><tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>')
    for r in rows:
        b.append('<tr><td class="mono">%s</td><td class="mono">%s</td><td>%s</td><td>%s</td></tr>' % r)
    b.append('</table></div>')
    b.append('<div class="note">CVE-2026-59822 (BerriAI LiteLLM) is in the September 2 KEV batch and is '
             'listed in the deadline section below; no affected-version detail was re-sourced this run, so '
             'it gets no row here rather than an inferred one. '
             '<b>On the Elementor Pro entry:</b> one aggregated return this run described the flaw as '
             'being actively exploited in the wild, while a dedicated follow-up search states only that a '
             'proof of concept has been published. In-the-wild exploitation is therefore <b>not</b> '
             'asserted, and the flaw is not in the CISA KEV catalog. The disagreement is printed rather '
             'than resolved.</div>')

    b.append('<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>')
    b.append('<div class="panel"><ul class="b">'
             '<li><b>Saturday, September 5, 2026</b> &mdash; <span class="down">2 days left</span> &mdash; '
             'SonicWall SMA1000 CVE-2026-83548 and CVE-2026-83549, JFrog Artifactory CVE-2026-82329, '
             'Sangoma Switchvox CVE-2026-9586, Kestra OSS CVE-2026-49869. All added September 2.</li>'
             '<li><b>Monday, September 14, 2026</b> &mdash; 11 days left &mdash; PaperCut NG/MF '
             'CVE-2026-81578 (missing authentication for a critical function) and CVE-2026-82078 '
             '(unsafe reflection). Added to KEV August 31.</li>'
             '<li><b>Wednesday, September 16, 2026</b> &mdash; 13 days left &mdash; Starlette '
             'CVE-2026-48710 and BerriAI LiteLLM CVE-2026-59822. NVD and Vulnerability-Lookup state the '
             'September 2 KEV add and the September 16 due date for CVE-2026-48710 explicitly.</li>'
             '</ul>'
             '<div class="note">The PaperCut pair was dropped from the earlier edition this morning '
             'because nothing in that run\'s searches restated its deadline. It is restored here on a '
             'fresh fetch that gives the August 31 add and the September 14 due date. Countdowns above '
             'are computed from today, September 3, 2026.</div></div>')

    b.append(css.sources([
        ("U.S. Attorney, Northern District of California &mdash; Russian national indicted for exploiting an online freelance-employment platform",
         "https://www.justice.gov/usao-ndca/pr/russian-national-indicted-exploiting-online-platform-used-freelance-employment-and"),
        ("BleepingComputer &mdash; US charges Russian for infecting 80,000 freelancers with malware",
         "https://www.bleepingcomputer.com/news/security/us-charges-russian-for-infecting-80-000-freelancers-with-malware/"),
        ("Help Net Security &mdash; Russian man indicted for spreading malware to 80,000 freelancers",
         "https://www.helpnetsecurity.com/2026/09/03/russian-national-indicted-freelance-platform-malware/"),
        ("The Hacker News &mdash; Extradited Russian hacker faces charges over Excel malware campaign",
         "https://thehackernews.com/2026/09/extradited-russian-hacker-faces-charges.html"),
        ("The Record &mdash; Russian national facing 20 years for malware campaign",
         "https://therecord.media/russian-national-facing-20-years-malware-campaign"),
        ("Infosecurity Magazine &mdash; Russian man extradited over malware campaign targeting freelancers",
         "https://www.infosecurity-magazine.com/news/russian-man-extradited-malware/"),
        ("The Hacker News &mdash; CISA adds seven exploited flaws as attackers deploy reverse shells and crypto miners",
         "https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html"),
        ("CISA &mdash; Adds Two Known Exploited Vulnerabilities to Catalog (Aug 31, 2026)",
         "https://www.cisa.gov/news-events/alerts/2026/08/31/cisa-adds-two-known-exploited-vulnerabilities-catalog"),
        ("SOC Prime &mdash; CVE-2026-81578 exploited PaperCut auth bypass",
         "https://socprime.com/blog/cve-2026-81578-analysis/"),
        ("Cybersecurity Dive &mdash; PaperCut issues emergency patches as threat actors target chained vulnerabilities",
         "https://www.cybersecuritydive.com/news/papercut-emergency-patches-threat-actors-chained-vulnerabilities/829184/"),
        ("Rapid7 &mdash; PaperCut NG/MF critical zero-day exploited in the wild",
         "https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/"),
        ("Orca Security &mdash; Critical Elementor Pro file-upload flaw enables unauthenticated RCE",
         "https://orca.security/resources/blog/elementor-pro-wordpress-rce-flaw/"),
        ("BleepingComputer &mdash; Critical Elementor Pro bug exposes WordPress sites to RCE attacks",
         "https://www.bleepingcomputer.com/news/security/critical-elementor-pro-bug-exposes-wordpress-sites-to-rce-attacks/"),
        ("CVEFeed &mdash; CVE-2026-32475 (Elementor Pro &le; 4.2.1)",
         "https://cvefeed.io/vuln/detail/CVE-2026-32475"),
        ("CISA &mdash; Adds Seven Known Exploited Vulnerabilities to Catalog (Sept 2, 2026)",
         "https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog"),
        ("CISA &mdash; Known Exploited Vulnerabilities Catalog",
         "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
        ("Rapid7 &mdash; Critical SonicWall SMA1000 vulnerabilities exploited in the wild",
         "https://www.rapid7.com/blog/post/etr-critical-sonicwall-sma1000-vulnerabilities-cve-2026-83548-cve-2026-83549-exploited-in-the-wild/"),
        ("NVD &mdash; CVE-2026-49869 (Kestra OSS)", "https://nvd.nist.gov/vuln/detail/CVE-2026-49869"),
        ("NVD &mdash; CVE-2026-48710 (Starlette)", "https://nvd.nist.gov/vuln/detail/CVE-2026-48710"),
        ("Vulnerability-Lookup &mdash; CVE-2026-48710 KEV add and due date",
         "https://vulnerability.circl.lu/vuln/CVE-2026-48710"),
        ("BleepingComputer &mdash; Hackers exploit critical JFrog Artifactory flaw to forge admin tokens",
         "https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-jfrog-artifactory-flaw-to-forge-admin-tokens/"),
        ("The Hacker News &mdash; Attackers exploit critical JFrog Artifactory flaw",
         "https://thehackernews.com/2026/09/attackers-exploit-critical-jfrog.html"),
        ("The Register &mdash; Another Artifactory CVE under attack",
         "https://www.theregister.com/security/2026/09/01/another-artifactory-cve-under-attack-by-ai-agents-or-humans/5293769"),
        ("Help Net Security &mdash; Exploitation of Sangoma Switchvox flaw is underway",
         "https://www.helpnetsecurity.com/2026/09/02/exploitation-of-sangoma-switchvox-flaw-underway-cve-2026-9586/"),
        ("Horizon3.ai &mdash; CVE-2026-9586 Sangoma Switchvox RCE",
         "https://horizon3.ai/attack-research/disclosures/cve-2026-9586-sangoma-switchvox-rce/"),
        ("SentinelOne &mdash; CVE-2026-9586 vulnerability database entry",
         "https://www.sentinelone.com/vulnerability-database/cve-2026-9586/"),
        ("BleepingComputer &mdash; Hackers exploit Sangoma Switchvox flaw to deploy reverse shells",
         "https://www.bleepingcomputer.com/news/security/hackers-exploit-sangoma-switchvox-flaw-to-deploy-reverse-shells/"),
        ("ThreatFabric &mdash; From Meta ads to full device takeover: uncovering StreamRat",
         "https://www.threatfabric.com/blogs/from-meta-ads-to-full-device-takeover-uncovering-streamrat"),
        ("The Hacker News &mdash; Meta ads push StreamRat Android trojan",
         "https://thehackernews.com/2026/09/meta-ads-push-streamrat-android-trojan.html"),
        ("Cyber Security News &mdash; Ransomware hackers use new TukTuk malware",
         "https://cybersecuritynews.com/new-tuktuk-malware/"),
        ("The Hacker News &mdash; Researcher releases FalconFlank PoC",
         "https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html"),
        ("Security Affairs &mdash; Chaotic Eclipse releases CrowdStrike Falcon zero-day FalconFlank",
         "https://securityaffairs.com/198342/hacking/chaotic-eclipse-releases-crowdstrike-falcon-zeroday-falconflank.html"),
        ("Infosecurity Magazine &mdash; Healthcare giant McKesson investigates data breach incident",
         "https://www.infosecurity-magazine.com/news/healthcare-mckesson-investigates/"),
    ]))
    b.append('<div class="disc">Information only, not security advice. Severity scores, deadlines and '
             'affected versions are reproduced as stated by the vendor, CISA or NVD source cited; where '
             'sources disagree, the disagreement is printed rather than resolved.</div></footer>')
    b.append('</div>' + css.STAMP_JS + '</body></html>')
    write("cyber-briefing.html", "\n".join(b))

# ================================================================ WALL STREET
def build_ws():
    c = css.base_css("#caa64a", "#e8c766", "#0c0d10", "#15171c", "#26282f")
    extra = """
h1,h3,h4,.lead h3{font-family:Georgia,'Times New Roman',serif}
h2.sec{font-family:var(--mono)}
"""
    b = []
    b.append(css.head("The Closing Bell &mdash; Daily Market Briefing", c + extra))
    b.append('<header class="masthead"><h1>The Closing Bell</h1>'
             '<p class="tag">&#9650; Your daily Wall Street briefing &mdash; the tape, the movers and '
             'what is next.</p>' + css.meta_row() + '</header>')
    b.append('<div class="tldr"><b>The Tape</b> <span>%s</span></div>' % SUM_WS)
    b.append(FRESH)
    b.append(css.nav("ws"))

    # BLOCK A
    b.append('<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>'
             + w("ticker-tape",
                 '{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},'
                 '{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},'
                 '{"proName":"FOREXCOM:DJI","title":"Dow 30"},'
                 '{"proName":"NYSE:SNOW","title":"Snowflake"},'
                 '{"proName":"NASDAQ:AVGO","title":"Broadcom"},'
                 '{"proName":"NASDAQ:DDOG","title":"Datadog"},'
                 '{"proName":"NYSE:NOW","title":"ServiceNow"},'
                 '{"proName":"NASDAQ:MRNA","title":"Moderna"},'
                 '{"proName":"TVC:USOIL","title":"WTI Crude"},'
                 '{"proName":"TVC:US10Y","title":"US 10Y"}],'
                 '"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,'
                 '"displayMode":"adaptive","locale":"en"}')
             + '</div>')

    # BLOCK B
    b.append('<h2 class="sec">Live Index Quotes &mdash; updates in real time</h2>')
    b.append('<div class="tickers">')
    for sym in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI"):
        b.append('<div class="ticker">' + w("single-quote",
                 '{"symbol":"%s","width":"100%%","colorTheme":"dark","isTransparent":true,"locale":"en"}' % sym)
                 + '</div>')
    b.append('</div>')
    b.append('<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects '
             'the latest edition; official closes are in the Weekly Scorecard.</div>')

    b.append('<h2 class="sec">The Lead</h2>')
    b.append('<div class="callout"><div class="k">Pre-open &middot; ~8:40 AM ET</div>'
             '<h3>Dow futures inch up, Nasdaq contracts slip, and oil keeps its war premium</h3>'
             '<p>U.S. stock futures are narrowly mixed early Thursday. Dow futures are up about 0.2%, at '
             '53,274.00 for a gain of 153.00 points or 0.29%; S&amp;P 500 futures are little changed at '
             '7,679.50, up 3.00 points or 0.04%; and Nasdaq 100 contracts sit just below the flat line at '
             '29,130.50, down 55.75 or 0.19%. A separate pre-market index reading has the S&amp;P 500 '
             '+0.12%, the Nasdaq 100 +0.04%, the Dow +0.25% and the Russell 2000 &minus;0.09%.</p>'
             '<p>Iran struck U.S. allies Jordan, the United Arab Emirates and Kuwait with missiles and '
             'drones overnight in retaliation for the latest round of American airstrikes, and its '
             'Revolutionary Guards say two oil tankers hit naval mines attempting to transit the Strait of '
             'Hormuz. TheStreet notes oil has "rebuilt some geopolitical premium, creating another '
             'potential inflationary headache at a time when markets are already debating whether US '
             'rates need to move higher." Brent is the contested figure this morning &mdash; see the '
             'rates and commodities table. The Labor Department released the week-ending-August-29 '
             'jobless claims report at 8:30 AM ET; no actual figure appeared in anything fetched for this '
             'edition, so none is printed. Friday\'s August employment report is the last labour reading '
             'the FOMC sees before its September 16 decision.</p>'
             '<p class="note">These futures readings differ from the 8:16 AM edition\'s (Dow +0.07%, '
             'S&amp;P 500 &minus;0.05%, Nasdaq 100 &minus;0.11%). That is drift across roughly twenty '
             'minutes of pre-market trade, not a disagreement between sources. Nothing on this page is a '
             'live Thursday session price &mdash; the opening bell is 9:30 AM ET.</p></div>')

    b.append('<h2 class="sec">Movers &amp; Drivers &mdash; pre-market</h2>')
    b.append('<div class="cards two">')
    b.append('<div class="card"><span class="tag a">+24% pre-market</span>'
             '<h4>Snowflake</h4><p>Shares jumped in pre-market trade after fiscal second-quarter results '
             'and a raised outlook: adjusted EPS $0.62 against $0.45 expected on revenue of $1.55 billion '
             'against $1.48 billion. Product revenue rose 37% year over year to $1.49 billion and '
             'non-GAAP operating income reached $237 million versus a $187 million estimate. Full-year '
             'product revenue guidance went to $6.07 billion, about 36% growth, and full-year operating '
             'margin guidance to 14.5% from 13.5%. Cortex Code passed 9,100 accounts after adding more '
             'than 2,000 in the quarter. <b>Two different windows:</b> the Wednesday after-hours move was '
             'reported at 22% by CNBC and 23% by Yahoo Finance; the figure above is Thursday\'s '
             'pre-market print of more than 24%. These are not competing readings of the same move '
             'and are not treated as such.</p></div>')
    b.append('<div class="card"><span class="tag new">New</span><span class="tag c">&minus;2%+</span>'
             '<h4>Moderna</h4><p>Off more than 2% pre-market after Rothschild &amp; Co Redburn '
             'downgraded the stock to sell. No price target was stated in the material fetched this run, '
             'so none is printed.</p></div>')
    b.append('<div class="card"><span class="tag c">&minus;7%</span>'
             '<h4>The Campbell\'s Company</h4><p>Down almost 7% pre-market after issuing fiscal 2027 '
             'earnings guidance below expectations. No guidance figures were stated in the material '
             'fetched this run, so none are printed.</p></div>')
    b.append('<div class="card"><span class="tag c">&minus;2.5%</span>'
             '<h4>Broadcom</h4><p>Lower after a fourth-quarter revenue forecast of $34.8 billion against '
             'a $35.03 billion estimate. The "fourth quarter" label is CNBC\'s own wording for the '
             'guidance period; no fiscal-period label is being inferred here.</p></div>')
    b.append('<div class="card"><span class="tag a">Software bid</span>'
             '<h4>Datadog and ServiceNow</h4><p>Snowflake\'s rally lifted its software peers, with Datadog '
             'up more than 5% and ServiceNow up 3%. Hewlett Packard Enterprise, carried in the earlier '
             'edition at &minus;3%, was not restated in this run\'s searches and is therefore not '
             'repeated with a number.</p></div>')
    b.append('</div>')

    b.append('<h2 class="sec">Chart of the Day &mdash; Snowflake (SNOW)</h2>')
    b.append('<div class="panel" style="padding:8px">' + w("mini-symbol-overview",
             '{"symbol":"NYSE:SNOW","width":"100%","height":240,"locale":"en","dateRange":"1D",'
             '"colorTheme":"dark","isTransparent":true,"autosize":false}') + '</div>')
    b.append('<div class="note">Snowflake is the largest pre-market move among the large-cap names in the section above. It is <b>not</b> the largest move in the pre-market return overall: the same list carries Ultragenyx Pharmaceutical down 44.40% and Generation Income Properties up 44.46%, with Gelteq +35%, Tilly&#39;s +29.40% and Ethan Allen Interiors &minus;11.01%. Those are thinly traded small caps and are noted here only so the superlative above is not overstated.</div>')

    b.append('<h2 class="sec">Sector Heat &mdash; live</h2>')
    b.append('<div class="panel" style="padding:8px">' + w("stock-heatmap",
             '{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change",'
             '"grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,'
             '"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,'
             '"isMonoSize":false,"width":"100%","height":420}') + '</div>')
    b.append('<div class="note">Single-session sector leadership is <b>not</b> asserted for a twelfth '
             'consecutive edition. This run\'s sector return offers single-day leader and laggard readings '
             'inside a piece that also states the S&amp;P 500 "declined 0.71% to 7,631.47" on the day '
             'in question. That '
             'contradicts Wednesday\'s verified close of 7,666.60, up 0.46%, so the session cannot be '
             'pinned and the daily figures are not published. Only the year-to-date readings are firm, '
             'and even those return two ways for energy: <span class="up">+43% YTD</span> in this run\'s '
             'return and <span class="up">+42.32% YTD</span> for XLE in the standing record &mdash; both '
             'printed, neither adopted. Consumer discretionary is <span class="down">&minus;2.3% '
             'YTD</span>; materials <span class="up">+15.86% YTD</span>.</div>')

    b.append('<h2 class="sec">The Calendar &mdash; live</h2>')
    b.append('<div class="panel" style="padding:8px">' + w("events",
             '{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en",'
             '"importanceFilter":"0,1","countryFilter":"us"}') + '</div>')

    b.append('<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2>')
    b.append('<div class="panel" style="padding:8px">' + w("timeline",
             '{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,'
             '"displayMode":"regular","width":"100%","height":420,"locale":"en"}') + '</div>')

    b.append('<h2 class="sec">Weekly Scorecard &mdash; official closes</h2>')
    b.append('<div class="tblwrap"><table>'
             '<tr><th>Index</th><th>Close</th><th>Change</th><th>Session</th></tr>'
             '<tr><td>S&amp;P 500</td><td class="mono">7,666.60</td><td class="mono up">+0.46%</td>'
             '<td>Wed, Sept 2, 2026</td></tr>'
             '<tr><td>Nasdaq Composite</td><td class="mono">26,217.83</td><td class="mono up">+0.45%</td>'
             '<td>Wed, Sept 2, 2026</td></tr>'
             '<tr><td>Dow Jones Industrial Average</td><td class="mono">53,061.95</td>'
             '<td class="mono up">+295.07 &middot; +0.56%</td><td>Wed, Sept 2, 2026</td></tr>'
             '</table></div>')
    b.append('<div class="note">These three closes have now returned identical on seven consecutive '
             'fetches across editions, this run from The Globe and Mail, TheStreet and CNBC. Newly '
             'sourced framing: stocks rose Wednesday as Treasury yields "took a breather" from the '
             'run-up that had carried them to multiyear highs. The streak framing still does not agree '
             '&mdash; one reading has Wednesday snapping a <b>two-day</b> losing streak, CNBC coverage a '
             '<b>three-day</b> one; both are printed, neither adopted. Only Wednesday\'s official closes '
             'are listed &mdash; earlier sessions in the week were not re-sourced in this run.</div>')

    b.append('<h2 class="sec">Rates, Bonds &amp; Commodities</h2>')
    b.append('<div class="tblwrap"><table>'
             '<tr><th>Instrument</th><th>Level</th><th>Note</th></tr>'
             '<tr><td>10-year Treasury yield</td><td class="mono">4.796% prior close</td>'
             '<td>Investing.com gives a previous close of 4.796% and a day\'s range of '
             '4.765&ndash;4.820%. Wednesday\'s intraday high of 4.814% has been described as the highest '
             'since November 2023.</td></tr>'
             '<tr><td>WTI crude</td><td class="mono">$90.76 (Sept 2 close, +0.60%)</td>'
             '<td>Historical data for Wednesday. A Thursday futures quote returned this run showed '
             '$91.01; the earlier edition carried $90.51 and $89.62 from other feeds. No single Thursday '
             'level is adopted.</td></tr>'
             '<tr><td>Brent crude</td><td class="mono">Sources disagree</td>'
             '<td>Trading Economics puts Brent at $95.25, down 0.40% on Thursday, "snapping a three-day '
             'rally" as investors weigh renewed hostilities against efforts to reopen the Strait of '
             'Hormuz. Fortune\'s daily oil page says that by 8 AM ET Brent had reached $99.38, $3.27 '
             'above the same hour yesterday. The gap is too wide to reconcile; both are printed, neither '
             'is adopted.</td></tr>'
             '<tr><td>Fed funds target</td><td class="mono">Not re-sourced this run</td>'
             '<td>No level is published. The next decision is Wednesday, September 16 at 2:00 PM ET.</td></tr>'
             '</table></div>')

    b.append('<h2 class="sec">On the Radar</h2>')
    b.append('<div class="panel"><ul class="b">'
             '<li><b>Released this morning &mdash; initial jobless claims.</b> The Labor Department put '
             'out the weekly claims report for the week ending August 29 at 8:30 AM ET. Consensus was '
             '205,000 against 203,000 the week before. The actual print did not appear in any source '
             'fetched for this edition, so no figure is published here.</li>'
             '<li><b>Also this morning &mdash; July international trade in goods and services.</b> '
             'Expected &minus;$71.2 billion against a prior &minus;$73.26 billion.</li>'
             '<li><b>Friday, September 4, 8:30 AM ET &mdash; the August employment report.</b> Kiplinger '
             'reports economists expect about 58,000 jobs added and unemployment holding at 4.1%. It is '
             'the last labour reading the FOMC sees before its decision.</li>'
             '<li><b>Wednesday, September 16, 2:00 PM ET &mdash; FOMC decision.</b> Elevated energy prices '
             'tied to the Iran conflict have supported bets on a 25-basis-point <i>hike</i>, while '
             'softening labour data has left the probability of no change nearly as high. A strong August '
             'print is the hawkish outcome.</li>'
             '<li><b>The Strait of Hormuz.</b> Iran\'s Revolutionary Guards say two tankers struck naval '
             'mines attempting to transit; any confirmation of sustained disruption is the live supply '
             'risk under the oil bid.</li>'
             '</ul></div>')

    b.append(css.sources([
        ("TheStreet &mdash; Stock Market Today, Sept. 3, 2026",
         "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-03-2026"),
        ("CNBC &mdash; Stocks making the biggest moves premarket, Sept. 3",
         "https://www.cnbc.com/2026/09/03/stocks-making-the-biggest-moves-premarket-snow-mrna-avgo.html"),
        ("Benzinga &mdash; Futures fall as U.S.-Iran tensions escalate",
         "https://www.benzinga.com/markets/equities/26/09/61568360/stock-market-today-nasdaq-100-sp-500-futures-fall-as-us-iran-tensions-escalate-dell-panw-mdb-avgo-in-focus"),
        ("CNBC &mdash; S&amp;P 500 futures little changed as Treasury yields stabilize (Sept 2 live blog)",
         "https://www.cnbc.com/2026/09/02/stock-market-today-live-updates.html"),
        ("TheStreet &mdash; Stock Market Today, Sept. 2, 2026",
         "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-02-2026"),
        ("Yahoo Finance &mdash; Stock market today, Wednesday, September 2",
         "https://finance.yahoo.com/markets/live/stock-market-today-wednesday-september-2-dow-sp-500-nasdaq-082624175.html"),
        ("Yahoo Finance &mdash; 10-year Treasury touches highest level since 2023 as oil prices stay elevated",
         "https://finance.yahoo.com/markets/article/10-year-treasury-touches-highest-level-since-2023-as-oil-prices-stay-elevated-134238599.html"),
        ("CNBC &mdash; Snowflake spikes on results and AI coding momentum",
         "https://www.cnbc.com/2026/09/02/snowflake-snow-q2-earnings-report-2027.html"),
        ("Yahoo Finance &mdash; Snowflake leaps on earnings beat and raised guidance",
         "https://finance.yahoo.com/markets/stocks/articles/snowflake-soars-20-earnings-beat-204552979.html"),
        ("Investing.com &mdash; Snowflake shares surge as AI demand powers growth, lifts outlook",
         "https://www.investing.com/news/stock-market-news/snowflake-shares-surge-as-ai-demand-powers-growth-lifts-outlook-4887223"),
        ("Kiplinger &mdash; August jobs report preview",
         "https://www.kiplinger.com/investing/economy/jobs-report-august-2026-what-to-expect"),
        ("Trading Economics &mdash; United States initial jobless claims",
         "https://tradingeconomics.com/united-states/jobless-claims"),
        ("Robinhood prediction markets &mdash; September 3, 2026 unemployment claims",
         "https://robinhood.com/us/en/prediction-markets/economics/events/2026-september-3-unemployment-claims-sep-03-2026/"),
        ("Investing.com &mdash; S&amp;P 500 sector performance: energy leads with +42% YTD",
         "https://www.investing.com/news/stock-market-news/sp-500-sector-performance-energy-leads-with-42-ytd-gain-in-2026-93CH-4883146"),
        ("Yahoo Finance &mdash; Stock Market News for Sep 2, 2026",
         "https://finance.yahoo.com/markets/stocks/articles/stock-market-news-sep-2-095800348.html"),
        ("Polymarket &mdash; Fed decision in September",
         "https://polymarket.com/event/fed-decision-in-september-762"),
        ("Yahoo Finance &mdash; Stock market today, Thursday, September 3 (live futures blog)",
         "https://finance.yahoo.com/markets/live/stock-market-today-thursday-september-3-dow-sp-500-nasdaq-futures-081525933.html"),
        ("The Globe and Mail &mdash; Stock Market News for Sep 2, 2026",
         "https://www.theglobeandmail.com/investing/markets/stocks/CVX/pressreleases/4395975/stock-market-news-for-sep-2-2026/"),
        ("Fortune &mdash; Current price of oil as of Sept. 3, 2026",
         "https://fortune.com/article/price-of-oil-09-03-2026/"),
        ("Trading Economics &mdash; Brent crude oil",
         "https://tradingeconomics.com/commodity/brent-crude-oil"),
        ("Investing.com &mdash; U.S. 10-year Treasury bond yield",
         "https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield"),
        ("Investing.com &mdash; Crude oil WTI futures historical prices",
         "https://www.investing.com/commodities/crude-oil-historical-data"),
        ("Econoday &mdash; Jobless Claims, September 3, 2026",
         "https://us.econoday.com/byevent?fid=672522&amp;year=2026&amp;lid=0"),
        ("StockCharts &mdash; The S&amp;P 500 is rallying, so why are industrials falling behind?",
         "https://articles.stockcharts.com/article/sp-500-rallying-so-why-are-industrials-falling-behind/"),
    ]))
    b.append('<div class="disc">Information only, not investment advice. Live widgets stream third-party '
             'quotes that may be delayed; editorial figures are reproduced only where a source fetched '
             'this run states them.</div></footer>')
    b.append('</div>' + css.STAMP_JS + '</body></html>')
    write("wallstreet-briefing.html", "\n".join(b))

# ================================================================ MMA
CDN_JS = """<script>(function(){var t=new Date('2026-09-05T00:00:00-04:00');function u(){var e=document.getElementById('ufccdn');if(!e)return;var d=t-new Date();if(d<=0){e.textContent='Fight week \\u2014 live/completed';return;}var dd=Math.floor(d/864e5),hh=Math.floor(d%864e5/36e5),mm=Math.floor(d%36e5/6e4);e.textContent=dd+'d '+hh+'h '+mm+'m';}u();setInterval(u,30000);})();</script>"""

def build_mma():
    c = css.base_css("#e84545", "#ff8a5c", "#100c0c", "#1a1313", "#322020")
    b = []
    b.append(css.head("The Octagon &mdash; Daily MMA Briefing", c))
    b.append('<header class="masthead"><h1>The Octagon</h1>'
             '<p class="tag">&#8856; Your daily MMA briefing &mdash; UFC, prospects &amp; the business '
             'of fighting</p>' + css.meta_row() + '</header>')
    b.append('<div class="tldr"><b>Tale of the Tape</b> <span>%s</span></div>' % SUM_MMA)
    b.append(FRESH)
    b.append(css.nav("mma"))

    b.append('<div class="cdn"><span class="lbl">Next card</span>'
             '<span class="clk" id="ufccdn">&nbsp;</span>'
             '<span class="ev">UFC Fight Night: Hooker vs. Parnasse &mdash; Saturday, September 5, '
             'Accor Arena, Paris. Countdown runs to fight day; no start time is asserted.</span></div>')

    b.append('<h2 class="sec">Top Story</h2>')
    b.append('<div class="callout crit"><div class="k">UFC 332 &middot; still TBD</div>'
             '<h3>Salt Lake City is a month out and still has no main event</h3>'
             '<p>Valentina Shevchenko is out of UFC 332 with an injury, and the promotion is still '
             'searching for a headliner for the card at the Delta Center in Salt Lake City on Saturday, '
             'October 3. Reporting this week says the UFC is working on an interim women\'s flyweight '
             'title fight between <b>Natalia Silva</b> and <b>Wang Cong</b> as the replacement main '
             'event.</p>'
             '<p>Shevchenko\'s defence against No. 1 contender Natalia Silva had been the promotion\'s leading '
             'option to headline the show. Coverage of the reported replacement adds that the '
             'pairing would give Silva a chance to avenge a <b>2015 kickboxing loss to Wang Cong</b>.</p>'
             '<p>Nothing is official. UFC CEO Dana White has said the main event will be announced this '
             'week, and Bloody Elbow framed the Silva&ndash;Wang pairing as rumoured ahead of an '
             'announcement rather than booked. No replacement bout, no Shevchenko return timeline and no '
             'co-main event are confirmed as of this edition.</p></div>')

    b.append('<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>')
    b.append('<div class="cards two">')
    b.append('<div class="card"><div class="k">Sat, Sept 5 &middot; Accor Arena, Paris</div>'
             '<h4>UFC Fight Night: Hooker vs. Parnasse</h4>'
             '<p>Fourteen fights. Dan Hooker meets Salahdine Parnasse, who is making his UFC debut in a '
             'main event after arriving as a two-time KSW featherweight champion and one-time KSW '
             'lightweight champion &mdash; not through the Contender Series. Far&egrave;s Ziam vs. Axel '
             'Sola sits on the main card.<br><b>Odds:</b> Parnasse &minus;600 / Hooker +440 '
             '(DraftKings); some books show &minus;500 / +400. Ziam is quoted &minus;145 against Sola at '
             '+125 this run, against &minus;155 in the earlier edition &mdash; both printed, neither '
             'adopted. The main-event total sits at 3.5 rounds, under at &minus;260.</p></div>')
    b.append('<div class="card"><div class="k">Sat, Sept 12 &middot; Desert Diamond Arena, Glendale</div>'
             '<h4>Noche UFC: Silva vs. Delgado</h4>'
             '<p>Jean Silva headlines against Jose Miguel Delgado, who stepped in after Yair Rodr&iacute;guez '
             'was forced out injured. The card also carries Waldo Cortes-Acosta vs. Curtis Blaydes, Manon '
             'Fiorot vs. Alexa Grasso and Brandon Moreno vs. Joseph Morales. No headline odds were stated '
             'in the material fetched this run, so none are printed.</p></div>')
    b.append('<div class="card"><div class="k">Sat, Sept 19 &middot; Crypto.com Arena, Los Angeles</div>'
             '<h4>UFC 331: Van vs. Pantoja 2</h4>'
             '<p>Thirteen fights. Flyweight champion Joshua Van rematches Alexandre Pantoja, whom he beat '
             'for the belt at UFC 323 in December 2025 by technical knockout 26 seconds into round one '
             'after Pantoja suffered an arm injury. Arman Tsarukyan vs. Mauricio Ruffy is a five-round '
             'lightweight co-main. Early prelims about 5 PM ET, prelims 7 PM ET, main card 9 PM ET on '
             'Paramount+. No headline odds stated this run.</p></div>')
    b.append('<div class="card"><div class="k">Sat, Oct 3 &middot; Delta Center, Salt Lake City</div>'
             '<h4>UFC 332 &mdash; main event TBD</h4>'
             '<p>Without a headliner after the Shevchenko withdrawal. See the top story: Silva vs. Wang '
             'Cong for an interim women\'s flyweight title is reported as the target, not announced.</p></div>')
    b.append('</div>')

    b.append('<h2 class="sec">Last Event &mdash; UFC Shanghai, Saturday, August 29, 2026</h2>')
    b.append('<div class="tblwrap"><table><tr><th>Result</th><th>Bout</th><th>Method</th></tr>'
             '<tr><td class="win">Song Yadong</td><td>def. Umar Nurmagomedov &middot; bantamweight, main event</td>'
             '<td>KO (right uppercut) &mdash; R2, 1:48</td></tr>'
             '<tr><td class="win">Denise Gomes</td><td>def. Yan Xiaonan &middot; strawweight, co-main</td>'
             '<td>TKO (elbow and punches) &mdash; R1, 4:49</td></tr>'
             '<tr><td class="win">Kai Asakura</td><td>def. Aoriqileng &middot; bantamweight</td>'
             '<td>KO (head kick and punches) &mdash; R2, 0:34</td></tr>'
             '</table></div>')
    b.append('<div class="note">Only the bouts re-sourced in this run\'s searches are listed; '
             'this is not the full results table, and no card depth is asserted because '
             'none was re-sourced this run. Nurmagomedov entered a '
             '&minus;600 favourite. Gomes extended her win streak to five, the longest among active '
             'strawweights, and tied Jessica Andrade for the most knockout wins in UFC strawweight '
             'history at four. Her opponent\'s name is rendered "Aoriqileng" by UFC.com and "Aori Qileng" '
             'by other outlets.</div>')
    b.append('<div class="panel" style="margin-top:12px"><h4>Performance bonuses</h4>'
             '<p style="font-size:14.5px;margin:0">$400,000 was paid across the two headline awards. '
             '<b>$100,000 each:</b> Performance of the Night to Song Yadong and Bilal Hasan; Fight of the '
             'Night to Ce Liu and Levi Rodrigues Jr. <b>$25,000 finish bonuses:</b> Hector Santiago, '
             'Francesco Nuzzi, Rei Tsuruya, Kai Asakura and Denise Gomes.</p>'
             '<div class="note">The Fight of the Night winner is rendered "Liu Ce" in the bonus coverage '
             'and "Ce Liu" elsewhere; this page uses Ce Liu consistently. The source says "five more '
             'fighters collected for finishing" and then names five, so the count and the names agree '
             'this run &mdash; an earlier fetch named seven.</div></div>')

    b.append('<h2 class="sec">Prospect Watch</h2>')
    b.append('<div class="cards two">')
    b.append('<div class="card"><span class="tag new">New</span><span class="tag a">Next up</span>'
             '<h4>Contender Series Week 5 lands Tuesday</h4>'
             '<p>Season 10, Week 5 runs Tuesday, September 8 at 7:00 PM ET from the Meta APEX in Las '
             'Vegas on Paramount+, headlined by Berisha against Pasley at 205 pounds &mdash; the listing '
             'gives surnames only, so no first names are supplied. That fills the gap '
             'this desk flagged earlier today, when no date had been sourced for the week between the '
             'September 1 card and Week 6 on September 15.</p></div>')
    b.append('<div class="card"><span class="tag a">Prospect</span>'
             '<h4>Five contracts from Contender Series Week 4</h4>'
             '<p>Adam Darby, Modestino Rodrigues, Silvestre Sanchez, Gabriel Louren&ccedil;o and Adam '
             'Livingston each earned UFC deals at the Meta APEX on September 1. Louren&ccedil;o dropped '
             'his opponent with a right hand and finished with hammer-fists in the first round; '
             'Livingston took his by split decision in a second DWCS appearance. His surname is rendered '
             'both "Louren&ccedil;o" and "Lorenco" across outlets.</p></div>')
    b.append('<div class="card"><span class="tag a">Prospect</span>'
             '<h4>Season 10 so far</h4>'
             '<p>Contract winners through four weeks: Anthony Wint, Bilal Hasan, Tom Pagliarulo and '
             'Joseph Kropschot in Week 1; Kaik Brito, Trent Miller, Cristian P&eacute;rez, Alik Lorenz, '
             'Roman Puga and Taner Trembley in Week 2; Alex Apodaca, Guilherme Uriel, Sean Clancy Jr., '
             'Ronald Humphrey and Nick Galanti in Week 3. Week 6 lands September 15 with Akbar Abdullaev '
             'against Anthony Figueroa.</p></div>')
    b.append('</div>')

    b.append('<h2 class="sec">Around the Sport</h2>')
    b.append('<div class="panel"><ul class="b">'
             '<li><b>A fast rise for Bilal Hasan.</b> He earned his UFC contract on Contender Series '
             'Week 1 of this season and has already collected a $100,000 Performance of the Night '
             'award at Shanghai.</li>'
             '<li><b>Noche UFC lost its original headliner.</b> Yair Rodr&iacute;guez was forced out '
             'injured against Jean Silva; Jose Miguel Delgado of Mexico stepped in, and the bout was '
             'announced as the new main event on August 22.</li>'
             '<li><b>One September title fight is on the books</b> &mdash; Van vs. Pantoja 2 for the '
             'flyweight belt at UFC 331 &mdash; while October\'s pay-per-view is still shopping for a '
             'headliner.</li>'
             '</ul></div>')

    b.append('<h2 class="sec">Rankings &amp; Business</h2>')
    b.append('<div class="panel"><h4>Rankings movement</h4>'
             '<ul class="b">'
             '<li>Islam Makhachev sits at No. 1 on the men\'s pound-for-pound board in aggregated '
             'rankings dated September 1; Merab Dvalishvili and Sean O\'Malley are the top two ranked '
             'bantamweights behind the champion.</li>'
             '<li>Song Yadong\'s post-Shanghai climb at bantamweight &mdash; reported in the earlier edition '
             'as a move from No. 7 to No. 4 &mdash; was not restated in this run\'s rankings return, so '
             'it is recorded here with that provenance rather than asserted as the current ranking.</li></ul>'
             '<h4 style="margin-top:14px">Business &amp; broadcast</h4>'
             '<ul class="b">'
             '<li>Paramount is in the first year of a <b>seven-year, $7.7 billion</b> media-rights deal '
             'with the UFC, which is owned by TKO Group. UFC 331 and the Paris card are Paramount+ '
             'events.</li>'
             '<li>TKO\'s own investor release puts UFC Freedom 250 &mdash; the White House card on June 14 '
             '&mdash; at <b>34 million total global viewers</b>, including 17 million across the U.S. and '
             'Latin America on Paramount+. The U.S. average is disputed: one return gives 7.0 million, '
             'described as the most-watched UFC event domestically, while The Hollywood Reporter\'s '
             'headline says the card averaged 8 million viewers on Paramount+. Both are printed; neither '
             'is adopted.</li>'
             '<li>No gate figure was stated in anything fetched this run, so none is printed.</li>'
             '</ul></div>')

    b.append('<h2 class="sec">Champions Board</h2>')
    b.append('<div class="tblwrap"><table><tr><th>Division</th><th>Champion</th><th>Note</th></tr>'
             '<tr><td><b>Heavyweight</b></td><td>Tom Aspinall</td><td>Undisputed since June 21, 2025. '
             '<b>Interim:</b> Ciryl Gane, since June 14, 2026.</td></tr>'
             '<tr><td><b>Light Heavyweight</b></td><td>Carlos Ulberg</td><td>Champion since April 11, 2026.</td></tr>'
             '<tr><td><b>Middleweight</b></td><td>Sean Strickland</td>'
             '<td>Split-decision win over Khamzat Chimaev at UFC 328, Prudential Center, Newark &mdash; '
             'two judges 48-47 Strickland, one 48-47 Chimaev. Two-time champion.</td></tr>'
             '<tr><td><b>Welterweight</b></td><td>Islam Makhachev</td><td>Champion since November 15, 2025.</td></tr>'
             '<tr><td><b>Lightweight</b></td><td>Justin Gaethje</td><td>Champion since June 14, 2026.</td></tr>'
             '<tr><td><b>Featherweight</b></td><td>Alexander Volkanovski</td><td>Champion since April 12, 2025. Not vacant.</td></tr>'
             '<tr><td><b>Bantamweight</b></td><td>Petr Yan</td><td>Champion since December 6, 2025.</td></tr>'
             '<tr><td><b>Flyweight</b></td><td>Joshua Van</td><td>Champion since December 6, 2025. Defends against Pantoja at UFC 331.</td></tr>'
             '<tr><td><b>Women\'s Bantamweight</b></td><td>Kayla Harrison</td><td>Champion since June 7, 2025.</td></tr>'
             '<tr><td><b>Women\'s Flyweight</b></td><td>Valentina Shevchenko</td>'
             '<td class="nc">Champion, but withdrawn from her UFC 332 defence with an injury; an interim '
             'title bout is reported as the replacement target.</td></tr>'
             '<tr><td><b>Women\'s Strawweight</b></td><td>Mackenzie Dern</td><td>Champion since October 25, 2025.</td></tr>'
             '<tr><td><b>Women\'s Featherweight</b></td><td class="nc">Vacant</td><td>&mdash;</td></tr>'
             '</table></div>')
    b.append('<div class="note"><b>Corrected again this run:</b> the aggregated champions list fetched for '
             'this edition returned Khamzat Chimaev at middleweight for the twenty-ninth time, dating his '
             'reign to August 16, 2025. It is wrong. Strickland\'s title win was re-verified on a fresh '
             'fetch this run against ESPN ("Strickland stuns rival Chimaev"), CBS Sports, Sky Sports and '
             'Al Jazeera &mdash; a split decision, two judges 48-47 Strickland and one 48-47 Chimaev, at '
             'the Prudential Center in Newark. The list got eleven of its twelve cells right. Sources '
             'also disagree on the date of UFC 328 &mdash; Al Jazeera files it under May 10, 2026, while '
             'this desk\'s standing record is May 9, 2026; the discrepancy is printed rather than '
             'silently resolved, and no weekday is attached to either.</div>')

    b.append(css.sources([
        ("Yahoo Sports &mdash; Shevchenko out of UFC 332, Wang Cong&ndash;Silva reportedly targeted",
         "https://sports.yahoo.com/articles/shevchenko-ufc-332-wang-cong-065427888.html"),
        ("Sports Illustrated &mdash; UFC reportedly working on new UFC 332 title fight",
         "https://www.si.com/fannation/mma/news/ufc-working-on-new-ufc-332-title-fight-valentina-shevchenko-injury"),
        ("Bloody Elbow &mdash; Fans react to rumoured replacement UFC 332 main event",
         "https://bloodyelbow.com/2026/09/02/fans-react-to-rumored-replacement-ufc-332-main-event-ahead-of-announcement-nightmare-come-true/"),
        ("Athlon Sports &mdash; UFC 332: Wang Cong, Natalia Silva, Shevchenko",
         "https://athlonsports.com/mma/ufc-332-wang-cong-natalia-silva-shevchenko-rematch"),
        ("UFC.com &mdash; UFC Fight Night: Hooker vs Parnasse (Sept 5)",
         "https://www.ufc.com/event/ufc-fight-night-september-05-2026"),
        ("Tapology &mdash; UFC Fight Night: Hooker vs. Parnasse",
         "https://www.tapology.com/fightcenter/events/144513-ufc-fight-night"),
        ("SportsLine &mdash; UFC Fight Night odds and picks for Hooker vs. Parnasse",
         "https://www.sportsline.com/insiders/ufc-fight-night-odds-picks-seasoned-mma-analyst-reveals-selections-for-hooker-vs-parnasse-and-other-matchups-at-paris-on-sept-5/"),
        ("VSiN &mdash; UFC Paris: Hooker vs. Parnasse odds and predictions",
         "https://vsin.com/mma/ufc-paris-hooker-vs-parnasse-odds-picks-predictions-and-best-bets/"),
        ("UFC.com &mdash; Noche UFC: Silva vs Delgado (Sept 12)",
         "https://www.ufc.com/event/ufc-fight-night-september-12-2026"),
        ("CBS Sports &mdash; Jose Delgado steps in to face Jean Silva",
         "https://www.cbssports.com/ufc/news/noche-ufc-main-event-jose-delgado-yair-rodriguez-jean-silva/"),
        ("Tapology &mdash; UFC 331: Van vs. Pantoja 2",
         "https://www.tapology.com/fightcenter/events/145652-ufc-331"),
        ("Al Jazeera &mdash; Van&ndash;Pantoja rematch to headline UFC 331",
         "https://www.aljazeera.com/sports/2026/8/6/ufc-331-van-pantoja-rematch-tsarukyan-returns-and-full-fight-card"),
        ("UFC.com &mdash; UFC Shanghai results: Nurmagomedov vs Song",
         "https://www.ufc.com/news/ufc-shanghai-results-nurmagomedov-vs-song"),
        ("UFC.com &mdash; UFC Shanghai bonus coverage",
         "https://www.ufc.com/news/ufc-fight-night-shanghai-2026-bonus-coverage"),
        ("Sherdog &mdash; UFC Shanghai bonuses: Song and three others earn $100,000",
         "https://www.sherdog.com/news/news/UFC-Shanghai-bonuses-Yadong-Song-3-others-earn-36100000-202571"),
        ("CBS Sports &mdash; UFC Shanghai live results and updates",
         "https://www.cbssports.com/ufc/news/ufc-fight-night-results-live-updates-umar-nurmagomedov-song-yadong/live/"),
        ("ESPN &mdash; Current and all-time UFC champions",
         "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
        ("ESPN &mdash; Strickland stuns rival Chimaev for UFC middleweight title",
         "https://www.espn.com/mma/ufc/story/_/id/48728368/strickland-stuns-chimaev-ufc-middleweight-title"),
        ("Bleacher Report &mdash; Strickland beats Chimaev by split decision at UFC 328",
         "https://bleacherreport.com/articles/25426415-sean-strickland-beats-khamzat-chimaev-split-decision-ufc-328-win-middleweight-title"),
        ("Al Jazeera &mdash; Strickland downs Chimaev on split decision",
         "https://www.aljazeera.com/sports/2026/5/10/strickland-vs-chimaev-ufc-328-strickland-downs-chimaev-on-split"),
        ("UFC.com &mdash; Welcome to the UFC: DWCS Season 10 Week 4",
         "https://www.ufc.com/news/welcome-ufc-dwcs-season-10-week-4"),
        ("Sherdog &mdash; Dana White awards five UFC contracts after DWCS Week 4",
         "https://www.sherdog.com/news/news/Dana-White-awards-5-UFC-contracts-after-wild-DWCS-Week-4-202619"),
        ("ESPN &mdash; MMA divisional rankings",
         "https://www.espn.com/mma/story/_/id/21807736/mma-divisional-rankings-ufc-pfl-rankings-weight-class"),
        ("Yahoo Sports &mdash; New UFC bantamweight rankings after Shanghai",
         "https://sports.yahoo.com/articles/ufc-bantamweight-rankings-song-shockingly-153825681.html"),
        ("UFC.com &mdash; UFC Fight Night: Nurmagomedov vs Song (event page, Aug 29, 2026)",
         "https://www.ufc.com/event/ufc-fight-night-august-29-2026"),
        ("Sky Sports &mdash; Strickland defeats Chimaev at UFC 328 to regain the middleweight title",
         "https://www.skysports.com/mma/news/19828/13542189/sean-strickland-defeats-khamzat-chimaev-in-ufc-328-to-regain-middleweight-title-after-split-decision"),
        ("CBS Sports &mdash; UFC 328 results: Strickland upsets Chimaev",
         "https://www.cbssports.com/ufc/news/ufc-328-live-updates-results-khamzat-chimaev-sean-strickland-highlights/live/"),
        ("Tapology &mdash; Dana White's Contender Series 2026",
         "https://www.tapology.com/fightcenter/promotions/2026-dana-whites-contender-series-dwcs"),
        ("TKO Group Holdings &mdash; UFC Freedom 250 delivers 34 million total global viewers",
         "https://investor.tkogrp.com/news/news-details/2026/UFC-Freedom-250-Delivers-34-Million-Total-Global-Viewers/default.aspx"),
        ("The Hollywood Reporter &mdash; UFC White House card viewership on Paramount+",
         "https://www.hollywoodreporter.com/tv/tv-news/ufc-white-house-card-8-million-viewers-paramount-plus-1236625635/"),
        ("CBS News &mdash; Paramount acquires UFC rights in a seven-year, $7.7 billion deal with TKO",
         "https://www.cbsnews.com/amp/miami/news/ufc-paramount-plus-deal-2026-streaming-cbs"),
        ("CBS Sports &mdash; 2026 UFC event schedule",
         "https://www.cbssports.com/ufc/news/2026-ufc-event-schedule-islam-makhachev-ian-machado-garry/"),
    ]))
    b.append('<div class="disc">Cards and bouts are subject to change. Odds are reproduced as quoted by '
             'the book named and move constantly; nothing here is wagering advice.</div></footer>')
    b.append('</div>' + css.STAMP_JS + CDN_JS + '</body></html>')
    write("mma-briefing.html", "\n".join(b))

if __name__ == "__main__":
    build_index(); build_cyber(); build_ws(); build_mma()
