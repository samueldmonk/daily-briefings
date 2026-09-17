# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))

EXTRA = """
.livebar{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 8px 4px;margin-bottom:18px}
.livebar-label{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--up);display:flex;align-items:center;gap:8px;padding:4px 8px 8px}
.livebar-label .dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--up)}
.tickers{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px}
.ticker{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 10px}
h2.sec,.card h3,.masthead h1,.panel h3{font-family:Georgia,'Times New Roman',serif}
h2.sec{font-family:var(--mono)}
"""
CSS = css("#caa64a", "#e8c766", "#0c0b09", "#17150f", "#2b2720", EXTRA)

TLDR = ("Stocks are rebounding the day after the Fed's first rate hike in three years, with the "
        "S&amp;P 500 up 1.04% and the Nasdaq Composite up 1.45% as of noon ET on falling oil and easing "
        "yields, while Generac soars on an Amazon data-centre supply deal.")

TAPE_A = """<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NYSE:GNRC","title":"Generac"},{"proName":"NASDAQ:FLNC","title":"Fluence"},{"proName":"NASDAQ:NBIS","title":"Nebius"},{"proName":"NYSE:LEN","title":"Lennar"},{"proName":"NASDAQ:NVDA","title":"NVIDIA"},{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script>"""

def quote(sym):
    return ('<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>'
            '{"symbol":"%s","width":"100%%","colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>' % sym)

