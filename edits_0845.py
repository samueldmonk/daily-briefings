#!/usr/bin/env python3
"""Targeted edits for the Saturday Aug 29 2026 second Morning Edition."""
import sys, os, datetime, zoneinfo

D = sys.argv[1] if len(sys.argv) > 1 else "."
now = datetime.datetime.now(zoneinfo.ZoneInfo("America/New_York"))
STAMP = now.strftime("%-I:%M %p")
OLD = "8:40 AM"

def rd(p):
    return open(os.path.join(D, p), encoding="utf-8").read()

def wr(p, s):
    open(os.path.join(D, p), "w", encoding="utf-8").write(s)

fails = []

def sub(s, old, new, label, count=None):
    n = s.count(old)
    if n == 0:
        fails.append("MISSING: " + label)
        return s
    if count is not None and n != count:
        fails.append("COUNT %d!=%d: %s" % (n, count, label))
    return s.replace(old, new)

# ---------------------------------------------------------------- MMA
m = rd("mma-briefing.html")

MMA_TLDR = ("Denise Gomes knocked out No. 4 strawweight Yan Xiaonan in the first round of the UFC Shanghai "
            "co-main event, the biggest upset on a card that has now produced twelve results in twelve completed "
            "bouts &mdash; only the Nurmagomedov&ndash;Song headliner was still unresulted when this edition was built.")
m = sub(m,
  "<div class=\"tldr\"><b>Tale of the Tape</b> <span>UFC Shanghai is running live as this edition publishes &mdash; all seven prelims and four main-card bouts are decided, six of the eleven by finish, but neither the Yan Xiaonan co-main nor the Nurmagomedov&ndash;Song headliner had been resulted by any source seen this run.</span></div>",
  "<div class=\"tldr\"><b>Tale of the Tape</b> <span>" + MMA_TLDR + "</span></div>",
  "mma tldr", 1)

# Top story
m = sub(m,
  "<h3>Shanghai, live: eleven bouts decided, six by finish, and the two that matter most still in the cage</h3>",
  "<h3>Gomes flattens Yan Xiaonan in Shanghai. Twelve bouts are in the book; only the headliner is not.</h3>",
  "mma top story h3", 1)

old_top = m[m.find("<h3>Gomes flattens"):m.find("<h2 class=\"sec\">Fight Week")]
new_top = """<h3>Gomes flattens Yan Xiaonan in Shanghai. Twelve bouts are in the book; only the headliner is not.</h3>
<p>UFC Fight Night: Nurmagomedov vs Song ran from the <b>Oriental Sports Center in Shanghai's Pudong
District</b> &mdash; prelims from <b>3:00 AM ET</b>, main card from <b>6:00 AM ET</b>, on Paramount+ in the
United States. A rare morning card for a U.S. audience, and it landed in the middle of this edition.</p>
<p>The result that moves a division came in the co-main. <b>Denise Gomes</b>, the No. 14 strawweight and a
<b>+125 underdog</b> against a <b>&minus;150</b> favourite, stopped <b>Yan Xiaonan</b> &mdash; No. 4 in the
division and a former title challenger &mdash; by <b>knockout with elbows and punches at 4:49 of round one</b>.
Gomes had rocked her with an overhand right roughly two minutes in; Yan came straight back at her, and the
fight stayed competitive until Gomes landed the finishing sequence in the closing seconds of the round.
Gomes entered on a four-fight winning streak.</p>
<p>Around it, the card was violent and it belonged to the newcomers. <b>Eight of the twelve completed bouts
ended inside the distance.</b> <b>Francesco Nuzzi</b>, <b>Hector Santiago</b>, <b>Bilal Hasan</b>, <b>Liu Ce</b>
and <b>Cam Nelson</b> all won in their first Octagon appearance, four of them by knockout; two of the three
Road to UFC winners on the card lost their debuts.</p>
<p><b>What this page still will not do is guess.</b> The five-round bantamweight headliner,
<b>Umar Nurmagomedov vs. Song Yadong</b>, was <b>not resulted by any source fetched this run</b> &mdash;
UFC.com's own main-card page, its scorecards page and Sherdog's live play-by-play were all still pre-result
at fetch time. It stays in the table below as <b>undecided</b> rather than being left out, so the gap is
visible. The next edition will carry it.</p>
<p class="note">Provenance, stated plainly: the co-main result comes from post-event search results fetched
this run, <b>not</b> from UFC.com, which had not yet published it. The prelim results are UFC.com's own
official page. The other four main-card results are corroborated this run by an independent results listing
and match the prior edition. Venue naming: UFC.com's event card reads &ldquo;Oriental Sports Center, Pudong
District&rdquo;; other listings render it &ldquo;Pudong Development Bank Shanghai Oriental Sports Center&rdquo;
and &ldquo;SPD Bank Oriental Sports Center&rdquo;. All three forms are recorded; none is adopted as canonical.</p>
</div>"""
m = sub(m, old_top, new_top, "mma top story body", 1)

