# -*- coding: utf-8 -*-
import io, common_r4 as C

OUT = "/sessions/youthful-bold-tesla/mnt/outputs/wallstreet-briefing.html"

TLDR = ("Wall Street opened the week higher on retreating oil and the rally widened through "
        "mid-morning &mdash; Warner Bros. Discovery, Intel and AMD were each up more than 9% "
        "as of 10:28&nbsp;AM ET, with no later index print published.")

TICKER = ('<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>'
 '<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>'
 '{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},'
 '{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NASDAQ:WBD","title":"Warner Bros. Discovery"},'
 '{"proName":"NASDAQ:INTC","title":"Intel"},{"proName":"NASDAQ:AMD","title":"AMD"},'
 '{"proName":"NASDAQ:PSKY","title":"Paramount Skydance"},{"proName":"NYSE:NVO","title":"Novo Nordisk"},'
 '{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],'
 '"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script></div>')

def quote(sym):
    return ('<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>'
            '{"symbol":"%s","width":"100%%","colorTheme":"dark","isTransparent":true,"locale":"en"}</script></div>' % sym)

QUOTES = ('<div class="tickers">' + quote("FOREXCOM:SPXUSD") + quote("FOREXCOM:NSXUSD") + quote("FOREXCOM:DJI") +
 '</div><div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the latest '
 'edition; official closes are in the Weekly Scorecard.</div>')

TIMELINE = ('<div class="panel" style="padding:8px">'
 '<script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>'
 '{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,"displayMode":"regular",'
 '"width":"100%","height":420,"locale":"en"}</script></div>')

HEATMAP = ('<div class="panel" style="padding:8px">'
 '<script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>'
 '{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en",'
 '"colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,'
 '"isMonoSize":false,"width":"100%","height":420}</script></div>')

MINI = ('<div class="panel" style="padding:8px">'
 '<script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>'
 '{"symbol":"NASDAQ:WBD","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark",'
 '"isTransparent":true,"autosize":false}</script></div>')

EVENTS = ('<div class="panel" style="padding:8px">'
 '<script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>'
 '{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en",'
 '"importanceFilter":"0,1","countryFilter":"us"}</script></div>')

LEAD = ('<div class="lead"><h3>Stocks start the week higher as oil retreats and diplomacy dominates the '
 'calendar &mdash; index figures as of the 9:31&nbsp;AM ET open</h3>'
 '<p>The U.S. market opened Monday with the <b class="up">Dow Jones Industrial Average up 0.61%</b>, the '
 '<b class="up">S&amp;P 500 up 0.67%</b> and the <b class="up">Nasdaq up 0.77%</b>, while the '
 '<b class="down">Russell 2000 slipped 0.50%</b> &mdash; TheStreet&rsquo;s opening-bell entry, timestamped '
 '9:31&nbsp;AM ET. <b>No index reading later than that open appeared in anything read this run.</b> '
 'TheStreet&rsquo;s live blog was last updated at <b>10:28&nbsp;AM ET</b>, and that update carried a '
 'market-movers block rather than a fresh index print. The page says so rather than implying the open is live.</p>'
 '<p>The driver is oil. Crude fell as diplomatic efforts around the U.S.&ndash;Iran conflict gathered pace and '
 'Saudi supply recovered, easing the inflation anxiety that has dogged the month. &ldquo;Markets are starting the '
 'week on a more constructive footing, with falling oil prices helping revive risk appetite after several weeks '
 'dominated by inflation and interest-rate concerns,&rdquo; said <b>Daniela Hathorn</b>, senior market analyst at '
 'Capital.com, who called oil &ldquo;the biggest source of relief.&rdquo;</p>'
 '<p>Sourced this run and attributed: the <b>PHLX Semiconductor Index rose more than 2%</b> to its highest price '
 'since <b>9 September</b>; <b>QQQ</b>, tracking the Nasdaq-100, was the morning&rsquo;s standout at <b>+1.5%</b>; '
 'the advance <b>erased the S&amp;P 500&rsquo;s decline for the month</b> (no monthly percentage was stated, so none '
 'is printed); <b>Treasury 10-year yields fell below 5%</b> (no level stated, so the H.15 17-September row below '
 'stands); and <b>Brent extended its drop into a fourth straight session</b>, which would be its longest losing '
 'streak since June. On sectors, the account read this run says <b>most sectors were in the green, led by technology '
 'and financial stocks, while oil and gas shares retreated</b>.</p>'
 '<p class="mut" style="font-size:14px">Two further readings of the same morning, printed rather than smoothed. '
 'Yahoo Finance&rsquo;s quote strip, captured with the page still reading &ldquo;U.S. markets open in 25m&rdquo; '
 '(so roughly 9:05&nbsp;AM ET): S&amp;P futures <b>7,761.75, +0.64%</b>; Dow futures <b>52,484.00, +0.78%</b>; '
 'Nasdaq futures <b>30,230.75, +1.05%</b>; Russell 2000 futures <b>2,902.00, +0.71%</b>; <b>VIX 14.85, +0.27%</b>. '
 'And an untimed second account, <b>retained from a previous edition and not restated this run</b>: S&amp;P +0.6%, '
 'Nasdaq +0.8&ndash;0.9%, Dow +153 points (+0.3%), crude &minus;3% above $96.</p></div>')

