import re
Y='https://sg.finance.yahoo.com/news/live/stock-market-today-thursday-november-12-sp-500-nasdaq-dow-nvidia-slides-jensen-huang-resigns-invest-165632931.html'
T='https://pro.thestreet.com/stock-market-today/2026-11-12'
A=lambda u,t:f'<a href="{u}" target="_blank" rel="noopener">{t}</a>'
s=open('wallstreet-briefing.html').read()
def rep(old,new):
    global s
    assert s.count(old)==1,old[:80]; s=s.replace(old,new)
# tldr
i=s.find('<div class="tldr"><b>The Tape</b> <span>'); j=s.find('</span></div>',i)
s=s[:i]+'<div class="tldr"><b>The Tape</b> <span>Stocks climbed back into the green at midday despite Jensen Huang’s exit from Nvidia: Yahoo’s quotes at about 12:51 PM ET had the Dow +0.37%, the S&amp;P 500 +0.26% and the Nasdaq Composite +0.21%, with Nvidia −4.77%.'+s[j:]
rep('Data as of ≈11:42 AM ET (Yahoo index strip, fetched ~12:05 PM ET)','Data as of ≈12:51 PM ET (Yahoo quotes, fetched ~12:55 PM ET)')
rep('<h3>As of ~11:42 AM ET: Gains fade toward flat — Dow +0.15%, S&amp;P 500 +0.03%, Nasdaq −0.06% — as Nvidia slides 5% after Huang resigns</h3>',
    '<h3>As of ~12:51 PM ET: Stocks claw back gains — Dow +0.37%, S&amp;P 500 +0.26%, Nasdaq +0.21% — as Nvidia trims its slide to under 5% after Huang resigns</h3>')
i=s.find('<p><span class="tag new">New</span> <b>Latest read'); j=s.find('<p><b>Strategy',i)
new=('<p><span class="tag new">New</span> <b>Latest read.</b> Yahoo Finance’s Dow quote at 12:51:40 PM ET was 52,681.73, up 195.24 points, or 0.37%, and its quote chips on the live blog (updated 12:43 PM ET) showed the S&amp;P 500 +0.26% and the Nasdaq Composite +0.21% ('+A(Y,'Yahoo Finance')+'). '
 '“Stocks rebounded from session lows in midday trading as tech pared losses and energy stocks gained,” Yahoo’s Grace O’Donnell wrote, adding that the 10-year Treasury yield rose 8 basis points to 5.09% “amid broader bond pressure” ('+A(Y,'Yahoo Finance')+'). '
 'That is up from the ≈11:42 AM ET read (prior edition), when the Dow was +0.15%, the S&amp;P 500 +0.03% and the Nasdaq −0.06%.</p>'
 '<p><span class="tag new">New</span> <b>Nvidia trims losses.</b> Nvidia’s quote at 12:51:39 PM ET was $165.44, −$8.29 (−4.77%); the stock “sank as much as 13% in early trading” before paring the drop to about 5% as traders weighed the company’s future without Huang. Other notable movers Yahoo flagged included Alibaba, Alphabet, Nebius and Intuitive Machines ('+A(Y,'Yahoo Finance')+'). '
 'Former Goldman Sachs CEO Lloyd Blankfein posted on X: “Sad about Jensen. Shakespearean. But as [Charles] de Gaulle said, ‘The graveyards are filled with indispensable men’” (David Hollerith — '+A(Y,'Yahoo Finance')+'). '
 'Bernstein’s Stacy Rasgon, who downgraded the stock overnight and cut his price target to $200 from $400, said fundamentals “are clearly still intact” but questioned what happens to Nvidia’s “myriad of investments in the space, various backstops and residual guarantees” (per Bloomberg, via '+A(T,'TheStreet Pro')+').</p>')
s=s[:i]+new+s[j:]
# Radar additions
rep('<h2 class="sec">On the Radar</h2><div class="panel"><ul class="bul">',
 '<h2 class="sec">On the Radar</h2><div class="panel"><ul class="bul">'
 '<li><span class="tag new">New</span> <b>Fed:</b> Cleveland Fed President Beth Hammack, a 2026 voter, said “We need to move to a restrictive stance of policy” and that October CPI showed progress had “really stalled,” but favored “smaller increments, more frequent, smaller rises”; a larger move is only on the table “if we get behind the curve” (per Bloomberg, via TheStreet Pro’s Neil Sethi, 12:45 PM ET — '+A(T,'TheStreet Pro')+'). Chicago Fed President Goolsbee said inflation “looks like it’s going the wrong way” (same source).</li>'
 '<li><span class="tag new">New</span> <b>Anthropic IPO:</b> the company posted that “shares are expected to begin publicly trading on November 19th (EST),” with pricing expected Nov. 18 ('+A(Y,'Yahoo Finance')+').</li>'
 '<li><b>Sentiment:</b> AAII bears rose to 51.4%, the most in eight weeks, and bulls fell to 30.8%, a bull-bear spread of −20.6 ('+A(T,'TheStreet Pro')+', 10:12 AM ET).</li>')
# sources
rep('<footer><b>Sources</b> (Nov. 12 items fetched ~8:05–10:05 AM ET;','<footer><b>Sources</b> (Nov. 12 items fetched ~8:05 AM–12:55 PM ET;')
rep('<ol><li>','<ol><li>'+A(Y,'Yahoo Finance (SG mirror of US live blog) — Stock market today: Dow, S&amp;P 500, Nasdaq turn higher as Nvidia stock slides after CEO Jensen Huang resigns (updated 9:43 AM PST = 12:43 PM ET; ^DJI and NVDA quotes 12:51 PM ET; fetched ~12:55 PM ET)')+'</li><li>'+A(T,'TheStreet Pro — Stock Market Today, Nov. 12, 2026 (Neil Sethi; updates 7:59 AM–12:45 PM ET; fetched ~12:50 PM ET)')+'</li><li>',)
# old-New tags in movers: strip New from previously tagged items other than ours
open('wallstreet-briefing.html','w').write(s)
print(s.count('tag new'))
# index card
x=open('index.html').read()
o1='As of ~11:42 AM ET: Gains fade toward flat — Dow +0.15%, S&amp;P 500 +0.03%, Nasdaq −0.06% — as Nvidia slides 5% after Huang resigns'
assert o1 in x
x=x.replace(o1,'As of ~12:51 PM ET: Stocks claw back gains — Dow +0.37%, S&amp;P 500 +0.26%, Nasdaq +0.21% — as Nvidia trims its slide after Huang resigns')
o2='Stocks gave back most of their late-morning gains after Jensen Huang resigned as Nvidia CEO: Yahoo’s ≈11:42 AM ET strip had the Dow +0.15%, the S&amp;P 500 +0.03% and the Nasdaq Composite −0.06%, with the Russell 2000 −0.60% and Nvidia −5.42%.'
assert o2 in x
x=x.replace(o2,'Stocks climbed back into the green at midday despite Jensen Huang’s exit from Nvidia: Yahoo’s quotes at about 12:51 PM ET had the Dow +0.37%, the S&amp;P 500 +0.26% and the Nasdaq Composite +0.21%, with Nvidia −4.77%.')
x=re.sub(r'(id="freshline">Data as of )[^·<]*',r'\1~12:51 PM ET ',x)
open('index.html','w').write(x)
