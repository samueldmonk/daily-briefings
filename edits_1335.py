import re, sys
def rw(p, pairs, must=True):
    h=open(p, encoding='utf-8').read()
    for old,new in pairs:
        if old not in h:
            print("!! MISS in",p,":",old[:90]); sys.exit(1)
        h=h.replace(old,new,1)
    open(p,'w',encoding='utf-8').write(h)
    print("ok",p)

# ---------------- WALL STREET ----------------
ws_tldr_old = '<div class="tldr"><b>The Tape</b> <span>Chip and memory weakness is still setting the tone &mdash; the group gapped down on weekend reports Washington may let Apple buy memory from China&rsquo;s CXMT and YMTC &mdash; leaving the S&amp;P 500 off about 0.2%, the Nasdaq Composite off about 0.4% and the Dow up about 0.2% in early-afternoon trade, while Treasury Secretary Scott Bessent&rsquo;s Iran sanctions press conference begins at 1 p.m. ET and the bond market keeps refusing to reward his $1 trillion cash pile.</span></div>'
ws_tldr_new = '<div class="tldr"><b>The Tape</b> <span>Treasury Secretary Scott Bessent launched what he called Operation Economic Outcast at his 1 p.m. ET press conference &mdash; more than 60 Iran-linked entities, individuals and vessels sanctioned and secondary-sanctions risk broadened across digital assets, technology, gold, aviation and shipping &mdash; while the tape held the shape it has kept all day, with the S&amp;P 500 off 0.18%, the Nasdaq Composite off 0.40% and the Dow up 0.23% on chip and memory weakness, and crude sold off into the announcement.</span></div>'

ws_h2_old = '<h2>Chips keep the Nasdaq red as Bessent takes the podium &mdash; and the bond market keeps saying no</h2>'
ws_h2_new = '<h2>Bessent launches &ldquo;Operation Economic Outcast&rdquo; &mdash; and the tape barely moves</h2>'

ws_p1_old = '<p><b>As of roughly 1:15 p.m. ET.</b> The tape has settled into the shape it has held all day: blue chips up, semiconductors down, and nothing resolved until Nvidia reports on Wednesday. The Motley Fool&rsquo;s live index board, read at this edition, had the <b>S&amp;P 500 off about 0.2%</b>, the <b>Nasdaq Composite off about 0.4%</b> and the <b>Dow Jones Industrial Average up about 0.2%</b> &mdash; and for the first time today all three of those readings reconcile <em>exactly</em> against Friday&rsquo;s verified closes,'
ws_p1_new = '<p><b>As of roughly 1:35 p.m. ET.</b> The biggest headline of the day landed at the Treasury Building rather than on the tape, and the tape has barely acknowledged it: blue chips up, semiconductors down, and nothing resolved until Nvidia reports on Wednesday. The Motley Fool&rsquo;s live index board, re-read at this edition, had the <b>S&amp;P 500 off 0.18%</b>, the <b>Nasdaq Composite off 0.40%</b> and the <b>Dow Jones Industrial Average up 0.23%</b> &mdash; and, as at the previous edition, all three of those readings reconcile <em>exactly</em> against Friday&rsquo;s verified closes,'

ws_p2_old = 'The event risk is on the podium, not the tape. Treasury Secretary Scott Bessent holds his press conference detailing the new Iran sanctions package at <b>1 p.m. ET</b> at the Treasury Building &mdash; the time and venue fixed by CBS News&rsquo;s &ldquo;how to watch&rdquo; box &mdash; unveiling what The Washington Post describes as a wider range of secondary sanctions on countries and entities doing business with Iran, aimed at pressuring Tehran to reopen the Strait of Hormuz.'
ws_p2_new = 'The event risk has come off the podium. Treasury Secretary Scott Bessent held his press conference at the Treasury Building at <b>1 p.m. ET</b> and announced <b>Operation Economic Outcast</b> &mdash; in his words &ldquo;an unprecedented campaign against the Islamic Republic of Iran and its enablers,&rdquo; begun at President Trump&rsquo;s direction. Treasury&rsquo;s Office of Foreign Assets Control is sanctioning more than 60 entities, individuals and vessels accused of helping Iran procure nuclear and missile technology, run cyber operations or generate oil revenue, and the package widens secondary-sanctions exposure across what Bessent called &ldquo;five of Iran&rsquo;s most vital lifelines that it exploits in other countries &mdash; digital assets, technology, gold, aviation, and shipping.&rdquo; The stated aim is unchanged: pressure Tehran to reopen the Strait of Hormuz and end a war the administration originally said would last four to six weeks and which is now in its sixth month.'

