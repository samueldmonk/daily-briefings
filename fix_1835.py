# -*- coding: utf-8 -*-
import io
def rd(f): return io.open(f,encoding="utf-8").read()
def wr(f,s): io.open(f,"w",encoding="utf-8").write(s)
def rep(s, old, new, n=1, label=""):
    c = s.count(old); assert c==n, "EXPECT %d got %d %s :: %s"%(n,c,label,old[:70])
    return s.replace(old,new)

WS_OLD = ('re-verified a thirteenth time this run by a search that returned all three index levels, all three '
 'percentage moves and the three weekly figures together &mdash; the third consecutive check of that breadth')
WS_NEW = ('re-verified a <b>fourteenth</b> time this run by a search that again returned all three index levels, '
 'all three percentage moves and the three weekly figures together &mdash; the <b>fourth consecutive</b> check '
 'of that breadth, and on a tape that has been shut since Friday afternoon <b>nothing else on this page moved '
 'either</b>')

w = rd("wallstreet-briefing.html")
w = rep(w, WS_OLD, WS_NEW, 1, "ws tldr")
# stale time-of-day in the lead: it is now evening
w = rep(w, 'It is Saturday morning and U.S. equity markets are <b>closed</b>.',
           'It is <b>Saturday evening</b> and U.S. equity markets are <b>closed</b>.', 1, "ws morning")
w = rep(w, '<b>re-verified an eleventh time at 12:35 PM',
           '<b>re-verified a fourteenth time at 6:20 PM, and an eleventh time at 12:35 PM', 1, "ws lead")
wr("wallstreet-briefing.html", w)

MM_OLD = ('though the $400,000 figure still stands as the total of the four and no source states a combined '
 'total for the card.')
MM_NEW = ('though the $400,000 figure still stands as the total of the four and no source states a combined '
 'total for the card; and at <b>6:35 PM</b> Song&rsquo;s own words arrived &mdash; &ldquo;I think the UFC '
 'should give me the title shot. I feel like I can finish everyone. I can finish Petr, I can finish '
 'Merab&rdquo; &mdash; alongside sourced framing that with the belt booked for October his realistic next step '
 'is a <b>backup role or a fight with the Yan&ndash;Dvalishvili winner</b>, and two figures in the results '
 'table above were challenged by an aggregated listing this hour and <b>both survived</b>: the Bilal Hasan '
 'knockout is <b>round two at 2:28</b>, not round one, and Rei Tsuruya&rsquo;s choke is at <b>4:14</b>, not '
 '4:03.')
m = rd("mma-briefing.html")
m = rep(m, MM_OLD, MM_NEW, 1, "mma tldr")
wr("mma-briefing.html", m)

i = rd("index.html")
i2 = rep(i, MM_OLD, MM_NEW, 1, "index mma card")
wr("index.html", i2)
print("FIX OK")
