# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page
from common_1635 import S_WS, tldr, FRESH, srcblock

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
 ("CNBC - Dow rises 500 points to snap 4-day slide as oil cools, traders look past inflation report",
  "https://www.cnbc.com/2026/09/10/stock-market-today-live-updates.html"),
 ("TV News Check - Dow Adds 509, Nasdaq Climbs 251, S&P 500 Gains 65",
  "https://tvnewscheck.com/business/article/dow-adds-509-nasdaq-climbs-251-sp-500-gains-65/"),
 ("Benzinga - S&P 500 Snaps 4-Day Decline as Oil Cools, Dell Jumps 11%",
  "https://www.benzinga.com/markets/market-summary/26/09/61745848/stocks-snap-four-day-slide-oil-cools-fed-hike-odds-90-percent-markets-friday"),
 ("TheStreet - Stock Market Today (Sept. 11, 2026): S&P 500, Dow recover as CPI report arrives in-line; oil falls",
  "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-11-2026"),
 ("TheStreet - Stock Market Today (Sept. 10, 2026): Stocks fall for fourth straight day as Brent oil hits $105/bbl",
  "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-10-2026"),
 ("Investing.com - Earnings call transcript: Zumiez posts Q2 2026 miss as stock sinks after hours",
  "https://www.investing.com/news/transcripts/earnings-call-transcript-zumiez-posts-q2-2026-miss-as-stock-sinks-after-hours-93CH-4896998"),
 ("WTOP - Frequency Electronics: Fiscal Q1 Earnings Snapshot",
  "https://wtop.com/national/2026/09/frequency-electronics-fiscal-q1-earnings-snapshot"),
 ("CME Group - FedWatch Tool",
  "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html"),
 ("CNBC - US 1-Year Treasury quote (curve reference)", "https://www.cnbc.com/quotes/US1y"),
 ("CNBC - Bessent says 'a large bank' to be sanctioned",
  "https://www.cnbc.com/2026/09/11/bessent-large-bank-sanctioned.html"),
 ("Yahoo Finance - Oracle posts cloud sales that top estimates on surging AI demand",
  "https://finance.yahoo.com/technology/articles/oracle-posts-cloud-sales-top-201512207.html"),
 ("24/7 Wall St. - Hewlett Packard Enterprise and Dell Surge 11% as Oracle's Capex Guidance Lifts AI Server Demand",
  "https://247wallst.com/investing/2026/09/11/hewlett-packard-enterprise-and-dell-surge-11-as-oracles-capex-guidance-lifts-ai-server-demand-super-micro-climbs-7/"),
]

TICKER = """<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>
<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NASDAQ:VICR","title":"Vicor"},{"proName":"NYSE:DELL","title":"Dell"},{"proName":"NYSE:HPE","title":"HPE"},{"proName":"NASDAQ:SWKS","title":"Skyworks"},{"proName":"NYSE:OKLO","title":"Oklo"},{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script>
</div>"""


def quote(sym):
    return ('<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>'
            '{"symbol":"' + sym + '","width":"100%","colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>')


QUOTES = '<div class="tickers">' + quote("FOREXCOM:SPXUSD") + quote("FOREXCOM:NSXUSD") + quote("FOREXCOM:DJI") + '</div>'

