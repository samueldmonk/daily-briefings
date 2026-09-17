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

TLDR = ("Stocks are extending Wednesday's rebound &mdash; the S&amp;P 500 is up 1.12% and the Dow 0.73% "
        "as of about 2:50 p.m. ET, with Treasury yields easing right across the curve and crude slipping, "
        "while Generac remains the day's outsized single-name move on its Amazon generator deal.")

TAPE_A = """<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NYSE:GNRC","title":"Generac"},{"proName":"NYSE:HPE","title":"HPE"},{"proName":"NASDAQ:MRNA","title":"Moderna"},{"proName":"NASDAQ:FLNC","title":"Fluence"},{"proName":"NYSE:CTRA","title":"Coterra"},{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script>"""

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
<h3 style="margin:0 0 9px;font-size:21px">The rebound holds into the afternoon: S&amp;P 500 +1.12%, Dow +0.73% as of about 2:50 p.m. ET</h3>
<p style="margin:0 0 10px">A day after the Federal Reserve raised rates for the first time in three years, buyers are still in control. As of roughly <strong>2:50 p.m. ET</strong> the <strong>S&amp;P 500 was +1.12%</strong>, up <strong>84.90 points</strong> on Wednesday's settle, and the <strong>Dow was +0.73%</strong>, up <strong>374.13 points</strong>. Both reconcile exactly against Wednesday's closes, which is the reason they are the figures carried here.</p>
<p style="margin:0 0 10px">Earlier in the session TheStreet had the S&amp;P &ldquo;up about one percent&rdquo; at <strong>10:54 a.m. ET</strong>, with <strong>259 of the index's 503 holdings advancing</strong> and strength concentrated in cyclicals and technology. The Dow had opened only <strong>+0.48%</strong>, a 248-point gain, so the blue chips have added to their move through the day rather than faded it.</p>
<p style="margin:0 0 10px">The two forces doing the work are <strong>easing yields</strong> and <strong>softer crude</strong>. The whole Treasury curve is lower &mdash; the <strong>10-year at 4.95%, down about seven basis points</strong>, the <strong>2-year at 4.69%</strong> and the <strong>30-year at 5.30%</strong>. Oil has given back part of the war premium after Saudi Arabia offered extra cargoes to Asian refiners through ship-to-ship transfers off Oman's Sohar port, and after U.S. Energy Secretary Chris Wright signalled a quicker return to service for the Saudi East-West pipeline. Crude nonetheless remains above <strong>$100</strong>.</p>
<p style="margin:0 0 10px">Wednesday's decision itself was <strong>unanimous</strong>: a <strong>25 basis point</strong> increase to a target range of <strong>3.75%&ndash;4.00%</strong>, the first rise since July 2023. The sting was in the projections. &ldquo;The decision was unanimous and the new projections show <strong>16 of 18 officials expecting at least one further hike this year</strong>,&rdquo; said Daniela Hathorn of Capital.com. Chair <strong>Kevin Warsh</strong> put it plainly: &ldquo;the plain fact is that inflation is too high and has been for too long.&rdquo; President Trump, who nominated him, said on Wednesday he still has confidence in Warsh &mdash; while also saying he wants rates slashed to <strong>1% &ldquo;or less.&rdquo;</strong></p>
<p style="margin:0" class="note">Refused this run, for the second consecutive edition: 24/7 Wall St.'s site-header quote strip, read at about 2:50 p.m. ET while the session was still trading, showed S&amp;P 500 <strong>7,630.50 &ldquo;+0.85%&rdquo;</strong> and Dow <strong>51,737.00 &ldquo;+0.37%&rdquo;</strong> under an <em>At close</em> label. Against Wednesday's settles those levels imply +1.04% and +0.53% &mdash; neither pair is internally consistent, so no level from that strip is published. The same page carried three different quotes for Super Micro (+6.08%, +10.29% and +3.40%) and two for QQQ; both names are therefore omitted entirely rather than picked between.</p>
</div>

