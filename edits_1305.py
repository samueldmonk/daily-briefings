#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Edits for the 2026-08-24 ~1:05pm ET Midday Edition run."""
import io

D = "/sessions/amazing-bold-curie/mnt/outputs/"
FAIL = []
M = u"−"  # literal minus sign used throughout the pages

def load(f): return io.open(D+f, encoding="utf-8").read()
def save(f, s): io.open(D+f, "w", encoding="utf-8").write(s)

def rep(s, old, new, label, count=1):
    n = s.count(old)
    if n != count:
        FAIL.append("MISS[%s] found %d expected %d" % (label, n, count))
        return s
    return s.replace(old, new)

def cut(s, start_marker, label):
    """return the block from start_marker through the next </div>"""
    i = s.find(start_marker)
    if i == -1:
        FAIL.append("MISS[%s] anchor" % label); return None
    j = s.find('</div>', i)
    return s[i:j+6]

# ============================== WALL STREET ==============================
w = load("wallstreet-briefing.html")

w = rep(w,
 u'<div class="tldr"><b>The Tape</b> <span>The chip slide now has a named cause &mdash; weekend reports that Washington may let Apple buy memory from China&rsquo;s CXMT and YMTC knocked SanDisk down 9% and Micron and Western Digital down 7% apiece &mdash; while the broad tape keeps grinding back, with CNBC reading the S&amp;P 500 off about 0.1%, the Nasdaq Composite off about 0.4% and the Dow up 161 points, and Treasury Secretary Scott Bessent&rsquo;s Iran sanctions press conference confirmed for 1 p.m. ET.</span></div>',
 u'<div class="tldr"><b>The Tape</b> <span>Chip and memory weakness is still setting the tone &mdash; the group gapped down on weekend reports Washington may let Apple buy memory from China&rsquo;s CXMT and YMTC &mdash; leaving the S&amp;P 500 off about 0.2%, the Nasdaq Composite off about 0.4% and the Dow up about 0.2% in early-afternoon trade, while Treasury Secretary Scott Bessent&rsquo;s Iran sanctions press conference begins at 1 p.m. ET and the bond market keeps refusing to reward his $1 trillion cash pile.</span></div>',
 "ws-tldr")

w = rep(w,
 u'<h2>The memory trade finally has a headline behind it &mdash; and Bessent speaks at 1 p.m. ET</h2>',
 u'<h2>Chips keep the Nasdaq red as Bessent takes the podium &mdash; and the bond market keeps saying no</h2>',
 "ws-lead-h2")

# --- replace first lead paragraph ---
i = w.find(u'<p><b>Fresh this edition:</b> the chip weakness that has led the tape all session')
j = w.find(u'</p>', i) if i != -1 else -1
if i == -1 or j == -1:
    FAIL.append("MISS[ws-lead-p1] anchor")
