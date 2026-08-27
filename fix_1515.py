# -*- coding: utf-8 -*-
import re
# 1) demote stale freshness tags
for p in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    s=open(p,encoding='utf-8').read()
    before=s
    s=s.replace('<span class="tag new">New &middot; 2:41</span>','<span class="tag">Carried &middot; 2:41</span>')
    s=re.sub(r'<span class="tag new">(?!New &middot; 3:15|Updated &middot; 3:15 PM ET|Updated · 3:15 PM ET)', '<span class="tag">', s)
    if s!=before: open(p,'w',encoding='utf-8').write(s); print('demoted in',p)

# 2) fresh tags on updated cards
def rep(p,old,new,label):
    s=open(p,encoding='utf-8').read()
    assert old in s, "NOT FOUND: "+label
    assert s.count(old)==1, "NOT UNIQUE: "+label
    open(p,'w',encoding='utf-8').write(s.replace(old,new,1)); print("ok:",label)

rep('cyber-briefing.html',
 '<div class="card"><span class="tag">Carried &middot; 12:38</span><span class="tag crit">Federal</span>\n<h3>The ATF confirms',
 '<div class="card"><span class="tag new">New &middot; 3:15</span><span class="tag">Carried &middot; 12:38</span><span class="tag crit">Federal</span>\n<h3>The ATF confirms',
 'ATF card tag')

rep('mma-briefing.html',
 '<div class="card" style="grid-column:1/-1"><span class="tag">Carried</span><span class="tag acc">Fight week</span>',
 '<div class="card" style="grid-column:1/-1"><span class="tag new">New &middot; 3:15</span><span class="tag acc">Fight week</span>',
 'MMA Shanghai card tag')

# 3) verify no stale `tag new`
for p in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    s=open(p,encoding='utf-8').read()
    bad=[t for t in re.findall(r'<span class="tag new">[^<]*</span>', s) if '3:15' not in t]
    assert not bad, (p,bad)
    n=len(re.findall(r'<span class="tag new">', s))
    assert n>0, "no fresh tag on "+p
    print(p,'fresh tags:',n)
