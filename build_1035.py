#!/usr/bin/env python3
# Daily Briefings builder - 2026-09-02 Morning Edition (~10:52 AM ET), SIXTH run of the day.
# Every line below traces to a source fetched THIS run or a sourced CORRECTIONS.md entry.
import os

OUT = "/sessions/wizardly-compassionate-cerf/mnt/outputs"
CSSD = "/tmp"

def css(name):
    return open(os.path.join(CSSD, "css_%s.css" % name)).read()

STAMP = """<script>(function(){try{var n=new Date();var et=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'long',year:'numeric',month:'long',day:'numeric'}).format(n);var t=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',minute:'2-digit'}).format(n);var h=parseInt(new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',hour12:false}).format(n),10);var ed=h<11?'Morning Edition':(h<15?'Midday Edition':'Afternoon Edition');document.getElementById('datestamp').textContent=et;document.getElementById('updated').textContent=t+' ET';document.getElementById('edition').textContent=ed;var fl=document.getElementById('freshline');if(fl)fl.textContent='Data as of '+t+' ET \\u00b7 briefings refresh every 30 minutes, 8 AM\\u20136 PM ET';}catch(e){}})();</script>"""

def nav(active):
    items = [("index.html", "★ Front Page", "ix"),
             ("cyber-briefing.html", "⛨ The Cyber Wire", "cy"),
             ("wallstreet-briefing.html", "▲ The Closing Bell", "ws"),
             ("mma-briefing.html", "⊘ The Octagon", "mma"),
             ("archive.html", "\U0001f5c4 Archive", "ar")]
    out = ['<nav>']
    for href, label, key in items:
        cls = ' class="on"' if key == active else ''
        out.append('<a href="%s"%s>%s</a>' % (href, cls, label))
    out.append('</nav>')
    return "".join(out)

def meta():
    return ('<div class="meta"><span class="pill live"><span class="dot"></span> Live</span>'
            '<span class="pill" id="edition"></span><span class="pill" id="datestamp"></span>'
            '<span class="pill">Updated <span id="updated"></span></span></div>')

FRESH = '<div class="freshline" id="freshline"></div>'

PROV = ('<div class="note">Provenance: where an item below says &ldquo;this run,&rdquo; it refers to the edition that '
        'first wrote the line. Every figure on this page traces to a source fetched during the 10:35&ndash;10:50 AM ET '
        'research window of this edition, or to an explicitly labelled sourced entry from an earlier edition today.</div>')

def page(title, css_name, body, active):
    return ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><style>%s</style></head><body><div class="wrap">%s</div>%s</body></html>'
            % (title, css(css_name), body, STAMP))

# ============================================================ WALL STREET
TICKER = """<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>
<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NASDAQ:CRDO","title":"Credo"},{"proName":"NASDAQ:MDB","title":"MongoDB"},{"proName":"NASDAQ:DELL","title":"Dell"},{"proName":"NASDAQ:PANW","title":"Palo Alto"},{"proName":"NASDAQ:GTLB","title":"GitLab"},{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script></div>"""

def sq(sym):
    return ('<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/'
            'embed-widget-single-quote.js" async>{"symbol":"%s","width":"100%%","colorTheme":"dark",'
            '"isTransparent":true,"locale":"en"}</script></div>' % sym)

ws_body = []
ws_body.append('<header class="masthead serif"><h1>The Closing Bell</h1>'
    '<p class="tag">Your daily markets briefing &mdash; Wall Street, rates &amp; the tape</p>' + meta() + '</header>')
ws_body.append('<div class="tldr"><b>The Tape</b> <span>Stocks are narrowly higher at midmorning even as a global bond '
    'sell-off pushes the U.S. 10-year Treasury yield to its highest level since November 2023, with Dell up on AI-server '
    'demand while Credo Technology, MongoDB and Palo Alto Networks are all down sharply.</span></div>')
ws_body.append(FRESH)
ws_body.append(nav("ws"))
ws_body.append(TICKER)

ws_body.append('<h2>Live Index Quotes &mdash; updates in real time</h2>')
ws_body.append('<div class="tickers">' + sq("FOREXCOM:SPXUSD") + sq("FOREXCOM:NSXUSD") + sq("FOREXCOM:DJI") + '</div>')
ws_body.append('<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the latest '
    'edition; official closes are in the Weekly Scorecard.</div>')

ws_body.append('<h2>The Lead</h2>')
ws_body.append('<div class="panel"><h3 class="lead-h">Yields set the agenda and the tape follows &mdash; as of ~10:35 AM ET, '
    'the Dow leads a narrowly positive open while the 10-year touches its highest since November 2023</h3>'
    '<p style="margin:0 0 10px;color:var(--muted2)">Two clocked reads, one hour apart, both fetched this run. '
    'At the <b>9:35 AM ET opening bell</b>, TheStreet had the S&amp;P 500 up 0.06%, the Dow up 0.37%, the Nasdaq Composite '
    'down 0.06% and the Russell 2000 down 1.23%. At a <b>Yahoo Finance quote-board read taken at roughly 10:35 AM ET</b>, '
    'the S&amp;P 500 was <span class="up">+15.23 (+0.20%)</span>, the Dow <span class="up">+277.47 (+0.53%)</span>, the '
    'Nasdaq Composite <span class="up">+7.53 (+0.03%)</span> and the Russell 2000 <span class="up">+21.95 (+0.75%)</span>, '
    'with the VIX at 15.90, down 2.69%.</p>'
    '<p style="margin:0 0 10px;color:var(--muted2)"><b>The Russell is the largest index swing on this page and nothing '
    'fetched explains it.</b> It was down 1.23% at 9:35 and up 0.75% an hour later &mdash; a roughly two-percentage-point '
    'reversal inside one hour, while the Dow moved a fifth of that. No source offers a cause and none is invented here; '
    'the divergence is recorded as an observation, not a causal claim.</p>'
    '<p style="margin:0 0 10px;color:var(--muted2)"><b>Every point-change on that quote board reconciles exactly to '
    'Tuesday’s official closes</b> &mdash; 7,631.47 + 15.23, 52,766.88 + 277.47, 26,099.77 + 7.53 &mdash; and each '
    'percentage matches its own points figure. That reconciliation is this desk’s arithmetic, disclosed as such; the '
    'implied intraday levels are not published as figures, because intraday levels are not closes.</p>'
    '<p style="margin:0 0 10px;color:var(--muted2)">The driver is the bond market. The benchmark <b>U.S. 10-year Treasury '
    'yield hit a day high of 4.814%, its highest level since November 2023</b>, CNBC reported via TheStreet’s 10:15 AM '
    'entry; yields in the U.K., Germany and France also rose, and Japan’s 10-year government bond yield remained near a '
    'multidecade high. Kyle Rodda of Capital.com framed the move as renewed Middle East hostilities sending crude surging '
    'and global bond yields to &ldquo;multi-year &ndash; and in some instances, multi-decade &ndash; highs,&rdquo; adding that '
    'markets &ldquo;will be hopeful&rdquo; the flare-up is another attempt to &ldquo;escalate to de-escalate.&rdquo; '
    'TheStreet Pro’s James &ldquo;Rev Shark&rdquo; DePorre dates the selling differently, to &ldquo;Friday by Fed Chair '
    'Kevin Warsh,&rdquo; calling the U.S. &ldquo;the best house in a deteriorating neighborhood.&rdquo; Both attributions are '
    'printed; neither is adopted over the other.</p>'
    '<p style="margin:0 0 10px;color:var(--muted2)">The morning’s data point cut the same way. <b>ADP private payrolls '
    'rose 38,000 in August</b>, below the 47,000 estimate and down from an upwardly revised 46,000 in July &mdash; the '
    'smallest gain since January. Education and health services added 45,000, leisure and hospitality 16,000 and construction '
    '12,000; manufacturing shed 17,000, professional and business services 16,000, and both natural resources and mining and '
    'trade, transportation and utilities lost 5,000 apiece.</p>'
    '<p style="margin:0;color:var(--muted2)"><b>A refusal, recorded.</b> A search summariser this run offered the Nasdaq '
    '&ldquo;up 0.42%&rdquo; in the same block as &ldquo;up 10.94 points.&rdquo; On a 26,099.77 base, 10.94 points is about '
    '+0.04%, not +0.42% &mdash; the two cannot both be right, so the percentage was refused and only the reconciled '
    'quote-board read above is published.</p></div>')