# Results table
old_tbl = m[m.find("<h2 class=\"sec\">UFC Shanghai &mdash; Results So Far (live)</h2>"):m.find("<h2 class=\"sec\">Prospect Watch</h2>")]
new_tbl = """<h2 class="sec">UFC Shanghai &mdash; Results</h2>
<div class="panel" style="padding:6px 10px">
<table>
<tr><th>Result</th><th>Bout</th><th>Method</th></tr>
<tr><td class="warnc"><b>Undecided</b></td><td><b>Main event &middot;</b> Umar Nurmagomedov vs. Song Yadong (bantamweight, 5 rds)</td><td>Not resulted in any source fetched this run</td></tr>
<tr><td class="up"><b>Denise Gomes</b></td><td><b>Co-main &middot;</b> def. Yan Xiaonan (women's strawweight)</td><td>KO (elbows and punches), 4:49 of round 1</td></tr>
<tr><td class="up"><b>Kai Asakura</b></td><td>def. Aoriqileng (bantamweight)</td><td>KO (head kick and strikes), 0:34 of round 2</td></tr>
<tr><td class="up"><b>Sumudaerji</b></td><td>def. Alex Perez (flyweight)</td><td>Unanimous decision (29-28, 29-28, 29-28)</td></tr>
<tr><td class="up"><b>Liu Ce</b></td><td>def. Levi Rodrigues Jr. (light heavyweight)</td><td>KO (punch), 4:26 of round 1</td></tr>
<tr><td class="up"><b>Bilal Hasan</b></td><td>def. Nilson Rojas (flyweight)</td><td>KO (punch), 2:28 of round 2</td></tr>
<tr><td class="up"><b>Andre Lima</b></td><td>def. Namsrai Batbayar (flyweight, prelim)</td><td>Submission (guillotine choke), 3:03 of round 3</td></tr>
<tr><td class="up"><b>Rei Tsuruya</b></td><td>def. Kevin Borjas (flyweight, prelim)</td><td>Submission (rear-naked choke), 4:14 of round 1</td></tr>
<tr><td class="up"><b>Sean Woodson</b></td><td>def. Jack Jenkins (featherweight, prelim)</td><td>Split decision (29-28, 28-29, 29-28)</td></tr>
<tr><td class="up"><b>Francesco Nuzzi</b></td><td>def. Xiao Long (bantamweight, prelim)</td><td>TKO (punches), 1:00 of round 1</td></tr>
<tr><td class="up"><b>Hector Santiago</b></td><td>def. Lawrence Lui (bantamweight, prelim)</td><td>KO (punches), 0:53 of round 2</td></tr>
<tr><td class="up"><b>Julia Polastri</b></td><td>def. Xiong Jingnan (catchweight, prelim)</td><td>KO (head kick), 3:06 of round 1</td></tr>
<tr><td class="up"><b>Cam Nelson</b></td><td>def. Ding Meng (welterweight, prelim)</td><td>Unanimous decision (29-28, 29-28, 29-28)</td></tr>
</table></div>
<div class="note"><b>Every weight class above is now sourced.</b> The four bouts that carried no division label
in the previous edition have one here, taken from UFC.com's official scorecards headings and from Sherdog's
published weigh-in figures for each fighter. The Polastri&ndash;Xiong bout is labelled <b>catchweight</b>
because <b>both</b> women missed the 115-pound strawweight limit (117 and 118.5) and the contest was
rescheduled at a catchweight &mdash; a fact the previous edition had only half of.
<b>A method discrepancy, recorded:</b> an aggregated results listing seen this run describes the Lima finish
as a rear-naked choke; <b>UFC.com's own recap and Sherdog's round-by-round both say guillotine choke</b>, and
the primary sources are what this table prints.
<b>Performance bonuses: still none announced in any source seen this run</b> &mdash; expected, since the main
event has not been resulted. <b>Three fighters missed weight</b>: Andre Lima (127, his second miss in the UFC,
which eliminates him from the bonus conversation and costs him <b>20% of his purse to Batbayar</b>), Xiong
Jingnan (117) and Julia Polastri (118.5).</div>"""
m = sub(m, old_tbl, new_tbl, "mma results table", 1)

