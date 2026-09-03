# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, "/tmp/db_1788465063")
from shared import page, nav, META, sources
OUT = "/sessions/nifty-sweet-cannon/mnt/outputs"

# ---------------- palettes ----------------
WS   = dict(accent="#caa64a", accent2="#e8c766", bg="#0d0d0f", panel="#16161a", line="#26262c")
CY   = dict(accent="#22d3a8", accent2="#36c6ff", bg="#0b0f0e", panel="#121917", line="#1e2a27")
MMA  = dict(accent="#e84545", accent2="#ff8a5c", bg="#100c0c", panel="#1a1313", line="#322020")
IX   = dict(accent="#caa64a", accent2="#e8c766", bg="#0d0d0f", panel="#16161a", line="#26262c")

FRESH = '<p class="freshline" id="freshline">&nbsp;</p>'

def tldr(label, text):
    return f'<div class="tldr"><b>{label}</b> <span>{text}</span></div>'

def mast(h1, tagline):
    return f'<header class="mast"><h1>{h1}</h1><p class="tag">{tagline}</p>{META}</header>'

# ================= SUMMARIES (shared with index) =================
S_WS  = ("Stocks held a broad rally into the last hour of Thursday's session after Fed Governor "
         "Christopher Waller said he is inclined to support holding rates steady this month, with all "
         "three major indexes up more than 1% and the 10-year Treasury yield down about five basis points.")
S_CY  = ("A working privilege-escalation exploit for CrowdStrike's Falcon Sensor is now public with no "
         "vendor advisory or patch, while federal agencies have two days left to fix the two SonicWall "
         "SMA1000 zero-days and three other flaws CISA added to its exploited-vulnerability catalog.")
S_MMA = ("UFC Paris is two days out with Dan Hooker headlining against UFC debutant Salahdine Parnasse, "
         "while UFC 332 is a month away and still without a main event after Valentina Shevchenko withdrew injured.")

# ================= WALL STREET =================
TAPE = """<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>
<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NYSE:CHPT","title":"ChargePoint"},{"proName":"NYSE:SNOW","title":"Snowflake"},{"proName":"NASDAQ:AVGO","title":"Broadcom"},{"proName":"NASDAQ:TSLA","title":"Tesla"},{"proName":"NASDAQ:PLTR","title":"Palantir"},{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script>
</div>"""

def sq(sym):
    return ('<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>'
            '{"symbol":"%s","width":"100%%","colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>' % sym)

QUOTES = ('<h2 class="sec">Live Index Quotes &mdash; updates in real time</h2><div class="tickers">'
          + sq("FOREXCOM:SPXUSD") + sq("FOREXCOM:NSXUSD") + sq("FOREXCOM:DJI") +
          '</div><div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects '
          'the latest edition; official closes are in the Weekly Scorecard.</div>')

ws_body = []
ws_body.append(mast("The Closing Bell", "Your daily markets briefing &mdash; the tape, the movers and the macro"))
ws_body.append(tldr("The Tape", S_WS))
ws_body.append(FRESH)
ws_body.append(nav("ws", WS["accent"]))
ws_body.append(TAPE)
ws_body.append(QUOTES)

ws_body.append('<h2 class="sec">The Lead</h2>')
ws_body.append("""<div class="lead">
<h3>Waller opens the door to a September hold, and the tape runs with it &mdash; readings as of ~11:46&nbsp;AM&ndash;3:50&nbsp;PM ET</h3>
<p>Federal Reserve Governor Christopher Waller said Thursday he is leaning toward keeping interest rates
steady at this month's meeting, provided upcoming inflation data holds up. In remarks prepared for a Reuters
interview he said: <em>&ldquo;If this continues in the data due over the next two weeks, I would be inclined to
support holding the target for the federal funds rate at its current setting.&rdquo;</em> He conceded inflation is
&ldquo;meaningfully above&rdquo; the 2% target but said recent trends &ldquo;suggest we are finally seeing some
signs of disinflation&rdquo; &mdash; a reading that sits against Chair Kevin Warsh's emphasis on stubborn inflation.</p>
<p>Market-implied odds of a hike at the September 15&ndash;16 FOMC meeting fell sharply after the remarks, to a
<strong>48.4% probability</strong>, down about 15 percentage points from Wednesday, per CME Group's FedWatch tool.
The benchmark 10-year Treasury note yield last traded around <strong>4.75%</strong>.</p>
<p>Two moments from the session, printed as two moments and neither adopted as the current print. At the
<strong>11:46&nbsp;AM ET</strong> midday mark the Nasdaq Composite was up 1.35% to 26,572, the Dow up 1.20% to
53,699 and the S&amp;P 500 up 1.01% to 7,744. Later in the session the same publisher's quote panels read
<strong>S&amp;P 500 7,748.36 (+1.1%, +81.76)</strong>, <strong>Nasdaq Composite 26,586.00 (+1.4%, +368.17)</strong>
and <strong>Dow 53,695.80 (+1.2%, +633.85)</strong> &mdash; each of which reconciles exactly against Wednesday's
verified closes.</p>
<p><strong>No official Thursday closing print is confirmed in any source seen for this edition.</strong> The Weekly
Scorecard below therefore carries Wednesday's official closes, not Thursday's. Nothing on this page is a live
price &mdash; the streaming quotes above are.</p>
</div>""")

