# -*- coding: utf-8 -*-
import io, os, re
OUT="/sessions/fervent-pensive-ramanujan/mnt/outputs"
CORE=open('/tmp/core.css').read()

def vars_block(bg,panel,line,accent,accent2):
    return (":root{\n  --bg:%s; --panel:%s; --line:%s;\n  --accent:%s; --accent2:%s;\n"
            "  --text:#e8e6e3; --muted:#9aa0a6;\n  --up:#22c55e; --down:#ef4444; --warn:#f0a132; --crit:#ef4444;\n"
            "  --mono:ui-monospace,SFMono-Regular,\"SF Mono\",Menlo,Consolas,monospace;\n}\n")%(bg,panel,line,accent,accent2)

def css_for(bg,panel,line,accent,accent2,extra=""):
    body=CORE.split('}\n',0)
    # replace the :root block at the top of CORE
    c=re.sub(r':root\{.*?\n\}\n', vars_block(bg,panel,line,accent,accent2), CORE, count=1, flags=re.S)
    return c+extra

NAV_ITEMS=[("index.html","&#9733; Front Page"),
           ("cyber-briefing.html","&#9960; The Cyber Wire"),
           ("wallstreet-briefing.html","&#9650; The Closing Bell"),
           ("mma-briefing.html","&#8856; The Octagon"),
           ("archive.html","&#128452; Archive")]
def nav(active):
    return '<nav class="tabs">'+''.join(
        '<a href="%s"%s>%s</a>'%(h,' class="active"' if h==active else '',t) for h,t in NAV_ITEMS)+'</nav>'

META='<div class="meta"><span class="pill live"><span class="dot"></span>Live</span><span class="pill" id="edition">&nbsp;</span><span class="pill" id="datestamp">&nbsp;</span><span class="pill">Updated <span id="updated">&nbsp;</span></span></div>'

STAMP=("<script>(function(){try{var n=new Date();"
 "var et=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'long',year:'numeric',month:'long',day:'numeric'}).format(n);"
 "var t=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',minute:'2-digit'}).format(n);"
 "var h=parseInt(new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',hour12:false}).format(n),10);"
 "var ed=h<11?'Morning Edition':(h<15?'Midday Edition':'Afternoon Edition');"
 "document.getElementById('datestamp').textContent=et;document.getElementById('updated').textContent=t+' ET';"
 "document.getElementById('edition').textContent=ed;var fl=document.getElementById('freshline');"
 "if(fl)fl.textContent='Data as of '+t+' ET \\u00b7 briefings refresh every 30 minutes, 8 AM\\u20136 PM ET';}catch(e){}})();</script>")

def page(title,css,masthead,body,active):
    return ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
      '<meta name="viewport" content="width=device-width,initial-scale=1">'
      '<title>%s</title><style>\n%s</style></head><body><div class="wrap">%s%s%s</div>%s</body></html>'
      %(title,css,masthead,nav(active),body,STAMP))

def mast(h1,tagline,tldr_label=None,tldr=None):
    s='<div class="masthead"><h1>%s</h1><p class="tag">%s</p>%s</div>'%(h1,tagline,META)
    if tldr:
        s+='<div class="tldr"><b>%s</b> <span>%s</span></div>'%(tldr_label,tldr)
    s+='<div class="freshline" id="freshline">&nbsp;</div>'
    return s

def srcs(items):
    return '<footer><h5>Sources</h5><ul>'+''.join('<li><a href="%s">%s</a></li>'%(u,t) for u,t in items)+'</ul>'

# ============================================================ WALL STREET
WS_EXTRA=""".masthead h1{font-family:Georgia,'Times New Roman',serif;color:var(--accent2)}
h3,h2.lead{font-family:Georgia,'Times New Roman',serif}
.livebar{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 8px 4px;margin-bottom:18px}
.livebar-label{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--up);
  display:flex;align-items:center;gap:8px;padding:4px 8px 8px}
.livebar-label .dot{width:7px;height:7px;border-radius:50%;background:var(--up);display:inline-block}
.tickers{display:grid;gap:11px;grid-template-columns:1fr}
@media(min-width:700px){.tickers{grid-template-columns:repeat(3,1fr)}}
.ticker{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 10px}
"""
WSCSS=css_for("#0d0c0a","#171512","#2b2721","#caa64a","#e8c766",WS_EXTRA)