# Fight week: add Paris card
m = sub(m,
  """<div class="card"><div class="tags"><span class="tag">Carried</span></div>
<div class="dateline">Tue, Sept 1 &middot; 7:00 PM ET</div>""",
  """<div class="card"><div class="tags"><span class="tag new">New &middot; %s</span></div>
<div class="dateline">Sat, Sept 5 &middot; Accor Arena, Paris</div>
<h4>UFC Fight Night 287 &mdash; Dan Hooker vs. Salahdine Parnasse</h4>
<p>The promotion's return to France, headlined by a lightweight bout between <b>Dan Hooker</b> and
<b>Salahdine Parnasse</b>. <b>13 bouts</b>, with <b>Fares Ziam vs. Axel Sola</b>, <b>Michael Page vs.
Nursulton Ruziboev</b> and <b>Losene Keita vs. Muhammadjon Naimov</b> also listed. Prelims from
<b>12:00 PM ET</b> on Paramount+ &mdash; another early card for a U.S. audience.
<b>No betting line for this card was stated by any source seen this run, so none is printed.</b></p></div>
<div class="card"><div class="tags"><span class="tag">Carried</span></div>
<div class="dateline">Tue, Sept 1 &middot; 7:00 PM ET</div>""" % STAMP,
  "mma paris card", 1)

# Around the sport - add catchweight / purse item
m = sub(m,
  """<li><b>Sean Woodson's return.</b>""",
  """<li><b>The weight problem on this card was collective, not individual.</b> Three of thirteen fighters
missed. Lima forfeits <b>20% of his purse</b> to Batbayar; the Xiong&ndash;Polastri bout was re-made as a
<b>catchweight</b> after both women came in heavy, which is why that row above carries no divisional label.
Batbayar's <b>six-fight winning streak</b> ended with the guillotine.</li>
<li><b>Sean Woodson's return.</b>""",
  "mma weight item", 1)

# Rankings card
m = sub(m,
  """<p><b>Umar Nurmagomedov</b> is the No. 3 bantamweight and a former title challenger; <b>Song Yadong</b> is No. 6.
In the co-main, <b>Yan Xiaonan</b> is the No. 4 strawweight and <b>Denise Gomes</b> No. 14. At UFC 331,
<b>Arman Tsarukyan</b> is the No. 2 lightweight and <b>Mauricio Ruffy</b> No. 10. <b>No ranking movement has been
published for this card</b> &mdash; the main event is unresolved, so none is asserted.</p>""",
  """<p><b>Umar Nurmagomedov</b> is the No. 3 bantamweight and a former title challenger; <b>Song Yadong</b> is
No. 6 &mdash; both rankings taken from UFC.com's own event copy this run, which corrects the No. 2 this page
carried for Nurmagomedov in earlier editions. In the co-main, <b>Denise Gomes</b> was ranked <b>No. 14</b> and
beat the <b>No. 4</b>, <b>Yan Xiaonan</b>, by first-round knockout &mdash; a ten-place gap closed in a single
round, and Gomes's fifth straight win. At UFC 331, <b>Arman Tsarukyan</b> is the No. 2 lightweight and
<b>Mauricio Ruffy</b> No. 10. <b>No updated rankings table has been published for this card</b>, so no new
position is asserted for anyone; the movement above is described, not numbered.</p>""",
  "mma rankings card", 1)

# Sources
m = sub(m,
  """<a href="https://www.si.com/fannation/mma/news/ufc-shanghai-free-live-stream-results-highlights-for-nurmagomedov-vs-song">Sports Illustrated / FanNation &mdash; UFC Shanghai results and highlights</a><br>""",
  """<a href="https://www.si.com/fannation/mma/news/ufc-shanghai-free-live-stream-results-highlights-for-nurmagomedov-vs-song">Sports Illustrated / FanNation &mdash; UFC Shanghai results and highlights</a><br><a href="https://sports.yahoo.com/articles/ufc-shanghai-results-nurmagomedov-vs-040000866.html">Yahoo Sports &mdash; UFC Shanghai Results: Nurmagomedov vs. Song</a><br><a href="https://www.ufc.com/news/ufc-shanghai-official-scorecards-nurmagomedov-vs-song">UFC.com &mdash; Official Scorecards | UFC Shanghai (bout weight classes)</a><br><a href="https://www.fightmag.com/ufc-shanghai-nurmagomedov-vs-song-live-results/">FIGHTMAG &mdash; UFC Shanghai live results</a><br><a href="https://www.ufc.com/event/ufc-fight-night-september-05-2026">UFC.com &mdash; UFC Fight Night: Hooker vs Parnasse (Paris, Sept 5)</a><br><a href="https://en.wikipedia.org/wiki/UFC_Fight_Night:_Hooker_vs._Parnasse">Wikipedia &mdash; UFC Fight Night: Hooker vs. Parnasse (card, venue, broadcast)</a><br>""",
  "mma sources", 1)