else:
    NEW_P1 = (u'<p><b>As of roughly 1:15 p.m. ET.</b> The tape has settled into the shape it has held all day: '
      u'blue chips up, semiconductors down, and nothing resolved until Nvidia reports on Wednesday. The Motley Fool&rsquo;s '
      u'live index board, read at this edition, had the <b>S&amp;P 500 off about 0.2%</b>, the <b>Nasdaq Composite off about 0.4%</b> '
      u'and the <b>Dow Jones Industrial Average up about 0.2%</b> &mdash; and for the first time today all three of those readings '
      u'reconcile <em>exactly</em> against Friday&rsquo;s verified closes, which is the test this desk has been applying all session to '
      u'separate live quotes from cached ones. A second, independent board agrees on direction: 24/7&nbsp;Wall&nbsp;St.&rsquo;s index strip, '
      u'read minutes earlier, showed the S&amp;P 500 off 0.07%, the Dow up 0.24%, the Nasdaq&nbsp;100 off 0.63% and the Russell&nbsp;2000 off 0.56%. '
      u'The Motley Fool&rsquo;s own 11:37 a.m. ET snapshot &mdash; Dow +0.27%, S&amp;P 500 ' + M + u'0.23%, Nasdaq Composite ' + M + u'0.44% &mdash; brackets '
      u'the same picture 90 minutes earlier. The cause of the chip weakness is no longer a mystery. 24/7&nbsp;Wall&nbsp;St. reported at '
      u'11:29 a.m. ET that memory stocks slid on weekend reports Washington may permit Apple to source DRAM from China&rsquo;s ChangXin Memory '
      u'Technologies (CXMT) and NAND flash from Yangtze Memory Technologies (YMTC), described as a possible diplomatic gesture ahead of President '
      u'Xi Jinping&rsquo;s planned US visit, expected on or around September&nbsp;24. <b>No policy decision has been announced.</b> The tape traded it '
      u'as if one had: SanDisk down 9%, Micron down 7%, Western Digital down 7%, SK Hynix down 5% and the Roundhill Memory ETF down 7% in that '
      u'11:29 a.m. read, the uniformity across NAND and DRAM names the tell that this is a policy-headline shock rather than a fundamental '
      u're-rating. Those losses have since narrowed: 24/7&rsquo;s live top-losers board at this edition had Micron down 5.13% at $917.23, Seagate '
      u'down 5.64% at $802.10, Western Digital down 5.06% at $436.19, J.B.&nbsp;Hunt down 5.16% and Coterra Energy the single worst name on the '
      u'board at ' + M + u'8.62%. The session&rsquo;s biggest identified decliner is elsewhere: The Motley Fool has <b>Applied Optoelectronics down 11% '
      u'this morning</b> after the company announced a $600&nbsp;million equity offering. Precise intraday index levels are again withheld from this '
      u'editorial &mdash; two market bars fetched this run were cached at earlier prints this desk has already published and superseded &mdash; and only '
      u'percentage moves are asserted. The official closes sit in the Weekly Scorecard below; the live widgets at the top of this page carry the real-time tape.</p>')
    w = w[:i] + NEW_P1 + w[j+4:]

ANCHOR2 = u'<p>The damage was done overnight.'
NEWP2 = (u'<p>The event risk is on the podium, not the tape. Treasury Secretary Scott Bessent holds his press conference detailing the '
  u'new Iran sanctions package at <b>1 p.m. ET</b> at the Treasury Building &mdash; the time and venue fixed by CBS News&rsquo;s &ldquo;how to watch&rdquo; box '
  u'&mdash; unveiling what The Washington Post describes as a wider range of secondary sanctions on countries and entities doing business with Iran, '
  u'aimed at pressuring Tehran to reopen the Strait of Hormuz. Bessent trailed the package in a <em>Financial Times</em> op-ed as &ldquo;an economic D-Day '
  u'&mdash; the single greatest financial offensive ever marshaled against an adversary,&rdquo; and criticised China last week for historically buying about '
  u'90% of Iran&rsquo;s oil. CNBC reported ahead of the conference that Iran is warning of ship seizures in the Strait of Hormuz. The second, quieter fight is '
  u'over the long end of the curve: 24/7&nbsp;Wall&nbsp;St. published at 11:37 a.m. ET that Treasury officials indicated the department is considering drawing '
  u'on its Treasury General Account &mdash; which was approaching $1&nbsp;trillion &mdash; to fund expanded buybacks, and argued the usable buffer is realistically '
  u'$100&nbsp;billion to $200&nbsp;billion rather than the headline figure. The 10-year yield was down four basis points at 4.69% on The Motley Fool&rsquo;s '
  u'11:37 a.m. read, but the pattern of the past week is that relief does not stick. ' + ANCHOR2)
w = rep(w, ANCHOR2, NEWP2, "ws-lead-p2")

# --- drop last edition's two New tags ---
w = rep(w,
 u'<div class="tags"><span class="tag down">SNDK ' + M + u'9%</span><span class="tag">Apple / CXMT / YMTC</span><span class="tag new">New</span></div>',
 u'<div class="tags"><span class="tag down">SNDK ' + M + u'9%</span><span class="tag">Apple / CXMT / YMTC</span></div>',
 "ws-drop-new-1")