TICKER='<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div><script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NYSE:DELL","title":"Dell"},{"proName":"NASDAQ:PANW","title":"Palo Alto"},{"proName":"NASDAQ:AVGO","title":"Broadcom"},{"proName":"NYSE:SNOW","title":"Snowflake"},{"proName":"NASDAQ:CRDO","title":"Credo"},{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script></div>'

def sq(sym):
    return '<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>{"symbol":"%s","width":"100%%","colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>'%sym

QUOTES=('<h2 class="sec">Live Index Quotes &mdash; updates in real time</h2><div class="tickers">'
  +sq("FOREXCOM:SPXUSD")+sq("FOREXCOM:NSXUSD")+sq("FOREXCOM:DJI")+'</div>'
  '<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the latest edition; official closes are in the Weekly Scorecard.</div>')

TIMELINE='<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2><div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,"displayMode":"regular","width":"100%","height":420,"locale":"en"}</script></div>'
HEAT='<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}</script></div>'
CAL='<h2 class="sec">The Calendar &mdash; live</h2><div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en","importanceFilter":"0,1","countryFilter":"us"}</script></div>'
MINI='<h2 class="sec">Chart of the Day &mdash; Dell Technologies (DELL)</h2><div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"NYSE:DELL","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}</script></div>'

WS_TLDR=("Wall Street snapped a three-day losing streak at Wednesday's close &mdash; S&amp;P 500 +0.46%, Dow +295.07 points, "
 "Nasdaq Composite +0.45% &mdash; led by Dell, the index's best performer on record AI-server orders, while Palo Alto Networks fell "
 "roughly 11% and Broadcom slipped after the bell.")

ws=[]
ws.append(TICKER); ws.append(QUOTES)
ws.append('<h2 class="sec">The Lead</h2><div class="panel">'
 '<h3>Stocks snap a three-day skid, and Dell&rsquo;s AI backlog is the reason the close looks the way it does</h3>'
 '<p>All three major U.S. indexes finished Wednesday, September 2 higher, ending a three-session losing streak. The '
 '<b>S&amp;P 500 rose 0.46%</b>, the <b>Dow Jones Industrial Average added 295.07 points, or 0.56%</b>, and the '
 '<b>Nasdaq Composite gained 0.45%</b>. Those closes were re-confirmed against a fresh fetch this run, not carried forward.</p>'
 '<p>The session had a single clear engine. <b>Dell Technologies was the best-performing stock in the S&amp;P 500</b>, '
 'after booking a record <b>$60.9 billion in AI-server orders</b> and exiting the quarter with a record <b>$95 billion backlog</b>. '
 'Fiscal Q2 earnings of <b>$7.04 per share</b> cleared a $4.92 estimate on <b>$46.97 billion</b> of revenue against $44.92 billion expected, '
 'up 58% year over year, and the company lifted its annual outlook. Sources disagree on the size of the move &mdash; one puts Dell up 13%, '
 'another &ldquo;nearly 11%&rdquo; &mdash; so the magnitude is printed both ways below and neither is adopted. '
 '<b>Nvidia was the best performer in the Dow, up more than 3%.</b></p>'
 '<p>The offsetting story was a cybersecurity name beating estimates and being sold anyway: <b>Palo Alto Networks was the worst '
 'performer in the S&amp;P 500</b>, down about 11% despite fiscal Q4 results that topped Wall Street on what the company called a strong '
 'market for AI security. The 10-year Treasury yield touched an intraday high and then eased, which is what let the indexes turn; '
 'how far back that high reaches is disputed three ways and is set out in the rates section rather than settled here.</p>'
 '<div class="note"><b>How this edition was built.</b> Research for this run was fetched between 5:09 and 5:22 PM ET, roughly 80 minutes after the close. '
 'The index closes are official and each reconciles arithmetically against Tuesday’s verified closes '
 '(S&amp;P 7,631.47; Dow 52,766.88; Nasdaq 26,099.77). Intraday figures carry the time their source published them. '
 'Where the live widgets above and this editorial disagree, the widgets are right.</div></div>')