ws_body.append('<h2>Movers &amp; Drivers</h2>')
ws_body.append('<div class="cards">'
    '<div class="card"><div class="tags"><span class="tag t-c">Down 17.5%</span><span class="tag t-new">New</span></div>'
    '<h3>Credo Technology (CRDO) &mdash; a double beat sold anyway</h3>'
    '<p>Yahoo Finance’s trending board at ~10:35 AM ET had CRDO at <span class="down">170.44, −36.19 '
    '(−17.51%)</span>. Credo reported first-quarter revenue of about <b>$479 million against a $471.77 million '
    'estimate</b> and adjusted EPS of <b>$1.20 against $1.17</b> &mdash; both beats.</p>'
    '<p>The selling is attributed to margins, not the top line: <b>GAAP operating margin narrowed to 25.2% from 35.7% in '
    'the prior quarter</b>, with operating expenses, especially R&amp;D and SG&amp;A, rising faster than revenue. '
    'Second-quarter guidance is <b>$525&ndash;535 million</b> against a $515.79 million estimate, with adjusted gross margin '
    'guided to <b>67&ndash;69%</b>.</p>'
    '<p class="note" style="margin-bottom:0">Two windows, both printed: a premarket read had CRDO down 8.00% at $190.10; '
    'the post-open board has it down 17.51%. Neither is adopted as &ldquo;the&rdquo; move.</p></div>'

    '<div class="card"><div class="tags"><span class="tag t-c">Down 12.9%</span></div>'
    '<h3>MongoDB (MDB) &mdash; beat, then guided cautiously</h3>'
    '<p><span class="down">378.25, −55.96 (−12.89%)</span> on the ~10:35 AM board. TheStreet’s 8:15 AM '
    'premarket entry had it down 12.4%, attributing the fall to cautious guidance after a second-quarter earnings beat.</p>'
    '<p class="note" style="margin-bottom:0">Both reads back out to a Tuesday close of $434.21; the gap between them is a '
    'clock, not a dispute.</p></div>'

    '<div class="card"><div class="tags"><span class="tag t-c">Down 9.4%</span><span class="tag t-new">New</span></div>'
    '<h3>Palo Alto Networks (PANW) &mdash; falling, cause unsourced</h3>'
    '<p><span class="down">328.22, −33.87 (−9.35%)</span> on the ~10:35 AM board, backing out to a Tuesday close '
    'of $362.09.</p>'
    '<p class="note" style="margin-bottom:0">No source fetched this run gives a reason for the decline, and none is '
    'supplied here.</p></div>'

    '<div class="card"><div class="tags"><span class="tag t-a">Up 6.2%</span></div>'
    '<h3>Dell Technologies (DELL) &mdash; AI servers carry the quarter</h3>'
    '<p><span class="up">451.21, +26.21 (+6.17%)</span> at ~10:35 AM ET. TheStreet’s 8:15 AM premarket entry had it '
    'up 8.1% after Dell beat Wall Street expectations for its fiscal second quarter of 2027, &ldquo;driven by massive demand '
    'for artificial intelligence servers.&rdquo;</p>'
    '<p class="note" style="margin-bottom:0">Premarket +8.1%, post-open +6.17% &mdash; two windows, both printed.</p></div>'

    '<div class="card"><div class="tags"><span class="tag t-a">Premarket +21%</span></div>'
    '<h3>GitLab (GTLB) &mdash; strong quarter, no post-open quote</h3>'
    '<p>TheStreet’s 8:15 AM premarket entry had GitLab shares up <b>21%</b> after strong second-quarter earnings.</p>'
    '<p class="note" style="margin-bottom:0">No post-open GitLab quote was fetched this run, so no intraday figure is '
    'published &mdash; the premarket number is labelled as premarket and left there.</p></div>'

    '<div class="card"><div class="tags"><span class="tag t-w">Headcount</span><span class="tag t-new">New</span></div>'
    '<h3>Uber (UBER) &mdash; up slightly on a 10% workforce cut</h3>'
    '<p><span class="up">+0.58% to $75.68</span> as of TheStreet’s 10:15 AM entry. CEO Dara Khosrowshahi told staff the '
    'changes are designed to &ldquo;make Uber simpler and faster, and create more capacity to invest in our future.&rdquo;</p>'
    '<p>The plan cuts the number of small teams with one or two direct reports by nearly half, reduces employees seven or '
    'more levels below the CEO by 20%, concentrates staff in hubs such as New York and San Francisco, and limits fully '
    'remote employees to about 1% of the workforce. Uber had around 34,000 employees at the end of 2025.</p></div>'
    '</div>')

ws_body.append('<h2>Chart of the Day &mdash; Credo Technology (CRDO)</h2>')
ws_body.append('<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/'
    'embed-widget-mini-symbol-overview.js" async>{"symbol":"NASDAQ:CRDO","width":"100%","height":240,"locale":"en",'
    '"dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}</script></div>')
ws_body.append('<div class="note">Credo holds this slot on the arithmetic, not on the story: at −17.51% it is the '
    'largest single-name move on this page, ahead of MongoDB (−12.89%), Palo Alto Networks (−9.35%) and Dell '
    '(+6.17%). That ranking is this desk’s comparison across figures from one quote board read at one time, not a claim '
    'any source makes.</div>')

ws_body.append('<h2>Sector Heat &mdash; live</h2>')
ws_body.append('<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/'
    'embed-widget-stock-heatmap.js" async>{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change",'
    '"grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,'
    '"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}</script></div>')
ws_body.append('<div class="note">No dated S&amp;P sector percentage was sourced this run, so none is asserted &mdash; the '
    'live heatmap above carries sectors instead. The one breadth figure that is sourced is the VIX at <b>15.90, down '
    '2.69%</b> on the ~10:35 AM quote board: volatility is easing even as the long end of the curve sells off.</div>')

ws_body.append('<h2>The Calendar &mdash; live</h2>')
ws_body.append('<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/'
    'embed-widget-events.js" async>{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en",'
    '"importanceFilter":"0,1","countryFilter":"us"}</script></div>')

ws_body.append('<h2>Live Market Headlines &mdash; updates in real time</h2>')
ws_body.append('<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/'
    'embed-widget-timeline.js" async>{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,'
    '"displayMode":"regular","width":"100%","height":420,"locale":"en"}</script></div>')

ws_body.append('<h2>Weekly Scorecard</h2>')
ws_body.append('<table><thead><tr><th>Index</th><th>Close (Tue Sept 1)</th><th>Change</th><th>%</th></tr></thead><tbody>'
    '<tr><td>S&amp;P 500</td><td>7,631.47</td><td class="down">&mdash;</td><td class="down">−0.71%</td></tr>'
    '<tr><td>Nasdaq Composite</td><td>26,099.77</td><td class="down">&mdash;</td><td class="down">−1.03%</td></tr>'
    '<tr><td>Dow Jones Industrial Average</td><td>52,766.88</td><td class="down">−419.02</td><td class="down">'
    '−0.79%</td></tr></tbody></table>')
ws_body.append('<div class="note">These are Tuesday, September 1 official closes, re-corroborated this run. <b>There is no '
    'September 2 close</b> &mdash; the session is open as this edition publishes, so no Wednesday level appears anywhere on '
    'this page as a completed figure. Points changes for the S&amp;P and Nasdaq were not stated in any source fetched this '
    'run and are left blank rather than derived.</div>')

