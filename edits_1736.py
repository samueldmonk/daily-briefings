#!/usr/bin/env python3
"""Incremental edits for the 5:36 PM ET Afternoon Edition, Aug 26 2026.
Every replacement asserts its anchor exists exactly once."""
import io, sys, os

O = os.path.dirname(os.path.abspath(__file__))
fails = []

def rd(n):
    return io.open(os.path.join(O, n), encoding='utf-8').read()

def wr(n, s):
    io.open(os.path.join(O, n), 'w', encoding='utf-8').write(s)

def rep(h, old, new, label, count=1):
    n = h.count(old)
    if n != count:
        fails.append("%s: anchor found %d times, expected %d" % (label, n, count))
        return h
    return h.replace(old, new)

# ============================ WALL STREET =================================
w = rd('wallstreet-briefing.html')

# --- 1. ticker tape: feature tonight's actual movers, keep the five mandatory
w = rep(w,
  '{"proName":"NYSE:ANF","title":"Abercrombie"},{"proName":"NASDAQ:OKTA","title":"Okta"}',
  '{"proName":"NASDAQ:OKTA","title":"Okta"},{"proName":"NYSE:HPQ","title":"HP Inc"},'
  '{"proName":"NASDAQ:SNPS","title":"Synopsys"}',
  'tape symbols')

# --- 2. THE LEAD
w = rep(w, '<h2>Software takes the night that Nvidia was supposed to own</h2>',
  '<h2>Nvidia finally has an after-hours number &mdash; and it is HP, not Nvidia, taking the night&rsquo;s worst punishment</h2>',
  'lead h2')

OLD_LEAD = ('<p><b>&#9679; New &middot; 5:06 &mdash; every name that mattered tonight now has a price, '
            'and the biggest one is the only red.</b>')
NEW_LEAD = (
 '<p><b>&#9679; New &middot; 5:36 &mdash; a full after-hours roundup lands, and it does three things at once: '
 'it puts the first magnitude on Nvidia, it adds three names this page had not seen, and it disagrees '
 'with every earlier percentage on this list.</b> <b>Investing.com&rsquo;s after-hours movers wrap, fetched in full '
 'this run, prices the night as: Okta &plus;17%, Salesforce &plus;12%, CrowdStrike &plus;10%, Nutanix &plus;5%, '
 'Nvidia &minus;1%, Synopsys &minus;6% and HP Inc &minus;11%.</b> <b>&#9888; Those are LATER READS OF A MOVING TAPE, '
 'not corrections</b> &mdash; the 4:36&ndash;5:06 figures from CNBC, Quartz and Yahoo (<b>Okta ~&plus;15%, Salesforce '
 '&plus;14%, CrowdStrike as much as &plus;12%</b>) are kept below with their own timestamps, and <b>nothing is merged '
 'into a single number.</b> <b>The night&rsquo;s biggest loser is not Nvidia but HP Inc, down about 11% despite '
 'beating on both lines</b>, on soft fourth-quarter margin guidance and rising component costs, memory above all. '
 '<b>&#9679; Nvidia now has a sourced after-hours magnitude for the first time today: down about 1%</b> '
 '(Investing.com), with a second read of <b>&minus;1.3% roughly half an hour before the call</b> (Kiplinger&rsquo;s '
 'live blog) &mdash; <b>both printed, neither adopted as the figure.</b> '
 '<b>&#9888; Note the size of the disappointment being expressed: Nvidia beat on both lines and guided the current '
 'quarter entirely above consensus, and still went down.</b> The earlier framing stands:')
w = rep(w, OLD_LEAD, NEW_LEAD, 'lead para open')

# --- 3. TLDR
old = w[w.find('<div class="tldr"><b>The Tape</b>'):]
old = old[:old.find('</div>') + 6]
if old.count('The Tape') != 1:
    fails.append('ws tldr: could not isolate')