w = rep(w,
 u'<div class="tags"><span class="tag down">F, STLA ' + M + u'4%</span><span class="tag">Auto tariffs</span><span class="tag new">New</span></div>',
 u'<div class="tags"><span class="tag down">F, STLA ' + M + u'4%</span><span class="tag">Auto tariffs</span></div>',
 "ws-drop-new-2")
w = rep(w,
 u'<h3>Washington may let Apple buy Chinese memory &mdash; and the whole complex gapped down on it</h3>\n<p><b>New this edition.</b> Weekend reports',
 u'<h3>Washington may let Apple buy Chinese memory &mdash; and the whole complex gapped down on it</h3>\n<p>Weekend reports',
 "ws-drop-newtext-1")
w = rep(w,
 u'<h3>Detroit takes the other side of the tariff trade</h3>\n<p><b>New this edition.</b> Ford and Stellantis',
 u'<h3>Detroit takes the other side of the tariff trade</h3>\n<p>Ford and Stellantis',
 "ws-drop-newtext-2")

# --- two NEW cards at the top of the movers grid ---
ANCH = u'<div class="cards">\n\n<div class="card">\n<div class="tags"><span class="tag up">10Y ' + M + u'4bp</span>'
NEWCARDS = (u'<div class="cards">\n\n'
 u'<div class="card">\n'
 u'<div class="tags"><span class="tag down">MRNA ' + M + u'7%</span><span class="tag">Profit-taking</span><span class="tag new">New</span></div>\n'
 u'<h3>Moderna gives back part of a 392% year</h3>\n'
 u'<p><b>New this edition.</b> Moderna sank 7% on Monday as traders booked profits on a 392% year-to-date surge, with BioNTech down 4% and Merck slipping alongside it, per 24/7&nbsp;Wall&nbsp;St.&rsquo;s Monday coverage. It is the same trade running in reverse across the market&rsquo;s biggest 2026 winners: names that have tripled or better on the year are the ones being sold into an event-heavy week, exactly as SanDisk (+572% year to date through Friday&rsquo;s close) and Micron (+239%) are on the memory side. No company-specific catalyst is attached to the move in the reporting &mdash; no data readout, no guidance change, no regulatory action.</p>\n'
 u'</div>\n\n'
 u'<div class="card">\n'
 u'<div class="tags"><span class="tag down">Drones, quantum</span><span class="tag">Risk appetite</span><span class="tag new">New</span></div>\n'
 u'<h3>The speculative complexes are unwinding together</h3>\n'
 u'<p><b>New this edition.</b> The de-risking ahead of Nvidia is not confined to memory. 24/7&nbsp;Wall&nbsp;St. logged three separate speculative pockets selling off on Monday: drone names, with Unusual Machines down 9%, Red Cat down 7% and Ondas down 5% as risk appetite faded; quantum-computing names unwinding a revenue-headline rally, with Rigetti Computing and Infleqtion each down 7% and IonQ down 6%; and critical-minerals names, where USA Rare Earth fell 5% <em>despite</em> $1.55&nbsp;billion of government-backed funding and United States Antimony dropped 9%. Read alongside the memory unwind and the Moderna reversal, the common factor is not a sector thesis but a positioning one: the highest-beta, highest-momentum cohorts are the ones being trimmed into Wednesday&rsquo;s earnings print and Friday&rsquo;s Jackson Hole keynote.</p>\n'
 u'</div>\n\n'
 u'<div class="card">\n<div class="tags"><span class="tag up">10Y ' + M + u'4bp</span>')
w = rep(w, ANCH, NEWCARDS, "ws-newcards")