ws_body.append('<h2>Rates, Bonds &amp; Commodities</h2>')
ws_body.append('<table><thead><tr><th>Instrument</th><th>Read</th><th>Clock &amp; source</th></tr></thead><tbody>'
    '<tr><td>U.S. 10-year Treasury</td><td>day high <b>4.814%</b> &mdash; highest since November 2023</td>'
    '<td>CNBC, via TheStreet 10:15 AM ET entry</td></tr>'
    '<tr><td>U.S. 10-year / 30-year</td><td>4.81% / 5.28%</td><td>September 1 curve read (search summary of yield-curve '
    'trackers); prior session, not today</td></tr>'
    '<tr><td>U.S. 2-year</td><td>4.356%, up more than 12 basis points</td><td>CNBC, August 28, after Warsh’s Jackson '
    'Hole remarks</td></tr>'
    '<tr><td>WTI crude</td><td>+0.32% at $90.51 → −0.71% at $89.58 → <b>89.71, −0.51 (−0.57%)</b></td>'
    '<td>TheStreet 7:04 AM → TheStreet 9:24 AM → Yahoo quote board (Crude Oil Oct 26) ~10:35 AM</td></tr>'
    '<tr><td>Brent crude</td><td>+0.57% at $95.19 → −0.39% at $94.28</td><td>TheStreet 7:04 AM → 9:24 AM</td></tr>'
    '<tr><td>Gold</td><td>futures −0.94% at $4,355 → <b>4,418.20, +21.80 (+0.50%)</b></td>'
    '<td>TheStreet 7:09 AM → Yahoo quote board ~10:35 AM &mdash; direction reverses between the two reads and neither '
    'is adopted</td></tr>'
    '<tr><td>Silver</td><td>futures −1.69% at $64.26</td><td>TheStreet 7:13 AM, &ldquo;early trading&rdquo;</td></tr>'
    '<tr><td>VIX</td><td>15.90, −0.44 (−2.69%)</td><td>Yahoo quote board ~10:35 AM</td></tr>'
    '<tr><td>Bitcoin (USD)</td><td>77,072.09, −971.55 (−1.24%)</td><td>Yahoo quote board ~10:35 AM</td></tr>'
    '<tr><td>Fed funds target</td><td>not sourced this run</td><td>no current target range appeared in anything fetched '
    'this run, so none is stated</td></tr></tbody></table>')
ws_body.append('<div class="note">Two 10-year reads sit side by side above and are deliberately not merged: an intraday '
    '<b>day high</b> of 4.814% for today, and a <b>4.81% / 5.28%</b> curve mark dated to the prior session. A day high and a '
    'settlement are different measurements, and only the first belongs to Wednesday.</div>')

ws_body.append('<h2>On the Radar</h2>')
ws_body.append('<ul class="bul">'
    '<li><b>After today’s close:</b> Broadcom (AVGO), Snowflake (SNOW) and Hewlett Packard Enterprise (HPE) report. '
    'HPE shares were up 3.8% and Snowflake down 2.5% in TheStreet’s 8:15 AM premarket entry, both ahead of their '
    'own numbers.</li>'
    '<li><b>Oil is a binary, and the desks say so.</b> Saxo Bank head of commodity strategy Ole Hansen: &ldquo;An '
    'announcement that a deal has been reached, or that progress is being made, could send prices tumbling, while any '
    'escalation would further undermine the prospect of a peace deal&hellip; a potential $5 move in either direction on fresh '
    'developments.&rdquo;</li>'
    '<li><b>Semiconductor tariffs are being drafted.</b> Commerce Secretary Howard Lutnick told CNBC the administration is '
    'developing a tariff framework for semiconductors and that companies know it is coming: &ldquo;if you build here, you '
    'don’t pay, but if you don’t build here, expect to pay to enter the greatest market in the world.&rdquo; No '
    'market impact was sourced.</li>'
    '<li><b>The Strait of Hormuz is the transmission channel.</b> Iran’s Revolutionary Guards said two oil tankers '
    'struck naval mines attempting to transit the Strait and were disabled, their crews forced to disembark after ignoring '
    'warnings about an &ldquo;illegal route.&rdquo; Iran targeted Jordan, the UAE and Kuwait with missiles and drones '
    'overnight in retaliation for U.S. strikes; Trump posted that the U.S. has &ldquo;almost total control&rdquo; over the '
    'Strait and that he is &ldquo;not trying to force Iran to the bargaining table.&rdquo;</li>'
    '<li><b>The September Fed meeting is being priced as a hike, not a cut.</b> After Warsh’s Jackson Hole keynote on '
    'August 28 saying the central bank still has &ldquo;work to do&rdquo; on inflation, CNBC reported traders lifted the '
    'probability of a September hike to <b>55.7%</b>; a Chase Wealth Management piece says its strategists now expect a '
    '25-basis-point increase at that meeting.</li>'
    '<li><b>Not on this page:</b> no after-hours section appears, because the session is open. Post-close movers return in '
    'the first edition published after 4 PM ET.</li></ul>')

ws_body.append('<h2>Sources</h2><div class="panel srcs">'
    '<a href="https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-02-2026">TheStreet &mdash; Stock Market Today, Sept. 2, 2026 (live blog, entries 6:42 AM&ndash;10:15 AM ET)</a><br>'
    '<a href="https://finance.yahoo.com/markets/stocks/articles/stock-market-today-sept-2-134032621.html">Yahoo Finance &mdash; Sept. 2 markets article and live quote board (read ~10:35 AM ET)</a><br>'
    '<a href="https://www.cnbc.com/2026/09/01/stock-market-today-live-updates.html">CNBC &mdash; stock market live updates (10-year day high 4.814%)</a><br>'
    '<a href="https://www.cnbc.com/2026/09/02/private-payrolls-rose-by-38000-in-august-fewer-than-expected-adp-reports.html">CNBC &mdash; ADP private payrolls +38,000 in August</a><br>'
    '<a href="https://www.cnbc.com/2026/08/28/treasury-yields-jackson-hole.html">CNBC &mdash; 2-year yield jumps as Warsh says Fed may &lsquo;have work to do&rsquo;</a><br>'
    '<a href="https://www.cnbc.com/2026/08/28/kevin-warsh-jackson-hole-federal-reserve-inflation.html">CNBC &mdash; Warsh on inflation at Jackson Hole</a><br>'
    '<a href="https://www.chase.com/personal/investments/learning-and-insights/article/september-2026-rate-hike-now-expected-amid-energy-shocks">Chase &mdash; September 2026 rate hike now expected amid energy shocks</a><br>'
    '<a href="https://www.benzinga.com/markets/earnings/26/09/61563224/credo-technology-reports-q1-results-shares-slip">Benzinga &mdash; Credo Technology reports Q1 results, shares slip</a><br>'
    '<a href="https://en.cryptonomist.ch/2026/09/02/credo-technology-group-holding-stock-drops-despite-115-revenue-surge-to-479m/">Credo Q1 2027 revenue and margin detail</a><br>'
    '<a href="https://www.reuters.com/business/energy/oil-up-nearly-1-us-iran-trade-fresh-strikes-2026-09-02/">Reuters &mdash; oil and the U.S.&ndash;Iran exchange of fire</a><br>'
    '<a href="https://www.cnbc.com/2026/09/02/us-iran-war-trump-hormuz-irgc-jordan-bahrain.html">CNBC &mdash; tankers struck naval mines in the Strait of Hormuz</a><br>'
    '<a href="https://www.cnbc.com/2026/09/02/g20-innovation-ministerial-live-updates.html">CNBC &mdash; Lutnick on a semiconductor tariff framework</a>'
    '</div>')
ws_body.append(PROV)
ws_body.append('<div class="disc">For information only. Nothing on this page is investment advice, a recommendation, or an '
    'offer to buy or sell any security. Live widgets are supplied by TradingView and may be delayed. Intraday figures are '
    'point-in-time reads with their clocks stated; only the Weekly Scorecard carries official closes.</div>')

# ============================================================ CYBER
cy_body = []
cy_body.append('<header class="masthead"><h1>The Cyber Wire</h1>'
    '<p class="tag">Your daily security briefing &mdash; breaches, vulnerabilities &amp; federal deadlines</p>' + meta() + '</header>')
cy_body.append('<div class="tldr"><b>The Wire</b> <span>A federal patch deadline for an actively exploited MLflow flaw '
    'falls today, while SonicWall’s SMA1000 appliance is dealing with its second pair of exploited zero-days in seven '
    'weeks and attackers are minting admin credentials on unpatched JFrog Artifactory servers.</span></div>')
cy_body.append(FRESH)
cy_body.append(nav("cy"))

cy_body.append('<div class="banner" style="border-color:var(--crit);background:var(--panel)">'
    '<span class="lvl" style="color:var(--crit)">Threat Level: High</span>'
    '<span class="why">A CVSS 10.0 pre-authentication flaw and a critical authentication bypass are both confirmed '
    'exploited in the wild right now, and a CISA federal remediation deadline for a third actively exploited flaw expires '
    'today.</span></div>')

cy_body.append('<div class="stats">'
    '<div class="stat"><div class="n">10.0</div><div class="l">CVSS &mdash; SonicWall CVE-2026-83548</div></div>'
    '<div class="stat"><div class="n">284M</div><div class="l">Records ShinyHunters claims from McKesson</div></div>'
    '<div class="stat"><div class="n">~22,000</div><div class="l">Exchange servers still exposed</div></div>'
    '<div class="stat"><div class="n">0 days</div><div class="l">Left on the MLflow KEV deadline</div></div></div>')

