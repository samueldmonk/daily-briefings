import re, io, sys
FAIL=[]
def rd(p): return io.open(p,encoding='utf-8').read()
def wr(p,s): io.open(p,'w',encoding='utf-8').write(s)
def sub(s, old, new, path, label):
    if old not in s:
        FAIL.append("MISSING anchor [%s] in %s"%(label,path)); return s
    return s.replace(old,new,1)

# ============ WALL STREET ============
p='wallstreet-briefing.html'; w=rd(p)

# 1. demote prior New tags
w=w.replace('New &middot; 1:09','Carried from the 1:09 edition').replace('New at 1:09','Carried from the 1:09 edition')

# 2. tldr
old_tldr=re.search(r'<div class="tldr"><b>The Tape</b>[\s\S]*?</div>',w).group(0)
new_tldr=('<div class="tldr"><b>The Tape</b> <span>The afternoon has its <b>first four-index board</b>, and every line on it reconciles: '
 '<b>S&amp;P&nbsp;500 7,673.94 (&minus;3.34, &minus;0.04%)</b>, <b>Dow 53,468.18 (&minus;109.22, &minus;0.20%)</b>, '
 '<b>Nasdaq Composite 26,100.65 (&minus;50.65, &minus;0.19%)</b> and &mdash; for the first time this session &mdash; '
 '<b>Russell&nbsp;2000 3,003.80 (&minus;6.22, &minus;0.21%)</b>, each subtracting exactly to Tuesday&rsquo;s close. '
 'All three headline indices are still red, but <b>less red than the 12:27 board</b> this page carried through the 1:09 edition, '
 'so the tape has clawed back rather than extended. <b>Abercrombie &amp; Fitch</b> now has a <b>seventh</b> rendering &mdash; and, at '
 '<b>$144.03, &plus;$35.12, &plus;32.25%</b>, a second one that reconciles &mdash; while the whole tape still waits on '
 '<b>Nvidia after the close</b>.</span></div>')
w=sub(w,old_tldr,new_tldr,p,'ws tldr')

# 3. lead: new h2 + new first paragraph
old_h2='<h2>Red across all three, and for once every number on the board reconciles</h2>'
new_h2=('<h2>A fourth index joins the board at 1:24, and all four of them reconcile</h2>\n'
 '<p><b>&#9679; New at 1:40 &mdash; the first board of the day to carry the Russell&nbsp;2000, and the first to pass this page&rsquo;s three-way test on four lines at once.</b> '
 'A Yahoo Finance live quote board, read this run on Yahoo&rsquo;s syndication of the Motley Fool midday report, returns '
 '<b>S&amp;P&nbsp;500 7,673.94, &minus;3.34, &minus;0.04%</b>; <b>Dow&nbsp;30 53,468.18, &minus;109.22, &minus;0.20%</b>; '
 '<b>Nasdaq 26,100.65, &minus;50.65, &minus;0.19%</b>; and <b>Russell&nbsp;2000 3,003.80, &minus;6.22, &minus;0.21%</b>. '
 'Every one of the four subtracts to a close already published in the Weekly Scorecard below &mdash; '
 '<b>7,673.94 &plus; 3.34 = 7,677.28</b>, <b>53,468.18 &plus; 109.22 = 53,577.40</b>, <b>26,100.65 &plus; 50.65 = 26,151.30</b>, '
 '<b>3,003.80 &plus; 6.22 = 3,010.02</b> &mdash; and every percent equals points over that prior close '
 '(0.0435%, 0.204%, 0.194%, 0.207%, rounding to the four stated figures). '
 '<b>&#9888; The board carries no clock stamp of its own; its header reads &ldquo;U.S. markets close in 2h 36m,&rdquo; which places it at approximately '
 '<b>1:24&nbsp;p.m. ET</b> &mdash; roughly seventeen minutes behind the wall clock when it was fetched, so it is published as a cached render stamped by its own countdown, not as a live tick.</b> '
 'Read against the 12:27-stamped strip this page carried through the 1:09 edition '
 '(S&amp;P &minus;0.13%, Dow &minus;0.27%, Nasdaq &minus;0.37%), <b>all three headline indices have narrowed their losses</b>. '
 'The same board gives the <b>VIX at 15.55, &plus;0.10, &plus;0.65%</b> &mdash; 15.55 &minus; 0.10 = 15.45, and 0.10 &divide; 15.45 = 0.647%, which also reconciles.</p>')
