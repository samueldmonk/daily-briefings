# -*- coding: utf-8 -*-
import sys
def rep(t, old, new, label):
    if old not in t: sys.exit("MISS: " + label)
    if t.count(old) != 1: sys.exit("NOT UNIQUE (%d): %s" % (t.count(old), label))
    return t.replace(old, new)

w = open('wallstreet-briefing.html').read()
w = rep(w,
 '<h3>A hot jobs number closed the week &mdash; and the next real test doesn&rsquo;t come until Thursday</h3>',
 '<h3>A hot jobs number closed the week &mdash; but the vote now turns on Friday&rsquo;s CPI</h3>',
 'WS lead headline')
w = rep(w,
 'Everything below reflects Friday 4 September, the most recent completed session.',
 'Everything below reflects Friday 4 September, the most recent completed session. '
 'The payrolls beat pushed the hike case forward, but it is no longer the newest input: on Thursday 3 September, before those numbers landed, Fed governor '
 '<b>Christopher Waller</b> said the <b>11 September CPI report</b> would largely determine his vote, and hike odds fell back to roughly even. That exchange is set out in full under On the Radar.',
 'WS lead pointer')
open('wallstreet-briefing.html','w').write(w)

t = open('index.html').read()
t = rep(t, '<h3>A hot payrolls print, then a long weekend</h3>',
           '<h3>Payrolls ran hot, but the hike case just cooled</h3>', 'index mkt headline')
open('index.html','w').write(t)
print("OK")
