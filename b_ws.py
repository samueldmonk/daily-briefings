# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))
ACC, ACC2 = "#caa64a", "#e8c766"
EXTRA = """
.masthead h1{font-family:Georgia,'Times New Roman',serif;font-weight:700}
h2.sec{font-family:var(--mono)}
.card h3,.panel h3{font-family:Georgia,'Times New Roman',serif}
.livebar{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 8px 4px;margin-bottom:18px}
.livebar-label{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--up);display:flex;align-items:center;gap:8px;padding:4px 8px 8px}
.livebar-label .dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--up)}
.tickers{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-bottom:6px}
.ticker{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 10px}
"""
CSS = css(ACC, ACC2, "#0d0c09", "#171510", "#2b2618", EXTRA)

SRC = [
 ("Yahoo Finance — Stock Market Today (Sept. 8, 2026): S&P 500 edges lower as oil prices climb, Mideast tensions rise", "https://finance.yahoo.com/markets/stocks/articles/stock-market-today-sept-8-133744027.html"),
 ("Yahoo Finance — Live: Dow, S&P 500 slip as oil prices rise, US-Canada trade war escalates (Tuesday, September 8)", "https://finance.yahoo.com/markets/live/stock-market-today-tuesday-september-8-dow-sp-500-nasdaq-080440338.html"),
 ("TheStreet — Stock Market Today (Sept. 8, 2026)", "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-08-2026"),
 ("Bloomberg — Stock Market Today: Dow, S&P Live Updates for September 8", "https://www.bloomberg.com/news/articles/2026-09-07/stock-market-today-dow-s-p-live-updates"),
 ("CNBC — Stock market Tuesday: live updates", "https://www.cnbc.com/2026/09/07/stock-market-tuesday-live-updates.html"),
 ("Trading Economics — United States Stock Market Index (US500)", "https://tradingeconomics.com/united-states/stock-market"),
 ("StockMarketWatch — Energy and commodities surge as Dow slumps", "https://stockmarketwatch.com/live/stock-market-today"),
 ("Traders Agency — Stock Market Today: Energy leads while S&P 500 slips", "https://tradersagency.com/blog/stock-market-today-energy-leads-while-sandp-500-slips"),
 ("TipRanks — Stock Market News Today, 9/8/2026", "https://www.tipranks.com/news/stock-market-news-today-9-8-2026-futures-fall-on-rising-geopolitical-worries-oil-prices-climb"),
 ("Investrade — Morning Preview: September 08, 2026", "https://investrade.com/morning-preview-september-08-2026/"),
 ("Trading Economics — US 10 Year Treasury Note Yield", "https://tradingeconomics.com/united-states/government-bond-yield"),
 ("StreetStats — U.S. Treasury yield curve", "https://streetstats.finance/rates/treasuries"),
 ("Federal Reserve — H.15 Selected Interest Rates (Daily), September 04, 2026", "https://www.federalreserve.gov/releases/h15/"),
 ("Trading Economics — Treasury yields continue to advance", "https://tradingeconomics.com/united-states/government-bond-yield/news/532986"),
]

def srcblock():
    return "".join('<div style="margin-bottom:7px">%s &mdash; <a href="%s">%s</a></div>' % (t, u, u) for t, u in SRC)

TICKER = """<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>
<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NASDAQ:INTC","title":"Intel"},{"proName":"NASDAQ:MU","title":"Micron"},{"proName":"NASDAQ:NVDA","title":"NVIDIA"},{"proName":"NYSE:ORCL","title":"Oracle"},{"proName":"AMEX:XLE","title":"Energy Sector"},{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script>
</div>"""

def quote(sym):
    return ('<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>'
            '{"symbol":"%s","width":"100%%","colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>' % sym)

QUOTES = '<div class="tickers">%s%s%s</div>' % (quote("FOREXCOM:SPXUSD"), quote("FOREXCOM:NSXUSD"), quote("FOREXCOM:DJI"))

