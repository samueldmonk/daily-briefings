#!/usr/bin/env python3
# Daily briefings -- 2026-08-30 ~6:45 PM ET edition. Targeted content edits.
import re, sys, io

REPO = sys.argv[1]

def rd(f): return io.open(REPO+'/'+f, encoding='utf-8').read()
def wr(f, s): io.open(REPO+'/'+f, 'w', encoding='utf-8').write(s)

def sub1(h, old, new, label):
    assert h.count(old) >= 1, 'MISSING ANCHOR: ' + label
    return h.replace(old, new, 1)

# ---------------------------------------------------------------- TLDRs
TLDR_CY = (
 '<b>The Questel listing this page published as fresh is wrong three ways, and one search corrected all three:</b> '
 'the company is <b>Questel SAS</b> (this page spelled it &ldquo;Questal&rdquo;), a Paris provider of '
 '<b>intellectual-property, innovation-management and legal software</b> rather than a generic IT provider; the listing is '
 '<b>dated August 2 with an August 4 deadline</b> &mdash; four weeks old, from the same ShinyHunters batch as '
 '<b>Alcon</b> and <b>Lumenis</b>, not a fresh weekend entry; and it is <b>no longer unconfirmed</b>, because '
 '<b>Questel has confirmed unauthorised access to part of its Microsoft 365 environment after a voice-phishing attack</b> '
 'and that some of the data was published. &#9888; <b>But the confirmation does not confirm the claim:</b> ShinyHunters '
 'calls the haul <b>Salesforce records</b>; Questel says the access it confirmed was to a <b>Sales SharePoint environment '
 'in Microsoft 365</b> &mdash; so the volumes stay the attacker&rsquo;s (<b>21 million records, 147 GB claimed, an archive '
 'advertised at <i>over 134 GB compressed</i></b>) and only the intrusion is the company&rsquo;s. '
 'The two deadlines that expire today, <b>ownCloud</b> and the <b>Linux kernel</b>, are unchanged at a '
 '<b>nineteenth catalogue check</b>.'
)

TLDR_WS = (
 '<b>The first item on this page that postdates Friday&rsquo;s close is not a price but a strike:</b> the '
 '<b>U.S. military hit Iranian rocket launchers preparing to send mines into the Strait of Hormuz</b> on Sunday, and '
 '<b>global benchmark crude gained 2% at the open</b> while <b>S&amp;P 500 futures edged lower</b> &mdash; the week&rsquo;s '
 'equity numbers are settled and the risk attached to them is not. Friday&rsquo;s closes stand for a '
 '<b>twenty-ninth verification</b> (<b>S&amp;P 500 7,711.76 &minus;0.25%</b>, <b>Nasdaq Composite 26,402.42 &minus;0.52%</b>, '
 '<b>Dow 53,559.99 &minus;0.02%</b>); the Nasdaq&rsquo;s weekly gain came back this run as <b>+0.9%</b> against the '
 '<b>+0.8% / +221.97</b> carried, and <b>the carried form is kept because only it reconciles arithmetically</b>. '
 'The week ahead finally has dates rather than adjectives: <b>Broadcom reports Wednesday after the close</b> and the '
 '<b>August jobs report lands Friday at 8:30 AM ET</b>.'
)

TLDR_MM = (
 '<b>The cross-check that has settled this page&rsquo;s champions board twelve times returned stale cells on the '
 'thirteenth.</b> ESPN&rsquo;s list matched on all <b>six men&rsquo;s divisions it covered</b> &mdash; Aspinall, Ulberg, '
 'Strickland, Makhachev, Gaethje, Volkanovski &mdash; but the same return carried <b>bantamweight as Merab Dvalishvili</b> '
 'and <b>flyweight as Alexandre Pantoja</b>, both superseded at <b>UFC 323 on December 6, 2025</b>. '
 '&#9888; <b>Both were refuted inside this same run</b>, by the UFC 331 preview calling Pantoja a <b>former champion</b> and '
 '<b>Joshua Van</b> the current one, and by <b>Petr Yan&rsquo;s booked October 24 defence</b> against Dvalishvili at UFC 333. '
 'The board is unchanged for a <b>seventieth consecutive edition</b>, and the rule tightens: <b>an authoritative source is '
 'authoritative per cell, not per return</b>. Separately Paris fills in completely &mdash; <b>Accor Arena, September 5, '
 'UFC Fight Night 287, billed by the promotion as <i>Hooker vs. Parnasse</i></b> in that order &mdash; and BetWay&rsquo;s '
 'missing side arrives at <b>Hooker +300</b>.'
)

