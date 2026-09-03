# -*- coding: utf-8 -*-
"""Daily Briefings — Thursday, September 3, 2026 · Morning Edition (~9:05 AM ET, pre-open)."""
import io, os, css

OUT = "/sessions/inspiring-practical-pasteur/mnt/outputs"

TV = "https://s3.tradingview.com/external-embedding/embed-widget-%s.js"

def w(name, cfg):
    return '<script src="%s" async>%s</script>' % (TV % name, cfg)

def write(fn, s):
    with io.open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        f.write(s)
    print("wrote", fn, len(s))

# ---------------------------------------------------------------- summaries
SUM_WS = ("Futures have firmed into the last half hour before the bell &mdash; Dow contracts up about "
          "0.6%, S&amp;P 500 up 0.3% &mdash; after weekly jobless claims came in at 206,000 against a "
          "205,000 consensus, while Snowflake holds a pre-market gain of about 24%.")
SUM_CY = ("Attackers are forging administrator tokens on self-hosted JFrog Artifactory servers through "
          "CVE-2026-82329, a CVSS 9.8 authentication bypass that went from vendor disclosure to "
          "confirmed in-the-wild exploitation in roughly 72 hours and now carries a federal remediation "
          "deadline two days out.")
SUM_MMA = ("UFC 332 still has neither a main event nor a co-main event a month out after Valentina "
           "Shevchenko withdrew injured, with an interim women's flyweight title fight between Natalia "
           "Silva and Wang Cong reported &mdash; but not announced &mdash; as the replacement.")

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
             'Five actively exploited flaws &mdash; two scored CVSS 10.0, and one in the server that '
             'holds an organisation\'s build artifacts &mdash; carry a federal remediation deadline two '
             'days out, a second federal deadline lands eleven days out, and two healthcare incidents in '
             'the news this week involve millions of records between them.</div>')

    b.append('<div class="stats">'
             '<div class="stat"><div class="n">~72 hrs</div><div class="l">From JFrog\'s Aug 28 '
             'disclosure to watchTowr confirming exploitation on Sept 1</div></div>'
             '<div class="stat"><div class="n">2 days</div><div class="l">Until the Sept 5 federal '
             'deadline for five of the seven Sept 2 KEV additions</div></div>'
             '<div class="stat"><div class="n">9,540,683</div><div class="l">Individuals in Aesto '
             'Health\'s breach report to HHS</div></div>'
             '<div class="stat"><div class="n">80,000</div><div class="l">Freelance-platform users sent '
             'malware-laced Excel files in the charged campaign (DOJ)</div></div>' 
             '</div>')

    b.append('<h2 class="sec">Top Story</h2>')
    b.append('<div class="callout crit"><div class="k">Exploited &middot; 2 days to the federal deadline</div>'
             '<h3>Attackers are minting their own Artifactory administrators &mdash; CVE-2026-82329</h3>'
             '<p>A critical authentication weakness in <b>JFrog Artifactory</b>, scored <b>CVSS 9.8</b>, '
             'lets an unauthenticated attacker with plain network access reach administrative privileges '
             'in the product\'s <b>default configuration</b>, with no user interaction. JFrog\'s advisory '
             'describes instances without an additional join key configured as receiving a "phantom" join '
             'key &mdash; which, watchTowr\'s principal threat intelligence specialist says, attackers can '
             'abuse to forge access and mint administrator-level credentials.</p>'
             '<p>JFrog disclosed the flaw on <b>August 28, 2026</b>. On <b>September 1</b>, watchTowr '
             'reported that its Attacker Eye honeypot network was seeing attackers create administrator '
             'tokens for themselves and enumerate users, groups, credential sets and federated access '
             'topologies &mdash; roughly <b>72 hours</b> between disclosure and confirmed exploitation. '
             'CISA added the CVE to its Known Exploited Vulnerabilities catalog on <b>September 2</b>, '
             'with a federal remediation deadline of <b>September 5</b>. Self-hosted instances only; '
             'JFrog\'s SaaS offering is not affected.</p>'
             '<p class="note">The reason this one outranks the two CVSS 10.0 flaws beside it on the same '
             'deadline is blast radius rather than score. An attacker holding a valid administrator token '
             'controls the repositories, user accounts, access permissions, build artifacts and software '
             'packages stored in the platform &mdash; which is to say the inputs to everything downstream '
             'of it.</p></div>')

    b.append('<h2 class="sec">Also Leading</h2>')
    b.append('<div class="callout"><div class="k">Charged &middot; Northern District of California</div>'
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

    b.append('<h2 class="sec">The KEV Batch</h2>')
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
             '<h3>JFrog Artifactory &mdash; CVE-2026-82329 (CVSS 9.8), due Saturday, September 5</h3>'
             '<p>Patch self-hosted Artifactory first. It is under confirmed in-the-wild exploitation, it '
             'is exploitable in the default configuration without credentials, and a successful attacker '
             'ends up an administrator of the server that holds your build artifacts and packages. JFrog '
             'shipped the fix on August 28.</p>'
             '<p>The same September 5 deadline covers SonicWall SMA1000 &mdash; CVE-2026-83548 '
             '(CVSS 10.0), an unauthenticated server-side request forgery in the Appliance Work Place '
             'chained with the authenticated OS command-injection flaw CVE-2026-83549 (CVSS 7.8) for '
             'unauthenticated remote code execution, both exploited in the wild, on models 6210, 7210 and '
             '8200v, hotfixes 12.4.3-03526 and 12.5.0-02952 and later &mdash; plus Sangoma Switchvox '
             '(CVE-2026-9586) and Kestra OSS (CVE-2026-49869), the latter also CVSS 10.0 and used to '
             'plant a cryptocurrency miner. If your triage is driven purely by score, SonicWall and '
             'Kestra come first; if it is driven by what an attacker inherits, Artifactory does.</p>'
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
             'smash-and-grab. The reporting carries today\'s date.</p></div></div>')

    b.append('<h2 class="sec">Breaches &amp; Incidents</h2>')
    b.append('<div class="cards two">')
    b.append('<div class="card"><span class="tag new">New</span><span class="tag m">Healthcare</span>'
             '<h4>Aesto Health reports a breach affecting 9.5 million people</h4>'
             '<p>The Alabama healthcare technology company has told the U.S. Department of Health and '
             'Human Services\' Office for Civil Rights that the incident involves the electronic '
             'protected health information of <b>9,540,683 individuals</b>. Attackers reached part of its '
             'Amazon Web Services infrastructure <b>between December 2 and 18, 2025</b>; Aesto confirmed '
             'on <b>May 26, 2026</b> that protected health information may have been accessed or '
             'acquired. Exposed fields include names, dates of birth, medical information, driver\'s '
             'licence numbers, financial account numbers, health insurance information, taxpayer '
             'identification numbers and Social Security numbers. At least <b>30 provider clients</b> are '
             'affected. It is reported as the second-largest confirmed healthcare data breach of the '
             'year to date, behind a 15 million record breach at DentaQuest. Aesto says it has found no '
             'evidence of resulting identity theft or financial fraud.</p></div>')
    b.append('<div class="card"><span class="tag c">Zero-day</span>'
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
    b.append('<div class="card"><span class="tag new">New detail</span><span class="tag m">Ongoing</span>'
             '<h4>McKesson: an 8-K, a vishing call and a $55.2 million demand</h4>'
             '<p>McKesson detected unauthorised activity within third-party software applications on '
             '<b>August 25, 2026</b> and filed a Form 8-K with the SEC. Initial findings confirm data '
             'exfiltration affecting its <b>Oncology &amp; Multispecialty</b> and <b>Medical-Surgical</b> '
             'business units. Coverage of the ShinyHunters claim describes the access route as a voice '
             'phishing call in which the group spoofed a real support employee, retrieved employee '
             'credentials from Okta and reached connected Salesforce and Snowflake environments. The '
             'group claims <b>1 terabyte</b> of data and a <b>$55.2 million</b> ransom demand; McKesson '
             'is reported to have refused to negotiate, and says the attackers no longer have access.</p>'
             '<p class="note">The record count is claimed, disputed and not a headcount: one set of '
             'coverage puts the claim at <b>284 million</b> raw database records and another at '
             '<b>248 million</b>. Both are printed; neither is adopted, and neither is a count of unique '
             'individuals.</p></div>')
    b.append('</div>')
    b.append('<div class="note"><b>Refused this run &mdash; three date mismatches.</b> '
             '(1) A search return again surfaced the INC Ransom attack on the Pennsylvania Attorney '
             'General\'s Office alongside September 2026 material, this time carrying a claimed volume '
             'of stolen data. The underlying coverage is dated September 2025; the item is not published '
             'as current news for the second consecutive edition, and the claimed figure is not '
             'reprinted. '
             '(2) A query for September 2026 threat-actor campaigns returned the <b>TeamPCP</b> '
             'supply-chain compromise of Trivy, Checkmarx KICS, LiteLLM and the Telnyx Python SDK. A '
             'dedicated follow-up dates that campaign to <b>March 19&ndash;27, 2026</b>, so it is not '
             'published as current news either. '
             '(3) The Handala group\'s attack on Stryker appeared in the same return; it is described in '
             'a <b>first-quarter 2026</b> threat report, not as this week\'s news. '
             'All three are the mis-shelving pattern that has repeatedly surfaced last year\'s Nevada '
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
             '<div class="note">The PaperCut pair was dropped from the 8:16 AM edition for want of a '
             'restated deadline, restored at 8:49 AM, and re-verified again for this edition: CISA added '
             'both CVEs on Monday, August 31 with a September 14 remediation date, and the vendor scores '
             'them CVE-2026-81578 at CVSS 8.8 and CVE-2026-82078 at 9.4. Coverage this week describes '
             'the attacks escalating from reconnaissance to hands-on-keyboard activity. Countdowns above '
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
        ("Dark Reading &mdash; Attackers jump on critical Artifactory flaw after disclosure",
         "https://www.darkreading.com/application-security/attackers-pounce-critical-artifactory-flaw-disclosure"),
        ("SecurityWeek &mdash; Critical JFrog Artifactory vulnerability reportedly exploited in the wild",
         "https://www.securityweek.com/critical-jfrog-artifactory-vulnerability-reportedly-exploited-in-the-wild/"),
        ("Cyber Security News &mdash; JFrog Artifactory auth bypass exploited",
         "https://cybersecuritynews.com/jfrog-artifactory-auth-bypass-exploited/"),
        ("SOC Prime &mdash; CVE-2026-82329 analysis",
         "https://socprime.com/blog/cve-2026-82329-analysis/"),
        ("BleepingComputer &mdash; Aesto Health says data breach affects over 9.5 million patients",
         "https://www.bleepingcomputer.com/news/security/aesto-health-says-data-breach-affects-over-95-million-patients/"),
        ("HIPAA Journal &mdash; Aesto Health data breach affects 9.5 million patients",
         "https://www.hipaajournal.com/aesto-health-data-breach/"),
        ("SecurityWeek &mdash; 9.5 million impacted by Aesto Health data breach",
         "https://www.securityweek.com/9-5-million-impacted-by-aesto-health-data-breach/"),
        ("Security Affairs &mdash; Attackers access Aesto Health AWS infrastructure",
         "https://securityaffairs.com/198250/data-breach/attackers-access-aesto-health-aws-infrastructure-exposing-9-5-million-records.html"),
        ("Help Net Security &mdash; ShinyHunters claims it stole 284 million patient records from McKesson",
         "https://www.helpnetsecurity.com/2026/08/31/healthcare-company-mckesson-data-breach/"),
        ("BleepingComputer &mdash; McKesson discloses breach after ShinyHunters claims patient data theft",
         "https://www.bleepingcomputer.com/news/security/mckesson-discloses-breach-after-shinyhunters-claims-patient-data-theft/"),
        ("TechCrunch &mdash; Hackers claim millions of patient records stolen in McKesson breach",
         "https://techcrunch.com/2026/08/31/hackers-claim-millions-of-patient-records-stolen-during-data-breach-at-healthcare-giant-mckesson/"),
        ("Unit 42 &mdash; Weaponizing the protectors: TeamPCP\'s multi-stage supply chain attacks (dated March 2026; refused as current news)",
         "https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/"),
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
    b.append('<div class="callout"><div class="k">Pre-open &middot; ~9:05 AM ET</div>'
             '<h3>Futures firm up into the bell as claims land at 206,000</h3>'
             '<p>U.S. stock futures have turned higher across the board in the last half hour before the '
             'open. Dow futures are at <b>53,430.00</b>, up 309.00 points or <b>0.58%</b>; S&amp;P 500 '
             'futures at <b>7,699.50</b>, up 23.00 or <b>0.30%</b>; Nasdaq futures at <b>29,233.00</b>, '
             'up 46.75 or <b>0.16%</b>. Separately, Dow futures are described as up 0.2% with S&amp;P 500 '
             'contracts little changed and Nasdaq 100 contracts just below flat &mdash; a softer '
             'characterisation than the point-level quotes above, printed rather than reconciled.</p>'
             '<p>The Labor Department released its weekly claims report at 8:30 AM ET: initial jobless '
             'claims for the week ending <b>August 29</b> rose to <b>206,000</b>, above the 205,000 '
             'consensus, against <b>204,000</b> the week before &mdash; itself revised up from the '
             '203,000 first reported. The 8:16 and 8:49 AM editions of this page withheld the print '
             'because no source fetched for them stated it; it is published here on a fetch that '
             'does.</p>'
             '<p>Iran struck U.S. allies Jordan, the United Arab Emirates and Kuwait with missiles and '
             'drones overnight in retaliation for the latest round of American airstrikes, and its '
             'Revolutionary Guards say two oil tankers hit naval mines attempting to transit the Strait of '
             'Hormuz. TheStreet notes oil has "rebuilt some geopolitical premium, creating another '
             'potential inflationary headache at a time when markets are already debating whether US '
             'rates need to move higher." Brent is the contested figure this morning &mdash; see the '
             'rates and commodities table. Gold futures are up 1.81% at $4,494.70 an ounce in early '
             'trading and silver futures up 1.42% at $66.39. Friday\'s August employment report is the '
             'last labour reading the FOMC sees before its September 16 decision.</p>'
             '<p class="note">Futures have moved with each edition this morning: Dow contracts read '
             '+0.07% at 8:16 AM, +0.29% at 8:49 AM and +0.58% here. That is drift across pre-market '
             'trade, not a disagreement between sources. Nothing on this page is a live Thursday session '
             'price &mdash; the opening bell is 9:30 AM ET.</p></div>')

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
             'and are not treated as such. This run\'s fetch gives the pre-market move as 24%; the '
             '8:49 AM fetch gave more than 24%.</p></div>')
    b.append('<div class="card"><span class="tag new">Now with figures</span><span class="tag c">&minus;7%</span>'
             '<h4>The Campbell\'s Company</h4><p>Down almost 7% pre-market after guiding fiscal 2027 '
             'earnings to <b>$1.65 to $1.80 a share</b> against a FactSet consensus of <b>$1.83</b>. The '
             'two earlier editions today carried this move without figures because none had been '
             'sourced; the range is published here on a fetch that states it.</p></div>')
    b.append('<div class="card"><span class="tag c">&minus;2.5%</span>'
             '<h4>Broadcom</h4><p>Lower after a fourth-quarter revenue forecast of $34.8 billion against '
             'a $35.03 billion estimate. The "fourth quarter" label is CNBC\'s own wording for the '
             'guidance period; no fiscal-period label is being inferred here.</p></div>')
    b.append('<div class="card"><span class="tag a">Software bid</span>'
             '<h4>Datadog, ServiceNow and Salesforce</h4><p>Snowflake\'s rally lifted its software peers: '
             'Datadog up more than 5%, ServiceNow up 3% and Salesforce up just over 1.5%. Salesforce is '
             'new to this list on the fetch made for this edition.</p></div>')
    b.append('<div class="card"><span class="tag c">&minus;3%</span>'
             '<h4>Hewlett Packard Enterprise</h4><p>The enterprise technology company slipped 3% '
             'pre-market. The figure was not restated in the 8:49 AM edition and is carried here only '
             'because this run\'s fetch states it again.</p></div>')
    b.append('</div>')

    b.append('<h2 class="sec">Chart of the Day &mdash; Snowflake (SNOW)</h2>')
    b.append('<div class="panel" style="padding:8px">' + w("mini-symbol-overview",
             '{"symbol":"NYSE:SNOW","width":"100%","height":240,"locale":"en","dateRange":"1D",'
             '"colorTheme":"dark","isTransparent":true,"autosize":false}') + '</div>')
    b.append('<div class="note">Snowflake is the largest pre-market move among the large-cap names in '
             'the section above, which are the names this run\'s movers fetch identified. No claim is '
             'made about the pre-market list as a whole: an earlier edition today sourced several '
             'thinly traded small caps with larger percentage moves, and those figures were not '
             're-fetched for this edition, so they are not restated here.</div>')

    b.append('<h2 class="sec">Sector Heat &mdash; live</h2>')
    b.append('<div class="panel" style="padding:8px">' + w("stock-heatmap",
             '{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change",'
             '"grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,'
             '"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,'
             '"isMonoSize":false,"width":"100%","height":420}') + '</div>')
    b.append('<div class="note">Single-session sector leadership is <b>not</b> asserted for a '
             'thirteenth consecutive edition. The only same-day reading this run\'s sector fetch offers '
             'is energy up 1.3% on <b>August 31</b>, which is not Wednesday\'s session. The return '
             'describes August 31 as the last trading day before September 2; September 1 was itself a '
             'trading day, so that framing is not adopted either. Year-to-date readings are the firm '
             'ones: energy leads, '
             'returning as <span class="up">+43% YTD</span> for the sector and <span class="up">+42.32% '
             'YTD</span> for the XLE ETF in the same return &mdash; both printed, neither adopted, and '
             'XLE is separately given as +40.82% over the past year. At the other end, communication '
             'services (XLC) is <span class="down">&minus;5.60% YTD</span> and consumer discretionary '
             '(XLY) <span class="down">&minus;3.02% YTD</span> &mdash; the latter against '
             '&minus;2.3% in the 8:49 AM edition, printed, not adopted. The materials figure carried '
             'earlier today was not re-sourced for this edition and is not repeated.</div>')

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
    b.append('<div class="note">These three closes have now returned identical on <b>eight</b> '
             'consecutive fetches across editions. On the streak framing, this run\'s return says all '
             'three indices snapped a <b>three-day</b> losing streak, matching CNBC and against the '
             '<b>two-day</b> reading carried in both earlier editions today. Neither is adopted, but the '
             'three-day version has now returned on more fetches than the two-day one. Only Wednesday\'s '
             'official closes are listed &mdash; earlier sessions in the week were not re-sourced in '
             'this run.</div>')

    b.append('<h2 class="sec">Rates, Bonds &amp; Commodities</h2>')
    b.append('<div class="tblwrap"><table>'
             '<tr><th>Instrument</th><th>Level</th><th>Note</th></tr>'
             '<tr><td>10-year Treasury yield</td><td class="mono">4.796% prior close</td>'
             '<td>Investing.com gives a previous close of 4.796% and a day\'s range of '
             '4.765&ndash;4.820%. Wednesday\'s intraday high of 4.814% has been described as the highest '
             'since November 2023.</td></tr>'
             '<tr><td>WTI crude</td><td class="mono">$90.87, +0.72%</td>'
             '<td>This run\'s quote. Earlier editions today carried $90.76 as the September 2 close, a '
             'Thursday futures quote of $91.01, and $90.51 and $89.62 from other feeds. The readings sit '
             'within about $1.25 of each other; no single Thursday level is adopted.</td></tr>'
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
             '<li><b>Released this morning &mdash; initial jobless claims came in at 206,000.</b> The '
             'week-ending-August-29 print landed above the 205,000 consensus and above the prior week\'s '
             '204,000, which was itself revised up from 203,000.</li>'
             '<li><b>Also released at 8:30 AM ET &mdash; July international trade in goods and '
             'services.</b> No actual print appeared in anything fetched for this edition, so none is '
             'published. The consensus was &minus;$71.2 billion against a prior &minus;$73.26 '
             'billion.</li>'
             '<li><b>Friday, September 4, 8:30 AM ET &mdash; the August employment report.</b> The '
             'forecasts fetched for this edition spread widely: about <b>58,000</b> jobs added in one '
             'consensus reading and <b>53,000</b> in another, against <b>80,000</b> from Wells Fargo '
             'economists and a below-consensus <b>25,000 decline</b> from Fifth Third. Unemployment is '
             'expected to hold at <b>4.1%</b>. July payrolls fell 23,000, and Wednesday\'s ADP report '
             'put private payrolls up just <b>38,000</b> in August, fewer than expected. It is the last '
             'labour reading the FOMC sees before its decision.</li>'
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
             'October 3. The event is a month away and has <b>neither a main event nor a co-main '
             'event</b>. Reporting this week says the UFC is '
             'working on an interim women\'s flyweight title fight between <b>Natalia Silva</b> and '
             '<b>Wang Cong</b> as the replacement main event.</p>'
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
             '(DraftKings); another book is quoted at &minus;625 / +450, and a third reading has '
             '&minus;500 / +400. All three are printed; none is adopted. The line has moved a long way '
             'from the opening price of Parnasse &minus;357 / Hooker +275; one implied-probability '
             'reading puts Parnasse at 83%. The Ziam quote returned &minus;145 / +125 in the previous '
             'edition against &minus;155 earlier, and was not restated this run.</p></div>')
    b.append('<div class="card"><div class="k">Sat, Sept 12 &middot; Desert Diamond Arena, Glendale</div>'
             '<h4>Noche UFC: Silva vs. Delgado</h4>'
             '<p>Brazil\'s Jean Silva headlines at featherweight against Arizona\'s Jose Miguel Delgado, '
             'who stepped in after Yair Rodr&iacute;guez was forced out injured. The card also carries '
             'Waldo Cortes-Acosta vs. Curtis Blaydes at heavyweight, Manon Fiorot vs. Alexa Grasso at '
             'women\'s flyweight, Brandon Moreno vs. Joseph Morales at flyweight, David Mart&iacute;nez '
             'vs. Dan Ige at bantamweight and Tommy McMillen vs. Marwan Rahiki at featherweight. Doors '
             'open 10:00 AM PT, prelims 11:00 AM PT, main card live on Paramount+ at 2:00 PM PT. No '
             'headline odds were stated in the material fetched this run, so none are printed.</p></div>')
    b.append('<div class="card"><div class="k">Sat, Sept 19 &middot; Crypto.com Arena, Los Angeles</div>'
             '<h4>UFC 331: Van vs. Pantoja 2</h4>'
             '<p>Thirteen fights. Flyweight champion Joshua Van rematches Alexandre Pantoja, whom he beat '
             'for the belt at UFC 323 in December 2025 by technical knockout 26 seconds into round one '
             'after Pantoja suffered an arm injury. Arman Tsarukyan vs. Mauricio Ruffy is a five-round '
             'lightweight co-main. Early prelims about 5 PM ET, prelims 7 PM ET, main card 9 PM ET on '
             'Paramount+. No headline odds stated this run.</p></div>')
    b.append('<div class="card"><div class="k">Sat, Sept 26 &middot; Meta APEX, Las Vegas</div>'
             '<h4>UFC Fight Night: Rosas Jr. vs. Barcelos</h4>'
             '<p>Also billed UFC Vegas 121 and UFC Fight Night 289. Twenty-one-year-old bantamweight '
             'prospect Raul Rosas Jr. headlines his first UFC card against Brazilian veteran Raoni '
             'Barcelos, an eighteen-year age gap. The bantamweight and women\'s strawweight finals of '
             'The Ultimate Fighter: Team Cormier vs. Team Bisping are also scheduled for this event. '
             'Prelims 5 PM ET, main card 8 PM ET on Paramount+. No headline odds stated this run.</p></div>')
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
    b.append('<div class="note">This run\'s results fetch restated the main event and the bonus '
             'awards; the co-main and the Asakura bout are carried from this desk\'s verified record of '
             'the card. It is not the full results table, and no card depth is asserted because none has '
             'been re-sourced. Nurmagomedov entered a '
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
            '<p>Season 10, Week 5 runs Tuesday, September 8 from the Meta APEX in Las Vegas &mdash; '
             'five fights, headlined by undefeated light heavyweights <b>Quentin Pasley</b> and '
             '<b>Arlind Berisha</b>. The rest of the card: Isaac Moreno vs. Reginaldo Junior at '
             'welterweight, Martin Kozak vs. Christian Echols at middleweight, Apollo Gomes vs. Won Il '
             'Kwon at bantamweight and Colton Loud vs. Christian Natividad at flyweight. The earlier '
             'editions today had surnames only; full names come from this run\'s fetch. Broadcast '
             'listings disagree &mdash; one carries the card on ESPN, another on Paramount+ at 7:00 PM '
             '&mdash; and neither is adopted.</p></div>')
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
             '<li>No pound-for-pound or divisional ranking is asserted this edition. The aggregated '
             'rankings source that supplied them in earlier editions is the same one that returned two '
             'wrong champions for this build, so its unverified positions are not carried forward.</li>'
             '<li>Song Yadong\'s post-Shanghai climb at bantamweight &mdash; reported in the earlier edition '
             'as a move from No. 7 to No. 4 &mdash; was not restated in this run\'s rankings return, so '
             'it is recorded here with that provenance rather than asserted as the current ranking.</li></ul>'
             '<h4 style="margin-top:14px">Business &amp; broadcast</h4>'
             '<ul class="b">'
             '<li>Paramount is in the first year of a <b>seven-year, $7.7 billion</b> U.S. media-rights '
             'deal with TKO Group\'s UFC, announced in August 2025 and beginning this year &mdash; an '
             'average of <b>$1.1 billion a year</b>, against the roughly $550 million a year ESPN was '
             'reported to pay under the previous arrangement.</li>'
             '<li>The deal covers all <b>43 annual UFC live events</b>, streamed exclusively in the U.S. '
             'on Paramount+: <b>30 Fight Nights and 13 marquee events</b> a year across CBS and '
             'Paramount+. It ends the pay-per-view model ESPN used, with events carried at no extra '
             'charge.</li>'
             '<li>The UFC Freedom 250 viewership figures carried in the 8:49 AM edition were not '
             'restated in this run\'s fetch and are not repeated here. No gate figure was stated in '
             'anything fetched this run, so none is printed.</li>'
             '</ul></div>')

    b.append('<h2 class="sec">Champions Board</h2>')
    b.append('<div class="tblwrap"><table><tr><th>Division</th><th>Champion</th><th>Note</th></tr>'
             '<tr><td><b>Heavyweight</b></td><td>Tom Aspinall</td><td>Undisputed since June 21, 2025. '
             '<b>Interim:</b> Ciryl Gane, since June 14, 2026.</td></tr>'
             '<tr><td><b>Light Heavyweight</b></td><td>Carlos Ulberg</td>'
             '<td>Won the vacant belt at UFC 327 by first-round knockout of Ji&#345;&iacute; '
             'Proch&aacute;zka. This desk\'s standing record dates the card April 11, 2026; Al Jazeera '
             'files its report under April 12. The discrepancy is printed, not resolved.</td></tr>'
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
    b.append('<div class="note"><b>Corrected again this run &mdash; and this time two cells were '
             'wrong, not one.</b> The aggregated champions list fetched for this edition returned '
             '<b>Khamzat Chimaev</b> at middleweight for the thirtieth time, and also returned '
             '<b>Alex Pereira</b> at light heavyweight, dating that reign to a win over Magomed Ankalaev '
             'in October 2025. Both are wrong, and both were re-verified against fresh fetches this run. '
             'Middleweight: Sean Strickland took the belt from Chimaev by split decision at UFC 328 at '
             'the Prudential Center in Newark &mdash; two judges 48-47 Strickland, one 48-47 Chimaev '
             '&mdash; per ESPN ("Strickland stuns rival Chimaev"), Bleacher Report, CBS Sports, Sky '
             'Sports and Al Jazeera; Strickland moved to 31-7 and handed Chimaev, 17-1, his first defeat. '
             'Light heavyweight: <b>Carlos Ulberg</b> knocked out Ji&#345;&iacute; Proch&aacute;zka at '
             '3:45 of round one at UFC 327 at the Kaseya Center in Miami to win the <b>vacant</b> belt '
             '&mdash; he blew out his right knee in the opening minute and won with a left hook while '
             'cornered &mdash; per ESPN, UFC.com and Al Jazeera. He is the third City Kickboxing fighter '
             'to win a UFC title, after Alexander Volkanovski and Israel Adesanya. Ten of the list\'s '
             'twelve cells were right. Sources also disagree on the date of UFC 328 &mdash; Al Jazeera '
             'files it under May 10, 2026, while this desk\'s standing record is May 9, 2026; the '
             'discrepancy is printed rather than silently resolved, and no weekday is attached to '
             'either.</div>')

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
        ("ESPN &mdash; UFC 327 results: Carlos Ulberg stuns Ji&#345;&iacute; Proch&aacute;zka to win the light heavyweight title",
         "https://www.espn.com/mma/story/_/id/48432076/ufc-327-live-results-analysis-ji%C5%99i-prochazka-vs-carlos-ulberg-light-heavyweight-championship"),
        ("UFC.com &mdash; UFC 327: Proch&aacute;zka vs Ulberg results",
         "https://www.ufc.com/news/ufc-327-results-prochazka-vs-ulberg-main-card-highlights-winners-interviews"),
        ("Al Jazeera &mdash; UFC 327: Ulberg wins the light-heavyweight belt with a knockout",
         "https://www.aljazeera.com/sports/2026/4/12/ufc-327-ulberg-wins-light-heavyweight-belt-with-knockout-in-front-of-trump"),
        ("ESPN &mdash; Dana White&#39;s Contender Series Season 10 Week 5 fight centre",
         "https://www.espn.com/mma/fightcenter/_/id/600060736/league/ufc"),
        ("Tapology &mdash; Contender Series 2026: Week 5",
         "https://www.tapology.com/fightcenter/events/142724-contender-series-2026-week-5"),
        ("Wikipedia &mdash; UFC Fight Night: Silva vs. Delgado (card and start times)",
         "https://en.wikipedia.org/wiki/UFC_Fight_Night:_Silva_vs._Delgado"),
        ("Yahoo Sports &mdash; Raul Rosas Jr. vs. Raoni Barcelos headlines UFC Vegas 121 on Sept. 26",
         "https://sports.yahoo.com/articles/raul-rosas-jr-vs-raoni-220000231.html"),
        ("UFC.com &mdash; UFC Fight Night, September 26, 2026",
         "https://www.ufc.com/event/ufc-fight-night-september-26-2026"),
        ("Rotowire &mdash; Hooker vs. Parnasse odds, September 5, 2026",
         "https://www.rotowire.com/betting/mma/fight/salahdine-parnasse-vs-dan-hooker-odds-2026-09-05-5365"),
        ("MMA Odds Breaker &mdash; Opening betting odds for UFC Paris: Hooker vs. Parnasse",
         "https://www.mmaoddsbreaker.com/fight-odds/opening-odds/161246-opening-betting-odds-for-ufc-paris-hooker-vs-parnasse/"),
        ("CBS News &mdash; Paramount acquires UFC rights in a seven-year, $7.7 billion deal with TKO",
         "https://www.cbsnews.com/news/ufc-paramount-plus-deal-2026-streaming-cbs/"),
        ("CNBC &mdash; Paramount buys UFC rights in $7.7 billion, seven-year deal",
         "https://www.cnbc.com/2025/08/11/paramount-buys-ufc-rights-skydance-merger.html"),
        ("Sportico &mdash; UFC media deal: $7.7 billion Paramount rights fee ends pay-per-views",
         "https://www.sportico.com/leagues/other-sports/2025/ufc-paramount-cbs-media-deal-streaming-contract-2026-1234866546/"),
        ("Sky Sports &mdash; Strickland defeats Chimaev at UFC 328 to regain the middleweight title",
         "https://www.skysports.com/mma/news/19828/13542189/sean-strickland-defeats-khamzat-chimaev-in-ufc-328-to-regain-middleweight-title-after-split-decision"),
        ("CBS Sports &mdash; UFC 328 results: Strickland upsets Chimaev",
         "https://www.cbssports.com/ufc/news/ufc-328-live-updates-results-khamzat-chimaev-sean-strickland-highlights/live/"),
        ("Tapology &mdash; Dana White's Contender Series 2026",
         "https://www.tapology.com/fightcenter/promotions/2026-dana-whites-contender-series-dwcs"),
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