else:
    new = ('<div class="tldr"><b>The Tape</b> <span>A full after-hours roundup fetched at <b>5:36</b> prices the night as '
           '<b>Okta &plus;17%, Salesforce &plus;12%, CrowdStrike &plus;10%, Nutanix &plus;5%, Nvidia &minus;1%, '
           'Synopsys &minus;6% and HP Inc &minus;11%</b> &mdash; giving <b>Nvidia its first sourced magnitude of the day</b> '
           'after a beat-and-raise the tape sold anyway, and making <b>HP, not Nvidia, the night&rsquo;s worst punishment</b> '
           'on soft Q4 margin guidance; <b>the earlier CNBC and Quartz percentages are kept beside these, not replaced by them.</b>'
           '</span></div>')
    w = rep(w, old, new, 'ws tldr')

# --- 4. AFTER-HOURS section intro
OLD_NOTE = ('<p class="note"><b>&#9679; Updated 5:06 &mdash; the after-hours tape is now nearly complete, and it '
            'disagrees with the earnings in exactly one place.</b>')
NEW_NOTE = ('<p class="note"><b>&#9679; Updated 5:36 &mdash; the roundup arrives, and it is bigger than the four names '
            'this desk was watching.</b> <b>Investing.com&rsquo;s after-hours movers wrap</b>, fetched in full this run, '
            'covers <b>seven</b> names &mdash; three of which (<b>HP Inc, Synopsys, Nutanix</b>) had not appeared on this '
            'page at all &mdash; and puts a percentage on <b>every</b> one, Nvidia included. '
            '<b>&#9888; ITS NUMBERS DIFFER FROM THE 4:36&ndash;5:06 NUMBERS BELOW AND BOTH SETS ARE KEPT.</b> '
            'An extended-hours quote is a live price, so a later read moving is the expected behaviour of the tape, '
            'not evidence that an earlier read was wrong; each figure below is stamped with the time and the source that '
            'produced it and <b>no two reads are averaged, reconciled or replaced.</b> The older framing: ')
w = rep(w, OLD_NOTE, NEW_NOTE, 'ah note')