wr("mma-briefing.html", m)

# ---------------------------------------------------------------- CYBER
c = rd("cyber-briefing.html")

CY_TLDR = ("Two federal remediation deadlines expire today &mdash; the exploited Citrix NetScaler flaw and a "
           "2019 SQL Server bug &mdash; and Cisco Talos has named the crew behind four of the six CVEs in the "
           "same CISA batch: a Chinese-speaking group running <b>agentic AI</b> through its intrusions against a "
           "target list of roughly 170,000 URLs.")
c = sub(c,
  "<div class=\"tldr\"><b>The Wire</b> <span>The federal deadline to remediate an actively exploited Citrix NetScaler flaw expires today, and PaperCut has shipped a <b>second</b> emergency patch after attackers bypassed the first &mdash; two internet-facing products under live exploitation with the clock already run out on one of them.</span></div>",
  "<div class=\"tldr\"><b>The Wire</b> <span>" + CY_TLDR + "</span></div>",
  "cyber tldr", 1)

c = sub(c,
  """<span class="why">A CISA remediation deadline for an exploited Citrix NetScaler flaw runs out <b>today</b>,
a second federal deadline falls <b>tomorrow</b>, and PaperCut's first emergency patch for an exploited
zero-day chain was bypassed within a day and required a replacement.</span></div>""",
  """<span class="why">Two CISA remediation deadlines run out <b>today</b> and two more fall <b>tomorrow</b>;
one of today's flaws is under live exploitation from a dozen attacker IPs, and PaperCut's first emergency
patch for an exploited zero-day chain was bypassed within a day and required a replacement.</span></div>""",
  "cyber threat why", 1)

old_stats = c[c.find('<div class="stats">'):c.find('<h2 class="sec">Top Story</h2>')]
new_stats = """<div class="stats">
<div class="stat"><div class="n">0 days</div><div class="l">Left on <b>two</b> federal deadlines &mdash; CVE-2026-8452 and CVE-2019-1068 are both due today, Aug 29</div></div>
<div class="stat"><div class="n">36</div><div class="l">Citrix NetScaler exploitation attempts detected in 12 days, from 12 unique attacker IPs in 10 countries</div></div>
<div class="stat"><div class="n">170,000</div><div class="l">URLs on the target list recovered from UAT-10147's own infrastructure by Cisco Talos</div></div>
<div class="stat"><div class="n">21,019</div><div class="l">CVEs in 2025 attributable to injection weaknesses &mdash; CISA's most dominant category, up from 7,701 in 2024</div></div>
</div>"""
c = sub(c, old_stats, new_stats, "cyber stats", 1)

# Patch priority callout
c = sub(c,
  """<h4>CVE-2026-8452 &mdash; Citrix NetScaler ADC and Gateway &mdash; federal deadline expires TODAY</h4>""",
  """<h4>CVE-2026-8452 &mdash; Citrix NetScaler ADC and Gateway &mdash; federal deadline expires TODAY</h4>""",
  "cyber pp h4", 1)

c = sub(c,
  """with AAA or Gateway exposed, this is the one item on this page that was already overdue when you read it.</p>
</div>""",
  """with AAA or Gateway exposed, this is the item on this page most likely to be already overdue when you read
it.</p>
<p><b>New this run &mdash; the exploitation is quantified.</b> Telemetry cited by CISA-tracking researchers
records <b>36 exploitation attempts over the past 12 days</b> from <b>12 unique attacker IP addresses</b>
across <b>Switzerland, Germany, Hong Kong, Japan, the Netherlands, Russia, Singapore, T&uuml;rkiye, the United
States and Vietnam</b>. The observed post-exploitation behaviour is specific enough to hunt for: attackers
dropped web shells named <b>x.php</b> and <b>z.php</b> and ran discovery commands including <b>id</b> and
<b>echo</b>. If you cannot patch today, look for those filenames first.</p>
<p><b>A second deadline expires alongside it.</b> <b>CVE-2019-1068</b>, a remote code execution flaw in
<b>Microsoft SQL Server</b> that lets an attacker execute code in the context of the SQL Server Database Engine
service account, was added to KEV in the same August 26 batch and carries the <b>same August 29 due date</b>.
It ranks second here only because <b>there is currently no public information on how it is being exploited in
the wild</b> &mdash; which is a reason to patch it, not a reason to deprioritise it.</p>
</div>""",
  "cyber pp additions", 1)