ws.append('<h2 class="sec">Movers &amp; Drivers</h2><div class="cards two">'
 '<div class="card"><div class="k">Dell Technologies (DELL)</div><h4><span class="up">+13% / &ldquo;nearly 11%&rdquo;</span></h4>'
 '<span class="tag new">New</span><p>The best-performing stock in the S&amp;P 500 on the session. Record $60.9B in AI-server orders, '
 'a record $95B backlog, fiscal Q2 EPS of $7.04 against $4.92 expected on $46.97B of revenue (+58% year over year), and a raised annual outlook. '
 'Two sources this run give the move as +13% and as &ldquo;nearly 11%&rdquo;; both are printed, neither adopted. Citi and Bank of America '
 'each raised their target to $600. The stock has more than tripled in 2026.</p></div>'
 '<div class="card"><div class="k">Palo Alto Networks (PANW)</div><h4><span class="down">&minus;10.9%</span></h4>'
 '<p>The worst performer in the S&amp;P 500, sold despite fiscal Q4 results that beat expectations on strong AI-security demand. '
 'A separate fetch gives the close as &minus;10.82% to $323.08; TheStreet had it &minus;7.8% at 10:36 AM ET. Benzinga frames the slide '
 'against rising bond yields on inflation fears.</p></div>'
 '<div class="card"><div class="k">Nvidia (NVDA)</div><h4><span class="up">+3%+</span></h4><span class="tag new">New</span>'
 '<p>The best-performing Dow component on the day, up more than 3% &mdash; the AI-infrastructure bid that carried Dell reached the '
 'index’s largest chip name as well.</p></div>'
 '<div class="card"><div class="k">Credo Technology (CRDO)</div><h4><span class="down">&minus;20.69% to $163.87</span></h4>'
 '<p>Record fiscal Q1 revenue of $479M, up 114.7% year over year and ahead of estimates, undone by shrinking margins and rising R&amp;D. '
 'The largest single-name regular-session decline sourced across today’s runs; the pair reconciles to the cent against the sourced '
 'prior close of $206.63.</p></div>'
 '<div class="card"><div class="k">MongoDB (MDB)</div><h4><span class="down">&minus;13.84% to $374.64</span></h4>'
 '<p>Beat second-quarter earnings expectations but issued cautious guidance; the stock was already down 12.4% in the 8:15 AM premarket.</p></div>'
 '<div class="card"><div class="k">PG&amp;E (PCG)</div><h4><span class="down">&minus;9.7% at 10:36 AM ET</span></h4>'
 '<p>The utility cut its capital spending plans amid continuing uncertainty over California&rsquo;s wildfire liability framework. '
 'Edison International (EIX) fell 7.6% the same hour as lawmakers advanced Senate Bill 492 without wildfire liability protections.</p></div>'
 '</div>'
 '<div class="note">Also sourced today: Reddit (RDDT) +7% and Uber (UBER) +0.58% to $75.68 at 10:15 AM ET after announcing it will cut about '
 '10% of its workforce; AST SpaceMobile (ASTS) +10.93% to $61.89 at the close. A live after-hours board also showed Eos Energy (EOSE) +20.10% '
 'and Faeth Therapeutics (FTH) +14.25%, but that board carries no publication time, so those two are noted rather than published as a session move.</div>')

ws.append(MINI)
ws.append('<div class="note"><b>Why this slot.</b> Dell is the session&rsquo;s defining name: the best performer in the S&amp;P 500, on the '
 'largest sourced fundamental catalyst of the day &mdash; a record $60.9 billion of AI-server orders and a record $95 billion backlog against '
 'fiscal Q2 EPS of $7.04 versus $4.92 expected. It displaces Credo, which held this slot earlier today on a larger percentage move '
 '(&minus;20.69%) but is a smaller company outside the index and had already been explained. The one thing this edition will not do is pick '
 'between the +13% and &ldquo;nearly 11%&rdquo; readings of Dell&rsquo;s move; the chart above settles it live.</div>')

