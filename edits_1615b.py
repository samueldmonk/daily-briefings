#!/usr/bin/env python3
# Post-close edition, Wed Aug 26 2026 ~4:15pm ET. Incremental edits to the 3:50 pages.
import re, sys, io

OUT = "/sessions/lucid-sleepy-wright/mnt/outputs/"
fails = []

def rd(f):
    return io.open(OUT + f, encoding="utf-8").read()

def wr(f, h):
    io.open(OUT + f, "w", encoding="utf-8").write(h)

def sub1(h, old, new, tag):
    if h.count(old) != 1:
        fails.append("ANCHOR %s count=%d" % (tag, h.count(old)))
        return h
    return h.replace(old, new, 1)

def demote(h):
    """Demote every prior-edition New marker: class AND label."""
    h = h.replace('<span class="tag new">New &middot; 3:50</span>', '<span class="tag">3:50</span>')
    h = h.replace('<span class="tag new">New &middot; 3:05</span>', '<span class="tag">3:05</span>')
    h = h.replace('New at 3:50', 'Carried from the 3:50 edition')
    h = h.replace('New at 3:05', 'Carried from the 3:05 edition')
    h = h.replace('&#9679; New &middot; 3:50 &mdash;', '&#9679; Carried from the 3:50 edition &mdash;')
    return h

# ────────────────────────────── WALL STREET ──────────────────────────────
w = rd("wallstreet-briefing.html")
w = demote(w)

# 1. TLDR — post-close
old_tldr = re.search(r'<div class="tldr"><b>The Tape</b> <span>.*?</span></div>', w, re.S)
if not old_tldr:
    fails.append("WS tldr anchor")
else:
    w = w.replace(old_tldr.group(0),
      '<div class="tldr"><b>The Tape</b> <span>The session is over and it finished almost exactly where it '
      'started &mdash; <b>the S&amp;P&nbsp;500 closed at 7,675.70, down 1.58 points, &minus;0.02%</b>, with the '
      '<b>Dow off about 0.2%</b> and the <b>Nasdaq Composite down about 0.08%</b> &mdash; leaving the day&rsquo;s '
      'actual event to the after-hours tape, where <b>Nvidia&rsquo;s Q2&nbsp;FY2027 report</b> lands with roughly '
      '<b>$282&nbsp;billion of market value in play</b> on the options-implied move; <b>&#9888; the one source that '
      'appeared to have the close and the Nvidia reaction already turned out to be an August&nbsp;2024 story, and '
      'none of it is published.</b></span></div>', 1)

