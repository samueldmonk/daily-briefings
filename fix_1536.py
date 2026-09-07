# -*- coding: utf-8 -*-
import io,re
f='mma-briefing.html'; s=io.open(f,encoding='utf-8').read()
old=('at UFC&nbsp;325 on 31 January 2026, and this page carries the result')
new=('at <b>UFC&nbsp;325</b> on <b>31 January 2026</b> &mdash; it is the <b>one defence</b> the champions board below already credits to Volkanovski, '
     'though the board names his <b>UFC&nbsp;314</b> win over Lopes rather than the rematch')
assert old in s, "anchor missing"
s=s.replace(old,new,1)
io.open(f,'w',encoding='utf-8').write(s)
print("ok")