# Threat actor spotlight
old_spot = c[c.find('<h2 class="sec">Threat Actor Spotlight</h2>'):c.find('<h2 class="sec">Breaches &amp; Incidents</h2>')]
new_spot = """<h2 class="sec">Threat Actor Spotlight</h2><div class="cards">
<div class="card"><div class="tags"><span class="tag new">New &middot; __STAMP__</span><span class="tag crit">Agentic AI</span><span class="tag">China-nexus</span></div>
<h4>UAT-10147 &mdash; and the SPECTRE implant</h4>
<p>Cisco Talos has documented a Chinese-speaking cybercrime group tracked as <b>UAT-10147</b>, active since
early 2026, that targets internet-facing Windows and Linux web servers for <b>data theft and SEO fraud</b>.
What sets it apart is that it has wired <b>AI-driven tooling into exploitation, reconnaissance, payload
generation, validation and persistence</b>. Talos recovered <b>AI-generated operational playbooks</b> from
actor infrastructure &mdash; including a nine-section ASP.NET ViewState exploitation guide documenting a real
intrusion in granular detail, down to hostnames, IP addresses and the MachineKey values needed to forge a
valid ViewState payload &mdash; alongside a target list of roughly <b>170,000 URLs</b>. Tooling observed:
<b>Metasploit</b>, <b>ysoserial</b>, <b>PentestGPT</b>, <b>DeepAudit</b> and multiple privilege-escalation
exploits. Its most capable payload is <b>SPECTRE</b>, a custom C backdoor for Windows and Linux; the Windows
build supports <b>45 commands</b> covering screenshots, credential theft, keylogging, token impersonation,
process injection, in-memory .NET execution and privilege escalation, with Linux rootkit and BYOVD
capabilities reported. <b>This is the group behind four of the six CVEs CISA added on August 26</b>
&mdash; the two Red Hat flaws, the Linux kernel write and the Ajax.NET deserialization bug.</p></div>
<div class="card"><div class="tags"><span class="tag">Iran-nexus</span><span class="tag">Espionage</span></div>
<h4>Screening Serpens</h4>
<p>Unit 42 researchers report cyberattacks by the Iran-nexus advanced persistent threat group
<b>Screening Serpens</b>, targeting entities in the <b>United States, Israel and the United Arab Emirates</b>, and
likely two additional Middle Eastern entities. <b>No malware family, initial-access vector, victim count or
campaign date range is stated in the material seen this run, and none is printed here</b> &mdash; the finding on
this page is the targeting set, not a technical profile.</p></div>
<div class="card"><div class="tags"><span class="tag">Sector data</span></div>
<h4>Where the campaigns are landing</h4>
<p>CYFIRMA research, via Industrial Cyber, puts <b>energy and utilities</b> organisations in <b>66.6%</b> of all
observed APT campaigns over the last three months &mdash; the headline rounds it to 66%; both forms are recorded.
Named as remaining active in the same reporting: <b>Mustang Panda</b>, <b>Lazarus</b> and <b>Sandworm</b>.</p></div>
</div>""".replace("__STAMP__", STAMP)
c = sub(c, old_spot, new_spot, "cyber spotlight", 1)

# Vulnerability watch additions
c = sub(c,
  """<tr><td><b>CVE-2026-53362</b></td><td>Not stated</td><td>Linux kernel</td>""",
  """<tr><td><b>CVE-2019-1068</b></td><td>Not stated</td><td>Microsoft SQL Server</td>
<td>Remote code execution in the context of the SQL Server Database Engine service account. <b>KEV-listed
Aug 26, federal deadline today, Aug 29.</b> No public information on how it is being exploited in the wild;
no CVSS was stated this run, so none is printed.</td></tr>
<tr><td><b>CVE-2026-69836</b></td><td class="critc">10.0</td><td>Microsoft Entra ID</td>
<td>Unauthenticated, network-accessible remote code execution in the identity backbone; CWE-502,
deserialization of untrusted data. Disclosed <b>Aug 20</b>. Microsoft first tagged it &ldquo;Exploited:
Yes&rdquo;, then <b>corrected the status to &ldquo;No&rdquo; on Aug 21</b>. Microsoft says it fixed the issue
service-side and that customers need take no additional action. <b>Not KEV-listed.</b></td></tr>
<tr><td><b>CVE-2022-0995</b></td><td>Not stated</td><td>Linux kernel &mdash; watch queue</td>
<td>Out-of-bounds memory write; a local user can gain privileged access or cause a denial of service.
KEV-listed <b>Aug 26</b>, due <b>Sept 9</b>. Tied to UAT-10147 by Cisco Talos.</td></tr>
<tr><td><b>CVE-2021-23758</b></td><td>Not stated</td><td>Ajax.NET Professional (AjaxPro)</td>
<td>Deserialization of untrusted data allowing remote code execution via arbitrary .NET classes.
KEV-listed <b>Aug 26</b>, due <b>Sept 9</b>. Tied to UAT-10147.</td></tr>
<tr><td><b>CVE-2015-5287</b></td><td>Not stated</td><td>Red Hat Automatic Bug Reporting Tool (ABRT)</td>
<td>Privilege escalation via a symlink attack on a file with a predictable name, exploitable by local users
with certain permissions. KEV-listed <b>Aug 26</b>, due <b>Sept 9</b>. Eleven years old and being used now.</td></tr>
<tr><td><b>CVE-2015-3246</b></td><td>Not stated</td><td>Red Hat libuser</td>
<td>Race condition letting an authenticated local user corrupt /etc/passwd for denial of service or privilege
escalation. KEV-listed <b>Aug 26</b>, due <b>Sept 9</b>.</td></tr>
<tr><td><b>CVE-2026-53362</b></td><td>Not stated</td><td>Linux kernel</td>""",
  "cyber vuln rows", 1)

