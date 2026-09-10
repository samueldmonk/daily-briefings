import re,sys
D='/sessions/youthful-laughing-hamilton/mnt/outputs/'
fails=[]
def rep(fn,old,new,n=1):
    p=D+fn; h=open(p).read()
    c=h.count(old)
    if c!=n:
        fails.append(f'{fn}: expected {n} got {c} for {old[:70]!r}'); return
    h=h.replace(old,new); open(p,'w').write(h)

# ================= WALL STREET =================
WS='wallstreet-briefing.html'
TLDR_OLD='the Nasdaq Composite &minus;0.64% at 26,253.34.</span></div>'
TLDR_NEW='the Nasdaq Composite &minus;0.64% at 26,253.34, and the Russell 2000 worst of all at &minus;1.31%.</span></div>'
rep(WS,TLDR_OLD,TLDR_NEW)

rep(WS,'The <b>Russell 2000</b> was <b>&minus;1.24%</b> at 3:03 p.m., down over one percent for a second day &mdash; small caps taking the worst of an oil-and-yields squeeze, as they usually do.',
 'The <b>Russell 2000</b> was <b>&minus;1.24%</b> at 3:03 p.m. and finished worse still: two reads for this edition put its close at <b>&minus;1.31%, at 2,921.50</b>, and at <b>&minus;1.30%</b>. That reconciles against Tuesday&rsquo;s 2,960.20 close &mdash; 2,960.20 &minus; 2,921.50 = 38.70 points, or 1.307%, which rounds to both figures &mdash; so the closing level goes on the scorecard below, a row the previous edition had to drop for want of anything but the intraday mark. Small caps took the worst of an oil-and-yields squeeze, as they usually do.')

rep(WS,'<b>4:00 p.m. close</b> &mdash; the official figures above.',
 '<b>4:00 p.m. close</b> &mdash; the official figures above, with the Russell 2000 at &minus;1.31%.')

# scorecard row + note
rep(WS,'<tr><td>Dow Jones Industrial Average</td><td>52,380.66</td><td>&minus;405.41</td><td class="down">&minus;0.77%</td></tr>',
 '<tr><td>Dow Jones Industrial Average</td><td>52,380.66</td><td>&minus;405.41</td><td class="down">&minus;0.77%</td></tr>\n<tr><td>Russell 2000</td><td>2,921.50</td><td>&minus;38.70</td><td class="down">&minus;1.31%</td></tr>')

rep(WS,'<b>The Russell 2000 row is dropped this edition:</b> its closing level was not stated in anything read this run, and the &minus;1.24% seen at 3:03 p.m. is an intraday reading, not a close.',
 '<b>The Russell 2000 row is restored this edition.</b> The previous edition dropped it because no closing level had been stated anywhere read; two reads for this edition supply one &mdash; 2,921.50, described as a 1.31% fall, alongside a separate read giving 1.30% &mdash; and it reconciles against Tuesday&rsquo;s 2,960.20 close at 38.70 points, or 1.307%, which rounds to both. The point change in that row is derived here from the two levels, on the same basis as the S&amp;P and Nasdaq rows. The &minus;1.24% seen at 3:03 p.m. remains an intraday reading and is labelled as one in the Lead.')

# Canada
rep(WS,'The White House said it will ban imports of Canadian motorbikes and a slew of other products starting later this month as relations with Ottawa fray.',
 'The White House said it will ban imports of Canadian motorbikes and a slew of other products starting later this month as relations with Ottawa fray. <b>New this run:</b> the traffic runs both ways &mdash; <b>Canadian retaliatory tariffs on about $20 billion of U.S. goods took effect on Tuesday</b>, and the dispute is named in this session&rsquo;s reporting alongside oil and yields as a reason risk appetite faded.')

# demote tags
h=open(D+WS).read()
h=h.replace('<span class="t new">New</span>','<span class="t carried">Carried</span>')
h=h.replace('<span class="t carried">Updated</span>','<span class="t carried">Carried</span>')
open(D+WS,'w').write(h)

rep(WS,'<div class="note" style="margin:18px 0 0"><b>On the tags.</b> The previous edition of this page published at about 6:15 p.m. ET; research for this one ran from roughly 6:25 p.m. to 8:30 p.m., and it publishes after 8 p.m. <b>Every card carried over from that edition was demoted from New or Updated to <i>Carried</i> before tagging</b> &mdash; including Apple, SpaceX, the mega-cap board and the midday leaderboard, which were New last edition and are not new now. <b>Four cards are genuinely new this run:</b> <b>Chewy</b> above, and the three in After-Hours Movers below &mdash; the American Eagle results, the refused movers list, and the note on what else is and is not verified post-close.',
 '<div class="note" style="margin:18px 0 0"><b>On the tags.</b> This is the sixth edition of this page today, and the third since the closing bell. <b>Every card on the page is tagged Carried, and not one is tagged New</b> &mdash; the four that were New last edition (Chewy, American Eagle, the refused movers list and the post-close note) were demoted before tagging, because a card is not made new by the page being rebuilt around it. <b>What is new this edition is not a card at all:</b> the Russell 2000&rsquo;s closing level, which no source read earlier today had stated, is now verified and restored to the Weekly Scorecard, and the Canadian side of the trade dispute is on the radar below.')
