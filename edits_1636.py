#!/usr/bin/env python3
# Edition edits — Sunday Aug 30 2026, ~4:36 PM ET research (ninth run of the day)
import io, re, sys

O = "/sessions/relaxed-dreamy-einstein/mnt/outputs/"

def rd(p):
    with io.open(O+p, encoding="utf-8") as f: return f.read()

def wr(p, s):
    with io.open(O+p, "w", encoding="utf-8") as f: f.write(s)

fails = []
def sub_once(s, needle, repl, label):
    n = s.count(needle)
    if n != 1:
        fails.append("%s: needle count=%d (expected 1)" % (label, n))
        return s
    return s.replace(needle, repl, 1)

# ─────────────────────────────────────────────────────────────── CYBER ──
cy = rd("cyber-briefing.html")

# 1) Three new Breaches & Incidents cards at the head of the section.
CLOP = (
 '<div class="card"><div class="tags"><span class="tag new">New &middot; 4:36 PM</span>'
 '<span class="tag warn">Victim count disputed</span><span class="tag">Extortion</span></div>'
 '<h3>Cl0p emptied one product-lifecycle platform and forty-odd manufacturers came out with it &mdash; Shell, GE and Philips among them</h3>'
 '<p><b>What happened.</b> The <b>Cl0p</b> extortion group listed a batch of new victims on its leak site '
 'taken, according to reporting fetched this run, through <b>internet-exposed instances of PTC&rsquo;s '
 '<i>Windchill</i> and <i>FlexPLM</i></b> product-lifecycle-management software. The flaw is tracked as '
 '<b>CVE-2026-12569</b> and is described as a <b>critical improper-input-validation</b> issue. <b>Shell, '
 'General Electric and Philips have each confirmed they are investigating</b> the claims.</p>'
 '<p><b>The claimed volumes are the group&rsquo;s own figures, and they are printed as such:</b> '
 '<b>89 GB</b> from <b>Shell</b>, <b>391 GB</b> from <b>GE</b> and <b>15.5 GB</b> from <b>Philips</b>. '
 'In Shell&rsquo;s case the group says the material includes <b>engineering drawings, photographs of oil '
 'facilities and project plans</b>. &#9888; <b>No company has confirmed a volume</b>, and this page does not '
 'convert an extortion post into a measured loss.</p>'
 '<p>&#9888; <b>The victim count came back three ways and none is adopted.</b> One account says <b>43 new '
 'victims</b>, a second <b>more than 40</b>, a third <b>nearly 50</b>. <b>43 is the most specific and is '
 'printed as that source&rsquo;s figure</b>, with the spread recorded beside it &mdash; a leak-site tally '
 'moves as posts are added, so three counts taken on three days are not necessarily three contradictions.</p>'
 '<p><b>What the companies actually said, which is narrower than the claims.</b> <b>Philips</b> says it '
 '<b>identified and contained an attempted compromise of one enterprise server</b> holding internal data and '
 'that <b>customer-facing environments were not reached</b>. <b>Shell</b> confirms only that it is '
 '<b>investigating a potential incident</b>. <b>That gap &mdash; between what the leak site claims and what '
 'the victim confirms &mdash; is the whole story of a mass-exploitation campaign in its first fortnight</b>, '
 'and this page will carry both halves rather than resolve them early.</p></div>'
)

MEDUSA = (
 '<div class="card"><div class="tags"><span class="tag new">New &middot; 4:36 PM</span>'
 '<span class="tag">Ransomware</span><span class="tag">Healthcare</span></div>'
 '<h3>Medusa is past 500 victims, and the federal advisory has been reopened with a health-sector co-author</h3>'
 '<p><b>What was published.</b> <b>CISA, the FBI and HHS updated their joint advisory on Medusa ransomware '
 'on August 18, 2026</b>, adding findings from FBI investigations conducted <b>through April 2026</b>. The '
 'update states that Medusa actors have <b>impacted more than 500 victims</b> across <b>healthcare, '
 'education, legal services, insurance, technology and manufacturing</b>. Medusa is a '
 '<b>ransomware-as-a-service variant first identified in June 2021</b> and operates by <b>double extortion</b> '
 '&mdash; encrypting data while threatening to publish it.</p>'
 '<p><b>Why the re-issue is the news rather than the number.</b> The advisory was <b>first published on '
 'March 12, 2025</b>; this is an update to a standing document, not a new one. What changed is the '
 'authorship: <b>HHS joined as a co-sealer</b>, contributing what it sees of Medusa&rsquo;s operations '
 'against the <b>Healthcare and Public Health Sector</b>. <b>A federal advisory gaining a health-department '
 'co-author is a statement about where the victims are</b>, made in the only way that document can make it.</p>'
 '<p><b>One incident is cited for scale.</b> In <b>late February 2026</b> an attack took the <b>University '
 'of Mississippi Medical Center offline for nine days</b>. UMMC is described as the state&rsquo;s largest '
 'hospital system and its <b>only Level I trauma center, only children&rsquo;s hospital and only organ '
 'transplant program</b> &mdash; which is what "a frequent target" means when the target is a hospital '
 'and there is no second one.</p></div>'
)