# --- upgrade the TGA card ---
w = rep(w,
 u'The next test is Friday, when Fed Chair Kevin Warsh gives his first Jackson Hole keynote and may be pressed on how he sees the Fed&rsquo;s relationship with the Treasury and the bond market.</p>',
 u'The next test is Friday, when Fed Chair Kevin Warsh gives his first Jackson Hole keynote and may be pressed on how he sees the Fed&rsquo;s relationship with the Treasury and the bond market.</p>\n'
 u'<p><b>Refreshed at this edition.</b> 24/7&nbsp;Wall&nbsp;St., publishing at 11:37 a.m. ET, puts a sharper edge on the arithmetic: much of the General Account is already spoken for, and the realistically usable buffer is more like <b>$100&nbsp;billion to $200&nbsp;billion</b> &mdash; close to the scale Treasury itself modelled in 2025, when its own analysis showed even a $120&nbsp;billion annual buyback programme would move the roughly six-year weighted-average maturity of marketable debt by only a few weeks. The recent track record supports the scepticism. The 30-year yield fell nearly 10 basis points on August&nbsp;19 to 5.187%, after touching 5.337% the day before &mdash; its highest since 2007 &mdash; and the 10-year fell to 4.651%; by August&nbsp;20 the 10-year had climbed 4.7 basis points back to 4.70% and the 30-year had returned to 5.247%. The buyback expansion itself runs from <b>September&nbsp;9 through the November&nbsp;4 quarterly refunding</b> and targets older, less-liquid off-the-run securities for market functioning, not debt reduction. Treasury had already raised long-end buyback frequency from two operations a quarter to four in 2025, lifting the maximum liquidity-support programme from $30&nbsp;billion to $38&nbsp;billion per quarter. The framing 24/7 lands on: this is liquidity support, not quantitative easing, and not a fix for the fiscal arithmetic underneath it.</p>',
 "ws-tga-upgrade")

# --- chart of the day: SNDK -> AAOI ---
w = rep(w, u'<div class="lab">Chart of the day — SanDisk (SNDK)</div>',
        u'<div class="lab">Chart of the day — Applied Optoelectronics (AAOI)</div>', "ws-cotd-lab")
w = rep(w, u'{"symbol":"NASDAQ:SNDK","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}',
        u'{"symbol":"NASDAQ:AAOI","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}', "ws-cotd-widget")
old = cut(w, u'<div class="note">The chart moves to SanDisk this edition', "ws-cotd-note-anchor")
if old:
    w = rep(w, old,
     u'<div class="note">The chart moves back to Applied Optoelectronics this edition, and this time with a live source and a named cause. The Motley Fool&rsquo;s midday report, published 12:15&nbsp;p.m. ET and timestamped &ldquo;as of 11:37 a.m. ET,&rdquo; states plainly that Applied Optoelectronics <b>plunged 11% this morning after announcing a $600&nbsp;million equity offering</b> &mdash; the largest single-name decline attached to a stated cause anywhere in this edition, larger than the worst name on 24/7&rsquo;s live losers board (Coterra Energy, ' + M + u'8.62%) and larger than the lead story&rsquo;s biggest memory decliner (SanDisk, ' + M + u'9% at 11:29&nbsp;a.m.). The previous edition parked this slot on SanDisk specifically because AAOI&rsquo;s only readings then came from page bars this desk had date-stamped as cached; that objection no longer applies. The dilution is the story rather than the fundamentals: the company posted record second-quarter revenue of $191.9&nbsp;million on a 140% surge in data-centre sales and a swing to non-GAAP profitability, and this is its third large-scale equity financing of 2026 after a $500&nbsp;million raise in April and a $600&nbsp;million ATM programme in May.</div>',
     "ws-cotd-note")

