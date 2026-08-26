#!/usr/bin/env python3
# Wall Street incremental edits — 10:55 a.m. ET edition, Wed Aug 26 2026
import sys, io, re
P = sys.argv[1] if len(sys.argv) > 1 else '.'
f = P + '/wallstreet-briefing.html'
h = io.open(f, encoding='utf-8').read()
n = 0
def rep(old, new, cnt=1):
    global h, n
    assert h.count(old) >= 1, 'MISSING: ' + old[:110]
    h = h.replace(old, new, cnt); n += 1

# ---------- 1. demote old New tags ----------
rep('<span class="tag new">New &middot; 10:20</span>',
    '<span class="tag">Carried &middot; 10:20 edition</span>', 99)

# ---------- 2. TLDR ----------
rep('<div class="tldr"><b>The Tape</b> <span><b>Meta has settled the states&rsquo; social-media addiction case for about $16.7&nbsp;billion</b> &mdash; the single-name story of an otherwise flat, sticky-inflation Wednesday in which July PCE ran <b>a tenth hot on the headline</b> and <b>exactly on forecast at the core</b>, and the tape marks time in front of <b>Nvidia&rsquo;s report at 4:20&nbsp;p.m. ET</b>.</span></div>',
    '<div class="tldr"><b>The Tape</b> <span>The session has printed and it is barely moving &mdash; <b>S&amp;P&nbsp;500 +0.12%, Nasdaq +0.08%, Dow +0.03%, Russell&nbsp;2000 &minus;0.08%</b> on a Yahoo Finance board whose own countdown places it at <b>~9:59&nbsp;a.m. ET</b>, all four reconciling exactly against Tuesday&rsquo;s closes &mdash; while <b>Abercrombie &amp; Fitch is the day&rsquo;s outlier at +30.85%</b> on a raised guide, Meta&rsquo;s <b>~$16.7&nbsp;billion</b> settlement carries the news, and everything waits on <b>Nvidia at 4:20&nbsp;p.m. ET</b>.</span></div>')

# ---------- 3. ticker tape: SMTC -> ANF ----------
rep('{"proName":"NASDAQ:SMTC","title":"Semtech"}', '{"proName":"NYSE:ANF","title":"Abercrombie"}')

# ---------- 4. The Lead: headline + new verified-print paragraph ----------
rep('<h2>Meta writes a $16.7&nbsp;billion cheque &mdash; and as of this <i>~10:20&nbsp;a.m. ET</i> edition the rest of the tape is marking time into Nvidia night</h2>',
    '<h2>The tape finally prints &mdash; four indices, four reconciled reads, and almost no movement in any of them as of <i>~9:59&nbsp;a.m. ET</i></h2>\n'
    '<p><b>This edition retires the refusal that ran on this page all morning.</b> Every earlier Wednesday edition declined to publish an index level, because no source stated one against a stated clock time. That standard is now met. A Yahoo Finance quote board carried on the TheStreet syndication of <b>&ldquo;Stock Market Today (Aug. 26, 2026)&rdquo;</b> &mdash; bylined <b>Rob Lenihan</b> and stamped <b>9:43&nbsp;a.m. EDT</b> &mdash; returned a full board whose own header reads <b>&ldquo;U.S. markets close in 6h 1m,&rdquo;</b> which places the board at <b>approximately 9:59&nbsp;a.m. ET</b>. It reads: <b>S&amp;P&nbsp;500 7,686.64, +9.36, +0.12%</b>; <b>Dow&nbsp;30 53,594.69, +17.29, +0.03%</b>; <b>Nasdaq 26,173.36, +22.06, +0.08%</b>; <b>Russell&nbsp;2000 3,007.66, &minus;2.36, &minus;0.08%</b>. <b>All four reconcile exactly</b> against the Tuesday closes already published in the Weekly Scorecard below &mdash; subtract each change from each level and you land on 7,677.28, 53,577.40, 26,151.30 and 3,010.02 to the cent, and each percentage matches its own points-over-prior-close arithmetic. That is the three-way test this page requires, and it passes on all four indices.</p>\n'
    '<p><b>&#9888; A search summary read this run gave the opposite signs and is rejected.</b> It described the S&amp;P&nbsp;500 as having <i>slipped</i> 0.12%, the Dow <i>down</i> 0.08%, the Nasdaq <i>off</i> 0.16% and the Russell&nbsp;2000 <i>up</i> 0.50%. Three of those four contradict the fetched board on sign, and the Russell figure is Tuesday&rsquo;s close (+0.50%) rather than a Wednesday move. <b>The fetched, self-reconciling board is what is published; the summary is not.</b> <b>&#9888; The board is a cached render</b> &mdash; its countdown is roughly fifty minutes behind the clock at the time of this edition &mdash; so it is published as a <i>9:59&nbsp;a.m.</i> print and not as a live quote. The widgets above carry live.</p>\n'
    '<h3 style="margin:18px 0 6px">Meta writes a $16.7&nbsp;billion cheque, and it is still the news of the morning</h3>')

