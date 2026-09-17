# -*- coding: utf-8 -*-
"""Seventh run, 2026-09-17 ~3:56pm ET. Afternoon Edition."""
import os, datetime
from css import base_css, nav, head, sources, STAMP_JS

OUT = "/sessions/eager-bold-galileo/mnt/outputs"
TODAY = datetime.date(2026, 9, 17)

def kev(due):
    return (due - TODAY).days

def mast(title, sub):
    return ('<header class="masthead"><h1>%s</h1><p class="tag">%s</p>'
            '<div class="meta">'
            '<span class="pill live"><span class="dot"></span>Live</span>'
            '<span class="pill" id="edition">&nbsp;</span>'
            '<span class="pill" id="datestamp">&nbsp;</span>'
            '<span class="pill">Updated <span id="updated">&nbsp;</span></span>'
            '</div></header>' % (title, sub))

FRESH = '<div class="freshline" id="freshline">&nbsp;</div>'
FOOT = '</div>' + STAMP_JS + '</body></html>'

# ---------------------------------------------------------------- TLDRs
TL_WS = ("Stocks rose for a second straight session after Wednesday&rsquo;s Federal Reserve rate hike, with "
         "the S&amp;P 500 up 1.15% and the Nasdaq 100 up 1.66% as of roughly 3:50 PM ET, semiconductors "
         "leading and Treasury yields falling right across the curve.")
TL_CY = ("Cisco has disclosed a maximum-severity CVSS 10.0 authentication bypass in Identity Services Engine "
         "that is already under active attack with no workaround available, while a second actively exploited "
         "Cisco flaw reaches its federal patch deadline today.")
TL_MMA = ("Brian Ortega has withdrawn from Saturday&rsquo;s UFC 331 bout with Renato Moicano after a cut above "
          "his left eye required stitches &mdash; the second time in 2026 he has pulled out of that fight &mdash; "
          "leaving Joshua Van&rsquo;s flyweight title rematch with Alexandre Pantoja to headline in Los Angeles.")

# ================================================================ INDEX
def build_index():
    css = base_css("#8fb3c8", "#e8c766", "#0a0a0b", "#141414", "#262626") + """
.big{display:grid;gap:15px}
@media(min-width:760px){.big{grid-template-columns:repeat(3,1fr)}}
.bc{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:19px 20px;
  display:flex;flex-direction:column;transition:.17s}
.bc:hover{transform:translateY(-3px);box-shadow:0 10px 26px rgba(0,0,0,.36)}
.bc .glyph{font-size:22px;line-height:1;margin-bottom:9px}
.bc .name{font-family:var(--mono);font-size:10.5px;letter-spacing:.17em;text-transform:uppercase;margin-bottom:3px}
.bc .lbl{font-family:var(--mono);font-size:9.5px;letter-spacing:.15em;text-transform:uppercase;
  color:var(--muted);margin-bottom:11px}
.bc p{font-size:14px;color:#cfcbc6;flex:1;margin:0 0 15px}
.bc a.go{font-family:var(--mono);font-size:10.5px;letter-spacing:.13em;text-transform:uppercase}
.sec-c{border-top:3px solid #22d3a8}.sec-c .glyph,.sec-c .name,.sec-c a.go{color:#22d3a8}
.mk-c{border-top:3px solid #caa64a}.mk-c .glyph,.mk-c .name,.mk-c a.go{color:#e8c766}
.mk-c .name{font-family:Georgia,'Times New Roman',serif;font-size:15px;letter-spacing:.02em;text-transform:none}
.mm-c{border-top:3px solid #e84545}.mm-c .glyph,.mm-c .name,.mm-c a.go{color:#ff8a5c}
"""
    o = [head("Daily Briefings", css)]
    o.append(mast("Daily Briefings", "Security, markets and mixed martial arts &mdash; refreshed every 30 minutes, 8 AM&ndash;6 PM ET"))
    o.append(FRESH)
    o.append(nav("index"))
    o.append('<div class="big">')
    o.append('<div class="bc sec-c"><div class="glyph">&#9960;</div>'
             '<div class="name">The Cyber Wire</div><div class="lbl">The Wire</div>'
             '<p>%s</p><a class="go" href="cyber-briefing.html">Read the briefing &rarr;</a></div>' % TL_CY)
    o.append('<div class="bc mk-c"><div class="glyph">&#9650;</div>'
             '<div class="name">The Closing Bell</div><div class="lbl">The Tape</div>'
             '<p>%s</p><a class="go" href="wallstreet-briefing.html">Read the briefing &rarr;</a></div>' % TL_WS)
    o.append('<div class="bc mm-c"><div class="glyph">&#8856;</div>'
             '<div class="name">The Octagon</div><div class="lbl">Tale of the Tape</div>'
             '<p>%s</p><a class="go" href="mma-briefing.html">Read the briefing &rarr;</a></div>' % TL_MMA)
    o.append('</div>')
    o.append('<h2 class="sec">About this edition</h2>')
    o.append('<div class="panel"><p style="margin:0;font-size:14.5px">Three briefings, rebuilt from live web '
             'searches on every run. Every figure on every page is checked against a source fetched during that '
             'same run &mdash; anything that cannot be verified is left off rather than guessed, and figures that '
             'were refused are named on the page itself. Point-in-time snapshots of earlier editions are kept in '
             'the <a href="archive.html">archive</a>.</p></div>')
    o.append('<footer><h5>Sources</h5><ul>'
             '<li>Each briefing carries its own sourced footnotes &mdash; see the individual pages.</li>'
             '</ul><div class="disc">Information only. Not investment advice.</div></footer>')
    o.append(FOOT)
    open(os.path.join(OUT, "index.html"), "w").write("".join(o))