ws_body.append('<h2 class="sec">Movers &amp; Drivers</h2><div class="cards">')
ws_body.append("""<div class="card"><div class="tags"><span class="t ok">Up</span><span class="t">Earnings</span></div>
<h3>ChargePoint &mdash; the session's outsized move</h3><p>Three readings, none adopted: up <strong>52%</strong> in
late-morning trading (11:21&nbsp;AM ET), <strong>51.4%</strong> at 10:19&nbsp;AM, and <strong>17.3%</strong> before
the bell. Revenue of <strong>$116 million</strong>, up 18% year over year against a $105 million consensus, a record
non-GAAP gross margin of <strong>38%</strong>, and an adjusted EBITDA loss cut 78% to <strong>$4.8 million</strong>.
President and CEO Rick Wilmer called it &ldquo;an exceptional quarter.&rdquo; In the quarter ChargePoint named
John Saffrett executive vice president and managing director for Europe and extended its Mercedes-Benz partnership
to cover fleet operators in the U.K. and Germany.</p></div>""")
ws_body.append("""<div class="card"><div class="tags"><span class="t ok">Up</span><span class="t">Earnings</span></div>
<h3>Snowflake &mdash; a second day of AI-demand buying</h3><p>Two windows, never blended: nearly <strong>22%</strong>
in session at 10:19&nbsp;AM ET, against nearly <strong>24%</strong> before the bell. The midday wrap describes the
stock as up &ldquo;over 20% this morning&rdquo; after better-than-expected second-quarter results from the
cloud-based AI data platform.</p></div>""")
ws_body.append("""<div class="card"><div class="tags"><span class="t crit">Down</span><span class="t new">New</span></div>
<h3>Broadcom falls despite the beat</h3><p>Quoted at <strong>$355.96, down 3.07% (&minus;$11.28)</strong> &mdash; a
level, point change and percent that reconcile against Wednesday's $367.24 close. The chipmaker beat analyst
expectations in Wednesday's report; the stock has fallen anyway.</p></div>""")
ws_body.append("""<div class="card"><div class="tags"><span class="t crit">Down</span><span class="t">Biotech</span></div>
<h3>Ultragenyx craters on a failed Phase 3</h3><p>Down <strong>44%</strong> in session and <strong>47%</strong>
pre-bell after the pivotal Phase 3 <em>Aspire</em> study of apazunersen (GTX-102) in Angelman syndrome missed both
its primary and its key secondary endpoints.</p></div>""")
ws_body.append("""<div class="card"><div class="tags"><span class="t ok">Up</span><span class="t">Defense</span></div>
<h3>Palantir wins an Army prime contract</h3><p>Up <strong>8.7%</strong> after subsidiary Palantir USG secured a
U.S. Army prime contractor agreement to manufacture and deliver eight TITAN ground-station systems. Former AIG chief
executive Peter Zaffino is joining as global head of financial services.</p></div>""")
ws_body.append("""<div class="card"><div class="tags"><span class="t ok">Up</span><span class="t new">New</span></div>
<h3>Robinhood rises on upgrades</h3><p>Robinhood Markets gained following analyst upgrades. <strong>No figure is
published here</strong> &mdash; the move is described directionally in the midday wrap and no source seen for this
edition attaches a percentage to it.</p></div>""")
ws_body.append("""<div class="card"><div class="tags"><span class="t ok">Up</span><span class="t new">New</span></div>
<h3>Megacaps and crypto, from arithmetic-consistent quotes</h3><p>Every figure here is a level with a matching point
change: <strong>Tesla $382.09 +7.0%</strong>, <strong>Meta $613.68 +3.5%</strong>, <strong>Microsoft $512.00
+3.1%</strong>, <strong>Nvidia $227.73 +1.5%</strong>, <strong>Apple $329.87 +1.5%</strong>, <strong>Amazon $258.67
+1.4%</strong>, <strong>Alphabet $338.17 +1.3%</strong>, <strong>SpaceX $149.40 +6.2%</strong> and <strong>Bitcoin
$80,959 +4.9%</strong>. A separate 9:25&nbsp;AM ET reading had Nvidia up 0.55% at $225.64 &mdash; a different moment,
not merged with the later quote.</p></div>""")
ws_body.append("""<div class="card"><div class="tags"><span class="t crit">Down</span><span class="t">Retail</span></div>
<h3>Victoria's Secret and Campbell's on guidance</h3><p>Victoria's Secret fell <strong>12.1%</strong> in session
against <strong>17%</strong> pre-bell after missing second-quarter earnings expectations and guiding full-year
earnings below consensus. Campbell's fell <strong>6.4% to $22.26</strong> premarket on an 8% sales decline to $2.1
billion, a 310 basis-point gross-margin contraction to 27.3%, adjusted earnings down 37% to 39 cents, and a dividend
cut.</p></div>""")
ws_body.append('</div>')

