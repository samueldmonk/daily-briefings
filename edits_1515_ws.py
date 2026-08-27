# -*- coding: utf-8 -*-
p='wallstreet-briefing.html'
s=open(p,encoding='utf-8').read()
def rep(old,new,label):
    global s
    assert old in s, "NOT FOUND: "+label
    assert s.count(old)==1, "NOT UNIQUE: "+label
    s=s.replace(old,new,1); print("ok:",label)

rep('Nvidia is now quoted up 9.3% on the day and is credited with pushing the Nasdaq Composite up 1.51% by itself, the S&amp;P 500 is holding the 0.8% gain Bloomberg timestamped at 1:25 PM ET with technology the only sector advancing, and the Dow is up about 0.4%.',
'A live tracker timestamped at 3:05 PM ET has the Dow up just 0.15% and the Nasdaq Composite up 1.32%, both below the reads this page carried at 2:41, and the breadth behind the rally is now numeric as well as anecdotal: the technology sector ETF is up 2.3% while ten of the eleven S&amp;P 500 sectors are lower, led down by healthcare, utilities and consumer staples.',
'W1 tldr')

rep('<span class="tag new">Updated · 2:41 PM ET</span><span class="tag acc">Midday session</span><span class="tag">Carried · 2:21 PM ET</span><span class="tag">Carried · 12:38 PM ET</span>',
'<span class="tag new">Updated · 3:15 PM ET</span><span class="tag acc">Late session</span><span class="tag">Carried · 2:41 PM ET</span><span class="tag">Carried · 2:21 PM ET</span><span class="tag">Carried · 12:38 PM ET</span>',
'W2 lead tags')

rep("Nvidia alone is credited with the Nasdaq's 1.51% gain, and technology is carrying the tape by itself — as of ~2:41 PM ET",
"The Dow's gain has shrunk to 0.15% and ten of eleven sectors are red — the rally is one sector wide, as of ~3:15 PM ET",
'W3 lead h3')

NEWLEAD = ('<p style="margin:0 0 10px"><b>New at 3:15 — the second time-stamped cash-session read of the day, and the tape is lower than it was at 2:41.</b> '
'A live market tracker quotes, <b>at 3:05 PM ET</b>, the <b>Dow up 0.15%</b>, the <b>Nasdaq Composite up 1.32%</b> and <b>Nvidia up 8.34%</b>. '
'All three sit <b>below</b> the figures this page carried forty minutes earlier — 0.4%, 1.51% and 9.3% — so on the only two reads today that carry a clock, '
'the advance is narrower late in the session than it was after lunch. <span style="color:var(--mut)">This is the second time-stamped read of the cash session; the first was Bloomberg’s '
'1:25 p.m. S&amp;P 500 figure. Between them they are the only two figures on this page whose moment is known rather than inferred, which is why the comparison is drawn between '
'these two rather than against the undated roundups. <b>The 2:41 reads are not withdrawn</b> — they are kept below as the record of where the tape was then. '
'No point changes accompanied the 3:05 quotes and none is invented, and <b>no S&amp;P 500 figure was attached to that timestamp</b>, so the S&amp;P line is not restated as a 3:05 read.</span></p>\n'
'<p style="margin:0 0 10px"><b>New at 3:15 — the breadth question is answered with numbers at last, and the answer is that the rally is one sector wide.</b> '
'A mid-morning market note puts the <b>technology sector ETF (XLK) up 2.3%</b> while <b>ten of the eleven S&amp;P 500 sectors are lower</b>, led down by the defensives — '
'<b>healthcare, utilities and consumer staples</b>. <span style="color:var(--mut)">That XLK figure is the <b>first read of an actual S&amp;P sector</b> this page has been able to print today; '
'the two semiconductor ETFs it has been carrying are industry proxies, not sectors, and the sector note further down has been rewritten rather than left standing. '
'The figure is dated <b>mid-morning</b> by its own source and is labelled as such here, not passed off as a 3 PM reading. A separate piece, date-stamped August 28 and carrying no time, '
'reports the <b>S&amp;P 500 up 0.58% while the equal-weight index falls 0.16%</b> and credits <b>Nvidia with adding about $435 billion</b> in market value; because that source dates itself '
'after the session it describes, its figures are attributed here and <b>not treated as a close</b>, in line with how this page has handled two other date-slipped sources today. '
'What the two notes have in common, and what this page will assert, is the direction: the cap-weighted index is up and the average stock is not.</span></p>\n'
'<p style="margin:0 0 10px"><b>New at 3:15 — an intraday level that actually reconciles.</b> Trading Economics quotes the <b>US500 at 7,727, up 0.67%</b>. '
'Applied to Wednesday’s verified close of <b>7,675.70</b>, that percentage implies <b>7,727.1</b> — so for the first time today a level, a percentage and the prior close agree to the decimal. '
'<span style="color:var(--mut)">It is printed here for that reason and no other. It carries no timestamp, so it is not asserted as the level right now, and it is not promoted into the '
'Weekly Scorecard, which holds official closes only. It also gives this page a fourth distinct S&amp;P 500 read for the session — 0.4%, 0.8%, 0.58% and 0.67% — with no two of them '
'necessarily describing the same moment.</span></p>\n')

