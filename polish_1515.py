# -*- coding: utf-8 -*-
def rep(p,old,new,label):
    s=open(p,encoding='utf-8').read()
    assert old in s, "NOT FOUND: "+label
    assert s.count(old)==1, "NOT UNIQUE: "+label
    open(p,'w',encoding='utf-8').write(s.replace(old,new,1)); print("ok:",label)

W='wallstreet-briefing.html'; C='cyber-briefing.html'; M='mma-briefing.html'; I='index.html'

# (i) wrong relative gap + broken like-for-like comparison
rep(W,'All three sit <b>below</b> the figures this page carried forty minutes earlier — 0.4%, 1.51% and 9.3% — so on the only two reads today that carry a clock, the advance is narrower late in the session than it was after lunch.',
'All three sit <b>below</b> the figures this page carried at <b>2:41</b> — 0.4%, 1.51% and 9.3% — so on this evidence the advance is narrower at three o&rsquo;clock than it was after lunch. <span style="color:var(--mut)"><b>The comparison is drawn against the 2:41 reads, not against Bloomberg&rsquo;s 1:25 p.m. figure</b>, even though that is the only other clocked read on the page: Bloomberg timed an <i>S&amp;P 500</i> number and this read carries none, so the two do not measure the same thing and are not set against each other.</span>',
'P1 gap + comparison')

rep(W,'Between them they are the only two figures on this page whose moment is known rather than inferred, which is why the comparison is drawn between these two rather than against the undated roundups.',
'Between them they are the only two reads on this page whose moment is known rather than inferred, and they cover different indices.',
'P2 clocked reads')

# (ii) sector claim precision
rep(W,'That XLK figure is the <b>first read of an actual S&amp;P sector</b> this page has been able to print today;',
'That XLK figure is the <b>first read of a genuine S&amp;P 500 sector</b> this page has been able to print today — XLK is the technology sector&rsquo;s own SPDR, where the semiconductor funds it has been carrying track an industry rather than a sector;',
'P3 sector precision')

# (iii) level claim precision
rep(W,'Applied to Wednesday’s verified close of <b>7,675.70</b>, that percentage implies <b>7,727.1</b> — so for the first time today a level, a percentage and the prior close agree to the decimal.',
'Applied to Wednesday’s verified close of <b>7,675.70</b>, that percentage implies <b>7,727.1</b> — within a tenth of a point of the quoted level. <b>That makes it the first intraday <i>level</i> this page has been able to print all day.</b> The four earlier reads that reconciled were point-and-percent pairs, not levels, and the only levels offered until now came from the aggregator that dated them as the August 27 <i>close</i> — twice, in opposite directions — and were rejected both times.',
'P4 level precision')

# (iv) the bell has since rung
rep(W,'<p style="margin:0 0 10px"><b>New at 3:15 — the second time-stamped cash-session read of the day,',
'<p style="margin:0 0 12px;padding:9px 12px;border-left:3px solid var(--acc);background:rgba(202,166,74,.07);border-radius:8px;font-size:14.3px"><b>Note on timing.</b> The figures in this edition were fetched at about <b>3:15 PM ET</b>, before the closing bell, and every one of them is an intraday read. <b>If you are reading this after 4 PM, the session has closed and no closing figure below is a close</b> — this page publishes official closes only once they are verified, in the Weekly Scorecard, and none for August 27 had been verified when this edition was built. The next edition will carry them.</p>\n'
'<p style="margin:0 0 10px"><b>New at 3:15 — the second time-stamped cash-session read of the day,',
'P5 bell note')

# (v) MMA phrasing
rep(M,'and a fourth line seen at 3:15 has moved the favourite out to −550 / +400, wider than the −500 and −470 this page had been calling stable',
'and a fourth line seen at 3:15 has the favourite at −550 / +400, wider than the −500 and −470 this page had been calling stable',
'P6 mma tldr')
rep(M,'a range of eighty cents on the favourite,','a range of eighty points on the favourite&rsquo;s price,','P7 mma odds units')
rep(M,'<b>New at 3:15 — a fourth line, and it breaks the claim this card was carrying.</b> RotoWire lists the fight at <b>Nurmagomedov −550 / Song +400</b>.',
'<b>New at 3:15 — a fourth line, and it breaks the claim this card was carrying.</b> RotoWire lists the fight at <b>Nurmagomedov −550 / Song +400</b>. <span style="color:var(--mut)">Whether that is a move in the market or simply a different book pricing the fight differently is not something the sources seen this run establish, and no drift is asserted.</span>',
'P8 mma no-drift')

# (vi) hour countdown -> deadline stated without a fragile clock
rep(C,"expires today with roughly an hour of the East Coast business day left","expires today, with the business day nearly over",'P9 cyber tldr clock')
rep(C,'lands today, with roughly an hour of the business day left;','lands today, with the business day nearly over;','P10 cyber banner clock')
