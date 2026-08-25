#!/usr/bin/env python3
# Edits for the ~5:55 PM ET Tuesday Aug 25 2026 run (tenth run of the day, Afternoon Edition).
import re, sys, io, os

D = os.path.dirname(os.path.abspath(__file__))
def rd(f):
    return io.open(os.path.join(D, f), encoding='utf-8').read()
def wr(f, c):
    io.open(os.path.join(D, f), 'w', encoding='utf-8').write(c)

FAILS = []
def rep(c, old, new, label, count=1):
    n = c.count(old)
    if n != count:
        FAILS.append('%s: expected %d occurrence(s), found %d' % (label, count, n))
        return c
    return c.replace(old, new)

# ---------------------------------------------------------------- gotcha #15
# Demote every New tag from the previous (4:45 / archive 1643) edition.
DEMOTE = re.compile(r'<span class="tag new">New[^<]*</span>')
demoted = {}
for f in ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']:
    c = rd(f)
    demoted[f] = len(DEMOTE.findall(c))
    c = DEMOTE.sub('<span class="tag">Carried &middot; 4:45 edition</span>', c)
    wr(f, c)
print('demoted New tags:', demoted)

# ================================================================= WALL STREET
w = rd('wallstreet-briefing.html')

# --- 1. TLDR: carry the close, add the now-sourced after-hours reaction + Canada.
old_tldr_tail = ('oil settled more than 5% lower and the 10-year yield fell')
assert w.count(old_tldr_tail) == 1
w = rep(w,
  'oil settled more than 5% lower and the 10-year yield fell',
  'oil settled more than 5% lower and the 10-year yield fell, while after the bell <b>Intuit fell more than 7%</b> on soft fiscal-2027 guidance and <b>Zoom traded down 4.5% to $96.70</b> on a beat',
  'ws.tldr')

# --- 2. Intuit after-hours card: replace with the fetched-primary version.
old_intu = '<div class="tags"><span class="tag">Carried &middot; 4:45 edition</span><span class="tag down">Intuit lower after hours</span><span class="tag">INTU</span></div>'
new_intu = '<div class="tags"><span class="tag new">New &middot; 5:55</span><span class="tag down">Intuit &minus;7% after hours</span><span class="tag">INTU</span></div>'
w = rep(w, old_intu, new_intu, 'ws.intu.tags')

old_intu_body = '<b>Two different after-hours moves are on the wires and neither is merged into the other here:</b> one account has the stock <b>down 7.3%</b> in Tuesday after-hours trading; another has it <b>down 16%</b> after the bell. Direction is agreed, magnitude is not, so this page asserts only that Intuit fell sharply after hours.</p>'
new_intu_body = ('<b>The move now has a fetched primary source.</b> AskTraders, published at 22:03 on August&nbsp;25, reports that Intuit shares '
 '<b>&ldquo;plunged more than 7% in after-hours trading Tuesday&rdquo;</b> &mdash; the same account gives the regular-session close as '
 '<b>$358.91, down 2.98%</b>, and puts the value destroyed at roughly <b>$6.9&nbsp;billion</b> against the pre-earnings capitalisation. '
 'Underneath the guidance, the quarter itself was strong: <b>Online Ecosystem revenue rose 17% to $2.6&nbsp;billion</b> and '
 '<b>QuickBooks Online Accounting grew 20%</b>. The segment guidance splits the same way &mdash; <b>Global Business Solutions +13% to +14%</b> '
 'and <b>Credit Karma +11% to +13%</b>, against <b>Mailchimp guided to a decline of as much as 1% or flat</b> for fiscal&nbsp;2027. '
 'First-quarter adjusted EPS guidance of <b>$2.44 to $2.48</b> also weighed, though the company attributed that drop largely to a '
 '<b>revised stock-based-compensation accounting method</b> rather than to the underlying business. Wall Street&rsquo;s average price target '
 'is <b>$446.02</b>. <b>Correction of record:</b> a <b>&minus;16%</b> after-hours figure circulated earlier and was printed here unmerged; '
 '<b>no source fetched this run states it</b>, and the two sources fetched this run both put the move at roughly <b>7%</b>. '
 'This page now carries the 7% figure and flags the 16% one as uncorroborated.</p>')