# --- 5. new after-hours cards, inserted before the WSM/ANF card
ANCHOR = '<h3>Still to be seen: Williams-Sonoma and Abercrombie &amp; Fitch</h3>'
NEWCARDS = (
 '<h3>HP Inc (HPQ) &mdash; the night&rsquo;s biggest mover in either direction <span class="tag new">New &middot; 5:36</span></h3>'
 '<p><b>Shares dropped about 11% after hours</b> &mdash; <b>a larger move than any of tonight&rsquo;s winners</b> &mdash; '
 '<b>despite beating on both lines.</b> <b>Adjusted EPS $0.83</b> on <b>revenue of $15.7&nbsp;billion, &plus;12.5% year over '
 'year</b>, against a revenue estimate of <b>$14.34&nbsp;billion</b> (a <b>9.5%</b> beat, checked). Full-year FY2026 adjusted '
 'EPS guidance was <b>raised to $3.19&ndash;$3.29</b>, a <b>$3.24 midpoint against a $3.04 consensus</b> &mdash; <b>6.6% above '
 'the street</b>, checked. <b>&#9888; The sell is about the NEXT quarter, not this one:</b> the decline is attributed to '
 '<b>soft fourth-quarter margin expectations</b> as <b>component costs rise, memory in particular.</b> '
 '<b>&#9888; THREE DIFFERENT EPS ESTIMATES WERE IN CIRCULATION AND ALL THREE ARE PRINTED, NOT MERGED:</b> Investing.com&rsquo;s '
 'wrap implies a <b>$0.66</b> consensus (it calls the print a <b>17-cent</b> beat), <b>TradingView carried $0.69</b> and '
 '<b>AlphaStreet wrote that the street expected $0.72</b>. The <b>$0.83</b> print is the only figure asserted here. '
 '(Investing.com; Yahoo Finance/Zacks preview; TradingView; AlphaStreet.)</p>'

 '<h3>Synopsys (SNPS) &mdash; a beat, a raise, and a 6% fall <span class="tag new">New &middot; 5:36</span></h3>'
 '<p><b>Shares fell 6%</b> following third-quarter results that <b>beat on both lines</b> &mdash; <b>EPS $3.91 on revenue of '
 '$2.48&nbsp;billion</b> &mdash; and came with <b>raised full-year guidance</b>. Investing.com attributes the drop to '
 '<b>profit-taking</b>. <b>&#9888; Together with HP and Nvidia that is three of tonight&rsquo;s seven names falling on results '
 'that beat</b> &mdash; the through-line of this session is expectations, not execution. (Investing.com.)</p>'

 '<h3>Nutanix (NTNX) &mdash; the quiet beat <span class="tag new">New &middot; 5:36</span></h3>'
 '<p><b>Shares jumped 5% after hours</b> on a fiscal fourth quarter that beat: <b>adjusted EPS $0.60, eleven cents ahead of '
 'estimates</b> (so a <b>$0.49</b> consensus, checked), on <b>revenue of $757.1&nbsp;million</b> driven by <b>16% year-over-year</b> '
 'growth. (Investing.com.)</p>'

 '<h3>&#9888; CORRECTION &mdash; Williams-Sonoma and Abercrombie &amp; Fitch did NOT report after this bell '
 '<span class="tag new">New &middot; 5:36</span></h3>'
 '<p><b>Both reported BEFORE Wednesday&rsquo;s open, not after it, and this page said otherwise at 4:15 and 5:06.</b> '
 '<b>Williams-Sonoma</b> released its second quarter on the morning of <b>August&nbsp;26</b> &mdash; <b>net revenues '
 '$1.96&nbsp;billion, &plus;6.7% year over year</b> against a <b>$1.93&nbsp;billion</b> estimate, <b>diluted EPS $2.10, '
 '&plus;5%</b>, <b>comparable brand revenue growth of 6.2%, accelerating from 4.8% in the first quarter</b>, <b>operating '
 'margin 17.3%</b>, with <b>full-year fiscal 2026 guidance raised on both sales and profit</b> (comparable brand revenue '
 'growth <b>4% to 6.5%</b>, total net revenue growth <b>4.7% to 7.2%</b>, operating margin <b>17.8% to 18.2%</b>). '
 '<b>Abercrombie &amp; Fitch</b> likewise reported <b>before the open</b> &mdash; it is the regular session&rsquo;s biggest '
 'mover and the Chart of the Day, covered in Movers &amp; Drivers above. <b>&#9888; Neither belongs in an after-hours '
 'section and neither carries an after-hours price; the earlier &ldquo;still to be seen tonight&rdquo; framing was wrong '
 'and is retracted here.</b> (StockStory; Investing.com transcript; MarketBeat.)</p>'
)
w = rep(w, ANCHOR, NEWCARDS + ANCHOR, 'new AH cards')

# retire the old WSM/ANF placeholder body
OLD_WSM = ('<p><b>WSM</b> and <b>ANF</b> were also on tonight&rsquo;s list per Yahoo Finance and TheStreet. '
           '<b>&#9888; No results and no after-hours prices for either appeared in any source fetched this run &mdash; '
           'nothing is asserted about them.</b> Abercrombie was the <b>regular session&rsquo;s biggest mover</b> and '
           'remains the Chart of the Day on that basis.</p>')
NEW_WSM = ('<p><b>&#9888; SUPERSEDED at 5:36 &mdash; see the correction directly above.</b> This card previously said '
           'WSM and ANF were on tonight&rsquo;s after-the-bell list per Yahoo Finance and TheStreet, and correctly declined '
           'to assert any result or price for either. <b>Both had in fact already reported that morning.</b> Abercrombie '
           'remains the <b>regular session&rsquo;s biggest mover</b> and the Chart of the Day on that basis.</p>')
w = rep(w, OLD_WSM, NEW_WSM, 'wsm placeholder')

