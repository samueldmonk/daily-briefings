#!/usr/bin/env python3
# The W4 insertion anchored on a non-distinctive string ('<span class="mut">Th') and landed in
# The Lead instead of the WTI row. Move it. Caught by the read-through, not by any check.
import io, sys
F = 'wallstreet-briefing.html'

BLOCK = ('<span class="mut"><b>A third reading arrived this run and it lands between the two.</b> A search return this '
'morning puts <b>WTI at approximately $91.98, up about $0.50 or 0.5%</b> against Friday&rsquo;s settlement &mdash; '
'roughly 36 cents below Trading Economics&rsquo; 8:47 read of 92.34 and a smaller daily move than its +0.94%. '
'Both are live quotes taken at different minutes of a holiday-thinned session rather than competing settlements, '
'so the row header stays at <b>~$92</b> and neither intraday level is asserted as the figure. The same return '
'independently describes <b>$91.48 as Friday&rsquo;s official settlement</b> &mdash; a third path to that number, '
'after Trading Economics and EnergyNow.</span> ')

h = io.open(F, encoding='utf-8').read()

# 1. remove from the wrong place
if BLOCK in h:
    h = h.replace(BLOCK, '', 1)
    io.open(F, 'w', encoding='utf-8').write(h)
    h = io.open(F, encoding='utf-8').read()
    assert 'A third reading arrived this run' not in h
    print('ok: misplaced block removed from The Lead')
else:
    print('skip: block not in The Lead')

# 2. re-insert on a distinctive WTI-row anchor
TELL = 'A third reading arrived this run'
ANCHOR = 'put WTI at <b>92.34</b>, <b>+0.94% on the day</b>'
if TELL in h:
    print('skip (already applied): WTI row insertion')
else:
    if ANCHOR not in h:
        print('MISS ANCHOR: WTI row'); sys.exit(1)
    h = h.replace(ANCHOR, ANCHOR + ' &mdash; and ' + BLOCK.replace('<span class="mut"><b>A third', '<b>a third', 1)
                  .replace('arrived this run and it lands between the two.</b>',
                           'arrived this run and it lands just below it.</b>', 1)
                  .replace('</span> ', ' ', 1)
                  .rstrip(), 1)
    io.open(F, 'w', encoding='utf-8').write(h)
    h2 = io.open(F, encoding='utf-8').read()
    assert h2.count(TELL) == 1, 'duplicated'
    print('ok: third WTI reading re-inserted inside the WTI row')

# 3. verify it is now inside the commodities table, not The Lead
h = io.open(F, encoding='utf-8').read()
i = h.find('A third reading arrived this run')
tbl = h.rfind('<tr>', 0, i)
seg = h[tbl:i]
assert 'WTI' in seg or '92.34' in seg, 'still not in the WTI row: ' + seg[:200]
print('verified: block sits inside the WTI table row')