w = rep(w, old_intu_body, new_intu_body, 'ws.intu.body')

# --- 3. Zoom card: now has a sourced after-hours move.
old_zm = '<div class="tags"><span class="tag">Carried &middot; 4:45 edition</span><span class="tag">ZM</span></div>\n<h3>Zoom raises the year on its fastest enterprise growth in three years</h3>'
new_zm = '<div class="tags"><span class="tag new">New &middot; 5:55</span><span class="tag down">Zoom &minus;4.5% after hours</span><span class="tag">ZM</span></div>\n<h3>Zoom beats and raises &mdash; and still trades down after hours</h3>'
w = rep(w, old_zm, new_zm, 'ws.zm.head')

old_zm_body = '<b>No after-hours price move for Zoom was stated by any source fetched this run</b>, so none is published &mdash; the numbers above are results and guidance, not a share reaction.</p>'
new_zm_body = ('<b>The share reaction is now sourced.</b> StockStory via Yahoo Finance, filed at <b>4:25&nbsp;p.m. EDT</b>, reports that '
 '<b>&ldquo;the stock traded down 4.5% to $96.70 immediately after reporting&rdquo;</b> &mdash; its reading being that &ldquo;the market seemed to be '
 'hoping for more.&rdquo; The quarter beat: <b>revenue $1.28&nbsp;billion against $1.27&nbsp;billion estimated</b>, up <b>4.9%</b> year on year, '
 'and <b>adjusted EPS $1.55 against $1.48 estimated</b>, a 5% beat. Adjusted operating income was <b>$510.3&nbsp;million</b> (a 40% margin, in line), '
 'operating margin <b>24.6%</b> against 26.4% a year ago, free-cash-flow margin <b>37%</b> against 40.4% in the prior quarter. '
 '<b>Billings $1.34&nbsp;billion, up 5.2%</b>; <b>net revenue retention 99%</b>; <b>4,625 customers paying more than $100,000 a year</b>; '
 'market capitalisation <b>$30.74&nbsp;billion</b>. Full-year adjusted EPS guidance was <b>raised to $6.10 at the midpoint</b>, a 2% increase. '
 'Founder and chief executive <b>Eric S. Yuan</b>: total revenue growth was &ldquo;anchored by 7.8% growth in Enterprise revenue, its strongest '
 'growth rate in three years,&rdquo; with <b>Zoom Virtual Agent customer count up 256% year over year</b> and the acquisitions of '
 '<b>Common Room</b> and <b>BrightHire</b> folded in. <b>Recorded but not published as current:</b> a search synthesis suggested the loss had '
 'narrowed to about 2% later in the session; no fetched source states that, so only the 4.5% print stands.</p>')
w = rep(w, old_zm_body, new_zm_body, 'ws.zm.body')

w = rep(w,
 '<div class="note">This section exists only because sourced post-close material now exists.',
 '<div class="note">Both cards were rebuilt this run against sources fetched in full after the bell, replacing the search-synthesis versions carried at 4:45. This section exists only because sourced post-close material now exists.',
 'ws.ah.note')

# --- 4. On the radar: replace the Canada placeholder with the verified item.
old_can = '<li><b>Canada&rsquo;s retaliatory tariffs.</b> Ottawa has announced counter-measures to the 50% US duties on Canadian cars, trucks, automotive parts and steel that take effect <b>January&nbsp;1, 2027</b>. No source fetched this run stated the scope, the rate or the start date of the Canadian measures, so none is published here.</li>'
new_can = ('<li><b>New &mdash; Canada&rsquo;s retaliatory tariffs now have a scope, a rate and a date.</b> Finance minister '
 '<b>Fran&ccedil;ois-Philippe Champagne</b> on Tuesday issued a <b>99-page list</b> of hundreds of US goods that will face increased levies in Canada '
 '<b>after September&nbsp;8th</b>, covering <b>$20&nbsp;billion (&euro;17.14&nbsp;billion)</b> of US imports and including steel, dairy products and '
 'agricultural equipment. The counter-tariffs are set at <b>15, 25 or 50 per cent</b>, matching the rates Washington applied to the same categories of '
 'Canadian exports. Champagne: &ldquo;When the US asked too much and offered too little, we chose to stand up for Canadians,&rdquo; and the measures are '
 '&ldquo;dollar-for-dollar, rate-for-rate&hellip; as well as a multi-billion dollar support package.&rdquo; Context from the same report: trade talks '
 '<b>collapsed on Friday</b> after prime minister <b>Mark Carney</b> suspended them, US tariffs on <b>$20&nbsp;billion</b> of Canadian goods took effect '
 '<b>Saturday</b>, and on <b>Monday</b> the US raised duties on Canadian cars and automotive parts. <em>Figures beyond these &mdash; a C$27.6&nbsp;billion '
 'product total, a 700-plus line count and a C$7.5&nbsp;billion support package &mdash; appeared only in a search synthesis and are not published here.</em></li>')
