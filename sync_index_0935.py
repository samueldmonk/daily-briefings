#!/usr/bin/env python3
# Regenerate index.html cards FROM the briefing pages, so a card can never drift
# from the TL;DR it summarises. Each card paragraph is a verbatim copy of the page TL;DR.
import re, sys

def tldr(path):
    h = open(path, encoding='utf-8').read()
    m = re.search(r'<div class="tldr"><b>[^<]*</b>\s*<span>(.*?)</span></div>', h, re.S)
    if not m:
        print('FAIL: no tldr in ' + path); sys.exit(1)
    return m.group(1).strip()

cy = tldr('cyber-briefing.html')
ws = tldr('wallstreet-briefing.html')
mm = tldr('mma-briefing.html')

heads = {
    'cy': 'A model that can find its own zero-days',
    'ws': 'Stocks open mixed &mdash; and oil gives back its spike',
    'mm': 'UFC.com prices every Paris bout, and the newcomer is favoured',
}

cards = (
'<div class="big">\n'
'<div class="card c-sec"><div class="kicker">⛨ The Cyber Wire &middot; The Wire</div>\n'
'<h3>%s</h3>\n<p>%s</p>\n'
'<a class="more" href="cyber-briefing.html">Read the briefing &rarr;</a></div>\n\n'
'<div class="card c-mkt"><div class="kicker">▲ The Closing Bell &middot; The Tape</div>\n'
'<h3>%s</h3>\n<p>%s</p>\n'
'<a class="more" href="wallstreet-briefing.html">Read the briefing &rarr;</a></div>\n\n'
'<div class="card c-mma"><div class="kicker">⊘ The Octagon &middot; Tale of the Tape</div>\n'
'<h3>%s</h3>\n<p>%s</p>\n'
'<a class="more" href="mma-briefing.html">Read the briefing &rarr;</a></div>\n'
'</div>') % (heads['cy'], cy, heads['ws'], ws, heads['mm'], mm)

h = open('index.html', encoding='utf-8').read()
new, k = re.subn(r'<div class="big">.*?</div>\s*(?=<div class="disc">)', cards, h, count=1, flags=re.S)
if k != 1:
    print('FAIL: index card grid not replaced'); sys.exit(1)
open('index.html', 'w', encoding='utf-8').write(new)

# verify verbatim containment
chk = open('index.html', encoding='utf-8').read()
for lbl, t in (('cyber', cy), ('markets', ws), ('mma', mm)):
    if t not in chk:
        print('FAIL: %s card is not a verbatim copy of its page TL;DR' % lbl); sys.exit(1)
    print('  %-8s card == page TL;DR (verbatim, %d chars)' % (lbl, len(t)))
print('OK index regenerated from pages')
