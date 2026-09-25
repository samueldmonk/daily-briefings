import sys
p='/tmp/db_1790353991/'
def rep(s,a,b):
    assert s.count(a)==1,(a[:80],s.count(a)); return s.replace(a,b)
YL='https://finance.yahoo.com/markets/live/stock-market-today-friday-september-25-dow-sp-500-nasdaq-081738529.html'
INV='https://www.investopedia.com/market-update-akamai-stock-soars-on-11-billion-deal-with-anthropic-12140070'
OLD_T='As of 11:47 AM ET Friday the Dow was up about 0.3% while the S&amp;P 500 and Nasdaq hovered just above flat (Yahoo Finance), as oil slid on Iran&rsquo;s offer to reopen the Strait of Hormuz and Akamai jumped on an $11.6 billion Anthropic cloud deal.'
NEW_T='As of about 12:15 PM ET Friday stocks had extended their gains &mdash; the Dow up 0.86%, the Nasdaq 0.63% and the S&amp;P 500 0.53% (Yahoo Finance) &mdash; as oil fell nearly 3% on Iran&rsquo;s offer to reopen the Strait of Hormuz and Akamai rallied on an $11.6 billion Anthropic cloud deal.'
w=open(p+'wallstreet-briefing.html').read()
w=rep(w,OLD_T,NEW_T)
w=rep(w,'<h3>As of 11:47 AM ET: Dow up 0.3%, S&amp;P 500 and Nasdaq just above flat as oil slides on Iran&rsquo;s Hormuz offer</h3>',
 '<h3>As of ~12:15 PM ET: Dow up 0.86%, Nasdaq up 0.63%, S&amp;P 500 up 0.53% as oil slides on Iran&rsquo;s Hormuz offer</h3>')
w=rep(w,'Wall Street was trying to end a volatile week on a firmer note, though early gains had narrowed by late morning. As of 11:47 AM ET the Dow Jones Industrial Average was up about 153 points, or 0.3%, while the S&amp;P 500 and the Nasdaq Composite were only slightly above the flat line (Yahoo Finance).',
 'Wall Street is ending a volatile week on a firmer note, and after narrowing in late morning the gains widened again around midday. With about 3 hours 45 minutes left in the session (about 12:15 PM ET), Yahoo Finance&rsquo;s quote strip showed the Dow Jones Industrial Average up about 442 points, or 0.86%, the Nasdaq Composite up 0.63% and the S&amp;P 500 up 0.53%; the Russell 2000 was up just 0.10%, and the Cboe Volatility Index was down 3.51% at 15.12. Earlier, at 11:47 AM ET, the Dow had been up only 0.3% with the S&amp;P 500 and Nasdaq barely above flat (Yahoo Finance).')
w=rep(w,'The lift came from oil: WTI crude fell 2.34% to $92.54 around the open (Schwab)',
 'The lift came from oil: November WTI crude was down 2.80% at $91.96 at midday (Yahoo Finance), after falling 2.34% to $92.54 around the open (Schwab),')
w=rep(w,'Intraday index moves are Yahoo Finance&rsquo;s 11:47 AM ET reading &mdash; still the latest time-stamped index reading found at this 12:03 PM ET refresh (later fetches returned cached pages); no index levels are published until the official close.',
 'Intraday index moves are from Yahoo Finance&rsquo;s quote strip fetched at this 12:33 PM ET refresh, which read &ldquo;U.S. markets close in 3h 45m&rdquo; (about 12:15 PM ET); the point changes are consistent with Thursday&rsquo;s official closes. No index levels are published until the official close.')
# Akamai card
w=rep(w,'<span class="tag good">+15.3% pre-mkt</span><h3>Akamai Technologies (AKAM)</h3><p>Surged 15.31% in premarket trading (TheStreet) and was up almost 17% early (Schwab)',
 '<span class="tag good">+8% mid-morning</span><h3>Akamai Technologies (AKAM)</h3><p>Surged 15.31% in premarket trading (TheStreet) and was up almost 17% early (Schwab), then pared the gain to 8% at $119 by around 10 AM ET (Investopedia)')