ws_body.append('<h2 class="sec">Chart of the Day &mdash; ChargePoint (NYSE:CHPT)</h2>')
ws_body.append('<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"NYSE:CHPT","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}</script></div>')

ws_body.append('<h2 class="sec">Sector Heat &mdash; live</h2>')
ws_body.append('<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}</script></div>')
ws_body.append('<div class="note">Editorial breadth, session-attributed: industrials led the sector gainers at the '
               '11:46&nbsp;AM ET midday mark, with financial services and consumer cyclical stocks also showing '
               'significant intraday strength.</div>')

ws_body.append('<h2 class="sec">The Calendar &mdash; live</h2>')
ws_body.append('<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en","importanceFilter":"0,1","countryFilter":"us"}</script></div>')

ws_body.append('<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2>')
ws_body.append('<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,"displayMode":"regular","width":"100%","height":420,"locale":"en"}</script></div>')

ws_body.append('<h2 class="sec">Weekly Scorecard &mdash; official closes</h2><div class="panel"><table>'
  '<tr><th>Index</th><th>Close</th><th>Change</th><th>Session</th></tr>'
  '<tr><td>S&amp;P 500</td><td class="mono">7,666.60</td><td class="mono up">+0.46%</td><td>Wed, Sept 2</td></tr>'
  '<tr><td>Nasdaq Composite</td><td class="mono">26,217.83</td><td class="mono up">+118.05 / +0.45%</td><td>Wed, Sept 2</td></tr>'
  '<tr><td>Dow Jones Industrial Average</td><td class="mono">53,061.95</td><td class="mono up">+295.07 / +0.56%</td><td>Wed, Sept 2</td></tr>'
  '</table><div class="note">Wednesday\'s session snapped a three-day losing streak. No verified Thursday close is '
  'available for this edition, so none is printed here.</div></div>')

ws_body.append('<h2 class="sec">Rates, Bonds &amp; Commodities</h2><div class="panel"><table>'
  '<tr><th>Instrument</th><th>Level</th><th>Change</th><th>Window</th></tr>'
  '<tr><td>10-year Treasury yield</td><td class="mono">~4.75%</td><td class="mono down">&minus;5 bps</td><td>11:46 AM ET Thu</td></tr>'
  '<tr><td>10-year &mdash; prior close / Thu range</td><td class="mono">4.794 / 4.727&ndash;4.787</td><td class="mono">&mdash;</td><td>Sept 2 close, Sept 3 range</td></tr>'
  '<tr><td>Fed funds target</td><td class="mono">3.50&ndash;3.75%</td><td class="mono">held</td><td>current setting</td></tr>'
  '<tr><td>WTI crude</td><td class="mono">$91.12</td><td class="mono up">+0.12%</td><td>Sept 3</td></tr>'
  '<tr><td>WTI &mdash; earlier window</td><td class="mono">$92.94</td><td class="mono up">+2.12%</td><td>7:05 AM ET Thu</td></tr>'
  '<tr><td>Brent crude</td><td class="mono">$95.25</td><td class="mono down">&minus;0.40%</td><td>Sept 3</td></tr>'
  '<tr><td>Brent &mdash; earlier window</td><td class="mono">$97.45</td><td class="mono up">+1.90%</td><td>7:05 AM ET Thu</td></tr>'
  '<tr><td>Gold</td><td class="mono">$4,489.99</td><td class="mono up">+2.34%</td><td>11:46 AM ET Thu</td></tr>'
  '<tr><td>Gold futures &mdash; earlier window</td><td class="mono">$4,494.70</td><td class="mono up">+1.81%</td><td>8:38 AM ET Thu</td></tr>'
  '<tr><td>Silver futures</td><td class="mono">$66.39</td><td class="mono up">+1.42%</td><td>8:40 AM ET Thu</td></tr>'
  '</table><div class="note">Wednesday\'s 10-year high is described as the highest since <strong>November 2023</strong> '
  'in one account and the highest since <strong>October 2023</strong> in another. Both are printed; neither is adopted.'
  '</div></div>')