<h2 class="sec">Movers &amp; Drivers</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t gold">Power &amp; AI</span><span class="t">NYSE:GNRC</span></div>
<h3>Generac and the $8 billion generator order</h3>
<p>Generac and <strong>Amazon</strong> have signed a long-term supply agreement for up to <strong>$8 billion</strong> of industrial backup generators for Amazon data centres, with <strong>initial deliveries totalling $2.4 billion across 2027 and 2028</strong>. The percentages stated today are not averaged here, each carries its own clock: <strong>+30.1% premarket</strong> and <strong>+21.35% at 10:25 a.m. ET</strong> (TheStreet), and <strong>+18.58% to $207.65</strong> on 24/7 Wall St.'s biggest-winners board this afternoon. It remains the largest single-name move on the tape.</p>
</div>
<div class="card">
<div class="tags"><span class="t pro">AI hardware</span><span class="t">HPE &middot; DELL</span></div>
<h3>The memory bid broadens into server makers</h3>
<p>A rally that began this week in memory and chip names has widened into the box builders. <strong>Hewlett Packard Enterprise</strong> was <strong>+7.44%</strong> at 10:25 a.m. ET (TheStreet) and <strong>+9.02% to $61.64</strong> at 10:53 a.m. ET (24/7 Wall St.); <strong>Dell</strong> was <strong>+3.36% to $582.20</strong>. Tellingly, the iShares U.S. Technology ETF managed only <strong>+1.83%</strong> over the same window &mdash; this is a hardware-assembler rotation, not a broad tech move. A closely watched gauge of chipmakers climbed <strong>3%</strong>. Super Micro is excluded: the same page quoted it three incompatible ways.</p>
</div>
<div class="card">
<div class="tags"><span class="t pro">Phase 3</span><span class="t">NASDAQ:MRNA</span></div>
<h3>Moderna keeps running on the cancer-vaccine read-out</h3>
<p>Moderna gained <strong>9.39%</strong> by 10:25 a.m. ET and was <strong>+9.55% at $159.53</strong> on the afternoon winners board, as investors continued to react to positive Phase 3 results announced with <strong>Merck</strong> for their personalised mRNA cancer vaccine, <strong>intismeran autogene (mRNA-4157)</strong>.</p>
</div>
<div class="card">
<div class="tags"><span class="t hot">Guidance cut</span><span class="t">NASDAQ:FLNC</span></div>
<h3>Fluence Energy tumbles on a cut outlook</h3>
<p>The battery-storage company cut its full-year outlook, citing delays at its contract manufacturing facility. Shares were <strong>&minus;22.22% premarket</strong> and <strong>&minus;16.85%</strong> by 10:25 a.m. ET &mdash; both reads printed, neither averaged.</p>
</div>
<div class="card">
<div class="tags"><span class="t hot">Energy lags</span><span class="t new">New</span><span class="t">NYSE:CTRA</span></div>
<h3>Energy is the drag as crude gives ground</h3>
<p>With oil retreating, energy is the visible laggard: <strong>Coterra Energy</strong> headed 24/7 Wall St.'s biggest-losers board at <strong>&minus;8.62% to $32.56</strong> this afternoon. <strong>Salesforce</strong> (<strong>&minus;3.18%</strong> on the same board, <strong>&minus;4.30%</strong> at the open per Trading Economics) and <strong>Equity Residential</strong> (<strong>&minus;3.50%</strong>) round out the weak side. Single-board figures, so stated as such.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Balance sheet</span><span class="t">NASDAQ:CRWV</span></div>
<h3>CoreWeave slips on a $3 billion convertible</h3>
<p>CoreWeave dropped <strong>4.69%</strong> after announcing plans to raise <strong>$3 billion</strong> through a convertible debt offering. Elsewhere on the downside, <strong>Copart</strong> lost <strong>2.99%</strong> (&minus;3.91% on the afternoon board) after HSBC cut it to Hold from Buy with a <strong>$36</strong> price target, citing insurance-business challenges and slowing growth.</p>
</div>
</div>

<h2 class="sec">Chart of the Day &mdash; Generac (GNRC)</h2>
<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"NYSE:GNRC","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}</script></div>
<p class="note">The session's marquee single-name move for a second day. The chart is live; the percentages in the card above are the ones sources actually stated, each with its own clock.</p>

<h2 class="sec">Sector Heat &mdash; live</h2>
<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}</script></div>
<p class="note">One sourced line on breadth: <strong>259 of the S&amp;P 500's 503 holdings were advancing</strong> at 10:54 a.m. ET, a majority but not a landslide, with the strength &ldquo;anchored in cyclicals and tech&rdquo;. Full sector-level percentages with a stated measurement window were not published by any source fetched this run, so none is printed.</p>