cy_body.append('<h2>Top Story</h2>')
cy_body.append('<div class="panel" style="border-left:3px solid var(--accent)">'
    '<h3 style="margin:0 0 9px;font-size:19px">SonicWall’s SMA1000 has now had two exploited zero-day pairs in seven '
    'weeks &mdash; and they are different CVEs</h3>'
    '<p style="margin:0 0 10px;color:var(--muted2)">SonicWall advisory <b>SNWLID-2026-0016</b>, published September 1, 2026, '
    'confirms its Product Security Incident Response Team investigated a case indicating active exploitation of two flaws in '
    'the SMA1000 Series secure mobile access appliances. <b>CVE-2026-83548</b> is a pre-authentication server-side request '
    'forgery vulnerability in the Appliance Work Place interface carrying a <b>CVSS score of 10.0</b>. '
    '<b>CVE-2026-83549</b> is an authenticated OS command injection issue in the Appliance Management Console at <b>CVSS 7.8</b>, '
    'which can result in remote code execution. SonicWall says it observed exploitation of both, which reporting reads as '
    'chaining &mdash; that inference belongs to the reporting, not to a vendor statement.</p>'
    '<p style="margin:0 0 10px;color:var(--muted2)"><b>New this edition, and it changes the shape of the story:</b> a Tenable '
    'advisory published <b>July 15, 2026</b> documents a <i>separate</i> exploited SMA1000 pair &mdash; <b>CVE-2026-15409</b>, '
    'an SSRF in the SMA 1000 Workplace interface at CVSS 10, and <b>CVE-2026-15410</b>, a code injection flaw in the Appliance '
    'Management Console at CVSS 7.2 &mdash; disclosed July 14 under advisory <b>SNWLID-2026-0008</b>. Different CVE IDs, '
    'different advisory, seven weeks earlier, and the same two-component shape: an unauthenticated SSRF at the Workplace '
    'front door chained into command execution on the management console behind it.</p>'
    '<p style="margin:0 0 10px;color:var(--muted2)">Both July flaws were added to the CISA KEV catalog on <b>July 14 with a '
    'remediation date of Friday, July 17</b> &mdash; a three-day window, not the standard three weeks. Tenable’s fixed '
    'versions for that pair are <b>12.4.3-03453 and later</b> and <b>12.5.0-02835 and later</b>. The September pair’s '
    'fixes are hotfix 12.4.3-03526 / 12.5.0-02952 or higher, and SSL-VPN on firewalls and the SMA100 line are not affected.</p>'
    '<p style="margin:0;color:var(--muted2)">The practical reading for defenders: these appliances sit on the internet by '
    'design and aggregate remote-access credentials, which is why Tenable calls them high-value targets &mdash; a compromise '
    'at the appliance level yields administrator credentials, VPN session tokens and a map of the network behind the gateway. '
    'An organisation that patched in July is not covered for September.</p></div>')

cy_body.append('<div class="callout crit"><h3>Patch Priority &mdash; CVE-2026-64849, MLflow: the federal deadline is TODAY</h3>'
    '<p><b>MLflow server-side request forgery, actively exploited, affecting MLflow versions prior to 3.15.0.</b> Added to '
    'the CISA KEV catalog on August 19, 2026 with a remediation due date of <b>September 2, 2026</b> &mdash; '
    '<b id="kev1"></b>. Under BOD 22-01 that deadline is binding on federal civilian agencies today; upgrade to 3.15.0 or '
    'later.</p>'
    '<p style="margin-top:8px">This box sits on the <b>deadline</b> limb, not the severity limb. The SonicWall SMA1000 pair '
    'above is max-severity and confirmed exploited, but <b>no federal clock for it was sourced this run</b>, so it cannot '
    'outrank an expiring deadline &mdash; and the standing rule that an elapsed deadline outranks a live advisory does not '
    'reach a flaw with no deadline at all. The next clock after today is <b>CVE-2026-72530 (TrueConf Server), due September '
    '3 &mdash; <span id="kev2"></span></b>. Both dates match the KEV section below exactly.</p></div>')

cy_body.append('<h2>Threat Actor Spotlight</h2>')
cy_body.append('<div class="card"><div class="tags"><span class="tag t-c">Extortion</span><span class="tag t-w">Vishing</span>'
    '<span class="tag t-a">Identity abuse</span></div>'
    '<h3>ShinyHunters &mdash; phones first, SaaS second</h3>'
    '<p>The group told BleepingComputer it was behind the McKesson intrusion, saying it gained access through <b>voice '
    'phishing against multiple McKesson employees</b>, then used <b>compromised Okta single-sign-on accounts to reach '
    'Salesforce and Snowflake environments</b>. It claims <b>284 million records</b> including personal and protected '
    'health information, and has threatened publication unless the company opened payment negotiations by <b>September 1</b>, '
    'with a demand reported at approximately <b>$55 million</b>.</p>'
    '<p>The tradecraft is worth separating from the tooling: nothing in that chain is a software vulnerability. A help-desk '
    'phone call defeated the identity provider, and the identity provider was the key to two data platforms. Controls that '
    'assume the attacker starts at a network edge do not see this path.</p>'
    '<p class="note" style="margin-bottom:0">Boston Scientific has <b>not</b> named ShinyHunters over its own incident and '
    'the group has not publicly claimed it. The two are not linked here.</p></div>')

cy_body.append('<h2>Breaches &amp; Incidents</h2>')
cy_body.append('<div class="cards">'
    '<div class="card"><div class="tags"><span class="tag t-c">Healthcare</span><span class="tag t-new">New</span></div>'
    '<h3>McKesson confirms a cyber incident as the extortion clock runs</h3>'
    '<p>The U.S. healthcare distribution giant acknowledged a breach in late August 2026. ShinyHunters claims the theft of '
    '<b>284 million records</b> containing PII and PHI and is demanding roughly <b>$55 million</b>, with a stated deadline '
    'of September 1 for the company to begin negotiations.</p></div>'

    '<div class="card"><div class="tags"><span class="tag t-c">Manufacturing</span><span class="tag t-new">New</span></div>'
    '<h3>Boston Scientific incident is disrupting orders and shipping</h3>'
    '<p>The medical-device maker says the incident has <b>prevented access to certain operating systems and business '
    'applications</b> and is affecting its ability to process and ship customer orders. No threat actor has been named by '
    'the company and none has publicly claimed it.</p>'
    '<p class="note" style="margin-bottom:0">This is an operational-disruption incident, not a confirmed data-theft one, on '
    'what has been reported so far.</p></div>'

    '<div class="card"><div class="tags"><span class="tag t-c">Exploited</span><span class="tag t-a">Supply chain</span>'
    '<span class="tag t-new">New</span></div>'
    '<h3>JFrog Artifactory: attackers are minting administrator credentials</h3>'
    '<p><b>CVE-2026-82329</b>, an improper-authentication flaw in JFrog Artifactory, is being actively exploited. Under '
    'default configuration an unauthenticated attacker with network access can obtain administrative privileges. The '
    'mechanism: instances that were never given an <b>additional join key</b> receive a <b>&ldquo;phantom&rdquo; join key</b> '
    'an attacker forges to mint administrator-level credentials.</p>'
    '<p>A valid administrator token gives control of repositories, user accounts, access permissions, build artifacts and '
    'stored packages &mdash; which is why an artifact repository compromise is a supply-chain event rather than a single-host '
    'one. Exploitation was observed on internet-exposed systems <b>within days of the patch being released</b>. '
    '<b>Self-hosted deployments only</b>; the JFrog SaaS platform is not affected.</p>'
    '<p class="note" style="margin-bottom:0">Reporting states explicitly that this exploitation is <b>not</b> related to the '
    'OpenAI/Hugging Face incident, and that the flaw is improper authentication rather than RCE. Both clarifications are '
    'carried because both errors were circulating.</p></div>'

    '<div class="card"><div class="tags"><span class="tag t-w">Exposure</span><span class="tag t-new">New</span></div>'
    '<h3>Nearly 22,000 Exchange servers still exposed three weeks after the fix</h3>'
    '<p><b>CVE-2026-62911</b> is a critical authentication bypass in Microsoft Exchange with <b>public exploit code online</b>. '
    'Microsoft released the fix on <b>August 11, 2026</b>, and roughly <b>22,000 servers remain exposed</b>.</p>'
    '<p class="note" style="margin-bottom:0">No source fetched this run states in-the-wild exploitation of this flaw, so '
    'none is asserted &mdash; the number is an exposure count, not a victim count.</p></div>'
    '</div>')