# 2. Lead — three new paragraphs at the top of .lead
lead_anchor = '<div class="lab">The lead</div>\n<div class="lead">\n'
NEWLEAD = (
  '<p><b>&#9679; New &middot; 4:15 &mdash; the close, and the prior-close arithmetic that has now survived six '
  'independent boards.</b> The <b>S&amp;P&nbsp;500 closed at 7,675.70, &minus;1.58, &minus;0.02%</b> on the Yahoo '
  'Finance read fetched this run; a second summary this run gives <b>7,675.82, &minus;1.46, &minus;0.02%</b>. '
  '<b>Both subtract to exactly 7,677.28</b> &mdash; the Tuesday close this desk adopted at 2:44 over the '
  '<b>7,677.24</b> Zacks printed, now corroborated a fifth and sixth time. <b>The twelve-cent gap between the two '
  'closing reads is printed, not smoothed, and no S&amp;P closing level is asserted to the cent.</b> Alongside it: '
  'the <b>Dow declined about 0.2%</b>, the <b>Nasdaq Composite slipped about 0.08%</b>, and <b>NVDA closed down '
  '1.59%</b> walking into its own print. Set against the day&rsquo;s earlier boards the shape is now complete &mdash; '
  '<b>green at 9:59</b> (the only all-green reading all day), <b>worst at 12:29</b>, <b>clawing back by 1:24</b>, '
  '<b>flat at the bell</b>.</p>\n'
  '<p><b>&#9679; New &middot; 4:15 &mdash; &#9888; THE TRAP OF THE DAY: a &ldquo;close&rdquo; that is two years old.</b> '
  'A Barchart story surfaced this run under the headline <b>&ldquo;Stocks Close in the Red, Nvidia Trades Lower After '
  'Earnings Report&rdquo;</b>, with a meta-description reading <b>&ldquo;The Nasdaq&nbsp;100 fell to a 2-week low on '
  'Wednesday&rdquo;</b> ahead of Nvidia &mdash; and it carried a full set of numbers: <b>S&amp;P&nbsp;500 &minus;0.60%, '
  'Dow &minus;0.39%, Nasdaq&nbsp;100 &minus;1.18%</b>, plus an after-hours line that <b>Nvidia&rsquo;s revenue rose '
  '122% year over year and the stock fell 7%</b>. Fetched in full, the body dates itself: Super Micro Computer '
  '<b>&ldquo;closed down more than &minus;19% &hellip; after it said it would delay filing its Annual Report on Form '
  '10-K for the fiscal year ended June&nbsp;30, 2024&rdquo;</b>; Foot Locker <b>&ldquo;cutting its 2025 gross margin '
  'forecast&rdquo;</b>; and the next-morning earnings list names <b>Catalent</b> and <b>HashiCorp</b>. <b>This is an '
  'August&nbsp;2024 article, matched to today because both Wednesdays are the day of an Nvidia print.</b> '
  '<b>NONE of it publishes</b> &mdash; not the index moves, not the &plus;122%, not the &minus;7%.</p>\n'
  '<p><b>&#9679; New &middot; 4:15 &mdash; and the Tuesday-as-Wednesday relabel returns twice more.</b> Two separate '
  'search summaries this run handed back <b>7,677.24 / 53,577.40 &plus;160.24 / 26,151.30 &plus;171.11</b> as '
  '&ldquo;the August&nbsp;26 close.&rdquo; Those are <b>Tuesday&rsquo;s</b> closes, and the S&amp;P figure is '
  'additionally the rejected Zacks variant. <b>Third and fourth occurrences of this relabel today; rejected again.</b> '
  'The Yahoo live blog for Wednesday was also re-fetched and is <b>still served from its ~4:18&nbsp;a.m. cache</b> '
  '(&ldquo;U.S. markets open in 5h 4m&rdquo;), so its trending strip and futures board are <b>not</b> a post-close '
  'reading either.</p>\n')
w = sub1(w, lead_anchor, lead_anchor + NEWLEAD, "WS lead")