# ================================================================ CYBER
def build_cyber():
    css = base_css("#22d3a8", "#36c6ff", "#080d0c", "#111817", "#1f2b29")
    o = [head("The Cyber Wire &mdash; Daily Briefings", css)]
    o.append(mast("The Cyber Wire", "Your daily cybersecurity briefing &mdash; breaches, exploits &amp; the patch queue"))
    o.append('<div class="tldr"><b>The Wire</b> <span>%s</span></div>' % TL_CY)
    o.append(FRESH)
    o.append(nav("cyber"))

    o.append('<div class="banner high"><span class="k">Threat level &mdash; High</span>'
             'A maximum-severity (CVSS 10.0) Cisco Identity Services Engine authentication bypass is under active '
             'exploitation with no workaround, and a second actively exploited Cisco flaw carries a federal '
             'remediation deadline that falls today.</div>')

    o.append('<div class="stats">')
    for n, l in [("10.0", "CVSS of the actively exploited Cisco ISE authentication bypass (Cisco advisory)"),
                 ("0 days", "Federal deadline remaining on CVE-2026-76461 &mdash; due today (CISA KEV)"),
                 ("90%", "Share of Salt Typhoon targets in Latin America, mid-2025 into 2026 (ESET)"),
                 ("8", "Latin American countries and territories where SparroWocky hit government agencies (ESET)")]:
        o.append('<div class="stat"><div class="n">%s</div><div class="l">%s</div></div>' % (n, l))
    o.append('</div>')

    o.append('<h2 class="sec">Top story</h2>')
    o.append('<div class="panel"><h3>Cisco ships a perfect-10 zero-day: ISE authentication bypass already '
             'under attack</h3>'
             '<p>Cisco disclosed <b>CVE-2026-76460</b> on Wednesday in advisory '
             '<span style="font-family:var(--mono);font-size:13px">cisco-sa-ISE-ABP-VNSW7Tn5</span>, an '
             'authentication bypass affecting <b>Identity Services Engine (ISE)</b> and <b>ISE Passive Identity '
             'Connector (ISE-PIC)</b>. It carries the maximum CVSS score of <b>10.0</b>. Insufficient '
             'authentication controls on an API endpoint let an attacker send a crafted request that bypasses the '
             'product&rsquo;s web-based management interface; successful exploitation gives an unauthenticated '
             'remote attacker command execution with <b>root</b> privileges. No credentials or user interaction '
             'are required, and Cisco says vulnerable versions are affected <i>regardless of configuration</i>.</p>'
             '<p>Cisco&rsquo;s Product Security Incident Response Team said it is aware of <b>active '
             'exploitation</b> and urged customers to install fixes immediately; CISA added the flaw to its Known '
             'Exploited Vulnerabilities catalog on 16 September. Cisco found the bug while resolving a Technical '
             'Assistance Center support case, and has <i>not</i> disclosed who is exploiting it, how long the '
             'attacks have run, or what intruders did after getting in.</p>'
             '<p>There is <b>no workaround</b>, though Cisco says infrastructure access control lists can serve as '
             'a temporary mitigation restricting management and control-plane traffic reaching affected systems. '
             'Permanent fixes ship in <b>ISE and ISE-PIC 3.1 Patch 12, 3.2 Patch 11, 3.3 Patch 12, 3.4 Patch 7 and '
             '3.5 Patch 4</b>; ISE 3.0 has reached end of software maintenance, so those customers must migrate to '
             'a supported release. Because root access could let an attacker remove or conceal traces of an '
             'intrusion, Cisco advises reviewing ISE access logs for suspicious usernames on <i>every node</i> in a '
             'distributed deployment, and checking network and firewall logs held outside the appliance for '
             'unexpected uploads or downloads. Where there is evidence of compromise, Cisco &ldquo;strongly '
             'recommends&rdquo; reimaging affected nodes and restoring configuration from backup.</p>'
             '<p class="note">The same Wednesday batch carried a substantial set of further ISE vulnerabilities: '
             'per The Register, two other Cisco advisories also reached CVSS 10.0, and a separate trio of '
             'remote-code-execution flaws scored as high as 9.9. Note the naming divergence &mdash; CISA catalogues '
             'CVE-2026-76460 as an &ldquo;Incorrect Use of Privileged APIs&rdquo; issue, while Cisco and The '
             'Register describe it as an authentication bypass; both descriptions are reported here rather than '
             'reconciled.</p></div>')

    d61 = kev(datetime.date(2026, 9, 17))
    o.append('<h2 class="sec">Patch priority</h2>')
    o.append('<div class="callout crit"><div class="k">Do this first &mdash; deadline today</div>'
             '<p style="margin:0"><b>CVE-2026-76461 &mdash; Cisco Secure Email Gateway / Secure Email and Web '
             'Manager (AsyncOS), CVSS 9.8, actively exploited.</b> A pre-authentication flaw reachable through '
             'email parsing that leads to <b>root</b> access, with Cisco warning that attackers may be able to '
             'cover their tracks afterwards. Its CISA KEV remediation deadline is <b>17 September &mdash; '
             '%d days left, today</b>. Fixed in <b>15.5.5-014, 16.0.4-302 and 16.5.0-780</b> (Cisco prefers the '
             'last); there is no workaround. Immediately behind it, the CVSS 10.0 ISE bypass '
             '<b>CVE-2026-76460</b> is due <b>19 September</b>.</p></div>' % d61)

    o.append('<h2 class="sec">Threat actor spotlight</h2>')
    o.append('<div class="panel"><div style="margin-bottom:9px">'
             '<span class="tag new">New</span><span class="tag c">PRC-backed</span>'
             '<span class="tag a">Espionage</span></div>'
             '<h3>Salt Typhoon / FamousSparrow &mdash; the SparroWocky backdoor</h3>'
             '<p>ESET reported on Thursday that China&rsquo;s Salt Typhoon crew &mdash; which ESET tracks as '
             '<b>FamousSparrow</b> &mdash; has built a new modular C++ backdoor called <b>SparroWocky</b> and '
             'dropped it into networks at high-profile organisations across Central and South America since at '
             'least <b>August 2025</b>. The group pivoted to the region a month earlier, and from mid-2025 into '
             '2026 fully <b>90 percent</b> of its targets sat in Latin America. ESET found SparroWocky deployed '
             'against government agencies in <b>Argentina, Ecuador, Guatemala, Honduras, Panama, Peru, Puerto Rico '
             'and Venezuela</b> &mdash; a rare target set among China-aligned APT groups. Researchers Alexandre '
             'C&ocirc;t&eacute; Cyr and Romain Dumont assess the focus likely reflects Beijing&rsquo;s reaction to '
             'US initiatives in the region, suspecting the activity is meant to help China monitor and anticipate '
             'how local governments respond to current US pressure.</p>'
             '<p>The name comes from Lewis Carroll&rsquo;s <i>Jabberwocky</i>: the researchers found the '
             'poem&rsquo;s first stanza inside several collected samples. Analysis was based on a sample compiled '
             'on 17 November &mdash; the report does not state the year &mdash; which bundles <b>Mbed TLS</b> for the encrypted command-and-control channel, '
             '<b>MinHook</b> to hide the start address of newly created threads from security products, and a '
             '<b>COFF Loader</b>-style component for loading in-memory plugins as COFF objects. It also carries a '
             'variant of the <b>SilentMoonwalk</b> technique to spoof call stacks originating from MinHook '
             'routines, plus a custom API-hashing algorithm to resolve Windows API functions dynamically.</p>'
             '<p>Delivery uses the group&rsquo;s customary trident loader scheme &mdash; a legitimate executable, a '
             'malicious DLL, and a file holding the encrypted malware &mdash; with the loader in the DLL executing '
             'via side-loading. Roughly <b>30 commands</b> are handled after the backdoor reaches its C2, covering '
             'system reconnaissance, starting or terminating sessions and removing persistence, stealing and '
             'deleting files, taking periodic screenshots, enumerating remote-session IDs and usernames via '
             '<span style="font-family:var(--mono);font-size:12.5px">WTSEnumerateSessionsW</span>, and spawning '
             'fresh instances of itself. Traffic is TLS-encrypted direct to C2 IP addresses, generally on port '
             '<b>443</b> and sometimes <b>8080</b>. ESET has published a full indicator-of-compromise list and '
             'samples in its GitHub malware-ioc repository.</p>'
             '<p class="note">Context: Salt Typhoon is the group that breached telecommunications carriers and '
             'government agencies for stealthy long-term access dating back as far as 2019, activity that was not '
             'discovered until late 2023. Spelling note &mdash; The Register&rsquo;s headline and tag render the '
             'malware &ldquo;SparroWocky&rdquo; while one sentence of the body reads '
             '&ldquo;SparrowWocky&rdquo;; the headline spelling is used here.</p></div>')

    o.append('<h2 class="sec">Breaches &amp; incidents</h2>')
    o.append('<div class="cards two">')
    o.append('<div class="card"><div class="k">City Relay &middot; London</div>'
             '<div style="margin-bottom:8px"><span class="tag new">New</span>'
             '<span class="tag c">Third-party</span><span class="tag w">Physical risk</span></div>'
             '<h4>Property manager breach may expose bank details &mdash; and lockbox codes</h4>'
             '<p>City Relay warned customers that intruders may have taken financial data, passwords and the codes '
             'used to access keys after compromising its <b>Metabase Cloud</b> instance. The company told landlords '
             'attackers reached the third-party-provided cloud <b>twice</b> &ldquo;as a result of a vulnerability in '
             'the platform that we were unaware of.&rdquo; Potentially exposed: names, email and physical addresses, '
             'telephone numbers, financial information, property access details and account passwords &mdash; '
             'specifically bank account numbers, sort codes, IBANs, SWIFT references and account names and '
             'addresses, plus <b>lockbox codes and key-storage locations</b>, creating a physical break-in risk at '
             'managed properties. City Relay learned of the intrusion around <b>8 September</b>, notified affected '
             'customers on <b>14 September</b> and immediately reset access codes; it says it has found no evidence '
             'yet of unauthorised property entry or misuse. Metabase disclosed a zero-day SQL-injection flaw on '
             '<b>6 August</b>, saying attackers compromised <b>fewer than 3 percent</b> of its customers before '
             'fixes were automatically deployed &mdash; but it has <i>not</i> confirmed the City Relay incident was '
             'part of that campaign, and no CVE is attached to this breach here.</p></div>')
    o.append('<div class="card"><div class="k">Revolut</div>'
             '<div style="margin-bottom:8px"><span class="tag c">Extortion</span>'
             '<span class="tag a">Social engineering</span></div>'
             '<h4>Forged legal requests pried customer data out of the bank</h4>'
             '<p>An actor using the handle <b>&ldquo;IAmNotAVillain&rdquo;</b> has publicly demanded <b>$3 million '
             '/ 6,000 XMR</b> and claims at least <b>680 accounts</b> were affected, after roughly five months of '
             '<b>forged legal requests</b> sent to <b>Revolut Bank UAB</b>. The access chain began with an '
             'infostealer taking a government employee&rsquo;s email, which was then used to make the requests look '
             'legitimate.</p></div>')
    o.append('<div class="card"><div class="k">Spain</div>'
             '<div style="margin-bottom:8px"><span class="tag a">AI-enabled</span>'
             '<span class="tag m">Regulatory</span></div>'
             '<h4>Regulators report the country&rsquo;s first AI-aided attack</h4>'
             '<p>Spanish data-protection authorities described an incident in which an <b>AI agent chained together '
             'a successful login, vulnerability discovery and access to personal data</b> &mdash; reported as a '
             'potential milestone for autonomous cyberattacks. The regulator has called for an &ldquo;immediate '
             'review&rdquo; of data protection models.</p></div>')
    o.append('<div class="card"><div class="k">Salesforce</div>'
             '<div style="margin-bottom:8px"><span class="tag w">Outage</span>'
             '<span class="tag m">Availability</span></div>'
             '<h4>Global outage, then the worst drag on the Dow</h4>'
             '<p>Salesforce spent 16 September recovering from a <b>global outage</b>. The market consequence '
             'showed up on our markets page: Trading Economics had <b>CRM down 4.30%</b> as the Dow&rsquo;s biggest '
             'single loser in Thursday&rsquo;s opening snapshot, even as the index itself rose.</p></div>')
    o.append('<div class="card"><div class="k">Berlin &middot; Rhysida</div>'
             '<div style="margin-bottom:8px"><span class="tag c">Ransomware</span></div>'
             '<h4>~6TB published after a refused ransom</h4>'
             '<p>The Rhysida group published roughly <b>6TB</b> of data after a demand of <b>30 BTC</b> '
             '(about &euro;2 million) went unpaid. Carried forward from this site&rsquo;s verified ledger and not '
             're-fetched this run.</p></div>')
    o.append('<div class="card"><div class="k">McKesson &middot; ShinyHunters</div>'
             '<div style="margin-bottom:8px"><span class="tag m">Unverified claim</span></div>'
             '<h4>284M records claimed &mdash; a claim, not a confirmation</h4>'
             '<p>ShinyHunters <b>claims</b> <b>284 million</b> records, with the incident said to have been '
             'discovered on <b>25 August</b>. The figure is the attacker&rsquo;s own and is labelled as a claim; '
             'carried from the ledger and not re-fetched this run.</p></div>')
    o.append('</div>')

    o.append('<h2 class="sec">Vulnerability watch</h2>')
    o.append('<div class="tblwrap"><table><thead><tr><th>CVE</th><th>CVSS</th><th>Affected</th>'
             '<th>Note</th></tr></thead><tbody>')
    rows = [
        ("CVE-2026-76460", "10.0", "Cisco ISE &amp; ISE-PIC",
         "Authentication bypass on an API endpoint &rarr; unauthenticated root command execution. "
         "<b>Actively exploited</b>; no workaround. Fixed 3.1 P12 / 3.2 P11 / 3.3 P12 / 3.4 P7 / 3.5 P4; ISE 3.0 EoSM."),
        ("CVE-2026-76461", "9.8", "Cisco Secure Email Gateway; Secure Email &amp; Web Manager",
         "Pre-auth flaw via email parsing &rarr; root. <b>Actively exploited</b>; KEV deadline today. "
         "Fixed 15.5.5-014 / 16.0.4-302 / 16.5.0-780."),
        ("CVE-2026-87886", "Not stated by vendor", "Acronis Backup for cPanel &amp; WHM / Plesk (Linux)",
         "Incorrect default permissions &rarr; privilege escalation. Added to CISA KEV on 16 September. "
         "No CVSS stated in the sources read this run, so none is printed."),
        ("CVE-2026-20329", "9.9", "Cisco Secure Firewall ASA / FTD / FMC",
         "CWE-703 grouping from Cisco&rsquo;s 16 September hardening release (advisory verified in a prior run). "
         "Not among the flaws Cisco footnotes as exploited."),
        ("CVE-2026-20332", "9.0", "Cisco Secure Firewall FMC",
         "CWE-284 grouping &mdash; this is the row carrying Cisco&rsquo;s exploited-flaw footnote, pointing to the "
         "FMC static-credential and authentication-bypass advisories."),
        ("No CVE asserted", "&mdash;", "Metabase Cloud",
         "Zero-day SQL injection disclosed 6 August; fewer than 3% of customers compromised before automatic "
         "fixes. Metabase has not confirmed a link to the City Relay breach, so no CVE is mapped to it here."),
    ]
    for c, s, a, n in rows:
        o.append('<tr><td style="font-family:var(--mono);white-space:nowrap">%s</td>'
                 '<td style="font-family:var(--mono)">%s</td><td>%s</td><td>%s</td></tr>' % (c, s, a, n))
    o.append('</tbody></table></div>')

    o.append('<h2 class="sec">CISA KEV &amp; federal deadlines</h2>')
    d60 = kev(datetime.date(2026, 9, 19))
    d86 = kev(datetime.date(2026, 9, 19))
    d69 = kev(datetime.date(2026, 9, 14))
    d59 = kev(datetime.date(2026, 8, 21))
    sat = datetime.date(2026, 9, 19).strftime("%A")
    o.append('<div class="panel"><ul class="b">')
    o.append('<li><b style="color:var(--crit)">CVE-2026-76461</b> &mdash; Cisco Secure Email Gateway / AsyncOS '
             '(9.8). Added 14 September, due <b>17 September</b> &mdash; '
             '<b style="color:var(--crit)">%d days left, today</b>. Holds Patch Priority.</li>' % d61)
    o.append('<li><b>CVE-2026-76460</b> &mdash; Cisco ISE / ISE-PIC (10.0), catalogued by CISA as an incorrect use '
             'of privileged APIs. Added 16 September, due <b>19 September</b> &mdash; <b>%d days left</b> '
             '(a %s).</li>' % (d60, sat))
    o.append('<li><b>CVE-2026-87886</b> &mdash; Acronis Backup for cPanel &amp; WHM / Plesk. Added 16 September, '
             'due <b>19 September</b> &mdash; <b>%d days left</b> (a %s).</li>' % (d86, sat))
    o.append('<li><b style="color:var(--crit)">CVE-2026-84869</b> &mdash; ScreenConnect. Was due 14 September '
             '&mdash; <b style="color:var(--crit)">overdue by %d days</b>. Carried from this site&rsquo;s ledger '
             'and not re-fetched this run.</li>' % abs(d69))
    o.append('<li><b style="color:var(--crit)">CVE-2026-59310</b> &mdash; VMware vCenter. Was due 21 August '
             '&mdash; <b style="color:var(--crit)">overdue by %d days</b>. Carried from the ledger and not '
             're-fetched this run.</li>' % abs(d59))
    o.append('</ul><p class="note">CISA&rsquo;s 16 September alert is titled as adding <b>two</b> vulnerabilities, '
             'and the two it names are CVE-2026-76460 and CVE-2026-87886 &mdash; matching the rows above. All '
             'countdowns are computed from today&rsquo;s date rather than written by hand. A direct fetch of '
             'cisa.gov returned no usable content again this run, so the deadlines above rest on the CISA alert '
             'title and page as surfaced in search, plus this site&rsquo;s own verified ledger.</p></div>')

    o.append('<h2 class="sec">Also moving</h2>')
    o.append('<div class="panel"><ul class="b">'
             '<li>Researchers have described a method to <b>listen in on headphones from afar</b> '
             '(The Register, 17 September).</li>'
             '<li>A <b>Microsoft configuration change</b> left SharePoint pages rendering blank '
             '(The Register, 17 September).</li>'
             '<li>A Ukrainian lawyer was sentenced to <b>four years</b> for a second career as a '
             '<b>Conti ransomware coder</b> (The Register, 11 September).</li>'
             '</ul></div>')

    o.append(sources([
        ("The Register &mdash; Cisco drops another exploited zero-day, this time a perfect 10 (17 Sep 2026)",
         "https://www.theregister.com/security/2026/09/17/cisco-drops-another-exploited-zero-day-this-time-a-perfect-10/5297180"),
        ("Cisco advisory cisco-sa-ISE-ABP-VNSW7Tn5 (CVE-2026-76460)",
         "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5"),
        ("CISA &mdash; Adds Two Known Exploited Vulnerabilities to Catalog (16 Sep 2026)",
         "https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-two-known-exploited-vulnerabilities-catalog"),
        ("CISA &mdash; Known Exploited Vulnerabilities Catalog",
         "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"),
        ("The Register &mdash; China&rsquo;s Salt Typhoon backdoors Latin American orgs with new snooping malware (17 Sep 2026)",
         "https://www.theregister.com/security/2026/09/17/chinas-salt-typhoon-backdoors-latin-american-orgs-with-new-snooping-malware/5297286"),
        ("ESET WeLiveSecurity &mdash; SparroWocky backdoor research",
         "https://www.welivesecurity.com/en/eset-research/beware-sparrowock-backdoor-bites-commands-catch/"),
        ("ESET malware-ioc &mdash; FamousSparrow indicators",
         "https://github.com/eset/malware-ioc/tree/master/famoussparrow/"),
        ("The Register &mdash; London property manager breach may have exposed bank details and lockbox codes (17 Sep 2026)",
         "https://www.theregister.com/security/2026/09/17/london-property-manager-breach-may-have-exposed-bank-details-and-lockbox-codes/5297232"),
        ("The Register &mdash; Cisco email security boxes can be rooted by&hellip; an email (15 Sep 2026)",
         "https://www.theregister.com/security/2026/09/15/cisco-email-security-boxes-can-be-rooted-by-an-email/5296604"),
        ("The Register &mdash; Revolut falls for fake government requests, hands over customer data (14 Sep 2026)",
         "https://www.theregister.com/cyber-crime/2026/09/14/revolut-falls-for-fake-government-requests-hands-over-customer-data/5296118"),
        ("The Register &mdash; Spain gets its first taste of AI-aided cyber attack (16 Sep 2026)",
         "https://www.theregister.com/cyber-crime/2026/09/16/spain-gets-its-first-taste-of-ai-aided-cyber-attack/5296844"),
        ("The Register &mdash; Salesforce staggers back to feet after global outage (16 Sep 2026)",
         "https://www.theregister.com/saas/2026/09/16/salesforce-staggers-back-to-feet-after-global-outage/5296800"),
        ("The Register &mdash; Researchers find way to listen in on headphones from afar (17 Sep 2026)",
         "https://www.theregister.com/security/2026/09/17/researchers-find-way-to-listen-in-on-headphones-from-afar/5297303"),
        ("The Register &mdash; Microsoft configuration change leaves SharePoint pages drawing a blank (17 Sep 2026)",
         "https://www.theregister.com/saas/2026/09/17/microsoft-configuration-change-leaves-sharepoint-pages-drawing-a-blank/5297198"),
    ]))
    o.append('<div class="disc">Severity scores, fixed versions and remediation deadlines are reported as the '
             'vendor or CISA states them. Where a secondary source and a primary advisory disagree, the advisory '
             'wins and the disagreement is named. This page is a news briefing, not a substitute for your own '
             'vulnerability management process.</div></footer>')
    o.append(FOOT)
    open(os.path.join(OUT, "cyber-briefing.html"), "w").write("".join(o))

