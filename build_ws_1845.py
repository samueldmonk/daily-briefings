# -*- coding: utf-8 -*-
import io, common

TLDR = ("US markets are closed for the weekend: Friday ended a volatile Fed-hike week with the S&amp;P 500 "
        "and Nasdaq a touch higher and the Dow lower, the 10-year Treasury yield pressing toward 5% and "
        "the Dow down more than 1.5% on the week.")

TV = 'https://s3.tradingview.com/external-embedding/embed-widget-%s.js'

p = []
p.append(common.head("The Closing Bell &mdash; Daily Briefing", "ws"))
p.append(common.masthead("The Closing Bell",
         "Your daily markets briefing &mdash; the tape, the drivers and what&rsquo;s next"))
p.append(common.META)
p.append(common.tldr("The Tape", TLDR))
p.append(common.nav("ws"))

# BLOCK A - ticker tape
p.append('<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>'
         '<script src="' + (TV % 'ticker-tape') + '" async>'
         '{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},'
         '{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},'
         '{"proName":"FOREXCOM:DJI","title":"Dow 30"},'
         '{"proName":"NASDAQ:COIN","title":"Coinbase"},'
         '{"proName":"NASDAQ:AMAT","title":"Applied Materials"},'
         '{"proName":"NASDAQ:LRCX","title":"Lam Research"},'
         '{"proName":"NYSE:IBM","title":"IBM"},'
         '{"proName":"NYSE:DIS","title":"Disney"},'
         '{"proName":"TVC:USOIL","title":"WTI Crude"},'
         '{"proName":"TVC:US10Y","title":"US 10Y"}],'
         '"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,'
         '"displayMode":"adaptive","locale":"en"}</script></div>')

# BLOCK B - three single quotes
p.append(common.sec("Live index quotes &mdash; updates in real time"))
p.append('<div class="tickers">')
for sym in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI"):
    p.append('<div class="ticker"><script src="' + (TV % 'single-quote') + '" async>'
             '{"symbol":"%s","width":"100%%","colorTheme":"dark","isTransparent":true,'
             '"locale":"en"}</script></div>' % sym)
p.append('</div>')
p.append('<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects '
         'the latest edition; official closes are in the Weekly Scorecard.</div>')

# The lead
p.append(common.sec("The lead"))
p.append('<div class="lead"><h3>A Fed-hike week ends mixed, and the 10-year is the story going into Monday</h3>'
         '<p><b>US markets are closed for the weekend.</b> The figures below are Friday&rsquo;s official '
         'close, 18 September &mdash; re-verified this run against CNBC, TheStreet and Yahoo Finance, the '
         'eighth independent check this desk has run on them.</p>'
         '<p>Friday finished mixed and narrow. The <b>S&amp;P 500 rose 0.17%</b> and the <b>Nasdaq '
         'Composite advanced 0.39%</b>, while the <b>Dow shed 95.40 points, or 0.18%</b>. What made the '
         'week was not Friday: the Federal Reserve delivered its <b>first rate increase in three years</b> '
         'on 16 September, taking the funds target to <b>3.75%&ndash;4.00%</b>, and the benchmark '
         '<b>10-year Treasury yield pressed toward 5%</b> with oil elevated near $100.</p>'
         '<p><b>On the week</b>, the <b>Dow lost more than 1.5%</b>, the <b>S&amp;P 500 eked out a modest '
         'decline</b> and the <b>Nasdaq ended higher</b> &mdash; a split that says the damage was '
         'concentrated in the old-economy index while semiconductors recovered from the sharp selloff '
         'earlier in the week. Nine of the eleven broad sectors closed higher on Friday.</p></div>')

# Movers
p.append(common.sec("Movers &amp; drivers"))
p.append('<div class="cards">')
p.append('<div class="card"><span class="tag good">Up</span><span class="tag acc">Crypto / exchanges</span>'
         '<h3>Coinbase &mdash; the best performer in the Nasdaq 100</h3>'
         '<p>COIN <b>rose roughly 11&ndash;12%</b>, with readings of +11.77%, +12.07% and &ldquo;jumps '
         '12%&rdquo; on the record. The driver: the SEC issued a <b>five-year conditional '
         '&ldquo;Innovation Exemption&rdquo;</b> letting eligible venues trade <b>tokenised versions of '
         'US-listed stocks</b> without full traditional exchange registration. Baird framed the exemption '
         'as putting Coinbase&rsquo;s offering &ldquo;more on par&rdquo; with Robinhood&rsquo;s. Closing '
         'level: <b>$194.23</b> per the source that states it, against a <b>$194.25</b> reading carried '
         'from an earlier edition.</p></div>')