# 3. Movers — three new cards at the top
mov_anchor = '<div class="lab">Movers &amp; drivers</div>\n<div class="cards">\n'
NEWCARDS = (
  '<div class="card"><div class="tags"><span class="tag new">New &middot; 4:15</span><span class="tag">Earnings</span>'
  '<span class="tag">Estimates only</span></div>\n'
  '<h3>Nvidia after the bell &mdash; what is an expectation and what is a result</h3>\n'
  '<p>Nvidia released its <b>fiscal second-quarter 2027</b> results <b>after the U.S. market closed on Wednesday, '
  'August&nbsp;26</b>, with the earnings call <b>later that evening</b>. Going in, <b>Visible Alpha</b> had '
  '<b>$92.16&nbsp;billion in revenue, $2.09 in adjusted EPS and $85.67&nbsp;billion in Data Center revenue</b>; '
  '<b>forty-one analysts</b> had <b>$92.07&nbsp;billion and $2.09</b>; Data Center estimates ranged '
  '<b>$83.5&nbsp;billion to $91.5&nbsp;billion</b>; and the company&rsquo;s own guide was <b>$91.0&nbsp;billion plus '
  'or minus two percent</b>. For scale, the year-ago quarter did <b>$46.74&nbsp;billion and $1.05</b> &mdash; both '
  'figures roughly half. <b>&#9888; Every number in this card is an estimate or a company guide. No result is '
  'asserted, and none was available to this desk at the time of writing.</b></p></div> '
  '<div class="card"><div class="tags"><span class="tag new">New &middot; 4:15</span><span class="tag">Options</span>'
  '<span class="tag">$282B in play</span></div>\n'
  '<h3>The options market has already priced the move, and those numbers are sourced</h3>\n'
  '<p>Benzinga puts Nvidia&rsquo;s implied volatility into the print at <b>13.26%</b> against roughly '
  '<b>$5.26&nbsp;trillion</b> of market value &mdash; about <b>$282&nbsp;billion of market cap in play</b>. '
  '<b>&#9888; A second Benzinga headline from the same day puts the swing at $286&nbsp;billion; both are printed, '
  'neither is merged.</b> <b>CrowdStrike</b> is priced for a <b>7.59% move</b> on a <b>$196&nbsp;billion</b> market '
  'cap &mdash; roughly <b>$14.9&nbsp;billion</b> of value at stake. On sell-side positioning into the same night: '
  '<b>Salesforce 73% bullish / 4% bearish</b>, <b>CrowdStrike 77% bullish / 2% bearish</b>. Options on '
  '<b>Okta, Kohl&rsquo;s and Abercrombie &amp; Fitch</b> are named in the same screen.</p></div> '
  '<div class="card"><div class="tags"><span class="tag new">New &middot; 4:15</span><span class="tag">&minus;1.59%</span>'
  '<span class="tag">NVDA</span></div>\n'
  '<h3>Nvidia itself went into the print red</h3>\n'
  '<p>The same post-close read that gives the S&amp;P at <b>7,675.70</b> has <b>NVDA down 1.59%</b> on the session, '
  'with the <b>Nasdaq off 0.08%</b> around it. That is the whole of the day&rsquo;s single-name story that this desk '
  'can source at the bell: <b>the chip complex sold modestly into the event and left the verdict to the tape after '
  '4&nbsp;p.m.</b> <b>&#9888; The larger single-name moves circulating this run &mdash; a &minus;19% Super Micro and a '
  '&minus;7% Nvidia &mdash; belong to the August&nbsp;2024 article rejected in The Lead and are not published.</b></p>'
  '</div> ')
w = sub1(w, mov_anchor, mov_anchor + NEWCARDS, "WS movers")

# 4. After-Hours Movers section, inserted after the Live market headlines section
ah_anchor = ('<script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>'
             '{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,'
             '"displayMode":"regular","width":"100%","height":420,"locale":"en"}</script>\n</div>\n</section>\n')
AHSEC = (
  '\n<section>\n<div class="lab">After-hours movers</div>\n'
  '<p class="note"><b>&#9679; New &middot; 4:15 &mdash; the honest state of the after-hours tape.</b> '
  '<b>As of ~4:15&nbsp;p.m. ET no verified after-hours price move exists in any source this desk fetched this run.</b> '
  'Nvidia&rsquo;s release lands after the close with the call later this evening, and the wires had not yet published '
  'a reaction. <b>&#9888; The one &ldquo;after-hours&rdquo; figure that did surface &mdash; Nvidia down 7% on revenue '
  'up 122% &mdash; is from the August&nbsp;2024 Barchart story rejected in The Lead, and is not published here or '
  'anywhere on this page.</b> What follows is only what a source states.</p>\n'
  '<div class="cards">\n'
  '<div class="card"><div class="tags"><span class="tag new">New &middot; 4:15</span><span class="tag">Reporting tonight</span></div>\n'
  '<h3>The names that opened their books after this bell</h3>\n'
  '<p><b>Nvidia (NVDA)</b>, <b>CrowdStrike (CRWD)</b>, <b>Salesforce (CRM)</b>, <b>Okta (OKTA)</b>, '
  '<b>Williams-Sonoma (WSM)</b> and <b>Abercrombie &amp; Fitch (ANF)</b> all report on Wednesday, per Yahoo Finance '
  'and TheStreet; <b>Kohl&rsquo;s</b> appears in the same options screen. CNBC frames the night as '
  '<b>&ldquo;Nvidia, CrowdStrike and Salesforce face big tests tonight.&rdquo;</b></p></div> '
  '<div class="card"><div class="tags"><span class="tag new">New &middot; 4:15</span><span class="tag">Implied, not realised</span></div>\n'
  '<h3>What the market paid for the move &mdash; before it happened</h3>\n'
  '<p><b>NVDA:</b> <b>13.26%</b> implied vol, <b>~$5.26&nbsp;trillion</b> cap, <b>~$282&nbsp;billion</b> in play '
  '(a companion piece says <b>$286&nbsp;billion</b>). <b>CRWD:</b> <b>7.59%</b> implied move, <b>$196&nbsp;billion</b> '
  'cap, <b>~$14.9&nbsp;billion</b> at stake. <b>These are prices of options, not outcomes.</b></p></div>\n'
  '</div>\n</section>\n')