ws_cards_anchor = '<div class="lab">Movers &amp; drivers — the overnight tape and the late morning</div>\n<div class="cards">\n'
ws_new_cards = ws_cards_anchor + '''
<div class="card">
<div class="tags"><span class="tag">Iran sanctions</span><span class="tag">Announced 1 p.m. ET</span><span class="tag new">New</span></div>
<h3>Bessent launches &ldquo;Operation Economic Outcast&rdquo;</h3>
<p><b>New this edition.</b> Treasury Secretary Scott Bessent used his 1 p.m. ET press conference at the Treasury Building to announce the campaign by name. &ldquo;Today, at President Trump&rsquo;s direction, the United States Treasury has begun Operation Economic Outcast, an unprecedented campaign against the Islamic Republic of Iran and its enablers,&rdquo; he said. Treasury&rsquo;s Office of Foreign Assets Control is sanctioning more than 60 entities, individuals and vessels accused of helping Iran procure nuclear and missile technology, conduct cyber operations or generate oil revenue. Bessent said the department had mapped the networks Iran uses to smuggle oil and evade sanctions &mdash; exchange houses, free-trade zones, banks, shipping registries and aviation links &mdash; and that the new measures &ldquo;broaden secondary sanctions risk for anyone foolish enough to continue conducting business with this regime.&rdquo; He gave countries still trading with Tehran a brief window to cut those relationships: &ldquo;If people do not want to meet our expectations than we expect, and they should expect that they will leave the dollar system.&rdquo; He added that President Trump was telephoning world leaders with specific requests to stop trading with the regime, and that &ldquo;any entity that facilitates money laundering on behalf of Iran will be removed from the U.S. dollar system.&rdquo; His summary of the intent: &ldquo;This is economic asphyxiation of this regime.&rdquo; CBS News headlined the remarks &ldquo;The clock just started ticking.&rdquo;</p>
</div>

<div class="card">
<div class="tags"><span class="tag down">WTI &minus;2.7%</span><span class="tag">Hormuz</span><span class="tag new">New</span></div>
<h3>Crude sells off into the announcement</h3>
<p><b>New this edition.</b> Oil fell on Monday as investors waited for the detail of what Washington billed as its toughest-ever sanctions campaign against Iran. CNBC put West Texas Intermediate futures down about <b>2.7% at $84.73</b> a barrel and Brent down <b>2.1% at $92.44</b>. The direction is the opposite of the reflex &mdash; a tighter squeeze on Iranian barrels reads as bullish on its face &mdash; and the supply picture is the reconciliation: the US military says it has helped tankers move more than 660 million barrels of crude through the Strait of Hormuz since early May, so the corridor has kept flowing through the conflict even as the rhetoric has escalated. Note that these CNBC figures sit below the earlier Investing.com quotes carried in the rates table further down this page; they are the fresher of the two readings and are attributed accordingly.</p>
</div>
'''