BODY = """@@MAST@@
<div class="tldr"><b>The Tape</b> <span>@@TLDR@@</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
@@NAV@@

<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>@@TAPE@@</div>

<h2 class="sec">Live Index Quotes &mdash; updates in real time</h2>
<div class="tickers">@@Q1@@@@Q2@@@@Q3@@</div>
<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the latest edition; official closes are in the Weekly Scorecard.</div>

<h2 class="sec">The Lead</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 9px;font-size:21px">The tape turns back up: S&amp;P 500 +1.04% as of 12:00 p.m. ET, with the Nasdaq doing most of the lifting</h3>
<p style="margin:0 0 10px">A day after the Federal Reserve raised rates for the first time in three years, the selling has reversed. At the bell the S&amp;P 500 was <strong>+0.94%</strong> &mdash; a 71-point gain that put it back above 7,600 &mdash; and by <strong>12:00 p.m. ET</strong> it stood at <strong>+1.04%</strong>, with the index at <strong>7,631</strong>. The <strong>Nasdaq Composite was +1.45%</strong>, more than three times the <strong>Dow's +0.42%</strong>: technology and growth are carrying this leg while value-heavy and industrial names lag. A closely watched gauge of chipmakers climbed <strong>3%</strong>.</p>
<p style="margin:0 0 10px">The two things doing the work are <strong>falling oil</strong> and <strong>easing bond-market pressure</strong>. The 10-year Treasury yield, which had climbed back to 5% on the decision itself, was <strong>more than six basis points lower at 4.943%</strong>, and the 2-year slipped more than five basis points to <strong>4.675%</strong>. Brent fell to <strong>$103.61</strong>, down 2.10%.</p>
<p style="margin:0 0 10px">Wednesday's decision was unanimous: all twelve FOMC members approved a <strong>25 basis point</strong> increase to a target range of <strong>3.75%&ndash;4.00%</strong>, the first rise since July 2023, with officials forecasting one further hike in 2026 before holding through 2027. It was that decision together with Chair Kevin Warsh's talk of persistent inflation that unnerved investors and sent equities down on the day.</p>
<p style="margin:0 0 10px">The morning's data helped rather than hurt. Initial jobless claims for the week ending 12 September fell <strong>10,000 to 196,000</strong>, roughly 11,000 below a consensus near 207,000. Housing was the offsetting note: <strong>August housing starts fell 2.6%</strong> to a seasonally adjusted annual rate of 1.275 million. Europe closed green across the board &mdash; the FTSE 100 finished <strong>+0.93% at 14,433</strong>, the DAX <strong>+1.06%</strong> and the CAC 40 <strong>+0.69%</strong>.</p>
<p style="margin:0" class="note">A later read of the same publisher's quote strip, taken around 1:35 p.m. ET, showed the S&amp;P 500 at 7,636.90 &ldquo;+0.94%&rdquo; and the Dow at 51,847.40 &ldquo;+0.59%&rdquo; under an <em>At close</em> label while the session was still open. Neither pair reconciles against Wednesday's settled closes &mdash; those levels imply +1.13% and +0.75% &mdash; so they are not published here as current. The 12:00 p.m. ET figures above do reconcile: 7,551.81 &times; 1.0104 = 7,630.4.</p>
</div>

<h2 class="sec">Movers &amp; Drivers</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t gold">Power &amp; AI</span><span class="t">NYSE:GNRC</span></div>
<h3>Generac and the $8 billion generator order</h3>
<p>Generac and <strong>Amazon</strong> have signed a long-term supply agreement for up to <strong>$8 billion</strong> of backup power generators for Amazon data centres, with <strong>initial deliveries of $2.4 billion across 2027 and 2028</strong>. Generac also issued Amazon a <strong>warrant for up to roughly 1.69 million shares</strong> at an exercise price of about <strong>$200.93</strong>. The moves quoted for it differ by session and are not averaged here: shares jumped <strong>as much as 45% in after-market trading</strong> on Wednesday's announcement, one Thursday read has the stock <strong>+34%</strong>, and another Thursday read headlines <strong>+16%</strong>. Citi's Vikram Bagri called the deal &ldquo;substantially larger than expected&rdquo; while arguing the price-to-revenue multiple had run too far.</p>
</div>
<div class="card">
<div class="tags"><span class="t hot">Guidance cut</span><span class="t">NASDAQ:FLNC</span></div>
<h3>Fluence Energy slashes the year</h3>
<p>Fluence cut FY2026 revenue guidance to about <strong>$2.4 billion</strong> from roughly <strong>$3.0 billion</strong>, and widened the projected adjusted EBITDA loss to about <strong>$200 million</strong> from around <strong>$10 million</strong>. One read put the stock <strong>down 16%</strong>; a mid-morning read on Thursday had it <strong>down 22.1%</strong>. Analysts turned bearish alongside the guidance.</p>
</div>
<div class="card">
<div class="tags"><span class="t pro">Pricing power</span><span class="t">Neocloud</span></div>
<h3>Nebius raises prices, and the stock likes it</h3>
<p>Nebius Group advanced <strong>8% in premarket trading</strong> after the neocloud provider announced price increases &mdash; a straightforward read-through on how tight AI compute capacity currently is.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Housing</span><span class="t">NYSE:LEN</span></div>
<h3>Lennar misses, and the miss is wide</h3>
<p>The homebuilder reported third-quarter earnings of <strong>$1.19 per share</strong> against the <strong>$1.28</strong> expected by analysts polled by FactSet &mdash; and nearly half what it earned in the same quarter last year. Shares were <strong>1.2% lower</strong>. It lands the same morning as a 2.6% drop in August housing starts.</p>
</div>
</div>

<h2 class="sec">Chart of the Day &mdash; Generac (GNRC)</h2>
<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"NYSE:GNRC","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}</script></div>
<p class="note">The session's marquee single-name move. The chart is live; the percentages in the card above are the ones sources actually stated, each with its own clock.</p>

<h2 class="sec">Sector Heat &mdash; live</h2>
<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}</script></div>
<p class="note">One sourced line on breadth: a closely watched gauge of chipmakers climbed <strong>3%</strong>, and at midday the Nasdaq Composite's 1.45% gain was more than triple the Dow's &mdash; growth leading, old-economy blue chips lagging. Sector-level percentages circulating today came without a stated measurement window, so none is printed.</p>

<h2 class="sec">The Calendar &mdash; live</h2>
<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en","importanceFilter":"0,1","countryFilter":"us"}</script></div>

<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2>
<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,"displayMode":"regular","width":"100%","height":420,"locale":"en"}</script></div>

<h2 class="sec">Weekly Scorecard</h2>
<div class="panel" style="padding:4px 0">
<table>
<tr><th>Session</th><th>S&amp;P 500</th><th>Nasdaq Composite</th><th>Dow Jones Industrial Average</th></tr>
<tr><td>Wed 16 Sep &mdash; close</td><td class="down">7,551.81 &nbsp;&minus;0.45%</td><td class="down">25,978.42 &nbsp;&minus;0.01%</td><td class="down">51,461.90 &nbsp;&minus;631.21 (&minus;1.21%)</td></tr>
<tr><td>Thu 17 Sep</td><td class="mut" colspan="3">Session in progress &mdash; no close to publish. Latest verified intraday read: 12:00 p.m. ET, S&amp;P 500 +1.04% (7,631), Nasdaq Composite +1.45%, Dow +0.42%.</td></tr>
</table>
</div>
<p class="note">Only settled closes appear as levels. Wednesday's Dow reconciles exactly: 52,093.11 &minus; 631.21 = 51,461.90. One publisher's closing card described the Dow's loss as &ldquo;622 points, a 1.2% drop&rdquo;; the 631.21 figure is the one consistent with the level, so that is the one carried here, with the disagreement noted rather than split.</p>

<h2 class="sec">Rates, Bonds &amp; Commodities</h2>
<div class="panel" style="padding:4px 0">
<table>
<tr><th>Instrument</th><th>Level</th><th>Move</th><th>As of / source</th></tr>
<tr><td>US 10-year Treasury yield</td><td>4.943%</td><td class="up">&minus;6 bp or more</td><td>17 Sep, CNBC</td></tr>
<tr><td>US 2-year Treasury yield</td><td>4.675%</td><td class="up">&minus;5 bp or more</td><td>17 Sep, CNBC</td></tr>
<tr><td>Fed funds target range</td><td>3.75%&ndash;4.00%</td><td class="down">+25 bp, 12&ndash;0</td><td>16 Sep FOMC decision</td></tr>
<tr><td>Brent crude</td><td>$103.61</td><td class="up">&minus;2.10%</td><td>17 Sep, Trading Economics</td></tr>
<tr><td>WTI crude</td><td>$102.13</td><td class="up">&minus;0.29%</td><td>17 Sep, Trading Economics</td></tr>
</table>
</div>
<p class="note">Falls in yields and oil are shown in green because that is the direction helping equities today, not because lower is inherently better. The 30-year yield, gold, silver and bitcoin are omitted: no source fetched this run gave a current level for them. One-month rolling correlation between front-month WTI and the 10-year yield has reached <strong>0.96</strong>, per BMO Capital Markets &mdash; which is why the oil tape is being read as a rates tape.</p>

<h2 class="sec">On the Radar</h2>
<div class="panel">
<ul class="bul">
<li><strong>Still to come today:</strong> the Philadelphia Fed Manufacturing Index and pending home sales, alongside the building-permits detail that accompanies the housing-starts release.</li>
<li><strong>One more in 2026.</strong> The Fed's own forecast points to a further hike this year before a hold through 2027 &mdash; so every inflation print between now and December is a policy print.</li>
<li><strong>Central banks abroad.</strong> The Bank of England is expected to hold at 3.75%; the Bank of Japan is expected to lift its policy rate to a three-decade high.</li>
<li><strong>Oil is the swing factor.</strong> With crude and the 10-year moving together at a 0.96 correlation, an energy headline is now a bond headline and therefore an equity headline.</li>
</ul>
</div>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
<a href="https://247wallst.com/cards/tech-is-doing-the-heavy-lifting-at-midday-the-nasdaq-s-1-45-gspc-market-bell-01m2r1pgh0014krfmnx2pd7d96">24/7 Wall St. midday card, 12:00pm ET</a> &middot;
<a href="https://247wallst.com/cards/">24/7 Wall St. market updates feed</a> &middot;
<a href="https://finance.yahoo.com/markets/live/stock-market-today-thursday-september-17-dow-sp-500-nasdaq-081248626.html">Yahoo Finance live blog, 17 Sep</a> &middot;
<a href="https://finance.yahoo.com/markets/stocks/articles/stock-market-today-sept-16-133949098.html">Yahoo Finance, 16 Sep close</a> &middot;
<a href="https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-16-2026">TheStreet, 16 Sep</a> &middot;
<a href="https://www.cnbc.com/2026/09/17/treasury-yields-move-lower-after-fed-kicks-off-hiking-cycle.html">CNBC on Treasury yields, 17 Sep</a> &middot;
<a href="https://www.cnbc.com/2026/09/16/treasury-yield-bond-market-fed-decision.html">CNBC on the Fed decision</a> &middot;
<a href="https://www.cnbc.com/2026/09/17/generac-shares-surge-on-amazon-deal-wall-street-thinks-it-has-more-to-go-.html">CNBC on Generac</a> &middot;
<a href="https://www.cnbc.com/2026/09/16/amazon-obtains-right-to-buy-up-to-340m-of-generac-boosting-stock-.html">CNBC on the Amazon warrant</a> &middot;
<a href="https://seekingalpha.com/news/4643652-generac-soars-as-analysts-see-earnings-upside-from-amazon-deal">Seeking Alpha</a> &middot;
<a href="https://247wallst.com/investing/2026/09/17/generac-holdings-surges-16-on-2-4b-amazon-data-center-generator-deal-caterpillar-ticks-up-cummins-sits-out-the-rally/">24/7 Wall St. on Generac</a> &middot;
<a href="https://stockstotrade.com/news/fluence-energy-inc-flnc-news-2026_09_17/">StocksToTrade on Fluence</a> &middot;
<a href="https://www.cnbc.com/2026/09/17/stocks-making-the-biggest-moves-premarket-gnrc-len-nke.html">CNBC premarket movers</a> &middot;
<a href="https://www.bloomberg.com/news/articles/2026-09-17/us-jobless-claims-fall-to-196-000-continuing-applications-drop">Bloomberg on jobless claims</a> &middot;
<a href="https://tradingeconomics.com/commodity/brent-crude-oil">Trading Economics, Brent</a> &middot;
<a href="https://tradingeconomics.com/commodity/crude-oil">Trading Economics, WTI</a> &middot;
<a href="https://www.cnbc.com/2026/09/15/oil-us-treasurys-stocks-pressure.html">CNBC on the oil&ndash;yield correlation</a> &middot;
<a href="https://ng.investing.com/news/stock-market-news/building-permits-jobless-claims-and-pending-home-sales-due-thursday-93CH-2698711">Investing.com on today's calendar</a>
</div>

<div class="disc">Information only. Nothing on this page is investment advice, a recommendation, or an offer to buy or sell any security. Intraday figures carry the time at which the source stated them and are not aged forward; where two sources disagreed, both reads are shown rather than averaged, and figures no source stated are left out rather than estimated. Live widgets are supplied by TradingView and may lag.</div>
"""

BODY = (BODY.replace("@@MAST@@", masthead("The Closing Bell", "Your daily markets briefing &mdash; the tape, the movers and what moves it"))
            .replace("@@NAV@@", nav("ws"))
            .replace("@@TLDR@@", TLDR)
            .replace("@@TAPE@@", TAPE_A)
            .replace("@@Q1@@", quote("FOREXCOM:SPXUSD"))
            .replace("@@Q2@@", quote("FOREXCOM:NSXUSD"))
            .replace("@@Q3@@", quote("FOREXCOM:DJI")))

html = page("The Closing Bell &mdash; Daily Markets Briefing", CSS, BODY)
io.open(os.path.join(OUT, "wallstreet-briefing.html"), "w", encoding="utf-8").write(html)
print("ws ok", len(html))