# --- sector heat note ---
old = cut(w, u'<div class="note">Semiconductors, memory and storage are the identifiable drag', "ws-sector-anchor")
if old:
    w = rep(w, old,
     u'<div class="note"><b>Sector read refreshed this edition.</b> The Motley Fool&rsquo;s midday report, as of 11:37&nbsp;a.m. ET, has <b>communication services and financials leading the sector gainers</b>, against <b>technology, energy and industrials lagging</b>. That supersedes the &ldquo;energy is the day&rsquo;s best performer&rdquo; line carried in earlier editions, which this desk now assesses as Friday&rsquo;s session rather than Monday&rsquo;s and has withdrawn. The split is the whole session in one line: the Dow is up because the money leaving semiconductors is rotating into blue chips, not out of the market. Semiconductors, memory and storage remain the identifiable drag &mdash; Investing.com named Sandisk, Seagate, Coherent, Marvell, AMD and Intel among the decliners, with Samsung and Alibaba leading the overnight Asian rout, and Trading Economics put Micron, Marvell and SanDisk in a 6%-to-10% decline band. In Europe, the Stoxx 600 opened 0.1% lower with technology down 0.78% while travel, miners and food and beverage each rose about 0.4%. The megacap tape splits the same way: on The Motley Fool&rsquo;s live board read at this edition, Alphabet was up 1.6%, Amazon up 1.5%, Microsoft up 1.2%, Meta up 1.0% and Apple up 0.7%, while Nvidia was off 1.9% and Tesla off 1.7%. Volatility is bid &mdash; the VIX read 15.89, up 0.76, on both the Yahoo Finance market bar and Trading Economics earlier this run. The live heatmap above carries the full sector picture.</div>',
     "ws-sector-note")

# --- rates table ---
w = rep(w, u'<tr><td>US 10-year Treasury yield</td><td>4.70%</td><td class="down">' + M + u'4 bp on CNBC&rsquo;s midday read,',
        u'<tr><td>US 10-year Treasury yield</td><td>4.69%</td><td class="down">' + M + u'4 bp (' + M + u'0.04) on The Motley Fool&rsquo;s 11:37&nbsp;a.m. ET read at this edition, corroborating CNBC&rsquo;s earlier midday read of 4.70%, also ' + M + u'4 bp,', "ws-10y")
w = rep(w, u'<tr><td>Gold</td><td>$4,723.70</td><td class="up">+43.10 (+0.92%)</td></tr>',
        u'<tr><td>Gold</td><td>$4,671.09</td><td class="up">+1.20% on The Motley Fool&rsquo;s 11:37&nbsp;a.m. ET read at this edition. Earlier reads this run had $4,731.50 (+1.09%) and $4,723.70 (+0.92%) on the Yahoo market bar; the readings differ by source and time, so the freshest attributed one is carried here.</td></tr>', "ws-gold")
w = rep(w, u'<tr><td>Bitcoin</td><td>$79,111.23</td><td class="up">+1,930.77 (+2.50%)</td></tr>',
        u'<tr><td>Bitcoin</td><td>$79,716.00</td><td class="up">+2,434.18 (+3.1%) on The Motley Fool&rsquo;s live board read at this edition.</td></tr>', "ws-btc")

# --- on the radar ---
w = rep(w, u'<li><b>Monday, August 24 — Bessent&rsquo;s Iran press conference.</b> The Treasury Secretary details new US economic sanctions on Iran at a press conference at <b>1 p.m. ET</b> today,',
        u'<li><b>Monday, August 24 — Bessent&rsquo;s Iran press conference.</b> The Treasury Secretary details new US economic sanctions on Iran at a press conference beginning at <b>1 p.m. ET</b> today at the Treasury Building &mdash; a wider set of secondary sanctions on countries and entities transacting with Tehran, per The Washington Post, NPR and CBS News, with Iran warning of ship seizures in the Strait of Hormuz ahead of it, per CNBC &mdash;', "ws-radar-1")

