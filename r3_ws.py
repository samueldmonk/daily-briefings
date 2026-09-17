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
 ("Yahoo Finance - Stock market today: Dow, S&P 500, Nasdaq rise as Fed rate hike pacifies markets' inflation worries (Thursday, September 17)", "https://finance.yahoo.com/markets/live/stock-market-today-thursday-september-17-dow-sp-500-nasdaq-081248626.html"),
 ("Yahoo Finance - US stocks rise after oil prices fall and pressure from the bond market eases", "https://ca.finance.yahoo.com/news/asian-stocks-mixed-wall-street-074043165.html"),
 ("TheStreet - Stock Market Today (Sept. 17, 2026): Nasdaq climbs after Fed rate hike decision", "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-17-2026"),
 ("TheStreet - Stock Market Today (Sept. 16, 2026): Dow, S&P 500 plummet after Fed hikes, forecasts further hikes ahead", "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-16-2026"),
 ("CNBC - Fed rate decision September 2026: Rates rise to 3.75%-4%", "https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html"),
 ("CNBC - 10-year Treasury yield falls as traders bet Fed rate increase can tamp down inflation", "https://www.cnbc.com/2026/09/16/treasury-yield-bond-market-fed-decision.html"),
 ("Bloomberg - Fed Raises Rates, Treasuries Hold Gains as More Hikes Forecast", "https://www.bloomberg.com/news/articles/2026-09-16/treasuries-hold-gains-as-fed-hikes-rates-signaling-more-ahead"),
 ("Bloomberg - Stock Market Today: Dow, S&P Live Updates for September 17", "https://www.bloomberg.com/news/articles/2026-09-16/stock-market-today-dow-s-p-live-updates"),
 ("Trading Economics - United States Stock Market Index (US500)", "https://tradingeconomics.com/united-states/stock-market"),
 ("Seeking Alpha - Biggest stock movers Thursday: GNRC, FLNC, and more", "https://seekingalpha.com/news/4643656-biggest-stock-movers-thursday-gnrc-flnc-and-more"),
 ("MarketScreener - Generac Up on Amazon Agreement; CoreWeave Kicks Off Fundraising", "https://www.marketscreener.com/news/generac-up-on-amazon-agreement-coreweave-kicks-off-fundraising-stock-movers-ce785bd3dc8ef126"),
 ("TradingKey - US Pre-Market: US Stock Futures Rise as Fed Delivers Rate Hike; Generac Surges 33%", "https://www.tradingkey.com/analysis/stocks/us-stocks/262173053-us-pre-market-tradingkey"),
 ("StockMarketWatch - Tech and Small-Caps Lead Market Surge Following Federal Reserve Decision", "https://stockmarketwatch.com/live/stock-market-today"),
 ("Yahoo Finance - Semiconductors Stock Performance", "https://finance.yahoo.com/sectors/technology/semiconductors/"),
 ("Kiplinger - What to Look Out for in Economic Data This Week", "https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar"),
 ("Trading Economics - United States Economic Calendar", "https://tradingeconomics.com/united-states/calendar"),
 ("Trading Economics - US 10 Year Treasury Note Yield", "https://tradingeconomics.com/united-states/government-bond-yield"),
]

def srcblock():
    return "".join('<div style="margin-bottom:7px">%s &mdash; <a href="%s">%s</a></div>' % (t, u, u) for t, u in SRC)

TLDR = ("Wall Street is rebounding from the Fed&#39;s first rate hike since 2023, with the S&amp;P 500 up "
        "around 0.9% near 11 a.m. ET on falling oil and steadier bond yields, and Generac surging on an "
        "Amazon backup-power agreement worth up to $8 billion.")

TICKER = """<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>
<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NYSE:GNRC","title":"Generac"},{"proName":"NASDAQ:FLNC","title":"Fluence Energy"},{"proName":"NASDAQ:NVDA","title":"NVIDIA"},{"proName":"NASDAQ:MU","title":"Micron"},{"proName":"AMEX:SLV","title":"Silver Trust"},{"proName":"TVC:UKOIL","title":"Brent Crude"},{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script>
</div>"""

def quote(sym):
    return ('<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>'
            '{"symbol":"' + sym + '","width":"100%","colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>')

QUOTES = '<div class="tickers">' + quote("FOREXCOM:SPXUSD") + quote("FOREXCOM:NSXUSD") + quote("FOREXCOM:DJI") + '</div>'