w = sub1(w, ah_anchor, ah_anchor + AHSEC, "WS afterhours")

# 5. Rates — one attributed 10-year line
rates_anchor = '<div class="lab">Rates, bonds &amp; commodities</div>\n'
RATENOTE = ('<p class="note"><b>&#9679; New &middot; 4:15 &mdash; a third 10-year figure, attributed and still not '
  'reconciled.</b> Trading Economics states the <b>10-year U.S. Treasury yield eased to 4.65% from the 20-month high '
  'of 4.75% reached on August&nbsp;21</b>, as lower energy prices softened near-term inflation concerns. '
  '<b>&#9888; That does not reconcile with the midday arithmetic already printed below</b> &mdash; Zacks&rsquo; '
  '4.625% Tuesday settle plus the Motley Fool&rsquo;s stated <b>&plus;0.017</b> gives <b>4.642%</b>, not 4.65% and not '
  '4.67%. <b>All three figures are printed with their sources; this desk asserts no single 10-year level.</b></p>\n')
w = sub1(w, rates_anchor, rates_anchor + RATENOTE, "WS rates")

# 6. On the radar — Jackson Hole / Warsh
radar_anchor = '<div class="lab">On the radar</div>\n'
RADARNOTE = ('<p class="note"><b>&#9679; New &middot; 4:15 &mdash; Jackson Hole is the week&rsquo;s other event.</b> '
  'Yahoo Finance reports that the <b>Jackson Hole annual gathering of Fed policymakers</b> falls this week, where '
  '<b>Chairman Kevin Warsh will deliver a speech on the central bank&rsquo;s future plans</b> &mdash; and that the PCE '
  'print arrived <b>amid angst in the bond market</b>. <b>Core PCE came in at 3.3% for July, in line with the 3.3% '
  'economists expected and unchanged from the month before.</b></p>\n')
w = sub1(w, radar_anchor, radar_anchor + RADARNOTE, "WS radar")

