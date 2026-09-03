# -*- coding: utf-8 -*-
"""Edits for the 9:05 AM ET Thursday, September 3, 2026 Morning Edition (pre-open, third run)."""
import io, sys

P = "/sessions/inspiring-practical-pasteur/build_0905.py"
s = io.open(P, encoding="utf-8").read()
n = 0

def rep(old, new, label):
    global s, n
    if old not in s:
        print("MISS:", label); sys.exit(1)
    if s.count(old) != 1:
        print("AMBIG(%d):" % s.count(old), label); sys.exit(1)
    s = s.replace(old, new)
    n += 1
    print("ok:", label)

# ------------------------------------------------------------------ docstring
rep('"""Daily Briefings — Thursday, September 3, 2026 · Morning Edition (~8:40 AM ET, pre-open)."""',
    '"""Daily Briefings — Thursday, September 3, 2026 · Morning Edition (~9:05 AM ET, pre-open)."""',
    "docstring")

# ------------------------------------------------------------------ summaries
rep('''SUM_WS = ("Futures are narrowly mixed before the bell &mdash; Dow contracts up about 0.2%, Nasdaq 100 "
          "contracts just below flat &mdash; as Iran's overnight strikes on Jordan, the UAE and Kuwait "
          "keep a war premium in oil and Snowflake holds a pre-market gain of more than 24%.")''',
    '''SUM_WS = ("Futures have firmed into the last half hour before the bell &mdash; Dow contracts up about "
          "0.6%, S&amp;P 500 up 0.3% &mdash; after weekly jobless claims came in at 206,000 against a "
          "205,000 consensus, while Snowflake holds a pre-market gain of about 24%.")''',
    "SUM_WS")

rep('''SUM_CY = ("A Russian national extradited from Cyprus has been indicted in San Francisco over a campaign "
          "that pushed malware-laced Excel attachments to roughly 80,000 users of a freelance-work "
          "platform, while five of the seven flaws CISA added to its KEV catalog on September 2 come "
          "due for federal agencies on Saturday.")''',
    '''SUM_CY = ("Attackers are forging administrator tokens on self-hosted JFrog Artifactory servers through "
          "CVE-2026-82329, a CVSS 9.8 authentication bypass that went from vendor disclosure to "
          "confirmed in-the-wild exploitation in roughly 72 hours and now carries a federal remediation "
          "deadline two days out.")''',
    "SUM_CY")

rep('''SUM_MMA = ("UFC 332 still has no announced main event after Valentina Shevchenko withdrew injured, with an "
           "interim women's flyweight title fight between Natalia Silva and Wang Cong reported as the "
           "target &mdash; a pairing coverage says would let Silva avenge a 2015 kickboxing loss.")''',
    '''SUM_MMA = ("UFC 332 still has neither a main event nor a co-main event a month out after Valentina "
           "Shevchenko withdrew injured, with an interim women's flyweight title fight between Natalia "
           "Silva and Wang Cong reported &mdash; but not announced &mdash; as the replacement.")''',
    "SUM_MMA")

# ------------------------------------------------------------------ CYBER: banner + stats
rep('''    b.append('<div class="banner high"><span class="k">Threat level &middot; High</span>'
             'Five actively exploited flaws &mdash; two of them scored CVSS 10.0 &mdash; carry a federal '
             'remediation deadline two days out, a second federal deadline lands eleven days out, and a '
             'critical WordPress upload bug has a public proof of concept.</div>')''',
    '''    b.append('<div class="banner high"><span class="k">Threat level &middot; High</span>'
             'Five actively exploited flaws &mdash; two scored CVSS 10.0, one a supply-chain server that '
             'holds an organisation\\'s build artifacts &mdash; carry a federal remediation deadline two '
             'days out, a second federal deadline lands eleven days out, and two healthcare data '
             'incidents disclosed this week run into the millions of records.</div>')''',
    "cy banner")