p.append('<div class="card"><span class="tag new">New</span><span class="tag good">Up</span>'
         '<span class="tag acc">Semis</span>'
         '<h3>Chip equipment outruns the sector</h3>'
         '<p>Capital-equipment names led the semiconductor recovery, on <b>future capital spending plans '
         'rather than current chip demand</b>: <b>Lam Research climbed 5%</b> and <b>KLA gained 3%</b>. '
         '<b>Applied Materials</b> rose alongside them, helped by a <b>multi-billion-dollar semiconductor '
         'research park investment in India</b> &mdash; reported elsewhere as $5 billion over the next '
         'decade. <b>No percentage is published for AMAT here:</b> five readings of the same session '
         '&mdash; +6.38%, +6.51%, an opening +3.03%, &ldquo;rises 4%&rdquo; and &ldquo;rose almost '
         '2%&rdquo; &mdash; are too far apart to resolve.</p></div>')
p.append('<div class="card"><span class="tag new">New</span><span class="tag crit">Down</span>'
         '<h3>The laggards had names</h3>'
         '<p>Friday&rsquo;s declines were led by <b>IBM (&minus;3.19%)</b>, <b>Walt Disney '
         '(&minus;2.68%)</b> and <b>Nike (&minus;2.26%)</b> &mdash; a trio with nothing in common except '
         'that none of them are semiconductors, which is roughly the shape of the whole week. '
         '<b>Technology and industrials</b> were the green sectors in an otherwise mixed tape.</p></div>')
p.append('</div>')

# Chart of the day
p.append(common.sec("Chart of the day &mdash; Coinbase (COIN)"))
p.append('<div class="panel" style="padding:8px"><script src="' + (TV % 'mini-symbol-overview') + '" async>'
         '{"symbol":"NASDAQ:COIN","width":"100%","height":240,"locale":"en","dateRange":"1D",'
         '"colorTheme":"dark","isTransparent":true,"autosize":false}</script></div>')
p.append('<p class="note">Friday&rsquo;s biggest single-name move among the majors, on the SEC&rsquo;s '
         'tokenised-securities exemption. Chart is live and will show the most recent session the feed '
         'has, not necessarily 18 September.</p>')

# Sector heat
p.append(common.sec("Sector heat &mdash; live"))
p.append('<div class="panel" style="padding:8px"><script src="' + (TV % 'stock-heatmap') + '" async>'
         '{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change",'
         '"grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,'
         '"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,"isMonoSize":false,'
         '"width":"100%","height":420}</script></div>')
p.append('<p class="note">Editorially, on Friday: <b>nine of the eleven broad sectors closed higher</b>, '
         'with <b>technology and industrials</b> green and semiconductor shares continuing their recovery '
         'from earlier in the week.</p>')

# Calendar
p.append(common.sec("The calendar &mdash; live"))
p.append('<div class="panel" style="padding:8px"><script src="' + (TV % 'events') + '" async>'
         '{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en",'
         '"importanceFilter":"0,1","countryFilter":"us"}</script></div>')

# Headlines
p.append(common.sec("Live market headlines &mdash; updates in real time"))
p.append('<div class="panel" style="padding:8px"><script src="' + (TV % 'timeline') + '" async>'
         '{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,'
         '"displayMode":"regular","width":"100%","height":420,"locale":"en"}</script></div>')