rep('<p style="margin:0 0 10px"><b>New at 2:41 — the first read of the day that ties a single stock to an index move.</b>',
NEWLEAD+'<p style="margin:0 0 10px"><b>At 2:41 — the first read of the day that tied a single stock to an index move.</b>',
'W4 insert new lead paras')

rep('The S&amp;P 500 and Dow are unchanged from the 2:21 read at about 0.8% and 0.4%, and are not restated here as if they were re-fetched levels.',
'The S&amp;P 500 and Dow were unchanged from the 2:21 read at about 0.8% and 0.4% at that point, and were not restated as if they were re-fetched levels. <b>The 3:05 read above has since put the Dow at 0.15%</b>, which is why that paragraph, and not this one, carries the current Dow figure.',
'W4b retense')

rep('near-60-year low of <b>189,000</b> in mid-July.',
'near-60-year low of <b>189,000</b> in mid-July. <b>New at 3:15 — the forecast is sourced now too:</b> economists had looked for roughly <b>208,000</b>, so the print is a modest downside surprise on claims, which is the good direction.',
'W5 jobless forecast')

rep('The two sector proxies quoted in sources this run — the VanEck Semiconductor ETF at <b>+3.5%</b> and the iShares Semiconductor ETF at <b>+3%</b> — remain the only numeric sector reads printed here, and both date from before the open.',
'<b>Rewritten at 3:15.</b> For most of today this note said the two semiconductor ETFs quoted in sources — VanEck at <b>+3.5%</b> and iShares at <b>+3%</b>, both dating from before the open — were the only numeric sector reads on the page. <b>That is no longer true, and the sentence is replaced rather than quietly amended:</b> a mid-morning note puts the <b>technology sector ETF (XLK) up 2.3%</b> with <b>ten of eleven S&amp;P 500 sectors lower</b>, led down by <b>healthcare, utilities and consumer staples</b>. The semiconductor figures are industry proxies; XLK is the first genuine sector return this page has printed today, and it is dated mid-morning by its source rather than presented as current.',
'W6 sector note')

