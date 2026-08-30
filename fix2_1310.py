# -*- coding: utf-8 -*-
import io, re, sys
def rd(p): return io.open(p,encoding='utf-8').read()
def wr(p,s): io.open(p,'w',encoding='utf-8').write(s)

for p in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    s = rd(p)
    i = s.rfind('<div class="srcs">')
    head, blk = s[:i], s[i:]
    seen = set(); out = []; pos = 0
    for mo in re.finditer(r'<a\b[^>]*href="([^"]+)"[^>]*>.*?</a>', blk, re.S):
        h = mo.group(1)
        out.append(blk[pos:mo.start()])
        if h not in seen:
            seen.add(h); out.append(mo.group(0))
        pos = mo.end()
    out.append(blk[pos:])
    blk2 = ''.join(out)
    blk2 = re.sub(r'(<br>\s*){2,}', '<br>\n', blk2)
    blk2 = re.sub(r'<br>\s*(</div>)', r'\1', blk2)
    wr(p, head + blk2)
    t = rd(p); b = t[t.rfind('<div class="srcs">'):]
    hrefs = re.findall(r'href="([^"]+)"', b)
    if len(hrefs) != len(set(hrefs)):
        print("FAIL: %s dupes remain" % p); sys.exit(1)
    print("%s: %d unique footer links" % (p, len(hrefs)))
print("fix2_1310.py OK")