cy_body.append('<h2>Vulnerability Watch</h2>')
cy_body.append('<table><thead><tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr></thead><tbody>'
    '<tr><td>CVE-2026-83548</td><td class="down">10.0</td><td>SonicWall SMA1000 (6210, 7210, 8200v)</td>'
    '<td>Pre-auth SSRF in the Appliance Work Place interface; exploitation observed by SonicWall PSIRT (SNWLID-2026-0016, Sept 1)</td></tr>'
    '<tr><td>CVE-2026-83549</td><td class="down">7.8</td><td>SonicWall SMA1000 Appliance Management Console</td>'
    '<td>Authenticated OS command injection → possible RCE; exploitation observed; read by reporting as chained with 83548</td></tr>'
    '<tr><td>CVE-2026-15409</td><td class="down">10</td><td>SonicWall SMA 1000 Workplace interface</td>'
    '<td>SSRF; exploited as a zero-day in July 2026 (SNWLID-2026-0008). Fixed 12.4.3-03453+ / 12.5.0-02835+. A <b>different</b> flaw from 83548</td></tr>'
    '<tr><td>CVE-2026-15410</td><td class="down">7.2</td><td>SonicWall SMA 1000 Appliance Management Console</td>'
    '<td>Code injection; chained with 15409 for unauthenticated command execution</td></tr>'
    '<tr><td>CVE-2026-82329</td><td class="flat">not taken from the vendor this run</td><td>JFrog Artifactory (self-hosted only)</td>'
    '<td>Improper authentication → administrator token via forged &ldquo;phantom&rdquo; join key; actively exploited</td></tr>'
    '<tr><td>CVE-2026-62911</td><td class="flat">not sourced this run</td><td>Microsoft Exchange</td>'
    '<td>Critical authentication bypass; public exploit code; fix released Aug 11, 2026; ~22,000 servers still exposed</td></tr>'
    '<tr><td>CVE-2026-64849</td><td class="flat">not sourced this run</td><td>MLflow, versions prior to 3.15.0</td>'
    '<td>Server-side request forgery; actively exploited; KEV due <b>today</b></td></tr>'
    '<tr><td>CVE-2026-72530</td><td class="flat">not sourced this run</td><td>TrueConf Server 5.3.x&ndash;5.3.9, 5.4.x&ndash;5.4.9, 5.5.x&ndash;5.5.5</td>'
    '<td>Code injection via port 4307/TCP escaping the isolated environment; patch is 5.5.6+; KEV due Sept 3</td></tr>'
    '</tbody></table>')
cy_body.append('<div class="note">Where the CVSS column says <b>not sourced this run</b>, no vendor advisory or NVD figure '
    'was fetched, so no number is printed. A widely circulated third-party score exists for the JFrog flaw; it is not '
    'reproduced here, because this desk has twice published a blog CVSS that the vendor later contradicted, and a missing '
    'number is cheaper than a wrong one.</div>')

cy_body.append('<h2>CISA KEV &amp; Federal Deadlines</h2>')
cy_body.append('<ul class="bul">'
    '<li><b>CVE-2026-64849 &mdash; MLflow SSRF.</b> Added August 19, 2026; remediation due <b>September 2, 2026</b> '
    '&mdash; <b id="kevA"></b>. <span class="tag t-c">Patch Priority</span></li>'
    '<li><b>CVE-2026-72530 &mdash; TrueConf Server code injection.</b> Added August 20, 2026; due <b>September 3, 2026</b> '
    '&mdash; <b id="kevB"></b>. Patch is TrueConf Server 5.5.6 or later.</li>'
    '<li><b>CVE-2021-23758.</b> Added August 26, 2026; due <b>September 9, 2026</b> &mdash; <b id="kevC"></b>. '
    'The affected product was not stated in anything fetched this run, so none is named.</li>'
    '<li><b>CVE-2026-66384.</b> Added August 27, 2026; due <b>September 10, 2026</b> &mdash; <b id="kevD"></b>. '
    'The affected product was not stated in anything fetched this run, so none is named.</li>'
    '<li><b>CVE-2026-81578.</b> Added August 31, 2026; due <b>September 14, 2026</b> &mdash; <b id="kevE"></b>. '
    'Earlier editions today identified this as one of a PaperCut pair; the product was not re-confirmed this run and the '
    'date is what is published.</li>'
    '<li><b>Citrix CVE-2026-8452 &mdash; no deadline is published this edition.</b> A search this run places it as '
    'KEV-added on <b>August 26, 2026</b>, while editions earlier today carried an <b>August 29</b> due date. Those two are '
    'not reconcilable under any single window, neither was confirmed against the CISA catalog this run, and so no Citrix '
    'countdown appears on this page. The absence is deliberate and is recorded rather than quietly dropped.</li>'
    '</ul>')
cy_body.append('<div class="note">Standard BOD 22-01 windows run three weeks from the add date, but shortened windows are '
    'real and are not an error to be corrected: the July SonicWall pair above was added July 14 and due <b>July 17</b>. '
    'Every countdown on this page is computed in your browser from today’s date to the due date printed beside it.</div>')

cy_body.append('<h2>Sources</h2><div class="panel srcs">'
    '<a href="https://www.securityweek.com/sonicwall-warns-of-two-sma1000-zero-days-exploited-in-attacks/">SecurityWeek &mdash; SonicWall warns of two SMA1000 zero-days exploited in attacks</a><br>'
    '<a href="https://thehackernews.com/2026/09/attackers-exploit-two-sonicwall-sma.html">The Hacker News &mdash; attackers exploit two SonicWall SMA 1000 zero-days</a><br>'
    '<a href="https://www.tenable.com/blog/cve-2026-15409-cve-2026-15410-sonicwall-sma-1000-zero-day-vulnerabilities-exploited-in-the">Tenable &mdash; CVE-2026-15409, CVE-2026-15410: SonicWall SMA 1000 zero-days exploited in the wild (July 15, 2026)</a><br>'
    '<a href="https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0008">SonicWall PSIRT &mdash; advisory SNWLID-2026-0008</a><br>'
    '<a href="https://thehackernews.com/2026/09/attackers-exploit-critical-jfrog.html">The Hacker News &mdash; attackers exploit critical JFrog Artifactory flaw to mint admin credentials</a><br>'
    '<a href="https://www.securityweek.com/critical-jfrog-artifactory-vulnerability-reportedly-exploited-in-the-wild/">SecurityWeek &mdash; critical JFrog Artifactory vulnerability reportedly exploited in the wild</a><br>'
    '<a href="https://www.ionix.io/threat-center/cve-2026-82329/">IONIX threat center &mdash; CVE-2026-82329</a><br>'
    '<a href="https://www.helpnetsecurity.com/2026/09/02/microsoft-exchange-cve-2026-62911-critical-authentication-bypass-flaw/">Help Net Security &mdash; ~22,000 Exchange servers exposed to CVE-2026-62911</a><br>'
    '<a href="https://www.securityweek.com/mckesson-confirms-data-breach-as-attacker-deadline-looms/">SecurityWeek &mdash; McKesson confirms data breach as attacker deadline looms</a><br>'
    '<a href="https://www.malwarebytes.com/blog/news/2026/08/mckesson-confirms-cyber-incident-after-shinyhunters-claims-patient-data-theft">Malwarebytes &mdash; McKesson confirms cyber incident after ShinyHunters claims</a><br>'
    '<a href="https://www.hipaajournal.com/boston-scientific-cyberattack/">HIPAA Journal &mdash; Boston Scientific cyberattack impacting operations</a><br>'
    '<a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">CISA &mdash; Known Exploited Vulnerabilities Catalog</a><br>'
    '<a href="https://www.cisa.gov/news-events/alerts/2026/08/19/cisa-adds-one-known-exploited-vulnerability-catalog">CISA &mdash; alert adding CVE-2026-64849 (Aug 19, 2026)</a>'
    '</div>')