w = rep(w, old_can, new_can, 'ws.radar.canada')

# --- 5. Rates / commodities: post-close drift on the four continuously quoted lines.
w = rep(w,
 '<tr><td>WTI crude (Oct 26 contract)</td><td><b>$80.57</b></td><td class="down"><b>&minus;$4.44, or &minus;5.22%</b>, on the settled commodities board read after the bell',
 '<tr><td>WTI crude (Oct 26 contract)</td><td><b>$81.09</b></td><td class="down"><b>&minus;$3.92, or &minus;4.61%</b>, on the Yahoo Finance commodities board read at about <b>5:50&nbsp;p.m. ET</b> &mdash; futures keep trading after the equity bell, and this line has firmed from the <b>$80.57, &minus;$4.44, &minus;5.22%</b> print taken at 4:35&nbsp;p.m., which is retained rather than overwritten. That earlier figure was the settled commodities board read after the bell',
 'ws.rates.wti')

w = rep(w,
 '<tr><td>Gold</td><td><b>$4,723.10</b></td><td class="up"><b>+$25.30, or +0.54%</b>, on the settled post-close commodities board',
 '<tr><td>Gold</td><td><b>$4,715.90</b></td><td class="up"><b>+$18.10, or +0.39%</b>, on the <b>5:50&nbsp;p.m. ET</b> board, easing from the <b>$4,723.10, +$25.30, +0.54%</b> print taken at 4:35&nbsp;p.m. Both are published; neither is merged. The 4:35 figure was the settled post-close commodities board',
 'ws.rates.gold')

w = rep(w,
 '<tr><td>Bitcoin</td><td><b>$78,851.16</b></td><td class="down"><b>&minus;$78.10, or &minus;0.10%</b>, on the settled post-close board &mdash; the day&rsquo;s gain given back.',
 '<tr><td>Bitcoin</td><td><b>$78,107.04</b></td><td class="down"><b>&minus;$863.27, or &minus;1.09%</b>, on the <b>5:50&nbsp;p.m. ET</b> board &mdash; the slide extended through the evening from the <b>$78,851.16, &minus;$78.10, &minus;0.10%</b> print at 4:35&nbsp;p.m. Crypto trades around the clock, so both reads are point-in-time and both are printed.',
 'ws.rates.btc')

w = rep(w,
 '<tr><td>VIX</td><td><b>15.49</b></td><td class="down"><b>&minus;0.36, or &minus;2.27%</b>, on the settled post-close board.',
 '<tr><td>VIX</td><td><b>15.45</b></td><td class="down"><b>&minus;0.40, or &minus;2.52%</b>, on the <b>5:50&nbsp;p.m. ET</b> board, against <b>15.49, &minus;0.36, &minus;2.27%</b> at 4:35&nbsp;p.m. Both printed.',
 'ws.rates.vix')

