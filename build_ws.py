# -*- coding: utf-8 -*-
import io, os
from common import head, masthead, nav, STAMP_JS, FOOT

OUT = os.path.dirname(os.path.abspath(__file__))

PAL = """
:root{
  --bg:#0a0a0b; --panel:#141414; --line:#262626;
  --accent:#caa64a; --accent2:#e8c766;
  --txt:#ece9e3; --muted:#9b9690;
  --up:#22c55e; --down:#ef4444; --warn:#f0b429; --crit:#ef4444;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
.masthead h1,h3.lead,.card h3{font-family:Georgia,'Times New Roman',serif}
.livebar{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 8px 4px;margin-bottom:18px}
.livebar-label{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--up);display:flex;align-items:center;gap:8px;padding:4px 8px 8px}
.livebar-label .dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--up)}
.tickers{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin-bottom:8px}
.ticker{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 10px}
"""

# --- Verified index readings (Trading Economics, Sep/17, read ~3:05 PM ET) ---
# Wednesday 16 Sep settles carried from the standing ledger: S&P 500 7,551.81; Dow 51,461.90.
SP_PREV, SP_CHG = 7551.81, 84.90
DOW_PREV, DOW_CHG = 51461.90, 374.13

SP_LVL = round(SP_PREV + SP_CHG, 2)
DOW_LVL = round(DOW_PREV + DOW_CHG, 2)
SP_PCT = round(SP_CHG / SP_PREV * 100, 2)
DOW_PCT = round(DOW_CHG / DOW_PREV * 100, 2)

MOVERS = [
    ("Generac Holdings (GNRC)", "up", "+21.35%", False,
     "Up <b>30.1% premarket</b> and <b>+21.35% by 10:25 a.m.</b> on a long-term agreement to supply Amazon with "
     "industrial backup generators for its data centres. Initial deliveries are put at <b>$2.4 billion across 2027 "
     "and 2028</b>, with potential payments of up to <b>$8 billion</b>. Each figure carries its own clock; they are "
     "not averaged."),
    ("Goldman Sachs (GS)", "up", "+1.77%", True,
     "A within-session reversal rather than a headline: Goldman was among the Dow&rsquo;s three biggest drags at the "
     "open, <b>&minus;0.80%</b>, and was later quoted at <b>+1.77% at $954.57</b>. Caterpillar led the Dow at the open "
     "at <b>+2.60%</b> and was still <b>+2.32% at $800.89</b> later in the session."),
    ("Moderna (MRNA)", "up", "+9.39%", False,
     "Still rising on the Merck collaboration&rsquo;s positive Phase 3 results for the personalised mRNA cancer "
     "vaccine <b>intismeran autogene (mRNA-4157)</b>."),
    ("Hewlett Packard Enterprise (HPE)", "up", "+7.44%", False,
     "Up on continued investor interest in AI hardware and data-centre infrastructure spending &mdash; part of the "
     "same hardware-assembler bid rather than a broad tech move."),
    ("Fluence Energy (FLNC)", "down", "&minus;16.85%", False,
     "Down <b>22.22% premarket</b> and <b>&minus;16.85% by 10:25 a.m.</b> after the battery storage company cut its "
     "full-year outlook, citing delays at its contract manufacturing facility."),
    ("CoreWeave (CRWV)", "down", "&minus;4.69%", False,
     "Lower after announcing plans to raise <b>$3 billion</b> through a convertible debt offering."),
    ("United Rentals (URI)", "up", "+9.53%", False,
     "A premarket figure only: UBS added the equipment rental company to its high-conviction list of industrial "
     "stocks. No later reading was published by the sources read this run."),
    ("SentinelOne (S)", "down", "&minus;3.49%", False,
     "A premarket figure only, on an analyst downgrade and as investors kept working through the Fed decision."),
]

SCOREBOARD = [
    ("S&amp;P 500", "7,551.81", "Wed 16 Sep close, carried from the standing ledger"),
    ("Dow Jones Industrial Average", "51,461.90", "Wed 16 Sep close, carried from the standing ledger"),
    ("Nasdaq Composite", "not published", "No source read this run states a Wednesday close for the Composite"),
]