w=sub(w,old_h2,new_h2,p,'ws lead h2')

# 4. movers cards
anchor='<div class="lab">Movers &amp; drivers</div>\n<div class="cards">'
cards=('<div class="card"><div class="tags"><span class="tag new">New &middot; 1:40</span><span class="tag">Four-index board</span><span class="tag">Reconciles 4/4</span></div>'
 '<h3>Losses narrow across the board &mdash; and the small caps finally get a Wednesday print</h3>'
 '<p>The <b>~1:24&nbsp;p.m. ET</b> Yahoo board is the first this session to state a Wednesday level for the <b>Russell&nbsp;2000</b>: '
 '<b>3,003.80, &minus;6.22, &minus;0.21%</b> against Tuesday&rsquo;s 3,010.02 close. Small caps are therefore moving with the large-cap tape rather than against it &mdash; '
 'the four moves span just <b>17 basis points</b>, from the S&amp;P&rsquo;s &minus;0.04% to the Russell&rsquo;s &minus;0.21%. '
 '<b>&#9888; Earlier today a search summary put the Russell <i>up</i> 0.50% on Wednesday; that figure was and remains rejected &mdash; &plus;0.50% is Tuesday&rsquo;s close, not a Wednesday move.</b> '
 'The board also carries <b>VIX 15.55, &plus;0.10, &plus;0.65%</b>, off the 15.67 premarket read but above the ~9:59 print of 15.51.</p></div>\n'
 '<div class="card"><div class="tags"><span class="tag new">New &middot; 1:40</span><span class="tag">Seventh rendering</span><span class="tag">&plus;32.25%</span></div>'
 '<h3>Abercrombie gets a seventh number &mdash; and this one reconciles too</h3>'
 '<p>The trending-tickers strip on the same ~1:24 board reads <b>ANF $144.03, &plus;$35.12, &plus;32.25%</b>. '
 'It passes on its own arithmetic: <b>144.03 &minus; 35.12 = 108.91</b>, and <b>35.12 &divide; 108.91 = 32.25%</b>. '
 'That makes <b>two</b> self-consistent Abercrombie reads on this page &mdash; the earlier <b>&plus;30.85% to $142.50</b> and this one &mdash; alongside five that state a percent with no level '
 '(8.3%, 11.9%, &ldquo;over 11%&rdquo; premarket, 17% and the Motley Fool&rsquo;s &ldquo;eye-watering 40%&rdquo;). '
 '<b>&#9888; The two reconciling reads are not merged and neither is corrected: they are successive ticks off the same $108.91 prior close, and the stock is higher at 1:24 than it was when the earlier figure was struck.</b> '
 'The move is attributed throughout to an earnings beat and raised full-year guidance.</p></div>\n'
 '<div class="card"><div class="tags"><span class="tag new">New &middot; 1:40</span><span class="tag">&plus;51.80%</span><span class="tag crit">No reason stated</span></div>'
 '<h3>Expion360 is the biggest percentage move any source has put a number on today</h3>'
 '<p><b>XPON &mdash; Expion360 Inc. &mdash; $8.00, &plus;$2.73, &plus;51.80%</b> on the ~1:24 trending strip. '
 'The arithmetic holds (<b>8.00 &minus; 2.73 = 5.27</b>; <b>2.73 &divide; 5.27 = 51.80%</b>), which is the only reason it is published. '
 '<b>&#9888; No catalyst, filing, release or analyst note is stated by the source, and none is asserted here. It does not displace Abercrombie as Chart of the Day, '
 'which is scoped to names with a stated reason for the move.</b></p></div>\n'
 '<div class="card"><div class="tags"><span class="tag new">New &middot; 1:40</span><span class="tag">Third tick</span><span class="tag">Guidance</span></div>'
 '<h3>Intuit&rsquo;s decline deepens on the third successive read</h3>'
 '<p><b>INTU $344.53, &minus;$12.93, &minus;3.62%</b> at ~1:24. It reconciles to the same prior close this page has used all day &mdash; '
 '<b>344.53 &plus; 12.93 = 357.46</b> &mdash; and <b>12.93 &divide; 357.46 = 3.617%</b>. '
 'That is the third distinct Wednesday reading published unmerged: <b>357.46 / &minus;12.46 / &minus;3.37%</b> premarket, '
 '<b>345.35 / &minus;12.11</b> intraday, and now this. All three share the 357.46 base; the stock is lower at 1:24 than at either earlier read. '
 'The move traces to <b>2027 revenue growth guided to 9&ndash;10%</b>.</p></div>')