MICROCOMM = (
 '<div class="card"><div class="tags"><span class="tag new">New &middot; 4:36 PM</span>'
 '<span class="tag warn">Attribution refused</span><span class="tag">Critical infrastructure</span></div>'
 '<h3>The FBI is looking at a hack of the company that makes the controllers in America&rsquo;s water plants</h3>'
 '<p><b>What happened.</b> <b>Micro-Comm</b>, of <b>Olathe, Kansas</b>, which makes the <b>programmable logic '
 'controllers</b> used by water and wastewater facilities, <b>discovered a breach on July 31</b>. The '
 '<b>Barracuda</b> ransomware group &mdash; a new group that says it is <b>profit-motivated and not '
 'government sponsored</b> &mdash; then published what it claimed were <b>nearly 850,000 stolen files '
 'totalling roughly 644 GB</b>. <b>The company and the FBI have both confirmed the attack</b>, which had not '
 'been reported before.</p>'
 '<p>&#9888; <b>The tempting attribution is available and this page is not making it.</b> The breach fell '
 'inside a <b>late-July run of attacks on PLCs in Minnesota and at least six other states</b> that '
 'researchers link to a <b>long-running Iranian-affiliated campaign</b>. <b>The government has not connected '
 'Micro-Comm to that campaign</b>, and the FBI is reported to have told the company its attack <b>appeared '
 'opportunistic rather than specifically targeted</b>. <b>Sitting inside a window is not membership of a '
 'campaign</b>, and the two claims are printed apart because the only source that joins them is inference.</p>'
 '<p><b>What the company says was not taken.</b> Micro-Comm describes the attack as limited and says it did '
 '<b>not expose customer passwords, credentials, or the information that lets Micro-Comm remotely reach its '
 'own equipment</b> &mdash; which is the sentence that matters, because remote access to a supplier&rsquo;s '
 'installed controllers is the reason a supplier breach in this sector is worth a briefing at all.</p></div>'
)

cy = sub_once(cy,
    '<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">\n',
    '<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">\n' + CLOP + "\n" + MEDUSA + "\n" + MICROCOMM + "\n",
    "cyber: breaches head")

# 2) Vulnerability Watch — add CVE-2026-12569.
mrow = re.search(r'<tr>\s*<td[^>]*>\s*<b>CVE-2026-62878</b>', cy)
if not mrow:
    fails.append("cyber: could not locate CVE-2026-62878 row to anchor new row")
else:
    NEWROW = (
      '<tr><td><b>CVE-2026-12569</b></td><td>Not stated</td>'
      '<td>PTC <b>Windchill</b> / <b>FlexPLM</b> (internet-exposed instances)</td>'
      '<td><b>Improper input validation</b>, described as critical. Reported as the entry point for the '
      '<b>Cl0p</b> mass-extortion campaign that named <b>Shell, GE and Philips</b> among a batch of victims. '
      '&#9888; <b>No CVSS figure was stated by any source fetched this run and none is invented</b>; the '
      'severity word is the reporting&rsquo;s, not a vendor score. Not KEV-listed as of this run.</td></tr>\n'
    )
    cy = cy[:mrow.start()] + NEWROW + cy[mrow.start():]

# 3) Stat strip — add the Cl0p and Medusa figures.
cy = sub_once(cy,
    '<div class="stat"><div class="n">Overdue</div>',
    '<div class="stat"><div class="n">43</div><div class="l">Victims named in one leak-site batch tied to the '
    '<b>PTC Windchill / FlexPLM</b> flaw &mdash; the most specific of three counts in circulation '
    '(<b>&ldquo;more than 40&rdquo;</b>, <b>&ldquo;nearly 50&rdquo;</b>); <b>Cl0p&rsquo;s tally, not a confirmed one</b></div></div>\n'
    '<div class="stat"><div class="n">500+</div><div class="l">Medusa ransomware victims in the <b>CISA / FBI / HHS</b> '
    'advisory updated <b>Aug 18</b>, from FBI investigations through <b>April 2026</b></div></div>\n'
    '<div class="stat"><div class="n">Overdue</div>',
    "cyber: stat strip")