# --- 6. Nvidia AH card: replace the direction-only sentence with the sourced magnitudes
OLD_NV = ('<b>The stock slipped in extended trading.</b> <b>&#9888; DIRECTION ONLY &mdash; the two percentages offered '
          'this run are both rejected in The Lead, so no magnitude is printed.</b>')
NEW_NV = ('<b>The stock slipped in extended trading, and as of 5:36 that slip finally has sourced magnitudes: '
          '&minus;1% (Investing.com&rsquo;s after-hours wrap) and &minus;1.3% about half an hour before the call '
          '(Kiplinger&rsquo;s live blog).</b> <b>&#9888; BOTH PRINTED, NEITHER ADOPTED &mdash; they are two reads of a '
          'live price, minutes apart, and this page does not pick between them.</b> <b>&#9888; Distinguish these from '
          '&minus;1.59%, which is NVDA&rsquo;s REGULAR-SESSION close and was offered to this desk as an after-hours '
          'figure at 5:06 and rejected; it remains rejected.</b>')
w = rep(w, OLD_NV, NEW_NV, 'nvda AH magnitude')

# --- 7. later reads appended to the three earlier movers
w = rep(w, '<b>Shares gained about 15% in extended trading.</b>',
  '<b>Shares gained about 15% in extended trading</b> (CNBC, ~5:06); <b>a later read at 5:36 has the gain at 17%</b> '
  '(Investing.com), which also adds <b>raised full-year sales guidance of $3.216&ndash;$3.226&nbsp;billion.</b> '
  '<b>&#9888; Two reads of a live price, thirty minutes apart &mdash; both printed, neither adopted.</b>',
  'okta later read')

w = rep(w, '<b>Shares soared 14% in extended trading</b>',
  '<b>Shares soared 14% in extended trading</b> (CNBC, ~4:36); <b>a later read at 5:36 has the gain at 12%</b> '
  '(Investing.com). <b>&#9888; A THIRD, IRRECONCILABLE EPS FIGURE ARRIVED WITH THAT LATER READ AND IS NOT MERGED:</b> '
  'Investing.com states <b>&ldquo;an EPS of $5.90 ($2.63 ahead of consensus)&rdquo;</b>, which cannot be the same measure '
  'as CNBC&rsquo;s <b>$4.29 a share</b> &mdash; and <b>four quarters at $5.90 is $23.60, far above the company&rsquo;s own '
  '$16.67&ndash;$16.71 full-year guide</b> (checked), so it cannot be a comparable annualisable figure either. '
  '<b>Recorded, flagged, not published as Salesforce&rsquo;s EPS.</b> The figures below are unchanged',
  'crm later read')

w = rep(w, 'shares jumped as much as 12% in extended trading</b>',
  'shares jumped as much as 12% in extended trading</b> (Quartz, ~5:06), with <b>a later 5:36 read at &plus;10%</b> '
  '(Investing.com) &mdash; <b>both printed, neither adopted</b>',
  'crwd later read')