w=sub(w,anchor,anchor+'\n'+cards,p,'ws movers cards')

# 5. Chart of the day note
old_cn='The chart now tracks <b>ANF</b>.'
new_cn=('<b>&#9679; Updated 1:40 &mdash; a newer figure, and it also reconciles.</b> The ~1:24&nbsp;p.m. ET Yahoo trending strip puts '
 '<b>ANF at $144.03, &plus;$35.12, &plus;32.25%</b>, which supersedes the &plus;30.85% / $142.50 read below as the freshest self-consistent number, '
 'without displacing it &mdash; both are printed as successive ticks off the same $108.91 prior close. The chart now tracks <b>ANF</b>.')
w=sub(w,old_cn,new_cn,p,'ws chart note')

# 6. rates rows
rates_anchor='<tr><td>Gold</td><td>$4,680.70</td>'
rows=('<tr><td>WTI crude (Oct 26 contract)</td><td>$82.73</td><td class="up">&plus;$0.37 &nbsp;&plus;0.45%</td><td>~1:24 p.m. ET Wed (Yahoo) &mdash; <b>&#9888; opposite sign to the Trading Economics row above ($80.78, &minus;1.92%); both stated this run, neither adjudicated</b></td></tr>\n'
 '<tr><td>Gold</td><td>$4,650.50</td><td class="down">&minus;$44.00 &nbsp;&minus;0.94%</td><td>~1:24 p.m. ET Wed (Yahoo) &mdash; <b>&#9888; implies a $4,694.50 prior close; the Motley Fool row implies ~$4,637; both printed</b></td></tr>\n'
 '<tr><td>Bitcoin (USD)</td><td>$78,349.37</td><td class="down">&minus;$887.63 &nbsp;&minus;1.12%</td><td>~1:24 p.m. ET Wed (Yahoo)</td></tr>\n'
 '<tr><td>VIX</td><td>15.55</td><td class="up">&plus;0.10 &nbsp;&plus;0.65%</td><td>~1:24 p.m. ET Wed (Yahoo)</td></tr>\n')
w=sub(w,rates_anchor,rows+rates_anchor,p,'ws rates rows')
wr(p,w)