ws_drop = [
 ('<div class="tags"><span class="tag down">MRNA −7%</span><span class="tag">Profit-taking</span><span class="tag new">New</span></div>',
  '<div class="tags"><span class="tag down">MRNA −7%</span><span class="tag">Profit-taking</span></div>'),
 ('<div class="tags"><span class="tag down">Drones, quantum</span><span class="tag">Risk appetite</span><span class="tag new">New</span></div>',
  '<div class="tags"><span class="tag down">Drones, quantum</span><span class="tag">Risk appetite</span></div>'),
 ('<h3>Moderna gives back part of a 392% year</h3>\n<p><b>New this edition.</b> Moderna sank 7%',
  '<h3>Moderna gives back part of a 392% year</h3>\n<p>Moderna sank 7%'),
 ('<h3>The speculative complexes are unwinding together</h3>\n<p><b>New this edition.</b> The de-risking',
  '<h3>The speculative complexes are unwinding together</h3>\n<p>The de-risking'),
]

ws_wti_old = '<tr><td>WTI crude (Oct contract)</td><td>$85.93</td><td class="down">−1.13 (−1.30%) on Yahoo&rsquo;s market bar read this run;'
ws_wti_new = '<tr><td>WTI crude (Oct contract)</td><td>$84.73</td><td class="down">&minus;2.7% on CNBC&rsquo;s Monday oil report, the freshest attributed read at this edition; an earlier Yahoo market-bar read this run had $85.93, &minus;1.30%,'
ws_brent_old = '<tr><td>Brent crude</td><td>$91.30</td><td class="down">−1.37 (−1.48%) (Investing.com, this run).</td></tr>'
ws_brent_new = '<tr><td>Brent crude</td><td>$92.44</td><td class="down">&minus;2.1% on CNBC&rsquo;s Monday oil report, read at this edition; an earlier Investing.com quote this run had $91.30, &minus;1.48%. The two sources disagree on the level; the CNBC figure is the more recent and is the one carried here.</td></tr>'

ws_src_anchor = '<div class="lab">Sources</div>\n<ul>\n'
ws_src_new = ws_src_anchor + '''<li>CBS News — Bessent announces new economic sanctions against Iran: &ldquo;The clock just started ticking&rdquo; (Aug 24, 2026; article timestamped 12:06 PM ET, updated through the 1 p.m. ET press conference; fetched this run) — https://www.cbsnews.com/news/bessent-press-conference-iran-sanctions-economic-d-day/</li>
<li>WEAR TV — Bessent launches &lsquo;Operation Economic Outcast&rsquo; targeting Iran&rsquo;s global lifelines (Aug 24, 2026) — https://weartv.com/news/nation-world/treasury-secretary-scott-bessent-to-detail-economic-d-day-sanctions-push-against-iran-tehran-war-revenue-streams-finances-oil-trade-president-trump-strait-of-hormuz</li>
<li>NBC News — Trump administration live updates: U.S. announces new sanctions against Iran (Aug 24, 2026) — https://www.nbcnews.com/politics/trump-administration/live-blog/trump-iran-live-updates-rcna594071</li>
<li>CNBC — Oil prices fall as investors await &lsquo;toughest&rsquo; U.S. sanctions on Iran (Aug 24, 2026) — https://www.cnbc.com/2026/08/24/oil-price-today-wti-brent-us-sanctions-iran.html</li>
<li>TheStreet via Yahoo Finance — Stock Market Today (Aug. 24, 2026): Nasdaq slides on Iran sanctions, U.S.-Canada tariff threats (Rob Lenihan, Aug 24, 2026, 9:48 AM ET; live blog, fetched this run) — https://finance.yahoo.com/markets/stocks/articles/stock-market-today-aug-24-134834490.html</li>
'''

rw('wallstreet-briefing.html',
   [(ws_tldr_old,ws_tldr_new),(ws_h2_old,ws_h2_new),(ws_p1_old,ws_p1_new),(ws_p2_old,ws_p2_new),
    (ws_cards_anchor,ws_new_cards)] + ws_drop + [(ws_wti_old,ws_wti_new),(ws_brent_old,ws_brent_new),
    (ws_src_anchor,ws_src_new)])

