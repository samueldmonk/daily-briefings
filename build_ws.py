# -*- coding: utf-8 -*-
import css as C

ACCENT, ACCENT2 = "#caa64a", "#e8c766"
CSS = C.base_css(ACCENT, ACCENT2, "#0d0c0a", "#171512", "#2b2721") + """
.masthead h1{font-family:Georgia,'Times New Roman',serif;color:var(--accent2)}
h3,h2.lead{font-family:Georgia,'Times New Roman',serif}
.livebar{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 8px 4px;margin-bottom:18px}
.livebar-label{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--up);
  display:flex;align-items:center;gap:8px;padding:4px 8px 8px}
.livebar-label .dot{width:7px;height:7px;border-radius:50%;background:var(--up);display:inline-block}
.tickers{display:grid;gap:11px;grid-template-columns:1fr}
@media(min-width:700px){.tickers{grid-template-columns:repeat(3,1fr)}}
.ticker{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 10px}
"""

TLDR = ("Wall Street snapped a three-day losing streak on Wednesday, with the S&amp;P 500 closing up "
        "0.46%, the Dow up 295.07 points and the Nasdaq Composite up 0.45% — then Snowflake jumped "
        "and Broadcom fell after the bell.")

SOURCES = [
    ("TheStreet — Stock Market Today (Sept. 2, 2026) live blog [fetched this run; last modified 2:33 PM ET]",
     "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-02-2026"),
    ("CNBC — Stock market news for Sept. 2, 2026",
     "https://www.cnbc.com/2026/09/01/stock-market-today-live-updates.html"),
    ("Investing.com — After-Hours Movers: AVGO, SNOW, HPE, NTAP… [published 4:30 PM ET Sept 2]",
     "https://in.investing.com/news/stock-market-news/afterhours-movers-avgo-snow-hpe-ntap-ntsk-chpt-five-tlys-pvh-rare-432SI-5580445"),
    ("Yahoo Finance — Stock Market Today (Sept. 2, 2026): Dow edges higher as oil prices…",
     "https://finance.yahoo.com/markets/stocks/articles/stock-market-today-sept-2-134032621.html"),
    ("Yahoo Finance — 10-year Treasury touches highest level since 2023 as oil prices stay elevated",
     "https://finance.yahoo.com/markets/article/10-year-treasury-touches-highest-level-since-2023-as-oil-prices-stay-elevated-134238599.html"),
    ("Benzinga — Why Is Credo Technology Stock Sinking",
     "https://www.benzinga.com/trading-ideas/movers/26/09/61568461/why-is-credo-technology-stock-sinking-tuesday-2"),
    ("Morningstar — Top Stock Market Gainers, Losers and Most Active",
     "https://www.morningstar.com/markets/movers"),
    ("Investing.com — S&amp;P 500 sector performance: Energy leads with +42% YTD gain in 2026 [figures refused, see note]",
     "https://www.investing.com/news/stock-market-news/sp-500-sector-performance-energy-leads-with-42-ytd-gain-in-2026-93CH-4883146"),
    ("Investing.com — Broadcom, Hewlett Packard Enterprise, Snowflake and more set to report Wednesday",
     "https://www.investing.com/news/stock-market-news/broadcom-hewlett-packard-enterprise-snowflake-and-more-set-to-report-wednesday-93CH-4884463"),
    ("CNBC — WTI Crude (Oct'26) quote",
     "https://www.cnbc.com/quotes/@CL.1"),
]

TICKER = ('<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>'
          '{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},'
          '{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},'
          '{"proName":"FOREXCOM:DJI","title":"Dow 30"},'
          '{"proName":"NASDAQ:CRDO","title":"Credo"},'
          '{"proName":"NYSE:SNOW","title":"Snowflake"},'
          '{"proName":"NASDAQ:AVGO","title":"Broadcom"},'
          '{"proName":"NYSE:DELL","title":"Dell"},'
          '{"proName":"NASDAQ:MDB","title":"MongoDB"},'
          '{"proName":"TVC:USOIL","title":"WTI Crude"},'
          '{"proName":"TVC:US10Y","title":"US 10Y"}],'
          '"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,'
          '"displayMode":"adaptive","locale":"en"}</script>')