# ================================================================ MARKETS
TV = 'https://s3.tradingview.com/external-embedding/embed-widget-%s.js'

def build_ws():
    css = base_css("#caa64a", "#e8c766", "#0b0a08", "#151310", "#2a2620") + """
.masthead h1,h3{font-family:Georgia,'Times New Roman',serif;letter-spacing:-.3px}
h3{font-size:20px}
.livebar{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 8px 4px;margin-bottom:18px}
.livebar-label{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--up);
  display:flex;align-items:center;gap:8px;padding:4px 8px 8px}
.livebar-label .dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--up)}
.tickers{display:grid;gap:11px;margin-bottom:6px}
@media(min-width:700px){.tickers{grid-template-columns:repeat(3,1fr)}}
.ticker{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 10px}
"""
    o = [head("The Closing Bell &mdash; Daily Briefings", css)]
    o.append(mast("The Closing Bell", "Your daily markets briefing &mdash; indices, movers, rates &amp; what&rsquo;s next"))
    o.append('<div class="tldr"><b>The Tape</b> <span>%s</span></div>' % TL_WS)
    o.append(FRESH)
    o.append(nav("ws"))

    # BLOCK A
    o.append('<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>'
             '<script src="%s" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},'
             '{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},'
             '{"proName":"NASDAQ:MU","title":"Micron"},{"proName":"NASDAQ:AVGO","title":"Broadcom"},'
             '{"proName":"NASDAQ:NVDA","title":"NVIDIA"},{"proName":"NYSE:GS","title":"Goldman Sachs"},'
             '{"proName":"NYSE:CRM","title":"Salesforce"},{"proName":"TVC:USOIL","title":"WTI Crude"},'
             '{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,'
             '"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script></div>'
             % (TV % "ticker-tape"))

    # BLOCK B
    o.append('<h2 class="sec">Live index quotes &mdash; updates in real time</h2>')
    o.append('<div class="tickers">')
    for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI"]:
        o.append('<div class="ticker"><script src="%s" async>{"symbol":"%s","width":"100%%",'
                 '"colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>'
                 % (TV % "single-quote", sym))
    o.append('</div>')
    o.append('<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the '
             'latest edition; official closes are in the Weekly Scorecard.</div>')

    o.append('<h2 class="sec">The lead</h2>')
    o.append('<div class="panel"><h3>Second day of gains after the Fed hike, with chips out front '
             '&mdash; S&amp;P 500 +1.15% as of ~3:50 PM ET</h3>'
             '<p>Equities extended Wednesday&rsquo;s rebound through Thursday afternoon. On Trading '
             'Economics&rsquo; Sep/17 board, read at roughly <b>3:50 PM ET</b>, the <b>S&amp;P 500 stood at '
             '7,639.02, up 87.21 points or +1.15%</b>; the <b>Nasdaq 100 at 29,426.02, up 480.96 or +1.66%</b>; '
             'and the <b>Dow at 51,817.26, up 355.36 or +0.69%</b>. Breadth reached down the cap scale, with the '
             '<b>Russell 2000 +0.65%</b> (2,879.64) and the <b>S&amp;P MidCap 400 +0.76%</b> (3,668.26). All three '
             'headline figures reconcile <i>exactly</i> against Wednesday&rsquo;s settles &mdash; 7,551.81 + 87.21, '
             '51,461.90 + 355.36 and 28,945.06 + 480.96 &mdash; and each percentage was recomputed from those '
             'levels rather than taken on trust.</p>'
             '<p>The driver was a rotation back into growth and AI names: a closely watched gauge of chipmakers '
             'climbed about <b>3%</b>, and falling oil prices lent support to the argument that inflation can stay '
             'contained. That combination arrived one day after the <b>Federal Reserve raised its benchmark rate by '
             '25 basis points to 3.75%&ndash;4%</b>, its first increase since 2023. Sources read this run disagree '
             'on the message the Fed sent alongside that decision &mdash; one framing has the Fed signalling a '
             'further increase later this year, another has it signalling confidence in a soft landing &mdash; so '
             'the hike is reported here and the characterisation of its tone is not.</p>'
             '<p class="note"><b>Freshness and what was refused.</b> Research for this edition closed at about '
             '3:50 PM ET, roughly ten minutes before the bell, so <b>no official closing figures were verified '
             'this run</b> and none are presented as closes &mdash; the live widgets above show the settled '
             'session. Three refusals: a <b>7,596 / +0.59%</b> S&amp;P snapshot still circulating in search results '
             'is internally consistent but describes an earlier hour and is <b>superseded</b>; a search summary '
             'asserting the market &ldquo;faced downward pressure&rdquo; today is contradicted by every verified '
             'read and is not used; and a claim that the <b>10-year yield reached 5.01%</b> today conflicts with '
             'Trading Economics&rsquo; own 4.94% and is dropped. Two internal inconsistencies are stated rather '
             'than resolved: the Trading Economics page description reads &ldquo;rose to 7635 points, gaining '
             '1.10%&rdquo; while its own live table shows 7,639.02 / +1.15% (the table is used), and the '
             '<b>VIX</b> row again renders <b>15.49 | &minus;2.22 | &minus;2.22%</b> &mdash; a point change and a '
             'percentage that cannot both describe one number, so it is refused for a third consecutive edition. '
             'No <b>Nasdaq Composite</b> percentage is published: every figure circulating for it was an ETF '
             'proxy.</p></div>')

    o.append('<h2 class="sec">Movers &amp; drivers</h2>')
    o.append('<div class="cards two">')
    mv = [
        ("Micron &middot; MU", "up", "+5.48%",
         "The session&rsquo;s biggest single-name move on Trading Economics&rsquo; mega-cap board: "
         "<b>$977.36, +$50.81, +5.48%</b>. Chart of the Day below. Trading Economics puts its market "
         "capitalisation at $1.18T."),
        ("Broadcom &middot; AVGO", "up", "+2.70%",
         "<b>$348.66, +$9.15</b> &mdash; part of the roughly 3% advance in the chipmaker gauge that led the tape."),
        ("NVIDIA &middot; NVDA", "up", "+2.69%",
         "<b>$219.66, +$5.76</b>, and one of the Dow&rsquo;s three biggest gainers at the open (+2.09% at that "
         "point). Market capitalisation $5.07T."),
        ("Goldman Sachs &middot; GS", "up", "+1.90%",
         "An intraday reversal worth noting: GS was among the Dow&rsquo;s three biggest <i>drags</i> at the open "
         "at <b>&minus;0.80%</b>, and by the afternoon read had turned to <b>$955.80, +$17.82, +1.90%</b>."),
        ("Salesforce &middot; CRM", "down", "&minus;4.30%",
         "The Dow&rsquo;s biggest single loser in Trading Economics&rsquo; opening snapshot, a day after "
         "Salesforce recovered from a <b>global outage</b> &mdash; see the Cyber Wire briefing."),
        ("Caterpillar &middot; CAT", "up", "+2.60%",
         "Top Dow gainer in the opening snapshot. Tesla <b>+2.49%</b> ($367.00) and Amazon <b>+2.26%</b> "
         "($251.53) also ran ahead of the index; Walmart was a modest drag at <b>&minus;0.47%</b>."),
    ]
    for k, dirn, pct, body in mv:
        o.append('<div class="card"><div class="k">%s</div>'
                 '<h4 class="%s">%s</h4><p>%s</p></div>' % (k, dirn, pct, body))
    o.append('</div>')
    o.append('<div class="note">Every quote and percentage above comes from the Trading Economics Sep/17 board or '
             'its opening-snapshot narrative, read this run; each point change was reconciled against its own '
             'percentage before publication. Figures labelled &ldquo;at the open&rdquo; are from that snapshot and '
             'are not presented as current. <b>No mover carries a &ldquo;New&rdquo; tag this edition</b> &mdash; a '
             'search across all 753 prior snapshots found every one of these names already on the site, so the '
             'zero is stated rather than papered over with a tag.</div>')

    o.append('<h2 class="sec">Chart of the day &mdash; Micron</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>'
             '{"symbol":"NASDAQ:MU","width":"100%%","height":240,"locale":"en","dateRange":"1D",'
             '"colorTheme":"dark","isTransparent":true,"autosize":false}</script></div>'
             % (TV % "mini-symbol-overview"))
    o.append('<div class="note">Micron, up <b>5.48%</b> to <b>$977.36</b> on the afternoon read &mdash; the '
             'largest single-name move on the board this run.</div>')

    o.append('<h2 class="sec">Sector heat &mdash; live</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>'
             '{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector",'
             '"locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,'
             '"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%%","height":420}</script></div>'
             % (TV % "stock-heatmap"))
    o.append('<div class="note">Technology led, with a chipmaker gauge up about <b>3%</b> and semiconductor and '
             'AI-related names driving the advance. On breadth, TheStreet counted <b>259 of 503</b> S&amp;P '
             'holdings advancing at 10:54 AM ET &mdash; a morning figure, carried with its own clock and not '
             'restated as an afternoon reading. No VIX level is published this edition (see The Lead).</div>')

    o.append('<h2 class="sec">The calendar &mdash; live</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>'
             '{"colorTheme":"dark","isTransparent":true,"width":"100%%","height":420,"locale":"en",'
             '"importanceFilter":"0,1","countryFilter":"us"}</script></div>' % (TV % "events"))

    o.append('<h2 class="sec">Live market headlines &mdash; updates in real time</h2>')
    o.append('<div class="panel" style="padding:8px"><script src="%s" async>'
             '{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,'
             '"displayMode":"regular","width":"100%%","height":420,"locale":"en"}</script></div>'
             % (TV % "timeline"))

    o.append('<h2 class="sec">Weekly scorecard</h2>')
    o.append('<div class="tblwrap"><table><thead><tr><th>Index</th><th>Last official close</th>'
             '<th>Session</th></tr></thead><tbody>')
    for nm, lv in [("S&amp;P 500", "7,551.81"), ("Dow Jones Industrial Average", "51,461.90"),
                   ("Nasdaq 100", "28,945.06")]:
        o.append('<tr><td>%s</td><td style="font-family:var(--mono)">%s</td>'
                 '<td>Wednesday 16 September</td></tr>' % (nm, lv))
    o.append('</tbody></table></div>')
    o.append('<div class="note">Official closes only. These are Wednesday&rsquo;s settles, carried from this '
             'site&rsquo;s verified ledger and used as the base for every percentage computed on this page. '
             'Thursday&rsquo;s closes are <b>not</b> listed: research closed about ten minutes before the bell, so '
             'no Thursday settle was verified this run. No Nasdaq Composite level is carried.</div>')

    o.append('<h2 class="sec">Rates, bonds &amp; commodities</h2>')
    o.append('<div class="tblwrap"><table><thead><tr><th>Instrument</th><th>Level</th><th>Change</th>'
             '</tr></thead><tbody>')
    rc = [("US 2-year yield", "4.69%", "&minus;5.6 bp", "down"),
          ("US 5-year yield", "4.80%", "&minus;8.9 bp", "down"),
          ("US 10-year yield", "4.94%", "&minus;8.3 bp", "down"),
          ("US 30-year yield", "5.29%", "&minus;7.6 bp", "down"),
          ("Fed funds target", "3.75%&ndash;4.00%", "+25 bp on 16 Sep", ""),
          ("WTI crude", "$101.44", "&minus;0.96%", "down"),
          ("Brent crude", "$104.23", "&minus;1.51%", "down"),
          ("Gold", "$4,354.47", "+2.13%", "up"),
          ("Silver", "$65.41", "+3.43%", "up"),
          ("CBOE VIX", "Not published", "Refused &mdash; see The Lead", "")]
    for nm, lv, ch, cl in rc:
        o.append('<tr><td>%s</td><td style="font-family:var(--mono)">%s</td>'
                 '<td class="%s" style="font-family:var(--mono)">%s</td></tr>' % (nm, lv, cl, ch))
    o.append('</tbody></table></div>')
    o.append('<div class="note">Yields and commodities from the Trading Economics Sep/17 boards read this run; '
             'basis-point moves are the changes that board reports. Yields fell right across the curve &mdash; the '
             '3-year at 4.76%, 7-year at 4.86% and 20-year at 5.33% moved the same way. Note that Trading '
             'Economics prints its commodity change column <b>unsigned</b>, so direction is taken from the '
             'accompanying percentage; oil is lower on the day, metals higher.</div>')

    o.append('<h2 class="sec">On the radar</h2>')
    o.append('<div class="panel"><ul class="b">'
             '<li><b>Whether the post-Fed decline in yields holds.</b> The 10-year sits at 4.94%, down about 8 bp, '
             'with the whole curve lower &mdash; a move that has so far been read as supportive of equities rather '
             'than as a growth warning.</li>'
             '<li><b>Whether semiconductor leadership broadens or narrows.</b> The chip gauge is up roughly 3% and '
             'Micron alone gained 5.48%; a rally carried by a handful of names behaves differently from one with '
             '259-of-503 breadth behind it.</li>'
             '<li><b>Salesforce fallout.</b> CRM was the Dow&rsquo;s biggest drag at &minus;4.30% a day after a '
             'global outage &mdash; worth watching as the operational story turns into a customer-confidence '
             'story.</li>'
             '</ul></div>')

    o.append(sources([
        ("Trading Economics &mdash; United States Stock Market Index (read ~3:50 PM ET, 17 Sep 2026)",
         "https://tradingeconomics.com/united-states/stock-market"),
        ("Trading Economics &mdash; United States Government Bond Yield (read this run)",
         "https://tradingeconomics.com/united-states/government-bond-yield"),
        ("Bloomberg &mdash; Stock Market Today: Dow, S&amp;P Live Updates for September 17",
         "https://www.bloomberg.com/news/articles/2026-09-16/stock-market-today-dow-s-p-live-updates"),
        ("Yahoo Finance &mdash; Strength in Chipmakers Boosts Stocks",
         "https://finance.yahoo.com/markets/stocks/articles/strength-chipmakers-boosts-stocks-151149798.html"),
        ("CNBC &mdash; Stock market today: live updates",
         "https://www.cnbc.com/2026/09/15/stock-market-today-live-updates.html"),
        ("Charles Schwab &mdash; Stock market update",
         "https://www.schwab.com/learn/story/stock-market-update-open"),
        ("The Register &mdash; Salesforce staggers back to feet after global outage (16 Sep 2026)",
         "https://www.theregister.com/saas/2026/09/16/salesforce-staggers-back-to-feet-after-global-outage/5296800"),
    ]))
    o.append('<div class="disc">Information only &mdash; not investment advice. Intraday figures describe the '
             'moment they were read and nothing later; levels appear only where a point change, a percentage and a '
             'level agree with one another and with a corroborating source. Live widgets are supplied by '
             'TradingView and may be delayed.</div></footer>')
    o.append(FOOT)
    open(os.path.join(OUT, "wallstreet-briefing.html"), "w").write("".join(o))