MOVERS = [
 ("Warner Bros. Discovery (WBD)","up","+9.77%",
  "The session&rsquo;s largest sourced move. The Wall Street Journal reported progress in negotiations aimed at "
  "resolving legal challenges to the proposed merger with Paramount Skydance. Premarket the same name was "
  "<b>+7.12%</b> at 8:42&nbsp;AM; this is the 10:28&nbsp;AM regular-session figure."),
 ("Intel (INTC)","up","+9.7%",
  "Up on reports the chipmaker is partnering with Taiwanese display-panel manufacturer <b>AUO Optronics</b> to "
  "jointly develop <b>Micro LED advanced packaging</b> technology. Premarket reading was +5.76%."),
 ("Advanced Micro Devices (AMD)","up","+9.17%",
  "Up on reports AMD plans to <b>raise prices by 10% on some AI accelerators and GPUs</b>."),
 ("Paramount Skydance (PSKY)","up","+9.1%",
  "The other side of the merger trade; +6% premarket. Separately, CNN reports Paramount is in advanced talks with "
  "state attorneys general to resolve the antitrust suit blocking the acquisition."),
 ("Novo Nordisk (NVO)","down","&minus;8.01%",
  "The day&rsquo;s largest sourced decline. The drugmaker unveiled its long-term strategy and obesity ambitions but "
  "failed to ease investor concerns about competing in an increasingly crowded weight-loss market, per CNBC. "
  "Premarket the loss was &minus;4.35%; it has roughly doubled."),
 ("HP (HPQ)","down","&minus;3.39%",
  "Lower after the company warned it expects <b>global PC unit volumes to shrink by mid-single digits in calendar "
  "2027</b> against 2026. This one <b>narrowed</b> from &minus;4.75% premarket."),
 ("United Parcel Service (UPS)","down","&minus;2.78%",
  "Down amid investor concerns about an unusually high dividend yield and tight free cash flow."),
]

SCORE = [
 ("S&amp;P 500","7,650.50","+0.17%","up"),
 ("Nasdaq Composite","26,522.55","+0.39%","up"),
 ("Dow Jones Industrial Average","51,682.64","&minus;95.40 (&minus;0.18%)","down"),
]