# --- 8. ANF: the price ladder resolves, and a second consensus figure appears
OLD_ANF_TAIL = ('so that percentage is not published; the 2:40 strip figure is.</p>')
NEW_ANF_TAIL = ('so that percentage is not published; the 2:40 strip figure is. '
  '<b>&#9679; New &middot; 5:36 &mdash; A THIRD STOCKSTORY READ TURNS UP, AND IT VINDICATES THE LADDER RATHER THAN '
  'BREAKING IT.</b> A separate StockStory piece, <b>published 11:39&nbsp;a.m. ET</b>, is headlined <b>&ldquo;Stock Jumps '
  '11.9%&rdquo;</b> and prints <b>$121.47</b> &mdash; a number that, taken alone, looks like it contradicts the &plus;40.86% '
  'above. <b>It does not.</b> Read as a sequence, the three prices are <b>$121.47 at 11:39, $144.81 at 12:55, $153.40 at '
  '2:40</b>, and against the common <b>$108.90</b> base (which the 2:40 strip confirms exactly: <b>153.40 &minus; 44.50 = '
  '108.90</b>) they are <b>&plus;11.5%, &plus;33.0% and &plus;40.9%</b> &mdash; <b>a stock climbing monotonically through '
  'the session, checked in Python.</b> <b>&#9888; What still does NOT reconcile is StockStory&rsquo;s own arithmetic: '
  'its 11.9% needs a $108.55 base and its 41.8% needs no base this page can find.</b> That article also gives figures the '
  'earlier read did not: <b>adjusted EBITDA $296&nbsp;million against a $170.3&nbsp;million estimate, a 23.4% margin</b>; '
  '<b>third-quarter revenue guidance of $1.36&nbsp;billion at the midpoint against $1.34&nbsp;billion expected</b>; '
  '<b>full-year GAAP EPS guidance of $13.35 at the midpoint</b> (the exact midpoint of the <b>$13.10&ndash;$13.60</b> range '
  'already published, checked); <b>operating margin 19.9%, up from 17.1%</b>; <b>free cash flow margin 15.9%, up from 4.2%</b>; '
  'and <b>same-store sales flat year over year.</b> <b>&#9888; It also puts the GAAP EPS consensus at $1.97, where this page '
  'carries $1.99 &mdash; a two-cent divergence, printed, not smoothed.</b> <b>&#9888; NO ANF CLOSING PRICE IS ASSERTED: '
  'searches for one this run returned mutually contradictory figures</b> (one summary offered <b>$112.62, &plus;1.94%</b> and '
  'flagged it as three weeks old; another offered <b>$97.69, &plus;5.19%</b>, which is beneath every intraday price above). '
  '<b>Nothing from either is published.</b></p>')
w = rep(w, OLD_ANF_TAIL, NEW_ANF_TAIL, 'anf tail')

# --- 9. demote stale "New" prose markers from earlier editions
w = w.replace('<span class="tag new">New &middot; 5:06</span>', '<span class="tag">5:06</span>')
w = w.replace('<b>&#9679; New &middot; 5:06 &mdash;', '<b>&#9679; 5:06 &mdash;')
if 'New &middot; 5:06' in w:
    fails.append('ws: stale 5:06 New marker survived')

wr('wallstreet-briefing.html', w)

# ================================ CYBER ===================================
c = rd('cyber-briefing.html')

# --- tldr
old = c[c.find('<div class="tldr"><b>The Wire</b>'):]
old = old[:old.find('</div>') + 6]
if old.count('The Wire') != 1:
    fails.append('cy tldr: could not isolate')
else:
    new = ('<div class="tldr"><b>The Wire</b> <span>Two vendors emptied their queues on Tuesday &mdash; '
           '<b>NVIDIA published four advisories, one of them covering 18 flaws in its NemoClaw and OpenShell AI-agent '
           'runtime products, two critical</b>, and <b>Adobe shipped seven advisories with critical code execution fixes '
           'in five products</b> &mdash; while the live problem for anyone running WordPress is <b>two critical '
           'authentication bypasses in the MiniOrange SAML SSO plugin (CVE-2026-61979 and CVE-2026-15981) that are being '
           'sprayed at every site running it</b>, silently patched and largely unannounced; <b>CISA&rsquo;s KEV catalogue '
           'is static for a fifteenth consecutive edition</b>, leaving Patch Priority at <b>Oracle CVE-2026-21962, due '
           'tomorrow</b>.</span></div>')
    c = rep(c, old, new, 'cy tldr')

# --- Vulnerability Watch: replace the 5:06 "not added" note with the fetched detail
OLD_VN_START = '<p class="note"><b>&#9679; New &middot; 5:06 &mdash; seen this run, deliberately NOT added to the table.</b>'
i = c.find(OLD_VN_START)
if i < 0 or c.count(OLD_VN_START) != 1:
    fails.append('cy vuln note: anchor missing')