MOVERS = [
 (['<span class="t pro">best in the large-cap index</span>', '<span class="t">power components</span>'],
  "Vicor <span class='up'>+11.84%</span>",
  "The single best performer in the large-cap index on Benzinga&rsquo;s board, which was updated by <b>11:50 AM ET</b>. "
  "It is this edition&rsquo;s Chart of the Day."),
 (['<span class="t pro">leader</span>', '<span class="t">AI infrastructure</span>'],
  "Dell <span class='up'>+11.28%</span>, HPE <span class='up'>+9.08%</span>",
  "Both rode the read-through from Oracle&rsquo;s capital-spending guidance. HPE had posted record quarterly revenue of "
  "<b>$12.2 billion</b>, up <b>34%</b> year-over-year, with <b>$9.0 billion</b> from Cloud &amp; AI. Super Micro rose "
  "<b>6.1%</b> on the same theme."),
 (['<span class="t gold">M&amp;A</span>', '<span class="t">semis</span>'],
  "Skyworks <span class='up'>+8.04%</span>, Flex <span class='up'>+7.94%</span>",
  "A second straight session of gains for Skyworks after CEO Phil Brace told a Goldman Sachs conference that the "
  "<b>$22 billion</b> merger with Qorvo is in its final stages and should close by year-end."),
 (['<span class="t gold">earnings</span>', '<span class="t">the session&rsquo;s engine</span>'],
  "Oracle &mdash; flat shares, a $95 billion capex bill",
  "Adjusted EPS of <b>$1.92</b>, up <b>30%</b>, on revenue of <b>$19.35 billion</b> against a $19.14 billion consensus, "
  "with cloud infrastructure revenue up <b>121% to $7.4 billion</b> and remaining performance obligations swelling "
  "<b>$209 billion</b> year-over-year to <b>$664 billion</b>. Full-year capital expenditure was guided to "
  "<b>$90&ndash;95 billion</b>. Benzinga: the shares themselves &ldquo;traded flat&rdquo; &mdash; it was the capex line "
  "that lifted the whole AI-infrastructure complex."),
 (['<span class="t down">laggards</span>', '<span class="t">nuclear</span>'],
  "Oklo <span class='down'>&minus;7.10%</span>, X-Energy <span class='down'>&minus;5.12%</span>",
  "The downside was dominated by nuclear. Oklo entered an equity distribution agreement on Friday to sell up to "
  "<b>$1 billion</b> of Class A common stock through ten sales agents including Goldman Sachs, BofA Securities, "
  "Citigroup, J.P. Morgan and Morgan Stanley."),
 (['<span class="t down">downgrade</span>'],
  "Chewy <span class='down'>&minus;4.89%</span>, SailPoint <span class='down'>&minus;4.00%</span>, AeroVironment <span class='down'>&minus;3.60%</span>",
  "JPMorgan cut Chewy to Neutral from Overweight with a <b>$24</b> target, down from $29. SailPoint extended a "
  "post-earnings drift that began Wednesday, when second-quarter revenue of <b>$308.8 million</b> missed consensus "
  "despite an EPS beat and 25% ARR growth to <b>$1.23 billion</b>."),
 (['<span class="t">groceries</span>'],
  "Kroger <span class='up'>+2.1%</span>",
  "Reported EPS of <b>$1.09</b> before the open, ahead of the <b>$1.06</b> consensus. Adobe, which reported alongside "
  "Oracle after Thursday&rsquo;s close, was flat."),
 (['<span class="t gold">settlement</span>', '<span class="t">energy</span>'],
  "Crude settles back below the $100 line it broke this week",
  "Iranian state media said Tehran will sit down with Gulf states in <b>Oman next week</b> to discuss the Strait of "
  "Hormuz, and the headline knocked the war premium out of crude. West Texas Intermediate settled <b>2.4%</b> lower at "
  "<b>$100.05</b> and Brent <b>2.8%</b> lower at <b>$104.61</b>; a Benzinga midday read had WTI at <b>$99.36</b>, down "
  "<b>3.0%</b>. Even after Friday, <b>WTI is up 8.6% on the week</b> and more than <b>19%</b> over the past month."),
]


def movers():
    out = ['<div class="cards">']
    for tags, h, p in MOVERS:
        out.append('<div class="card"><div class="tags">%s</div><h3>%s</h3><p>%s</p></div>' % ("".join(tags), h, p))
    out.append('</div>')
    return "".join(out)


AH = [
 (['<span class="t pro">after hours</span>', '<span class="t gold">earnings beat</span>'],
  "Frequency Electronics <span class='up'>+27.3%</span> to $79",
  "Fiscal first-quarter earnings of <b>$0.41</b> a share on revenue of <b>$23.5 million</b>, against expectations of "
  "<b>$0.29</b> on <b>$19.25 million</b>. Revenue was a record and backlog climbed to <b>$129 million</b>. The move is "
  "measured from a regular-session close of <b>$62.06</b>."),
 (['<span class="t down">after hours</span>', '<span class="t">guidance cut</span>'],
  "Zumiez <span class='down'>&minus;14.7%</span> to $14.25",
  "An adjusted loss of <b>$0.17</b> a share on revenue of <b>$209 million</b>, missing estimates of a <b>$0.11</b> loss "
  "on <b>$213.1 million</b>. The stock had already fallen <b>4.8%</b> in regular trading, and management guided third "
  "quarter sales lower with earnings near breakeven."),
]


def ahcards():
    out = ['<div class="cards">']
    for tags, h, p in AH:
        out.append('<div class="card"><div class="tags">%s</div><h3>%s</h3><p>%s</p></div>' % ("".join(tags), h, p))
    out.append('</div>')
    return "".join(out)