# --- sources ---
w = rep(w, u'<li>Yahoo Finance — Stock market today: Dow, S&amp;P 500, Nasdaq futures mixed after US-Canada talks break down (Aug 24, 2026, 4:03 AM ET)',
 u'<li>The Motley Fool — Stock Market Midday, Aug. 24: Dow Edges Higher as Chip Weakness Pressures Nasdaq (published Aug 24, 2026, 12:15 PM ET; figures as of 11:37 AM ET; live index board read this run) — https://www.fool.com/coverage/stock-market-today/2026/08/24/stock-market-midday-aug-24-dow-edges-higher-as-chip-weakness-pressures-nasdaq/</li>\n'
 u'<li>24/7 Wall St. — Scott Bessent&rsquo;s $1 Trillion Bond Market Fight: Treasury Yields Aren&rsquo;t Buying It (Aug 24, 2026, 11:37 AM ET; index strip and live top-losers board read this run) — https://247wallst.com/investing/2026/08/24/scott-bessents-1-trillion-bond-market-fight-treasury-yields-arent-buying-it/</li>\n'
 u'<li>24/7 Wall St. — Memory Stocks Slide on Report Apple May Source Chinese Chips: SanDisk Down 9%, Micron and Western Digital Down 7% (Aug 24, 2026, 11:29 AM ET) — https://247wallst.com/investing/2026/08/24/memory-stocks-slide-on-report-apple-may-source-chinese-chips-sandisk-down-9-micron-and-western-digital-down-7/</li>\n'
 u'<li>24/7 Wall St. — Moderna Sinks 7% as Traders Book Profits on a 392% Year-to-Date Surge; BioNTech Drops 4%, Merck Slips (Aug 24, 2026) — https://247wallst.com/investing/2026/08/24/moderna-sinks-7-as-traders-book-profits-on-a-392-year-to-date-surge-biontech-drops-4-merck-slips/</li>\n'
 u'<li>24/7 Wall St. — Drone Stocks Slide as Risk Appetite Fades: Unusual Machines Tumbles 9%, Red Cat Falls 7%, Ondas Declines 5% (Aug 24, 2026) — https://247wallst.com/investing/2026/08/24/drone-stocks-slide-as-risk-appetite-fades-unusual-machines-tumbles-9-red-cat-falls-7-ondas-declines-5/</li>\n'
 u'<li>24/7 Wall St. — Quantum Stocks Unwind a Revenue-Headline Rally: Rigetti Computing and Infleqtion Down 7%, IonQ Down 6% (Aug 24, 2026) — https://247wallst.com/investing/2026/08/24/quantum-stocks-unwind-a-revenue-headline-rally-rigetti-computing-and-infleqtion-down-7-ionq-down-6/</li>\n'
 u'<li>24/7 Wall St. — USA Rare Earth Falls 5% Despite $1.55B Government-Backed Funding, United States Antimony Drops 9% (Aug 24, 2026) — https://247wallst.com/investing/2026/08/24/usa-rare-earth-falls-5-despite-1-55b-government-backed-funding-united-states-antimony-drops-9/</li>\n'
 u'<li>The Washington Post — Bessent to unveil &lsquo;economic D-Day&rsquo; sanctions against Iran (Aug 24, 2026) — https://www.washingtonpost.com/business/2026/08/24/bessent-unveil-economic-d-day-sanctions-against-iran/</li>\n'
 u'<li>CNBC — Iran warns of Hormuz ship seizures ahead of Bessent&rsquo;s planned sanctions push (Aug 24, 2026) — https://www.cnbc.com/2026/08/24/us-iran-war-trump-hormuz-bessent-economic-sanctions-.html</li>\n'
 u'<li>NPR — Treasury Secretary Scott Bessent to unveil new economic sanctions on Iran (Aug 24, 2026) — https://www.npr.org/2026/08/24/g-s1-139743/treasury-secretary-scott-bessent-to-unveil-new-economic-sanctions-on-iran</li>\n'
 u'<li>Yahoo Finance — Stock market today: Dow, S&amp;P 500, Nasdaq futures mixed after US-Canada talks break down (Aug 24, 2026, 4:03 AM ET)', "ws-sources")
save("wallstreet-briefing.html", w)

# ============================== CYBER ==============================
c = load("cyber-briefing.html")

c = rep(c,
 u'<div class="tldr"><b>The Wire</b> <span>Iran-linked hackers took a British power plant offline for four days in the first cyberattack known to have halted a UK generating station &mdash; and the Treasury Secretary details the US sanctions response at 1 p.m. ET today &mdash; while CISA&rsquo;s remediation deadline for an actively exploited Zimbra command-injection flaw falls today and eight other Known Exploited Vulnerabilities entries tracked here are already past due.</span></div>',
 u'<div class="tldr"><b>The Wire</b> <span>Iran-linked hackers took a British power plant offline for four days in the first cyberattack known to have halted a UK generating station &mdash; the Treasury Secretary details the US sanctions response at 1 p.m. ET as this edition publishes &mdash; while CISA&rsquo;s remediation deadline for an actively exploited Zimbra command-injection flaw falls today, eight other Known Exploited Vulnerabilities entries tracked here are already past due, and a maximum-severity SAP Commerce Cloud flaw is drawing exploitation attempts against honeypots.</span></div>',
 "cy-tldr")

