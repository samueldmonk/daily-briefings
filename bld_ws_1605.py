# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page
from common_1605 import S_WS, tldr, FRESH, srcblock

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
  "https://finance.yahoo.com/markets/live/stock-market-today-friday-september-11-dow-sp-500-nasdaq-cpi-inflation-082201751.html"),
 ("TheStreet - Stock Market Today (Sept. 10, 2026): Stocks fall for fourth straight day as Brent oil hits $105/bbl",
  "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-10-2026"),
 ("CME Group - FedWatch Tool",
  "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html"),
 ("CNBC - US 1-Year Treasury quote (curve reference)", "https://www.cnbc.com/quotes/US1y"),
 ("CNBC - Bessent says 'a large bank' to be sanctioned",
  "https://www.cnbc.com/2026/09/11/bessent-large-bank-sanctioned.html"),
 ("MarketWatch - SpaceX is inching closer to this lofty $100 billion milestone",
  "https://www.marketwatch.com/story/spacex-is-inching-closer-to-this-lofty-100-billion-milestone-11536cfc"),
 ("Yahoo Finance - Oracle posts cloud sales that top estimates on surging AI demand",
  "https://finance.yahoo.com/technology/articles/oracle-posts-cloud-sales-top-201512207.html"),
 ("Yahoo Finance - US average diesel price passes $6 a gallon for the first time, GasBuddy says",
  "https://finance.yahoo.com/energy/articles/us-average-diesel-price-passes-224140256.html"),
 ("The Independent - Iran war live: Trump says he has 'no regrets'",
  "https://www.independent.co.uk/news/world/middle-east/iran-us-war-live-trump-houthis-red-sea-yemen-oil-b3048368.html"),
]

TICKER = """<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>
<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NYSE:HPE","title":"HPE"},{"proName":"NYSE:DELL","title":"Dell"},{"proName":"NYSE:HPQ","title":"HP Inc."},{"proName":"NYSE:ANET","title":"Arista"},{"proName":"NYSE:ORCL","title":"Oracle"},{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script>
</div>"""


def quote(sym):
    return ('<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>'
            '{"symbol":"' + sym + '","width":"100%","colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>')


QUOTES = '<div class="tickers">' + quote("FOREXCOM:SPXUSD") + quote("FOREXCOM:NSXUSD") + quote("FOREXCOM:DJI") + '</div>'