ws.append('<h2 class="sec">Sector Heat &mdash; live</h2>'+HEAT+
 '<div class="note"><b>The static sector table is refused for a seventh consecutive run.</b> The only sector-bearing source available again '
 'this run dates its &ldquo;energy leads, +1.3%&rdquo; line and its &ldquo;four of 11 sectors higher&rdquo; count to <b>September 1</b>, and it '
 'reports Tuesday&rsquo;s index closes as though they were Wednesday&rsquo;s. A source that mis-dates the closes it leads with does not supply '
 'the day’s sector table. What that source does support, on a year-to-date basis rather than a daily one, is that <b>energy is 2026&rsquo;s '
 'leading sector</b> &mdash; the Energy Select Sector SPDR (XLE) up <b>+42.32% year to date</b> and trading at a 13.0&times; P/E &mdash; with '
 '<b>technology the worst performer</b>. The one sourced sector statement from Wednesday itself remains TheStreet&rsquo;s 12:05 PM ET note that '
 'advances came &ldquo;from virtually every sector but tech, real estate, and utilities.&rdquo; The live heatmap above is the sector read.</div>')

ws.append(CAL)
ws.append(TIMELINE)

ws.append('<h2 class="sec">After-Hours Movers</h2><div class="cards two">'
 '<div class="card"><div class="k">Snowflake (SNOW)</div><h4><span class="up">+21%</span></h4>'
 '<p>Q2 EPS of $0.62 beat the $0.45 estimate on revenue of $1.55 billion, with Q3 revenue guided to $1.588&ndash;$1.593 billion. '
 'Figure from an after-hours movers report published 4:30 PM ET.</p></div>'
 '<div class="card"><div class="k">Broadcom (AVGO)</div><h4><span class="down">&minus;3.5% / &minus;5%</span></h4>'
 '<span class="tag new">New</span><p>Q3 EPS of $3.32 cleared the $3.21 estimate on $29.59 billion of revenue, but Q4 revenue guidance of '
 '$34.8 billion came in under the $35.05 billion consensus. <b>Four different magnitudes are now in circulation for this one move</b> &mdash; '
 '&minus;3.5% (the only one carrying a publication time, 4:30 PM ET), &minus;5% newly sourced this run, plus &ldquo;about &minus;6.5%&rdquo; '
 'and &minus;4.14% &ldquo;in extended trading.&rdquo; The disagreement is printed rather than reconciled; only the direction is firm.</p></div>'
 '<div class="card"><div class="k">Hewlett Packard Enterprise (HPE)</div><h4><span class="down">&minus;1%</span></h4>'
 '<p>A clean beat-and-raise sold anyway &mdash; Q3 EPS $1.11 against $0.92 expected on $12.2 billion of revenue, FY26 EPS guidance lifted to '
 '$3.75&ndash;$3.85 and Q4 revenue guided to $13.9&ndash;$14.8 billion. HPE had risen 3.8% in the premarket.</p></div></div>'
 '<div class="note">Extended-hours prices move continuously; the figures above are a snapshot taken roughly half an hour after the close, '
 'not settlements. This run is about 80 minutes past the bell, and no later timestamped after-hours report was found.</div>')

ws.append('<h2 class="sec">Weekly Scorecard &mdash; official closes, Wednesday Sept 2</h2><div class="tblwrap"><table>'
 '<tr><th>Index</th><th>Close</th><th>Change</th><th>%</th></tr>'
 '<tr><td>S&amp;P 500</td><td>7,666.60</td><td class="up">+35.13</td><td class="up">+0.46%</td></tr>'
 '<tr><td>Nasdaq Composite</td><td>26,217.83</td><td class="up">+118.06</td><td class="up">+0.45%</td></tr>'
 '<tr><td>Dow Jones Industrial Average</td><td>53,061.95</td><td class="up">+295.07</td><td class="up">+0.56%</td></tr>'
 '</table></div>'
 '<div class="note">Levels are published because all three reconcile: adding each index&rsquo;s point change to Tuesday&rsquo;s verified close '
 'reproduces Wednesday&rsquo;s level exactly (7,631.47 + 35.13 = 7,666.60; 52,766.88 + 295.07 = 53,061.95; 26,099.77 + 118.06 = 26,217.83), and '
 'each percentage checks against those levels. The three closes were independently re-fetched this run and came back identical. The S&amp;P and '
 'Nasdaq point changes are derived from that reconciliation rather than quoted directly.</div>')