def quote(sym):
    return ('<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/'
            'embed-widget-single-quote.js" async>{"symbol":"%s","width":"100%%",'
            '"colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>' % sym)


MOVERS = [
    ("Credo Technology (CRDO)", "down", "−20.69% to $163.87",
     "Record fiscal Q1 revenue of $479M, up 114.7% year over year, beat both internal and Wall Street "
     "estimates — but shrinking margins and rising R&amp;D expense drove the selling. The close "
     "reconciles to the cent against the sourced prior close of $206.63.", "new"),
    ("MongoDB (MDB)", "down", "−13.84% to $374.64",
     "Beat second-quarter earnings expectations but issued cautious guidance; the stock was already "
     "down 12.4% in the premarket at 8:15 AM ET.", ""),
    ("Palo Alto Networks (PANW)", "down", "−10.82% to $323.08",
     "Investors focused on slowing growth metrics, margin pressure and elevated expectations rather "
     "than the headline earnings beat. TheStreet had it −7.8% at 10:36 AM ET.", ""),
    ("Dell Technologies (DELL)", "up", "+4.7% at 10:36 AM ET",
     "Beat Wall Street expectations for fiscal Q2 2027 on what the company described as massive demand "
     "for AI servers. Dell was quoted +8.1% in the 8:15 AM premarket; no closing figure was sourced "
     "this run, so the timestamped intraday move is what is printed.", ""),
    ("Reddit (RDDT)", "up", "+7% at 10:36 AM ET",
     "Bullish analyst coverage, an upcoming wave of AI data-licensing renewals and underlying "
     "fundamental growth.", ""),
    ("PG&amp;E (PCG)", "down", "−9.7% at 10:36 AM ET",
     "The utility slashed its capital spending plans and addressed continuing uncertainty around "
     "California's wildfire liability framework. Edison International (EIX) fell 7.6% the same hour as "
     "lawmakers advanced Senate Bill 492 without wildfire liability protections.", ""),
]

AFTER_HOURS = [
    ("Snowflake (SNOW)", "up", "+21%",
     "Q2 EPS of $0.62 beat the $0.45 estimate on revenue of $1.55 billion, with Q3 revenue guided to "
     "$1.588–$1.593 billion. Snowflake had been quoted 2.5% lower in the 8:15 AM premarket ahead of "
     "the report; no regular-session closing figure for SNOW was sourced this run and none is printed.",
     "new"),
    ("Broadcom (AVGO)", "down", "−3.5%",
     "Q3 EPS of $3.32 cleared the $3.21 estimate on $29.59 billion of revenue, but Q4 revenue guidance "
     "of $34.8 billion came in under the $35.05 billion consensus. Two other summaries put the "
     "after-hours move at about −6.5% and at −4.14% in extended trading; the −3.5% figure is "
     "the one carrying a publication time (4:30 PM ET) and the disagreement is printed rather than "
     "reconciled.", "new"),
    ("Hewlett Packard Enterprise (HPE)", "down", "−1%",
     "A clean beat-and-raise — Q3 EPS $1.11 against $0.92 expected on $12.2 billion of revenue, "
     "full-year FY26 EPS guidance lifted to $3.75–$3.85 and Q4 revenue guided to "
     "$13.9–$14.8 billion — but profit-taking took hold. HPE had risen 3.8% in the premarket.", "new"),
]

SCORECARD = [
    ("S&amp;P 500", "7,666.60", "+35.13", "+0.46%", "up"),
    ("Nasdaq Composite", "26,217.83", "+118.06", "+0.45%", "up"),
    ("Dow Jones Industrial Average", "53,061.95", "+295.07", "+0.56%", "up"),
]