# ============ CYBER ============
p='cyber-briefing.html'; c=rd(p)
c=c.replace('New &middot; 1:09','Carried from the 1:09 edition').replace('New at 1:09','Carried from the 1:09 edition')
kev_anchor='<div class="lab">CISA KEV &amp; federal deadlines</div>'
note=('<div class="lab">CISA KEV &amp; federal deadlines</div>\n'
 '<div class="note"><b>&#9679; 1:40 &mdash; nothing new seen this run, and this page says so rather than re-dressing what it already carries.</b> '
 'Fresh searches this run for August&nbsp;26 breach news, ransomware claims, exploited-vulnerability advisories and KEV additions returned '
 '<b>no item not already published on this page</b>: the Hut American Group / Flynn franchise breach, the Apple American Group filings, the '
 '<b>24 malicious npm packages</b> staging ClickFix pages on UNPKG and npmmirror, the <b>miniOrange SAML SSO</b> authentication-bypass pair, the Adobe and Nvidia advisory waves, '
 'and the Oracle KEV entry <b>CVE-2026-21962</b> are all already carried above. '
 '<b>&#9888; KEV additions dated August&nbsp;26: nothing seen this run &mdash; the eighth consecutive edition in which a catalogue search returned no alert page later than August&nbsp;25.</b> '
 'The board therefore holds unchanged at <b>14 tracked deadlines, 10 past due</b>, and Patch Priority still reads Oracle <b>Aug&nbsp;27</b> and Gitea <b>Aug&nbsp;28</b>.</div>')
c=sub(c,kev_anchor,note,p,'cyber kev note')
old=re.search(r'<div class="tldr"><b>The Wire</b>[\s\S]*?</div>',c).group(0)
c=sub(c,'</span></div>','</span></div>',p,'noop')
c=c.replace(old, old[:-len('</span></div>')] +
  ' <b>Nothing new surfaced between the 1:09 and 1:40 editions</b> &mdash; no fresh breach, advisory or KEV addition that this page was not already carrying.</span></div>',1)
wr(p,c)

# ============ MMA ============
p='mma-briefing.html'; m=rd(p)
m=m.replace('Nothing moved in the sport between the 12:58 and 1:09 editions',
            'Nothing moved in the sport between the 12:58 and 1:40 editions')
m=m.replace('unchanged for a twenty-second consecutive edition',
            'unchanged for a twenty-third consecutive edition')
if 'twenty-third consecutive edition' not in m: FAIL.append('MMA tldr counter not updated')
wr(p,m)

# ============ INDEX ============
p='index.html'; i=rd(p)
def card(i, cls, h2, para):
    mm=re.search(r'(<a class="bcard c-%s"[\s\S]*?)<h2>[\s\S]*?</h2>\s*<p>[\s\S]*?</p>'%cls, i)
    if not mm:
        FAIL.append('index card %s not matched'%cls); return i
    return i[:mm.start()]+mm.group(1)+'<h2>%s</h2>\n<p>%s</p>'%(h2,para)+i[mm.end():]
i=card(i,'mkt','Four indices, one board, and every line reconciles',
  'A <b>~1:24&nbsp;p.m. ET</b> board reads <b>S&amp;P&nbsp;500 7,673.94 (&minus;0.04%)</b>, <b>Dow 53,468.18 (&minus;0.20%)</b>, '
  '<b>Nasdaq 26,100.65 (&minus;0.19%)</b> and, for the first time today, <b>Russell&nbsp;2000 3,003.80 (&minus;0.21%)</b> &mdash; '
  'all four subtracting exactly to Tuesday&rsquo;s closes, and all three headline indices <b>less red</b> than an hour earlier.')
i=card(i,'sec','Nothing new on the wire &mdash; the Gitea and Oracle deadlines still govern the day',
  'Fresh searches this run returned <b>no breach, advisory or KEV addition</b> this page was not already carrying, and no CISA alert page later than '
  '<b>August&nbsp;25</b>. The board holds at <b>14 tracked deadlines, 10 past due</b>; Oracle&rsquo;s <b>CVSS&nbsp;10.0</b> flaw is due <b>tomorrow</b> and Gitea&rsquo;s <b>9.8</b> on <b>Friday</b>.')
i=card(i,'mma','Still nothing moving in the fight game',
  'No new card, result, signing or title change since the last edition. <b>UFC Shanghai</b> is three days out, '
  '<b>Umar Nurmagomedov</b> remains a heavy favourite over <b>Song Yadong</b> across four unmerged lines, and the champions board is unchanged for a '
  '<b>twenty-third</b> consecutive edition.')
wr(p,i)

print("FAILURES:", len(FAIL))
for f in FAIL: print(" ",f)