# 7. Sources
src_anchor = '<div class="lab">Sources</div>\n'
NEWSRC = (
  '<div><a href="https://www.cnbc.com/2026/08/26/nvidia-nvda-earnings-report-q2-2027-live-updates.html">CNBC &mdash; Nvidia Q2 FY2027 earnings live updates (Aug 26)</a></div>\n'
  '<div><a href="https://www.cnbc.com/2026/08/26/nvidia-crowdstike-and-salesforce-face-big-tests-tonight.html">CNBC &mdash; Nvidia, CrowdStrike and Salesforce face big tests tonight</a></div>\n'
  '<div><a href="https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/08/nvidia-earnings-preview-q2-2027">S&amp;P Global &mdash; Nvidia earnings preview, Q2 FY2027</a></div>\n'
  '<div><a href="https://www.benzinga.com/markets/options/26/08/61420395/nvidia-could-swing-by-286-billion-after-earnings">Benzinga &mdash; Nvidia could swing by $286 billion after earnings</a></div>\n'
  '<div><a href="https://www.benzinga.com/trading-ideas/movers/26/08/61379652/nvidia-could-swing-282-billion-in-value-after-earnings">Benzinga &mdash; Nvidia could swing $282 billion in value after earnings</a></div>\n'
  '<div><a href="https://finance.yahoo.com/markets/live/stock-market-today-wednesday-august-26-dow-sp-500-nasdaq-081834782.html">Yahoo Finance &mdash; Aug 26 live blog (served from its ~4:18 a.m. cache)</a></div>\n'
  '<div><a href="https://tradingeconomics.com/united-states/government-bond-yield">Trading Economics &mdash; US 10-year Treasury yield</a></div>\n'
  '<div><a href="https://www.barchart.com/story/news/28260060/stocks-close-lower-ahead-of-nvidia-earnings">Barchart &mdash; &#9888; REJECTED: an August 2024 story, not today&rsquo;s close</a></div>\n')
w = sub1(w, src_anchor, src_anchor + NEWSRC, "WS sources")
wr("wallstreet-briefing.html", w)

# ────────────────────────────── CYBER ──────────────────────────────
c = rd("cyber-briefing.html")
c = demote(c)

old_ct = re.search(r'<div class="tldr"><b>The Wire</b> <span>.*?</span></div>', c, re.S)
if not old_ct:
    fails.append("CY tldr anchor")
else:
    c = c.replace(old_ct.group(0),
      '<div class="tldr"><b>The Wire</b> <span>The day&rsquo;s new item is a supply-chain one: <b>OX Security has '
      'found 24 distinct malicious npm packages carrying the exact same payload</b>, a <b>fake Cloudflare Captcha</b> '
      'page that delivers <b>ClickFix</b> &mdash; the same paste-and-run technique the <b>Cruciferra</b> loader in this '
      'page&rsquo;s Threat Actor Spotlight uses, now arriving through the package registry rather than a compromised '
      'WordPress site &mdash; while <b>CISA&rsquo;s KEV catalogue is static for a thirteenth consecutive edition</b>, '
      'leaving Patch Priority unchanged at <b>Oracle CVE-2026-21962, due tomorrow</b>.</span></div>', 1)

inc_anchor = '<div class="lab">Breaches &amp; incidents</div>\n<div class="cards">\n'
CYCARD = (
  '<div class="card"><div class="tags"><span class="tag new">New &middot; 4:15</span><span class="tag">Supply chain</span>'
  '<span class="tag">npm</span><span class="tag">No CVE</span></div>\n'
  '<h3>Twenty-four npm packages, one identical ClickFix payload</h3>\n'
  '<p><b>OX Security</b> reports identifying a <b>fake Cloudflare Captcha campaign that can distribute ClickFix '
  'malware through npm</b>, and finding <b>24 distinct malicious packages sharing the exact same malicious code</b>. '
  'The significance for defenders is the delivery path rather than the payload: <b>ClickFix works by persuading a '
  'human to paste and run a command, so nothing is ever downloaded and endpoint controls see a user action</b> &mdash; '
  'and a package mirror is a far more trusted staging point than the compromised WordPress sites the '
  '<b>Cruciferra / ErrTraffic</b> operation in the Spotlight below uses for the same trick. '
  '<b>&#9888; No CVE, and this is not in CISA KEV; there is no federal deadline attached to it.</b></p></div> ')
c = sub1(c, inc_anchor, inc_anchor + CYCARD, "CY incidents")

