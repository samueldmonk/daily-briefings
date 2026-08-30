# -*- coding: utf-8 -*-
import io, re, sys
def rd(p): return io.open(p,encoding='utf-8').read()
def wr(p,s): io.open(p,'w',encoding='utf-8').write(s)

def tldr_text(path):
    s = rd(path)
    i = s.find('<div class="tldr">')
    a = s.find('<span>', i)+6
    b = s.find('</span></div>', a)
    return s[a:b]

cy = tldr_text('cyber-briefing.html')
ws = tldr_text('wallstreet-briefing.html')
mm = tldr_text('mma-briefing.html')

idx = rd('index.html')
pat = re.compile(r'(<div class="bigcard c-(cy|ws|mm)">.*?<p>)(.*?)(</p>)', re.S)
mapping = {'cy':cy,'ws':ws,'mm':mm}
n = [0]
def rep(m):
    n[0]+=1
    return m.group(1)+mapping[m.group(2)]+m.group(4)
idx2, cnt = pat.subn(rep, idx)
if cnt != 3:
    print("FAIL: replaced %d cards" % cnt); sys.exit(1)
wr('index.html', idx2)

# verify equality
idx3 = rd('index.html')
for k,v in mapping.items():
    if v not in idx3:
        print("FAIL: card %s does not mirror tldr" % k); sys.exit(1)
print("sync_index_1310.py OK — 3 cards mirror their tldrs")