c = rep(c, u'<div class="stat"><div class="n">23</div><div class="l">Critical CVEs (9.0+) logged today</div></div>',
           u'<div class="stat"><div class="n">10.0</div><div class="l">CVSS of the SAP Commerce Cloud flaw drawing exploit attempts</div></div>', "cy-stat")

c = rep(c, u'<div class="tags"><span class="tag">Apple</span><span class="tag">4 &times; CVSS 9.8</span><span class="tag new">New</span></div>',
           u'<div class="tags"><span class="tag">Apple</span><span class="tag">4 &times; CVSS 9.8</span></div>', "cy-drop-new")
c = rep(c, u'<h3>Apple is today&rsquo;s largest single cluster of critical disclosures</h3>\n<p><b>New this edition.</b> CVE Brief&rsquo;s August 24 daily digest',
           u'<h3>Apple is today&rsquo;s largest single cluster of critical disclosures</h3>\n<p>CVE Brief&rsquo;s August 24 daily digest', "cy-drop-newtext")

# --- new cyber cards, inserted before the TikTok card ---
TIK = u'<div class="card">\n<div class="tags"><span class="tag">Regulation</span></div>\n<h3>TikTok to pay $400 million over US child-privacy claims</h3>'
NEWCY = (u'<div class="card">\n'
 u'<div class="tags"><span class="tag crit">CVSS 10.0</span><span class="tag">SAP Commerce Cloud</span><span class="tag new">New</span></div>\n'
 u'<h3>A maximum-severity SAP flaw is being probed &mdash; three days after the patch shipped</h3>\n'
 u'<p><b>New this edition.</b> <b>CVE-2026-58231</b> carries the maximum CVSS score of <b>10.0</b> and sits in SAP Commerce Cloud. Per CVE.org, &ldquo;SAP Commerce Cloud allows an unauthenticated attacker to abuse a default authentication client and submit specially crafted input to certain functions lacking sufficient validation,&rdquo; with successful exploitation enabling arbitrary code execution and compromise of internal components &mdash; high impact on confidentiality, integrity and availability. SAP patched it on <b>August 11</b>. Threat-intelligence firm Defused Cyber told The Hacker News that exploitation attempts began hitting its honeypots merely <b>three days after the patch</b>, and KEVIntel independently confirmed two attempts detected on <b>August 14</b> from a single IP address located in the United States.</p>\n'
 u'<p>SAP security firm Onapsis recommends customers patch to the fixed Commerce Cloud release levels and re-build and re-deploy, and offers a temporary mitigation: configure an IP Filter Set in SAP Commerce Cloud to restrict access to the vulnerable endpoint. Nobody has been publicly attributed to the activity, though prior SAP flaws &mdash; CVE-2025-31324 in NetWeaver &mdash; were weaponised by China-nexus espionage clusters including UNC5221, UNC5174 and CL-STA-0048, and by the BianLian and RansomExx cybercrime groups.</p>\n'
 u'<p class="note">Stated precisely, because the sourcing is nuanced: what is confirmed is <em>exploitation attempts</em> against honeypot and sensor infrastructure. Defused Cyber said in the same post that the vulnerability &ldquo;has no public PoC and is not known to be exploited,&rdquo; and CVE-2026-58231 does <b>not</b> appear in the CISA KEV catalog as of this edition, so it carries no federal remediation deadline. It is listed here as a maximum-severity flaw under active probing, not as a confirmed in-the-wild compromise.</p>\n'
 u'</div>\n\n'
 u'<div class="card">\n'
 u'<div class="tags"><span class="tag">Finance</span><span class="tag">Social engineering</span><span class="tag new">New</span></div>\n'
 u'<h3>Apollo Global says a social-engineering intrusion reached Social Security numbers</h3>\n'
 u'<p><b>New this edition.</b> Apollo Global Management disclosed that attackers breached its systems in July and accessed personal information, in what the firm describes as a social-engineering incident &mdash; manipulating people rather than exploiting a bug &mdash; to reach data held in Apollo&rsquo;s cloud. The investigation found unauthorised access to certain cloud platforms between <b>July 6 and July 10</b>. Apollo says it learned on <b>August 12</b> that the potentially affected information included names, dates of birth, contact information, home addresses and <b>Social Security numbers</b>. Notification letters to affected individuals are dated <b>August 21</b>. The firm notified law enforcement and engaged outside cybersecurity and forensic experts.</p>\n'
 u'<p>Bloomberg placed the disclosure in a run of attempted or successful cyberattacks against major hedge funds and alternative-asset managers in recent weeks. The pattern is the one running through several items on this page: the initial access is human, not technical, and the exposure sits in a cloud tenancy rather than on a server anyone owns.</p>\n'
 u'</div>\n\n' + TIK)