rep("""             '<div class="stat"><div class="n">80,000</div><div class="l">Freelance-platform users sent '
             'malware-laced Excel files in the charged campaign (DOJ)</div></div>'
             '<div class="stat"><div class="n">7</div><div class="l">Flaws added to CISA KEV on Sept 2, '
             'per the CISA alert page</div></div>'
             '<div class="stat"><div class="n">2 days</div><div class="l">Until the Sept 5 federal '
             'deadline for five of the seven</div></div>'
             '<div class="stat"><div class="n">9.0</div><div class="l">CVSS v3.1 of the Elementor Pro '
             'upload flaw CVE-2026-32475</div></div>'""",
    '''             '<div class="stat"><div class="n">~72 hrs</div><div class="l">From JFrog\\'s Aug 28 '
             'disclosure to watchTowr confirming exploitation on Sept 1</div></div>'
             '<div class="stat"><div class="n">2 days</div><div class="l">Until the Sept 5 federal '
             'deadline for five of the seven Sept 2 KEV additions</div></div>'
             '<div class="stat"><div class="n">9,540,683</div><div class="l">Individuals in Aesto '
             'Health\\'s breach report to HHS</div></div>'
             '<div class="stat"><div class="n">80,000</div><div class="l">Freelance-platform users sent '
             'malware-laced Excel files in the charged campaign (DOJ)</div></div>' ''',
    "cy stats")

# ------------------------------------------------------------------ CYBER: top story swap
rep('''    b.append('<h2 class="sec">Top Story</h2>')
    b.append('<div class="callout crit"><div class="k">Charged &middot; Northern District of California</div>'
             '<h3>Extradited Russian national indicted over an Excel-macro campaign aimed at 80,000 freelancers</h3>''',
    '''    b.append('<h2 class="sec">Top Story</h2>')
    b.append('<div class="callout crit"><div class="k">Exploited &middot; 2 days to the federal deadline</div>'
             '<h3>Attackers are minting their own Artifactory administrators &mdash; CVE-2026-82329</h3>'
             '<p>A critical authentication weakness in <b>JFrog Artifactory</b>, scored <b>CVSS 9.8</b>, '
             'lets an unauthenticated attacker with plain network access reach administrative privileges '
             'in the product\\'s <b>default configuration</b>, with no user interaction. JFrog\\'s advisory '
             'describes instances without an additional join key configured as receiving a "phantom" join '
             'key &mdash; which, watchTowr\\'s principal threat intelligence specialist says, attackers can '
             'abuse to forge access and mint administrator-level credentials.</p>'
             '<p>JFrog disclosed the flaw on <b>August 28, 2026</b>. On <b>September 1</b>, watchTowr '
             'reported that its Attacker Eye honeypot network was seeing attackers create administrator '
             'tokens for themselves and enumerate users, groups, credential sets and federated access '
             'topologies &mdash; roughly <b>72 hours</b> between disclosure and confirmed exploitation. '
             'CISA added the CVE to its Known Exploited Vulnerabilities catalog on <b>September 2</b>, '
             'with a federal remediation deadline of <b>September 5</b>. Self-hosted instances only; '
             'JFrog\\'s SaaS offering is not affected.</p>'
             '<p class="note">The reason this one outranks the two CVSS 10.0 flaws beside it on the same '
             'deadline is blast radius rather than score. An attacker holding a valid administrator token '
             'controls the repositories, user accounts, access permissions, build artifacts and software '
             'packages stored in the platform &mdash; which is to say the inputs to everything downstream '
             'of it.</p></div>')

    b.append('<h2 class="sec">Also Leading</h2>')
    b.append('<div class="callout"><div class="k">Charged &middot; Northern District of California</div>'
             '<h3>Extradited Russian national indicted over an Excel-macro campaign aimed at 80,000 freelancers</h3>''',
    "cy top story swap")

# demote the old "Also Leading" KEV block to a plain callout under a different heading
rep('''    b.append('<h2 class="sec">Also Leading</h2>')
    b.append('<div class="callout"><div class="k">Seven at once &middot; 2 days left</div>''',
    '''    b.append('<h2 class="sec">The KEV Batch</h2>')
    b.append('<div class="callout"><div class="k">Seven at once &middot; 2 days left</div>''',
    "cy kev heading")

# ------------------------------------------------------------------ CYBER: patch priority
rep('''    b.append('<div class="callout crit"><div class="k">Do this first &middot; 2 days left</div>'
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
             'chain.</p>''',
    '''    b.append('<div class="callout crit"><div class="k">Do this first &middot; 2 days left</div>'
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
             'Kestra come first; if it is driven by what an attacker inherits, Artifactory does.</p>''',
    "cy patch priority")