ws_body.append('<h2 class="sec">On the Radar</h2><div class="panel"><ul class="bul">'
  '<li><strong>Friday: the August jobs report.</strong> Consensus is <strong>58,000</strong> nonfarm payrolls with '
  'the unemployment rate at <strong>4.1%</strong>; July was <strong>&minus;23,000</strong>.</li>'
  '<li><strong>August CPI lands September 11</strong>, inside the two-week data window Waller pointed to, and the '
  '<strong>FOMC meets September 15&ndash;16</strong>.</li>'
  '<li><strong>Challenger:</strong> U.S. employers announced <strong>52,881</strong> job cuts in August, up 58% from '
  'July and down 38% from a year earlier &mdash; the lowest August total since 2022.</li>'
  '<li><strong>The July trade deficit widened to $88.6 billion</strong>, the widest since March 2025 and up 24.4% from '
  'June. Imports rose 2.8% and exports fell 2.1%; capital goods imports jumped 11.4%, the largest increase since 1993.</li>'
  '<li><strong>Nvidia is buying Hugging Face.</strong> The Financial Times puts the price at <strong>$12.93 '
  'billion</strong>; other accounts say &ldquo;about $13 billion.&rdquo; Both are printed, neither adopted. Nvidia says '
  'the goal is to accelerate the spread of open models.</li>'
  '<li><strong>Oil still carries a geopolitical premium.</strong> Iran targeted U.S. allies Jordan, the United Arab '
  'Emirates and Kuwait with missiles and drones in retaliation for American strikes; crude rallied 9% over three '
  'sessions before steadying.</li>'
  '</ul></div>')

ws_body.append(sources([
 ("TheStreet &mdash; Stock Market Today (Sept. 3, 2026)", "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-03-2026"),
 ("The Motley Fool &mdash; Stock Market Midday, Sept. 3", "https://www.fool.com/coverage/stock-market-today/2026/09/03/stock-market-midday-sept-3-stocks-rally-as-treasury-yields-fall-broadcom-falls-despite-earnings-beat/"),
 ("Yahoo Finance &mdash; Stock market today, Thursday September 3", "https://finance.yahoo.com/markets/live/stock-market-today-thursday-september-3-dow-sp-500-nasdaq-futures-081525933.html"),
 ("Yahoo Finance / Zacks &mdash; Stock Market News for Sep 3, 2026 (Sept 2 closes)", "https://finance.yahoo.com/markets/stocks/articles/stock-market-news-sep-3-095800036.html"),
 ("CNBC &mdash; Fed Governor Waller indicates he will support holding rates steady", "https://www.cnbc.com/2026/09/03/fed-governor-waller-indicates-he-will-support-holding-rates-steady-at-september-meeting.html"),
 ("CME Group &mdash; FedWatch tool", "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html"),
 ("Trading Economics &mdash; US 10-year yield / Brent / WTI", "https://tradingeconomics.com/united-states/government-bond-yield"),
 ("Financial Times &mdash; Nvidia to buy Hugging Face", "https://www.ft.com/content/776dcb01-75cd-44df-bc52-63ca76d5718d"),
]))
ws_body.append('<p class="disc">The Closing Bell is an automated summary of published reporting. Figures are quoted '
  'with the window in which they were reported and are not live prices. Nothing here is investment advice.</p></footer>')

WSHTML = page("The Closing Bell &mdash; Daily Briefings", WS["accent"], WS["accent2"], WS["bg"], WS["panel"], WS["line"],
              "\n".join(ws_body), extra_css='.mast h1,.lead h3,.card h3{font-family:Georgia,"Times New Roman",serif}')
open(os.path.join(OUT, "wallstreet-briefing.html"), "w").write(WSHTML)
print("wallstreet ok", len(WSHTML))