MOVERS = [
 (['<span class="t pro">leader</span>', '<span class="t">AI infrastructure</span>'],
  "Hewlett Packard Enterprise <span class='up'>+11.6%</span>",
  "TheStreet&rsquo;s 10:38 AM read has HPE surging <b>11.6%</b> as the post-earnings re-rating extends on accelerating "
  "demand for AI servers, networking and storage. The Motley Fool&rsquo;s 11:31 AM read had it <b>+9.91%</b>, and by "
  "2:18 PM TheStreet described HPE as leading the S&amp;P 500 at nearly <b>11%</b>."),
 (['<span class="t pro">upgrade</span>', '<span class="t">index add</span>'],
  "Dell <span class='up'>+10%</span>",
  "RBC initiated coverage with an Outperform rating, pointing to robust free cash flow and a competitive edge in AI "
  "infrastructure deployment. Dell joins the <b>S&amp;P 100</b> on <b>21 September</b>."),
 (['<span class="t">initiation</span>', '<span class="t">hardware</span>'],
  "HP Inc. <span class='up'>+8%</span>",
  "RBC also initiated the PC maker &mdash; which split from Hewlett Packard Enterprise in 2015 &mdash; with a Sector "
  "Perform rating and a <b>$33</b> price target."),
 (['<span class="t">networking</span>', '<span class="t">conference</span>'],
  "Arista Networks <span class='up'>+4.97%</span>",
  "Gained after management stressed demand strength at the Citi Global TMT Conference (Motley Fool, 11:31 AM read)."),
 (['<span class="t">megacap</span>'],
  "Alphabet <span class='up'>+2.66%</span>, Apple <span class='up'>+2.23%</span>",
  "TheStreet&rsquo;s 12:04 PM look inside the S&amp;P 500 flagged both as notable advances, with technology, "
  "communication services and industrials leading after a rough patch."),
 (['<span class="t gold">earnings</span>', '<span class="t">reversal</span>'],
  "Oracle &mdash; a beat that faded",
  "Oracle jumped in early trading after a fiscal first-quarter beat and raised profit guidance, with cloud "
  "infrastructure sales up <b>121% to $7.4 billion</b> against roughly $7.19 billion expected, and 850 megawatts of "
  "data-centre capacity added in the quarter. It then <b>pared those gains as the morning wore on</b> (Motley Fool, "
  "11:31 AM read)."),
 (['<span class="t new">New</span>', '<span class="t gold">settlement</span>', '<span class="t">energy</span>'],
  "Crude settles sharply lower &mdash; the reason the tape turned",
  "A CNBC read has West Texas Intermediate futures down <b>2.4%</b> to settle at <b>$100.05</b> a barrel and Brent down "
  "<b>2.8%</b> to <b>$104.61</b>. The pullback still leaves a brutal week behind it: <b>WTI rallied nearly 10%</b> and "
  "<b>Brent 8.6%</b> across the five sessions on Middle East escalation."),
 (['<span class="t down">laggards</span>'],
  "Clorox <span class='down'>&minus;3.1%</span>, Seagate <span class='down'>&minus;3.1%</span>, Albemarle <span class='down'>&minus;2.5%</span>",
  "Clorox slipped after Barclays lowered its target to <b>$84 from $86</b>. Seagate fell on profit-taking after a sharp "
  "year and a relatively high earnings multiple. Albemarle declined on its ex-dividend date for a <b>41-cent</b> cash "
  "payout, alongside persistent caution in the global lithium market."),
 (['<span class="t">pre-bell</span>', '<span class="t">private markets</span>'],
  "SpaceX <span class='up'>+1.25%</span> to $150.03 ahead of the bell",
  "CFO Bret Johnsen disclosed at a Goldman Sachs conference on Thursday that the company signed a computing deal worth "
  "<b>$1.1 billion a month</b> &mdash; roughly <b>$13 billion annualised</b> &mdash; with an undisclosed counterparty, "
  "with payments starting in December. MarketWatch frames it against a <b>$100 billion</b> annualised revenue run-rate "
  "target by the end of 2026."),
]


def movers():
    out = ['<div class="cards">']
    for tags, h, p in MOVERS:
        out.append('<div class="card"><div class="tags">%s</div><h3>%s</h3><p>%s</p></div>' % ("".join(tags), h, p))
    out.append('</div>')
    return "".join(out)


RATES = [
 ("1-year Treasury", "4.341%", "+7.7 bps", ""),
 ("2-year Treasury", "4.63%", "+8 bps", "52-week high"),
 ("3-year Treasury", "4.712%", "+6.5 bps", "52-week high"),
 ("5-year Treasury", "4.775%", "+4.2 bps", "52-week high"),
 ("7-year Treasury", "4.859%", "+2.7 bps", "52-week high"),
 ("10-year Treasury", "4.959%", "+1.5 bps", "52-week high"),
 ("20-year Treasury", "5.377%", "&minus;0.3 bps", "52-week high"),
 ("30-year Treasury", "5.346%", "&minus;1.5 bps", "52-week high"),
 ("WTI crude", "$100.05", "&minus;2.4%", "Friday settlement; up nearly 10% on the week"),
 ("Brent crude", "$104.61", "&minus;2.8%", "Friday settlement; up 8.6% on the week"),
 ("Gold futures", "$4,409.40", "+0.05%", "11:31 AM ET read"),
 ("Silver futures", "$65.17", "+0.37%", "early-trading read"),
]


def raterows():
    out = []
    for name, lvl, chg, note in RATES:
        cls = "down" if chg.startswith("&minus;") else "up"
        out.append('<tr><td><b>%s</b></td><td>%s</td><td class="%s">%s</td><td class="mut">%s</td></tr>'
                   % (name, lvl, cls, chg, note))
    return "".join(out)