cy_body.append(PROV)
cy_body.append('<div class="disc">For information only. Vulnerability details, CVSS scores and remediation dates change as '
    'vendors and CISA update their advisories; verify against the vendor bulletin and the CISA KEV catalog before acting. '
    'Nothing here is a substitute for your own incident-response process.</div>')

cy_kev = """<script>(function(){function d(id,y,m,dy){var e=document.getElementById(id);if(!e)return;
var n=new Date();var t=new Date(n.getFullYear(),n.getMonth(),n.getDate());var due=new Date(y,m-1,dy);
var k=Math.round((due-t)/86400000);var s,c;if(k>1){s=k+' days left';c='';}else if(k===1){s='1 day left';c='var(--warn)';}
else if(k===0){s='due today \\u2014 0 days left';c='var(--crit)';}else{s=Math.abs(k)+' days overdue';c='var(--crit)';}
e.textContent=s;if(c)e.style.color=c;}
d('kev1',2026,9,2);d('kev2',2026,9,3);d('kevA',2026,9,2);d('kevB',2026,9,3);d('kevC',2026,9,9);d('kevD',2026,9,10);d('kevE',2026,9,14);})();</script>"""

# ============================================================ MMA
mma_body = []
mma_body.append('<header class="masthead"><h1>The Octagon</h1>'
    '<p class="tag">Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting</p>' + meta() + '</header>')
mma_body.append('<div class="tldr"><b>Tale of the Tape</b> <span>Adam Darby headlined Contender Series Week 4 with a '
    'third-round doctor stoppage of Patrick Rivera, was one of five fighters handed a UFC contract on the night, and is '
    'already asking Dana White to put him on Saturday’s Paris card.</span></div>')
mma_body.append(FRESH)
mma_body.append(nav("mma"))

mma_body.append('<div class="cdn"><span class="lab">Next Card</span><span class="val" id="ufccdn">&mdash;</span>'
    '<span class="ev">UFC Fight Night 287: Hooker vs. Parnasse &mdash; Sat, Sept 5, Accor Arena, Paris '
    '(prelims noon ET / main card 3 PM ET)</span></div>')

mma_body.append('<h2>Top Story</h2>')
mma_body.append('<div class="panel" style="border-left:3px solid var(--accent)">'
    '<h3 style="margin:0 0 9px;font-size:19px">Adam Darby banked an eight-year-old note-app promise, and he wants to cash '
    'it in on Saturday</h3>'
    '<p style="margin:0 0 10px;color:var(--muted2)"><b>Adam Darby (8-1)</b> met <b>Patrick Rivera (13-5)</b> in the main '
    'event of <b>Week 4 of Dana White’s Contender Series</b> on <b>September 1</b>. Darby broke Rivera down until '
    'referee <b>Kerry Hatley</b> called in the cageside doctor, who saw enough damage to stop the fight <b>midway into the '
    'third round</b>. Darby earned a UFC contract for the performance.</p>'
    '<p style="margin:0 0 10px;color:var(--muted2)">He had posted a screenshot from his phone’s notes app last week, '
    'written while he was still an amateur in 2018. &ldquo;This has been in the making for 10 years,&rdquo; Darby said. '
    '&ldquo;In my notes app on my phone, I put one life, one chance, UFC or nothing else. That was eight years ago, and '
    'I’ve lived with it ever since&hellip; I’m not just here to stay here and not fight. I’m going to fight '
    'as soon as possible. So, I’m gonna ask Dana to get me on as soon as possible&hellip; They want me out next weekend. '
    'I’m good to go. Sept. 5, France.&rdquo;</p>'
    '<p style="margin:0;color:var(--muted2)"><b>A correction made inside this edition, and worth stating plainly.</b> An '
    'early search summary this run rendered the result as a &ldquo;TKO victory over Kerry Hatley in Round 3.&rdquo; '
    '<b>Hatley is the referee, not the opponent.</b> The opponent was Patrick Rivera, and the fight ended on a doctor '
    'stoppage that Hatley called in. Nothing was published until the primary report was read; the summariser had turned an '
    'official into a fighter, and a plausible-looking sentence would have carried a fabricated opponent onto this page.</p></div>')

mma_body.append('<h2>Fight Week &mdash; Upcoming Cards</h2>')
mma_body.append('<div class="cards">'
    '<div class="card"><div class="tags"><span class="tag t-c">Next up</span></div>'
    '<p class="note" style="color:var(--accent);margin:0 0 6px">SEPT 5 &middot; ACCOR ARENA, PARIS</p>'
    '<h3>UFC Fight Night 287: Hooker vs. Parnasse</h3>'
    '<p>Dan Hooker meets <b>Salahdine Parnasse</b>, who is being given a main event on his UFC debut. Prelims at noon ET, '
    'main card at 3 PM ET.</p>'
    '<p><b>Odds:</b> Parnasse −667 / Hooker +417 at one book; <b>DraftKings</b> Parnasse −600 / Hooker +440. '
    'Across books the band runs roughly <b>Parnasse −500 to −700</b> and <b>Hooker +360 to +450</b>. No average is '
    'taken. The line <b>opened</b> near Parnasse −400 / Hooker +300 and has moved further toward Parnasse since.</p></div>'

    '<div class="card">'
    '<p class="note" style="color:var(--accent);margin:0 0 6px">SEPT 12</p>'
    '<h3>UFC Fight Night 288: Noche UFC 4</h3>'
    '<p>Sherdog’s event calendar bills it <b>Noche UFC 4</b>; a separate schedule listing bills the same date as '
    '<b>Noche UFC: Silva vs Delgado</b>. Both renderings are printed and neither is adopted as the official billing. No '
    'venue was stated in either listing, so none is named.</p></div>'

    '<div class="card"><div class="tags"><span class="tag t-a">Title fight</span></div>'
    '<p class="note" style="color:var(--accent);margin:0 0 6px">SEPT 19 &middot; CRYPTO.COM ARENA, LOS ANGELES</p>'
    '<h3>UFC 331: Van vs. Pantoja 2</h3>'
    '<p>Flyweight champion Joshua Van rematches Alexandre Pantoja, the man he took the belt from. Main card at 9 PM ET / '
    '6 PM PT on Paramount+.</p>'
    '<p><b>Odds:</b> Sherdog headlines its odds story &ldquo;UFC 331 odds revealed: Joshua Van an underdog, Gable Steveson '
    '−1500.&rdquo; That is the headline’s wording; the champion being an underdog in his own defence is the '
    'notable part, and no per-fighter price for the main event was stated in anything fetched this run, so none is printed.</p></div>'

    '<div class="card">'
    '<p class="note" style="color:var(--accent);margin:0 0 6px">SEPT 26 &middot; META APEX, LAS VEGAS</p>'
    '<h3>UFC Fight Night 289</h3>'
    '<p>Sherdog’s calendar bills it <b>Barcelos vs. Rosas Jr.</b>; a schedule listing reverses the order to '
    '<b>Rosas Jr. vs. Barcelos</b> and gives a 6 PM ET / 3 PM PT main card on Paramount+. Both orderings are printed; the '
    'billing order determines who is the nominal headliner and the two sources disagree about it.</p></div>'

    '<div class="card">'
    '<p class="note" style="color:var(--accent);margin:0 0 6px">OCT 3</p>'
    '<h3>UFC 332: TBA</h3>'
    '<p>On Sherdog’s calendar with no announced headliner. No venue and no bouts are listed, so none are named.</p></div>'
    '</div>')

mma_body.append('<h2>Last Event &mdash; Results</h2>')
mma_body.append('<div class="note">UFC Shanghai (UFC Fight Night: Nurmagomedov vs. Song), <b>August 29, 2026</b> &mdash; '
    'still the most recent <b>completed</b> UFC event. Contender Series Week 4 on September 1 is a Contender Series card, '
    'not a UFC event, and is covered under Prospect Watch below.</div>')