# ---------------------------------------------------------------- CYBER
h = rd('cyber-briefing.html')

h = re.sub(r'(<div class="tldr"><b>The Wire</b> <span>).*?(</span></div>)',
           lambda m: m.group(1) + TLDR_CY + m.group(2), h, count=1, flags=re.S)

# Global spelling correction, then a note explaining it.
n_questal = h.count('Questal')
h = h.replace('Questal', 'Questel')

CY_TOP = (
 '<div class="note" style="margin-bottom:14px"><span class="tag crit">Corrected &middot; 6:45 PM</span> '
 '<b>The lead extortion listing on this page was wrong in three separate ways, and every correction came out of one '
 'search.</b> This page has carried, since 6:10 PM, a &ldquo;fresh&rdquo; ShinyHunters listing against <b>&ldquo;Questal&rdquo;</b>, '
 'described as a <b>Paris IT provider</b>, with the standing caveat that <b>no company named had confirmed anything</b>. '
 'All three of those are now corrected against dedicated reporting fetched this run.<br><br>'
 '<b>(1) The name.</b> It is <b>Questel SAS</b> &mdash; a Paris-based provider of <b>intellectual-property, '
 'innovation-management and legal software and services</b>, which is a more specific business than &ldquo;IT provider&rdquo;. '
 'The misspelling appeared in <b>' + str(n_questal) + '</b> places on this page and has been replaced throughout. '
 'The standing rule this violated is the project&rsquo;s oldest: <b>names are copied exactly as the sources spell them, '
 'never reconstructed</b>.<br><br>'
 '<b>(2) The date.</b> The listing is <b>dated August 2</b> and set an <b>August 4</b> deadline for the company to open '
 'negotiations. It is <b>four weeks old</b>, and it reached this page through an aggregator&rsquo;s &ldquo;August 2026&rdquo; '
 'roll-up, which is accurate as a month and misleading as a day. &#9888; <b>Same failure class as the Nevada item this page '
 'has refused eleven times</b> &mdash; a correctly-dated-by-month listing read as a new event &mdash; and this time it was '
 'this page that made it, not a source. The same batch named <b>Alcon Inc.</b> (Swiss; <b>25 million-plus Salesforce records '
 'claimed</b>, same August 2 listing and August 4 deadline, <b>no confirmation or regulatory filing from Alcon</b> as of the '
 'reporting) and <b>Lumenis</b>.<br><br>'
 '<b>(3) The confirmation &mdash; and it is the part that changes the entry&rsquo;s standing rather than its accuracy.</b> '
 'Questel <b>has confirmed</b> that attackers gained <b>unauthorised access to part of its Microsoft 365 environment '
 'following a voice-phishing attack</b>, and that <b>some of the stolen data was subsequently published online</b>. '
 'This page said no company named had confirmed anything; one of them has.<br><br>'
 '&#9888; <b>And yet the confirmation does not confirm the claim, which is why the figures below are unchanged.</b> '
 'ShinyHunters describes the stolen material as <b>Salesforce records</b>. Questel says the unauthorised access it confirmed '
 'involved a <b>Sales SharePoint environment in Microsoft 365</b> &mdash; a different system, and a name close enough to '
 '&ldquo;Salesforce&rdquo; that the divergence is worth stating rather than smoothing. <b>Questel has not confirmed the '
 'attacker&rsquo;s claims in full</b>, so <b>21 million records</b> and <b>147 GB</b> remain the attacker&rsquo;s numbers and are '
 'still printed as such. New figure, same footing: the listing advertises a downloadable archive of '
 '<b>more than 134 GB compressed</b>, and the reporting notes plainly that <b>extortion claims routinely inflate volumes</b>.'
 '<br><br><b>What this does and does not do to the McKesson story at the top of this page.</b> Questel&rsquo;s confirmed '
 'vector is <b>vishing</b>, which is the McKesson vector. That is now a <b>company-confirmed</b> instance of the technique '
 'rather than an attacker&rsquo;s assertion of it. &#9888; It is still <b>not</b> evidence the two are one campaign, and the '
 'flag stays a flag: <b>a shared technique is the weakest kind of link, and a claim that fits the pattern remains the '
 'easiest claim to make</b>.</div>'
)
h = sub1(h, '<h2 class="sec">Top Story</h2>', '<h2 class="sec">Top Story</h2>' + CY_TOP, 'cyber top story')

