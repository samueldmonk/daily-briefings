#!/usr/bin/env python3
"""Cyber page edits for the 10:50 AM Saturday Aug 29 2026 edition."""
import sys, io, os

D = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(D, "cyber-briefing.html")
STAMP = "10:50 AM"

h = io.open(P, encoding="utf-8").read()
fails = []


def rep(old, new, n=1):
    """Replace, treating count==0 as a FAILURE (standing rule)."""
    global h
    c = h.count(old)
    if c == 0:
        fails.append("NOT FOUND: " + old[:110])
        return
    if c != n:
        fails.append("COUNT %d != %d: %s" % (c, n, old[:110]))
        return
    h = h.replace(old, new)


# ---------------------------------------------------------------- 1. tldr
rep(
    "<div class=\"tldr\"><b>The Wire</b> <span>Two federal remediation deadlines expire today &mdash; the exploited Citrix NetScaler flaw and a 2019 SQL Server bug &mdash; PaperCut&rsquo;s researchers say new bypasses affect even the latest fully patched build, and the ATF has confirmed a cybersecurity &ldquo;major incident&rdquo; on a standalone system holding investigation records, which the Qilin group has claimed without evidence and the agency has not attributed to anyone.</span></div>",
    "<div class=\"tldr\"><b>The Wire</b> <span>McKesson has told the SEC it discovered a cybersecurity incident on August 25 involving third-party applications and data theft, and the ShinyHunters group claims it took roughly 284 million patient-related data records &mdash; records, not people &mdash; and demanded a $55,236,150 ransom the company did not answer; two federal remediation deadlines also expire today, and Ubiquiti has patched three separate maximum-severity UniFi flaws.</span></div>",
)

# ---------------------------------------------------------------- 2. threat-level why
rep(
    """<span class="why">Two CISA remediation deadlines run out <b>today</b> and two more fall <b>tomorrow</b>;
one of today's flaws is under live exploitation from a dozen attacker IPs, and PaperCut's first emergency
patch for an exploited zero-day chain was bypassed within a day and required a replacement.</span>""",
    """<span class="why">Two CISA remediation deadlines run out <b>today</b> and two more fall <b>tomorrow</b>;
one of today's flaws is under live exploitation from a dozen attacker IPs, PaperCut's first emergency
patch for an exploited zero-day chain was bypassed within a day and required a replacement, and the
largest claimed healthcare data theft on this page all week &mdash; McKesson &mdash; was reportedly reached
through phone calls to employees rather than through any of it.</span>""",
)

# ---------------------------------------------------------------- 3. stat strip
rep(
    """<div class="stat"><div class="n">21,019</div><div class="l">CVEs in 2025 attributable to injection weaknesses &mdash; CISA's most dominant category, up from 7,701 in 2024</div></div>""",
    """<div class="stat"><div class="n">284M</div><div class="l">Data <b>records</b> &mdash; explicitly not patients &mdash; ShinyHunters claims it took from McKesson's Snowflake environment</div></div>
<div class="stat"><div class="n">$55,236,150</div><div class="l">Ransom the group says it demanded of McKesson, with a 72-hour deadline; it says the company did not reply</div></div>""",
)