ws.append('<h2 class="sec">Rates, Bonds &amp; Commodities</h2><div class="tblwrap"><table>'
 '<tr><th>Instrument</th><th>Level</th><th>Note</th></tr>'
 '<tr><td><b>10-year Treasury</b></td><td>4.799%</td><td>Newly sourced this run as the September 2 close, with a session range of 4.765% to 4.820%. '
 'An earlier fetch had it easing to 4.77% after an intraday high. How far back that high reaches is disputed three ways &mdash; see the note below.</td></tr>'
 '<tr><td><b>2-year Treasury</b></td><td>4.369%</td><td>Tuesday&rsquo;s settlement, reported then as the highest in 19 months. Carried from a prior fetch; not re-sourced this run.</td></tr>'
 '<tr><td><b>30-year Treasury</b></td><td>5.27%</td><td>Tuesday. Carried from a prior fetch; not re-sourced this run.</td></tr>'
 '<tr><td><b>Fed funds target</b></td><td>&mdash;</td><td>Not sourced this run; no figure published.</td></tr>'
 '<tr><td><b>WTI crude</b></td><td>$90.76</td><td>Settled up 0.60%, a third consecutive advancing session. A separate read this run describes '
 'a modest pullback in oil easing inflation pressure, with energy prices near six-week highs.</td></tr>'
 '<tr><td><b>Brent crude</b></td><td>$94.28</td><td>&minus;0.39% as of 9:24 AM ET &mdash; an intraday quote, not a settlement.</td></tr>'
 '<tr><td><b>Gold</b></td><td>$4,355</td><td>&minus;0.94% in early trading (7:09 AM ET). Silver $64.26, &minus;1.69% (7:13 AM ET).</td></tr>'
 '<tr><td><b>Bitcoin</b></td><td>$76,763.96</td><td>&minus;1.43% at 11:04 AM ET.</td></tr>'
 '</table></div>'
 '<div class="note"><b>The yield descriptor now disagrees three ways, and this edition adopts none of them.</b> TheStreet, citing CNBC, has the '
 '10-year&rsquo;s intraday high at 4.814%, &ldquo;its highest level since <b>November 2023</b>.&rdquo; A fresh fetch this run has the yield '
 'pausing above 4.81% after a five-session rally, &ldquo;its highest level since <b>October 2023</b>.&rdquo; Yahoo and the WSJ excerpt it quotes '
 'describe Tuesday&rsquo;s 4.79%/4.798% as the highest since <b>January 2025</b>. Three descriptors for one yield. The 4.799% close and the '
 '4.765&ndash;4.820% range are published because they are a stated close and a stated range; the &ldquo;highest since&rdquo; claim is not '
 'published as fact in any table cell. Also sourced but not tabled: the 10-year&rsquo;s 50-day moving average at 4.32%.</div>')