# KEV section
old_kev = c[c.find('<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>'):c.find('<footer>')]
new_kev = """<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>
<div class="panel"><ul class="bul">
<li><b>CVE-2026-8452</b> (Citrix NetScaler ADC and Gateway) and <b>CVE-2019-1068</b> (Microsoft SQL Server)
&mdash; added <b>Aug 26</b> in a six-CVE batch, both due <b>Saturday, Aug 29</b>.
<span class="critc"><b>(0 days left &mdash; due today)</b></span></li>
<li><b>CVE-2026-53362</b> (Linux kernel) and <b>CVE-2023-49105</b> (ownCloud) &mdash; added <b>Aug 27</b>, due
<b>Sunday, Aug 30</b>. <span class="warnc"><b>(1 day left)</b></span></li>
<li><b>CVE-2022-0995</b> (Linux kernel), <b>CVE-2021-23758</b> (Ajax.NET Professional),
<b>CVE-2015-5287</b> (Red Hat ABRT) and <b>CVE-2015-3246</b> (Red Hat libuser) &mdash; the remaining four of the
<b>Aug 26</b> batch, all due <b>Wednesday, Sept 9</b>. <b>(11 days left)</b></li>
<li><b>CVE-2026-66384</b> &mdash; JFrog Artifactory &mdash; added <b>Aug 27</b>, due
<b>Thursday, Sept 10</b>. <b>(12 days left)</b></li>
</ul></div>
<div class="note">These windows are assigned per-CVE under <b>BOD 26-04</b>, which prioritises security updates
based on risk. They are not computed by this page and they do not follow a fixed interval: the Aug 26 batch
splits <b>3 days</b> for two CVEs and <b>14 days</b> for the other four from the same add date, and the Aug 27
batch splits <b>3</b> and <b>14</b> the same way. The older <b>BOD 22-01</b> &ldquo;three weeks from the add
date&rdquo; heuristic is superseded and is not used here. Countdowns above are measured from
<b>Saturday, August 29, 2026</b>.</div>
<div class="note"><b>What changed since the last edition.</b> The <b>Aug 26 batch is now fully enumerated</b>
&mdash; the previous edition carried only the Citrix entry from it and described the Aug 27 batch as
&ldquo;three CVEs&rdquo;. Six were added on Aug 26, and a second deadline expiring today
(<b>CVE-2019-1068</b>) was previously unrecorded on this page. Four of those six are attributed by Cisco Talos
to <b>UAT-10147</b>, which is why the spotlight above and this section describe the same operation. The Oracle
item (CVE-2026-21962), overdue as of Aug 27, was again not restated by any source seen this run and is again
not carried.</div>
<div class="note"><b>Context from CISA's own review, published alongside the batch.</b> Analysing CVE records
from 2024 and 2025, the agency found <b>injection weaknesses</b> the most dominant category &mdash;
<b>7,701 CVEs in 2024 and 21,019 in 2025</b> &mdash; and reported that <b>memory safety and improper input
validation weaknesses appear disproportionately in KEV entries compared with the full CVE population</b>.
CISA's framing: attackers are exploiting simple, known flaws that persist in exposed assets, and AI is being
used to automate that exploitation. The four aged CVEs above &mdash; two from 2015 &mdash; are the argument
made in list form.</div>"""
c = sub(c, old_kev, new_kev, "cyber kev", 1)

