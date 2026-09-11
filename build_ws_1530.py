# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page
from build_1530 import S_WS, tldr, FRESH, srcblock

OUT = os.path.dirname(os.path.abspath(__file__))
ACC, ACC2 = "#caa64a", "#e8c766"
EXTRA = """
.masthead h1{font-family:Georgia,'Times New Roman',serif;font-weight:700}
.card h3,.card h4,.panel h3{font-family:Georgia,'Times New Roman',serif}
.livebar{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 8px 4px;margin-bottom:18px}
.livebar-label{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--up);display:flex;align-items:center;gap:8px;padding:4px 8px 8px}
.livebar-label .dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--up)}
.tickers{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-bottom:6px}
.ticker{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 10px}
"""
CSS = css(ACC, ACC2, "#0d0c09", "#171510", "#2b2618", EXTRA)

SRC = [
 ("TheStreet - Stock Market Today (Sept. 11, 2026): S&P 500, Dow recover as CPI report arrives in-line; oil falls",
  "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-11-2026"),
 ("The Motley Fool - Stock Market Midday, Sept. 11: Stocks Rise as Falling Oil Prices Outweigh Sticky Inflation",
  "https://www.fool.com/coverage/stock-market-today/2026/09/11/stock-market-midday-sept-11-stocks-rise-as-falling-oil-prices-outweigh-sticky-inflation/"),
 ("CNBC - Stock market today: live updates",
  "https://www.cnbc.com/2026/09/10/stock-market-today-live-updates.html"),
 ("Yahoo Finance - Stock market today: Dow, S&P 500, Nasdaq rise as CPI fuels Fed rate-hike bets, oil prices fall",
  "https://ca.finance.yahoo.com/news/stock-market-today-friday-september-11-dow-sp-500-nasdaq-cpi-inflation-082201751.html"),
 ("TheStreet - Stock Market Today (Sept. 10, 2026): Stocks fall for fourth straight day as Brent oil hits $105/bbl",
  "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-10-2026"),
 ("CME Group - FedWatch Tool",
  "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html"),
 ("CNBC - US 1-Year Treasury quote (curve reference)", "https://www.cnbc.com/quotes/US1y"),
 ("CNBC - Bessent says 'a large bank' to be sanctioned",
  "https://www.cnbc.com/2026/09/11/bessent-large-bank-sanctioned.html"),
 ("MarketWatch - SpaceX is inching closer to this lofty $100 billion milestone",
  "https://www.marketwatch.com/story/spacex-is-inching-closer-to-this-lofty-100-billion-milestone-11536cfc"),
 ("The Independent - Iran war live: Trump says he has 'no regrets'",
  "https://www.independent.co.uk/news/world/middle-east/iran-us-war-live-trump-houthis-red-sea-yemen-oil-b3048368.html"),
 ("CNBC - Trump brushes off AI extinction risks",
  "https://www.cnbc.com/2026/09/11/trump-ai-extinction-risks.html"),
]

TICKER = """<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>
<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NYSE:HPE","title":"HPE"},{"proName":"NYSE:DELL","title":"Dell"},{"proName":"NYSE:HPQ","title":"HP Inc."},{"proName":"NYSE:ANET","title":"Arista"},{"proName":"NYSE:ORCL","title":"Oracle"},{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script>
</div>"""

def quote(sym):
    return ('<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>'
            '{"symbol":"' + sym + '","width":"100%","colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>')

QUOTES = '<div class="tickers">' + quote("FOREXCOM:SPXUSD") + quote("FOREXCOM:NSXUSD") + quote("FOREXCOM:DJI") + '</div>'