CY_BREACH = (
 '<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 6:45 PM</span> '
 '<b>Five more names off the leak sites, and they are printed at the weight of listings.</b> A ransomware round-up fetched '
 'this run adds <b>Southeastern Oklahoma State University</b> (<b>InterLock</b>, dated <b>August 19</b>), '
 '<b>Roadvision Systems</b> of Hanover, New Hampshire (<b>August 18</b>), <b>Motorenmaier GmbH</b> of Germany '
 '(<b>Qilin</b>, confirmed <b>August 16</b>), <b>Babcock Africa</b>, an engineering and asset-management firm '
 '(<b>thegentlemen</b>), and <b>Alcon Inc.</b> (<b>ShinyHunters</b>, <b>25 million-plus Salesforce records</b> claimed). '
 '&#9888; <b>Every one of these is a leak-site entry, not a disclosure</b> &mdash; no statement from any of the five named '
 'organisations was returned by anything fetched this run, and the Alcon claim in particular is <b>four weeks old</b> and '
 'still uncorroborated by the company. <b>No victim counts, data categories or ransom figures are printed for any of them.</b> '
 'They are here because a leak-site census is a useful shape even when every individual entry is unproven &mdash; but a '
 'census of claims is what it is, and this page has now been caught once this weekend treating one as newer than it was.'
 '</div>'
)
h = sub1(h, '<h2 class="sec">Breaches &amp; Incidents</h2>',
         '<h2 class="sec">Breaches &amp; Incidents</h2>' + CY_BREACH, 'cyber breaches')

CY_VULN = (
 '<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 6:45 PM</span> '
 '<b>The ServiceNow entry gains the one line that tells a reader whether they have work to do.</b> Reporting fetched this '
 'run re-confirms all three flaws at <b>CVSS 10.0</b> and unauthenticated, adds that ServiceNow rated all three at '
 '<b>low attack complexity</b>, and &mdash; the operative part &mdash; states that customers enrolled in ServiceNow&rsquo;s '
 '<b>Patching Program received the updates automatically on hosted instances</b>, while <b>self-hosted customers must apply '
 'them themselves</b>. Three maximum-severity unauthenticated flaws where most of the fleet is already patched and a '
 'self-hosted minority is not is a very different operational picture from three unpatched 10.0s, and this page had not '
 'drawn that line before. Component detail also firms up: <b>CVE-2026-18885</b> is code injection in the '
 '<b>GraphQL Composite Data API</b>, <b>CVE-2026-18886</b> is improper access control in the <b>system configuration image '
 'upload processor</b> (unauthenticated create/modify &rarr; privilege escalation), and <b>CVE-2026-74820</b> is SQL '
 'injection in the <b>ServiceNow AI Platform</b>. &#9888; <b>The fourth identifier is still not adopted</b>, but the '
 'evidence for a four-record advisory strengthens: this run&rsquo;s source says ServiceNow stated it is not aware of '
 'exploitation <b>in each of the four records</b> &mdash; which confirms there are four, and still does not settle whether '
 'the fourth is CVE-2026-6875 or CVE-2026-6876. <b>A count is not an identifier</b>, so the row stays out of the table.'
 '</div>'
)
h = sub1(h, '<h2 class="sec">Vulnerability Watch</h2>',
         '<h2 class="sec">Vulnerability Watch</h2>' + CY_VULN, 'cyber vuln watch')

