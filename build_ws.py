# -*- coding: utf-8 -*-
import shared, io

ACCENT = "#caa64a"; ACCENT2 = "#e8c766"
EXTRA = """
.mast h1,.lead h3,.card h3{font-family:Georgia,'Times New Roman',serif;font-weight:600}
.mast h1{letter-spacing:0}
"""
SUMMARY = ("Wall Street snapped a three-day losing streak on Wednesday, with the S&amp;P 500 closing up "
           "0.46% at 7,666.60 as Dell surged roughly 16% on record AI-server orders, even as Palo Alto "
           "Networks fell about 10% to finish worst in the index.")

TAPE = """<script type="application/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NYSE:DELL","title":"Dell"},{"proName":"NASDAQ:PANW","title":"Palo Alto"},{"proName":"NYSE:SNOW","title":"Snowflake"},{"proName":"NASDAQ:AVGO","title":"Broadcom"},{"proName":"NASDAQ:NVDA","title":"NVIDIA"},{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script>"""

def sq(sym):
    return ('<div class="ticker"><script type="application/javascript" '
            'src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>'
            '{"symbol":"%s","width":"100%%","colorTheme":"dark","isTransparent":true,"locale":"en"}'
            '</script></div>' % sym)

body = []
A = body.append

A('<header class="mast">')
A('<h1>&#9650; The Closing Bell</h1>')
A('<p class="tag">Your daily markets briefing &mdash; indexes, movers, rates &amp; what is next</p>')
A(shared.META)
A('</header>')
A(f'<div class="tldr"><b>The Tape</b> <span>{SUMMARY}</span></div>')
A('<p class="freshline" id="freshline">&nbsp;</p>')
A(shared.nav("ws", ACCENT))

# BLOCK A
A('<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>')
A(TAPE)
A('</div>')

# BLOCK B
A('<h2 class="sec">Live Index Quotes &mdash; updates in real time</h2>')
A('<div class="tickers">')
A(sq("FOREXCOM:SPXUSD")); A(sq("FOREXCOM:NSXUSD")); A(sq("FOREXCOM:DJI"))
A('</div>')
A('<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the latest '
  'edition; official closes are in the Weekly Scorecard.</div>')

# The Lead
A('<h2 class="sec">The Lead</h2>')
A('<div class="lead">')
A('<h3>Stocks snap a three-day slide as Dell\'s AI backlog does the heavy lifting &mdash; official close, '
  '4:00 PM ET</h3>')
A('<p>The <b>S&amp;P 500 advanced 0.46% to 7,666.60</b>, the <b>Nasdaq Composite gained 0.45% to 26,217.83</b>, '
  'and the <b>Dow Jones Industrial Average added 295.07 points, or 0.56%, to 53,061.95</b>. All three snapped a '
  'three-day losing streak, with the gains coming as Treasury yields eased slightly and the dollar weakened.</p>')
A('<p>The session\'s engine was <b>Dell Technologies</b>, which rose about <b>16%</b> after blowout results: '
  'sales up <b>58%</b> and adjusted EPS up <b>203%</b> in the quarter, with the AI-optimised server business '
  'doubling its revenue. The AI unit recorded <b>$61 billion in orders</b> and pushed backlog <b>above $95 '
  'billion</b>. Cutting the other way, <b>Palo Alto Networks</b> was the worst performer in the S&amp;P 500, '
  'down about <b>10%</b> despite reporting better-than-expected quarterly results. In the Dow, '
  '<b>Nvidia</b> was the best performer, up more than <b>3%</b>.</p>')
A('<p>These closing levels have now come back <b>identical on four independent fetches across four '
  'editions</b>, and they reconcile against Tuesday\'s closes, so they are published as levels rather than '
  'as percentage moves alone.</p>')
A('</div>')

# Movers
A('<h2 class="sec">Movers &amp; Drivers</h2>')
A('<div class="cards">')
A('<div class="card"><div class="tags"><span class="t ok">Best in S&amp;P 500</span></div>'
  '<h3>Dell Technologies &mdash; up about 16%</h3>'
  '<p>Quarterly sales <b>+58%</b> and adjusted EPS <b>+203%</b>; AI-optimised server revenue doubled. '
  '<b>$61 billion</b> in AI orders, backlog <b>above $95 billion</b>. Carried from the previous edition and '
  'reconciled there: a close of <b>$492.00, +15.76%</b>, against a prior close read as $425. Reported adjusted '
  'EPS of <b>$7.04 &mdash; earnings before certain costs</b> &mdash; versus a $4.92 estimate, on revenue of '
  '$46.97 billion against $44.92 billion expected.</p></div>')