# ---------- 5. remove the now-superseded "no opening level" sentence ----------
rep('<b>No opening level for any index is published in this edition</b>, because no source fetched this run states one against a stated clock time; the live quote widgets above carry the actual tape.',
    '<b>Those direction-only reads are now superseded by the reconciled ~9:59&nbsp;a.m. board at the top of this section</b>, which supplies the levels this page had been withholding; they are left standing above as the record of what the morning looked like before a number could be confirmed.')

# ---------- 6. new movers cards (insert at top of the cards list) ----------
rep('<div class="lab">Movers &amp; drivers</div>\n<div class="cards">\n<div class="card">',
    '<div class="lab">Movers &amp; drivers</div>\n<div class="cards">\n'
    '<div class="card">\n<div class="tags"><span class="tag new">New &middot; 10:55</span><span class="tag">+30.85%</span><span class="tag">Retail</span></div>\n'
    '<h3>Abercrombie &amp; Fitch is the day&rsquo;s move, and it is not close</h3>\n'
    '<p>On the same ~9:59&nbsp;a.m. Yahoo board, <b>ANF stands at $142.50, up $33.59 or 30.85%</b> &mdash; the largest single-name move any source fetched this run puts a number on, and the first regular-session individual move this page has been able to publish today. The board&rsquo;s own arithmetic implies a prior close of <b>$108.91</b>; no source read this run states that close independently, so it is noted as implied rather than asserted.</p>\n'
    '<p><b>The quarter behind it.</b> Abercrombie reported <b>earnings of $4.17 a share against a $1.98 forecast</b> and <b>record second-quarter net sales of $1.27&nbsp;billion, up 5%</b> year on year. The company said about <b>$100&nbsp;million in tariff refunds</b> boosted the result, while adding that the core business also beat &mdash; both brands delivered record quarterly sales and Abercrombie returned to comparable-sales growth. Full-year guidance was raised to <b>$13.10&ndash;$13.60 a share on net sales growth of around 5%</b>, from <b>$10.20&ndash;$11.00 on growth of 3&ndash;5%</b>, and the company now expects <b>at least $500&nbsp;million of share repurchases in 2026</b>.</p>\n'
    '<p><b>&#9888; Five different renderings of the share reaction surfaced this run and none is merged into another.</b> RTTNews: <b>&ldquo;Shares Surge 8.3%.&rdquo;</b> StockStory, via FinancialContent: <b>&ldquo;Stock Jumps 11.9%.&rdquo;</b> A separate read: <b>&ldquo;rose over 11% in premarket trading.&rdquo;</b> Investing.com&rsquo;s earnings-call transcript headline: <b>&ldquo;stock jumps 17%.&rdquo;</b> And the Yahoo board above: <b>+30.85%</b>. Only the last of these carries a derivable clock time and reconciles against a prior close, which is why it is the one used in the Chart of the Day note; the other four are printed as found.</p></div>\n'
    '<div class="card">\n<div class="tags"><span class="tag new">New &middot; 10:55</span><span class="tag">Session</span><span class="tag">Reconciled</span></div>\n'
    '<h3>The indices themselves: green, but by hundredths</h3>\n'
    '<p>The first Wednesday index prints this page has been able to verify, all from the ~9:59&nbsp;a.m. board and all reconciling against Tuesday&rsquo;s closes: <b>S&amp;P&nbsp;500 +0.12% to 7,686.64</b>, <b>Nasdaq +0.08% to 26,173.36</b>, <b>Dow +0.03% to 53,594.69</b>, <b>Russell&nbsp;2000 &minus;0.08% to 3,007.66</b>. Three green, one red, none of them moving more than a tenth of a percent an hour and a half into the session.</p>\n'
    '<p>That is a market that has already priced the inflation print and has nothing left to do until 4:20&nbsp;p.m. <b>Chris Zaccarelli</b>, chief investment officer at <b>Northlight Asset Management</b>, put the reason plainly to TheStreet: while many of the PCE numbers came in worse than expected, the most important measure &mdash; core PCE &mdash; <b>&ldquo;held constant and that will give the Fed more time to leave rates on hold.&rdquo;</b> He also called it <b>&ldquo;an extremely busy week &ndash; especially for one in late August, when it is typically more quiet &ndash; with the largest company in the world reporting earnings this afternoon, a meaningful inflation data release this morning and a consequential speech from the Chair of the Federal Reserve, which is scheduled for Friday.&rdquo;</b></p></div>\n'
    '<div class="card">\n<div class="tags"><span class="tag new">New &middot; 10:55</span><span class="tag">&minus;3.39%</span><span class="tag">Software</span></div>\n'
    '<h3>Intuit&rsquo;s regular-session damage is a third of what the premarket implied</h3>\n'
    '<p>The ~9:59&nbsp;a.m. trending board has <b>INTU at $345.35, down $12.11 or 3.39%</b> &mdash; and $345.35 plus $12.11 is $357.46, Tuesday&rsquo;s close to the cent, so this is a clean Wednesday move. <b>&#9888; It is materially shallower than the &minus;11.8% premarket print to $315.30</b> this desk carried from Investing.com&rsquo;s 7:10&nbsp;a.m. wire, and shallower again than the 7%&ndash;9% band of Tuesday-night after-hours reads. Five snapshots of one repricing, published in sequence and not averaged; the regular-session figure is the one with a prior close behind it.</p>\n'
    '<p>Alongside it on the same board: <b>Kohl&rsquo;s (KSS) at $16.85, down $0.83 or 4.69%</b>, after second-quarter comparable sales fell <b>0.9%</b> &mdash; the premarket wire had put that decline at about 5%. <b>Oklo (OKLO) at $44.84, up $0.57 or 1.29%</b>, extending Tuesday&rsquo;s 11.54% gain. <b>Rezolve AI (RZLV) unchanged at $2.96</b>, exactly flat on the session.</p></div>\n'
    '<div class="card">')