RATES = [
    ("10-year Treasury", "4.77%", "Eased to 4.77% after touching a higher level intraday. The intraday "
     "high itself carries two irreconcilable descriptors and is deliberately held out of this table — "
     "see the note below."),
    ("2-year Treasury", "4.369%", "Tuesday's settlement, reported as the highest in 19 months. Carried "
     "from a prior fetch; not re-sourced this run."),
    ("30-year Treasury", "5.27%", "Tuesday. Carried from a prior fetch; not re-sourced this run."),
    ("Fed funds target", "—", "Not sourced this run; no figure published."),
    ("WTI crude", "$90.76", "Settled up 0.60%, a third consecutive advancing session. It had been "
     "$89.58 (−0.71%) at 9:24 AM ET after touching a one-month high overnight."),
    ("Brent crude", "$94.28", "−0.39% as of 9:24 AM ET — an intraday quote, not a settlement."),
    ("Gold", "$4,355", "−0.94% in early trading (7:09 AM ET). Silver $64.26, −1.69% (7:13 AM ET)."),
    ("Bitcoin", "$76,763.96", "−1.43% at 11:04 AM ET."),
]

RADAR = [
    "<b>Thursday, Sept 3:</b> ISM Services; earnings from Ciena (CIEN) and Lululemon (LULU).",
    "<b>Friday, Sept 4:</b> August nonfarm payrolls, consensus 45,000. ADP's private-payroll print for "
    "August came in at +38,000 against a +47,000 estimate, with July revised up to +46,000 — the "
    "slowest month since January. Education and health services added 45,000; manufacturing shed 17,000 "
    "and professional and business services 16,000.",
    "<b>Monday, Sept 7:</b> Labor Day — U.S. markets closed.",
    "<b>FOMC:</b> September 15–16. CME FedWatch put the odds of a hike at 66.1% as of Monday, up from "
    "35.4% before Chair Kevin Warsh's remarks.",
    "<b>Trade:</b> Commerce Secretary Howard Lutnick told CNBC a semiconductor tariff framework is being "
    "developed — \"if you build here, you don't pay\" — with no rate or date made public.",
    "<b>Geopolitics:</b> Iran's Revolutionary Guards said two oil tankers struck naval mines attempting to "
    "transit the Strait of Hormuz; Iran targeted Jordan, the UAE and Kuwait overnight in retaliation for "
    "U.S. airstrikes. Oil has now advanced for three straight sessions.",
    "<b>The bear case:</b> Man Group chief market strategist Kristina Hooper told TheStreet at 2:33 PM ET "
    "that a 10–20% pullback in U.S. equities is \"absolutely still coming.\"",
]


def card(name, direction, move, body, tag):
    t = '<span class="tag new">New</span>' if tag == "new" else ""
    return ('<div class="card"><div class="k">%s</div>'
            '<h4><span class="%s">%s</span></h4>%s<p>%s</p></div>'
            % (name, direction, move, t, body))