# --- 6. Sources: new entries at the top of the footer list.
ws_src_anchor = '<li><b>New this run &mdash; THE VERIFIED CLOSE (4:35&nbsp;p.m. ET).</b>'
new_ws_sources = ('<li><b>New this run (5:55&nbsp;p.m. ET) &mdash; the after-hours prints, upgraded from synthesis to fetched primaries.</b> '
 'AskTraders &mdash; <a href="https://www.asktraders.com/analysis/intuit-stock-tumbles-in-after-hours-trading-despite-q4-earnings-beat/">&ldquo;Intuit Stock Tumbles in After-Hours Trading Despite Q4 Earnings Beat&rdquo;</a> '
 '(published 22:03 on August&nbsp;25, fetched in full): &ldquo;plunged more than 7% in after-hours trading&rdquo;; regular-session close <b>$358.91, &minus;2.98%</b>; '
 '<b>$6.9&nbsp;billion</b> of value erased; Online Ecosystem <b>+17% to $2.6&nbsp;billion</b>; QuickBooks Online Accounting <b>+20%</b>; '
 'FQ1 adjusted EPS <b>$2.44&ndash;$2.48</b> attributed to a revised stock-based-compensation accounting method; Mailchimp <b>&minus;1% to flat</b>; '
 'Global Business Solutions <b>+13&ndash;14%</b>; Credit Karma <b>+11&ndash;13%</b>; average price target <b>$446.02</b>. '
 'StockStory via Yahoo Finance &mdash; <a href="https://finance.yahoo.com/markets/stocks/articles/zoom-nasdaq-zm-exceeds-q2-202522404.html">&ldquo;Zoom (NASDAQ:ZM) Exceeds Q2 CY2026 Expectations, Large Customer Wins Accelerate&rdquo;</a> '
 '(Kayode Omotosho, Tue August&nbsp;25 at 4:25&nbsp;p.m. EDT, fetched in full): &ldquo;the stock traded down 4.5% to $96.70 immediately after reporting&rdquo;; '
 'revenue <b>$1.28&nbsp;billion</b> (+4.9%) vs <b>$1.27&nbsp;billion</b>; adjusted EPS <b>$1.55</b> vs <b>$1.48</b>; adjusted operating income <b>$510.3&nbsp;million</b>; '
 'operating margin <b>24.6%</b>; FCF margin <b>37%</b>; billings <b>$1.34&nbsp;billion (+5.2%)</b>; NRR <b>99%</b>; <b>4,625</b> customers above $100,000; '
 'market cap <b>$30.74&nbsp;billion</b>; full-year adjusted EPS raised to <b>$6.10</b> at the midpoint; the Eric S. Yuan quote and the '
 '<b>256%</b> Zoom Virtual Agent growth. <b>The same Yahoo page, post-close, re-served the settled index board unchanged</b> &mdash; '
 'S&amp;P&nbsp;500 <b>7,677.28 +24.42 +0.32%</b>, Dow <b>53,577.40 +160.24 +0.30%</b>, Nasdaq <b>26,151.30 +171.11 +0.66%</b>, Russell&nbsp;2000 '
 '<b>3,010.02 +14.94 +0.50%</b> &mdash; independently re-confirming the close under a &ldquo;U.S. markets closed&rdquo; header, while its '
 'continuously quoted lines had drifted to VIX <b>15.45</b>, Gold <b>4,715.90</b>, Bitcoin <b>78,107.04</b> and Crude Oil Oct&nbsp;26 <b>81.09</b>. '
 'The DKS trending ticker was unchanged at <b>124.31 &minus;55.02 (&minus;30.68%)</b>.</li>\n'
 '<li><b>New this run &mdash; the Canada counter-tariffs.</b> The Irish Times / Financial Times &mdash; '
 '<a href="https://www.irishtimes.com/business/2026/08/25/canada-announces-20bn-retaliatory-tariffs-as-us-trade-war-escalates/">&ldquo;Canada announces $20bn retaliatory tariffs as US trade war escalates&rdquo;</a> '
 '(Ilya Gridneff, Tue August&nbsp;25 16:48, fetched in full): the 99-page list, the September&nbsp;8th start, the $20&nbsp;billion / &euro;17.14&nbsp;billion scope, '
 'the 15/25/50 per cent rates, the two Champagne quotes, the Friday collapse of talks under Mark Carney, the Saturday US tariffs and Monday&rsquo;s '
 'increase on Canadian cars and parts.</li>\n')
w = rep(w, ws_src_anchor, new_ws_sources + ws_src_anchor, 'ws.sources')