# New CVE row -- inserted immediately before the 62878 row.
ROW = ('<tr><td><code>CVE-2026-62893</code></td><td>9.8</td><td>Windows Deployment Services</td>'
       '<td><span class="tag new">New &middot; 6:45 PM</span> <b>Critical remote code execution</b>, reported this run at '
       '<b>CVSS 9.8</b>. This is the <b>second of the four unauthenticated, network-reachable 9.8 RCE flaws</b> in the '
       'August Patch Tuesday release to be named on this page &mdash; the row below, Windows DNS Server, was the first. '
       'The same source also names <b>CVE-2026-62818</b>, a critical RCE in <b>Windows Active Directory Certificate '
       'Services</b> at <b>CVSS 8.8</b>, which is <b>not</b> in the 9.8 group and is recorded here rather than given a row '
       'of its own. &#9888; <b>Not exploited and not KEV-listed</b> on anything fetched this run; it is on the board for '
       'severity and reachability. The only flaw in that release confirmed under exploitation remains '
       '<b>CVE-2026-68820</b>.</td></tr>\n')
h = sub1(h, '<tr><td><code>CVE-2026-62878</code></td>', ROW + '<tr><td><code>CVE-2026-62878</code></td>', 'cve row')

CY_KEV = (
 '<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 6:45 PM</span> '
 '<b>A nineteenth check, and the board did not move on the last run of the day.</b> The sweep returned CISA&rsquo;s own '
 'dated alert pages for <b>August 11</b> (three: CVE-2026-20349 Cisco Secure Firewall ASA/FTD, CVE-2026-68820 Windows '
 'afd.sys, CVE-2026-72898 Metabase), <b>August 18</b> (four: CVE-2026-33824 Microsoft IKE, CVE-2026-55040 SharePoint, '
 'CVE-2026-59310 Broadcom VMware vCenter, CVE-2026-65400 Apple macOS, with a stated federal deadline of <b>August 21</b>) '
 'and <b>August 20</b> (two: CVE-2026-72529 and CVE-2026-72530, TrueConf Server) &mdash; every identifier matching the rows '
 'below. <b>Nothing dated later than August 27 for a thirteenth consecutive check.</b> The two rows due today were re-read '
 'against the clock: it is still <b>Sunday, August 30</b>, so <b>CVE-2023-49105</b> (ownCloud) and <b>CVE-2026-53362</b> '
 '(Linux kernel) remain <b>due today at 0 days left</b>, and the Citrix / SQL Server pair and the Oracle proxy plug-in row '
 'remain <b>overdue</b>. &#9888; <b>Nothing new was added to this board on the strength of the August round-ups fetched this '
 'run</b>: those name CVEs by severity, not by catalogue entry, and this page still publishes KEV rows only from CISA&rsquo;s '
 'own dated alert pages. It still certifies no August total of its own.</div>'
)
h = sub1(h, '<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>',
         '<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>' + CY_KEV, 'cyber kev')

wr('cyber-briefing.html', h)
print('cyber ok; Questal->Questel replacements:', n_questal)

# ---------------------------------------------------------------- MARKETS
h = rd('wallstreet-briefing.html')
h = re.sub(r'(<div class="tldr"><b>The Tape</b> <span>).*?(</span></div>)',
           lambda m: m.group(1) + TLDR_WS + m.group(2), h, count=1, flags=re.S)