# 4) TL;DR
CY_TLDR = (
 'Three ransomware and extortion stories are new to this board and each one is carried with its claim and its '
 'confirmation kept apart: <b>Cl0p</b> named a batch of victims &mdash; <b>43</b> by the most specific count, '
 'with <b>&ldquo;more than 40&rdquo;</b> and <b>&ldquo;nearly 50&rdquo;</b> also in circulation &mdash; taken '
 'through <b>CVE-2026-12569</b> in internet-exposed <b>PTC Windchill and FlexPLM</b>, with <b>Shell, GE and '
 'Philips</b> all confirming investigations while the terabyte figures remain <b>the group&rsquo;s own</b>; '
 'the <b>CISA / FBI / HHS Medusa advisory was reopened on August 18</b> past <b>500 victims</b> and with '
 '<b>HHS joining as a co-sealer</b>; and the <b>FBI is investigating a breach at Micro-Comm</b>, the Kansas '
 'maker of the <b>programmable logic controllers used in water and wastewater plants</b> &mdash; where the '
 'nearby <b>Iranian-linked PLC campaign is recorded and explicitly not attributed</b>, the FBI having reportedly '
 'called the intrusion <b>opportunistic</b>. Carried: <b>CVE-2026-62878</b> in <b>Windows DNS Server</b> stays '
 'on the board for reachability rather than activity, and the <b>two federal deadlines due today</b> '
 '&mdash; ownCloud <b>CVE-2023-49105</b> and Linux kernel <b>CVE-2026-53362</b> &mdash; were re-read against a '
 '4:36 PM clock and still fall <b>Sunday, August 30</b>.'
)
cy = re.sub(r'(<div class="tldr"><b>The Wire</b> <span>).*?(</span></div>)',
            lambda m: m.group(1) + CY_TLDR + m.group(2), cy, count=1, flags=re.S)

# 5) Sources
CY_SRC = (
 '<a href="https://www.bleepingcomputer.com/news/security/philips-and-ge-investigating-clop-ransomware-data-theft-claims/">BleepingComputer &mdash; Philips and GE investigating Clop data-theft claims (CVE-2026-12569, 43 victims)</a><br>'
 '<a href="https://www.computerweekly.com/news/366648757/Multiple-organisations-investigating-fresh-wave-of-Cl0p-breaches">Computer Weekly &mdash; Multiple organisations investigating fresh wave of Cl0p breaches</a><br>'
 '<a href="https://www.helpnetsecurity.com/2026/08/19/medusa-ransomware-cisa-warning/">Help Net Security &mdash; Medusa ransomware gang has hit over 500 organizations, CISA warns</a><br>'
 '<a href="https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a">CISA &mdash; #StopRansomware: Medusa Ransomware (AA25-071A, updated Aug 18 2026)</a><br>'
 '<a href="https://www.newsmax.com/newsfront/cybersecurity-ransomware-water/2026/08/26/id/1267342/">Newsmax &mdash; Hack of water sector supplier Micro-Comm in Kansas draws FBI scrutiny</a><br>'
)
mfoot = re.search(r'<div class="srcs">', cy)
if not mfoot:
    fails.append("cyber: no srcs block")
else:
    # insert after the first link that follows the srcs marker
    ins = cy.index('<a href="', mfoot.start())
    cy = cy[:ins] + CY_SRC + cy[ins:]

wr("cyber-briefing.html", cy)

# ──────────────────────────────────────────────────────────── WALL ST ──
ws = rd("wallstreet-briefing.html")

WS_PARA = (
 '<p><b>Twelfth September read, taken at 4:36 PM, and the venue that had been quoted round now has a '
 'precise pair &mdash; which makes the split wider, not narrower.</b> <b>Kalshi</b> returned this run at '
 '<b>47% for a 25-basis-point hike and 54% for a hold</b>. This page has carried Kalshi at <b>52% hold</b> '
 'and at <b>48% hike</b> in earlier editions; <b>47/54 is a third rendering, not a correction of the other '
 'two</b>, and it is recorded rather than substituted, because no source fetched this run dates its quote '
 'or states which reading is current. &#9888; <b>Note that 47 and 54 sum to 101</b> &mdash; the two figures '
 'come from the same account and are printed as that account gives them, not reconciled into a pair that '
 'adds up. <b>The CME side gained two more renderings of its own:</b> <b>&ldquo;nearly 56%&rdquo;</b>, and a '
 'separate account putting the post-speech probability at <b>&ldquo;nearly 60%, up from 35% the previous '
 'day&rdquo;</b>. Against the <b>57%</b>, <b>55.7%</b> and <b>55%</b> already carried, the honest statement '
 'is a <b>range in the mid-to-high fifties on CME futures against a hold-leaning reading on the prediction '
 'markets</b>, and that is what is printed. <b>The direction is not in dispute and the level is</b>; the '
 '<b>FOMC decision is September 16</b>, unchanged.</p>'
)
m = re.search(r'<b>The FOMC date is unchanged and not in dispute: September 16\.</b></p>', ws)
if not m:
    fails.append("ws: FOMC anchor not found")