mma_body.append('<table><thead><tr><th>Result</th><th>Bout</th><th>Method</th></tr></thead><tbody>'
    '<tr><td class="up">Song Yadong</td><td>def. Umar Nurmagomedov <span class="note" style="display:inline">(main event)</span></td><td>KO (right uppercut), R2 1:48</td></tr>'
    '<tr><td class="up">Denise Gomes</td><td>def. Yan Xiaonan <span class="note" style="display:inline">(co-main)</span></td><td>TKO (strikes), R1 4:49</td></tr>'
    '<tr><td class="up">Kai Asakura</td><td>def. Aoriqileng</td><td>TKO (strikes), R2 0:34</td></tr>'
    '<tr><td class="up">Sumudaerji</td><td>def. Alex Perez</td><td>Unanimous decision (29-28, 29-28, 29-28)</td></tr>'
    '<tr><td class="up">Hector Santiago</td><td>def. Lawrence Lui</td><td>KO (punches), R2 0:53</td></tr>'
    '<tr><td class="up">Julia Polastri</td><td>def. Xiong Jingnan</td><td>KO (head kick), R1 3:06</td></tr>'
    '<tr><td class="up">Cam Nelson</td><td>def. Ding Meng <span class="note" style="display:inline">(prelims)</span></td><td>Unanimous decision (29-28, 29-28, 29-28)</td></tr>'
    '</tbody></table>')
mma_body.append('<div class="note"><b>Bonuses, carried and labelled.</b> Performance of the Night, $100,000 each: '
    '<b>Song Yadong</b> and <b>Bilal Hasan</b>. Fight of the Night, $100,000 each: <b>Liu Ce</b> and <b>Levi Rodrigues Jr.</b> '
    'These were sourced in an earlier edition today and are recorded in this desk’s standing corrections file; they were '
    '<b>not</b> re-verified in this run’s searches, and are printed on that basis rather than as a fresh confirmation. '
    'No total finish count for the card is asserted, because no source gives one.</div>')

mma_body.append('<h2>Prospect Watch</h2>')
mma_body.append('<div class="note">Dana White’s Contender Series, Season 10, Week 4 &mdash; September 1, Meta Apex, '
    'Las Vegas. <b>All five winners were awarded UFC contracts.</b></div>')
mma_body.append('<div class="cards">'
    '<div class="card"><div class="tags"><span class="tag t-new">Prospect</span><span class="tag t-a">Contract</span></div>'
    '<h3>Adam Darby (8-1)</h3><p>TKO (doctor stoppage, R3) over Patrick Rivera (13-5) in the main event. Wants a Paris slot '
    'on Sept 5.</p></div>'
    '<div class="card"><div class="tags"><span class="tag t-new">Prospect</span><span class="tag t-a">Contract</span></div>'
    '<h3>Modestino Rodrigues</h3><p>TKO (punches), Round 1, over Brandon Holmes.</p></div>'
    '<div class="card"><div class="tags"><span class="tag t-new">Prospect</span><span class="tag t-a">Contract</span></div>'
    '<h3>Silvestre Sanchez</h3><p>KO (punch), Round 3, over Liam McCraken.</p>'
    '<p class="note" style="margin-bottom:0">This run’s read renders the opponent <b>McCraken</b>; an earlier edition '
    'read it <b>McCracken</b>. The variance is flagged and not resolved.</p></div>'
    '<div class="card"><div class="tags"><span class="tag t-new">Prospect</span><span class="tag t-a">Contract</span></div>'
    '<h3>Gabriel Loren&ccedil;o</h3><p>KO (elbow and punches), Round 1, over Charlie Cleveland.</p>'
    '<p class="note" style="margin-bottom:0">Earlier editions today <b>withheld this name</b> because reports rendered it '
    'both &ldquo;Loren&ccedil;o&rdquo; and &ldquo;Lourenco.&rdquo; This run’s read gives <b>Gabriel Loren&ccedil;o</b> '
    'consistently, and the name is published on that basis with the earlier variant recorded.</p></div>'
    '<div class="card"><div class="tags"><span class="tag t-new">Prospect</span><span class="tag t-a">Contract</span></div>'
    '<h3>Adam Livingston</h3><p>Split decision over Hunter Smith &mdash; the only bout of the five to reach the scorecards.</p></div>'
    '</div>')

mma_body.append('<h2>Around the Sport</h2>')
mma_body.append('<ul class="bul">'
    '<li><b>Dan Hooker on his form.</b> Sherdog, September 2: &ldquo;Dan Hooker admits distractions crept in before recent '
    'UFC struggles.&rdquo; Four days out from a main event in which he is a substantial underdog.</li>'
    '<li><b>Justin Gaethje on his career.</b> Sherdog, September 2: &ldquo;Justin Gaethje says his UFC legacy is '
    '&lsquo;fulfilled&rsquo; after Topuria win.&rdquo; Gaethje took the undisputed lightweight belt from Ilia Topuria at '
    'Freedom 250 on June 14, 2026.</li>'
    '<li><b>A Vegas main event is set.</b> Sherdog, September 2: &ldquo;Brendan Allen, Christian Leroy Duncan collide in '
    'UFC Vegas 122 main event.&rdquo; No date for that card was given in anything fetched this run, so none is stated.</li>'
    '<li><b>A sixth contract, separately reported.</b> Sherdog, September 2: &ldquo;Dana White hands UFC deal to 22-year-old '
    'following controversial 15-second KO.&rdquo; The fighter is not named in the headline and the card is not identified, '
    'so neither is supplied here.</li>'
    '<li><b>A Contender Series result this desk will not describe.</b> Three separate Sherdog items on September 2 reference '
    'a &ldquo;historic&rdquo; and &ldquo;stunning&rdquo; DWCS upset involving <b>Bella Mir</b>, daughter of Frank Mir, and '
    'the backlash to it. <b>Nothing fetched this run states the actual result</b>, so no outcome is asserted &mdash; only '
    'that the coverage exists.</li>'
    '<li><b>Hooker names a price.</b> Sherdog, September 2: &ldquo;Dan Hooker says he’d fight Francis Ngannou for the '
    'right price.&rdquo;</li></ul>')

mma_body.append('<h2>Rankings &amp; Business</h2>')
mma_body.append('<div class="cards">'
    '<div class="card"><h3>Rankings movement</h3>'
    '<p>Sherdog’s divisional rankings update is headlined <b>&ldquo;UFC Shanghai stunner sends Yadong Song soaring in '
    'Sherdog Rankings&rdquo;</b> &mdash; consistent with his round-two knockout of Umar Nurmagomedov in the results table '
    'above.</p>'
    '<p>Sherdog’s pound-for-pound list is headlined <b>&ldquo;Islam Makhachev remains No. 1.&rdquo;</b> Its women’s '
    'pound-for-pound update: <b>&ldquo;Tatiana Suarez in, Taila Santos out.&rdquo;</b></p>'
    '<p class="note" style="margin-bottom:0">These are Sherdog’s own rankings, not the official UFC rankings, and are '
    'described here in the publisher’s own headline wording. No ordinal position beyond Makhachev at No. 1 is stated, '
    'because none was fetched.</p></div>'
    '<div class="card"><h3>Business &amp; broadcast</h3>'
    '<p>Every September UFC event listed on this page streams on <b>Paramount+</b> per the schedule listings fetched this run.</p>'
    '<p><b>No viewership, gate, purse or TKO Group financial figure was sourced this run, so none is published.</b> This '
    'section stays empty of numbers rather than reaching for last month’s.</p></div>'
    '</div>')

mma_body.append('<h2>Champions Board</h2>')
mma_body.append('<table><thead><tr><th>Division</th><th>Champion</th><th>Note</th></tr></thead><tbody>'
    '<tr><td>Heavyweight</td><td>Tom Aspinall</td><td>Undisputed; inherited June 21, 2025</td></tr>'
    '<tr><td>Heavyweight (interim)</td><td>Ciryl Gane</td><td>KO2 Alex Pereira, Freedom 250, June 14, 2026</td></tr>'
    '<tr><td>Light Heavyweight</td><td>Carlos Ulberg</td><td>Won the vacant belt KO1 over Ji&#345;&iacute; Proch&aacute;zka, UFC 327, April 11, 2026</td></tr>'
    '<tr><td>Middleweight</td><td>Sean Strickland</td><td>Split decision over Khamzat Chimaev, UFC 328, May 9, 2026 &mdash; two-time champion</td></tr>'
    '<tr><td>Welterweight</td><td>Islam Makhachev</td><td>Won November 15, 2025; one defence &mdash; UD Ian Machado Garry, UFC 330, August 15, 2026</td></tr>'
    '<tr><td>Lightweight</td><td>Justin Gaethje</td><td>TKO4 Ilia Topuria, Freedom 250, June 14, 2026</td></tr>'
    '<tr><td>Featherweight</td><td>Alexander Volkanovski</td><td>Won April 12, 2025; defended UD over Diego Lopes, UFC 325, January 31, 2026</td></tr>'
    '<tr><td>Bantamweight</td><td>Petr Yan</td><td>UD over Merab Dvalishvili, UFC 323, December 6, 2025</td></tr>'
    '<tr><td>Flyweight</td><td>Joshua Van</td><td>TKO1 Alexandre Pantoja, UFC 323, December 6, 2025; one defence, TKO5 Tatsuro Taira, UFC 328 &mdash; rematches Pantoja at UFC 331</td></tr>'
    '<tr><td>Women’s Bantamweight</td><td>Kayla Harrison</td><td>Won June 7, 2025; <b>zero defences</b></td></tr>'
    '<tr><td>Women’s Flyweight</td><td>Valentina Shevchenko</td><td>Won September 14, 2024</td></tr>'
    '<tr><td>Women’s Strawweight</td><td>Mackenzie Dern</td><td>Won October 25, 2025; one defence &mdash; UD Gillian Robertson, UFC 330, August 15, 2026</td></tr>'
    '</tbody></table>')
