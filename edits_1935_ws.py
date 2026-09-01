# -*- coding: utf-8 -*-
import io, sys, re
P='/tmp/db_1788305419/wallstreet-briefing.html'
s=io.open(P,encoding='utf-8').read()
n=0
def rep(old,new,label):
    global s,n
    if old not in s:
        print('MISS:',label); return False
    c=s.count(old)
    if c!=1:
        print('AMBIG(%d):'%c,label); return False
    s=s.replace(old,new); n+=1; print('ok:',label); return True

# ---------- W1: TLDR ----------
old_tldr_start='<div class="tldr"><b>The Tape</b> <span>Stocks closed lower to open September'
i=s.find(old_tldr_start); j=s.find('</span></div>',i)
assert i>0 and j>i
new_tldr=('<div class="tldr"><b>The Tape</b> <span>The macro session gave way to an earnings evening: '
 'after a global bond sell-off closed all three indices lower &mdash; the Dow down 419.02 points, or 0.79%, to 52,766.88, '
 'the S&amp;P 500 down 0.71% to 7,631.47 and the Nasdaq Composite down 1.03% to 26,099.77 &mdash; '
 '<b>Dell reported record quarterly revenue of $47 billion, a record $60.9 billion in AI server orders and a record $95 billion backlog, '
 'and rose roughly 8% to 10% after the bell</b>, GitLab jumped about 16% on a raised full-year outlook, '
 'and MongoDB fell by double digits <i>despite</i> beating on both lines, '
 'while crude stayed bid on renewed U.S.&ndash;Iran fighting and the U.S. 10-year was quoted as high as 4.81%.</span></div>')
s=s[:i]+new_tldr+s[j+len('</span></div>'):]
n+=1; print('ok: W1 tldr')

# ---------- W2: ticker tape symbols ----------
rep('{"proName":"NASDAQ:SNOW","title":"Snowflake"}' if '{"proName":"NASDAQ:SNOW","title":"Snowflake"}' in s else '{"proName":"NYSE:SNOW","title":"Snowflake"}',
    '{"proName":"NASDAQ:GTLB","title":"GitLab"},{"proName":"NASDAQ:MDB","title":"MongoDB"}',
    'W2 ticker symbols')

io.open(P,'w',encoding='utf-8').write(s)
print('edits applied:',n)