else:
    j = c.find('</p>', i) + 4
    NEW_VN = (
     '<p class="note"><b>&#9679; New &middot; 5:36 &mdash; the advisories flagged but withheld at 5:06 have now been read, '
     'and they publish.</b> At 5:06 this page saw an aggregator headline saying Adobe and NVIDIA had each shipped critical '
     'advisories and <b>refused to print anything from it because no bulletin had been fetched.</b> SecurityWeek&rsquo;s '
     'write-up has now been fetched in full, so here is what is actually in them. <b>NVIDIA published four advisories on '
     'Tuesday.</b> One covers <b>18 vulnerabilities in NemoClaw and OpenShell</b>, the company&rsquo;s enterprise AI '
     'security and runtime products that wrap around autonomous AI agents: <b>two are critical</b> and can be exploited for '
     '<b>code execution, privilege escalation, data tampering, information disclosure and denial of service</b>, with '
     '<b>a dozen more rated high</b> and similar impact. <b>Cyera has detailed one of them, showing it can be used to hijack '
     'AI agents.</b> A second advisory fixes <b>five flaws in the DGX Spark AI computer</b> (three high-severity); a third '
     'fixes <b>two high- and three medium-severity issues in Unified Fabric Manager</b>; the fourth adds mitigation advice '
     'for <b>Rowhammer attacks against NVIDIA GPUs</b>. Separately, last week NVIDIA disclosed <b>five vulnerabilities in '
     'Triton Inference Server</b>, some allowing arbitrary code execution, plus fixes in <b>Cumulus Linux and NVOS</b>. '
     '<b>Adobe &mdash; which now publishes advisories twice a month &mdash; released seven advisories</b>, patching '
     '<b>critical code execution flaws in Substance 3D Designer, Substance 3D Sampler, Substance 3D Painter, XD and '
     'Campaign Classic</b>, and denial-of-service and information-exposure flaws in <b>Illustrator and the Content '
     'Credentials SDK</b>. <b>&#9888; Adobe says none of these have been exploited in the wild, and only the Campaign '
     'Classic advisory carries a priority rating of 1</b>, its higher-risk-of-exploitation tier. '
     '<b>&#9888; NO CVE IDENTIFIER, CVSS SCORE OR FIXED VERSION IS ASSERTED FOR ANY OF THESE</b> &mdash; the coverage '
     'fetched this run states counts and severities, not identifiers, and this desk does not manufacture the rest. '
     '<b>None of them is in CISA KEV and none carries a federal deadline.</b> Administrators should read the vendor '
     'advisories directly. Separately, <b>CISA&rsquo;s alert pages remain unchanged</b> &mdash; the latest are still '
     '<b>August&nbsp;18 (four CVEs)</b>, <b>August&nbsp;20 (two TrueConf)</b> and <b>August&nbsp;21 (one Zimbra)</b>, with '
     'the <b>Gitea addition of August&nbsp;25</b> already on the board below. '
     '(SecurityWeek, securityweek.com/adobe-and-nvidia-patch-dozens-of-vulnerabilities/.)</p>')
    c = c[:i] + NEW_VN + c[j:]

# --- MiniOrange row into the CVE table
TBL_HDR = '<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>'
MINI_ROW = (TBL_HDR +
 '<tr><td>CVE-2026-61979 and CVE-2026-15981 <span class="tag new">New &middot; 5:36</span></td>'
 '<td><span class="muted">Not stated in the coverage fetched this run &mdash; described as &ldquo;critical&rdquo;; '
 'no numeric score is asserted</span></td>'
 '<td>MiniOrange SAML 2.0 Single Sign-On plugin for WordPress &mdash; free edition fixed in <b>5.4.5</b>; paid and '
 'enterprise editions use a different versioning scheme and were <b>not</b> separately notified</td>'
 '<td><b>Authentication bypass, exploitation attempts under way.</b> Analysis by <b>DigitalOcean and Patchstack</b> finds '
 'the two flaws are <b>critical authentication bypasses that allow logging in as any WordPress user, administrators '
 'included.</b> Patchstack characterises the activity as <b>opportunistic rather than targeted</b> &mdash; the operator is '
 '<b>&ldquo;throwing the exploit at every site with the plugin installed without checking which edition or version is '
 'behind it.&rdquo;</b> <b>&#9888; This is a silent-patch problem as much as a code problem:</b> all affected versions have '
 'been patched, but <b>only the free edition has an advisory, and it lists the fix as a bugfix rather than a security '
 'patch</b>; paid users must <b>check and update manually</b>. The free edition alone is installed on <b>more than 10,000 '
 'sites</b>; paid-edition install counts are not published. <b>&#9888; Not in CISA KEV, so no federal deadline &mdash; '
 'which is not a reason to wait.</b> (SecurityWeek, Aug&nbsp;25; Patchstack.)</td></tr>')