else:
    ws = ws[:m.end()] + "\n" + WS_PARA + ws[m.end():]

WS_TLDR_ADD = (
 ' <b>New at 4:36 PM:</b> a <b>twelfth read of September</b> and still no adoption &mdash; <b>Kalshi</b> came '
 'back at <b>47% hike / 54% hold</b>, a third rendering from that venue rather than a correction of the '
 '<b>52%</b> and <b>48%</b> this page already carried, while the CME side added <b>&ldquo;nearly 56%&rdquo;</b> '
 'and <b>&ldquo;nearly 60%, up from 35% the day before&rdquo;</b> to its own spread; the direction is '
 'undisputed and the level is not, so a <b>range</b> is printed and no number is adopted.'
)
mt = re.search(r'(<div class="tldr"><b>The Tape</b> <span>)(.*?)(</span></div>)', ws, flags=re.S)
if not mt:
    fails.append("ws: tldr not found")
else:
    ws = ws[:mt.start(3)] + WS_TLDR_ADD + ws[mt.start(3):]

WS_SRC = (
 '<a href="https://news.kalshi.com/p/fed-rate-hike-odds-september-2026-jackson-hole-speech">Kalshi &mdash; Fed rate-hike odds after the Jackson Hole speech (47% hike / 54% hold)</a><br>'
 '<a href="https://www.cnbc.com/2026/08/28/-september-fed-decision-now-a-coin-flip-as-rate-hike-odds-increase.html">CNBC &mdash; September Fed decision now a coin flip as rate-hike odds increase post-Warsh</a><br>'
)
mfoot = re.search(r'<div class="srcs">', ws)
if not mfoot:
    fails.append("ws: no srcs block")
else:
    ins = ws.index('<a href="', mfoot.start())
    ws = ws[:ins] + WS_SRC + ws[ins:]

wr("wallstreet-briefing.html", ws)

# ──────────────────────────────────────────────────────────────── MMA ──
mma = rd("mma-briefing.html")

mma = sub_once(mma,
    '<b>The main card starts at 2 PM ET / 11 AM PT</b>',
    '<b>New at 4:36 PM &mdash; the prelims now have a start time too: 10 AM ET</b>, which puts the full '
    'broadcast day for a U.S. audience between mid-morning and late afternoon. '
    '<b>The main card starts at 2 PM ET / 11 AM PT</b>',
    "mma: UFC 333 prelim time")

MMA_TLDR_ADD = (
 ' <b>New at 4:36 PM:</b> <b>UFC 333&rsquo;s prelims have a start time &mdash; 10 AM ET</b>, ahead of the '
 '<b>2 PM ET</b> main card already carried, and the <b>Paris broadcast window was re-confirmed at prelims '
 '12 PM ET / main card 3 PM ET</b>. The <b>champions board was cross-checked against ESPN&rsquo;s current-champions '
 'page for a ninth consecutive run and is unchanged</b> &mdash; <b>Ulberg</b> at light heavyweight, '
 '<b>Strickland</b> at middleweight and <b>Volkanovski</b> at featherweight all confirmed again.'
)
mt = re.search(r'(<div class="tldr"><b>Tale of the Tape</b> <span>)(.*?)(</span></div>)', mma, flags=re.S)
if not mt:
    fails.append("mma: tldr not found")
else:
    mma = mma[:mt.start(3)] + MMA_TLDR_ADD + mma[mt.start(3):]

MMA_SRC = (
 '<a href="https://en.wikipedia.org/wiki/UFC_333">Wikipedia &mdash; UFC 333: Volkanovski vs. Evloev (prelims 10 AM ET, main card 2 PM ET)</a><br>'
 '<a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">ESPN &mdash; Current and all-time UFC champions (re-verified this run)</a><br>'
)
mfoot = re.search(r'<div class="srcs">', mma)
if not mfoot:
    fails.append("mma: no srcs block")
else:
    ins = mma.index('<a href="', mfoot.start())
    mma = mma[:ins] + MMA_SRC + mma[ins:]

wr("mma-briefing.html", mma)

print("EDIT FAILURES:", fails if fails else "none")
sys.exit(1 if fails else 0)
