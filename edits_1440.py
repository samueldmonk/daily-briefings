#!/usr/bin/env python3
"""Incremental edits for the 2:44 p.m. ET Midday Edition, Wed Aug 26 2026."""
import re, sys, os

D = sys.argv[1] if len(sys.argv) > 1 else '.'
def rd(f): return open(os.path.join(D, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(D, f), 'w', encoding='utf-8').write(s)

def once(s, old, new, label):
    n = s.count(old)
    assert n == 1, f'{label}: expected 1 occurrence, found {n}'
    return s.replace(old, new)

# ---------------------------------------------------------------- WALL STREET
w = rd('wallstreet-briefing.html')

# 1. Demote previous edition's New markers.
w = w.replace('<span class="tag new">New &middot; 1:40</span>',
              '<span class="tag">Carried &middot; 1:40 edition</span>')
w = w.replace('&#9679; New at 1:40 &mdash;', '&#9679; Carried from the 1:40 edition &mdash;')
assert 'New &middot; 1:40' not in w and 'New at 1:40' not in w

# 2. New lead bullet + headline.
w = once(w,
 '<h2>A fourth index joins the board at 1:24, and all four of them reconcile</h2>\n<p><b>&#9679; Carried from the 1:40 edition',
 '<h2>Two widgets, one page, ninety minutes apart &mdash; and the day&rsquo;s biggest move is bigger than this desk had it</h2>\n'
 '<p><b>&#9679; New at 2:44 &mdash; the single most useful thing learned this run is that one Yahoo Finance page serves its index board and its '
 'trending-ticker strip from separate caches, and they can sit more than an hour apart.</b> Yahoo&rsquo;s syndication of the Zacks &ldquo;Stock Market News '
 'for Aug 26&rdquo; report was fetched in full at approximately <b>2:40&nbsp;p.m. ET</b>. Its index board header reads &ldquo;U.S. markets close in 3h 55m,&rdquo; '
 'which places that board at roughly <b>12:05&nbsp;p.m. ET</b> &mdash; older than the 1:25 board below and <b>two and a half hours behind the wall clock at fetch</b>. '
 'Its <em>trending-ticker</em> strip on the very same page is not: it carries moves materially larger than any this page has published today. '
 '<b>&#9888; The two are therefore treated as two independent reads with two different effective times, and neither is used to date the other.</b> '
 'On that strip: <b>ANF $153.40, &plus;$44.50, &plus;40.86%</b>; <b>XPON $8.86, &plus;$3.59, &plus;68.12%</b>; <b>INTU $339.41, &minus;$18.05, &minus;5.05%</b>; '
 '<b>CRE $6.18, &plus;$3.61, &plus;140.47%</b>; and META $577.46, &plus;$7.41, &plus;1.30% unchanged from the earlier strip. Every one of those five reconciles: '
 '153.40 &minus; 44.50 = 108.90, 8.86 &minus; 3.59 = 5.27, 339.41 &plus; 18.05 = 357.46, 6.18 &minus; 3.61 = 2.57, 577.46 &minus; 7.41 = 570.05 &mdash; and each percent '
 'equals its own points-over-prior-close. <b>Read against the strip on the earlier page (ANF &plus;32.33%, XPON &plus;51.99%, INTU &minus;3.59%), all three of those names have '
 'extended their moves in the same direction</b>, which is what makes this the later read despite sitting on a page whose index board is the older one. '
 '<b>&#9888; One caveat printed rather than smoothed: ANF&rsquo;s implied prior close here is $108.90, where eight earlier renderings gave $108.91.</b> That is a one-cent '
 'difference in Yahoo&rsquo;s change field, it is not adjudicated, and both bases are left standing.</p>\n'
 '<p><b>&#9679; New at 2:44 &mdash; the four-index board advances by one tick, and it still reconciles four ways.</b> A second Yahoo page fetched this run '
 '(the Wednesday earnings live blog) carries a board whose header reads &ldquo;U.S. markets close in 2h 35m,&rdquo; placing it at approximately '
 '<b>1:25&nbsp;p.m. ET</b>: <b>S&amp;P&nbsp;500 7,674.09, &minus;3.19, &minus;0.04%</b>; <b>Dow&nbsp;30 53,469.42, &minus;107.98, &minus;0.20%</b>; '
 '<b>Nasdaq 26,101.79, &minus;49.51, &minus;0.19%</b>; <b>Russell&nbsp;2000 3,003.81, &minus;6.22, &minus;0.21%</b>. The first three subtract exactly to the Weekly '
 'Scorecard closes &mdash; 7,677.28, 53,577.40, 26,151.30 &mdash; and each percent equals points over that close (0.0416%, 0.2015%, 0.1893%). '
 '<b>&#9888; The Russell line is one cent out</b>: 3,003.81 &plus; 6.22 = 3,010.03 against a published close of 3,010.02, consistent with a level rounded from '
 '3,003.805; the percent (6.22 &divide; 3,010.02 = 0.2066%) still lands on the stated 0.21%. Set against the 1:24 board carried from the 1:40 edition below, this is '
 'the <b>same session one minute later and barely moved</b> &mdash; the S&amp;P fifteen cents higher, the Dow a point and a quarter higher. '
 '<b>&#9888; It is a cached render sixty-nine minutes behind the wall clock at fetch, published as a 1:25 print and not as a live tick.</b> Same board: '
 '<b>VIX 15.55, &plus;0.10, &plus;0.65%</b>, which reconciles against a 15.45 prior close &mdash; and Zacks independently confirms that 15.45 was Tuesday&rsquo;s VIX close.</p>\n'
 '<p><b>&#9679; New at 2:44 &mdash; and a mover this page nearly published a day late.</b> A trending strip read this run listed '
 '<b>DKS (DICK&rsquo;S Sporting Goods) at $124.31, &minus;$55.02, &minus;30.68%</b>, arithmetic clean against a $179.33 prior close. '
 '<b>&#9888; It is rejected as a Wednesday mover.</b> Seeking Alpha (&ldquo;plunges 31% after earnings miss&rdquo;), Schaeffer&rsquo;s (&ldquo;on track for worst day ever,&rdquo; '
 'dated Aug&nbsp;25) and The Motley Fool (&ldquo;Why Dick&rsquo;s Sporting Goods Stock Crashed Today,&rdquo; dated Aug&nbsp;25) all place the collapse on <b>Tuesday</b>, after a '
 'Q2 miss on both lines and a guidance cut driven by a promotional athletic-footwear market and the acquired Foot&nbsp;Locker banner. The &minus;30.68% is '
 'Tuesday&rsquo;s close carried forward in a stale strip, not a Wednesday move, and no Wednesday DKS figure is asserted here.</p>\n'
 '<p><b>&#9679; Carried from the 1:40 edition', 'ws-lead')

# 3. Movers: new cards at the top of the deck.
w = once(w, 'Movers &amp; drivers</div>\n<div class="cards">\n',
 'Movers &amp; drivers</div>\n<div class="cards">\n'
 '<div class="card"><div class="tags"><span class="tag new">New &middot; 2:44</span><span class="tag">Biggest move of the day</span>'
 '<span class="tag">Reconciles</span></div><h3>Abercrombie &amp; Fitch extends to &plus;40.86%, and the tariff line explains a chunk of the beat</h3>'
 '<p>The <b>~2:40&nbsp;p.m. ET</b> Yahoo trending strip prices <b>ANF at $153.40, &plus;$44.50, &plus;40.86%</b> &mdash; up from the &plus;32.33% this page carried an hour '
 'earlier, and <b>the largest single-name move any source has put a number on today</b>. StockStory&rsquo;s note, timestamped <b>12:55&nbsp;p.m. EDT</b>, priced it at '
 '<b>$144.81, a new 52-week high</b>, and reports record Q2 net sales of <b>$1.27&nbsp;billion, up 5% year over year, a 15th consecutive quarter of growth</b>, with '
 'diluted EPS of <b>$4.17 against a $1.99 consensus</b>. <b>&#9888; Roughly $100&nbsp;million of pre-tax tariff refunds contributed $1.75 of that $4.17</b> &mdash; so a '
 'material share of the headline beat is a one-off recovery rather than trading. Gross margin <b>62.4%</b>, operating margin near <b>20%</b>; APAC sales <b>&plus;19%</b>, '
 'the Abercrombie brand <b>&plus;8%</b>, Hollister <b>&plus;2%</b>. Guidance raised to net sales growth of about <b>5%</b>, diluted EPS of <b>$13.10 to $13.60</b>, and '
 'buybacks of <b>at least $500&nbsp;million</b>. <b>&#9888; StockStory&rsquo;s own headline figure of &ldquo;41.8%&rdquo; does not reconcile against the $144.81 it prints in the '
 'same article</b> ($144.81 off a $108.91 close is &plus;32.96%), so that percentage is not published; the 2:40 strip figure is.</p></div>\n'
 '<div class="card"><div class="tags"><span class="tag new">New &middot; 2:44</span><span class="tag">Chips</span>'
 '<span class="tag">~20-min delayed</span></div><h3>Nvidia slips under $210 going into its own print</h3>'
 '<p>A CloudQuote-powered quote table on FinancialContent, fetched this run and labelled <b>&ldquo;quotes delayed at least 20 minutes&rdquo;</b> &mdash; so an effective read of '
 'roughly <b>2:07&nbsp;p.m. ET</b> or later &mdash; puts <b>NVDA at $209.99, &minus;$3.06, &minus;1.44%</b> against a $213.05 Tuesday close. That is deeper than the '
 '&minus;1.28% this page carried from the cached midday strip, and it has the stock <b>below $210 hours before it opens its books</b>. The same table gives '
 '<b>ORCL $148.19, &plus;$3.44, &plus;2.37%</b> and <b>AMD $483.88, &plus;$4.70, &plus;0.98%</b> &mdash; so the chip complex is not moving as one bloc. '
 '<b>&#9888; The ORCL percentage is the one line here that does not round cleanly</b>: 3.44 &divide; 144.75 = 2.3765%, which rounds to 2.38 and not the stated 2.37; the '
 'source&rsquo;s figure is reproduced and flagged rather than corrected.</p></div>\n'
 '<div class="card"><div class="tags"><span class="tag new">New &middot; 2:44</span><span class="tag">Two prior closes corroborated</span>'
 '</div><h3>Mega-cap tape: two independent feeds land on the same prior closes to the cent</h3>'
 '<p>The FinancialContent table and the earlier Motley Fool strip disagree on the current tick but agree exactly on where each name started the day &mdash; '
 '<b>AAPL 309.90, META 570.05, MSFT 491.71, AMZN 261.06</b> all fall out of both feeds&rsquo; level-minus-change arithmetic, which is the strongest corroboration '
 'of a prior close this page has had today. On the later read: <b>AAPL $313.17, &plus;$3.27, &plus;1.05%</b>; <b>META $577.20, &plus;$7.15, &plus;1.25%</b>; '
 '<b>MSFT $494.72, &plus;$3.01, &plus;0.61%</b>; <b>AMZN $258.93, &minus;$2.13, &minus;0.82%</b>; <b>GOOG $338.26, &minus;$5.08, &minus;1.48%</b>; '
 '<b>TSLA $346.46, &minus;$3.79, &minus;1.08%</b>. <b>&#9888; GOOG is the one name where the two feeds imply prior closes a cent apart</b> (343.34 here against 343.35 '
 'from the Fool strip); both are printed. <b>&#9888; BAC at $62.45, &plus;$0.02, &plus;0.04% is dropped</b> &mdash; 0.02 &divide; 62.43 is 0.032%, which rounds to 0.03 and '
 'not the stated 0.04, and the move is too small to publish on a disputed rounding.</p></div>\n'
 '<div class="card"><div class="tags"><span class="tag new">New &middot; 2:44</span><span class="tag">No catalyst asserted</span>'
 '</div><h3>The small-cap tail: XPON doubles its gain, CRE more than doubles outright</h3>'
 '<p><b>XPON (Expion360) $8.86, &plus;$3.59, &plus;68.12%</b> on the 2:40 strip, up from &plus;51.80% and &plus;51.99% on two earlier reads off the same $5.27 base &mdash; '
 'a name whose move has now widened three times today. <b>CRE (Cre8 Enterprise Limited) $6.18, &plus;$3.61, &plus;140.47%</b> is new to this page entirely and is the '
 'largest percentage gain any source has stated today; 6.18 &minus; 3.61 = 2.57 and 3.61 &divide; 2.57 = 140.47%, so it reconciles exactly. '
 '<b>&#9888; No source read this run states a catalyst for either name, and none is asserted here.</b> Neither takes Chart of the Day. On the other side, '
 '<b>INTU (Intuit) $339.41, &minus;$18.05, &minus;5.05%</b> is a fifth successive tick off the same <b>$357.46</b> prior close, and the loss has widened at every '
 'reading today &mdash; &minus;3.37% premarket, then &minus;3.62%, &minus;3.59%, and now &minus;5.05%.</p></div>\n', 'ws-movers')

# 4. Chart of the day note.
w = once(w, '<div class="note"><b>&#9679; Updated 1:40 &mdash; a newer figure, and it also reconciles.</b>',
 '<div class="note"><b>&#9679; Updated 2:44 &mdash; the newest figure, and the move has widened again.</b> The ~2:40&nbsp;p.m. ET Yahoo trending strip puts '
 '<b>ANF at $153.40, &plus;$44.50, &plus;40.86%</b> &mdash; a ninth rendering of this name today and the largest of them. It implies a $108.90 prior close where the '
 'eight before it implied $108.91; the one-cent gap is printed, not reconciled. <b>Chart of the Day stays NYSE:ANF.</b> '
 '<b>&#9679; Carried from the 1:40 edition &mdash; a newer figure, and it also reconciles.</b>', 'ws-chart')

# 5. Weekly scorecard corroboration note.
w = once(w, 'Weekly scorecard</div>\n<div class="panel">\n<table>',
 'Weekly scorecard</div>\n'
 '<div class="note" style="margin-bottom:10px"><b>&#9679; New at 2:44 &mdash; Tuesday&rsquo;s closes independently re-confirmed, with one discrepancy printed.</b> '
 'Zacks&rsquo; Aug&nbsp;26 recap, fetched in full this run, gives the <b>Dow &plus;0.3% / &plus;160.24 to 53,577.40</b> and the <b>Nasdaq &plus;0.7% / &plus;171.11 to '
 '26,151.30</b> &mdash; both matching this table exactly &mdash; and confirms the <b>VIX closed at 15.45, down 2.52%</b>, which is the base every VIX reconciliation on '
 'this page has used. <b>&#9888; Zacks puts the S&amp;P close at 7,677.24, four cents below the 7,677.28 published here.</b> That 7,677.28 is what roughly a dozen '
 'independent quote renderings today subtract to exactly, so it stands; the Zacks figure is recorded as a discrepancy and not adopted. Zacks also gives Tuesday&rsquo;s '
 'breadth: advancers over decliners <b>1.71-to-1 on the NYSE</b> and <b>1.76-to-1 on the Nasdaq</b>, <b>14.32&nbsp;billion shares</b> traded against a 20-session average of '
 '<b>16.4&nbsp;billion</b>, and <b>190 new highs against 79 new lows</b> on the NYSE.</div>\n'
 '<div class="panel">\n<table>', 'ws-score')

# 6. Rates & commodities rows.
w = once(w, '<tr><td>10-year Treasury yield</td><td>4.67%</td>',
 '<tr><td>Gold (futures)</td><td>$4,655.50</td><td class="down">&minus;$39.00 (&minus;0.83%)</td><td>Wed, Aug 26, ~12:05 p.m. ET (Yahoo)</td></tr>\n'
 '<tr><td>WTI crude, Oct-26 contract</td><td>$82.88</td><td class="up">&plus;$0.52 (&plus;0.63%)</td><td>Wed, Aug 26, ~12:05 p.m. ET (Yahoo)</td></tr>\n'
 '<tr><td>Bitcoin</td><td>$78,100.48</td><td class="down">&minus;$1,052.82 (&minus;1.33%)</td><td>Wed, Aug 26, ~12:05 p.m. ET (Yahoo)</td></tr>\n'
 '<tr><td>CBOE Volatility Index (VIX)</td><td>15.45</td><td>0.00 (0.00%)</td><td>Wed, Aug 26, ~12:05 p.m. ET (Yahoo)</td></tr>\n'
 '<tr><td>10-year Treasury yield</td><td>4.67%</td>', 'ws-rates')

w = once(w, 'Rates, bonds &amp; commodities</div>\n<div class="panel">\n<table>',
 'Rates, bonds &amp; commodities</div>\n'
 '<div class="note" style="margin-bottom:10px"><b>&#9679; New at 2:44 &mdash; four rows added, none replaced, and one base that legitimately moves.</b> '
 'The ~12:05&nbsp;p.m. board and the ~1:25&nbsp;p.m. board give <b>gold at $4,655.50 (&minus;0.83%) and $4,650.50 (&minus;0.94%)</b> and <b>WTI Oct-26 at $82.88 '
 '(&plus;0.63%) and $82.73 (&plus;0.45%)</b> &mdash; two successive ticks each off a single prior close ($4,694.50 and $82.36 respectively), which is how they are '
 'published. <b>&#9888; Bitcoin is the exception</b>: the two reads imply different reference points ($79,153.30 and $79,237.00), which is expected of a 24-hour market '
 'where the trailing base itself rolls, and neither is treated as an error. <b>&#9888; The Trading Economics WTI row further down, at $80.78 and &minus;1.92%, carries the '
 'opposite sign to both Yahoo reads and remains unadjudicated.</b></div>\n'
 '<div class="panel">\n<table>', 'ws-rates-note')

# 7. On the radar.
w = once(w, 'On the radar</div>\n<div class="panel">\n<ul class="bul">\n',
 'On the radar</div>\n<div class="panel">\n<ul class="bul">\n'
 '<li><b>&#9679; New at 2:44 &mdash; the consumer is where Tuesday&rsquo;s soft spot was, and Wednesday&rsquo;s data agrees.</b> Zacks reports the Conference Board&rsquo;s '
 'August consumer confidence reading at <b>89.4, a seven-month low</b>, down 0.8% on the month and short of a <b>90.2</b> consensus. Bloomberg&rsquo;s and CNN&rsquo;s '
 'coverage of Wednesday&rsquo;s PCE release lands in the same place from the spending side &mdash; <b>consumer spending stalled in July</b>. Two separate surveys, one '
 'confidence and one outlay, pointing the same way in the same week.</li>\n'
 '<li><b>&#9679; New at 2:44 &mdash; where Tuesday&rsquo;s yield relief came from.</b> Zacks attributes the two-day decline in bond yields partly to a Monday report that '
 'Treasury Secretary <b>Scott Bessent</b> could deploy the department&rsquo;s <b>nearly $1&nbsp;trillion General Account</b> to help finance bond buybacks. The 10-year '
 'settled at <b>4.625%</b> Tuesday, more than seven basis points lower. <b>&#9888; That is a report of a possibility, not an announced programme, and nothing here asserts '
 'the buybacks will happen.</b> Separately, Zacks notes the US&ndash;Canada trade dispute escalating, with Canada imposing retaliatory tariffs on American imports.</li>\n'
 '<li><b>&#9679; New at 2:44 &mdash; housing, for the record.</b> The S&amp;P Cotality Case-Shiller index has US home prices up <b>0.4% sequentially in June</b> and '
 '<b>1.5% year over year</b>, per Zacks.</li>\n', 'ws-radar')

# 8. Sources.
w = once(w, 'Sources</div>\n<ul>\n',
 'Sources</div>\n<ul>\n'
 '<li><b>&#9679; New at 2:44 &mdash; the 2:40 trending strip, the Tuesday recap, breadth, the VIX close, consumer confidence, Case-Shiller and the Bessent report:</b> '
 '<a href="https://finance.yahoo.com/markets/stocks/articles/stock-market-news-aug-26-130500595.html">Yahoo Finance / Zacks Equity Research, &ldquo;Stock Market News for '
 'Aug 26, 2026&rdquo; (published 9:05&nbsp;a.m. EDT, Aug&nbsp;26, 2026)</a> &mdash; fetched in full; the source for <b>ANF $153.40 / &plus;40.86%</b>, <b>XPON $8.86 / '
 '&plus;68.12%</b>, <b>INTU $339.41 / &minus;5.05%</b>, <b>CRE $6.18 / &plus;140.47%</b>, the Tuesday index closes, the <b>15.45 VIX close</b>, and the ~12:05&nbsp;p.m. '
 'commodity board. <b>&#9888; Its index board and its trending strip are separately cached and are treated here as two different reads.</b></li>\n'
 '<li><b>&#9679; New at 2:44 &mdash; the 1:25 four-index board and the earlier trending strip:</b> '
 '<a href="https://finance.yahoo.com/markets/live/earnings-live-updates-q2-nvidia-115314802.html">Yahoo Finance, &ldquo;Earnings live updates: Abercrombie &amp; Fitch stock '
 'jumps on earnings beat, guidance raise&rdquo;</a> &mdash; fetched in full; the source for <b>S&amp;P 7,674.09</b>, <b>Dow 53,469.42</b>, <b>Nasdaq 26,101.79</b>, '
 '<b>Russell 3,003.81</b>, <b>VIX 15.55</b>, and the FactSet figure that S&amp;P&nbsp;500 Q2 earnings are on pace to <b>rise 50% year over year, the highest growth rate '
 'since 2021</b>.</li>\n'
 '<li><b>&#9679; New at 2:44 &mdash; the Abercrombie fundamentals and the 52-week high:</b> '
 '<a href="https://markets.financialcontent.com/stocks/article/stockstory-2026-8-26-abercrombie-and-fitch-anf-stock-trades-up-here-is-why">StockStory via FinancialContent, '
 '&ldquo;Abercrombie and Fitch (ANF) Stock Trades Up, Here Is Why&rdquo; (12:55&nbsp;p.m. EDT, Aug&nbsp;26, 2026)</a> &mdash; the source for <b>$1.27&nbsp;billion net sales</b>, '
 '<b>EPS $4.17 vs $1.99</b>, the <b>$100&nbsp;million tariff refund / $1.75 per share</b>, <b>62.4% gross margin</b>, the raised guidance, and the <b>$144.81</b> 52-week high. '
 'The same page carried the CloudQuote table behind <b>NVDA $209.99</b>, <b>ORCL $148.19</b> and <b>AMD $483.88</b>.</li>\n'
 '<li><b>&#9679; New at 2:44 &mdash; the PCE detail:</b> '
 '<a href="https://www.cnbc.com/2026/08/26/feds-preferred-inflation-gauge-shows-core-prices-rose-3point3percent-annually-in-july.html">CNBC, &ldquo;Fed&rsquo;s preferred '
 'inflation gauge shows core prices rose 3.3% annually in July&rdquo;</a>, with '
 '<a href="https://www.cbsnews.com/news/july-pce-inflation-index-federal-reserve/">CBS News</a> and '
 '<a href="https://us.cnn.com/2026/08/26/economy/pce-consumer-spending-inflation-july">CNN Business</a> &mdash; <b>core PCE 0.2% m/m and 3.3% y/y, in line</b>; headline '
 '<b>0.2% and 3.7%</b>, each a tenth above consensus; <b>consumer spending stalled</b>.</li>\n'
 '<li><b>&#9679; New at 2:44 &mdash; the DKS rejection:</b> '
 '<a href="https://seekingalpha.com/news/4636761-dicks-sporting-goods-plunges-31-after-earnings-miss">Seeking Alpha</a>, '
 '<a href="https://www.schaeffersresearch.com/content/news/2026/08/25/dicks-sporting-goods-stock-on-track-for-worst-day-ever">Schaeffer&rsquo;s Investment Research (Aug&nbsp;25)</a> '
 'and <a href="https://www.fool.com/investing/2026/08/25/why-dicks-sporting-goods-stock-crashed-today/">The Motley Fool (Aug&nbsp;25)</a> &mdash; all placing the '
 'DICK&rsquo;S collapse on <b>Tuesday</b>, which is why the &minus;30.68% strip figure is not published as a Wednesday move.</li>\n', 'ws-sources')

# 9. TLDR.
m = re.search(r'(<div class="tldr"><b>The Tape</b>\s*<span>)(.*?)(</span></div>)', w, re.S)
assert m, 'ws tldr not found'
w = w[:m.start(2)] + (
 'The day&rsquo;s clearest finding is a methodological one &mdash; a single Yahoo page serves its index board and its trending strip from separate caches, '
 'and at 2:40&nbsp;p.m. ET they sat two and a half hours apart &mdash; while the later of the two shows <b>Abercrombie &amp; Fitch extending to &plus;40.86%</b>, the '
 'biggest move anyone has numbered today, on a beat in which roughly $100&nbsp;million of tariff refunds supplied $1.75 of the $4.17 EPS; the 1:25 four-index board has the '
 'S&amp;P &minus;0.04%, the Dow &minus;0.20%, the Nasdaq &minus;0.19% and the Russell &minus;0.21%, all reconciling; <b>Nvidia has slipped under $210 at &minus;1.44% going '
 'into its own after-the-bell print</b>; and the DICK&rsquo;S Sporting Goods collapse circulating in a stale strip is Tuesday&rsquo;s news, rejected here as a Wednesday mover.'
) + w[m.end(2):]
wr('wallstreet-briefing.html', w)

# --------------------------------------------------------------------- CYBER
c = rd('cyber-briefing.html')
c = c.replace('<span class="tag new">New &middot; 1:40</span>', '<span class="tag">Carried &middot; 1:40 edition</span>')
c = c.replace('&#9679; New at 1:40 &mdash;', '&#9679; Carried from the 1:40 edition &mdash;')

c = once(c, '<tr><td>CVE-2026-66152</td>',
 '<tr><td>CVE-2026-19490 <span class="tag new">New &middot; 2:44</span></td><td>9.3 (CVSS v4.0, Citrix advisory CTX696939 via Rapid7)</td>'
 '<td>NetScaler ADC &amp; NetScaler Gateway 14.1 before 14.1-73.32; 13.1 before 13.1-63.21; NetScaler ADC FIPS before 14.1-73.32 FIPS; FIPS/NDcPP before 13.1-37.277</td>'
 '<td>Critical authentication bypass on appliances configured as <b>gateway or AAA virtual servers</b>. Exploitable remotely by an <b>unauthenticated</b> attacker over the '
 'network, with <b>no user interaction and no privileges</b>. Advisory published <b>Aug&nbsp;19, 2026</b>. Citrix says operators can test exposure by inspecting the '
 'configuration for <code>add authentication samlAction</code> together with <code>add authentication vserver</code> or <code>add vpn vserver</code> entries &mdash; if those '
 'are present on an affected build, the system is likely exploitable. <b>&#9888; As of Aug&nbsp;19 Rapid7 had not observed in-the-wild exploitation</b>, and none is asserted '
 'here; Rapid7 nonetheless urges emergency patching because perimeter Citrix appliances &ldquo;are nearly always exploited by threat actors.&rdquo; '
 '<b>Not in KEV, so no federal deadline.</b> &#9888; This is a distinct flaw from CVE-2026-3055, the earlier NetScaler SAML issue this desk carries at an official Citrix '
 '9.3; the two share a vendor, a product line and a score, and are not to be merged.</td></tr>\n'
 '<tr><td>CVE-2026-66152</td>', 'cy-cve')

m = re.search(r'(<div class="tldr"><b>The Wire</b>\s*<span>)(.*?)(</span></div>)', c, re.S)
assert m, 'cy tldr not found'
c = c[:m.start(2)] + (
 'Boston Scientific&rsquo;s 8-K still leads &mdash; a cyber incident the company itself says has disrupted <b>its ability to process and ship customer orders worldwide</b>, '
 'with no threat actor, ransomware family, CVE or intrusion vector named &mdash; and the one genuinely new item this run is <b>CVE-2026-19490</b>, a <b>CVSS&nbsp;9.3</b> '
 'authentication bypass in Citrix NetScaler ADC and Gateway that is not yet known to be exploited but sits on exactly the kind of internet-facing appliance that historically '
 'is; Patch Priority is unchanged, with the miniOrange WordPress SSO pair under live opportunistic scanning and federal deadlines for Oracle (Aug&nbsp;27) and Gitea '
 '(Aug&nbsp;28) now inside 48 hours, and the KEV board holds at 14 rows with 10 past due for a ninth consecutive edition with no new CISA alert.'
) + c[m.end(2):]

c = once(c, 'CISA KEV &amp; federal deadlines</div>',
 'CISA KEV &amp; federal deadlines</div>\n'
 '<div class="note" style="margin-bottom:10px"><b>&#9679; New at 2:44 &mdash; still nothing new from CISA, for a ninth consecutive edition.</b> Searches this run for KEV '
 'additions surfaced no alert page later than the <b>August&nbsp;18</b> batch (CVE-2026-33824, CVE-2026-55040, CVE-2026-59310, CVE-2026-65400). '
 '<b>The board below therefore holds at 14 rows, 10 of them past due, and the Patch Priority deadlines above are unchanged and match it.</b> '
 '<b>&#9888; Deadlines under BOD 26-04 are risk-based and assigned per CVE</b> &mdash; the old flat three-week BOD 22-01 window is superseded, and every date on this board is '
 'the date CISA itself published for that CVE.</div>', 'cy-kev')
wr('cyber-briefing.html', c)

# ----------------------------------------------------------------------- MMA
m_ = rd('mma-briefing.html')
m_ = m_.replace('<span class="tag new">New &middot; 1:40</span>', '<span class="tag">Carried &middot; 1:40 edition</span>')
m_ = m_.replace('&#9679; New at 1:40 &mdash;', '&#9679; Carried from the 1:40 edition &mdash;')

m_ = once(m_, '<p class="note"><b>&#9679; Venue, re-confirmed this run.</b>',
 '<p><b>&#9679; New at 2:44 &mdash; a fifth line on the main event, and the venue is now settled from the primary source.</b> A LowKick report read this run gives the '
 '<b>consensus at Nurmagomedov &minus;500 / Song &plus;380</b>, which it converts to roughly an <b>80% market-implied chance for Nurmagomedov and near 20% for Song</b>, and '
 'characterises the market as pointing to <b>a controlled decision rather than a quick finish</b>. That is the fifth distinct rendering of this line carried on this page and '
 'the fifth to make Nurmagomedov a heavy favourite; all five are printed unmerged. <b>&#9679; The venue no longer rests on a secondary source.</b> <b>UFC.com&rsquo;s own '
 'announcement</b> names the building as the <b>Pudong Development Bank Shanghai Oriental Sports Center</b> &mdash; the full sponsored form of the Oriental Sports Center this '
 'page publishes &mdash; and confirms <b>Saturday, August&nbsp;29</b>, first fight <b>3&nbsp;p.m. CST</b> and main card <b>6&nbsp;p.m. CST</b>. '
 '<b>&#9888; The &ldquo;Shanghai Indoor Stadium&rdquo; rendering that has recurred in search results all week is rejected on the strength of that primary source.</b> '
 '<b>&#9888; One conflict is printed rather than resolved:</b> UFC.com&rsquo;s announcement ranks the pair <b>#3 Nurmagomedov and #5 Song</b>, which is what this page carries, '
 'while a separate summary read this run cites &ldquo;the latest Meta UFC rankings&rdquo; at <b>#2 and #6</b>. The official site&rsquo;s numbers are published; the other is '
 'recorded and not adopted.</p>\n'
 '<p class="note"><b>&#9679; Carried from the 1:40 edition &mdash; venue, re-confirmed.</b>', 'mma-odds')

m_ = once(m_, 'Around the sport</div>',
 'Around the sport</div>\n'
 '<ul class="bul" style="margin-bottom:6px"><li><b>&#9679; New at 2:44 &mdash; fight week has produced its theatre.</b> Song Yadong removed his shirt during the UFC Shanghai '
 'faceoff with Umar Nurmagomedov, per MiddleEasy and The Body Lock, both of which frame the staredown around the title shot understood to be waiting for the winner. '
 'Yahoo Sports separately carries video of the pair&rsquo;s first fight-week faceoff. <b>&#9888; No new bout, result, signing, ranking change or title change was reported in '
 'the sport between the 1:40 and 2:44 editions</b>, and the champions board below is unchanged for a <b>twenty-fourth consecutive edition</b>.</li></ul>', 'mma-around')

mm = re.search(r'(<div class="tldr"><b>Tale of the Tape</b>\s*<span>)(.*?)(</span></div>)', m_, re.S)
assert mm, 'mma tldr not found'
m_ = m_[:mm.start(2)] + (
 'Three days out from UFC Shanghai, the line on <b>Umar Nurmagomedov (20-1) vs. Song Yadong (23-9-1)</b> has now been read five different ways &mdash; &minus;470/&plus;360 at '
 'DraftKings, &minus;700/&plus;500 at BetOnline.ag, &minus;500/&plus;385, &minus;500/&plus;375 on the official UFC site, and now a consensus &minus;500/&plus;380 worth about '
 '80% implied &mdash; all published unmerged and all pointing the same way, for a 6:00&nbsp;a.m. EDT Saturday main event whose venue <b>UFC.com itself now confirms</b> as the '
 'Pudong Development Bank Shanghai Oriental Sports Center, settling a name that search results had been rendering wrong all week; nothing else moved in the sport this run, and '
 'the champions board is unchanged for a twenty-fourth consecutive edition.'
) + m_[mm.end(2):]

m_ = once(m_, 'Sources</div>\n<ul>\n',
 'Sources</div>\n<ul>\n'
 '<li><b>&#9679; New at 2:44 &mdash; the venue, the ranks and the start times, from the primary source:</b> '
 '<a href="https://www.ufc.com/news/ufc-returns-shanghai-pivotal-bantamweight-clash-between-3-umar-nurmagomedov-and-5-song-yadong">UFC.com, &ldquo;UFC returns to Shanghai with a '
 'pivotal bantamweight clash between #3 Umar Nurmagomedov and #5 Song Yadong&rdquo;</a> &mdash; the source for the <b>Pudong Development Bank Shanghai Oriental Sports Center</b>, '
 'the <b>#3 / #5</b> rankings and the <b>3&nbsp;p.m. / 6&nbsp;p.m. CST</b> start times.</li>\n'
 '<li><b>&#9679; New at 2:44 &mdash; the fifth odds line:</b> '
 '<a href="https://www.lowkickmma.com/umar-nurmagomedov-favourite-song-yadong-ufc-shanghai/">LowKick MMA, &ldquo;Umar Nurmagomedov heavy favourite over Song Yadong ahead of UFC '
 'Shanghai&rdquo;</a> &mdash; <b>&minus;500 / &plus;380</b>, roughly 80% / 20% implied.</li>\n'
 '<li><b>&#9679; New at 2:44 &mdash; fight week:</b> '
 '<a href="https://middleeasy.com/mma-news/song-yadong-umar-nurmagomedov-ufc-shanghai-faceoff-title-shot">MiddleEasy</a> and '
 '<a href="https://thebodylockmma.com/ufc/news-ufc/song-yadong-goes-shirtless-at-ufc-shanghai-faceoff-as-title-shot-looms/">The Body Lock</a> on the faceoff; '
 '<a href="https://sports.yahoo.com/articles/umar-nurmagomedov-not-taking-yadong-051748749.html">Yahoo Sports</a> on Nurmagomedov calling it &ldquo;not an easy fight.&rdquo;</li>\n',
 'mma-sources')
wr('mma-briefing.html', m_)

print('OK: all edits applied')