# Weekly scorecard
p.append(common.sec("Weekly scorecard &mdash; official closes, Friday 18 September"))
p.append('<div class="panel" style="padding:8px 10px"><table><thead><tr><th>Index</th><th>Close</th>'
         '<th>Day</th><th>On the week</th></tr></thead><tbody>'
         '<tr><td>S&amp;P 500</td><td class="mono">7,650.50</td><td class="up mono">+0.17%</td>'
         '<td class="down">a modest decline</td></tr>'
         '<tr><td>Nasdaq Composite</td><td class="mono">26,522.55</td><td class="up mono">+0.39%</td>'
         '<td class="up">higher</td></tr>'
         '<tr><td>Dow Jones Industrial Average</td><td class="mono">51,682.64</td>'
         '<td class="down mono">&minus;95.40 (&minus;0.18%)</td><td class="down">lost more than 1.5%</td></tr>'
         '<tr><td>Russell 2000</td><td class="mut">not published</td>'
         '<td class="down">lower, figure disputed</td><td class="mut">&mdash;</td></tr>'
         '</tbody></table></div>')
p.append('<p class="note">Levels and day moves are CNBC&rsquo;s, corroborated by TheStreet and Yahoo '
         'Finance. Two small disagreements are printed rather than smoothed: the Dow&rsquo;s points and '
         'percent change reconcile to within <b>1.81 points</b> of the stated level, and a separate '
         'account of the same session reads <b>S&amp;P +0.11%, Dow &minus;0.13%, Nasdaq +0.39%</b>. '
         'The Russell has four disagreeing readings &mdash; IWM &minus;0.47%, &minus;0.53% and '
         '&minus;0.75% against one account of IWM up 0.6% &mdash; so direction is published without a '
         'number. A <b>VIX reading of 14.82</b> and a <b>Brent crude price</b> were both refused for '
         'want of a stated date or source, and appear nowhere else on this page.</p>')

# Rates
p.append(common.sec("Rates, bonds &amp; commodities"))
p.append('<div class="panel" style="padding:8px 10px"><table><thead><tr><th>Instrument</th><th>Level</th>'
         '<th>Note</th></tr></thead><tbody>'
         '<tr><td>US 10-year Treasury</td><td class="mono">5.01%</td>'
         '<td>As of 18 September per CNBC. The yield <b>touched 5.041%</b> this week, its highest since '
         '<b>July 2007</b>. A <b>~4.94%</b> reading this desk carried earlier was not restated in '
         'anything read this run and appears only in this sentence.</td></tr>'
         '<tr><td>Fed funds target</td><td class="mono">3.75%&ndash;4.00%</td>'
         '<td>After a <b>25 bp hike on 16 September</b>, up from 3.50%&ndash;3.75% &mdash; the first '
         'increase in three years, with at least one more signalled.</td></tr>'
         '<tr><td>WTI crude</td><td class="mono">$100.30</td>'
         '<td>Settled <b>&minus;1.6%</b>. Saudi Arabia moved <b>2.8 million bpd</b> through the Strait of '
         'Hormuz over six days against <b>700,000 bpd</b> in August, and sold as many as <b>60 million '
         'barrels</b> from Ras Tanura for September/October loading via ship-to-ship transfer outside the '
         'strait &mdash; which eased supply fears. A separate weekly wrap describes oil simply as holding '
         'above $95.</td></tr>'
         '<tr><td>Oil / yield correlation</td><td class="mono">0.96</td>'
         '<td>One-month rolling correlation between front-month WTI and the 10-year yield &mdash; the '
         'strongest positive relationship since <b>June 2019</b>.</td></tr>'
         '</tbody></table></div>')

# On the radar
p.append(common.sec("On the radar &mdash; week of 21&ndash;25 September"))
p.append('<div class="panel"><ul class="bul">'
         '<li><b>The Fed does the talking.</b> The economic calendar is light on data and heavy on '
         'speakers, with central bankers making <b>no fewer than ten appearances</b> as the market looks '
         'for the path after the September hike.</li>'
         '<li><b>Monday.</b> Chicago Fed President <b>Goolsbee speaks at 10:30 AM ET</b>; the '
         '<b>Chicago Fed National Activity Index</b> lands at 12:30 PM ET.</li>'
         '<li><b>Tuesday.</b> <b>ADP weekly employment change at 8:15 AM ET</b>; earnings from '
         '<b>Thor Industries, AutoZone and KB Home</b>.</li>'
         '<li><b>Wednesday.</b> <b>S&amp;P Global flash manufacturing PMI</b>.</li>'
         '<li><b>Friday.</b> <b>University of Michigan consumer sentiment</b>, preliminary reading.</li>'
         '<li><b>Earnings through the week.</b> <b>Darden Restaurants</b> is expected at <b>$2.05 per '
         'share</b>, up 4.1% year over year, on revenue of <b>$3.2 billion</b>. Counts by day: 14 '
         'companies Monday, 11 Tuesday, 11 Wednesday, 18 Thursday, 2 Friday &mdash; which supersedes an '
         'earlier &ldquo;no noteworthy earnings Monday&rdquo; note this desk carried.</li>'
         '<li><b>The wildcard.</b> A <b>Trump&ndash;Xi meeting</b> is flagged as potentially the week&rsquo;s '
         'most important moment for the market.</li>'
         '</ul></div>')