<h2 class="sec">The Calendar &mdash; live</h2>
<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en","importanceFilter":"0,1","countryFilter":"us"}</script></div>

<h2 class="sec">Live Market Headlines &mdash; updates in real time</h2>
<div class="panel" style="padding:8px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,"displayMode":"regular","width":"100%","height":420,"locale":"en"}</script></div>

<h2 class="sec">Weekly Scorecard</h2>
<div class="panel" style="padding:4px 0">
<table>
<tr><th>Session</th><th>S&amp;P 500</th><th>Nasdaq Composite</th><th>Dow Jones Industrial Average</th></tr>
<tr><td>Wed 16 Sep &mdash; close</td><td class="down">7,551.81 &nbsp;&minus;0.45%</td><td class="down">25,978.42 &nbsp;&minus;0.01%</td><td class="down">51,461.90 &nbsp;&minus;631.21 (&minus;1.21%)</td></tr>
<tr><td>Thu 17 Sep</td><td class="mut" colspan="3">Session in progress &mdash; no close to publish. Latest verified intraday read, ~2:50 p.m. ET: S&amp;P 500 <span class="up">+1.12%</span> (+84.90 pts), Dow <span class="up">+0.73%</span> (+374.13 pts). No Nasdaq Composite figure is published &mdash; see note.</td></tr>
</table>
</div>
<p class="note">Only settled closes appear as levels. Both of Thursday's intraday moves reconcile exactly to Wednesday's settles: 7,551.81 + 84.90 = 7,636.71 and 51,461.90 + 374.13 = 51,836.03. <strong>No Nasdaq Composite percentage is published this run:</strong> every figure circulating for it came from ETF proxies (QQQ) rather than the index, and the one page carrying those proxies quoted QQQ two incompatible ways.</p>

<h2 class="sec">Rates, Bonds &amp; Commodities</h2>
<div class="panel" style="padding:4px 0">
<table>
<tr><th>Instrument</th><th>Level</th><th>Move</th><th>As of / source</th></tr>
<tr><td>US 2-year Treasury yield</td><td>4.69%</td><td class="up">&minus;5 bp</td><td>17 Sep, Trading Economics</td></tr>
<tr><td>US 5-year Treasury yield</td><td>4.81%</td><td class="up">&minus;8 bp</td><td>17 Sep, Trading Economics</td></tr>
<tr><td>US 10-year Treasury yield</td><td>4.95%</td><td class="up">&minus;7 bp</td><td>17 Sep, Trading Economics</td></tr>
<tr><td>US 30-year Treasury yield</td><td>5.30%</td><td class="up">&minus;7 bp</td><td>17 Sep, Trading Economics</td></tr>
<tr><td>Fed funds target range</td><td>3.75%&ndash;4.00%</td><td class="down">+25 bp, unanimous</td><td>16 Sep FOMC decision</td></tr>
<tr><td>WTI crude</td><td>$101.65</td><td class="up">&minus;0.8%</td><td>17 Sep, Trading Economics</td></tr>
<tr><td>WTI crude (early trade)</td><td>$100.70</td><td class="up">&minus;1.70%</td><td>17 Sep 7:07 a.m. ET, TheStreet</td></tr>
<tr><td>Brent crude (early trade)</td><td>$103.60</td><td class="up">&minus;2.07%</td><td>17 Sep 7:07 a.m. ET, TheStreet</td></tr>
<tr><td>Gold futures (early trade)</td><td>$4,404.30</td><td class="up">+0.38%</td><td>17 Sep, TheStreet</td></tr>
<tr><td>Silver futures (early trade)</td><td>$65.82</td><td class="up">+1.40%</td><td>17 Sep, TheStreet</td></tr>
<tr><td>CBOE Volatility Index</td><td class="mut">not published</td><td class="mut">&mdash;</td><td>see note</td></tr>
</table>
</div>
<p class="note">Falls in yields and oil are shown in green because that is the direction helping equities today, not because lower is inherently better. Two WTI reads appear because two sources gave two clocks; neither is aged forward onto the other. On the afternoon WTI row the source's change column rendered without a sign; the magnitude matches the percentage and the direction is corroborated by TheStreet and Reuters, so it is published as a fall and the caveat stated. Trading Economics also showed spot gold at <strong>$4,360.78, +2.28%</strong> &mdash; a different instrument and a different clock from TheStreet's futures quote, so both are shown rather than reconciled. <strong>The VIX is refused this run:</strong> the source row gave a level of 15.56 with a change of &ldquo;&minus;2.15&rdquo; and a percentage of &ldquo;&minus;2.15%&rdquo;, which cannot both be true of the same number, so neither is carried. Bitcoin is omitted: no source fetched this run gave a current level.</p>