WS_LEAD = (
 '<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 6:45 PM</span> '
 '<b>Something happened after Friday&rsquo;s close, and for the first time this weekend it is not a revision to a number '
 'already on this page.</b> A live markets file dated today reports that the <b>U.S. military struck Iranian rocket '
 'launchers on Sunday</b> that were <b>preparing to send mines into the Strait of Hormuz</b>, and that '
 '<b>global benchmark crude gained 2% at the open</b> of the new week&rsquo;s trading. The same file has '
 '<b>S&amp;P 500 futures edging lower</b> after the cash index closed down on Friday, and the dollar trading in a narrow '
 'range after its biggest gain in about a month.<br><br>'
 '<b>Why this belongs at the top of a page whose every other figure is Friday&rsquo;s.</b> The rate story this page has '
 'carried all weekend runs through energy: the reason a September hike repriced from the thirties to the fifties is an '
 'inflation print that sources attribute substantially to fuel, and <b>Treasury yields have tracked oil since the U.S. '
 'first struck Iran</b>. A 2% move in crude before Monday&rsquo;s equity open is therefore an input to the '
 '<b>September 16 FOMC</b> question and not merely a commodity headline.<br><br>'
 '&#9888; <b>Three things are deliberately withheld.</b> First, <b>no new WTI or Brent level is published</b>: the source '
 'gives a percentage at the open, and this page does not multiply Friday&rsquo;s <b>$83.44</b> WTI or <b>$88.29</b> Brent by '
 'it and print the product as a quote. Second, <b>futures are not the cash index</b> &mdash; two Dow futures figures were '
 'returned (<b>53,584.00</b> current against <b>53,608.00</b> at the open) from an undated quote page, and they are '
 '<b>recorded here and not promoted</b> into the Weekly Scorecard, which holds official closes only. Third, the direction '
 'itself is a <b>Sunday-evening</b> reading of a market that trades until Friday; it is <b>not a forecast of Monday&rsquo;s '
 'open</b>, and this page has spent the weekend declining to turn descriptions into forecasts.</div>'
)
h = sub1(h, '<h2 class="sec">The Lead</h2>', '<h2 class="sec">The Lead</h2>' + WS_LEAD, 'ws lead')

WS_RATES = (
 '<div class="note" style="margin-bottom:14px"><span class="tag warn">Recorded, not promoted &middot; 6:45 PM</span> '
 '<b>A full curve snapshot arrived this run and none of it goes into the table above, for one reason: it is undated.</b> '
 'A rates round-up fetched this run gives the <b>10-year at 4.72%</b>, the <b>30-year at 5.21%</b>, the <b>2-year at '
 '4.36%</b>, the <b>5-year at 4.49%</b>, the <b>1-year at 4.13%</b> and the <b>3-month bill at 3.83%</b> &mdash; all '
 'qualified only as <b>&ldquo;as of late August&rdquo;</b>. Every one of the three that overlap this table is '
 '<b>slightly above</b> what the table carries from dated sources (<b>4.73%</b> close, <b>5.20%</b>, <b>4.34%</b>), and '
 '<b>4.72% is now refused for the sixth time</b> on exactly the ground established at 2:39 PM: a dedicated August 28 '
 'yields snapshot states the 10-year <b>finished</b> at 4.73%, and an undated round-up&rsquo;s figure does not displace a '
 'stated close. &#9888; <b>The three genuinely new points &mdash; the 5-year, 1-year and 3-month &mdash; are printed here '
 'rather than added as rows</b>, because a row in that table asserts an as-of date and this source supplies none. '
 '<b>An undated number is not a wrong number; it is a number that cannot be placed on a timeline</b>, and this table is a '
 'timeline.<br><br><b>The policy read gains one corroboration and one contradiction, and both are printed.</b> '
 'Corroboration: a second source states independently that hike bets for September <b>spiked to 57%</b> after Warsh&rsquo;s '
 'remarks &mdash; the same figure this page attributed to CME FedWatch at 2:39 PM, now stated by a source that does not '
 'name the venue. Contradiction: the same undated round-up says markets are pricing <b>around a 65% chance the Fed holds '
 'in September</b>, which is the opposite conclusion. &#9888; <b>The contradiction is refused on the same ground as the '
 'yields &mdash; it is undated</b>, and a September probability that cannot be placed before or after the Jackson Hole '
 'speech is not comparable to one that can. Its December figure is recorded instead: the round-up puts the probability of '
 'a hike <b>by December above 70%</b>, which joins rather than settles the contested December readings this page already '
 'carries.</div>'
)
h = sub1(h, '<h2 class="sec">Rates, Bonds &amp; Commodities</h2>',
         '<h2 class="sec">Rates, Bonds &amp; Commodities</h2>' + WS_RATES, 'ws rates')