BODY = """@@MAST@@
@@TLDR@@
@@FRESH@@
@@NAV@@

@@TICKER@@

<h2 class="sec">Live Index Quotes &mdash; updates in real time</h2>
@@QUOTES@@
<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the latest edition; official closes are in the Weekly Scorecard.</div>

<h2 class="sec">The Lead</h2>
<div class="panel">
<h3 style="margin:0 0 9px;font-size:20px">Stocks snap a four-day skid as crude settles back below $101 &mdash; all three indexes up around 1.1% as of ~2:18 PM ET</h3>
<p style="margin:0 0 11px">The week&rsquo;s losing streak is ending. TheStreet&rsquo;s <b>2:18 PM ET</b> read has the
market higher across the board, having put the <b>S&amp;P 500 at +1.07%</b> at 1:49 PM and <b>+1.06%</b> at 12:04 PM; a
CNBC read has the <b>Dow up 527 points, or nearly 1.2%</b>, the S&amp;P up almost <b>1%</b> and the Nasdaq Composite up
<b>1.1%</b>. The <b>Russell 2000 (+0.63%</b> at 1:49 PM) is the weakest of the major indexes even on a green day, and
the Dow is snapping its <b>longest daily losing streak since late April</b>.</p>
<p style="margin:0 0 11px">The catalyst was crude giving back ground rather than the inflation print. August
<b>CPI rose 0.4%</b> on the month for a <b>3.4%</b> annual rate, both in line with the Dow Jones consensus; core CPI
<b>rose 0.3%</b>, a tenth of a point above forecast, with the core annual rate at <b>2.4%</b>, in line. That combination
left next Wednesday&rsquo;s Federal Reserve decision close to settled: CME FedWatch showed an <b>85.6%</b> probability
of a hike on TheStreet&rsquo;s 10:03 AM read, and the Motley Fool put it at <b>86%, up from 60% a week ago</b>.</p>
<p style="margin:0 0 11px">&ldquo;Friday&rsquo;s CPI print was in-line with expectations, but inflation is still too
hot, and the Federal Reserve&rsquo;s hands are tied,&rdquo; said Skyler Weinand, chief investment officer at Regan
Capital. &ldquo;A rate hike next week is all but assured.&rdquo; Jeffrey Roach, chief economist at LPL Financial, made
the opposite-facing point: &ldquo;Markets expect the Fed to raise rates by 25 basis points next week, but the impact may
be muted&rdquo; &mdash; a growing share of activity, he argues, is less interest-rate sensitive.</p>
<p style="margin:0"><b>Ten of the eleven S&amp;P 500 sectors are higher</b>, with communication services up
<b>1.9%</b>, and the Vanguard S&amp;P 500 ETF rose <b>0.93% to $703.12</b> in late-morning trading.
<span class="mut">No intraday index level is printed anywhere on this page. The only source offering one returned
values byte-identical to two earlier editions on a page marked for five-minute caching &mdash; a cache hit, not a flat
tape &mdash; so the editorial here runs on percentages and point changes only.</span></p>
</div>

<h2 class="sec">Movers &amp; Drivers</h2>
@@MOVERS@@
<p class="note">TheStreet&rsquo;s <b>1:04 PM</b> screen of the day&rsquo;s biggest winners above a $2 billion market
capitalisation is led by <b>$VICR</b>, <b>$DELL</b>, <b>$HPE</b>, <b>$MRNA</b> and <b>$SANM</b>; its <b>12:32 PM</b>
screen of the bottom 20 on the same filter is led by <b>$SMR</b>, <b>$OKLO</b>, <b>$SLS</b>, <b>$STX</b> and
<b>$CHWY</b> &mdash; two small-modular-reactor names heading the decliners on a day the broad tape is up more than a
percent. Those screens are published as ordered ticker lists with the percentages carried in images, so no figure is
attached to names that do not appear elsewhere on this page.</p>

<h2 class="sec">Chart of the Day &mdash; HPE, the session&rsquo;s biggest S&amp;P 500 mover</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"NYSE:HPE","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}</script>
</div>

<h2 class="sec">Sector Heat &mdash; live</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}</script>
</div>
<p class="note">Editorially: ten of eleven S&amp;P 500 sectors were higher on TheStreet&rsquo;s 2:18 PM read, led by
communication services at <b>+1.9%</b>; healthcare was the one sector the Motley Fool flagged as not participating in
the morning advance.</p>

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
<table><thead><tr><th>Index</th><th>Thursday&rsquo;s close</th><th>Change</th><th>Percent</th></tr></thead>
<tbody>
<tr><td><b>S&amp;P 500</b></td><td>7,591.70</td><td class="down">&minus;44.66</td><td class="down">&minus;0.58%</td></tr>
<tr><td><b>Nasdaq Composite</b></td><td>26,081.72</td><td class="mut">&mdash;</td><td class="down">&minus;0.65%</td></tr>
<tr><td><b>Dow Jones Industrial Average</b></td><td>52,064.10</td><td class="down">&minus;316.56</td><td class="down">&minus;0.60%</td></tr>
</tbody></table>
</div>
<p class="note">These are Thursday&rsquo;s verified official closes &mdash; the fourth straight down session &mdash; and
the only index levels printed on this page. Friday&rsquo;s closing levels will appear here once they are confirmed
after the bell.</p>

<h2 class="sec">Rates, Bonds &amp; Commodities</h2>
<div class="panel" style="padding:6px 10px">
<table><thead><tr><th>Instrument</th><th>Level</th><th>Change</th><th>Note</th></tr></thead>
<tbody>@@RATES@@</tbody></table>
</div>
<p class="note">Treasury yields are TheStreet&rsquo;s <b>2:18 PM ET</b> &ldquo;Treasury Watch&rdquo;, citing CNBC
quotes, which records <b>fresh 52-week highs at every tenor from two years out</b>. Note the shape: the front end led
higher while the 20- and 30-year were marginally lower &mdash; a hike being priced rather than an inflation scare
extending down the curve.</p>

<h2 class="sec">On the Radar</h2>
<div class="panel">
<ul class="bul">
<li><b>The FOMC decides on Wednesday.</b> CME FedWatch had a hike at <b>85.6%</b> on the 10:03 AM read, up from a
coin-flip a week ago. Weinand at Regan Capital expects &ldquo;several rate hikes over the coming months in an effort to
get short-term interest rates in line with where the market is pricing yields.&rdquo;</li>
<li><b>A &ldquo;large bank&rdquo; gets sanctioned Monday.</b> Treasury Secretary Scott Bessent told Real America&rsquo;s
Voice the U.S. will sanction an unnamed large bank on Monday &mdash; deliberately held back from today to honour the
9/11 anniversary &mdash; and that a Turkish bank that &ldquo;had been giving to the Iranians&rdquo; will be closed. The
administration recently sanctioned the Dubai branches of Egypt&rsquo;s second-largest bank over $1.8 billion it believes
was routed to Iran.</li>
<li><b>Consumer sentiment is sagging on pump prices.</b> The University of Michigan&rsquo;s September preliminary
readings were on today&rsquo;s calendar, with headline sentiment expected at <b>51</b> against 51.7 previously; the
Motley Fool notes sentiment fell this month as high gas prices weigh on budgets.</li>
<li><b>Diesel has passed $6 a gallon for the first time</b> on a U.S. average basis, per GasBuddy &mdash; the sharpest
consumer-facing expression of the oil move, and a reason this week&rsquo;s crude spike has fed straight into inflation
expectations.</li>
<li><b>The war is the oil story.</b> President Trump said he has &ldquo;no regrets&rdquo; about the Iran war and, per
Capital.com&rsquo;s Kyle Rodda, comments that he sees it ending after the midterms &ldquo;sparked concerns that the US
is preparing for a war that will carry on in its current form at least until the end of the year.&rdquo; Houthi forces
seizing Yemen&rsquo;s port of Mocha and satellite imagery showing smoke near Saudi Arabia&rsquo;s East-West pipeline are
the supply risks the market is pricing.</li>
</ul>
</div>

<h2 class="sec">Sources</h2>
<div class="panel"><div class="srcs">@@SRC@@</div></div>

<p class="disc">The Closing Bell is information only and is not investment advice. Streaming quotes above come from
third-party widgets and may be delayed; editorial figures carry the time of the read that produced them. Nothing here
is a recommendation to buy or sell any security.</p>
"""

body = (BODY.replace("@@MAST@@", masthead("The Closing Bell", "Markets, movers and the macro calendar &mdash; refreshed through the session"))
            .replace("@@TLDR@@", tldr("The Tape", S_WS))
            .replace("@@FRESH@@", FRESH)
            .replace("@@NAV@@", nav("ws"))
            .replace("@@TICKER@@", TICKER)
            .replace("@@QUOTES@@", QUOTES)
            .replace("@@MOVERS@@", movers())
            .replace("@@RATES@@", raterows())
            .replace("@@SRC@@", srcblock(SRC)))

html = page("The Closing Bell &mdash; Daily Briefings", CSS, body)
io.open(os.path.join(OUT, "wallstreet-briefing.html"), "w", encoding="utf-8").write(html)
print("ws ok", len(html))