# Sources
c = sub(c,
  """<a href="https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog">CISA &mdash; Adds three known exploited vulnerabilities to catalog (Aug 27, 2026)</a><br>""",
  """<a href="https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog">CISA &mdash; Adds three known exploited vulnerabilities to catalog (Aug 27, 2026)</a><br><a href="https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog">CISA &mdash; Adds six known exploited vulnerabilities to catalog (Aug 26, 2026)</a><br><a href="https://thehackernews.com/2026/08/cisa-adds-six-exploited-flaws-to-kev.html">The Hacker News &mdash; CISA adds six exploited flaws to KEV, including NetScaler, Linux and SQL Server bugs</a><br><a href="https://securityaffairs.com/197975/hacking/u-s-cisa-adds-red-hat-linux-kernel-ajax-net-professional-microsoft-sql-server-and-citrix-netscaler-flaws-to-its-known-exploited-vulnerabilities-catalog.html">Security Affairs &mdash; CISA adds Red Hat, Linux Kernel, Ajax.NET Professional, Microsoft SQL Server and Citrix NetScaler flaws to KEV</a><br><a href="https://blog.talosintelligence.com/uat-10147-chinese-speaking-adversary-integrates-agentic-ai-into-post-compromise-operations/">Cisco Talos &mdash; UAT-10147: Chinese-speaking adversary integrates agentic AI into post-compromise operations</a><br><a href="https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/">Cisco Talos &mdash; UAT-10147 deploys SPECTRE, a cross-platform implant with Linux rootkit and BYOVD capabilities</a><br><a href="https://thehackernews.com/2026/08/uat-10147-uses-ai-to-scale-server.html">The Hacker News &mdash; UAT-10147 uses AI to scale server attacks, deploys SPECTRE with EDR bypass</a><br><a href="https://www.helpnetsecurity.com/2026/08/21/microsoft-entra-id-vulnerability-cve-2026-69836/">Help Net Security &mdash; Microsoft patches critical Entra ID vulnerability (CVE-2026-69836)</a><br><a href="https://thehackernews.com/2026/08/microsoft-entra-id-flaw-cvss-100.html">The Hacker News &mdash; Microsoft patches severe Entra ID flaw (CVSS 10.0) allowing remote code execution</a><br><a href="https://www.cisa.gov/resources-tools/resources/cisa-vulnerability-review">CISA &mdash; Vulnerability review (root causes of insecure software)</a><br>""",
  "cyber sources", 1)

wr("cyber-briefing.html", c)

# ---------------------------------------------------------------- WALL STREET
w = rd("wallstreet-briefing.html")

WS_TLDR = ("Markets are closed for the weekend, so Friday&rsquo;s official closes stand &mdash; the S&amp;P 500 "
           "slipped 0.25% to 7,711.76 and still finished the week higher &mdash; while the weekend&rsquo;s live "
           "story is Stripe and Advent walking away from a bid that valued PayPal above $53 billion, and the "
           "week ahead turns on Friday&rsquo;s payrolls report.")
w = sub(w,
  "<div class=\"tldr\"><b>The Tape</b> <span>Markets are closed for the weekend, so Friday&rsquo;s official closes stand &mdash; the S&amp;P 500 slipped 0.25% to 7,711.76 and still finished the week higher &mdash; while the weekend&rsquo;s live story is Stripe and Advent walking away from a $50 billion-plus pursuit of PayPal.</span></div>",
  "<div class=\"tldr\"><b>The Tape</b> <span>" + WS_TLDR + "</span></div>",
  "ws tldr", 1)

w = sub(w,
  """source seen this run, so none is printed.</p>
<p class="note">Weekend standing:""",
  """source seen this run, so none is printed. <b>Two reads of that move are on the record and neither is
adopted:</b> one report describes the fall as &ldquo;as much as 16% in premarket trading&rdquo;, another
headlines it as a <b>15%</b> plunge. Reporting seen this run adds that the board rejected the offer over
concerns it <b>undervalued the company</b>, that the two sides had been negotiating a potential higher price,
and that a future approach by Advent and Stripe <b>remains possible should conditions shift</b>.</p>
<p class="note">Weekend standing:""",
  "ws paypal detail", 1)