# ---------------- CYBER ----------------
cy_tldr_old = 'the Treasury Secretary details the US sanctions response at 1 p.m. ET as this edition publishes &mdash;'
cy_tldr_new = 'the Treasury Secretary answered at 1 p.m. ET with &ldquo;Operation Economic Outcast,&rdquo; naming more than 60 Iran-linked entities, individuals and vessels, some of them accused of running cyber operations for Tehran &mdash;'

cy_top_old = 'The timing matters for the other desk: the Treasury Secretary details new US economic sanctions on Iran at a press conference this afternoon.'
cy_top_new = 'The timing matters for the other desk: at 1 p.m. ET on Monday, Treasury Secretary Scott Bessent announced &ldquo;Operation Economic Outcast,&rdquo; sanctioning more than 60 entities, individuals and vessels accused of helping Iran procure nuclear and missile technology, <b>conduct cyber operations</b> or generate oil revenue, and broadening secondary-sanctions risk across Iran&rsquo;s digital-asset, technology, gold, aviation and shipping links.'

cy = open('cyber-briefing.html',encoding='utf-8').read()
assert cy.count('<span class="tag new">New</span>')==2
cy = cy.replace('<span class="tag new">New</span>','')
cy = cy.replace('<b>New this edition.</b> ','')
open('cyber-briefing.html','w',encoding='utf-8').write(cy)
rw('cyber-briefing.html',[(cy_tldr_old,cy_tldr_new),(cy_top_old,cy_top_new)])

# add cyber source
rw('cyber-briefing.html',[('<div class="lab">Sources</div>\n<ul>\n',
 '<div class="lab">Sources</div>\n<ul>\n<li>CBS News — Bessent announces new economic sanctions against Iran: &ldquo;The clock just started ticking&rdquo; (Aug 24, 2026; fetched this run) — https://www.cbsnews.com/news/bessent-press-conference-iran-sanctions-economic-d-day/</li>\n')])

# ---------------- INDEX ----------------
idx_sec_old = 'Iran-linked hackers took a British power plant offline for four days in the first cyberattack known to have halted a UK generating station &mdash; the Treasury Secretary details the US sanctions response at 1 p.m. ET as this edition publishes &mdash;'
idx_sec_new = 'Iran-linked hackers took a British power plant offline for four days in the first cyberattack known to have halted a UK generating station &mdash; the Treasury Secretary answered at 1 p.m. ET with &ldquo;Operation Economic Outcast,&rdquo; naming more than 60 Iran-linked entities, individuals and vessels, some of them accused of running cyber operations for Tehran &mdash;'
idx_mkt_h_old = '<h2>Chips keep the Nasdaq red as Bessent takes the podium</h2>'
idx_mkt_h_new = '<h2>Bessent launches &ldquo;Operation Economic Outcast&rdquo;</h2>'
idx_mkt_p_old = '<p>Chip and memory weakness is still setting the tone &mdash; the group gapped down on weekend reports Washington may let Apple buy memory from China&rsquo;s CXMT and YMTC &mdash; leaving the S&amp;P 500 off about 0.2%, the Nasdaq Composite off about 0.4% and the Dow up about 0.2% in early-afternoon trade, while Treasury Secretary Scott Bessent&rsquo;s Iran sanctions press conference begins at 1 p.m. ET and the bond market keeps refusing to reward his $1 trillion cash pile.</p>'
idx_mkt_p_new = '<p>Treasury Secretary Scott Bessent launched what he called Operation Economic Outcast at his 1 p.m. ET press conference &mdash; more than 60 Iran-linked entities, individuals and vessels sanctioned and secondary-sanctions risk broadened across digital assets, technology, gold, aviation and shipping &mdash; while the tape held the shape it has kept all day, with the S&amp;P 500 off 0.18%, the Nasdaq Composite off 0.40% and the Dow up 0.23% on chip and memory weakness, and crude sold off into the announcement.</p>'
rw('index.html',[(idx_sec_old,idx_sec_new),(idx_mkt_h_old,idx_mkt_h_new),(idx_mkt_p_old,idx_mkt_p_new)])
print("ALL EDITS APPLIED")