kev_anchor = '<div class="lab">CISA KEV &amp; federal deadlines</div>\n'
KEVNOTE = (
  '<p class="note"><b>&#9679; New &middot; 4:15 &mdash; KEV static, thirteenth consecutive edition.</b> A direct '
  'search this run surfaced <b>no CISA alert page later than those already on this board</b>: the visible alert pages '
  'remain <b>Aug&nbsp;18 (four)</b>, <b>Aug&nbsp;20 (two &mdash; TrueConf Server '
  '<b>CVE-2026-72529</b> missing authentication and <b>CVE-2026-72530</b> code injection)</b> and <b>Aug&nbsp;21 '
  '(one &mdash; Zimbra Collaboration Suite OS command injection, <b>CVE-2026-73570</b>)</b>. The board holds at '
  '<b>14 rows, 10 past due</b>, and <b>Patch Priority is unchanged</b>. '
  '<b>&#9888; A search summary this run again garbled Gitea&rsquo;s CVE-2026-60004 into &ldquo;an Oracle HTTP Server '
  'and Oracle WebLogic Server Proxy Plug-in flaw&rdquo; while, in the same sentence, describing Gitea repository '
  'shell-command execution.</b> That is the identical garble rejected at 3:50 &mdash; <b>rejected again; the '
  'board&rsquo;s own description and the August&nbsp;28 deadline stand.</b></p>\n'
  '<p class="note"><b>&#9679; New &middot; 4:15 &mdash; a headline seen and deliberately not published.</b> '
  'A summary this run carried <b>&ldquo;Taco Bell and Pizza Hut operator discloses breach after suspicious network '
  'activity&rdquo;</b> as a current item. <b>Follow-up searches returned only the 2023 Yum!&nbsp;Brands ransomware '
  'incident</b> &mdash; the January&nbsp;13 attack and its notification letters &mdash; and produced <b>no 2026 body '
  'text at all</b>. <b>Nothing about it is asserted on this page.</b></p>\n')
c = sub1(c, kev_anchor, kev_anchor + KEVNOTE, "CY kev")

csrc = '<div class="lab">Sources</div>\n'
CYSRC = ('<div><a href="https://www.ox.security/blog/research-clickfix-phishing-npm-packages/">OX Security &mdash; ClickFix phishing pages discovered in 24 npm packages</a></div>\n'
         '<div><a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">CISA &mdash; Known Exploited Vulnerabilities Catalog</a></div>\n'
         '<div><a href="https://www.cisa.gov/news-events/alerts/2026/08/20/cisa-adds-two-known-exploited-vulnerabilities-catalog">CISA &mdash; Two KEV additions, Aug 20 (TrueConf)</a></div>\n'
         '<div><a href="https://www.cisa.gov/news-events/alerts/2026/08/21/cisa-adds-one-known-exploited-vulnerability-catalog">CISA &mdash; One KEV addition, Aug 21 (Zimbra)</a></div>\n')
c = sub1(c, csrc, csrc + CYSRC, "CY sources")
wr("cyber-briefing.html", c)

# ────────────────────────────── MMA ──────────────────────────────
m = rd("mma-briefing.html")
m = demote(m)

old_mt = re.search(r'<div class="tldr"><b>Tale of the Tape</b> <span>.*?</span></div>', m, re.S)
if not old_mt:
    fails.append("MMA tldr anchor")
else:
    m = m.replace(old_mt.group(0),
      '<div class="tldr"><b>Tale of the Tape</b> <span><b>UFC.com&rsquo;s own fight-by-fight preview</b> now fills in '
      'the rest of Saturday&rsquo;s <b>UFC Shanghai</b> card behind the <b>Umar Nurmagomedov &minus;500 / Song Yadong '
      '&plus;380</b> headliner: <b>Denise Gomes meets Xiaonan Yan in the co-main with strawweight title implications</b>, '
      'and the main card also carries <b>Qileng Aori vs. Kai Asakura</b> &mdash; three days out from the '
      '<b>Oriental Sports Center</b>, with the <b>champions board unchanged for a twenty-eighth consecutive '
      'edition</b>.</span></div>', 1)