w = sub(w,
  """<li><b>Friday, September 4 &mdash; the jobs report.</b> The Employment Situation, covering nonfarm payrolls and
the unemployment rate, is released by the Bureau of Labor Statistics at <b>8:30 AM ET</b>. It is the first major
read on the labour market since Warsh's Jackson Hole warning, and the week's largest scheduled risk.</li>
<li><b>Next week's other U.S. releases:</b> <b>ISM Manufacturing PMI</b> and <b>ISM Services PMI</b>, alongside
Eurozone flash CPI and a Bank of Canada rate decision. Markets reopen Monday, August 31.</li>""",
  """<li><b>Friday, September 4 &mdash; the jobs report, and it now has a number attached.</b> The Employment
Situation is released by the Bureau of Labor Statistics at <b>8:30 AM ET</b>. Expectations sourced this run:
nonfarm payrolls <b>+58,000</b>, the unemployment rate holding at <b>4.1%</b>, and average hourly earnings
<b>+3.1% year over year</b>. It is the first major read on the labour market since Warsh's Jackson Hole
warning, and the week's largest scheduled risk.</li>
<li><b>Next week's other U.S. releases:</b> <b>ISM Manufacturing</b> and <b>ISM Services</b> surveys, the
<b>JOLTS</b> report and the <b>ADP</b> employment reading all land before Friday, alongside Eurozone flash CPI
and a Bank of Canada rate decision. <b>Monday, August 31 is quiet</b> &mdash; no major U.S. economic report is
scheduled &mdash; but the tape reopens that morning.</li>
<li><b>Earnings still to come:</b> <b>Broadcom</b>, <b>Dell Technologies</b>, <b>lululemon athletica</b>,
<b>Palo Alto Networks</b> and <b>Zscaler</b> all report next week. Three of the five are read directly against
the AI-infrastructure trade that drove this week's tape.</li>""",
  "ws radar", 1)

w = sub(w,
  """<a href="https://us.econoday.com/">Econoday &mdash; 2026 economic calendar</a><br>""",
  """<a href="https://www.forbes.com/sites/fionariley/2026/08/28/paypal-plunges-15-after-reports-that-advent-stripe-abandon-53-billion-bid/">Forbes &mdash; PayPal plunges after reports that Advent and Stripe abandon $53 billion bid</a><br><a href="https://www.schaeffersresearch.com/content/news/2026/08/27/the-week-ahead-august-jobs-report-takes-center-stage">Schaeffer's Research &mdash; The week ahead: August jobs report takes center stage</a><br><a href="https://www.theglobeandmail.com/investing/markets/inside-the-market/article-calendar-what-investors-need-to-know-for-the-week-ahead-155/">The Globe and Mail &mdash; Calendar: what investors need to know for the week ahead</a><br><a href="https://us.econoday.com/">Econoday &mdash; 2026 economic calendar</a><br>""",
  "ws sources", 1)

wr("wallstreet-briefing.html", w)

# ---------------------------------------------------------------- INDEX
i = rd("index.html")
i = sub(i,
  "<p>The federal deadline to remediate an actively exploited Citrix NetScaler flaw expires today, and PaperCut has shipped a <b>second</b> emergency patch after attackers bypassed the first &mdash; two internet-facing products under live exploitation with the clock already run out on one of them.</p>",
  "<p>" + CY_TLDR + "</p>", "index cyber card", 1)
i = sub(i,
  "<p>Markets are closed for the weekend, so Friday&rsquo;s official closes stand &mdash; the S&amp;P 500 slipped 0.25% to 7,711.76 and still finished the week higher &mdash; while the weekend&rsquo;s live story is Stripe and Advent walking away from a $50 billion-plus pursuit of PayPal.</p>",
  "<p>" + WS_TLDR + "</p>", "index ws card", 1)
i = sub(i,
  "<p>UFC Shanghai is running live as this edition publishes &mdash; all seven prelims and four main-card bouts are decided, six of the eleven by finish, but neither the Yan Xiaonan co-main nor the Nurmagomedov&ndash;Song headliner had been resulted by any source seen this run.</p>",
  "<p>" + MMA_TLDR + "</p>", "index mma card", 1)
i = sub(i,
  "this edition records a Citrix build-number discrepancy, a set of unverified leak-site listings, and two live UFC bouts that had no result yet, each labelled as such rather than filled in.",
  "this edition records a Citrix build-number discrepancy, a set of unverified leak-site listings, two conflicting reads of one PayPal share move, a submission described two different ways, and a UFC main event that had no result yet &mdash; each labelled as such rather than filled in.",
  "index note", 1)
wr("index.html", i)

# ---------------------------------------------------------------- stamps
for p in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"):
    s = rd(p)
    n = s.count(OLD)
    s = s.replace(OLD, STAMP)
    wr(p, s)
    print("stamp %-26s %d replacements -> %s" % (p, n, STAMP))

if fails:
    print("\nEDIT FAILURES:")
    for f in fails:
        print("  " + f)
    sys.exit(1)
print("\nAll edits applied cleanly at %s ET." % STAMP)
