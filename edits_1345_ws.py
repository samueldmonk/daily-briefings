# -*- coding: utf-8 -*-
import io
P='wallstreet-briefing.html'
s=io.open(P,encoding='utf-8').read(); orig=s
def rep(a,b):
    global s
    assert s.count(a)>=1, "MISSING: "+a[:130]
    s=s.replace(a,b,1)

# provenance demotion of inherited claims
for a,b in [
 ('A sixth reading arrived this edition, and it is the widest of the six.',
  'A sixth reading arrived the 1:15 edition, and it is the widest of the six.'),
 ('This run EnergyNow, fetched directly, gives ',
  'EnergyNow, fetched directly in an earlier edition, gives '),
 ('This run&rsquo;s week-ahead return repeated the same CPI forecasts this page already carries',
  'The 1:15 edition&rsquo;s week-ahead return repeated the same CPI forecasts this page already carries'),
 ('This edition corrects it.','The 12:45 edition corrected it.'),
 ('Re-confirmed this edition.','Re-confirmed the 1:15 edition.'),
 ('the 162,000 payroll print re-confirmed this edition','the 162,000 payroll print re-confirmed the 1:15 edition'),
]:
    rep(a,b)

# THE CME HALT HAS NOW PASSED — this is the freshness fix of the edition
old = (u'So the live ticker at the top of this page has roughly two hours of matched trading left in it as the 12:16 edition publishes, '
       u'and then a quiet screen that is not the same thing as a flat market.')
new = (u'<b>That halt has now happened.</b> The 12:16 edition said the live ticker at the top of this page had roughly two hours of matched trading left in it; '
       u'as this edition publishes at about <b>1:45 PM ET</b>, the 1:00 PM ET halt is <b>about three quarters of an hour in the past</b>, so the equity-index quotes in the tape above are '
       u'<b>the last matched prices of a shortened holiday session, not a live market</b> &mdash; a quiet screen, which is not the same thing as a flat one. '
       u'<span class="mut">The halt time is the sourced fact and the arithmetic against the clock is this desk&rsquo;s; the reopen is 5:00 p.m. CT, 6:00 PM ET. '
       u'Nothing here asserts a level or a move for the futures session, because no settlement will be published for it.</span>')
rep(old,new)

# tldr: keep the diesel/Brent lead, add the futures-halt clause at the end
tl_old = u'as the U.S. and Iran exchange strikes around Hormuz.'
tl_new = (u'as the U.S. and Iran exchange strikes around Hormuz. '
          u'The one thing that changed on the screen since the last edition is that CME&rsquo;s equity-index futures hit their <b>1:00 PM ET holiday halt</b>, '
          u'so the tape at the top of this page is now showing the last matched prices of a shortened session rather than a live one.')
rep(tl_old,tl_new)

# sources
src = u'<h2 class="sec">Sources</h2>'
assert src in s
add = (u'<h2 class="sec">Sources</h2><p class="note" style="margin:-2px 0 10px"><b>Re-checked the 1:45 PM ET edition, none fetched first-hand:</b> '
 u'<span class="mut">a futures-holiday schedule return re-stating the CME equity-index halt at 12:00 p.m. CT / 1:00 PM ET with the usual evening Globex reopen; '
 u'Benzinga on the NYSE and Nasdaq being shut all day with the normal session resuming Tuesday 8&nbsp;September; '
 u'and a week-ahead return placing <b>PPI before Thursday&rsquo;s open and August CPI before Friday&rsquo;s</b>, with the FOMC quiet period running from Saturday 5&nbsp;September through Thursday 17&nbsp;September &mdash; '
 u'all of which this page already carried, so nothing on the markets beat is tagged New.</span></p>')
s=s.replace(src,add,1)

assert s!=orig
io.open(P,'w',encoding='utf-8').write(s); print('ws OK',len(s))