fw_anchor = '<div class="lab">Fight week &mdash; upcoming cards</div>\n'
MMANOTE = (
  '<p class="note"><b>&#9679; New &middot; 4:15 &mdash; the Shanghai card below the headliner, from UFC.com itself.</b> '
  'The promotion&rsquo;s <b>fight-by-fight preview</b> confirms the <b>bantamweight bout headlines UFC Fight Night at '
  'Shanghai&rsquo;s Oriental Sports Center on August&nbsp;29</b>, framing Nurmagomedov vs. Song as a fight of '
  '<b>&ldquo;massive divisional significance&rdquo;</b> with each man trying to become <b>the clubhouse leader in the '
  'chase for the next title opportunity</b>. In the <b>co-main event, Denise Gomes meets Xiaonan Yan</b> in a bout '
  'with <b>significant strawweight title implications</b>; the main card also features <b>Qileng Aori against Kai '
  'Asakura</b>. <b>&#9888; The card had not taken place at the time of writing &mdash; no result is asserted for any '
  'bout on it.</b> Odds are unchanged from the 3:50 edition: <b>consensus Nurmagomedov &minus;500 / Song &plus;380</b>, '
  'about <b>80% / 20%</b> market-implied.</p>\n')
m = sub1(m, fw_anchor, fw_anchor + MMANOTE, "MMA fightweek")

msrc = '<div class="lab">Sources</div>\n'
MMASRC = ('<div><a href="https://www.ufc.com/news/fight-fight-preview-ufc-shanghai-umar-nurmagomedov-vs-song-yadong">UFC.com &mdash; Fight by fight preview, UFC Shanghai</a></div>\n'
          '<div><a href="https://www.ufc.com/event/ufc-fight-night-august-29-2026">UFC.com &mdash; UFC Fight Night: Nurmagomedov vs Song (Aug 29)</a></div>\n'
          '<div><a href="https://www.lowkickmma.com/umar-nurmagomedov-favourite-song-yadong-ufc-shanghai/">LowKick MMA &mdash; Nurmagomedov heavy favourite over Song</a></div>\n')
m = sub1(m, msrc, msrc + MMASRC, "MMA sources")
wr("mma-briefing.html", m)

# ────────────────────────────── INDEX ──────────────────────────────
i = rd("index.html")
def swap_card(h, cls, newtext, tag):
    mm = re.search(r'(<div class="bcard ' + cls + r'".*?<p[^>]*>)(.*?)(</p>)', h, re.S)
    if not mm:
        fails.append("IDX %s anchor" % tag)
        return h
    return h[:mm.start(2)] + newtext + h[mm.end(2):]

i = swap_card(i, "c-sec",
  'OX Security has found <b>24 distinct npm packages carrying one identical payload</b> &mdash; a fake Cloudflare '
  'Captcha page delivering <b>ClickFix</b> &mdash; while CISA&rsquo;s KEV catalogue stays static for a thirteenth '
  'consecutive edition and Patch Priority holds at <b>Oracle CVE-2026-21962, due tomorrow</b>.', "sec")
i = swap_card(i, "c-mkt",
  'The <b>S&amp;P&nbsp;500 closed at 7,675.70, &minus;1.58, &minus;0.02%</b>, with the Dow off about 0.2% and the '
  'Nasdaq about 0.08% &mdash; leaving the day to <b>Nvidia after the bell</b>, and to a &ldquo;close&rdquo; that '
  'circulated all afternoon and turned out to be from <b>August&nbsp;2024</b>.', "mkt")
i = swap_card(i, "c-mma",
  'UFC.com&rsquo;s fight-by-fight preview fills in Saturday&rsquo;s <b>UFC Shanghai</b> card behind the '
  '<b>Nurmagomedov &minus;500 / Song &plus;380</b> headliner &mdash; <b>Denise Gomes vs. Xiaonan Yan</b> in the '
  'co-main, <b>Qileng Aori vs. Kai Asakura</b> on the main card.', "mma")
wr("index.html", i)

print("FAILS:", fails if fails else "none")
