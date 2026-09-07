# -*- coding: utf-8 -*-
import io
f='mma-briefing.html'; s=io.open(f,encoding='utf-8').read()
old='the longest of his career and his first stretch without a win since August 2024'
assert old in s,'A'
s=s.replace(old,'the longest of his career, leaving him without a win since <b>August 2024</b>',1)
io.open(f,'w',encoding='utf-8').write(s)

f='wallstreet-briefing.html'; s=io.open(f,encoding='utf-8').read()
old='and the two figures are the only new numbers this desk found today'
assert old in s,'B'
s=s.replace(old,'and the two figures are the only new numbers this edition found',1)
io.open(f,'w',encoding='utf-8').write(s)
print('ok')