BODY = """@@MAST@@
@@TLDR@@
@@FRESH@@
@@NAV@@

@@TICKER@@

<h2 class="sec">Live Index Quotes &mdash; updates in real time</h2>
@@QUOTES@@
<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the latest edition; official closes are in the Weekly Scorecard.</div>

<h2 class="sec">The Lead</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 9px;font-size:20px">Oil retreats, August CPI lands in line, and the four-day slide ends &mdash; on reads through ~2:18 PM ET, with the whole Treasury curve at fresh 52-week highs</h3>
<p>Friday&rsquo;s session reversed the week. Stocks <b>finished lower for four consecutive days</b> into Thursday, pressured by rising oil and rising yields; on Friday all three major indexes are <b>on track to snap those streaks</b>, and for the Dow it would end its <b>longest daily losing streak since late April</b>. Two things did the work: <b>crude gave back some of the week&rsquo;s sharp gains</b>, and the <b>August CPI arrived in line</b>, removing the tail risk of an upside inflation shock even as it confirmed the Fed&rsquo;s direction.</p>
<p>The index reads available at the time of this edition are printed with their own timestamps rather than blended:</p>
<ul class="bul">
<li><b>Opening bell, 9:34 AM ET (TheStreet):</b> S&amp;P 500 <b class="up">+0.96%</b>, Dow <b class="up">+1.15%</b>, Nasdaq <b class="up">+0.88%</b>, Russell 2000 <b class="up">+1.04%</b>.</li>
<li><b>12:04 PM ET (TheStreet):</b> S&amp;P 500 <b class="up">+1.06%</b>, &ldquo;back in the green today after four days of consecutive declines&rdquo;, with Alphabet <b class="up">+2.66%</b> and Apple <b class="up">+2.23%</b> standing out.</li>
<li><b>1:49 PM ET (TheStreet):</b> S&amp;P 500 <b class="up">+1.07%</b>; the <b>Russell 2000 at <span class="up">+0.63%</span> is the weakest major index</b> of the day despite a better session than the rest of its week.</li>
<li><b>Motley Fool quote modules:</b> S&amp;P 500 <b class="up">+1.06% (+80.64)</b>, Nasdaq Composite <b class="up">+1.19% (+309.43)</b>, Dow <b class="up">+1.11% (+579.62)</b>. <span class="mut">Fetched again this run, these modules returned byte-identical values to the previous edition&rsquo;s 2:38 PM read on a page marked <code>max-age=300</code> &mdash; almost certainly a CDN cache hit, so they are treated as a ~2:38 PM read rather than a 3 PM one. All three reconcile to the cent against Thursday&rsquo;s verified closes and the derived percentages match.</span></li>
<li><b>A separate CNBC-sourced read</b> has the <b>Dow up 527 points, nearly 1.2%</b>, the S&amp;P 500 up almost 1% and the Nasdaq up 1.1%. <span class="mut">That is a different moment in the session from the Fool modules and the point figures differ; both are printed and neither is picked.</span></li>
</ul>
<p style="margin:10px 0 0">The bond market did not join the relief. TheStreet&rsquo;s <b>2:18 PM ET</b> Treasury check, citing CNBC quotes, records <b>fresh 52-week highs across the curve</b> &mdash; the 2-, 3-, 5-, 7-, 10-, 20- and 30-year all set new highs on the same afternoon that equities rallied. That is the tension in this session: equity buyers stepped in on an in-line inflation print while the rates market moved further toward pricing a hike, and <b>money markets now treat a September increase as close to settled</b>.</p>
</div>

<h2 class="sec">Movers &amp; Drivers</h2>
<div class="cards">

<div class="card">
<div class="tags"><span class="t new">New</span><span class="t gold">Rates</span></div>
<h4>Fresh 52-week highs the length of the curve</h4>
<p>TheStreet&rsquo;s <b>2:18 PM ET</b> Treasury check, sourced to CNBC quotes, has new 52-week highs at every tenor from two years out: <b>2Y 4.63% (+8 bps)</b>, <b>3Y 4.712% (+6.5)</b>, <b>5Y 4.775% (+4.2)</b>, <b>7Y 4.859% (+2.7)</b>, <b>10Y 4.959% (+1.5)</b>, <b>20Y 5.377% (&minus;0.3)</b> and <b>30Y 5.346% (&minus;1.5)</b>, with the <b>1Y at 4.341% (+7.7)</b>. Note the shape: the front end is doing the moving while the long end is slightly lower on the day &mdash; a hike being priced, not an inflation scare being extended.</p>
<p style="margin:9px 0 0"><span class="mut">This read conflicts with the Motley Fool&rsquo;s 11:31 AM line that the 10-year &ldquo;slipped to 4.94%&rdquo;. Both are printed with their timestamps; the 2:18 PM figure is the later of the two.</span></p>
</div>

<div class="card">
<div class="tags"><span class="t new">New</span><span class="t">Breadth</span></div>
<h4>Ten of eleven sectors higher, and small caps lag</h4>
<p><b>Ten of the 11 S&amp;P 500 sectors are higher</b>, led by <b>communication services at +1.9%</b>. TheStreet describes the Russell 2000&rsquo;s internals as &ldquo;sort of a spitting image&rdquo; of the S&amp;P 500&rsquo;s, with <b>tech, cyclicals and industrials</b> the strongest areas in both. The Motley Fool&rsquo;s 11:31 AM read agrees on the shape: <b>apart from healthcare, almost every sector gained</b>, with technology and communication outperforming. But the rally is not evenly shared &mdash; the <b>Russell 2000&rsquo;s +0.63%</b> is roughly half the large-cap move.</p>
</div>

<div class="card">
<div class="tags"><span class="t new">New</span><span class="t">Leaderboard</span></div>
<h4>The midday leaderboards, both ends</h4>
<p>TheStreet&rsquo;s <b>1:04 PM</b> screen of the day&rsquo;s biggest winners among stocks above a <b>$2 billion market capitalisation</b> is led by <b>$VICR</b>, <b>$DELL</b>, <b>$HPE</b>, <b>$MRNA</b> and <b>$SANM</b>. Its <b>12:32 PM</b> screen of the bottom 20 on the same market-cap filter is led by <b>$SMR</b>, <b>$OKLO</b>, <b>$SLS</b>, <b>$STX</b> and <b>$CHWY</b> &mdash; two small modular-reactor names at the head of the decliners on a day the broad tape is up more than a percent. <span class="mut">Those two screens are published as ordered lists of tickers; the underlying percentages were carried in images rather than text, so no figure is attached to the names that do not appear elsewhere on this page.</span></p>
</div>

<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t gold">+11.6%</span></div>
<h4>Hewlett Packard Enterprise &mdash; the session&rsquo;s biggest gainer</h4>
<p><b>HPE surged 11.6%</b> at TheStreet&rsquo;s 10:38 AM mover check, &ldquo;as the tech company extended a post-earnings re-rating driven by accelerating demand for AI servers, networking and storage infrastructure.&rdquo; The Motley Fool&rsquo;s module later reads <b>+9.91%</b>, and a CNBC-sourced read has it <b>leading the S&amp;P 500, up nearly 11%</b>. All three agree it is the standout; the level has drifted through the day, so all three are printed. HPE is this edition&rsquo;s Chart of the Day.</p>
</div>

<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t gold">+10%</span></div>
<h4>Dell jumps on an RBC initiation, and joins the S&amp;P 100</h4>
<p><b>Dell (DELL) rose 10%</b> after <b>RBC initiated coverage with an Outperform rating</b>, citing robust free cash flow and what it called a massive competitive edge in AI infrastructure deployment. Dell <b>joins the S&amp;P 100 index on 21 September</b>. Alongside it, <b>HP Inc. (HPQ) rose 8%</b> after RBC initiated the PC maker &mdash; which split from HPE in 2015 &mdash; at <b>Sector Perform with a $33 price target</b>.</p>
</div>

<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t hot">Reversal</span></div>
<h4>Oracle opened sharply higher, then gave it back</h4>
<p><b>Oracle (ORCL) jumped in early trading</b> after reporting a fiscal first-quarter beat and hiking profit guidance &mdash; but the Motley Fool notes it <b>&ldquo;pared gains as the morning wore on&rdquo;</b>, and its quote module reads <b class="down">&minus;0.32%</b>. A premarket read of roughly <b>+7%</b> was circulating this morning; a premarket percentage is not a session result, and this page prints the reversal rather than the pop. <b>Arista Networks (ANET) is up 4.97%</b> after management stressed demand strength at the <b>Citi Global TMT Conference</b>.</p>
</div>

<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t">Mega caps</span></div>
<h4>Alphabet and Apple lead the index higher</h4>
<p>From the Motley Fool&rsquo;s quote rail: <b>GOOG $337.50 (+2.2%)</b>, <b>AAPL $333.26 (+2.0%)</b>, <b>AMZN $256.64 (+1.9%)</b>, <b>META $649.21 (+0.8%)</b>, <b>MSFT $494.70 (+0.5%)</b>, <b>NVDA $219.34 (+0.5%)</b> and <b>TSLA $365.62 (+0.6%)</b>. <b>Bitcoin</b> is at <b>$77,582 (+0.3%)</b>. TheStreet&rsquo;s 12:04 PM look inside the index has <b>Alphabet +2.66%</b> and <b>Apple +2.23%</b> &mdash; the same two names, at a slightly earlier moment and slightly higher.</p>
</div>

<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t hot">Decliners</span></div>
<h4>Clorox, Seagate and Albemarle on the wrong side</h4>
<p><b>Clorox (CLX) slipped 3.1%</b> after <b>Barclays lowered its price target to $84 from $86</b>. <b>Seagate (STX) lost 3.1%</b> on profit-taking after a sharp year-long run left the stock on a relatively high earnings multiple. <b>Albemarle (ALB) fell 2.5%</b> on its ex-dividend date for a <b>41-cents-per-share</b> payout, alongside continued caution in the global lithium market.</p>
</div>

<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t">Private markets</span></div>
<h4>SpaceX adds about $13B of annualized revenue</h4>
<p><b>SpaceX (SPCX) rose 1.25% to $150.03</b> ahead of the bell after reportedly signing a computing deal worth <b>$1.1 billion per month</b> with an undisclosed counterparty &mdash; roughly <b>$13 billion annualized</b>, as it works toward a <b>$100 billion annualized revenue run rate by the end of 2026</b>, per MarketWatch. CFO <b>Bret Johnsen</b> disclosed the deal Thursday at a Goldman Sachs conference; it was signed earlier this month with <b>payments beginning in December</b>. The shares debuted at <b>$135 on 12 June</b> and hit a record <b>$225.64 on 16 June</b>. The Fool&rsquo;s rail later has SPCX at <b>$149.88 (+1.1%)</b>.</p>
</div>

</div>

<h2 class="sec">Chart of the Day</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"NYSE:HPE","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}</script>
</div>
<p class="note">Hewlett Packard Enterprise is the largest single-name move verified in this run&rsquo;s reads &mdash; up 11.6% at TheStreet&rsquo;s 10:38 AM check, 9.91% on the Motley Fool&rsquo;s module, and named by a CNBC-sourced read as the S&amp;P 500&rsquo;s leader at nearly 11%.</p>

<h2 class="sec">Sector Heat &mdash; live</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}</script>
</div>
<p class="note">Ten of the 11 S&amp;P 500 sectors are higher, led by communication services at +1.9%; the Motley Fool&rsquo;s 11:31 AM read names healthcare as the lone sector not participating, with technology and communication outperforming.</p>

<h2 class="sec">The Calendar &mdash; live</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en","importanceFilter":"0,1","countryFilter":"us"}</script>
</div>

<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,"displayMode":"regular","width":"100%","height":420,"locale":"en"}</script>
</div>

<h2 class="sec">Weekly Scorecard</h2>
<div class="panel">
<table>
<tr><th>Index</th><th>Last official close (Thu 10 Sep)</th><th>Change</th></tr>
<tr><td>S&amp;P 500</td><td>7,591.70</td><td class="down">&minus;44.66 (&minus;0.58%)</td></tr>
<tr><td>Nasdaq Composite</td><td>26,081.72</td><td class="down">&minus;0.65%</td></tr>
<tr><td>Dow Jones Industrial Average</td><td>52,064.10</td><td class="down">&minus;316.56 (&minus;0.60%)</td></tr>
</table>
<p class="note">These are the most recent <b>official closes</b> &mdash; Thursday&rsquo;s, the fourth of the four consecutive down days. Friday&rsquo;s session was still open when this edition was built, so no 11 September close is published. Precise index levels appear only in this table; the editorial above uses percentage moves and attributed figures. No mover carries a &ldquo;New&rdquo; tag purely for reappearing &mdash; the three New tags in this edition mark material that was absent from the 2:42 PM snapshot.</p>
</div>

<h2 class="sec">Rates, Bonds &amp; Commodities</h2>
<div class="panel">
<table>
<tr><th>Instrument</th><th>Level</th><th>Note</th></tr>
<tr><td>Fed funds target range</td><td>3.50&ndash;3.75%</td><td>Unchanged since December 2025. The next decision is <b>Wednesday 16 September</b>. CME FedWatch put the probability of a hike at <b>85.6% as of 10:03 AM ET</b> (TheStreet) and <b>86%, up from 60% a week ago</b> (Motley Fool); TheStreet Pro&rsquo;s commentary headline reads <b>90%</b>. Regan Capital&rsquo;s Skyler Weinand: &ldquo;A rate hike next week is all but assured.&rdquo;</td></tr>
<tr><td>2-year Treasury</td><td>4.63% (+8 bps)</td><td rowspan="3">All figures from TheStreet&rsquo;s <b>2:18 PM ET</b> Treasury check citing CNBC quotes. <b>Fresh 52-week highs across the curve</b>: 1Y 4.341% (+7.7 bps), 3Y 4.712% (+6.5), 5Y 4.775% (+4.2), 7Y 4.859% (+2.7), 20Y 5.377% (&minus;0.3). The front end led; the 20- and 30-year were marginally lower on the day.</td></tr>
<tr><td>10-year Treasury</td><td>4.959% (+1.5 bps)</td></tr>
<tr><td>30-year Treasury</td><td>5.346% (&minus;1.5 bps)</td></tr>
<tr><td>10-year Treasury (earlier read)</td><td>4.94%</td><td class="mut">The Motley Fool&rsquo;s 11:31 AM read has the 10-year &ldquo;slipped to 4.94%&rdquo;. Kept with its timestamp; the 2:18 PM figure above supersedes it as the later read.</td></tr>
<tr><td>WTI crude</td><td>$99.05 (&minus;3.35%) &nbsp;<span class="mut">/</span>&nbsp; $99.44 (&minus;3%)</td><td>First figure TheStreet, 6:44 AM ET; second from a CNBC-sourced read later in the session. Both have WTI down about 3%; neither is picked.</td></tr>
<tr><td>Brent crude</td><td>$103.70 (&minus;3.61%)</td><td>TheStreet, 6:44 AM ET. Brent hit <b>$105/bbl</b> on Thursday, the highest since July, before Friday&rsquo;s retreat.</td></tr>
<tr><td>Gold futures</td><td>$4,409.40 (+0.05%) &nbsp;<span class="mut">/</span>&nbsp; $4,404.40 (&minus;0.66%)</td><td>First figure the Motley Fool at 11:31 AM; second TheStreet&rsquo;s 8:59 AM early-futures read. Both printed.</td></tr>
<tr><td>Silver futures</td><td>$65.17 (+0.37%)</td><td>TheStreet, early trading.</td></tr>
<tr><td>August CPI</td><td>+0.4% m/m, +3.4% y/y</td><td>Both in line with the Dow Jones consensus (BLS via TheStreet). <b>Core +0.3% m/m &mdash; a tenth above forecast</b> &mdash; and <b>core +2.4% y/y</b>, in line. August <b>PPI</b> was <b>+0.4% m/m, +5.4% y/y</b>.</td></tr>
</table>
<p class="note">Where two reads of the same instrument disagreed on level while agreeing on direction, both are shown with their timestamps rather than one being chosen. Anyone who needs a single current number should take it from the live ticker above, not from this table.</p>
</div>

<h2 class="sec">On the Radar</h2>
<div class="panel">
<ul class="bul">
<li><b>The FOMC decides Wednesday 16 September.</b> The target range has been <b>3.50&ndash;3.75%</b> since December 2025, and this meeting carries a Summary of Economic Projections and dot plot. LPL&rsquo;s <b>Jeffrey Roach</b> expects a 25 basis point hike but argues the impact may be muted: &ldquo;A growing share of economic activity is less interest-rate sensitive... nominal economic growth will remain above 6% over the next few quarters.&rdquo; Weinand at Regan Capital goes further, warning of &ldquo;several rate hikes over the coming months.&rdquo;</li>
<li><b>Treasury Secretary Scott Bessent says the U.S. will sanction &ldquo;a large bank&rdquo; on Monday</b>, declining to name the institution or its country: &ldquo;We&rsquo;re going to do it on Monday because we want to honor the memory of our fallen citizens on 9/11.&rdquo; He added that a Turkish bank that &ldquo;had been giving to the Iranians&rdquo; will be closed. Treasury sanctioned Turkey-based <b>Golden Global Yatirim Bankasi Anonim Sirketi</b> and its subsidiaries on <b>4 September</b>, and previously hit the Dubai branches of Egypt&rsquo;s second-largest bank over an alleged <b>$1.8 billion</b> in funds to Iran. Last month&rsquo;s escalation, which Bessent calls <b>&ldquo;Operation Economic Outcast&rdquo;</b>, covered nearly <b>60</b> entities, vessels and individuals.</li>
<li><b>The oil risk premium has not gone away.</b> President Trump told Fox News he has <b>&ldquo;no regrets&rdquo;</b> about the war with Iran and sees it ending after the November midterms &mdash; comments Capital.com&rsquo;s <b>Kyle Rodda</b> says &ldquo;sparked concerns that the US is preparing for a war that will carry on in its current form at least until the end of the year.&rdquo; Iran-aligned <b>Houthi forces seized Yemen&rsquo;s port city of Mocha</b>, raising fears over the <b>Bab el-Mandeb</b> strait, and Reuters-verified satellite imagery showed smoke near Saudi Arabia&rsquo;s <b>East-West oil pipeline</b>.</li>
<li><b>Thursday set the backdrop for Friday&rsquo;s bond move.</b> Rodda notes the <b>2-year yield jumped around 15 basis points to a more-than-two-year high</b> on Thursday, with rates markets then pricing a hike at about <b>70%</b> &mdash; well below where Friday&rsquo;s CPI left them.</li>
<li><b>Wall Street marked the 25th anniversary of 9/11.</b> The Ground Zero ceremony added an extra moment of silence for those later stricken with 9/11-related illnesses; all living former presidents attended in Manhattan alongside Vice President JD Vance and Mayor Zohran Mamdani, while President Trump spoke at the Pentagon.</li>
</ul>
</div>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
@@SRCS@@
</div>
<p class="disc">Compiled automatically from public reporting gathered during this run; nothing was fetched first-hand from an exchange. Live widgets on this page stream from TradingView and are independent of the editorial text, which carries its own as-of times. Every figure above traces to a source listed here or to a standing sourced correction, and where two sources disagreed both reads are shown. This is information, not investment advice; markets move, and quotes on this page may be delayed.</p>
"""

BODY = (BODY.replace("@@MAST@@", masthead("The Closing Bell", "Your daily markets briefing &mdash; indices, movers, rates &amp; the calendar"))
            .replace("@@TLDR@@", tldr("The Tape", S_WS))
            .replace("@@FRESH@@", FRESH)
            .replace("@@NAV@@", nav("ws"))
            .replace("@@TICKER@@", TICKER)
            .replace("@@QUOTES@@", QUOTES)
            .replace("@@SRCS@@", srcblock(SRC)))

io.open(os.path.join(OUT, "wallstreet-briefing.html"), "w", encoding="utf-8").write(
    page("The Closing Bell &mdash; Daily Briefings", CSS, BODY))
print("ws ok")
