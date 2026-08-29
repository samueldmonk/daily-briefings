# -*- coding: utf-8 -*-
import io,re
O="/sessions/tender-hopeful-newton/mnt/outputs/"
def tldr(fn):
    s=io.open(O+fn,encoding='utf-8').read()
    m=re.search(r'<div class="tldr">.*?<span>(.*?)</span></div>',s,re.S)
    return m.group(1).strip()
idx=io.open(O+"index.html",encoding='utf-8').read()
ok=0; miss=[]
for fn,old_key in [("cyber-briefing.html","McKesson has told the SEC"),
                   ("wallstreet-briefing.html","Markets are closed for the weekend"),
                   ("mma-briefing.html","Song Yadong knocked out Umar")]:
    new=tldr(fn)
    m=re.search(r'<p[^>]*>('+re.escape(old_key)+r'.*?)</p>',idx,re.S)
    if m:
        idx=idx[:m.start(1)]+new+idx[m.end(1):]; ok+=1
    else: miss.append(fn)
io.open(O+"index.html","w",encoding='utf-8').write(idx)
print("index cards synced:",ok,"misses:",miss)
# assert sync
idx=io.open(O+"index.html",encoding='utf-8').read()
for fn in ["cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]:
    t=tldr(fn)
    print(("OK  " if t in idx else "FAIL"), fn, t[:70])