BODY = """@@MAST@@
<div class="tldr"><b>The Tape</b> <span>@@TLDR@@</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
@@NAV@@

@@TICKER@@

<h2 class="sec">Live Index Quotes &mdash; updates in real time</h2>
@@QUOTES@@
<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the latest edition; official closes are in the Weekly Scorecard.</div>

<h2 class="sec">The Lead</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 9px;font-size:20px">Stocks rebound from the hike &mdash; the S&amp;P 500 up about 0.9% as of ~11 a.m. ET</h3>
<p style="margin:0 0 10px">Wall Street is reversing much of Wednesday&#39;s slide. In a read timed to <b>around 11 a.m. Eastern</b>, the S&amp;P 500 was <b>up 0.9%</b> and on track for <b>just its second rise in the last nine days</b>. The two drivers named are <b>falling oil prices</b> and <b>easing pressure from the bond market</b>.</p>
<p style="margin:0 0 10px">Trading Economics gives a different snapshot from a different moment, stating the S&amp;P 500 &ldquo;rose to <b>7,596</b> points on September 17, 2026, gaining <b>0.59%</b>.&rdquo; Both are intraday reads, both are printed, and neither is a close &mdash; the Thursday row of the Weekly Scorecard reads <i>session in progress</i>. Another read of the session has the <b>Dow at 51,783.71 (+321.81, +0.63%)</b> and the <b>Nasdaq Composite at 26,400.63 (+422.20, +1.63%)</b>; the Dow figures reconcile exactly against Wednesday&#39;s 51,461.90 close.</p>
<p style="margin:0">Behind it is Wednesday&#39;s decision. The FOMC voted <b>12&ndash;0</b> to raise its key rate by <b>25 basis points</b> to a <b>3.75%&ndash;4.00%</b> range &mdash; the first increase in more than three years &mdash; and signalled that the tightening cycle is not finished, with another increase possible later this year. Chair <b>Kevin Warsh</b>&#39;s stated resolve on inflation is credited with reassuring markets rather than alarming them.</p>
</div>

<h2 class="sec">Movers &amp; Drivers</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t gold">Up</span><span class="t">Industrials</span></div>
<h3>Generac &mdash; and five different percentages</h3>
<p><b>Generac (GNRC)</b> is the session&#39;s story, on a long-term agreement to supply <b>Amazon</b> with backup generators for AWS data centres. Reads fetched this run put it <b>+33%</b> and <b>+30%</b>; earlier reads logged today ran from <b>+21.35%</b> (10:25 a.m. session) to <b>+27.3% at $223.23</b> (session) to <b>45%</b> (Wednesday after-hours). They are different clocks, not a contradiction, and none is averaged here. The deal carries potential payments of <b>up to $8 billion</b>, with <b>$2.4 billion of initial deliveries slated for 2027 and 2028</b>. The $8 billion is a purchasing ceiling tied to vesting, <b>not</b> booked revenue or an unconditional order.</p>
</div>
<div class="card">
<div class="tags"><span class="t hot">Down</span><span class="t">Guidance cut</span></div>
<h3>Fluence Energy cuts its full-year guidance to $2.4 billion</h3>
<p><b>Fluence Energy (FLNC)</b> fell &mdash; <b>18%</b> in one read fetched this run, <b>16%</b> in another &mdash; after cutting full-year fiscal 2026 revenue guidance to <b>$2.4 billion</b> from a prior <b>$2.9&ndash;3.1 billion</b> range, blaming supply-chain bottlenecks in US battery production.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Semis</span></div>
<h3>Chips carry the tape</h3>
<p>Early in the session the <b>VanEck Semiconductor ETF (SMH)</b> was <b>+2.65%</b>, with <b>Nvidia +2.1%</b> on heavy volume, <b>Micron +3.0%</b> and <b>SanDisk +3.0%</b>. <b>QQQ +1.45%</b> and <b>IWM +0.95%</b> point to a rally broadening past the mega-caps. These are morning figures and are not presented as current.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Metals</span><span class="t">Energy</span></div>
<h3>Silver rips; energy and financials lag</h3>
<p>In the same early-session read, the <b>iShares Silver Trust (SLV)</b> was <b>+4.49%</b> and the <b>SPDR Gold Trust (GLD) +2.35%</b>. On the other side, <b>XLE &minus;0.35%</b> with <b>USO &minus;1.42%</b>, and <b>XLF &minus;0.55%</b> as the curve adjusts to the Fed. These are ETF percentages and are deliberately not converted into metal prices no source stated.</p>
</div>
</div>

<h2 class="sec">Chart of the Day &mdash; Generac (NYSE:GNRC)</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"NYSE:GNRC","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}</script>
</div>

<h2 class="sec">Sector Heat &mdash; live</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}</script>
</div>
<p class="note">One sourced editorial line: on a longer horizon, <b>energy leads all sectors year to date at +46.11%</b> and was also the strongest performer over the past month at <b>+6.14%</b> &mdash; while in this morning&#39;s read the energy ETF XLE was slightly lower. No single-day sector percentage is printed; one that circulated today did not cohere with the day&#39;s oil move and was dropped.</p>

<h2 class="sec">The Calendar &mdash; live</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en","importanceFilter":"0,1","countryFilter":"us"}</script>
</div>

<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,"displayMode":"regular","width":"100%","height":420,"locale":"en"}</script>
</div>

<h2 class="sec">Weekly Scorecard</h2>
<div class="panel" style="padding:6px 10px">
<table>
<tr><th>Session</th><th>Index</th><th>Close</th><th>Move</th></tr>
<tr><td>Thursday 17 Sep</td><td>S&amp;P 500 / Dow / Nasdaq</td><td class="mut">session in progress</td><td class="mut">no close yet &mdash; intraday reads are in The Lead above</td></tr>
<tr><td>Wednesday 16 Sep</td><td>Dow Jones Industrial Average</td><td>51,461.90</td><td class="down">&minus;631.21</td></tr>
<tr><td>Wednesday 16 Sep</td><td>S&amp;P 500</td><td class="mut">level not published</td><td class="down">&minus;0.45%</td></tr>
</table>
</div>
<p class="note">Wednesday&#39;s Dow close is the figure the Thursday intraday read reconciles against: <b>51,783.71 &minus; 321.81 = 51,461.90</b>. No S&amp;P 500 level is printed for Wednesday because no points-change, percent-change and level triple fetched this run is mutually consistent; the percentage alone is given. A parenthetical &ldquo;+0.93%&rdquo; attached to Wednesday&#39;s S&amp;P by one outlet contradicts its own down-session reporting and is refused.</p>

<h2 class="sec">Rates, Bonds &amp; Commodities</h2>
<div class="panel" style="padding:6px 10px">
<table>
<tr><th>Instrument</th><th>Level</th><th>Move / note</th></tr>
<tr><td>Fed funds target range</td><td>3.75% &ndash; 4.00%</td><td>Raised 25 bp on 16 September by a 12&ndash;0 vote; first increase in more than three years, with more signalled</td></tr>
<tr><td>US 2-year Treasury</td><td>4.72%</td><td class="down">&minus;1 bp on 17 September, after touching its highest since 2024 in the prior session</td></tr>
<tr><td>US 10-year Treasury</td><td>4.943%</td><td class="mut">This morning&#39;s read; easing back off the 5% mark it crossed after the decision</td></tr>
<tr><td>Brent crude</td><td>$103.38</td><td class="down">&minus;2.3% on 17 September &mdash; the fall that is doing most of the work in today&#39;s rebound</td></tr>
<tr><td>WTI crude</td><td>$100.70</td><td class="mut">Morning read, &minus;1.70%; not re-sourced later in this run and not aged forward as current</td></tr>
</table>
</div>
<p class="note">The 30-year Treasury, gold and silver spot prices, and Bitcoin are omitted: nothing fetched this run states a current level for any of them, and a stale level is worse than a blank. Silver and gold appear above only as the ETF percentages their source actually gave.</p>

<h2 class="sec">On the Radar</h2>
<div class="panel">
<ul class="bul">
<li><b>Whether the Fed is done.</b> The committee signalled another increase may come later this year, so every inflation print between now and the next meeting carries more weight than usual.</li>
<li><b>Oil as the swing factor.</b> The hike was framed as a response to inflation driven by spiralling oil prices; Brent falling 2.3% today is the reason equities could rally through a hawkish message. If crude turns back up, the same logic reverses.</li>
<li><b>Jobless claims stayed low.</b> Initial claims <b>fell 10,000 to 196,000</b> in the week ended 12 September, the lowest since mid-July &mdash; published with the caveat that the period included Labor Day and that the series fluctuates around holidays.</li>
<li><b>FOMC minutes and Fed speakers ahead.</b> The minutes from this meeting, plus a full slate of Fed member speeches, are the next read on how firm the &ldquo;more to come&rdquo; signal really is.</li>
</ul>
</div>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
@@SRCS@@
</div>
<p class="disc">Compiled automatically from public reporting gathered during this run; nothing was fetched first-hand. Live widgets on this page stream from TradingView and are independent of the editorial text, which is stamped with its own as-of time. Every figure above traces to a source listed here or to a standing sourced correction, and where two sources disagreed, both reads are shown rather than averaged. This is information only. It is not investment advice, no security is recommended here, and quotes on this page may be delayed.</p>
"""

BODY = (BODY.replace("@@MAST@@", masthead("The Closing Bell", "Wall Street, rates and commodities &mdash; refreshed every 30 minutes, 8 AM&ndash;6 PM ET"))
            .replace("@@NAV@@", nav("ws"))
            .replace("@@TLDR@@", TLDR)
            .replace("@@TICKER@@", TICKER)
            .replace("@@QUOTES@@", QUOTES)
            .replace("@@SRCS@@", srcblock()))

html = page("The Closing Bell &mdash; Daily Briefing", CSS, BODY)
io.open(os.path.join(OUT, "wallstreet-briefing.html"), "w", encoding="utf-8").write(html)
print("ws ok", len(html))
print("TLDR::" + TLDR)
