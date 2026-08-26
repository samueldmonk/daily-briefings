import sys, io, re
P = sys.argv[1] if len(sys.argv)>1 else '.'
def tldr(fn):
    h = io.open(P+'/'+fn, encoding='utf-8').read()
    m = re.search(r'<div class="tldr"><b>[^<]*</b> <span>(.*?)</span></div>', h, re.S)
    assert m, fn
    return m.group(1)
T = {'c-sec': tldr('cyber-briefing.html'),
     'c-mkt': tldr('wallstreet-briefing.html'),
     'c-mma': tldr('mma-briefing.html')}
H = {'c-sec': 'Boston Scientific&rsquo;s outage moves the stock &mdash; and a critical Adobe Commerce bug joins the watchlist',
     'c-mkt': 'The tape finally prints: four indices, all reconciled, and almost no movement in any of them',
     'c-mma': 'Shanghai media day: Song rips his shirt off &mdash; and the White House card&rsquo;s $30 million loss surfaces'}
h = io.open(P+'/index.html', encoding='utf-8').read()
for k in T:
    pat = re.compile(r'(class="bcard '+k+r'"[^>]*>\s*<div class="kicker">.*?</div>\s*<h2>)(.*?)(</h2>\s*<p>)(.*?)(</p>)', re.S)
    m = pat.search(h); assert m, k
    h = h[:m.start()] + m.group(1) + H[k] + m.group(3) + T[k] + m.group(5) + h[m.end():]
io.open(P+'/index.html','w',encoding='utf-8').write(h)
print('index synced')