p.append(common.srcs([
    ("https://www.cnbc.com/2026/09/17/stock-market-today-live-updates.html",
     "CNBC &mdash; stock market news for Sept. 18, 2026"),
    ("https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-18-2026",
     "TheStreet &mdash; Nasdaq, S&amp;P 500 close a touch higher to end Fed hike week"),
    ("https://finance.yahoo.com/markets/live/stock-market-today-friday-september-18-dow-sp-500-nasdaq-080504071.html",
     "Yahoo Finance &mdash; Dow, S&amp;P 500 post weekly losses as 10-year yield hovers near 5%"),
    ("https://www.cnbc.com/2026/09/18/stocks-making-the-biggest-moves-midday-nflx-xene-coin-sndk-spcx.html",
     "CNBC &mdash; stocks making the biggest moves midday, Sept. 18"),
    ("https://seekingalpha.com/news/4644518-coinbase-global-jumps-12-after-on-regulatory-win-for-tokenized-stock-trading",
     "Seeking Alpha &mdash; Coinbase jumps 12% on regulatory win for tokenised stock trading"),
    ("https://www.tipranks.com/news/coinbase-stock-coin-soars-12-as-baird-says-sec-exemption-puts-offerings-more-on-par-with-robinhoods",
     "TipRanks &mdash; Baird on the SEC exemption and Coinbase"),
    ("https://www.tradingkey.com/news/market-movers/262175736-market-movers-coin-20260918",
     "TradingKey &mdash; COIN moved up 11.77% on Sep 18"),
    ("https://247wallst.com/investing/2026/09/18/lam-research-climbs-5-as-chip-equipment-names-outrun-the-sector-applied-materials-rises-4-kla-corp-gains-3/",
     "24/7 Wall St. &mdash; Lam Research climbs 5% as chip equipment names outrun the sector"),
    ("https://www.benzinga.com/markets/tech/26/09/61869553/whats-going-on-with-applied-materials-stock-friday",
     "Benzinga &mdash; what&rsquo;s going on with Applied Materials stock Friday"),
    ("https://www.alainguillot.com/stock-market-recap-september-18-2026/",
     "Stock Market Recap &mdash; September 18, 2026 (sector detail and laggards)"),
    ("https://www.cnbc.com/quotes/US10Y", "CNBC &mdash; US 10-year Treasury yield"),
    ("https://www.cnbc.com/2026/09/15/oil-us-treasurys-stocks-pressure.html",
     "CNBC &mdash; oil and Treasury yields correlation"),
    ("https://www.cnbc.com/2026/09/18/stock-market-next-week-outlook-for-sept-21-25-2026.html",
     "CNBC &mdash; stock market next week: outlook for Sept. 21&ndash;25"),
    ("https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar",
     "Kiplinger &mdash; what to look out for in economic data this week"),
    ("https://www.kiplinger.com/investing/stocks/17494/next-week-earnings-calendar-stocks",
     "Kiplinger &mdash; earnings calendar for September 21&ndash;25"),
]))

p.append(common.footer(
    "For information only and not investment advice. Index levels, percentage moves and yields are as "
    "reported by the named sources at the time of reading and can be restated; where readings of the "
    "same session disagree, the disagreement is printed rather than resolved. Live widgets are supplied "
    "by TradingView and may be delayed."))
p.append(common.TAIL)

html = "".join(p)
io.open("wallstreet-briefing.html", "w", encoding="utf-8").write(html)
print("ws ok", len(html))