<h2 class="sec">On the Radar</h2>
<div class="panel">
<ul class="bul">
<li><strong>The SEC opened a door for tokenized stocks this morning.</strong> The Commission issued an order creating a regulatory pathway for certain trading venues to list and trade tokenized versions of publicly traded U.S. stocks, <strong>effective immediately</strong>. The five-year &ldquo;Innovation Exemption&rdquo; is not a formal rulemaking; two conditions are contested &mdash; token holders must retain the same rights as ordinary equity holders, and companies must be able to object to their securities being tokenized. It lands two days after the Clarity Act failed to advance in the Senate.</li>
<li><strong>One more hike is the base case.</strong> Sixteen of eighteen officials expect at least one further increase this year, so every inflation print between now and December is a policy print.</li>
<li><strong>Oil is still the swing factor.</strong> Crude stayed above $100 even while falling, and the war premium is what the Fed said it cannot directly influence &mdash; only its second- and third-round effects.</li>
<li><strong>SpaceX has a date.</strong> SPCX rose <strong>1.84% to $153.65</strong> premarket after ARK's Cathie Wood argued Starship could generate <strong>$10 trillion</strong> in annual revenue by 2030; Elon Musk called the underlying 10,000-flights-a-year target &ldquo;not impossible.&rdquo; The next Starship test flight is set for <strong>22 September</strong>. The stock debuted at $135 on 12 June and hit a record $225.64 on 16 June.</li>
<li><strong>Trade politics.</strong> Canadian PM Mark Carney welcomed an EU proposal to make Canada an associate member; Trump called the prospect &ldquo;laughable&rdquo; and threatened &ldquo;very heavy tariffs&rdquo; if he judged it a hostile act.</li>
</ul>
</div>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
<a href="https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-17-2026">TheStreet live blog, 17 Sep (movers, oil, gold, silver, SEC order, SpaceX, Fed)</a> &middot;
<a href="https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-16-2026">TheStreet, 16 Sep close</a> &middot;
<a href="https://tradingeconomics.com/united-states/stock-market">Trading Economics &mdash; US indices, VIX, Dow open detail</a> &middot;
<a href="https://tradingeconomics.com/united-states/government-bond-yield">Trading Economics &mdash; Treasury curve</a> &middot;
<a href="https://tradingeconomics.com/commodity/crude-oil">Trading Economics &mdash; WTI</a> &middot;
<a href="https://tradingeconomics.com/commodity/gold">Trading Economics &mdash; gold</a> &middot;
<a href="https://247wallst.com/investing/2026/09/17/ai-server-stocks-rally-as-the-hardware-bid-broadens-hewlett-packard-enterprise-jumps-9-super-micro-climbs-6-dell-rises-3/">24/7 Wall St. on AI server stocks, 10:53 a.m. ET 17 Sep</a> &middot;
<a href="https://www.bloomberg.com/news/articles/2026-09-16/stock-market-today-dow-s-p-live-updates">Bloomberg live updates, 17 Sep</a> &middot;
<a href="https://www.reuters.com/business/energy/oil-prices-extend-losses-fears-middle-east-supply-disruptions-ease-2026-09-17/">Reuters on crude, 17 Sep</a> &middot;
<a href="https://www.cnbc.com/2026/09/17/sec-clears-path-for-tokenized-stocks-bringing-24/7-trading-closer.html">CNBC on the SEC tokenized-stock order</a> &middot;
<a href="https://www.cnbc.com/2026/09/16/trump-fed-interest-rate-warsh.html">CNBC on Trump and Warsh</a> &middot;
<a href="https://www.cnbc.com/2026/09/17/carney-canada-eu-associate-member.html">CNBC on Carney and the EU</a> &middot;
<a href="https://www.barchart.com/story/news/4641652/a-10-trillion-reason-why-spacex-stock-is-up-today">Barchart on Cathie Wood and SpaceX</a>
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