BODY = """
%s
<div class="tldr"><b>The Tape</b> <span>Stocks are lower across the board in Tuesday morning trade with the Dow much the weakest of the three, as a renewed crude rally lifts energy to the top of the board and Canada&#39;s retaliatory tariffs on about $20 billion of U.S. goods take effect.</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
%s

%s

<h2 class="sec">Live Index Quotes &mdash; updates in real time</h2>
%s
<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the latest edition; official closes are in the Weekly Scorecard.</div>

<h2 class="sec">The Lead</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 8px;font-size:20px">As of ~10:35 AM ET: stocks slip on all three indices, the Dow much the hardest hit, as oil climbs and the Canada tariffs bite</h3>
<p style="margin:0 0 10px">The first regular session after the Labor Day long weekend opened with a cautious, mixed tone, with investors balancing a resurgence in the energy sector against broader weakness in blue-chip industrials and financials. Three separate reads of the morning were available at the time of this edition and they are printed here rather than smoothed into one:</p>
<ul class="bul">
<li>A Tuesday session summary has the <b>Dow down 0.8%%</b>, the <b>S&amp;P 500 down 0.2%%</b> and the <b>Nasdaq Composite down 0.1%%</b>.</li>
<li>A separate point read, from a different moment in the same session, gives the <b>Dow at 52,800.65, down 613.60 points or 1.15%%</b>, and the <b>Nasdaq Composite at 26,379.01, down 127.98 points or 0.48%%</b>. Both are arithmetically consistent with Friday&#39;s closes, so the level, the point change and the percentage agree in each case.</li>
<li>Early-trading ETF proxies put the <b>Dow (DIA) at &minus;1.09%%</b>, the <b>S&amp;P 500 (SPY) at &minus;0.45%%</b>, the <b>Nasdaq 100 (QQQ) at &minus;0.31%%</b> and small caps (<b>IWM</b>) at <b>&minus;0.47%%</b>.</li>
</ul>
<p style="margin:10px 0 0">What every read agrees on: all three major indices are lower, and the Dow is decisively the weakest of the three. What they do not agree on is magnitude, which is what you would expect from snapshots taken minutes apart in a session moving on an oil headline. A separate index tracker has the <b>S&amp;P 500 at 7,707, down 0.15%%</b> from the previous session &mdash; also consistent with Friday&#39;s close.</p>
</div>

<h2 class="sec">Movers &amp; Drivers</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t pro">+5.2%%</span></div>
<h3>Intel leads the tape on heavy volume</h3>
<p><b>Intel (INTC) has jumped 5.2%%</b> on high volume &mdash; the largest single-name move named in any return read this run. Semiconductors more broadly are providing the cushion under the Nasdaq: the <b>VanEck Semiconductor ETF (SMH) is trading 1%% higher</b>, with <b>Micron (MU) up 2.0%%</b> and <b>Nvidia (NVDA) up 1.2%%</b>.</p>
</div>
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t gold">Energy</span></div>
<h3>Crude rally puts energy at the top of the board</h3>
<p>The energy sector is the clear standout performer. The <b>Energy Select Sector SPDR (XLE) is up 1.7%%</b>, the <b>United States Oil Fund (USO) up 2.1%%</b>, the <b>Oil &amp; Gas Exploration &amp; Production ETF (XOP) up 2.41%%</b>, and the <b>Global X Uranium ETF (URA) has surged 4.3%%</b>. Military activity is described as maintaining a significant risk premium in energy markets on the possibility of deeper and more protracted disruptions to global supply.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Expanded</span><span class="t hot">Trade</span></div>
<h3>Canada&#39;s retaliatory tariffs take effect today</h3>
<p>Canada&#39;s retaliatory tariffs kicked in Tuesday, covering about <b>$20 billion in U.S. imports</b> at duties of up to <b>50%%</b>, after trade talks collapsed. New detail this run: the affected goods include <b>cheese and other dairy products, wood products, toilet paper and metal items</b>. The escalating trade war is named alongside oil as a driver of the mixed open.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t">Blue chips</span></div>
<h3>The drag is in industrials and financials</h3>
<p>The weakness is concentrated in blue-chip industrials and financial stocks, which is the mechanical reason a price-weighted Dow is falling roughly twice as fast as the S&amp;P 500, or worse, in every read above. <span class="mut">Named single-name decliners were available only from a tracker that does not identify which session its component moves belong to, so none are printed here.</span></p>
</div>
</div>

<h2 class="sec">Chart of the Day</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"NASDAQ:INTC","width":"100%%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}</script>
</div>
<p class="note">Intel, up 5.2%% on high volume, is the session&#39;s single biggest named mover in returns read this run.</p>

<h2 class="sec">Sector Heat &mdash; live</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%%","height":420}</script>
</div>
<p class="note">Leading: energy, on the crude rally, with semiconductors cushioning the Nasdaq. Lagging: blue-chip industrials and financials. Longer view: eight of the eleven S&amp;P sectors are higher year to date, energy leading at about +43%%.</p>

<h2 class="sec">The Calendar &mdash; live</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{"colorTheme":"dark","isTransparent":true,"width":"100%%","height":420,"locale":"en","importanceFilter":"0,1","countryFilter":"us"}</script>
</div>

<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,"displayMode":"regular","width":"100%%","height":420,"locale":"en"}</script>
</div>

<h2 class="sec">Weekly Scorecard</h2>
<div class="panel">
<table>
<tr><th>Index</th><th>Last official close (Fri 4 Sep)</th><th>Change</th></tr>
<tr><td>S&amp;P 500</td><td>7,718.60</td><td class="down">&minus;0.38%%</td></tr>
<tr><td>Nasdaq Composite</td><td>26,506.99</td><td class="down">&minus;0.29%%</td></tr>
<tr><td>Dow Jones Industrial Average</td><td>53,414.25</td><td class="down">&minus;271.86 (&minus;0.51%%)</td></tr>
</table>
<p class="note">These are the most recent official closes: Monday 7 September was Labor Day and U.S. stock and bond markets were shut all day. Today&#39;s session is still open, so no close is published for 8 September. Precise levels appear only in this table; the editorial above uses percentage moves and attributed figures.</p>
</div>

<h2 class="sec">Rates, Bonds &amp; Commodities</h2>
<div class="panel">
<table>
<tr><th>Instrument</th><th>Level</th><th>Note</th></tr>
<tr><td>Fed funds target range</td><td>3.50&ndash;3.75%%</td><td>Markets price a roughly <b>52%%</b> chance of a <b>25 basis point increase</b> this month; readings across sources this week span <b>50&ndash;63%%</b>, so the range is printed rather than averaged.</td></tr>
<tr><td>1-year Treasury</td><td>4.12%%</td><td rowspan="5" class="mut">Full curve as of Friday 4 September. The 10-year rose nearly 3 basis points to 4.79%% on Friday following a stronger-than-expected jobs report. The bond market was closed Monday for Labor Day; no 8 September curve was published in returns read this run.</td></tr>
<tr><td>2-year Treasury</td><td>4.37%%</td></tr>
<tr><td>5-year Treasury</td><td>4.55%%</td></tr>
<tr><td>10-year Treasury</td><td>4.79%%</td></tr>
<tr><td>30-year Treasury</td><td>5.25%%</td></tr>
<tr><td>Brent crude</td><td>$99.73 (+1.45%%) &nbsp;<span class="mut">/</span>&nbsp; near $98.50 (about +2.3%%)</td><td>Two reads from different moments this morning. Both have Brent up on the day; they do not agree on the level.</td></tr>
<tr><td>WTI crude</td><td>$94.28 (+1.50%%) &nbsp;<span class="mut">/</span>&nbsp; about $94.00 (+2.7%%)</td><td>Same two reads. Crude is at a six-week high as investors assess the impact of the U.S.&ndash;Iran conflict on global supply.</td></tr>
<tr><td>U.S. retail diesel</td><td>$5.85 / gal</td><td>A record set on Friday 4 September, past the $5.816 June 2022 peak.</td></tr>
</table>
<p class="note">The two crude reads moved in opposite directions against each other on the level while agreeing on direction, so both are shown with their percentages rather than one being picked. Anyone using a single number should take it from the live ticker above, not from this table.</p>
</div>

<h2 class="sec">On the Radar</h2>
<div class="panel">
<ul class="bul">
<li><b>Oracle&#39;s fiscal Q1 2027 report lands 10 September</b>, with an estimated EPS of <b>$1.67</b>. <span class="mut">This corrects an earlier edition of this briefing, which said the report was due after today&#39;s close.</span></li>
<li><b>August CPI, Friday 11 September.</b> The inflation print that will do most to settle the hike-versus-hold argument now running at 50&ndash;63%% odds.</li>
<li><b>The August payrolls consensus still has three numbers attached to it.</b> The actual print was <b>162,000</b> jobs, with unemployment at <b>4.1%%</b> and average hourly earnings up <b>3.1%%</b> year over year. The forecast this desk has verified repeatedly is <b>53,000</b>; a return this run gives <b>56,000</b>, and <b>55,000</b> is separately the June-plus-July revision total. All three are printed with what each is, because a fresh number that contradicts a verified one is often a different statistic rather than a correction.</li>
<li><b>Middle East risk stays in the oil price.</b> Iran has issued a fresh threat to the U.S. over its newly upgraded ballistic missile, with officials warning the country will act against any threat &ldquo;even before it is carried out&rdquo;.</li>
</ul>
</div>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
%s
</div>
<p class="disc">Compiled automatically from public reporting gathered during this run; nothing was fetched first-hand. Live widgets on this page stream from TradingView and are independent of the editorial text, which is stamped with its own as-of time. Every figure above traces to a source listed here or to a standing sourced correction. Where two sources disagreed, both reads are shown. This is information, not investment advice, and nothing here is investment advice; markets move, and quotes on this page may be delayed.</p>
""" % (masthead("The Closing Bell", "Your daily markets briefing &mdash; indices, movers, rates &amp; the calendar"), nav("ws"), TICKER, QUOTES, srcblock())

html = page("The Closing Bell &mdash; Daily Briefings", CSS, BODY)
io.open(os.path.join(OUT, "wallstreet-briefing.html"), "w", encoding="utf-8").write(html)
print("ws ok", len(html))