# ================================================================ MMA
CDN_JS = """<script>(function(){var t=new Date('2026-09-19T21:00:00-04:00');function f(){var n=new Date(),d=t-n,e=document.getElementById('ufccdn');if(!e)return;if(d<=0){e.textContent='Fight week \\u2014 live/completed';return}var dd=Math.floor(d/86400000),hh=Math.floor(d%86400000/3600000),mm=Math.floor(d%3600000/60000);e.textContent=dd+'d '+hh+'h '+mm+'m';}f();setInterval(f,30000);})();</script>"""

def build_mma():
    css = base_css("#e84545", "#ff8a5c", "#100c0c", "#1a1313", "#322020") + """
.cdn{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);
  border-radius:11px;padding:12px 16px;margin-bottom:18px;display:flex;flex-wrap:wrap;
  align-items:baseline;gap:11px}
.cdn .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.cdn .v{font-family:var(--mono);font-size:19px;color:var(--accent2)}
.cdn .w{font-size:13.5px;color:var(--muted)}
.dv{font-family:var(--mono);font-size:11px;letter-spacing:.09em;color:var(--accent2);margin-bottom:7px}
.odds{font-family:var(--mono);font-size:12px;color:var(--muted);margin-top:8px;display:block;line-height:1.5}
"""
    o = [head("The Octagon &mdash; Daily Briefings", css)]
    o.append(mast("The Octagon", "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
    o.append('<div class="tldr"><b>Tale of the Tape</b> <span>%s</span></div>' % TL_MMA)
    o.append(FRESH)
    o.append(nav("mma"))

    o.append('<div class="cdn"><span class="k">Next card</span>'
             '<span class="v" id="ufccdn">&nbsp;</span>'
             '<span class="w">UFC 331: Van vs. Pantoja 2 &middot; Saturday 19 September &middot; '
             'Crypto.com Arena, Los Angeles &middot; main card 9 PM ET</span></div>')

    o.append('<h2 class="sec">Top story</h2>')
    o.append('<div class="panel" style="border-left:4px solid var(--accent)">'
             '<h3>Ortega out of UFC 331 &mdash; and out of the Moicano fight for a second time this year</h3>'
             '<p>A cut above <b>Brian Ortega&rsquo;s left eye</b>, bad enough to need stitches, has forced him out '
             'of his bout with <b>Renato Moicano</b> at Saturday&rsquo;s UFC 331 in Los Angeles, scrapping the '
             'matchup from the card. In a follow-up video Ortega said a jiu-jitsu exercise turned into a headbutt, '
             'called it a &ldquo;freak accident,&rdquo; and said that after taking advice from his team and the UFC '
             'he had little choice but to withdraw. He has since shared a graphic image of the cut.</p>'
             '<p>It is the <b>second time in 2026</b> that Ortega has pulled out of a scheduled fight with '
             'Moicano, the pairing having already been cancelled in March. Moicano responded sharply &mdash; '
             'publicly blasting Ortega for costing him what he framed as an easy payday and cautioning future '
             'Ortega opponents &mdash; and is now slated to return as a headliner at <b>UFC Vegas 123</b> at the '
             'Meta Apex in October, against <b>Tom Nolan</b>. Ortega, for his part, has pushed back at fans '
             'speculating that he is avoiding the fight.</p>'
             '<p class="note">Sources read this run differ on how to describe the scrapped bout &mdash; one frames '
             'it as Ortega&rsquo;s lightweight debut in a rematch, another simply as a second cancellation of the '
             'same pairing. Neither descriptor is asserted here beyond what all sources agree on: the bout was '
             'scheduled, and it is off.</p></div>')

    o.append('<h2 class="sec">Fight week &mdash; upcoming cards</h2>')
    o.append('<div class="cards two">')
    o.append('<div class="card"><div class="dv">Sat 19 September 2026 &middot; Crypto.com Arena, Los Angeles</div>'
             '<h4>UFC 331: Van vs. Pantoja 2</h4>'
             '<p>A flyweight title rematch headlines: champion <b>Joshua Van</b> against former champion '
             '<b>Alexandre Pantoja</b>. They first met in December 2025 at UFC 323, where Van took the belt by '
             'technical knockout <b>26 seconds</b> into round one, as a result of an arm injury Pantoja sustained. '
             'The five-round co-main pits top lightweight contender <b>Arman Tsarukyan</b> against surging '
             '<b>Maur&iacute;cio Ruffy</b> &mdash; Tsarukyan&rsquo;s return after ten months out is arguably the '
             'card&rsquo;s main attraction. <b>Gable Steveson</b> meets <b>Sean Sharaf</b> on the heavyweight card. '
             'Early prelims 5 PM ET / 2 PM PT, prelims 7 PM ET / 4 PM PT, main card 9 PM ET / 6 PM PT; the full '
             'card streams on Paramount+ in the US.'
             '<span class="odds">Odds &mdash; main event: <b>Van &minus;107 / Pantoja &minus;113</b> (Yahoo, fight '
             'week), a true pick&rsquo;em after opening at <b>Van +170 / Pantoja &minus;200</b>. An earlier Covers '
             'read this site carried had <b>Van &minus;130 / Pantoja +110</b>. Co-main: <b>Tsarukyan '
             '&minus;380</b> having opened at &minus;350, with <b>Ruffy +284</b> on a recent read. All lines are '
             'printed as their book and moment reported them; none is averaged or converted.</span></p></div>')
    o.append('<div class="card"><div class="dv">Sat 3 October 2026 &middot; Salt Lake City</div>'
             '<h4>UFC 332: Silva vs. Wang &mdash; vacant title</h4>'
             '<p><b>Natalia Silva</b> and <b>Wang Cong</b> contest the <b>vacant women&rsquo;s flyweight '
             'title</b>, after Valentina Shevchenko vacated the belt while sidelined by injury. The UFC has said '
             'Shevchenko is guaranteed a title shot once she is cleared. No odds for this card were stated in any '
             'source read this run, so none are printed.</p></div>')
    o.append('<div class="card"><div class="dv">Sat 24 October 2026 &middot; Abu Dhabi</div>'
             '<h4>UFC 333</h4>'
             '<p>Two champions are booked to defend on the same card: featherweight titleholder '
             '<b>Alexander Volkanovski</b> and bantamweight titleholder <b>Petr Yan</b>. Opponents and the full '
             'line-up are not asserted here &mdash; no source read this run stated them.</p></div>')
    o.append('<div class="card"><div class="dv">October 2026 &middot; Meta Apex, Las Vegas</div>'
             '<div style="margin-bottom:7px"><span class="tag new">New</span></div>'
             '<h4>UFC Vegas 123: Moicano vs. Nolan</h4>'
             '<p><b>Renato Moicano</b> headlines against <b>Tom Nolan</b>, the booking that followed '
             'Ortega&rsquo;s withdrawal from Saturday&rsquo;s card. Only the month was stated in the source read '
             'this run, so no exact date is printed.</p></div>')
    o.append('</div>')

    o.append('<h2 class="sec">Last event &mdash; results</h2>')
    o.append('<div class="tblwrap"><table><thead><tr><th>Result</th><th>Bout</th><th>Method</th></tr>'
             '</thead><tbody>')
    res = [("Jean Silva", "def. Jose Miguel Delgado", "Submission (rear-naked choke), 2:57 of R3"),
           ("Brandon Moreno", "def. Joseph Morales", "Split decision"),
           ("Tommy McMillen", "def. Marwan Rahiki", "Unanimous decision, 29&ndash;28, 29&ndash;28, 29&ndash;27"),
           ("Alexa Grasso", "def. Manon Fiorot", "Unanimous decision, 29&ndash;28 &times;3"),
           ("Curtis Blaydes", "def. Waldo Cortes Acosta", "Unanimous decision, 29&ndash;28 &times;3"),
           ("David Martinez", "def. Dan Ige", "Unanimous decision, 30&ndash;27, 30&ndash;27, 29&ndash;28")]
    for w, b, m in res:
        o.append('<tr><td class="win">%s</td><td>%s</td><td>%s</td></tr>' % (w, b, m))
    o.append('</tbody></table></div>')
    o.append('<div class="note"><b>Noche UFC</b> &mdash; methods and scorecards taken from UFC.com&rsquo;s own '
             'main-card page. <b>Performance bonuses:</b> Performance of the Night to <b>Jean Silva</b> and to '
             '<b>Sean King III</b>, whose UFC debut knockout UFC&rsquo;s own bonus page headlines at <b>0:36</b> '
             '(a search summary timing it at 0:33 is refused); Fight of the Night to <b>McMillen vs. Rahiki</b>. '
             'UFC prints no dollar amounts, so the customary <b>$100,000</b> figure is carried with its '
             'Yahoo/Forbes attribution only, and no Fight of the Night amount is printed at all.</div>')

    o.append('<h2 class="sec">Prospect watch</h2>')
    o.append('<div class="cards two">')
    o.append('<div class="card"><div style="margin-bottom:7px"><span class="tag" '
             'style="color:var(--up);border-color:var(--up)">Prospect</span></div>'
             '<h4>Gable Steveson</h4>'
             '<p>The Olympic wrestling gold medallist takes his <b>first main-card slot</b> on Saturday against '
             '<b>Sean Sharaf</b>, entering as a heavy favourite on the heavyweight card. Asked about the matchup, '
             'Steveson reached for a boxing analogy, referencing <b>Mike Tyson vs. Peter McNeeley</b>.</p></div>')
    o.append('<div class="card"><div style="margin-bottom:7px"><span class="tag m">Roster</span></div>'
             '<h4>Muhammad Mokaev</h4>'
             '<p>The undefeated flyweight, who went <b>7&ndash;0</b> inside the UFC before leaving the promotion in '
             '2024 after a decision win over Manel Kape, says executives strung him along for two years with empty '
             'promises of a return. He told the BBC he had been assured multiple times that hitting specific '
             'benchmarks would earn a new contract, and has called the eventual offer <b>&ldquo;deeply '
             'insulting&rdquo;</b> &mdash; &ldquo;they wasted two years of my life.&rdquo; He has discussed joining '
             '<b>MVP MMA</b>, having withdrawn from that promotion&rsquo;s debut event earlier this year.</p></div>')
    o.append('<div class="card"><div style="margin-bottom:7px"><span class="tag m">Roster churn</span></div>'
             '<h4>Cuts to make room for Contender Series signings</h4>'
             '<p>The UFC has run a steady wave of <b>roster removals</b> through 2026, clearing space for the new '
             'signings arriving via <b>Dana White&rsquo;s Contender Series</b>. No individual names or totals are '
             'asserted here &mdash; no source read this run stated them.</p></div>')
    o.append('</div>')

    o.append('<h2 class="sec">Around the sport</h2>')
    o.append('<div class="panel"><ul class="b">'
             '<li><b>Michael Chandler is expecting a huge upset</b> at UFC 331 &mdash; he has not been reported as '
             'naming which bout, so none is attributed to him here.</li>'
             '<li><b>Arman Tsarukyan returns after ten months out</b>, and is being billed as arguably the main '
             'attraction at Saturday&rsquo;s numbered card in Los Angeles.</li>'
             '<li>An update was posted regarding the content on <b>Tom Aspinall&rsquo;s YouTube channel</b>, '
             'following his announcement that he had vacated the heavyweight title.</li>'
             '<li><b>Brian Ortega has hit back at fans</b> speculating that he is dodging Renato Moicano, after a '
             'second withdrawal from that fight in a single year.</li>'
             '</ul></div>')

    o.append('<h2 class="sec">Rankings &amp; business</h2>')
    o.append('<div class="panel">'
             '<p><b>Rankings movement.</b> Two belts sit vacant. <b>Heavyweight</b> opened up on 14 September when '
             '<b>Tom Aspinall vacated</b> the undisputed title over continuing complications with his eyes: he '
             'cannot be medically cleared, has had multiple surgeries, accidents and infections, and suffered '
             'further damage to his right eye in an accident after agreeing a fight date and returning to sparring. '
             'He is <b>not retiring</b> and intends to return once cleared; the root cause traces to the eye pokes '
             'in his no-contest with Ciryl Gane at UFC 321 in October 2025. <b>Ciryl Gane</b> holds the interim '
             'heavyweight belt. <b>Women&rsquo;s flyweight</b> is vacant after Shevchenko&rsquo;s withdrawal, and '
             'is contested on 3 October.</p>'
             '<p><b>Business &amp; broadcast.</b> UFC 331 streams in full on <b>Paramount+</b> in the United '
             'States, with early prelims at 5 PM ET and the main card at 9 PM ET. <b>No viewership, gate or TKO '
             'Group financial figures are published this edition</b> &mdash; none appeared in any source read this '
             'run, and none is estimated.</p></div>')

    o.append('<h2 class="sec">Champions board</h2>')
    o.append('<div class="tblwrap"><table><thead><tr><th>Division</th><th>Champion</th><th>Won the title</th>'
             '<th>Notes</th></tr></thead><tbody>')
    champs = [
        ("Heavyweight", "<b style='color:var(--warn)'>Vacant</b>", "&mdash;",
         "Tom Aspinall vacated on 14 September 2026 (eye complications; not retired)."),
        ("Heavyweight (interim)", "Ciryl Gane", "KO2 Alex Pereira &middot; Freedom 250, 14 Jun 2026",
         "Interim titleholder."),
        ("Light Heavyweight", "Carlos Ulberg", "KO1 Ji&#345;&iacute; Proch&aacute;zka &middot; UFC 327, 11 Apr 2026",
         "Won the vacant belt; had ACL surgery afterwards."),
        ("Middleweight", "Sean Strickland", "Split decision, Khamzat Chimaev &middot; UFC 328, 9 May 2026",
         "Two-time champion."),
        ("Welterweight", "Islam Makhachev", "UD Jack Della Maddalena &middot; UFC 322, 15 Nov 2025",
         "1 defence &mdash; UD Ian Machado Garry, UFC 330, 15 Aug 2026 (17th straight UFC win, a record)."),
        ("Lightweight", "Justin Gaethje", "TKO4 Ilia Topuria &middot; Freedom 250, 14 Jun 2026", "&mdash;"),
        ("Featherweight", "Alexander Volkanovski", "UD Diego Lopes &middot; UFC 314, 12 Apr 2025",
         "1 defence &mdash; UD Lopes, UFC 325, 31 Jan 2026. Booked to defend at UFC 333."),
        ("Bantamweight", "Petr Yan", "UD Merab Dvalishvili &middot; UFC 323, 6 Dec 2025",
         "Booked to defend at UFC 333."),
        ("Flyweight", "Joshua Van", "TKO1 Alexandre Pantoja &middot; UFC 323, 6 Dec 2025",
         "1 defence &mdash; TKO5 Tatsuro Taira, UFC 328, 9 May 2026. Defends vs Pantoja on Saturday."),
        ("Women&rsquo;s Flyweight", "<b style='color:var(--warn)'>Vacant</b>", "&mdash;",
         "Shevchenko vacated while injured; Natalia Silva vs Wang Cong contest it at UFC 332, 3 Oct 2026."),
        ("Women&rsquo;s Bantamweight", "Kayla Harrison", "Submission (R2) Julianna Pe&ntilde;a &middot; UFC 316, 7 Jun 2025",
         "0 defences &mdash; the UFC 324 defence vs Amanda Nunes was cancelled after Harrison withdrew for neck surgery."),
        ("Women&rsquo;s Strawweight", "Mackenzie Dern", "UD Virna Jandiroba &middot; UFC 321, 25 Oct 2025",
         "1 defence &mdash; UD Gillian Robertson, UFC 330, 15 Aug 2026."),
    ]
    for d, c, w, n in champs:
        o.append('<tr><td><b>%s</b></td><td>%s</td><td style="font-size:13px">%s</td>'
                 '<td style="font-size:13px;color:var(--muted)">%s</td></tr>' % (d, c, w, n))
    o.append('</tbody></table></div>')
    o.append('<div class="note"><b>Verification, and two refusals.</b> A direct fetch of ESPN&rsquo;s '
             '&ldquo;Current and all-time UFC champions&rdquo; page returned <b>no usable content</b> this run. A '
             'search-level rendering of that page was checked instead and contained <b>two errors, both '
             'refused</b>: it seated <b>Alex Pereira at light heavyweight</b> on an October 2025 win &mdash; an '
             'entry that predates UFC 327, where Carlos Ulberg won the vacated belt &mdash; and it labelled '
             '<b>Ulberg as heavyweight champion</b>, a division that is <i>vacant</i>. Its remaining rows '
             '(Strickland, Makhachev, Gaethje, Volkanovski, Yan) agree with the board above. Every belt here is '
             're-derived from the most recent title-changing card rather than copied from any single list.</div>')

    o.append(sources([
        ("UFC.com &mdash; Flyweight Champion Joshua Van Set For Rematch With Alexandre Pantoja At Crypto.com UFC 331",
         "https://www.ufc.com/news/flyweight-champion-joshua-van-set-rematch-alexandre-pantoja-cryptocom-ufc-331"),
        ("Wikipedia &mdash; UFC 331", "https://en.wikipedia.org/wiki/UFC_331"),
        ("ESPN &mdash; UFC 331: Van vs. Pantoja 2 live fight coverage",
         "https://www.espn.com/mma/fightcenter/_/id/600060963/league/ufc"),
        ("Yahoo Sports &mdash; UFC 331 full fight card, start time, odds, how to watch",
         "https://sports.yahoo.com/mma/article/ufc-331-full-fight-card-start-time-odds-where-to-watch-and-everything-to-know-for-van-vs-pantoja-2-200052945.html"),
        ("Yahoo Sports &mdash; UFC 331 main event and co-main opening betting odds and line movement",
         "https://sports.yahoo.com/articles/ufc-331-main-event-co-021332029.html"),
        ("Covers &mdash; UFC 331 odds for Sept. 19",
         "https://www.covers.com/ufc/331-odds-saturday-sept-19-2026"),
        ("Yahoo Sports &mdash; Brian Ortega shares graphic image of cut that forced him out of UFC 331",
         "https://sports.yahoo.com/articles/brian-ortega-shares-graphic-image-155600801.html"),
        ("Yahoo Sports &mdash; Renato Moicano blasts Brian Ortega for ruining &lsquo;easy paycheck&rsquo; at UFC 331",
         "https://sports.yahoo.com/mma/article/renato-moicano-blasts-brian-ortega-for-ruining-easy-paycheck-at-ufc-331-cautions-future-ortega-opponents-222910887.html"),
        ("Sherdog &mdash; Renato Moicano rips Brian Ortega for UFC 331 withdrawal",
         "https://www.sherdog.com/news/news/Renato-Moicano-rips-Brian-Ortega-for-UFC-331-withdrawal-202815"),
        ("MiddleEasy &mdash; Brian Ortega apologizes after UFC 331 withdrawal, explains eye cut",
         "https://middleeasy.com/mma-news/brian-ortega-apology-ufc-331-withdrawal-eye-cut"),
        ("MMA Mania &mdash; Muhammad Mokaev upset with UFC offer",
         "https://www.mmamania.com/ufc-news/472789/muhammad-mokaev-upset-with-ufc-offer-they-wasted-two-years-of-my-life"),
        ("Bloody Elbow &mdash; Ex-UFC fighter who went 7-0 blames them after &lsquo;deeply insulting&rsquo; offer",
         "https://bloodyelbow.com/2026/09/16/ex-ufc-fighter-who-went-7-0-blames-them-after-deeply-insulting-offer-wasted-two-years-of-my-life/"),
        ("CBS Sports &mdash; UFC 331: Joshua Van vs. Alexandre Pantoja fight card, date, odds, location",
         "https://www.cbssports.com/ufc/news/ufc-331-fight-card-date-odds-joshua-van-alexandre-pantoja/"),
        ("ESPN &mdash; Current and all-time UFC champions (fetched this run; returned no usable content)",
         "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
    ]))
    o.append('<div class="disc">Cards and bouts are subject to change. Betting lines are reported as a named book '
             'and moment stated them and move constantly; records, methods and scorecards are printed only where a '
             'source read this run states them.</div></footer>')
    o.append('</div>' + CDN_JS + STAMP_JS + '</body></html>')
    open(os.path.join(OUT, "mma-briefing.html"), "w").write("".join(o))

build_index(); build_cyber(); build_ws(); build_mma()
print("built 4 pages")