RATES = [
 ("Fed funds target","3.75%&ndash;4.00%","Raised 25bp on 16 September &mdash; 12&ndash;0, and the first hike since July 2023."),
 ("Fed funds (effective)","3.88%","Federal Reserve H.15, 17 September column &mdash; up from 3.63% before the hike."),
 ("2-year Treasury","4.67%","H.15, 17 September."),
 ("10-year Treasury","4.94%","H.15, 17 September. A 5.01% figure carried by earlier editions as &ldquo;18 September&rdquo; is in fact H.15&rsquo;s 16 September print. Separately, an account read this run says the 10-year <b>fell below 5%</b> today without stating a level."),
 ("20-year Treasury","5.32%","H.15, 17 September."),
 ("30-year Treasury","5.29%","H.15, 17 September."),
 ("Bank prime rate","7.00%","H.15 &mdash; up from 6.75% before the hike."),
 ("WTI crude","$97.79","&minus;2.50% at 7:42&nbsp;AM ET (TheStreet). Yahoo&rsquo;s strip separately shows the <b>November</b> contract at <b>$93.49, &minus;2.70%</b> &mdash; a different contract month, not a contradiction."),
 ("Brent crude","$101.30","&minus;2.49% at 7:42&nbsp;AM ET. Fourth straight daily decline."),
 ("Gold","$4,396.60 futures","&minus;0.64% in early trading (TheStreet, 7:46&nbsp;AM). Yahoo&rsquo;s strip reads <b>$4,392.30, &minus;0.74%</b>; both printed."),
 ("Silver","$66.80 futures","&minus;0.52% in early trading (TheStreet, 7:49&nbsp;AM)."),
 ("Bitcoin","$84,402.56 / $85,244.52","Three readings of the same morning, all printed: <b>+5.13% at $84,402.56</b> (TheStreet, 7:16&nbsp;AM); <b>+5.86% at $85,244.52</b> (Yahoo strip, ~9:05&nbsp;AM); and a third account simply saying bitcoin <b>topped $85,000</b>."),
 ("VIX","14.85","+0.27% on the Yahoo strip (~9:05&nbsp;AM ET)."),
]

