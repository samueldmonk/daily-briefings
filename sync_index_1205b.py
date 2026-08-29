import io, re
def tldr(p):
    h=io.open(p,encoding='utf-8').read()
    return re.search(r'<div class="tldr"><b>[^<]+</b>\s*<span>(.*?)</span></div>',h,re.S).group(1)
cy,ws,mm = tldr('cyber-briefing.html'), tldr('wallstreet-briefing.html'), tldr('mma-briefing.html')
h=io.open('index.html',encoding='utf-8').read()
n=0
for cls,new in [('c-cy',cy),('c-ws',ws),('c-mm',mm)]:
    m=re.search(r'(<div class="bigcard %s">.*?)<p>(.*?)</p>'%cls,h,re.S)
    if not m: print('MISS',cls); continue
    h=h[:m.start(2)]+new+h[m.end(2):]; n+=1
io.open('index.html','w',encoding='utf-8').write(h)
h2=io.open('index.html',encoding='utf-8').read()
for cls,want,name in [('c-cy',cy,'cyber'),('c-ws',ws,'markets'),('c-mm',mm,'mma')]:
    m=re.search(r'<div class="bigcard %s">.*?<p>(.*?)</p>'%cls,h2,re.S)
    print('%-8s mirrors tldr: %s'%(name, bool(m) and m.group(1)==want))
print('replaced',n)