c = rep(c, TIK, NEWCY, "cy-newcards")

# --- vulnerability watch row for SAP ---
VROW = u'<tr><td>CVE-2026-18963</td><td>9.1</td><td>Keycloak;'
c = rep(c, VROW,
 u'<tr><td>CVE-2026-58231</td><td>10.0</td><td>SAP Commerce Cloud; patched August 11, 2026 &mdash; customers must move to the fixed release levels and re-build/re-deploy</td><td>Insufficient authorisation checks and input validation. An unauthenticated attacker can abuse a default authentication client and submit crafted input to functions lacking sufficient validation, reaching arbitrary code execution and compromise of internal components. Defused Cyber recorded exploitation attempts against its honeypots three days after the patch, and KEVIntel confirmed two attempts on August 14 from a single US IP. <b>Defused Cyber states there is no public PoC and the flaw is not known to be exploited in real-world compromises</b>; it is not a KEV entry and carries no federal deadline. Onapsis mitigation: an IP Filter Set restricting access to the vulnerable endpoint.</td></tr>\n\n' + VROW,
 "cy-vulnrow")

# --- sources ---
CYSRC = u'<div class="lab">Sources</div>\n<ul>'
c = rep(c, CYSRC, CYSRC + u'\n'
 u'<li>The Hacker News — SAP Commerce Cloud CVE-2026-58231 Targeted in Exploitation Attempts Days After Patch (Aug 15, 2026; fetched in full this run) — https://thehackernews.com/2026/08/sap-commerce-cloud-cve-2026-58231.html</li>\n'
 u'<li>SecurityWeek — Iran-Linked Hackers Shut Down UK Power Plant for Four Days (Aug 24, 2026, 5:22 AM ET; fetched in full this run) — https://www.securityweek.com/iran-linked-hackers-shut-down-uk-power-plant-for-four-days/</li>\n'
 u'<li>Bloomberg — Apollo Reports Data Breach From &lsquo;Social Engineering Incident&rsquo; (Aug 21, 2026) — https://www.bloomberg.com/news/articles/2026-08-21/apollo-reports-data-breach-from-social-engineering-incident</li>\n'
 u'<li>Insurance Journal — Apollo Global Reveals Data Breach After Hackers Target Financial Firms (Aug 21, 2026) — https://www.insurancejournal.com/news/national/2026/08/21/882462.htm</li>\n'
 u'<li>CISA — Adds One Known Exploited Vulnerability to Catalog (Aug 21, 2026; CVE-2026-73570, Zimbra; re-verified this run) — https://www.cisa.gov/news-events/alerts/2026/08/21/cisa-adds-one-known-exploited-vulnerability-catalog</li>\n'
 u'<li>CISA — Known Exploited Vulnerabilities Catalog — https://www.cisa.gov/known-exploited-vulnerabilities-catalog</li>', "cy-sources")
save("cyber-briefing.html", c)

print("\n".join(FAIL) if FAIL else "ALL EDITS OK")