rep('<h2 class="sec">Movers &amp; Drivers</h2>\n<div class="cards">\n',
'<h2 class="sec">Movers &amp; Drivers</h2>\n<div class="cards">\n'
'<div class="card"><span class="tag new">New &middot; 3:15</span><span class="tag acc">Highest reads yet</span>\n'
'<h3>Salesforce and CrowdStrike are quoted higher than at any point today — and every earlier read stays on the page</h3>'
'<p><b>New at 3:15:</b> two roundups for August 27 put <b>Salesforce up 22.68%</b> and <b>CrowdStrike up 19.67%</b>; a third has the pair at <b>22.75%</b> and <b>19.75%</b>. '
'Both names are now quoted above every figure this page has carried for them. The ladders, none averaged and none withdrawn: <b>Salesforce</b> at <b>14.78%</b> (9:35), '
'<b>11.2%</b> (11:35, 12:05 and again in this run’s coverage), <b>21.04%</b> (12:38), <b>10.4%</b> (2:21) and now <b>22.68%</b> and <b>22.75%</b>; <b>CrowdStrike</b> at <b>8.9%</b> pre-open, '
'<b>14.34%</b> (9:35), <b>9%</b> (11:35, 2:21 and again in this run’s coverage), <b>9.4%</b> (12:05), <b>17.93%</b> (12:38) and now <b>19.67%</b> and <b>19.75%</b>. '
'<span style="color:var(--mut)"><b>The spread on these two names is the widest on the page</b> — roughly twelve points on Salesforce and eleven on CrowdStrike between the lowest and '
'highest read of the same session — and the low reads and the high reads came back <i>in the same run</i> this afternoon rather than in sequence. That rules out simple intraday drift as the '
'explanation, and it is why <b>this page asserts none of them as the move</b>. It prints what each source said and leaves the disagreement visible.</span></p></div>\n'
'<div class="card"><span class="tag new">New &middot; 3:15</span><span class="tag acc">Semis</span>\n'
'<h3>Nvidia at 8.34% — the first read of the day that comes in <i>below</i> the range, and it carries a clock</h3>'
'<p><b>New at 3:15:</b> a live tracker quotes <b>NVDA up 8.34% at 3:05 PM ET</b>. Every cash-session read before it sat between 5.87% and 9.48%, and the two most recent were 9% and 9.3%, '
'so this is the first Nvidia quote today that lands <b>under</b> the prevailing afternoon band rather than inside or above it — and, unlike almost all of them, it says which moment it describes. '
'<span style="color:var(--mut)">Read against Bloomberg’s 1:25 p.m. figure of about 7% and Yahoo’s 9.3% at 2:41, the honest summary is that Nvidia has held a gain somewhere between roughly '
'7% and 9.5% all afternoon with no clear trend inside that band. No point change or price level accompanied the 8.34% quote and none is printed.</span></p></div>\n',
'W7 movers cards')

rep('<footer><b style="color:var(--ink)">Sources</b><ul class="bul"><li><b>Fetched 2:41 PM ET</b>',
'<footer><b style="color:var(--ink)">Sources</b><ul class="bul">'
'<li><b>Fetched 3:15 PM ET</b> — StockMarketWatch, <a href="https://stockmarketwatch.com/live/stock-market-today">Tech Sector Surges as Nvidia and Semiconductors Lead</a> — at 3:05 PM EDT: Dow +0.15%, Nasdaq Composite +1.32%, NVDA +8.34%.</li>'
'<li><b>Fetched 3:15 PM ET</b> — Investrade, <a href="https://investrade.com/mid-morning-look-august-27-2026/">Mid-Morning Look: August 27, 2026</a> — XLK +2.3%; ten of eleven S&amp;P sectors lower, led by healthcare, utilities and consumer staples.</li>'
'<li><b>Fetched 3:15 PM ET</b> — Eastern Herald, <a href="https://easternherald.com/2026/08/28/sp-500-today-august-27-2026/">S&amp;P 500 Today, August 27, 2026: NVIDIA Adds $435bn as the Average Stock Falls</a> — S&amp;P 500 +0.58% against the equal-weight index −0.16%; date-stamped Aug 28, no time given, not treated here as a close.</li>'
'<li><b>Fetched 3:15 PM ET</b> — TheStreet, <a href="https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-27-2026">Stock Market Today (Aug. 27, 2026)</a> — Salesforce +22.68%, CrowdStrike +19.67%, Okta +17.4%.</li>'
'<li><b>Fetched 3:15 PM ET</b> — Trading Economics, <a href="https://tradingeconomics.com/united-states/stock-market">United States Stock Market Index</a> — US500 quoted at 7,727, +0.67%, which reconciles to Wednesday’s verified 7,675.70 close.</li>'
'<li><b>Fetched 3:15 PM ET</b> — Brisk Markets, on DOL data, <a href="https://www.briskmarkets.com/blog/initial-jobless-claims-fall-more-than-expected/">Initial Jobless Claims Fall More Than Expected</a> — 203,000 for the week ending Aug 22 against roughly 208,000 expected; prior week revised 206,000 to 207,000; four-week average 205,500.</li>'
'<li><b>Fetched 2:41 PM ET</b>',
'W8 sources')

open(p,'w',encoding='utf-8').write(s)
print("WROTE",p,len(s))