w=rep(w,'Piper Sandler raised its price target to $158 from $125 (Yahoo Finance). Reported premarket gains varied widely across outlets.',
 'Piper Sandler raised its price target to $158 from $125 (Yahoo Finance). JPMorgan lifted its target to $167 from $158 but stayed neutral, noting Anthropic accounts for some 93% of the $14.4 billion in new deals Akamai has signed this year; Oppenheimer reiterated outperform with a $180 target (Investopedia). Reported premarket gains varied widely across outlets.')
w=rep(w,'All moves are premarket or early-session readings and may differ materially by the close. These movers were first reported in the 11:46 AM edition and are carried with re-fetched sources.',
 'All moves are premarket or early-session readings and may differ materially by the close. These movers were first reported in the 11:46 AM edition; Akamai&rsquo;s later reading was added at 12:33 PM ET.')
w=rep(w,'<a href="https://finance.yahoo.com/markets/stocks/articles/akamai-anthropic-deal-magnitude-impressive-123738801.html" style="color:var(--acc2)">Yahoo Finance (Piper Sandler)</a></p>',
 '<a href="https://finance.yahoo.com/markets/stocks/articles/akamai-anthropic-deal-magnitude-impressive-123738801.html" style="color:var(--acc2)">Yahoo Finance (Piper Sandler)</a> &middot; <a href="'+INV+'" style="color:var(--acc2)">Investopedia (Akamai, ~10 AM)</a></p>')
w=rep(w,'Akamai, up almost 17% early on its Anthropic deal (Schwab), is the largest move among the large-cap stocks cited in this edition&rsquo;s sources.',
 'Akamai, up almost 17% early on its Anthropic deal (Schwab) before paring to about 8% (Investopedia), is the largest move among the large-cap stocks cited in this edition&rsquo;s sources.')
w=rep(w,'Early Friday the Cboe Volatility Index stood at 15.22, down 2.87% (Schwab).',
 'Early Friday the Cboe Volatility Index stood at 15.22, down 2.87% (Schwab); by about 12:15 PM ET it was 15.12, down 3.51% (Yahoo Finance).')
w=rep(w,'<tr><td>WTI Crude</td><td>$92.54 (&minus;2.34%)</td><td>Schwab, 9:13 AM; TheStreet had $92.89 (&minus;1.82%) at 7 AM</td></tr>',
 '<tr><td>WTI Crude (Nov)</td><td>$91.96 (&minus;2.80%)</td><td>Yahoo Finance quote strip, ~12:15 PM ET; $92.54 (&minus;2.34%) at 9:13 AM (Schwab)</td></tr>')
w=rep(w,'<tr><td>Gold</td><td>$4,335.70 (+0.86%)</td><td>Schwab, 9:13 AM</td></tr>',
 '<tr><td>Gold</td><td>$4,330.60 (+0.76%)</td><td>Yahoo Finance quote strip, ~12:15 PM ET; $4,335.70 (+0.86%) at 9:13 AM (Schwab)</td></tr>')
w=rep(w,'&middot; <a href="https://finance.yahoo.com/markets/stocks/articles/akamai-anthropic-deal-magnitude-impressive-123738801.html" style="color:inherit">Yahoo Finance (Akamai/Piper Sandler)</a>',
 '&middot; <a href="https://finance.yahoo.com/markets/stocks/articles/akamai-anthropic-deal-magnitude-impressive-123738801.html" style="color:inherit">Yahoo Finance (Akamai/Piper Sandler)</a> &middot; <a href="'+INV+'" style="color:inherit">Investopedia (Akamai)</a>')
open(p+'wallstreet-briefing.html','w').write(w)
i=open(p+'index.html').read()
i=rep(i,OLD_T,NEW_T)
open(p+'index.html','w').write(i)
print('ok')