mma_body.append('<div class="note"><b>The stale middleweight cell came back for a nineteenth consecutive edition.</b> A '
    'fresh search this run returned &ldquo;Middleweight: Khamzat Chimaev, won August 16, 2025.&rdquo; That is superseded: '
    '<b>Sean Strickland</b> beat Chimaev by split decision at <b>UFC 328 on May 9, 2026</b> to become a two-time champion, '
    'and Chimaev has not held the belt since. Every one of the eleven other cells in that search matched this board. The '
    'same search also offered &ldquo;Women’s Featherweight: Vacant&rdquo; &mdash; a division this board does not carry, '
    'and it is not added, because adding a row on a summariser’s word is how a board grows a wrong one.</div>')

mma_body.append('<h2>Sources</h2><div class="panel srcs">'
    '<a href="https://www.sherdog.com/news/news/New-UFC-fighter-predicted-his-signing-8-years-ago-UFC-or-nothing-else-202623">Sherdog &mdash; Adam Darby fulfils eight-year UFC prediction with DWCS contract (Sept 2, 2026)</a><br>'
    '<a href="https://www.sherdog.com/news/news/Dana-White-awards-5-UFC-contracts-after-wild-DWCS-Week-4-202619">Sherdog &mdash; Dana White awards 5 UFC contracts after wild DWCS Week 4</a><br>'
    '<a href="https://www.cbssports.com/ufc/news/dana-whites-contender-series-2026-week-4-results-winners-contracts-highlights/">CBS Sports &mdash; DWCS 2026 Week 4 results, winners and contracts</a><br>'
    '<a href="https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2">Sherdog &mdash; UFC event calendar (Sept 5, 12, 19, 26; Oct 3)</a><br>'
    '<a href="https://www.sherdog.com/news/news/UFC-331-odds-revealed-Joshua-Van-an-underdog-Gable-Steveson-1500-202630">Sherdog &mdash; UFC 331 odds revealed</a><br>'
    '<a href="https://www.rotowire.com/betting/mma/fight/salahdine-parnasse-vs-dan-hooker-odds-2026-09-05-5365">RotoWire &mdash; Hooker vs. Parnasse odds, Sept 5, 2026</a><br>'
    '<a href="https://www.mmaoddsbreaker.com/fight-odds/opening-odds/161246-opening-betting-odds-for-ufc-paris-hooker-vs-parnasse/">MMA Odds Breaker &mdash; opening odds for UFC Paris</a><br>'
    '<a href="https://www.ufc.com/event/ufc-fight-night-september-05-2026">UFC.com &mdash; UFC Fight Night: Hooker vs. Parnasse</a><br>'
    '<a href="https://www.ufc.com/news/ufc-shanghai-results-nurmagomedov-vs-song">UFC.com &mdash; UFC Shanghai main card results</a><br>'
    '<a href="https://www.ufc.com/news/ufc-shanghai-official-scorecards-nurmagomedov-vs-song">UFC.com &mdash; UFC Shanghai official scorecards</a><br>'
    '<a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">ESPN &mdash; Current and all-time UFC champions</a><br>'
    '<a href="https://www.paramountplus.com/sneak-peak/ufc-schedule-2026/">Paramount+ &mdash; UFC schedule 2026 (start times)</a>'
    '</div>')
mma_body.append(PROV)
mma_body.append('<div class="disc">Cards and bouts are subject to change. Betting odds move constantly and the prices above '
    'are point-in-time reads from the books named; they are not a recommendation to wager. Rankings cited are the '
    'publisher’s own and are not the official UFC rankings.</div>')

mma_cdn = """<script>(function(){var el=document.getElementById('ufccdn');if(!el)return;
var target=new Date('2026-09-05T15:00:00-04:00');function tick(){var n=new Date();var ms=target-n;
if(ms<=0){el.textContent='Fight week \\u2014 live/completed';return;}
var d=Math.floor(ms/86400000),h=Math.floor(ms%86400000/3600000),m=Math.floor(ms%3600000/60000);
el.textContent=d+'d '+h+'h '+m+'m';}tick();setInterval(tick,30000);})();</script>"""

# ============================================================ INDEX
ix_body = []
ix_body.append('<header class="masthead"><h1>Daily Briefings</h1>'
    '<p class="tag">Security, markets and MMA &mdash; refreshed every 30 minutes, 8 AM&ndash;6 PM ET</p>' + meta() + '</header>')
ix_body.append(FRESH)
ix_body.append(nav("ix"))
ix_body.append('<div class="big">'
    '<div class="card c-sec"><div class="kicker">⛨ The Cyber Wire &middot; The Wire</div>'
    '<h3>A federal patch deadline expires today</h3>'
    '<p>A federal patch deadline for an actively exploited MLflow flaw falls today, while SonicWall’s SMA1000 appliance '
    'is dealing with its second pair of exploited zero-days in seven weeks and attackers are minting admin credentials on '
    'unpatched JFrog Artifactory servers.</p>'
    '<a class="more" href="cyber-briefing.html">Read the briefing →</a></div>'

    '<div class="card c-mkt"><div class="kicker">▲ The Closing Bell &middot; The Tape</div>'
    '<h3>Higher stocks, higher yields</h3>'
    '<p>Stocks are narrowly higher at midmorning even as a global bond sell-off pushes the U.S. 10-year Treasury yield to '
    'its highest level since November 2023, with Dell up on AI-server demand while Credo Technology, MongoDB and Palo Alto '
    'Networks are all down sharply.</p>'
    '<a class="more" href="wallstreet-briefing.html">Read the briefing →</a></div>'

    '<div class="card c-mma"><div class="kicker">⊘ The Octagon &middot; Tale of the Tape</div>'
    '<h3>Five contracts, and one man asking for Saturday</h3>'
    '<p>Adam Darby headlined Contender Series Week 4 with a third-round doctor stoppage of Patrick Rivera, was one of five '
    'fighters handed a UFC contract on the night, and is already asking Dana White to put him on Saturday’s Paris card.</p>'
    '<a class="more" href="mma-briefing.html">Read the briefing →</a></div>'
    '</div>')
ix_body.append('<div class="disc">Each briefing is rebuilt from live web sources every 30 minutes between 8 AM and 6 PM ET. '
    'Every claim on every page traces to a source fetched during that run or to an explicitly labelled sourced entry from an '
    'earlier edition. Markets content is for information only and is not investment advice.</div>')

# ============================================================ WRITE
open(os.path.join(OUT, "index.html"), "w").write(
    page("Daily Briefings", "index", "".join(ix_body), "ix"))
open(os.path.join(OUT, "wallstreet-briefing.html"), "w").write(
    page("The Closing Bell &mdash; Daily Markets Briefing", "wallstreet", "".join(ws_body), "ws"))
open(os.path.join(OUT, "cyber-briefing.html"), "w").write(
    page("The Cyber Wire &mdash; Daily Security Briefing", "cyber", "".join(cy_body), "cy").replace(
        "</body>", cy_kev + "</body>"))
open(os.path.join(OUT, "mma-briefing.html"), "w").write(
    page("The Octagon &mdash; Daily MMA Briefing", "mma", "".join(mma_body), "mma").replace(
        "</body>", mma_cdn + "</body>"))

for f in ["index.html", "wallstreet-briefing.html", "cyber-briefing.html", "mma-briefing.html"]:
    print(f, os.path.getsize(os.path.join(OUT, f)))