wr('wallstreet-briefing.html', w)

# ===================================================================== CYBER
c = rd('cyber-briefing.html')

# Marimo: a new Vulnerability Watch row + an incident card.
vulnrow_anchor = None
m = re.search(r'<tr><th>CVE</th>.*?</tr>', c, re.S)
if not m:
    FAILS.append('cyber: CVE table header not found')
else:
    hdr = m.group(0)
    newrow = ('\n<tr><td><b>CVE-2026-75149</b></td><td><b>8.7</b> (CVSS v4) / <b>8.8</b> (v3.1)</td>'
      '<td>Marimo notebook, versions before <b>0.23.15</b></td>'
      '<td><b>New this run.</b> Code injection: a crafted notebook supplies an attacker-controlled '
      '<b>Model Context Protocol server command</b> through notebook configuration, and the CVE Numbering Authority record says that command '
      '<b>launches as a local subprocess before any notebook cell is executed</b> when the file is opened in <b>edit mode</b>. '
      'User interaction required; no attacker authentication required. Scored by <b>VulnCheck</b> as CNA; published <b>August&nbsp;19</b>. '
      'Fixed in <b>0.23.15</b> (released July&nbsp;23, 2026); the current PyPI release is <b>0.24.0</b>, published August&nbsp;17 and confirmed by '
      'The Hacker News on August&nbsp;25. Marimo&rsquo;s PEP&nbsp;723 hardening patch treats notebook metadata as attacker-controlled and strips the '
      '<b>ai, mcp, completion, secrets and server</b> configuration sections through an allowlist. Credited to <b>Gregory Tan</b> (handle Grg0rry). '
      '<b>Not KEV-listed and carries no federal deadline.</b></td></tr>')
    c = c.replace(hdr, hdr + newrow, 1)

# Breaches & incidents card for the Marimo family of flaws.
inc_anchor = '<div class="lab">Breaches &amp; incidents</div>\n<div class="cards">\n'
if c.count(inc_anchor) != 1:
    FAILS.append('cyber: breaches cards anchor count = %d' % c.count(inc_anchor))
else:
    card = ('<div class="card">\n'
      '<div class="tags"><span class="tag new">New &middot; 5:55</span><span class="tag">AI toolchain</span><span class="tag">CVE-2026-75149</span></div>\n'
      '<h3>Marimo patches a notebook that can run an MCP command before a single cell does</h3>\n'
      '<p>The Hacker News (Swati Khandelwal), <b>August&nbsp;25</b>: Marimo has fixed <b>CVE-2026-75149</b>, a code-injection flaw in its Python notebook '
      'software that let a crafted notebook hand the application an <b>attacker-supplied Model Context Protocol server command</b> through notebook '
      'configuration. Per VulnCheck&rsquo;s CNA record the command <b>runs as a local subprocess when the notebook is opened in edit mode &mdash; before any '
      'cell executes</b>, so simply opening a shared notebook is enough. VulnCheck scores it <b>8.7 on CVSS v4</b> and <b>8.8 on v3.1</b>, with user '
      'interaction required and no authentication needed. Versions <b>before 0.23.15</b> are affected; <b>0.23.15</b> is the fix, and the current PyPI '
      'release is <b>0.24.0</b> (August&nbsp;17), which The Hacker News confirmed on August&nbsp;25. The <b>PEP&nbsp;723 hardening commit</b> now treats '
      'notebook metadata as attacker-controlled and passes notebook-supplied configuration through an allowlist that removes the <b>ai</b>, <b>mcp</b>, '
      '<b>completion</b>, <b>secrets</b> and <b>server</b> sections. Discovery is credited to <b>Gregory Tan</b> (handle <b>Grg0rry</b>), who also appears '
      'as a co-author on that commit. <b>The same configuration boundary produced two other CVEs</b>, and the page keeps them distinct: '
      '<b>CVE-2026-67618</b> (CVSS <b>7.1</b>, disclosed <b>August&nbsp;4, 2026</b>, also before 0.23.15) sends the operator&rsquo;s <b>API key</b> to an '
      'attacker-controlled AI <code>base_url</code> supplied through notebook metadata, again with no cell execution required; and the earlier '
      '<b>CVE-2026-39987</b> was a missing authentication check on the <b>/terminal/ws</b> endpoint in versions <b>0.20.4 and earlier</b> that handed '
      'requests a full <b>pseudo-terminal shell</b>, patched in <b>0.23.0</b>. '
      '&#9888; <b>None of the three is KEV-listed and none carries a federal remediation deadline</b> &mdash; stated here so the Patch Priority box above '
      'is not misread.</p>\n'
      '</div>\n')
    c = c.replace(inc_anchor, inc_anchor + card, 1)