RATES = [
    ("Fed funds target", "3.75%&ndash;4.00%", "Raised 25bp on 16 Sep &mdash; unanimous, and the first increase since July 2023"),
    ("2-year Treasury", "4.69%", "&minus;5bp on the day (Trading Economics, Sep/17)"),
    ("5-year Treasury", "4.81%", "&minus;8bp"),
    ("10-year Treasury", "4.95%", "&minus;7bp, easing off the highest level since 2007"),
    ("30-year Treasury", "5.30%", "&minus;7bp"),
    ("WTI crude", "$101.65", "Trading Economics, &minus;0.76%. TheStreet had $100.70, &minus;1.70% at 7:07 a.m. "
                             "The TE change column renders without a sign; the magnitude matches the percentage and "
                             "the direction is corroborated by TheStreet and Reuters"),
    ("Brent crude", "$104.20", "Trading Economics, &minus;1.55%. TheStreet had $103.60, &minus;2.07% at 7:07 a.m."),
    ("Gold", "$4,360.78 spot", "+2.28% (Trading Economics). TheStreet quoted <i>futures</i> at $4,404.30, +0.38%, "
                               "at 8:56 a.m. &mdash; two different instruments, printed separately"),
    ("Silver", "$65.72 spot", "+3.91% (Trading Economics); TheStreet quoted futures at $65.82, +1.40%"),
    ("VIX", "not published", "Trading Economics rendered 15.56 with a change of &minus;2.15 and a percentage of "
                             "&minus;2.15% &mdash; a point change and a percentage that cannot both describe the "
                             "same number. Refused for a second consecutive edition"),
]

RADAR = [
    "<b>The Fed is not done.</b> The 25bp move to 3.75&ndash;4.00% was unanimous, and the new projections show "
    "<b>16 of 18 officials expecting at least one further hike this year</b> (Daniela Hathorn, Capital.com). "
    "Chair Kevin Warsh: &ldquo;the plain fact is that inflation is too high and has been for too long.&rdquo; "
    "President Trump has said he wants rates at 1% &ldquo;or less.&rdquo;",
    "<b>The SEC opened a path for tokenized U.S. stocks</b> on Thursday morning, effective immediately. The "
    "five-year &ldquo;Innovation Exemption&rdquo; is <b>not a formal rulemaking</b>; two conditions are contested "
    "&mdash; token holders must retain the same rights as equity holders, and companies must be able to object to "
    "tokenization. It lands two days after the Clarity Act failed to advance in the Senate.",
    "<b>Oil&rsquo;s fall has a supply story behind it.</b> Saudi Arabia is offering additional cargoes to Asian "
    "refiners through ship-to-ship transfers off Oman&rsquo;s Sohar port, and Energy Secretary Chris Wright signalled "
    "a quicker return to service for the East-West pipeline. Prices remain above $100.",
    "<b>The war backdrop.</b> Trump said the U.S. is &ldquo;hopefully&rdquo; nearing the end of its nearly "
    "seven-month war with Iran and that he has spoken with Tehran &ldquo;directly.&rdquo; TheStreet Pro&rsquo;s James "
    "DePorre cautions that a rate rise does not fix a supply-side energy shock.",
    "<b>SpaceX (SPCX)</b> was up 1.84% at $153.65 premarket after Cathie Wood argued Starship could generate "
    "$10 trillion in annual revenue by 2030; Trading Economics later quoted the stock at $154.93, +2.68%. The next "
    "Starship test flight is set for <b>22 September</b>, expected to deploy Starlink V3 satellites.",
]

SOURCES = [
    ("TheStreet &mdash; Stock Market Today, 17 September 2026 (live blog)",
     "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-17-2026"),
    ("Trading Economics &mdash; United States Stock Market Index",
     "https://tradingeconomics.com/united-states/stock-market"),
    ("Trading Economics &mdash; US Government Bond Yields",
     "https://tradingeconomics.com/united-states/government-bond-yield"),
    ("CNBC &mdash; SEC clears path for tokenized stocks",
     "https://www.cnbc.com/2026/09/17/sec-clears-path-for-tokenized-stocks-bringing-24/7-trading-closer.html"),
    ("CNBC &mdash; 10-year Treasury yield after the Fed hike",
     "https://www.cnbc.com/2026/09/16/treasury-yield-bond-market-fed-decision.html"),
    ("Reuters &mdash; Oil prices extend losses as Middle East supply disruption fears ease",
     "https://www.reuters.com/business/energy/oil-prices-extend-losses-fears-middle-east-supply-disruptions-ease-2026-09-17/"),
    ("CNBC &mdash; Trump says U.S. nearing end of Iran war",
     "https://www.cnbc.com/2026/09/17/us-iran-war-trump-hormuz.html"),
    ("TheStreet &mdash; Stock Market Today, 16 September 2026 (Wednesday close)",
     "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-16-2026"),
]


def widget(src, cfg):
    return ('<script src="https://s3.tradingview.com/external-embedding/embed-widget-%s.js" async>%s</script>'
            % (src, cfg))