RADAR = [
 "<b>The Trump&ndash;Xi summit is Thursday, 24 September</b>, in Washington. Talks are expected to cover tariffs, "
 "critical minerals and artificial intelligence. Treasury Secretary <b>Scott Bessent</b> met Chinese Vice Premier "
 "<b>He Lifeng</b> for hours ahead of the visit and proposed a <b>US&ndash;China AI safety notification "
 "mechanism</b>; Xinhua acknowledged only that AI was discussed. The South China Morning Post reports the two sides "
 "are discussing possible announcements to strengthen <b>military-to-military ties</b>.",
 "<b>AI chief executives are attending a dinner with Xi</b> &mdash; Nvidia&rsquo;s Jensen Huang, OpenAI&rsquo;s Sam "
 "Altman, former Apple CEO Tim Cook, Qualcomm&rsquo;s Cristiano Amon and Microsoft&rsquo;s Satya Nadella. The summit "
 "lands as an essay by Anthropic CEO Dario Amodei has reopened the debate over whether frontier labs should pace "
 "model development. Bessent told CNBC that AI developers &ldquo;need to take responsibility for themselves&rdquo; "
 "rather than expect a federal liability shield: &ldquo;It is humans who are responsible, not the AI.&rdquo;",
 "<b>Oura is going public.</b> The Finnish smart-ring maker and some backers are marketing <b>50 million shares at "
 "$40&ndash;$44</b>, valuing the company at up to <b>$14.1 billion</b> at the top of the range against about $11 "
 "billion in its 2025 Series E. Oura will sell 13.5 million shares and selling shareholders 36.5 million; the ticker "
 "is <b>OURA</b>. It sold about <b>3.6 million rings</b> in the past year at $399&ndash;$499. Goldman Sachs, Morgan "
 "Stanley, JPMorgan, Allen &amp; Company and Jefferies are leading.",
 "<b>The Paramount&ndash;Warner settlement has holdouts.</b> California AG <b>Rob Bonta</b>, who leads the 12-state "
 "coalition, has been pressing to strike a deal; New York AG <b>Letitia James</b> is resisting the terms and seeking "
 "additional protections for workers, and Connecticut plus at least two other states have reservations (CNN).",
 "<b>The oil supply story behind the move.</b> Saudi Arabia expects to restore about <b>half of its East-West "
 "pipeline capacity within days</b>; its crude exports have surged past <b>4 million barrels a day</b> this month, "
 "up from a 13-year low of <b>2.4 million</b> in August. Shipments through the Strait of Hormuz have climbed to a "
 "six-month high, and JPMorgan estimates total Gulf oil flows averaged <b>17.1 million barrels a day</b> over the "
 "past 10 days.",
 "<b>Today&rsquo;s calendar is thin.</b> Economic data: <b>Chicago Fed National Activity Index, August</b> "
 "(&minus;0.06 expected, &minus;0.08 previously). Yahoo&rsquo;s Monday entry reads <b>&ldquo;no notable "
 "earnings&rdquo;</b>; a Kiplinger week-ahead count carried from 20 September said 14. Both are printed; neither is "
 "reconciled.",
 "<b>Iran and the UN General Assembly.</b> President <b>Masoud Pezeshkian</b> leads an Iranian delegation to the "
 "UNGA in New York on Tuesday amid renewed hope of a diplomatic track. Iranian state agency IRNA says the U.S. has "
 "refused visas for some delegation members. Separately, Trump told Fox News correspondent Trey Yingst the question "
 "was &ldquo;if and when&rdquo; it would be necessary to &ldquo;blow the entire nation up&rdquo; should Tehran not "
 "meet his demands.",
 "<b>The White House press pool has fractured.</b> After CNN was barred from serving as the designated TV pooler on "
 "Monday, the four other members &mdash; NBC, ABC, CBS and Fox News &mdash; will stop covering the President&rsquo;s "
 "events. CNN, MS NOW and Politico are suing the administration to overturn the access ban.",
]

SRC = [
 ("https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-21-2026",
  "TheStreet &mdash; Stock Market Today, 21 September 2026 (live blog, fetched in full)"),
 ("https://finance.yahoo.com/markets/live/stock-market-today-monday-september-21-dow-sp-500-nasdaq-080214605.html",
  "Yahoo Finance &mdash; Stock market today, Monday 21 September (live blog + quote strip)"),
 ("https://www.cnbc.com/2026/09/21/novo-nordisk-stock-sales-target-obesity-drugs.html",
  "CNBC &mdash; Novo Nordisk sales target and obesity drugs"),
 ("https://www.cnbc.com/2026/09/21/treasury-bessent-cnbc-squawk-trump-bond-affordabilty.html",
  "CNBC &mdash; Bessent on AI developer responsibility"),
 ("https://www.cnbc.com/2026/09/21/trump-white-house-press-pool-cnn-ban.html",
  "CNBC &mdash; White House TV pool after the CNN ban"),
 ("https://www.bloomberg.com/news/articles/2026-09-21/smart-ring-maker-oura-backers-seek-2-2-billion-in-us-ipo",
  "Bloomberg &mdash; Oura and backers seek $2.2 billion in US IPO"),
 ("https://finance.yahoo.com/media-advertising/articles/paramount-nears-merger-settlement-key-203032002.html",
  "CNN via Yahoo Finance &mdash; Paramount nears merger settlement, state AGs not all on board"),
 ("https://www.coindesk.com/business/2026/09/21/live-updates-bitcoin-rises-above-usd82-000-as-falling-oil-lifts-risk-assets",
  "CoinDesk &mdash; bitcoin live updates, short-side liquidations"),
 ("https://www.federalreserve.gov/releases/h15/", "Federal Reserve &mdash; H.15 Selected Interest Rates"),
 ("https://www.bloomberg.com/news/articles/2026-09-20/us-stock-futures-up-ahead-of-talks-dollar-steady-markets-wrap",
  "Bloomberg &mdash; Stock Market Today live updates, 21 September"),
]