WS_RADAR = (
 '<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 6:45 PM</span> '
 '<b>The week ahead stops being a list of themes and becomes a list of dates.</b> This page has named Broadcom, the August '
 'employment data and a pre-decision inflation print as the week&rsquo;s three events without being able to date any of '
 'them. Two now have dates from primary-grade sources.<br><br>'
 '<b>Broadcom (AVGO) reports third-quarter fiscal 2026 results on Wednesday, September 2, after the market close</b>, with '
 'the call at <b>2:00 PM Pacific / 5:00 PM ET</b>. &#9888; <b>One source returned September 3 instead</b>; the September 2 '
 'date is taken because it comes from the company&rsquo;s own earnings-date announcement and the conflicting return is a '
 'third-party calendar. <b>Both are recorded</b>, per this page&rsquo;s practice of printing the conflict rather than the '
 'winner alone. Why it matters here rather than on a corporate page: this briefing carries, as attribution, Broadcom&rsquo;s '
 'own guidance of <b>a major acceleration in AI semiconductor revenue for the second half of fiscal 2026</b> &mdash; against '
 'a week in which semiconductors <b>lagged</b>. Wednesday is when those two things are reconciled or they are not.<br><br>'
 '<b>The August employment report is released Friday, September 4, at 8:30 AM ET</b> &mdash; the first Friday of the month, '
 'on the Bureau of Labor Statistics&rsquo; standard schedule. It is the <b>last major labour reading before the September 16 '
 'FOMC</b>, and on a page whose central question all weekend has been whether the Fed hikes, it is the single dated event '
 'with the most capacity to move that answer. <b>Labor Day falls Monday, September 7</b>, after both &mdash; so the week is '
 'a full five sessions and the holiday does not truncate it.</div>'
)
h = sub1(h, '<h2 class="sec" id="radar">On the Radar</h2>',
         '<h2 class="sec" id="radar">On the Radar</h2>' + WS_RADAR, 'ws radar')

wr('wallstreet-briefing.html', h)
print('markets ok')

# ---------------------------------------------------------------- MMA
h = rd('mma-briefing.html')
h = re.sub(r'(<div class="tldr"><b>Tale of the Tape</b> <span>).*?(</span></div>)',
           lambda m: m.group(1) + TLDR_MM + m.group(2), h, count=1, flags=re.S)