A('<div class="card"><div class="tags"><span class="t crit">Worst in S&amp;P 500</span></div>'
  '<h3>Palo Alto Networks &mdash; down about 10%</h3>'
  '<p>The index\'s worst performer, <b>down about 10%</b>, <b>despite</b> reporting better-than-expected '
  'quarterly results. TheStreet attributes the selling to slowing growth metrics, margin pressure and elevated '
  'expectations rather than the headline beat. The magnitude is disputed across the day: &minus;10.9%, '
  '&minus;10.82% at $323.08, and &minus;7.8% at 10:36 AM ET &mdash; the only reading carrying a timestamp. '
  'No fiscal-quarter label is asserted here.</p></div>')
A('<div class="card"><div class="tags"><span class="t ok">Best in the Dow</span></div>'
  '<h3>Nvidia &mdash; up more than 3%</h3>'
  '<p>The best-performing Dow component on the session. No closing level or precise percentage was stated in '
  'anything fetched this run beyond "more than 3%", so none is printed.</p></div>')
A('</div>')

# Chart of the day  (BLOCK E)
A('<h2 class="sec">Chart of the Day &mdash; Dell Technologies</h2>')
A('<div class="panel" style="padding:8px">')
A('<script type="application/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"NYSE:DELL","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}</script>')
A('</div>')
A('<p class="note">Dell was the single biggest mover in the S&amp;P 500 this session and the reason the index '
  'closed green.</p>')

# Sector heat (BLOCK D)
A('<h2 class="sec">Sector Heat &mdash; live</h2>')
A('<div class="panel" style="padding:8px">')
A('<script type="application/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}</script>')
A('</div>')
A('<p class="note"><b>Materials led, up 1.6%; real estate lagged, down 0.6%.</b> The breadth count is refused '
  'for a ninth consecutive run because the return contradicts itself: one line says nine of the eleven S&amp;P '
  'sectors finished higher, while a second line in the same return says advances came from virtually every '
  'sector <i>except</i> technology, real estate and utilities &mdash; which would be eight higher, not nine. '
  'Only the leader and laggard are printed. Separately and explicitly as a year-to-date figure, not a daily '
  'one: XLE is <b>+42.32% YTD</b>.</p>')

# Calendar (BLOCK F)
A('<h2 class="sec">The Calendar &mdash; live</h2>')
A('<div class="panel" style="padding:8px">')
A('<script type="application/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en","importanceFilter":"0,1","countryFilter":"us"}</script>')
A('</div>')

# Headlines (BLOCK C)
A('<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2>')
A('<div class="panel" style="padding:8px">')
A('<script type="application/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,"displayMode":"regular","width":"100%","height":420,"locale":"en"}</script>')
A('</div>')

# After hours
A('<h2 class="sec">After-Hours Movers</h2>')
A('<div class="cards">')
A('<div class="card"><div class="tags"><span class="t ok">Up</span></div>'
  '<h3>Snowflake &mdash; +20%</h3>'
  '<p>Second-quarter results topped expectations: adjusted earnings of <b>62 cents per share</b> on revenue of '
  '<b>$1.55 billion</b>, against consensus of 45 cents and $1.48 billion. The size of the move has returned two '
  'ways: +20% this run, and +21% in a reading carrying a timestamp. Both are printed; neither is adopted.'
  '</p></div>')
A('<div class="card"><div class="tags"><span class="t new">New</span><span class="t ok">Up</span></div>'
  '<h3>Netskope &mdash; +13%</h3>'
  '<p>The cybersecurity company popped in extended trading. No earnings figures for Netskope were stated in '
  'anything fetched this run, so none are printed.</p></div>')
