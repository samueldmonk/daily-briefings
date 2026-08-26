# -*- coding: utf-8 -*-
import re, sys
fails=[]
P={f:open(f,encoding='utf-8').read() for f in
   ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']}

# 1) demote stale new-markers (anything not 6:36) to Carried
demoted=0
for f in P:
    def d(mm):
        global demoted
        if mm.group(1)=='6:36': return mm.group(0)
        demoted+=1
        return '<span class="tag">Carried &middot; %s</span>'%mm.group(1)
    P[f]=re.sub(r'<span class="tag new">New &middot; (\d{1,2}:\d{2})</span>', d, P[f])
    # inline prose form
    P[f]=re.sub(r'<b>New &middot; (?!6:36)(\d{1,2}:\d{2})</b>', r'<b>Carried &middot; \1</b>', P[f])

# 2) sharpen the 6:36 closing-set rejection so it does not imply the Dow/Nasdaq levels are themselves false
old = ('<b>7,677.24 is a standing rejected figure in this desk&rsquo;s corrections file</b> and the set traces to '
       '<b>a CNBC article dated August&nbsp;25</b>, not August&nbsp;26.')
new = ('<b>The set traces to a CNBC article dated August&nbsp;25 &mdash; these are TUESDAY&rsquo;s closes, mislabelled as Wednesday&rsquo;s.</b> '
       '&#9888; <b>Two of the three numbers are perfectly good figures in the right slot:</b> <b>53,577.40</b> and <b>26,151.30</b> are the '
       'Dow and Nasdaq closes for <b>August&nbsp;25</b>, and they already appear on this page in exactly that role &mdash; as the prior-close '
       'bases every intraday board today subtracts back to. <b>What is rejected is the DATE on them, not the numbers.</b> The third, '
       '<b>7,677.24</b>, is rejected outright: it is the <b>Zacks</b> print of Tuesday&rsquo;s S&amp;P close that this desk declined to adopt at '
       '2:44 in favour of <b>7,677.28</b>, which every other board independently implies.')
if P['wallstreet-briefing.html'].count(old)==1:
    P['wallstreet-briefing.html']=P['wallstreet-briefing.html'].replace(old,new,1)
else:
    fails.append('ws close-set rewrite anchor n=%d'%P['wallstreet-briefing.html'].count(old))

if fails:
    print('FAILED',fails); sys.exit(1)
for f,h in P.items(): open(f,'w',encoding='utf-8').write(h)
print('fix OK; new-markers demoted =',demoted)