# Sources
cy_src = re.search(r'<div class="lab">Sources</div>\s*<ul>\s*', c)
if not cy_src:
    FAILS.append('cyber: sources anchor not found')
else:
    a = cy_src.group(0)
    s = ('<li><b>New this run (5:55&nbsp;p.m. ET) &mdash; Marimo.</b> The Hacker News (Swati Khandelwal), August&nbsp;25 &mdash; '
      '<a href="https://thehackernews.com/2026/08/marimo-notebook-flaw-could-run-mcp.html">&ldquo;Marimo Notebook Flaw Could Run MCP Commands Before Cells Execute in Edit Mode&rdquo;</a>, '
      'fetched in full: CVE-2026-75149, VulnCheck CNA scores 8.7 (v4) / 8.8 (v3.1), affected versions before 0.23.15, fix 0.23.15 (July&nbsp;23, 2026), '
      'current PyPI release 0.24.0 (August&nbsp;17) confirmed August&nbsp;25, the PEP&nbsp;723 allowlist and its five stripped sections, credit to Gregory Tan '
      '(Grg0rry), plus the related CVE-2026-67618 (7.1, August&nbsp;4) and CVE-2026-39987 (/terminal/ws, &le;0.20.4, patched 0.23.0).</li>\n'
      '<li><b>Re-verified this run &mdash; the KEV board did not move.</b> A dedicated search of CISA&rsquo;s alert index returned the same three most recent '
      'entries as the last nine editions: <b>August&nbsp;24 &mdash; one</b> (Oracle HTTP Server / WebLogic Server Proxy Plug-in improper access control, '
      '<b>CVE-2026-21962</b>), <b>August&nbsp;20 &mdash; two</b> (TrueConf Server <b>CVE-2026-72529</b> missing authentication and <b>CVE-2026-72530</b> code '
      'injection) and <b>August&nbsp;11 &mdash; three</b>. <b>Nothing was added on August&nbsp;25.</b> The same search re-confirmed that CISA gave FCEB agencies '
      '<b>the shortest deadline available under BOD 26-04 &mdash; three days</b> &mdash; for the Oracle flaw, matching the Forbes report already cited below, '
      'and re-confirmed that <b>BOD 26-04</b> is risk-based rather than the superseded flat three-week BOD 22-01 window &mdash; '
      '<a href="https://www.cisa.gov/news-events/alerts/2026/08/24/cisa-adds-one-known-exploited-vulnerability-catalog">CISA, August&nbsp;24</a>, '
      '<a href="https://www.cisa.gov/news-events/alerts/2026/08/20/cisa-adds-two-known-exploited-vulnerabilities-catalog">CISA, August&nbsp;20</a>, '
      '<a href="https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog">CISA, August&nbsp;11</a>. '
      '<em>cisa.gov itself returned an empty body to a direct fetch this run, as on previous runs; the alert titles, dates and CVE identifiers above come from '
      'the search index of those same pages, and no countdown was changed on the strength of them.</em></li>\n')
    c = c.replace(a, a + s, 1)

wr('cyber-briefing.html', c)

# ======================================================================= MMA
m = rd('mma-briefing.html')