def build():
    p = []
    p.append(C.head("The Closing Bell — Daily Briefings", CSS))
    p.append('<div class="masthead"><h1>The Closing Bell</h1>'
             '<p class="tag">Your daily Wall Street briefing — markets, movers &amp; the macro tape</p>'
             + C.meta_row() + "</div>")
    p.append('<div class="tldr"><b>The Tape</b> <span>%s</span></div>' % TLDR)
    p.append('<div class="freshline" id="freshline">&nbsp;</div>')
    p.append(C.nav("ws"))

    # BLOCK A
    p.append('<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>'
             + TICKER + "</div>")

    # BLOCK B
    p.append('<h2 class="sec">Live Index Quotes — updates in real time</h2>')
    p.append('<div class="tickers">%s%s%s</div>' % (quote("FOREXCOM:SPXUSD"), quote("FOREXCOM:NSXUSD"),
                                                    quote("FOREXCOM:DJI")))
    p.append('<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects '
             'the latest edition; official closes are in the Weekly Scorecard.</div>')

    # LEAD
    p.append('<h2 class="sec">The Lead</h2>')
    p.append('<div class="panel"><h3>Stocks snap a three-day skid at the close, and the after-hours tape '
             'splits on AI earnings</h3>'
             '<p>All three major U.S. indexes finished Wednesday, September 2 higher, ending a three-session '
             'losing streak. The <b>S&amp;P 500 rose 0.46%</b>, the <b>Dow Jones Industrial Average added '
             '295.07 points, or 0.56%</b>, and the <b>Nasdaq Composite gained 0.45%</b>. Breadth was wide: '
             'TheStreet counted closer to two-thirds of the market advancing at 1:15 PM ET, and had only 33% '
             'of U.S. issues declining at 12:41 PM.</p>'
             '<p>The recovery came despite the pressures that drove the previous three days down. The 10-year '
             'Treasury yield <b>eased to 4.77% after hitting 4.814%</b> intraday — how far back that high '
             'reaches is disputed between sources, and the dispute is set out in the rates section rather '
             'than settled here — and oil advanced for a third straight session as the U.S. and Iran '
             'traded fresh strikes. ADP\'s August private-payroll count came in soft at +38,000 against a '
             '+47,000 estimate, the slowest month since January.</p>'
             '<p>The day\'s real drama landed after the bell, where three large technology reports pulled in '
             'opposite directions: <b>Snowflake jumped about 21%</b> on a beat-and-raise, while '
             '<b>Broadcom fell</b> on soft fourth-quarter revenue guidance despite clearing third-quarter '
             'estimates.</p>'
             '<div class="note"><b>How this edition was built.</b> Research for this run was fetched between '
             '4:52 and 5:05 PM ET; the closing figures above are official closes, and each reconciles '
             'arithmetically against Tuesday\'s verified closes (S&amp;P 7,631.47; Dow 52,766.88; Nasdaq '
             '26,099.77). TheStreet\'s live blog was re-fetched this run and its last-modified stamp is '
             '2:33 PM ET — it carries no closing entry, so every figure taken from it is labelled with '
             'the time it was published. Where the widgets above and this editorial disagree, the widgets '
             'are right.</div></div>')

    # MOVERS
    p.append('<h2 class="sec">Movers &amp; Drivers</h2>')
    p.append('<div class="cards two">' + "".join(card(*m) for m in MOVERS) + "</div>")
    p.append('<div class="note">Also sourced at the close: AST SpaceMobile (ASTS) +10.93% to $61.89 and '
             'Eos Energy (EOSE) +20.10% to $3.65 among gainers. Uber (UBER) rose 0.58% to $75.68 at '
             '10:15 AM ET after announcing it will cut about 10% of its workforce, limiting fully remote '
             'staff to roughly 1% of headcount; Uber had around 34,000 employees at the end of 2025. '
             'GitLab (GTLB) was quoted +21% in the 8:15 AM premarket on strong second-quarter results, but '
             'no regular-session GitLab figure was sourced this run and none is printed as a close.</div>')

    # CHART OF THE DAY
    p.append('<h2 class="sec">Chart of the Day — Credo Technology (CRDO)</h2>')
    p.append('<div class="panel" style="padding:8px">'
             '<script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" '
             'async>{"symbol":"NASDAQ:CRDO","width":"100%","height":240,"locale":"en","dateRange":"1D",'
             '"colorTheme":"dark","isTransparent":true,"autosize":false}</script></div>')
    p.append('<div class="note"><b>Why this slot.</b> Credo\'s −20.69% close to $163.87 is the largest '
             'single-name regular-session move sourced this run, and unlike earlier editions it now comes '
             'with a catalyst: record fiscal Q1 revenue of $479 million, up 114.7% year over year and ahead '
             'of estimates, undone by shrinking margins and rising R&amp;D spend. One source gives the decline '
             'as −19.71% and another had the stock down 18% at midday; the −20.69%/$163.87 pair is '
             'the one that reconciles to the cent against the separately sourced prior close of $206.63, so it '
             'is what is printed. Snowflake\'s +21% is larger but is an after-hours move and appears in that '
             'section instead.</div>')

    # SECTOR HEAT
    p.append('<h2 class="sec">Sector Heat — live</h2>')
    p.append('<div class="panel" style="padding:8px">'
             '<script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>'
             '{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector",'
             '"locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,'
             '"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}</script></div>')
    p.append('<div class="note"><b>The sector table is refused for a sixth consecutive run, on the same '
             'ground and one new one.</b> The only sector-bearing source this run reports Tuesday\'s closes '
             '(Dow 52,766.88, −419.02; S&amp;P 7,631.47, −0.71%) as though they were Wednesday\'s, and '
             'dates its "energy leads, +1.3%" line to September 1 — a source that mis-dates the index closes '
             'it leads with does not supply the sector table. Its energy year-to-date figure also still reads '
             '+42% in the headline and +43% in the body. The one sourced sector statement from Wednesday '
             'itself is TheStreet\'s 12:05 PM ET note that S&amp;P advances came "from virtually every sector '
             'but tech, real estate, and utilities." The live heatmap above is the sector read.</div>')

    # CALENDAR
    p.append('<h2 class="sec">The Calendar — live</h2>')
    p.append('<div class="panel" style="padding:8px">'
             '<script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>'
             '{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en",'
             '"importanceFilter":"0,1","countryFilter":"us"}</script></div>')

    # HEADLINES
    p.append('<h2 class="sec">Live Market Headlines — updates in real time</h2>')
    p.append('<div class="panel" style="padding:8px">'
             '<script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>'
             '{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,'
             '"displayMode":"regular","width":"100%","height":420,"locale":"en"}</script></div>')

    # AFTER HOURS
    p.append('<h2 class="sec">After-Hours Movers</h2>')
    p.append('<div class="cards two">' + "".join(card(*m) for m in AFTER_HOURS) + "</div>")
    p.append('<div class="note">Figures above are from an after-hours movers report published at 4:30 PM ET, '
             'roughly half an hour after the close; extended-hours prices move continuously and these are a '
             'snapshot, not settlements.</div>')

    # SCORECARD
    p.append('<h2 class="sec">Weekly Scorecard — official closes, Wednesday Sept 2</h2>')
    rows = "".join('<tr><td>%s</td><td>%s</td><td class="%s">%s</td><td class="%s">%s</td></tr>'
                   % (n, lvl, d, chg, d, pct) for n, lvl, chg, pct, d in SCORECARD)
    p.append('<div class="tblwrap"><table><tr><th>Index</th><th>Close</th><th>Change</th><th>%</th></tr>'
             + rows + "</table></div>")
    p.append('<div class="note">Levels are published because all three reconcile: adding each index\'s '
             'point change to Tuesday\'s verified close reproduces Wednesday\'s level exactly '
             '(7,631.47 + 35.13 = 7,666.60; 52,766.88 + 295.07 = 53,061.95; 26,099.77 + 118.06 = 26,217.83), '
             'and each percentage checks against those levels. The S&amp;P and Nasdaq point changes are '
             'derived from that reconciliation rather than quoted directly.</div>')

    # RATES
    p.append('<h2 class="sec">Rates, Bonds &amp; Commodities</h2>')
    rows = "".join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % r for r in RATES)
    p.append('<div class="tblwrap"><table><tr><th>Instrument</th><th>Level</th><th>Note</th></tr>'
             + rows + "</table></div>")
    p.append('<div class="note"><b>An unreconciled yield descriptor, printed rather than resolved.</b> '
             'TheStreet, citing CNBC, has the 10-year hitting 4.814% on the day, "its highest level since '
             'November 2023." Yahoo and the WSJ excerpt it quotes describe Tuesday\'s 4.79%/4.798% as the '
             'highest since January 2025. Two descriptors for one yield; both are printed, neither is '
             'adopted, and 4.814% is deliberately kept out of the table cells above because its session '
             'framing is ambiguous. Also sourced but not tabled: the 10-year\'s 50-day moving average at '
             '4.32%; Japan\'s 10-year JGB near a multi-decade high; U.K., German and French yields also rose.</div>')

    # RADAR
    p.append('<h2 class="sec">On the Radar</h2>')
    p.append('<div class="panel"><ul class="b">' + "".join("<li>%s</li>" % r for r in RADAR) + "</ul></div>")

    p.append(C.sources(SOURCES))
    p.append('<div class="disc">For information only. Nothing here is investment advice, a recommendation, '
             'or an offer to buy or sell any security. Intraday figures are labelled with the time their '
             'source published them; live widgets are supplied by TradingView and may be delayed.</div>'
             "</footer>")
    p.append(C.STAMP_JS)
    p.append("</div></body></html>")
    return "".join(p)


if __name__ == "__main__":
    open("wallstreet-briefing.html", "w").write(build())
    print("wallstreet ok")
