# -*- coding: utf-8 -*-
import io,re
def tl(f,label):
    s=io.open(f,encoding='utf-8').read()
    m=re.search(r'<div class="tldr"><b>'+label+r'</b> <span>(.*?)</span></div>',s,re.S)
    assert m, f
    return m.group(1)
cy=tl('cyber-briefing.html','The Wire')
ws=tl('wallstreet-briefing.html','The Tape')
mm=tl('mma-briefing.html','Tale of the Tape')

F='index.html'; s=io.open(F,encoding='utf-8').read()
def rep(old,new):
    global s
    n=s.count(old); assert n==1,"count=%d %r"%(n,old[:80]); s=s.replace(old,new)

rep(u"<h3>Two federal patch deadlines now: Oracle today, Citrix Saturday</h3>\n<p>CISA's deadline to patch the maximum-severity Oracle WebLogic proxy flaw CVE-2026-21962 expires today; the actively exploited Citrix NetScaler flaw behind it, CVE-2026-8452, is due Saturday and now carries a confirmed CVSS of 8.8 — and a second, separate NetScaler bug, a 9.3 authentication bypass, is patched but not yet reported exploited.</p>",
    u"<h3>Oracle's deadline expires today — and the ATF confirms a breach</h3>\n<p>"+cy+u"</p>")

rep(u"<h3>The rally broadens at midday and the Dow joins in</h3>\n<p>Just past noon the tech-led rally has cooled a step — the latest read has the Dow up 147.67 points (+0.28%) and the Nasdaq Composite up 279.61 points (+1.07%), both below the 11:35 tallies, with the S&amp;P 500 still holding a 0.4% gain and Okta still the biggest single-stock mover.</p>",
    u"<h3>The rally re-accelerates: the Nasdaq adds more than 400 points</h3>\n<p>"+ws+u"</p>")

rep(u"<h3>Shanghai fight week: Nurmagomedov vs. Song for the next title shot</h3>\n<p>It is fight week in Shanghai: bantamweight contenders Umar Nurmagomedov and Song Yadong headline Saturday's card at the Oriental Sports Center, with Nurmagomedov a −500 favourite on two of the three lines seen this run and −470 on the third — and a stale champions list surfaced again today and was rejected.</p>",
    u"<h3>Shanghai fight week: Nurmagomedov vs. Song for the next title shot</h3>\n<p>"+mm+u"</p>")

io.open(F,'w',encoding='utf-8').write(s); print("INDEX OK")