# ---------- 7. Chart of the day -> ANF ----------
rep('{"symbol":"NASDAQ:INTU","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}',
    '{"symbol":"NYSE:ANF","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}')

i = h.find('<div class="note">The session is open, and <b>the largest single-name move')
j = h.find('</div>', h.find('not a Wednesday mover', i))
assert i > 0 and j > i
h = h[:i] + ('<div class="note">The chart now tracks <b>ANF</b>. With the session open and a reconciled quote board in hand, <b>the largest single-name move any source fetched this run puts a number on is Abercrombie &amp; Fitch at +30.85%, to $142.50</b>, on a raised full-year guide and a $4.17 quarter against a $1.98 forecast. That figure comes from the ~9:59&nbsp;a.m. ET Yahoo board and is a <i>regular-session</i> move, which is what this slot has been waiting for all morning &mdash; the earlier note here, which said no source stated a regular-session percentage move for any individual stock, is retired. <b>&#9888; Four lower readings of the same reaction (8.3%, 11.9%, &ldquo;over 11%&rdquo; premarket and 17%) are printed unmerged in Movers &amp; drivers above.</b> Intuit, which held this slot in the 10:20 edition on a &minus;11.8% premarket print, is running at <b>&minus;3.39%</b> in the regular session. The largest move on the most recent <i>completed</i> session was DICK&rsquo;S Sporting Goods at <b>&minus;30.68%</b> &mdash; that was <b>Tuesday</b>, and it is not a Wednesday mover.') + h[j:]
n += 1

# ---------- 8. rates & commodities: refresh to the 9:59 board ----------
rep('<tr><td>WTI crude (Oct contract)</td><td>$80.15</td><td class="down">&minus;$2.21 &nbsp;&minus;2.68%</td><td>~4:25 a.m. ET Wed (Yahoo)</td></tr>\n'
    '<tr><td>Gold</td><td>$4,682.80</td><td class="down">&minus;$11.70 &nbsp;&minus;0.25%</td><td>~4:25 a.m. ET Wed (Yahoo)</td></tr>\n'
    '<tr><td>Bitcoin (USD)</td><td>$78,998.81</td><td class="down">&minus;$907.00 &nbsp;&minus;1.14%</td><td>~4:25 a.m. ET Wed (Yahoo)</td></tr>\n'
    '<tr><td>VIX</td><td>15.67</td><td class="up">+0.22 &nbsp;+1.42%</td><td>~4:25 a.m. ET Wed (Yahoo)</td></tr>',
    '<tr><td>WTI crude (Oct contract)</td><td>$81.52</td><td class="down">&minus;$0.84 &nbsp;&minus;1.02%</td><td>~9:59 a.m. ET Wed (Yahoo)</td></tr>\n'
    '<tr><td>Gold</td><td>$4,680.70</td><td class="down">&minus;$13.80 &nbsp;&minus;0.29%</td><td>~9:59 a.m. ET Wed (Yahoo)</td></tr>\n'
    '<tr><td>Bitcoin (USD)</td><td>$78,410.76</td><td class="down">&minus;$222.59 &nbsp;&minus;0.28%</td><td>~9:59 a.m. ET Wed (Yahoo)</td></tr>\n'
    '<tr><td>VIX</td><td>15.51</td><td class="up">+0.06 &nbsp;+0.39%</td><td>~9:59 a.m. ET Wed (Yahoo)</td></tr>')