MM_WEEK = (
 '<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 6:45 PM</span> '
 '<b>Paris stops being a headliner and an odds argument and becomes a card.</b> Every detail below is new to this page.<br><br>'
 '<b>Sat, Sep 5 &middot; Accor Arena, Paris, France &middot; UFC Fight Night 287.</b> The promotion bills it '
 '<b>&ldquo;UFC Fight Night: Hooker vs. Parnasse&rdquo;</b> &mdash; and the order is worth noticing, because this page has '
 'been rendering it <b>Parnasse vs. Hooker</b> all weekend on the strength of the betting line. <b>The promotion puts the '
 'underdog first.</b> Dan Hooker is the established lightweight and the returning name; <b>Salahdine Parnasse is a '
 'promotional newcomer</b> who is nonetheless the price favourite. <b>Billing follows standing, and the line follows '
 'expectation, and here they point opposite ways</b> &mdash; which is the plainest available explanation for a spread this '
 'page has called unusually wide three times. It is the promotion&rsquo;s <b>fifth consecutive annual visit to Paris</b>.'
 '<br><br><b>Broadcast:</b> Paramount+, <b>prelims 12 PM ET, main card 3 PM ET</b> &mdash; an early-afternoon U.S. window '
 'set by Paris time, the same pattern as UFC 333 in Abu Dhabi.<br><br>'
 '<b>Co-main:</b> <b>Far&egrave;s Ziam vs. Axel Sola</b>, an all-French lightweight bout. Also listed: '
 '<b>Michael Page vs. Nursulton Ruziboev</b> (185 lbs), <b>Losene Keita vs. Muhammad Naimov</b> (145 lbs), '
 '<b>Mario Pinto vs. Ryan Spann</b> (265 lbs) and <b>Oumar Sy vs. Modestas Bukauskas</b> (205 lbs), with UFC debuts for '
 '<b>Matthieu Duclos</b> and <b>Delphine Benouaich</b>.<br><br>'
 '<b>Odds &mdash; the missing half of a pair arrives.</b> This page has carried BetWay&rsquo;s <b>Parnasse &minus;400</b> '
 'without the other side of it. It is <b>Hooker +300</b>. The UFC&rsquo;s own listing is re-confirmed at '
 '<b>Hooker +375 / Parnasse &minus;500</b>. &#9888; <b>Both quotes are internally coherent pairs, which is exactly what the '
 'listing refused at 5:48 PM was not</b> &mdash; that one carried the UFC&rsquo;s numbers with the fighters swapped. '
 'Parnasse is described as a <b>two-time KSW featherweight and one-time KSW lightweight champion</b> making his UFC debut, '
 'which is the first thing this page has been able to say about <i>why</i> a debutant prices at &minus;400.<br><br>'
 '&#9888; <b>The event-name problem returns, and this time it resolves rather than multiplying.</b> Two renderings came '
 'back &mdash; <b>&ldquo;UFC Fight Night: Hooker vs. Parnasse&rdquo;</b> and <b>&ldquo;UFC Fight Night 287&rdquo;</b> &mdash; '
 'but unlike the September 26 card, sources fetched this run <b>state both forms for the same September 5 event</b>, so they '
 'are printed together rather than kept apart. <b>The September 26 card&rsquo;s three names stay unreconciled</b>, because '
 'nothing fetched equates those.</div>'
 '<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 6:45 PM</span> '
 '<b>The rest of September, and UFC 331 fills out.</b> <b>Sat, Sep 12: Noche UFC &mdash; Rodriguez vs. Silva</b>, main card '
 '<b>2:00 PM ET</b>. <b>Sat, Sep 19: UFC 331 &mdash; Van vs. Pantoja 2</b>, now placed at the <b>Crypto.com Arena, Los '
 'Angeles</b>, with <b>early prelims about 5 PM ET, prelims 7 PM ET and the main card 9 PM ET</b> on Paramount+. The card '
 'adds <b>Renato Moicano vs. Brian Ortega 2</b>, <b>Patricio Pitbull vs. Doo Ho Choi</b> and '
 '<b>Charles Jourdain vs. Marlon Vera</b> to the Tsarukyan&ndash;Ruffy co-main already carried. &#9888; New detail on the '
 'first meeting, and it is the kind that changes how a rematch reads: <b>Van won the belt at UFC 323 by technical knockout '
 '26 seconds into round one, as a result of an arm injury Pantoja sustained</b>. A twenty-six-second title change on an '
 'injury is the weakest possible basis for a prediction, which is consistent with the two books this page carries opening '
 'the rematch on <b>opposite sides of pick-em</b>.</div>'
)
h = sub1(h, '<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>',
         '<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>' + MM_WEEK, 'mma fight week')

MM_RES = (
 '<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 6:45 PM</span> '
 '<b>The Shanghai bonus pool is bigger than this page has been reporting, and the shape of it is unusual.</b> '
 'A bonus report fetched this run states that alongside the four <b>$100,000</b> awards already carried &mdash; '
 '<b>Song Yadong</b> and <b>Bilal Hasan</b> on Performance, <b>Liu Ce</b> and <b>Levi Rodrigues Jr.</b> sharing Fight of '
 'the Night &mdash; <b>five further $25,000 bonuses</b> went to <b>Hector Santiago</b>, <b>Francesco Nuzzi</b>, '
 '<b>Rei Tsuruya</b>, <b>Kai Asakura</b> and <b>Denise Gomes</b>. That is <b>$400,000 plus $125,000 = $525,000</b>, and the '
 'arithmetic is this page&rsquo;s own, stated so rather than attributed. &#9888; <b>The $25,000 tier is stated by a single '
 'source</b> and by no other return this run, so it is printed as that report&rsquo;s claim; the four $100,000 awards, which '
 'five runs have now confirmed, are not affected either way. Three of the five names &mdash; Santiago, Nuzzi and Gomes &mdash; '
 'are already on this page&rsquo;s results and debut lines, which is a consistency check the entry passes.<br><br>'
 '<b>And the card&rsquo;s finish rate gets a second, independently worded source.</b> This page has carried '
 '<b>ten of thirteen bouts ending inside the distance</b> from post-event results. A separate write-up this run describes the '
 'night as having <b>ten finishes</b>. <b>Two differently-phrased sources arriving at the same count is the cheapest '
 'corroboration available and this page takes it</b>, because the figure was previously resting on one reading of a results '
 'listing.</div>'
)
h = sub1(h, '<h2 class="sec">UFC Shanghai &mdash; Results</h2>',
         '<h2 class="sec">UFC Shanghai &mdash; Results</h2>' + MM_RES, 'mma results')