RATES = [
 ("1-year Treasury", "4.341%", "+7.7 bps", "2:18 PM ET read"),
 ("2-year Treasury", "4.63%", "+8 bps", "52-week high"),
 ("3-year Treasury", "4.712%", "+6.5 bps", "52-week high"),
 ("5-year Treasury", "4.775%", "+4.2 bps", "52-week high"),
 ("7-year Treasury", "4.859%", "+2.7 bps", "52-week high"),
 ("10-year Treasury", "4.959%", "+1.5 bps", "52-week high"),
 ("20-year Treasury", "5.377%", "&minus;0.3 bps", "52-week high"),
 ("30-year Treasury", "5.346%", "&minus;1.5 bps", "52-week high"),
 ("WTI crude", "$100.05", "&minus;2.4%", "Friday settlement; up 8.6% on the week"),
 ("Brent crude", "$104.61", "&minus;2.8%", "Friday settlement; up 8.4% on the week"),
 ("Silver futures", "$65.17", "+0.37%", "early-trading read"),
 ("CBOE Volatility Index", "15.75", "&minus;11.7%", "Benzinga read, updated by 11:50 AM ET"),
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
<h3 style="margin:0 0 9px;font-size:20px">The losing streak ends at four: Dow adds 509 points at the close as crude settles back and CPI lands in line</h3>
<p style="margin:0 0 11px">Friday&rsquo;s official closes are in, and they reverse a week of selling. The
<b>Dow Jones Industrial Average advanced 509.19 points, or 0.98%</b>; the <b>S&amp;P 500 climbed 0.86%</b> and the
<b>Nasdaq Composite gained 0.96%</b>, adding <b>65</b> and <b>251</b> points respectively. All three had fallen for four
consecutive sessions going in, with the Dow carrying its <b>longest daily losing streak since late April</b>. Levels
are in the Weekly Scorecard below.</p>
<p style="margin:0 0 11px">The catalyst was crude giving ground rather than the inflation print. Iranian state media
said Tehran will meet Gulf states in <b>Oman next week</b> to discuss the Strait of Hormuz, and the war premium came
out of the barrel: <b>WTI settled 2.4% lower at $100.05</b> and <b>Brent 2.8% lower at $104.61</b>, back below the
$100 mark WTI breached earlier in the week. It was still a violent week in energy &mdash; <b>WTI finished up 8.6%</b>
and is more than <b>19%</b> higher over the past month, and AAA reported U.S. diesel at a record
<b>$6.05 a gallon</b>.</p>
<p style="margin:0 0 11px">August <b>CPI rose 0.4%</b> on the month &mdash; the most in three months, with a
<b>3.9% jump in gasoline</b> accounting for more than a third of the increase &mdash; for an annual rate of
<b>3.4%</b>, in line with the Dow Jones consensus. <b>Core CPI rose 0.3%</b>, a tenth above forecast and the fastest
since April, even as the annual core rate eased to a <b>five-year low of 2.4%</b>. Market-implied odds of a hike at
next week&rsquo;s <b>15&ndash;16 September</b> FOMC moved from roughly <b>70% to around 90%</b>; TheStreet&rsquo;s
10:03 AM CME FedWatch read put it at <b>85.6%</b>.</p>
<p style="margin:0">&ldquo;Friday&rsquo;s CPI print was in-line with expectations, but inflation is still too hot, and
the Federal Reserve&rsquo;s hands are tied,&rdquo; said Skyler Weinand, chief investment officer at Regan Capital.
&ldquo;A rate hike next week is all but assured.&rdquo; Jeffrey Roach, chief economist at LPL Financial, made the
opposite-facing point: a hike&rsquo;s &ldquo;impact may be muted&rdquo; because a growing share of activity is less
interest-rate sensitive.</p>
</div>

<h2 class="sec">Movers &amp; Drivers</h2>
@@MOVERS@@
<p class="note">Percentages in this section come from Benzinga&rsquo;s Russell 1000 leaderboard, <b>updated by
11:50 AM ET</b>, and its accompanying prose; they are intraday reads rather than closing marks. TheStreet&rsquo;s
<b>1:04 PM</b> screen of the biggest winners above a $2 billion market capitalisation was led by <b>$VICR</b>,
<b>$DELL</b>, <b>$HPE</b>, <b>$MRNA</b> and <b>$SANM</b>, and its <b>12:32 PM</b> screen of the bottom 20 by
<b>$SMR</b>, <b>$OKLO</b>, <b>$SLS</b>, <b>$STX</b> and <b>$CHWY</b> &mdash; two small-modular-reactor names heading
the decliners on a day the broad tape closed up around a percent. Those screens carry their percentages inside images,
so no figure is attached to names that do not appear elsewhere on this page.</p>

<h2 class="sec">Chart of the Day &mdash; Vicor, the session&rsquo;s single best large-cap performer</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"NASDAQ:VICR","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}</script>
</div>

<h2 class="sec">After-Hours Movers</h2>
@@AH@@
<p class="note">Both moves are measured against Friday&rsquo;s regular-session close and were reported after the bell.
No other after-hours move was corroborated by a source read this run, so none is listed.</p>

<h2 class="sec">Sector Heat &mdash; live</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}</script>
</div>
<p class="note">Editorially, the gains were broad but heavily concentrated in technology: <b>XLK led all sectors at
+1.7%</b>, ahead of communication services at <b>+1.3%</b> and industrials at <b>+1.2%</b>, while <b>health care was
the only sector in the red at &minus;0.2%</b>. At industry level the VanEck Semiconductor ETF was the standout, up
<b>2.0%</b>. The small-cap Russell 2000 lagged the majors, adding <b>0.7%</b>.</p>

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
<table><thead><tr><th>Index</th><th>Friday&rsquo;s close</th><th>Change</th><th>Percent</th></tr></thead>
<tbody>
<tr><td><b>S&amp;P 500</b></td><td>7,656.98</td><td class="up">+65</td><td class="up">+0.86%</td></tr>
<tr><td><b>Nasdaq Composite</b></td><td>26,333.04</td><td class="up">+251</td><td class="up">+0.96%</td></tr>
<tr><td><b>Dow Jones Industrial Average</b></td><td>52,573.29</td><td class="up">+509.19</td><td class="up">+0.98%</td></tr>
</tbody></table>
</div>
<p class="note">These are Friday&rsquo;s official closes and the only index levels printed on this page. Each
reconciles to the cent against Thursday&rsquo;s verified closes of <b>7,591.70</b>, <b>26,081.72</b> and
<b>52,064.10</b> &mdash; the fourth straight down session, which this one ends.</p>