old_biz = '<p>No viewership figure has been published in any source fetched this run, so none is given here.</p>'
new_biz = ('<p><b>New this run &mdash; gates behind the two year-end cards.</b> POST Wrestling (John Pollock), <b>August&nbsp;25</b>: the '
 '<b>November&nbsp;14 Madison Square Garden</b> show marks the <b>tenth anniversary</b> of the promotion&rsquo;s first card at the venue, '
 '<b>UFC&nbsp;205 in November 2016</b>, headlined by <b>Eddie Alvarez vs. Conor McGregor</b>; the UFC has run the Garden annually since, '
 'except in 2020. <b>Last year&rsquo;s MSG card &mdash; Islam Makhachev defeating Jack Della Maddalena for the welterweight title &mdash; drew a gate of '
 '$13.6&nbsp;million.</b> The <b>December&nbsp;12</b> card is a six-month turnaround at <b>T-Mobile Arena</b>, which staged '
 '<b>Max Holloway vs. Conor McGregor at UFC&nbsp;329</b> and produced <b>the promotion&rsquo;s highest gate in history at $26.4&nbsp;million</b>. '
 '<b>No title fights have been officially announced for either show.</b></p>\n'
 '<p>&#9888; <b>A numbering error in that same report, recorded rather than repeated.</b> Its headline and body text call the two shows '
 '&ldquo;UFC&nbsp;335&rdquo; and &ldquo;UFC&nbsp;336,&rdquo; but its own opening line and its own numbered-events list both read '
 '<b>UFC&nbsp;334 &mdash; Madison Square Garden (Saturday, Nov.&nbsp;14)</b> and <b>UFC&nbsp;335 &mdash; T-Mobile Arena in Las Vegas '
 '(Saturday, Dec.&nbsp;12)</b>. The article contradicts itself on the numbers while agreeing with every other source on the dates and venues, so '
 '<b>this page keeps the 334/335 numbering</b> already corroborated by Forbes, MMA Mania, Yahoo Sports, Cageside Press, FIGHTMAG and SI/MMA Knockout, '
 'and publishes only the dates, venues and gate figures from the new report. The same list re-confirms <b>UFC&nbsp;331: Joshua Van vs. Alexandre Pantoja '
 '(Saturday, Sept.&nbsp;19)</b>, <b>UFC&nbsp;332: Salt Lake City, Utah, no main event announced (Saturday, Oct.&nbsp;3)</b> and '
 '<b>UFC&nbsp;333: Alexander Volkanovski vs. Movsar Evloev (Saturday, Oct.&nbsp;24)</b>, all already carried above.</p>\n'
 '<p>No viewership figure has been published in any source fetched this run, so none is given here.</p>')
m = rep(m, old_biz, new_biz, 'mma.biz')

mma_src = re.search(r'<div class="lab">Sources</div>\s*<ul>\s*', m)
if not mma_src:
    FAILS.append('mma: sources anchor not found')
else:
    a = mma_src.group(0)
    s = ('<li><b>New this run (5:55&nbsp;p.m. ET) &mdash; the year-end cards, with gates.</b> POST Wrestling (John Pollock), August&nbsp;25, '
      'published 17:39 UTC, fetched in full &mdash; '
      '<a href="https://www.postwrestling.com/2026/08/25/ufc-335-ufc-336-dates-and-locations-confirmed-to-close-out-2026/">&ldquo;UFC 335 &amp; UFC 336 dates and locations confirmed to close out 2026&rdquo;</a>. '
      'Used for: the MSG tenth-anniversary framing (UFC&nbsp;205, November 2016, Eddie Alvarez vs. Conor McGregor; run annually except 2020), the '
      '<b>$13.6&nbsp;million</b> gate for last year&rsquo;s Makhachev&ndash;Della Maddalena MSG card, the <b>$26.4&nbsp;million</b> record gate for '
      'Max Holloway vs. Conor McGregor at UFC&nbsp;329 at T-Mobile Arena, the six-month turnaround, &ldquo;No title fights have been officially announced for '
      'either show,&rdquo; and the numbered-events list. <b>Not used: its event numbering.</b> The headline and prose say 335/336 while the same article&rsquo;s '
      'opening sentence and numbered list say 334/335 &mdash; an internal contradiction, resolved in favour of the numbering corroborated by every other source '
      'on this page.</li>\n')
    m = m.replace(a, a + s, 1)

wr('mma-briefing.html', m)

if FAILS:
    print('EDIT FAILURES:')
    for f in FAILS:
        print(' -', f)
    sys.exit(1)
print('all edits applied cleanly')