A('<div class="card"><div class="tags"><span class="t ok">Up</span></div>'
  '<h3>Petco &mdash; +10%</h3>'
  '<p>Second-quarter adjusted EBITDA margin of <b>8.2%</b> against a StreetAccount consensus of 7.4%; excluding '
  'a tariff benefit the metric was <b>7.7%</b>, which would still beat estimates.</p></div>')
A('<div class="card"><div class="tags"><span class="t ok">Up</span></div>'
  '<h3>Argan &mdash; +8%</h3>'
  '<p>The engineering and construction company posted better-than-expected second-quarter earnings and '
  'revenue.</p></div>')
A('<div class="card"><div class="tags"><span class="t new">New</span><span class="t ok">Beat</span></div>'
  '<h3>Five Below &mdash; earnings beat</h3>'
  '<p><b>$1.68 per share</b> on revenue of <b>$1.26 billion</b>, against consensus of $1.40 and $1.22 billion; '
  'same-store sales also surpassed estimates. <b>No share-price move was stated in anything fetched this run</b>, '
  'so none is printed.</p></div>')
A('<div class="card"><div class="tags"><span class="t crit">Down</span></div>'
  '<h3>Broadcom &mdash; down more than 2%</h3>'
  '<p>Investors reacted badly to the fourth-quarter revenue forecast of <b>$34.8 billion</b> against a '
  '<b>$35.03 billion</b> estimate, with non-GAAP operating margin guided to <b>66%</b> versus a 66.5% estimate. '
  'The magnitude of the after-hours move has now returned five ways across editions &mdash; &minus;3.5% at '
  '4:30 PM ET (the only timed reading), "more than 2%", &minus;5%, "about &minus;6.5%" and &minus;4.14% &mdash; '
  'so only the direction is treated as firm.</p></div>')
A('<div class="card"><div class="tags"><span class="t crit">Down</span></div>'
  '<h3>Hewlett Packard Enterprise &mdash; &minus;1%</h3>'
  '<p>HPE guided to earnings growth of <b>16% to 20%</b> for the fiscal year ending October 2027, against a '
  'FactSet consensus of an <b>18.7%</b> increase.</p></div>')
A('</div>')

# Weekly scorecard
A('<h2 class="sec">Weekly Scorecard &mdash; official closes</h2>')
A('<div class="panel" style="padding:6px 8px"><table>')
A('<tr><th>Index</th><th>Close</th><th>Change</th><th>Session</th></tr>')
for n, c, ch, cls, s in [
    ("S&amp;P 500", "7,666.60", "+0.46%", "up", "Wed, Sep 2 &mdash; snapped a three-day losing streak"),
    ("Nasdaq Composite", "26,217.83", "+0.45%", "up", "Wed, Sep 2 &mdash; snapped a three-day losing streak"),
    ("Dow Jones Industrial Average", "53,061.95", "+295.07 (+0.56%)", "up", "Wed, Sep 2 &mdash; snapped a three-day losing streak"),
]:
    A(f'<tr><td><b>{n}</b></td><td class="mono">{c}</td><td class="mono {cls}">{ch}</td><td>{s}</td></tr>')
A('</table></div>')
A('<p class="note">Levels are published only where the percentage change, the points change and the level are '
  'mutually consistent and corroborated. These three have now returned identically on four separate fetches.</p>')

# Rates
A('<h2 class="sec">Rates, Bonds &amp; Commodities</h2>')
A('<div class="panel" style="padding:6px 8px"><table>')
A('<tr><th>Instrument</th><th>Level</th><th>Move</th><th>Note</th></tr>')
A('<tr><td><b>US 10-year Treasury</b></td><td class="mono">4.79%</td><td class="mono down">&minus;0.01 pp</td>'
  '<td>Eased from the previous session. Intraday high <b>4.814%</b>. The prior edition sourced a close of '
  '4.799% and a session range of 4.765%&ndash;4.820%.</td></tr>')
A('<tr><td><b>Crude oil</b></td><td class="mono">~$95</td><td class="mono">&mdash;</td>'
  '<td>Oil jumped close to $95 a barrel, pushing long-dated yields higher worldwide on inflation concerns. No '
  'settlement price or percentage move was stated this run, so none is printed.</td></tr>')