<h2 class="sec">Rates, Bonds &amp; Commodities</h2>
<div class="panel" style="padding:6px 10px">
<table><thead><tr><th>Instrument</th><th>Level</th><th>Change</th><th>Note</th></tr></thead>
<tbody>@@RATES@@</tbody></table>
</div>
<p class="note">Treasury yields are TheStreet&rsquo;s <b>2:18 PM ET</b> &ldquo;Treasury Watch&rdquo;, citing CNBC
quotes, which records <b>fresh 52-week highs at every tenor from two years out</b>. Note the shape: the front end led
higher while the 20- and 30-year were marginally lower &mdash; a hike being priced rather than an inflation scare
extending down the curve. <b>No gold figure is printed:</b> three feeds read this week disagreed on direction as well
as level, so the line is left off rather than reconciled.</p>

<h2 class="sec">On the Radar</h2>
<div class="panel">
<ul class="bul">
<li><b>The FOMC meets Tuesday and Wednesday.</b> The <b>15&ndash;16 September</b> meeting ends with a decision at
<b>2:00 PM ET on Wednesday</b>, accompanied by a Summary of Economic Projections. Market-implied odds of a hike moved
from roughly <b>70% to around 90%</b> on the CPI print. Weinand at Regan Capital expects &ldquo;several rate hikes over
the coming months in an effort to get short-term interest rates in line with where the market is pricing
yields.&rdquo;</li>
<li><b>A &ldquo;large bank&rdquo; gets sanctioned Monday.</b> Treasury Secretary Scott Bessent told Real America&rsquo;s
Voice the U.S. will sanction an unnamed large bank on Monday &mdash; deliberately held back from today to honour the
9/11 anniversary &mdash; and that a Turkish bank that &ldquo;had been giving to the Iranians&rdquo; will be closed.</li>
<li><b>Diesel is at a record.</b> AAA reported the U.S. average at <b>$6.05 a gallon</b> on Friday &mdash; the sharpest
consumer-facing expression of the oil move, and a reason this week&rsquo;s crude spike fed straight into inflation
expectations.</li>
<li><b>Oman is the swing factor in energy.</b> The Strait of Hormuz talks Iranian state media flagged for next week are
what took the premium out of crude on Friday. If they slip, the move reverses.</li>
<li><b>Dell joins the S&amp;P 100 on 21 September</b>, an index change already flagged this week alongside RBC&rsquo;s
initiation of the stock at Outperform.</li>
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
            .replace("@@AH@@", ahcards())
            .replace("@@RATES@@", raterows())
            .replace("@@SRC@@", srcblock(SRC)))

html = page("The Closing Bell &mdash; Daily Briefings", CSS, body)
io.open(os.path.join(OUT, "wallstreet-briefing.html"), "w", encoding="utf-8").write(html)
print("ws ok", len(html))
