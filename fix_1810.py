#!/usr/bin/env python3
"""One job: repair the source-footer duplicates left by a regex that could not cross newlines.

The dedupe in sources_1810.py used `<a href="...">.*?</a>` WITHOUT re.S. Any anchor whose
label spans a newline never matched, so it was neither collected nor removed -- it survived in
the leftover text and was re-appended alongside the fresh copy. Same defect class as the guards
narrowed in earlier runs: the pattern was written for the shape the markup was assumed to have.
"""
import io, sys, re
REPO = sys.argv[1]
A = re.compile(r'<a href="([^"]+)"[^>]*>.*?</a>(?:<br>)?', re.S)

for f in ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']:
    p = REPO + '/' + f
    h = io.open(p, encoding='utf-8').read()
    k = h.find('<div class="srcs">')
    if k < 0:
        continue
    s = k + len('<div class="srcs">')
    e = h.find('</div>', k)
    block = h[s:e]
    seen, out, dropped = set(), [], 0
    for m in A.finditer(block):
        if m.group(1) in seen:
            dropped += 1
            continue
        seen.add(m.group(1))
        out.append(re.match(r'<a href="[^"]+"[^>]*>.*?</a>', m.group(0), re.S).group(0))
    rest = A.sub('', block).strip()
    h = h[:s] + '<br>'.join(out) + ('<br>' + rest if rest else '') + h[e:]
    io.open(p, 'w', encoding='utf-8').write(h)
    hrefs = re.findall(r'<a href="([^"]+)"', h[s:h.find('</div>', k)])
    print('%-26s %d unique, %d dupes removed, dup-free=%s'
          % (f, len(seen), dropped, len(hrefs) == len(set(hrefs))))