ws.append('<h2 class="sec">On the Radar</h2><div class="panel"><ul class="b">'
 '<li><b>Thursday, Sept 3:</b> ISM Services; earnings from Ciena (CIEN) and Lululemon (LULU).</li>'
 '<li><b>Friday, Sept 4:</b> August nonfarm payrolls, consensus 45,000. ADP&rsquo;s August private-payroll print came in at +38,000 against a '
 '+47,000 estimate, with July revised up to +46,000 &mdash; the slowest month since January. Education and health services added 45,000; '
 'manufacturing shed 17,000 and professional and business services 16,000.</li>'
 '<li><b>Monday, Sept 7:</b> Labor Day &mdash; U.S. markets closed.</li>'
 '<li><b>FOMC:</b> September 15&ndash;16. CME FedWatch put the odds of a <i>hike</i> at 66.1% as of Monday, up from 35.4% before Chair '
 'Kevin Warsh&rsquo;s remarks.</li>'
 '<li><b>Trade:</b> Commerce Secretary Howard Lutnick told CNBC a semiconductor tariff framework is being developed &mdash; &ldquo;if you build '
 'here, you don&rsquo;t pay&rdquo; &mdash; with no rate or date made public.</li>'
 '<li><b>Geopolitics:</b> Iran&rsquo;s Revolutionary Guards said two oil tankers struck naval mines attempting to transit the Strait of Hormuz; '
 'Middle East hostilities remain elevated and energy prices sit near six-week highs.</li>'
 '<li><b>The bear case:</b> Man Group chief market strategist Kristina Hooper told TheStreet at 2:33 PM ET that a 10&ndash;20% pullback in '
 'U.S. equities is &ldquo;absolutely still coming.&rdquo;</li>'
 '</ul></div>')

ws.append(srcs([
 ("https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-02-2026","TheStreet &mdash; Stock Market Today (Sept. 2, 2026): S&amp;P 500, Dow jump"),
 ("https://www.cnbc.com/2026/09/01/stock-market-today-live-updates.html","CNBC &mdash; Stock market news for Sept. 2, 2026"),
 ("https://www.washingtontimes.com/news/2026/sep/2/wall-street-rising-tech-stocks-climb-oil-prices-bond-yields-hold/","The Washington Times / AP &mdash; Wall Street rises as tech stocks climb and oil prices, bond yields hold"),
 ("https://www.cnbc.com/2026/09/02/dell-has-more-than-tripled-in-2026-two-analysts-say-it-has-more-room-to-run.html","CNBC &mdash; Dell has more than tripled in 2026; two analysts say it has more room to run"),
 ("https://www.cnbc.com/2026/09/01/dell-q2-earnings-report-2027.html","CNBC &mdash; Dell surges after lifting fiscal 2027 forecast on AI server demand"),
 ("https://www.investing.com/news/stock-market-news/dell-shares-gain-after-strong-ai-server-demand-boosts-annual-forecast-4885629","Investing.com / Reuters &mdash; Dell shares gain after strong AI server demand boosts annual forecast"),
 ("https://www.benzinga.com/trading-ideas/movers/26/09/61559817/palo-alto-stock-drops-as-inflation-fears-boost-bond-yields","Benzinga &mdash; Palo Alto stock drops as inflation fears boost bond yields"),
 ("https://tradingeconomics.com/united-states/government-bond-yield","Trading Economics &mdash; US 10-Year Treasury Note Yield [Sept 2 close and session range]"),
 ("https://in.investing.com/news/stock-market-news/afterhours-movers-avgo-snow-hpe-ntap-ntsk-chpt-five-tlys-pvh-rare-432SI-5580445","Investing.com &mdash; After-Hours Movers: AVGO, SNOW, HPE&hellip; [published 4:30 PM ET Sept 2]"),
 ("https://www.investing.com/news/stock-market-news/sp-500-sector-performance-energy-leads-with-42-ytd-gain-in-2026-93CH-4883146","Investing.com &mdash; S&amp;P 500 sector performance: Energy leads with +42% YTD gain [daily figures refused, see note]"),
 ("https://www.investing.com/equities/after-hours","Investing.com &mdash; After Hours Stock Movers board [unstamped; noted, not published as a session move]"),
])+'<div class="disc">For information only. Nothing here is investment advice, a recommendation, or an offer to buy or sell any security. '
 'Intraday figures are labelled with the time their source published them; live widgets are supplied by TradingView and may be delayed.</div></footer>')

open(os.path.join(OUT,'wallstreet-briefing.html'),'w').write(page(
 "The Closing Bell — Daily Briefings",WSCSS,
 mast("The Closing Bell","Your daily Wall Street briefing &mdash; markets, movers &amp; the macro tape","The Tape",WS_TLDR),
 ''.join(ws),"wallstreet-briefing.html"))
print("wallstreet ok")
