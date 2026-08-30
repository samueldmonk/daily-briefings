# -*- coding: utf-8 -*-
import io, re, sys
def rd(p): return io.open(p,encoding='utf-8').read()
def wr(p,s): io.open(p,'w',encoding='utf-8').write(s)

# 1) advance the board counter in MMA body prose (tldr already says sixtieth)
m = rd('mma-briefing.html')
old = ('The board is unchanged for a <b>fifty-ninth consecutive edition</b>; no title has been contested since, '
       'because <b>UFC Shanghai carried no championship bout.</b>')
new = ('The board is unchanged for a <b>sixtieth consecutive edition</b> &mdash; <b>a third consecutive clean '
       'run against ESPN&rsquo;s own page</b>, with all six men&rsquo;s divisions returning champion, method and '
       'date together and every one of them matching; no title has been contested since, because '
       '<b>UFC Shanghai carried no championship bout.</b>')
if old not in m:
    print("FAIL: board counter anchor missing"); sys.exit(1)
m = m.replace(old, new, 1)
wr('mma-briefing.html', m)

# 2) footer dedupe, first occurrence wins, across all three briefings
for p in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    s = rd(p)
    i = s.rfind('<div class="srcs">')
    head, blk = s[:i], s[i:]
    seen = set()
    def keep(mo):
        h = mo.group(1)
        if h in seen:
            return ''
        seen.add(h)
        return mo.group(0)
    blk2 = re.sub(r'<a href="([^"]+)">.*?</a>(?:<br>\s*)?', keep, blk, flags=re.S)
    blk2 = re.sub(r'(<br>\s*){2,}', '<br>', blk2)
    wr(p, head + blk2)
    hrefs = re.findall(r'href="([^"]+)"', rd(p)[rd(p).rfind('<div class="srcs">'):])
    if len(hrefs) != len(set(hrefs)):
        print("FAIL: %s still has duplicate hrefs" % p); sys.exit(1)
    print("%s: footer deduped to %d unique links" % (p, len(hrefs)))

print("fix_1310.py OK")