c = rep(c, TBL_HDR, MINI_ROW, 'miniorange row')

# --- Breaches & incidents: three new cards at the top of the deck
BR_ANCHOR = '<div class="lab">Breaches &amp; incidents</div>\n<div class="cards">\n'
NEW_BR = (BR_ANCHOR +
 '<div class="card"><div class="tags"><span class="tag new">New &middot; 5:36</span><span class="tag warn">Healthcare</span>'
 '<span class="tag">SEC disclosure</span></div>\n'
 '<h3>Nutex Health tells the SEC an intruder got in and took data out</h3>\n'
 '<p><b>Nutex Health has informed the U.S. Securities and Exchange Commission that it recently detected unauthorized '
 'access and data exfiltration</b>, and SecurityWeek reports <b>sensitive information was exposed.</b> '
 '<b>&#9888; Scope, record count, threat actor and dwell time are not asserted here</b> &mdash; the coverage fetched this '
 'run does not state them, and a healthcare breach headline is exactly the kind that attracts invented numbers. '
 '<b>No CVE, not in KEV, no federal deadline.</b> (SecurityWeek.)</p></div>\n'

 '<div class="card"><div class="tags"><span class="tag new">New &middot; 5:36</span><span class="tag warn">Phishing</span>'
 '<span class="tag">ShinyHunters</span></div>\n'
 '<h3>A security vendor gets phished &mdash; ReliaQuest confirms a ShinyHunters intrusion</h3>\n'
 '<p><b>ReliaQuest has confirmed it was hacked by ShinyHunters</b> and says <b>the impact was limited.</b> The entry point '
 'was ordinary: <b>an employee fell for a phishing attack and the attackers reached a dashboard.</b> '
 '<b>&#9888; Why it belongs on a defender&rsquo;s page:</b> this is the same pattern as the RMM and ClickFix items below '
 '&mdash; <b>no exploit, no CVE, a person persuaded to do something</b> &mdash; and the victim here is a company whose '
 'business is detecting exactly this. <b>Not in KEV, no federal deadline.</b> (SecurityWeek.)</p></div>\n'

 '<div class="card"><div class="tags"><span class="tag new">New &middot; 5:36</span><span class="tag crit">Critical '
 'infrastructure</span><span class="tag">CISA</span></div>\n'
 '<h3>CISA: more than 100 internet-exposed water systems were targeted in July</h3>\n'
 '<p><b>CISA reports that over 100 internet-exposed water systems were targeted in cyberattacks during July.</b> '
 '<b>&#9888; The exposure is the story</b> &mdash; these are operational-technology assets reachable from the public '
 'internet, a category where the fix is usually network architecture rather than a patch. <b>&#9888; Attribution, '
 'technique, and whether any system was actually compromised are not asserted here; the coverage fetched this run states '
 'the targeting and the count.</b> Also new from the same desk this week: <b>Chrome 152 patches more than 300 '
 'vulnerabilities</b>, and researchers describe <b>the first malware built specifically for car head units</b>, now feeding '
 'a botnet. <b>&#9888; No CVE, CVSS or fixed version is asserted for any of these three.</b> (SecurityWeek.)</p></div>\n')