A('</table></div>')
A('<p class="note">The "highest since" descriptor for the 10-year now disagrees three ways across editions: '
  '<b>November 2023</b> (this run and CNBC/TheStreet), <b>October 2023</b> (Trading Economics) and '
  '<b>January 2025</b> (Yahoo/WSJ). None appears in a table cell above; the level and the intraday high do, '
  'because both are stated figures.</p>')

# On the radar
A('<h2 class="sec">On the Radar</h2>')
A('<div class="panel"><ul class="bul">')
A('<li><b>Friday, September 4 &mdash; August non-farm payrolls.</b> The consensus is genuinely disputed: this '
  'desk has sourced <b>58,000</b>, <b>55,000</b> and <b>45,000</b> across editions, with one bank at '
  '<b>&minus;25,000</b>. Unemployment is expected at <b>4.1%</b>; July printed <b>&minus;23,000</b>.</li>')
A('<li><b>ADP set a soft tone.</b> Private payrolls rose <b>38,000</b> against a 47,000 estimate &mdash; the '
  'slowest since January &mdash; with July revised up to +46,000. Education and health added 45,000 and leisure '
  '16,000, while manufacturing shed 17,000 and professional/business services 16,000. Sourced in the previous '
  'edition, carried here.</li>')
A('<li><b>Oil is the macro variable to watch.</b> With crude near $95, the move in long-dated yields worldwide '
  'is being read as an inflation signal rather than a growth one &mdash; which is why a 0.46% equity gain '
  'arrived alongside a 10-year sitting near its highest level in nearly three years.</li>')
A('<li><b>Carried, not re-sourced this run:</b> the FOMC meeting on September 15&ndash;16, and calendar items '
  'previously logged for September 3 and September 7.</li>')
A('</ul></div>')

A(shared.sources([
 ("CNBC &mdash; Stock market news for Sept. 2, 2026",
  "https://www.cnbc.com/2026/09/01/stock-market-today-live-updates.html"),
 ("TheStreet &mdash; Stock Market Today (Sept. 2, 2026)",
  "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-02-2026"),
 ("The Motley Fool &mdash; Stock Market Today, Sept. 2: Dell Surges 16% on Soaring AI Backlog",
  "https://www.fool.com/coverage/stock-market-today/2026/09/02/stock-market-today-sept-2-dell-surges-16-on-soaring-ai-backlog/"),
 ("CNBC &mdash; Stocks making the biggest moves after hours: Snowflake, Broadcom, Netskope, Five Below",
  "https://www.cnbc.com/2026/09/02/stocks-making-the-biggest-moves-after-hours-snow-avgo-ntsk-five.html"),
 ("CNBC &mdash; Stocks making the biggest moves midday: PG&amp;E, Dell, GitLab, Credo",
  "https://www.cnbc.com/2026/09/02/stocks-making-the-biggest-moves-midday-pcg-dell-gtlb-crdo-bfb.html"),
 ("Investing.com &mdash; Palo Alto Networks, Dell among market cap stock movers on Wednesday",
  "https://www.investing.com/news/stock-market-news/palo-alto-networks-dell-among-market-cap-stock-movers-on-wednesday-93CH-4782176"),
 ("Yahoo Finance &mdash; 10-year Treasury touches highest level since 2023 as oil prices stay elevated",
  "https://finance.yahoo.com/markets/article/10-year-treasury-touches-highest-level-since-2023-as-oil-prices-stay-elevated-134238599.html"),
 ("Trading Economics &mdash; US 10 Year Treasury Note Yield",
  "https://tradingeconomics.com/united-states/government-bond-yield"),
 ("Yahoo Finance &mdash; Stock market today: Wednesday, September 2",
  "https://finance.yahoo.com/markets/live/stock-market-today-wednesday-september-2-dow-sp-500-nasdaq-082624175.html"),
]))
A('<p class="disc">Nothing here is investment advice. This briefing is compiled from public reporting for '
  'information only; figures move and reporting is revised. Verify prices and levels with a live quote before '
  'making any decision.</p>')
A('</footer>')

html = shared.page("The Closing Bell &mdash; Daily Briefings", ACCENT, ACCENT2,
                   "#100e0a", "#191610", "#2c2619", "\n".join(body), EXTRA)
io.open("wallstreet-briefing.html", "w", encoding="utf-8").write(html)
print("ws ok", len(html))