# ---------------------------------------------------------------- 4. new Top Story: McKesson
rep(
    """</div><h2 class="sec">Top Story</h2>
<div class="panel lead" style="border-left:3px solid var(--acc)">
<h3>PaperCut's emergency patch was bypassed. The second one shipped a day later.</h3>""",
    """</div><h2 class="sec">Top Story</h2>
<div class="panel lead" style="border-left:3px solid var(--acc)">
<div style="margin-bottom:9px"><span class="tag new">New &middot; """ + STAMP + """</span> <span class="tag crit">Healthcare</span> <span class="tag warn">Claims unverified</span></div>
<h3>McKesson tells the SEC it was breached. ShinyHunters says it took 284 million records and asked for $55 million.</h3>
<p><b>What the company itself says.</b> McKesson &mdash; a major U.S. healthcare company and pharmaceutical
distributor supplying medicines, medical supplies, technology and services to providers and pharmacies &mdash;
disclosed a cybersecurity incident in a <b>Form 8-K filing with the U.S. Securities and Exchange
Commission</b>, after CyberInsider first reported it. McKesson says it <b>discovered the incident on
August 25, 2026</b> and that the investigation <b>remains in the early stages</b>. In a separate notice to
customers it confirmed the incident <b>involved third-party applications and the unauthorised access and
exfiltration of data</b>. As of the filing date the company had <b>not determined that the incident is
material</b>, or reasonably likely to have a material impact on its financial condition or results. It warns
customers may see <b>intermittent service degradation</b> believed to be related to the attack, while saying
it is <b>not proactively disconnecting systems</b> in its environment.</p>
<p><b>What the company has not said &mdash; and this page does not fill in.</b> McKesson has
<b>not publicly disclosed which third-party applications were compromised, how the attackers gained access, or
what information was stolen</b>. Everything in the two paragraphs below is the attacker's account, relayed by
the outlet it spoke to, and the outlet states plainly that it has <b>not independently verified</b> it.</p>
<p><b>What the attacker claims.</b> <b>ShinyHunters</b> says it was behind the attack and that it got in by
<b>voice phishing &mdash; vishing &mdash; multiple McKesson employees</b>, compromising their <b>Okta
single sign-on accounts</b> and using those to reach the company's <b>Salesforce and Snowflake</b>
environments. It claims it fully compromised the Salesforce environment including support cases, took a much
larger set of patient-related data out of Snowflake, and <b>exfiltrated about 1TB over four days, between
August 21 and August 25</b>. It says it contacted McKesson after finishing on August 25 and demanded
<b>$55,236,150</b> within 72 hours, and that the company neither responded nor negotiated.</p>
<p><b>The 284 million figure is a count of records, not of people &mdash; and the correction came from the
attacker.</b> Earlier reporting stated that information belonging to <b>284 million patients</b> had been
exposed. ShinyHunters clarified that the number is a <b>raw count of roughly 284 million data records, or
lines</b>, and that it has <b>not fully analysed the data and does not know how many unique people appear in
it</b>. Both forms are printed here, because rows and people are different quantities and only one of them was
ever actually claimed. This page prints neither as a victim count.</p>
<p><b>The lure domain has a documented pattern behind it, and that part is actionable.</b> Separately from the
attacker, the reporting outlet says it learned the campaign used the domain
<span class="mono">mckesson[.]claims</span>. That matches a campaign documented by <b>ReliaQuest</b>'s threat
research team, which said ShinyHunters has been registering <span class="mono">company[.]claims</span> domains
carrying a target organisation's name or abbreviation in order to impersonate its help desk and IT teams.
ReliaQuest's post has since been deleted. If you do nothing else with this item, look for newly registered
<span class="mono">.claims</span> domains bearing your own company's name.</p>
<p><b>It is not an isolated case.</b> <b>Health-ISAC</b> has warned healthcare organisations about rising
ShinyHunters data-theft attacks that use social engineering to compromise corporate accounts and reach cloud
and SaaS platforms. Other healthcare and health-technology companies named as recent targets in the same
reporting: <b>Medtronic</b>, <b>DentaQuest</b>, <b>iRhythm</b>, <b>OneMedical</b> and <b>AdaptHealth</b>.</p>
<p class="note"><b>Claimed data categories, printed as claims.</b> ShinyHunters says the stolen material
includes names, addresses, dates of birth, Social Security numbers, patient IDs, phone numbers, email
addresses, Medicaid numbers, medical record numbers, medication and allergy information, illnesses,
disabilities, appointment information and physician information, and separately that it covers deceased and
terminally ill patients, prescriptions and medication shipments, invoices, employee information, Salesforce
records, internal communications, and the providers and clinics using McKesson's services. <b>McKesson has
confirmed none of this list</b>, and no regulator has. It is here as an allegation with a name attached to it,
not as a finding.</p>
</div>
<div class="panel lead">
<div style="margin-bottom:9px"><span class="tag">Carried &middot; from the 10:20 edition</span></div>
<h3>PaperCut's emergency patch was bypassed. The second one shipped a day later.</h3>""",
)