c = rep(c, BR_ANCHOR, NEW_BR, 'new breach cards')

# --- KEV static counter
c = rep(c, 'fourteenth consecutive edition', 'fifteenth consecutive edition', 'kev counter',
        count=c.count('fourteenth consecutive edition'))

# --- demote stale markers
c = c.replace('<span class="tag new">New &middot; 5:06</span>', '<span class="tag">5:06</span>')
c = c.replace('<b>&#9679; New &middot; 5:06 &mdash;', '<b>&#9679; 5:06 &mdash;')
if 'New &middot; 5:06' in c:
    fails.append('cy: stale 5:06 New marker survived')

wr('cyber-briefing.html', c)

# ================================= MMA ====================================
m = rd('mma-briefing.html')
m = rep(m, 'twenty-eighth consecutive edition', 'thirty-first consecutive edition', 'mma tldr counter',
        count=m.count('twenty-eighth consecutive edition'))
m = rep(m, 'thirtieth consecutive edition', 'thirty-first consecutive edition', 'mma board counter',
        count=m.count('thirtieth consecutive edition'))
m = m.replace('<span class="tag new">New &middot; 5:06</span>', '<span class="tag">5:06</span>')
m = m.replace('<b>&#9679; New &middot; 5:06 &mdash;', '<b>&#9679; 5:06 &mdash;')
if 'New &middot; 5:06' in m:
    fails.append('mma: stale 5:06 New marker survived')
wr('mma-briefing.html', m)

# ================================ INDEX ===================================
x = rd('index.html')
x = rep(x, '<h2>Twenty-four npm packages, one payload</h2>',
  '<h2>Two vendors empty their advisory queues, and WordPress takes the live hit</h2>', 'idx sec h2')
x = rep(x,
  '<p>CISA&rsquo;s newest KEV entry, the <b>Gitea flaw CVE-2026-60004 (CVSS 9.8)</b>, is being used to plant Git hooks and '
  'mine crypto, with a <b>federal deadline of August&nbsp;28</b>; a separate phishing operation is installing '
  '<b>legitimate remote-control software across 46 countries</b>.</p>',
  '<p><b>NVIDIA shipped four advisories &mdash; one covering 18 flaws in its AI-agent runtime products, two of them '
  'critical &mdash; and Adobe seven</b>, while two <b>critical authentication bypasses in the MiniOrange SAML SSO '
  'plugin</b> are being sprayed at every WordPress site running it. <b>CISA&rsquo;s KEV list is unchanged; Oracle '
  'CVE-2026-21962 is due tomorrow.</b></p>', 'idx sec p')

x = rep(x, '<h2>Software takes the night Nvidia was supposed to own</h2>',
  '<h2>Nvidia gets a number, HP takes the beating</h2>', 'idx mkt h2')
x = rep(x,
  '<p>Nvidia beat with <b>$96.22&nbsp;billion of revenue against $92.17&nbsp;billion expected</b> and guided the current '
  'quarter <b>above the street to $108&nbsp;billion</b> &mdash; and the stock slipped anyway, while <b>Okta rose about '
  '15%</b>, <b>Salesforce 14%</b> and <b>CrowdStrike as much as 12%</b> after the bell.</p>',
  '<p>A full after-hours roundup prices the night at <b>Okta &plus;17%, Salesforce &plus;12%, CrowdStrike &plus;10%, '
  'Nutanix &plus;5%, Nvidia &minus;1%, Synopsys &minus;6% and HP Inc &minus;11%</b> &mdash; giving Nvidia its <b>first '
  'sourced magnitude</b> after a beat-and-raise the tape sold anyway, and making <b>HP, not Nvidia, the night&rsquo;s '
  'worst punishment</b>.</p>', 'idx mkt p')
wr('index.html', x)

# ================================ REPORT ==================================
if fails:
    print("FAILED (%d):" % len(fails))
    for f in fails:
        print("  -", f)
    sys.exit(1)
print("OK - all anchors matched, four pages written")