def build():
    o = io.StringIO()
    o.write(head("The Closing Bell &mdash; Daily Markets Briefing", PAL))
    o.write(masthead("The Closing Bell",
                     "Your daily markets briefing &mdash; the tape, the drivers and what is next"))
    o.write('<div class="tldr"><b>The Tape</b> <span>Stocks rebounded broadly on Thursday &mdash; the S&amp;P 500 '
            'up 1.12% and the Dow up 0.73% on the latest read &mdash; as Treasury yields and oil both eased a day '
            'after the Federal Reserve&rsquo;s first rate rise since 2023.</span></div>\n')
    o.write('<div class="freshline" id="freshline">&nbsp;</div>\n')
    o.write(nav("ws"))

    # BLOCK A
    o.write('<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>')
    o.write(widget("ticker-tape",
                   '{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},'
                   '{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},'
                   '{"proName":"FOREXCOM:DJI","title":"Dow 30"},'
                   '{"proName":"NYSE:GNRC","title":"Generac"},'
                   '{"proName":"NASDAQ:MRNA","title":"Moderna"},'
                   '{"proName":"NYSE:HPE","title":"HPE"},'
                   '{"proName":"NASDAQ:FLNC","title":"Fluence"},'
                   '{"proName":"NYSE:GS","title":"Goldman Sachs"},'
                   '{"proName":"TVC:USOIL","title":"WTI Crude"},'
                   '{"proName":"TVC:US10Y","title":"US 10Y"}],'
                   '"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,'
                   '"displayMode":"adaptive","locale":"en"}'))
    o.write("</div>\n")

    # BLOCK B
    o.write('<h2 class="sec">Live Index Quotes &mdash; updates in real time</h2>\n<div class="tickers">')
    for sym in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI"):
        o.write('<div class="ticker">%s</div>' % widget(
            "single-quote",
            '{"symbol":"%s","width":"100%%","colorTheme":"dark","isTransparent":true,"locale":"en"}' % sym))
    o.write("</div>\n")
    o.write('<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the latest '
            'edition; official closes are in the Weekly Scorecard.</div>\n')

    # Lead
    o.write('<h2 class="sec">The Lead</h2>\n')
    o.write('<div class="panel">'
            '<h3 class="lead" style="margin:0 0 10px;font-size:22px">Stocks rebound as yields and oil ease &mdash; '
            'as of roughly 3:05 p.m. ET</h3>'
            '<p style="margin:0 0 10px">The market took back most of Wednesday&rsquo;s post-decision slide. On the '
            'latest Trading Economics read, the <b>S&amp;P 500 is up %.2f%%</b> (+%.2f to <b>%s</b>), the '
            '<b>Dow up %.2f%%</b> (+%.2f to <b>%s</b>), the <b>Nasdaq 100 up 1.67%%</b> (+482.91 to 29,427.97), the '
            '<b>Russell 2000 up 1.04%%</b> and the <b>S&amp;P MidCap 400 up 0.88%%</b>. Every one of those rows '
            'reconciles: the level, the point change and the percentage agree with Wednesday&rsquo;s settle, which is '
            'the stated reason they are carried. <b>No Nasdaq Composite percentage is published</b> &mdash; every '
            'figure circulating for it this run was an ETF proxy.</p>'
            '<p style="margin:0 0 10px">Breadth was positive but not overwhelming: TheStreet counted <b>259 of the '
            'index&rsquo;s 503 holdings advancing</b> at 10:54 a.m., with strength &ldquo;anchored in cyclicals and '
            'tech.&rdquo; The Dow had opened <b>+0.48%%, or 248 points</b>. Behind the bid: the 10-year Treasury yield '
            'eased to <b>4.95%%</b> off the highest level since 2007, and crude fell for a second day as Saudi '
            'ship-to-ship cargoes off Oman eased supply fears.</p>'
            '<p style="margin:0" class="mut"><b>Refused this run.</b> Three readings are on the page as refusals '
            'rather than facts. (1) TheStreet&rsquo;s own 9:32 a.m. opening-bell paragraph reads that &ldquo;the Dow '
            'Jones Industrial Average gained 8.81%%&rdquo; alongside an S&amp;P up 1.19%% and a Nasdaq down 0.01%% '
            '&mdash; internally impossible, so not one figure from it is used. (2) An earlier-session snapshot of '
            '<b>7,596, +0.59%%</b> for the S&amp;P is still circulating; it is internally consistent but describes an '
            'earlier hour and is superseded by the +1.12%% read. (3) The VIX row does not reconcile and is dropped '
            'from the rates table. A caveat on freshness: the Trading Economics table returned the same values at '
            '3:05 p.m. as it did at 2:50 p.m., so the feed may not have refreshed in between.</p>'
            "</div>\n" % (SP_PCT, SP_CHG, "{:,.2f}".format(SP_LVL), DOW_PCT, DOW_CHG, "{:,.2f}".format(DOW_LVL)))

    # Movers
    o.write('<h2 class="sec">Movers &amp; Drivers</h2>\n<div class="cards">')
    for name, d, pct, is_new, body in MOVERS:
        tags = '<span class="t new">New</span>' if is_new else ""
        tags += '<span class="t %s">%s</span>' % ("pro" if d == "up" else "hot", pct)
        o.write('<div class="card"><div class="tags">%s</div><h3>%s</h3><p>%s</p></div>' % (tags, name, body))
    o.write("</div>\n")
    o.write('<p class="note">Percentages carry the clock of the source that printed them &mdash; premarket, 10:25 a.m. '
            'or later &mdash; and are labelled rather than blended. Super Micro and QQQ are omitted entirely: one '
            'aggregator page quoted each of them several different ways within a single article.</p>\n')

    # BLOCK E
    o.write('<h2 class="sec">Chart of the Day &mdash; Generac (GNRC)</h2>\n<div class="panel" style="padding:8px">')
    o.write(widget("mini-symbol-overview",
                   '{"symbol":"NYSE:GNRC","width":"100%","height":240,"locale":"en","dateRange":"1D",'
                   '"colorTheme":"dark","isTransparent":true,"autosize":false}'))
    o.write("</div>\n")

    # BLOCK D
    o.write('<h2 class="sec">Sector Heat &mdash; live</h2>\n<div class="panel" style="padding:8px">')
    o.write(widget("stock-heatmap",
                   '{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector",'
                   '"locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,'
                   '"isZoomEnabled":true,"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}'))
    o.write("</div>\n")
    o.write('<p class="note">One sourced editorial line: at the open, the Dow&rsquo;s top gainers were Caterpillar '
            '(+2.60%), Nvidia (+2.09%) and Amazon (+2.02%), with the biggest drags Salesforce (&minus;4.30%), Goldman '
            'Sachs (&minus;0.80%) and Walmart (&minus;0.47%). Goldman had flipped to +1.77% by the later read, which '
            'is why the open is labelled as the open.</p>\n')

    # BLOCK F
    o.write('<h2 class="sec">The Calendar &mdash; live</h2>\n<div class="panel" style="padding:8px">')
    o.write(widget("events",
                   '{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en",'
                   '"importanceFilter":"0,1","countryFilter":"us"}'))
    o.write("</div>\n")

    # BLOCK C
    o.write('<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2>\n'
            '<div class="panel" style="padding:8px">')
    o.write(widget("timeline",
                   '{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,'
                   '"displayMode":"regular","width":"100%","height":420,"locale":"en"}'))
    o.write("</div>\n")

    # Scorecard
    o.write('<h2 class="sec">Weekly Scorecard &mdash; official closes</h2>\n'
            '<div class="panel" style="padding:6px 10px"><table>'
            "<tr><th>Index</th><th>Last official close</th><th>Note</th></tr>")
    for a, b, c in SCOREBOARD:
        o.write("<tr><td><b>%s</b></td><td>%s</td><td class=\"mut\">%s</td></tr>" % (a, b, c))
    o.write("</table></div>\n")
    o.write('<p class="note">Levels appear here only when the level, the point change and the percentage agree and are '
            'corroborated. Thursday is still trading at publication, so no Thursday close is shown.</p>\n')

    # Rates
    o.write('<h2 class="sec">Rates, Bonds &amp; Commodities</h2>\n<div class="panel" style="padding:6px 10px"><table>'
            "<tr><th>Instrument</th><th>Level</th><th>Note</th></tr>")
    for a, b, c in RATES:
        o.write("<tr><td><b>%s</b></td><td>%s</td><td class=\"mut\">%s</td></tr>" % (a, b, c))
    o.write("</table></div>\n")

    # Radar
    o.write('<h2 class="sec">On the Radar</h2>\n<div class="panel"><ul class="bul">')
    for r in RADAR:
        o.write("<li>%s</li>" % r)
    o.write("</ul></div>\n")

    # Sources
    o.write('<h2 class="sec">Sources</h2>\n<div class="panel srcs">')
    o.write("<br>".join('<a href="%s">%s</a>' % (u, t) for t, u in SOURCES))
    o.write("</div>\n")

    o.write('<p class="disc">The Closing Bell is for information only and is not investment advice. Figures are taken '
            'from public reporting at the time of publication and are stated with the hour they describe; intraday '
            'levels move. Live widgets are supplied by TradingView and some feeds are delayed by about 15 minutes.</p>\n')

    o.write(FOOT % STAMP_JS)
    return o.getvalue()


if __name__ == "__main__":
    html = build()
    with open(os.path.join(OUT, "wallstreet-briefing.html"), "w") as f:
        f.write(html)
    print("ws ok", len(html), SP_LVL, SP_PCT, DOW_LVL, DOW_PCT)