b = []
b.append(C.head("The Closing Bell &mdash; Daily Markets Briefing", "ws"))
b.append(C.masthead("The Closing Bell", "Your daily Wall Street briefing &mdash; markets, movers and the tape"))
b.append(C.META)
b.append(C.tldr("The Tape", TLDR))
b.append(C.nav("ws"))
b.append(TICKER)
b.append(C.sec("Live Index Quotes &mdash; updates in real time"))
b.append(QUOTES)
b.append(C.sec("The Lead"))
b.append(LEAD)
b.append(C.sec("Movers &amp; Drivers"))
b.append('<p class="note" style="margin-bottom:12px">All seven figures below come from a single timestamped block '
         '&mdash; TheStreet&rsquo;s <b>10:28&nbsp;AM ET regular-session</b> market-movers entry. None of the seven is '
         'new against the previous edition, so none carries a New tag.</p>')
b.append('<div class="cards">')
for name, cls, pct, txt in MOVERS:
    b.append('<div class="card"><span class="tag %s">%s</span><h3>%s</h3><p>%s</p></div>'
             % ("good" if cls == "up" else "crit", pct, name, txt))
b.append('</div>')
b.append(C.sec("Chart of the Day &mdash; Warner Bros. Discovery (WBD)"))
b.append(MINI)
b.append('<p class="note">WBD is the largest move on the sourced list at +9.77%.</p>')
b.append(C.sec("Sector Heat &mdash; live"))
b.append(HEATMAP)
b.append('<p class="note">Editorial line, sourced this run: most sectors were in the green, led by technology and '
         'financial stocks, while oil and gas shares retreated. The <b>VIX</b> was <b>14.85, +0.27%</b> on '
         'Yahoo&rsquo;s ~9:05&nbsp;AM strip.</p>')
b.append(C.sec("The Calendar &mdash; live"))
b.append(EVENTS)
b.append(C.sec("Live Market Headlines &mdash; updates in real time"))
b.append(TIMELINE)
b.append(C.sec("Weekly Scorecard &mdash; Friday 18 September close"))
b.append('<div class="panel"><table><tr><th>Index</th><th>Close</th><th>Change</th></tr>')
for n, lvl, chg, cls in SCORE:
    b.append('<tr><td>%s</td><td class="mono">%s</td><td class="%s">%s</td></tr>' % (n, lvl, cls, chg))
b.append('</table><p class="note">Official closes only. These three levels are carried from this desk&rsquo;s '
         'standing ledger, where they have been re-verified ten times and reconcile on points, percentage and level. '
         'The Dow&rsquo;s <b>third straight weekly loss</b> was restated in coverage read this run. Index levels '
         'appear on this page only here.</p></div>')
b.append(C.sec("Rates, Bonds &amp; Commodities"))
b.append('<div class="panel"><table><tr><th>Instrument</th><th>Level</th><th>Note</th></tr>')
for n, lvl, note in RATES:
    b.append('<tr><td>%s</td><td class="mono">%s</td><td class="mut">%s</td></tr>' % (n, lvl, note))
b.append('</table></div>')
b.append(C.sec("On the Radar"))
b.append('<div class="panel"><ul class="bul">')
for r in RADAR:
    b.append('<li>%s</li>' % r)
b.append('</ul></div>')
b.append(C.srcs(SRC))
b.append(C.footer("Information only, not investment advice. Quotes in the live widgets are supplied by TradingView "
                  "and may be delayed. Every figure above is either stated by a source fetched in this run, with its "
                  "as-of time, or explicitly labelled as carried from this desk&rsquo;s standing ledger."))
b.append(C.TAIL)

io.open(OUT, "w", encoding="utf-8").write("".join(b))
print("wrote", OUT)