# ------------------------------------------------------------------ CYBER: threat actor spotlight (re-sourced note)
rep('''             'organisations, and links the activity to the Gentlemen ransomware operation. The pattern on display is one '
             'intrusion combining access theft, surveillance and defence evasion rather than a '
             'smash-and-grab.</p></div></div>')''',
    '''             'organisations, and links the activity to the Gentlemen ransomware operation. The pattern on display is one '
             'intrusion combining access theft, surveillance and defence evasion rather than a '
             'smash-and-grab. The reporting was restated in a search return dated today, so the item is '
             'carried on a fresh fetch rather than from the earlier edition.</p></div></div>')''',
    "cy actor")

# ------------------------------------------------------------------ CYBER: breach cards
rep("""    b.append('<div class="card"><span class="tag new">New</span><span class="tag c">Zero-day</span>'
             '<h4>PaperCut is on its third emergency patch</h4>'""",
    """    b.append('<div class="card"><span class="tag new">New</span><span class="tag m">Healthcare</span>'
             '<h4>Aesto Health reports a breach affecting 9.5 million people</h4>'
             '<p>The Alabama healthcare technology company has told the U.S. Department of Health and '
             'Human Services\\' Office for Civil Rights that the incident involves the electronic '
             'protected health information of <b>9,540,683 individuals</b>. Attackers reached part of its '
             'Amazon Web Services infrastructure <b>between December 2 and 18, 2025</b>; Aesto confirmed '
             'on <b>May 26, 2026</b> that protected health information may have been accessed or '
             'acquired. Exposed fields include names, dates of birth, medical information, driver\\'s '
             'licence numbers, financial account numbers, health insurance information, taxpayer '
             'identification numbers and Social Security numbers. At least <b>30 provider clients</b> are '
             'affected. HIPAA Journal calls it the second-largest confirmed healthcare data breach of the '
             'year to date, behind a 15 million record breach at DentaQuest. Aesto says it has found no '
             'evidence of resulting identity theft or financial fraud.</p></div>')
    b.append('<div class="card"><span class="tag c">Zero-day</span>'
             '<h4>PaperCut is on its third emergency patch</h4>'""",
    "cy aesto card")

rep('''    b.append('<div class="card"><span class="tag a">Supply chain</span>'
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
             'individuals, and no individual count is asserted here.</p></div>')''',
    '''    b.append('<div class="card"><span class="tag new">New detail</span><span class="tag m">Ongoing</span>'
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
             'individuals.</p></div>')''',
    "cy mckesson card")

# refusal note
rep('''    b.append('<div class="note"><b>Refused this run:</b> a search return surfaced the INC Ransom attack on '
             'the Pennsylvania Attorney General\\'s Office alongside September 2026 material. The '
             'underlying coverage is dated September 2025, so the item was not published as current news. '
             'This is the same mis-shelving pattern that has repeatedly surfaced last year\\'s Nevada '
             'statewide ransomware incident as a 2026 breach.</div>')''',
    '''    b.append('<div class="note"><b>Refused this run &mdash; three date mismatches.</b> '
             '(1) A search return again surfaced the INC Ransom attack on the Pennsylvania Attorney '
             'General\\'s Office alongside September 2026 material, this time with a 5.7 terabyte claim. '
             'The underlying coverage is dated September 2025; not published as current news, for the '
             'second consecutive edition. '
             '(2) A query for September 2026 threat-actor campaigns returned the <b>TeamPCP</b> '
             'supply-chain compromise of Trivy, Checkmarx KICS, LiteLLM and the Telnyx Python SDK. A '
             'dedicated follow-up dates that campaign to <b>March 19&ndash;27, 2026</b>, so it is not '
             'published as current news either. '
             '(3) The Handala group\\'s attack on Stryker appeared in the same return; it is described in '
             'a <b>first-quarter 2026</b> threat report, not as this week\\'s news. '
             'All three are the mis-shelving pattern that has repeatedly surfaced last year\\'s Nevada '
             'statewide ransomware incident as a 2026 breach.</div>')''',
    "cy refusals")

print("cyber edits done")

# ------------------------------------------------------------------ CYBER sources: add
rep('''        ("Infosecurity Magazine &mdash; Healthcare giant McKesson investigates data breach incident",
         "https://www.infosecurity-magazine.com/news/healthcare-mckesson-investigates/"),''',
    '''        ("Infosecurity Magazine &mdash; Healthcare giant McKesson investigates data breach incident",
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
        ("Unit 42 &mdash; Weaponizing the protectors: TeamPCP\\'s multi-stage supply chain attacks (dated March 2026; refused as current news)",
         "https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/"),''',
    "cy sources")

io.open(P, "w", encoding="utf-8").write(s)
print("PATCH 1 COMPLETE:", n, "edits")