rep('The whole curve moved lower together on Tuesday as oil slid. <b>No federal funds target level is published here</b>',
    'The four non-Treasury rows above were refreshed this edition from the ~9:59&nbsp;a.m. ET board and replace the ~4:25&nbsp;a.m. readings carried since the pre-open editions; crude is <b>higher</b> than it was overnight ($81.52 against $80.15) while gold, bitcoin and the VIX have each drifted a little further from their overnight marks. The three Treasury rows are still Tuesday&rsquo;s, because no source fetched this run states a Wednesday yield. The whole curve moved lower together on Tuesday as oil slid. <b>No federal funds target level is published here</b>')

# ---------- 9. On the radar: add the Hathorn framing ----------
rep('<li><b>Nvidia reports at 4:20&nbsp;p.m. ET, with the earnings call at 5&nbsp;p.m.</b>',
    '<li><b>Why the whole tape is holding still.</b> <b>Daniela Hathorn</b>, senior market analyst at <b>Capital.com</b>, told TheStreet that Nvidia&rsquo;s report <b>&ldquo;is arguably bigger than a single-company earnings report given Nvidia&rsquo;s role as a barometer for the entire AI investment cycle&rdquo;</b> &mdash; with investors looking <b>&ldquo;beyond headline revenue and earnings towards data-center demand, margins, next-generation chip supply and, crucially, whether hyperscaler spending remains strong enough to justify the extraordinary amounts of capital flowing into AI infrastructure.&rdquo;</b> Her warning: <b>&ldquo;Expectations are extremely high, meaning even another strong quarter may need equally convincing guidance to sustain the rally.&rdquo;</b></li>\n'
    '<li><b>Nvidia reports at 4:20&nbsp;p.m. ET, with the earnings call at 5&nbsp;p.m.</b>')

# ---------- 10. Sources ----------
rep('<div class="lab">Sources</div>\n<ul>\n',
    '<div class="lab">Sources</div>\n<ul>\n'
    '<li><b>TheStreet, syndicated on Yahoo Finance &mdash; &ldquo;Stock Market Today (Aug. 26, 2026): S&amp;P 500 futures edge lower ahead Nvidia earnings&rdquo;</b> (Rob Lenihan, Wed, August&nbsp;26, 2026, 9:43&nbsp;a.m. EDT), <b>fetched in full this run</b> &mdash; the source for the reconciled index board (S&amp;P 7,686.64 / Dow 53,594.69 / Nasdaq 26,173.36 / Russell 3,007.66 and their point and percent changes), for the VIX, gold, bitcoin and crude rows now carried in the Rates table, for the trending-ticker levels on ANF, INTU, KSS, OKLO and RZLV, and for the Zaccarelli and Hathorn quotations. <b>&#9888; The page&rsquo;s own header reads &ldquo;U.S. markets close in 6h 1m,&rdquo;</b> which is how the ~9:59&nbsp;a.m. ET stamp on that board is derived; the render is cached and the board is published as a print at that time, not as a live quote.</li>\n'
    '<li><b>Abercrombie &amp; Fitch &mdash; second-quarter results</b>, via <b>Qz</b> (&ldquo;Abercrombie &amp; Fitch Q2 2026 earnings beat on tariff refunds&rdquo;), <b>RTTNews</b> (&ldquo;Abercrombie &amp; Fitch Boosts FY26 Outlook As Q2 EPS, Sales Rise; Shares Surge 8.3%&rdquo;), <b>StockStory / FinancialContent</b> (&ldquo;Beats On Revenue, Stock Jumps 11.9%&rdquo;) and <b>Investing.com</b> (earnings-call transcript, &ldquo;profit beats as stock jumps 17%&rdquo;) &mdash; sources for the $4.17 against $1.98, the record $1.27&nbsp;billion quarter, the ~$100&nbsp;million tariff refunds, the raised $13.10&ndash;$13.60 guide against the prior $10.20&ndash;$11.00, the &ge;$500&nbsp;million buyback plan, and the four lower share-reaction readings published unmerged. <b>Search summaries and headlines, not fetched in full.</b></li>')

io.open(f, 'w', encoding='utf-8').write(h)
print('wallstreet OK — %d edits' % n)
