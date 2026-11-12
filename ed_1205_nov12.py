import re,sys
def rep(s,a,b,n=1):
    c=s.count(a)
    if c<1: sys.exit("MISSING: "+a[:80])
    return s.replace(a,b) if n==0 else s.replace(a,b,1)
YU='https://finance.yahoo.com/markets/live/stock-market-today-thursday-november-12-sp-500-nasdaq-dow-nvidia-invest-110027430.html'
ws=open('wallstreet-briefing.html').read()
old_tldr=re.search(r'<div class="tldr"><b>The Tape</b> <span>.*?</span></div>',ws).group(0)
TL='Stocks gave back most of their late-morning gains after Jensen Huang resigned as Nvidia CEO: Yahoo’s ≈11:42 AM ET strip had the Dow +0.15%, the S&amp;P 500 +0.03% and the Nasdaq Composite −0.06%, with the Russell 2000 −0.60% and Nvidia −5.42%.'
ws=rep(ws,old_tldr,'<div class="tldr"><b>The Tape</b> <span>'+TL+'</span></div>')
ws=re.sub(r'(<div class="freshline" id="freshline">)[^<]*(</div>)',r'\1Data as of ≈11:42 AM ET (Yahoo index strip, fetched ~12:05 PM ET) · briefings refresh every 30 minutes, 8 AM–6 PM ET\2',ws,count=1)
H_old='As of ~11:31 AM ET: Stocks turn green — Dow +0.3%, S&amp;P 500 +0.2%, Nasdaq +0.2% — as Nvidia holds near −5% after Huang resigns'
H_new='As of ~11:42 AM ET: Gains fade toward flat — Dow +0.15%, S&amp;P 500 +0.03%, Nasdaq −0.06% — as Nvidia slides 5% after Huang resigns'
ws=rep(ws,H_old,H_new)
p1=re.search(r'<p><span class="tag new">New</span> <b>Latest read\.</b>.*?</p>',ws).group(0)
P1=('<p><span class="tag new">New</span> <b>Latest read.</b> Yahoo Finance’s index strip at about 11:42 AM ET (“close in 4h 18m”) showed the Dow up 81.16 points, or 0.15%, the S&amp;P 500 up 2.22 points, or 0.03%, and the Nasdaq Composite down 15.26 points, or 0.06% — all reconciling with Wednesday’s closes — while the Russell 2000 was down 0.60%; Yahoo’s ^DJI quote at 11:42:57 AM ET was +0.18%. The 10-year yield was 5.08% (+0.08), the VIX was 17.56 (+0.40%), gold fell 3.18% and bitcoin 3.62%, and December WTI was up 0.42% at $86.89 (<a href="'+YU+'" target="_blank" rel="noopener">Yahoo Finance</a>). Yahoo’s text still says “US stocks turned green late Thursday morning, paring earlier losses,” but its strip shows those gains narrowing from the ≈11:31 AM read, when the Dow was +0.30%, the S&amp;P 500 +0.21% and the Nasdaq +0.18%.</p>')
ws=rep(ws,p1,P1)
ws=rep(ws,'<b>Nvidia holds its losses near 5%.</b> Nvidia’s quote at 11:31:47 AM ET was $165.31, −$8.42 (−4.85%); Yahoo said the stock “tumbled 4% after trimming losses”',
 '<b>Nvidia slides about 5%.</b> Nvidia’s quote at 11:42:57 AM ET was $164.32, −$9.41 (−5.42%); Yahoo said the stock “tumbled 5% after trimming losses”')
open('wallstreet-briefing.html','w').write(ws)
ix=open('index.html').read()
ix=rep(ix,H_old,H_new)
old=re.search(r'Stocks turned green late Thursday morning after Jensen Huang resigned as Nvidia CEO: Yahoo’s ≈11:31.*?opening plunge\.',ix).group(0)
ix=rep(ix,old,TL)
open('index.html','w').write(ix)
m=open('mma-briefing.html').read()
anchor='<li><b>White &amp; Trump:</b>'
li='<li><span class="tag new">New</span> <b>Crossover card:</b> ESPN headline — “Overeem-Manuwa boxing match added as co-main event on Paul-Doumbé card” (<a href="https://www.espn.com/boxing/story/_/id/50461800/paul-doumbe-card-adds-overeem-manuwa-boxing-match-co-main" target="_blank" rel="noopener">ESPN, Brett Okamoto</a>, headline seen on ESPN this run).</li>'
m=rep(m,anchor,li+anchor)
open('mma-briefing.html','w').write(m)
print("ok")