# The PaperCut block's closing "not printed" note claims "this run" freshness; rescope it.
rep(
    """<p class="note">Still not stated by any source seen this run, and therefore not printed: the threat actor, the
number of victims, whether ransomware is involved, or how many servers are exposed.</p>""",
    """<p class="note">Still not stated by any source seen in any edition to date, and therefore still not
printed: the PaperCut threat actor, the number of victims, whether ransomware is involved, or how many servers
are exposed. This block is carried unchanged from the 10:20 AM edition; no source fetched at """ + STAMP + """
added to it.</p>""",
)

# ---------------------------------------------------------------- 5. Vulnerability Watch: Ubiquiti
rep(
    """<tr><td><b>GPUThor</b><br><span class="mono" style="font-size:11px">no CVE stated</span></td><td>Not stated</td>""",
    """<tr><td><b>CVE-2026-77537</b></td><td class="critc">10.0</td><td>Ubiquiti UniFi Protect Application (video surveillance management)</td>
<td><b>New &middot; """ + STAMP + """.</b> Improper input validation letting <b>unauthenticated</b> attackers
compromise unpatched devices. Patched <b>August 26, 2026</b>. <b>No credentials and no user interaction are
required</b> for any of the three Ubiquiti flaws in this table. <b>Not KEV-listed, and no source seen this run
states in-the-wild exploitation</b> &mdash; the severity, not the exploitation, is the reason it is here.</td></tr>
<tr><td><b>CVE-2026-77550</b></td><td class="critc">10.0</td><td>Ubiquiti UniFi OS</td>
<td><b>New &middot; """ + STAMP + """.</b> <b>CRLF injection</b> that remote, unprivileged attackers can use to
<b>bypass authentication</b> on UniFi OS devices or instances. Patched <b>August 26, 2026</b>. Not KEV-listed;
no exploitation stated.</td></tr>
<tr><td><b>CVE-2026-77554</b></td><td class="critc">10.0</td><td>Ubiquiti UniFi Talk Application (VoIP phone system)</td>
<td><b>New &middot; """ + STAMP + """.</b> <b>Command injection</b> arising from improper input validation.
Patched <b>August 26, 2026</b>. Three simultaneous maximum-severity flaws across three different UniFi
products is itself the story: successful exploitation of the set allows unauthorised access to management
functions, authentication bypass, or command execution. Not KEV-listed; no exploitation stated.</td></tr>
<tr><td><b>GPUThor</b><br><span class="mono" style="font-size:11px">no CVE stated</span></td><td>Not stated</td>""",
)

rep(
    """<td><b>New &middot; 10:20 AM.</b> A Rowhammer attack from University of Toronto researchers""",
    """<td><b>Sourced in the 10:20 AM edition; carried.</b> A Rowhammer attack from University of Toronto researchers""",
)

rep(
    """<b>No CVE identifier and no CVSS score were stated by any source seen this run, so neither is printed</b>""",
    """<b>No CVE identifier and no CVSS score were stated by any source seen in the edition that sourced it, so neither is printed</b>""",
)

# ---------------------------------------------------------------- 6. KEV re-verification note
rep(
    """<div class="note"><b>Re-verified at 10:20 AM, on weaker provenance than a direct read, and the page says so.</b> A <b>direct fetch of CISA&rsquo;s own August 26 alert page returned an empty body</b> this run. The batch was therefore confirmed from <b>search results that enumerate all six CVEs of that batch by identifier</b> &mdash; CVE-2015-3246, CVE-2015-5287, CVE-2019-1068, CVE-2021-23758, CVE-2022-0995 and CVE-2026-8452 &mdash; matching the standing record exactly, with <b>no new KEV batch added since August 26</b>. A snippet-mediated read of a primary source is not the same as reading it, and the difference is printed rather than smoothed over.""",
    """<div class="note"><b>Checked again at """ + STAMP + """, and the check this time was a different one.</b> A
direct fetch of CISA's own August 26 alert page had <b>returned an empty body</b> at 10:20 AM, so that edition
confirmed the batch from search snippets. At """ + STAMP + """ the catalogue was approached from the other end
instead: a search for August 2026 KEV additions returned <b>CISA's own alert pages for August 7 (one CVE),
August 11 (three), August 18 (four), August 20 (two) and August 26 (six)</b>, and <b>no CISA alert dated later
than August 26</b>. That is consistent with the board below and is the reason no new batch appears on it.
&#9888; Stated precisely: <b>no later alert was returned</b> by the search run at """ + STAMP + """, which is
not the same as CISA having published none &mdash; this page does not have a live view of the catalogue and
says so rather than implying one.""",
)

