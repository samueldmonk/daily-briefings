# -*- coding: utf-8 -*-
import io,re
from collections import Counter
def rd(p): return io.open(p,encoding='utf-8').read()
def wr(p,s): io.open(p,'w',encoding='utf-8').write(s)

# Dedupe footer source links: keep the FIRST occurrence of each href inside <footer>
for p in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    s=rd(p); f=s.rfind('<footer')
    head,foot=s[:f],s[f:]
    seen=set(); out=[]; pos=0
    for m in re.finditer(r'<a href="(https?://[^"]+)"[^>]*>.*?</a>(?:<br>)?\n?', foot, re.S):
        url=m.group(1)
        out.append(foot[pos:m.start()])
        if url in seen:
            pass  # drop the duplicate anchor entirely
        else:
            seen.add(url); out.append(m.group(0))
        pos=m.end()
    out.append(foot[pos:])
    foot=''.join(out)
    wr(p,head+foot)
    h=re.findall(r'<a href="(https?://[^"]+)"', rd(p)[rd(p).rfind('<footer'):])
    assert len(h)==len(set(h)), p
    print(p,'footer links:',len(h))