MM_CHAMP = (
 '<div class="note" style="margin-bottom:14px"><span class="tag crit">Cross-check &middot; 6:45 PM</span> '
 '<b>Thirteenth ESPN cross-check, and it is the first one that returned wrong cells &mdash; which makes it the most useful '
 'check this board has run.</b><br><br>'
 '<b>What matched.</b> ESPN&rsquo;s current-champions listing returned <b>six men&rsquo;s divisions</b> with title dates '
 'matching this board exactly: <b>Tom Aspinall</b> (heavyweight, June 21 2025), <b>Carlos Ulberg</b> (light heavyweight, '
 'April 11 2026, KO1 Proch&aacute;zka at UFC 327), <b>Sean Strickland</b> (middleweight, May 9 2026, split decision over '
 'Chimaev at UFC 328), <b>Islam Makhachev</b> (welterweight, November 15 2025, one defence), <b>Justin Gaethje</b> '
 '(lightweight, June 14 2026, TKO4 Topuria at Freedom 250) and <b>Alexander Volkanovski</b> (featherweight, April 12 2025, '
 'one defence). Six cells, six matches.<br><br>'
 '&#9888; <b>What did not match, and why the board did not move.</b> The same return carried '
 '<b>bantamweight as Merab Dvalishvili</b> (September 14 2024, three defences) and <b>flyweight as Alexandre Pantoja</b> '
 '(July 8 2023, four defences). <b>Both are superseded, and both were superseded on the same night</b> &mdash; '
 '<b>UFC 323, December 6, 2025</b>, where Petr Yan took the bantamweight title from Dvalishvili by unanimous decision and '
 'Joshua Van took the flyweight title from Pantoja by first-round technical knockout.<br><br>'
 '<b>The refutation came from inside this same run, twice, and neither source was looking for it.</b> The '
 '<b>UFC 331 preview</b> describes the September 19 main event as a flyweight title rematch between '
 '<b>&ldquo;current champion Joshua Van&rdquo;</b> and <b>&ldquo;former champion Alexandre Pantoja&rdquo;</b> &mdash; a '
 'promotion-grade statement of exactly the cell in dispute. And a separate search returns <b>Petr Yan defending the '
 'bantamweight title against Dvalishvili at UFC 333 on October 24</b>, in a trilogy bout, having taken the belt at UFC 323. '
 '<b>A champion with a booked defence is not a former champion, and a fighter the promotion calls a former champion is not '
 'the current one.</b><br><br>'
 '<b>The rule this tightens.</b> Twelve previous runs treated an ESPN return as authoritative for whatever it contained. '
 'This one shows a single return can be <b>current in six cells and stale in two</b>, with nothing in the return marking the '
 'difference. So: <b>an authoritative source is authoritative per cell, not per return</b>, and a cell only counts as '
 'checked when the check is <b>later than the event that could have changed it</b>. <b>Board unchanged &mdash; seventieth '
 'consecutive edition.</b> The three cells ESPN did not cover this run &mdash; women&rsquo;s strawweight, and the interim '
 'heavyweight and women&rsquo;s flyweight notes &mdash; rest on the checks recorded beneath, as they have.</div>'
)
h = sub1(h, 'Champions Board</h2>', 'Champions Board</h2>' + MM_CHAMP, 'mma champions')

wr('mma-briefing.html', h)
print('mma ok')