# ---------------------------------------------------------------- 7. "what changed" note
rep(
    """<div class="note"><b>What changed since the last edition.</b> The <b>Aug 26 batch is now fully enumerated</b>""",
    """<div class="note"><b>What changed at """ + STAMP + """: nothing on this board.</b> All four countdowns are
unchanged at <b>0 / 1 / 11 / 12</b> days and no CVE was added to or removed from the deadline list. The
paragraph below records the change made in an <b>earlier</b> edition and is kept because it explains the shape
of the board. The <b>Aug 26 batch is now fully enumerated</b>""",
)

# ---------------------------------------------------------------- 8. injection-stat context (stat strip moved it out)
rep(
    """<div class="note"><b>Context from CISA's own review, published alongside the batch.</b> Analysing CVE records""",
    """<div class="note"><b>Context from CISA's own review, published alongside the batch.</b> The two figures
below were on the headline stat strip in earlier editions and moved down here at """ + STAMP + """ to make room
for the McKesson numbers; the sourcing is unchanged. Analysing CVE records""",
)

# ---------------------------------------------------------------- 9. sources
rep(
    """<a href="https://industrialcyber.co/reports/energy-and-utilities-sector-targeted-in-66-of-observed-apt-campaigns-as-mustang-panda-lazarus-sandworm-remain-active/">Industrial Cyber &mdash; Energy and utilities targeted in 66% of observed APT campaigns</a><br></div>""",
    """<a href="https://industrialcyber.co/reports/energy-and-utilities-sector-targeted-in-66-of-observed-apt-campaigns-as-mustang-panda-lazarus-sandworm-remain-active/">Industrial Cyber &mdash; Energy and utilities targeted in 66% of observed APT campaigns</a><br><a href="https://www.bleepingcomputer.com/news/security/mckesson-discloses-breach-after-shinyhunters-claims-patient-data-theft/">BleepingComputer &mdash; McKesson discloses breach after ShinyHunters claims patient data theft</a><br><a href="https://cyberinsider.com/mckesson-data-breach-exposing-284-million-patients/">CyberInsider &mdash; ShinyHunters claims McKesson data breach exposing 284 million patients</a><br><a href="https://www.sec.gov/Archives/edgar/data/927653/000092765326000247/mck-20260825.htm">SEC EDGAR &mdash; McKesson Form 8-K, incident discovered August 25, 2026</a><br><a href="https://www.mckesson.com/utility/cybersecurity/customer-cybersecurity-information-center/">McKesson &mdash; Customer cybersecurity information center</a><br><a href="https://www.bleepingcomputer.com/news/security/ubiquiti-patches-three-max-severity-security-vulnerabilities/">BleepingComputer &mdash; Ubiquiti patches three max severity security vulnerabilities</a><br><a href="https://cyberscoop.com/ubiquiti-unifi-critical-vulnerabilities-patched/">CyberScoop &mdash; Three 10.0 security flaws fixed across Ubiquiti's UniFi line</a><br><a href="https://www.cisa.gov/news-events/alerts/2026/08/20/cisa-adds-two-known-exploited-vulnerabilities-catalog">CISA &mdash; Adds two known exploited vulnerabilities to catalog (Aug 20)</a><br></div>""",
)

# ---------------------------------------------------------------- 10. stamps
h = h.replace("10:20 AM ET", STAMP + " ET")

if fails:
    print("FAILURES:")
    for f in fails:
        print("  -", f)
    sys.exit(1)

io.open(P, "w", encoding="utf-8").write(h)
print("cyber OK")
