import re
A='style="color:var(--acc2)"'
TS='https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-oct-07-2026'
def rep(s,old,new,count=1):
    assert old in s, ('MISSING',old[:80]); return s.replace(old,new,count)
# ---------- WALL STREET ----------
f='wallstreet-briefing.html'; s=open(f).read()
s=s.replace('<span class="tag good">New</span> ','').replace('<span class="tag good">New</span>','')
s=re.sub(r'(<h3 class="lead-h"[^>]*>)Pre-market, as of ~7:23 AM ET:[^<]*(</h3>)', r'\1Pre-market, as of ~8:54 AM ET: futures lower as the 10-year yield hits 5.35%, its highest since 2002, ahead of the Fed minutes\2', s)
newp=(f'<p><b>Pre-market (TheStreet, 8:54 AM ET).</b> <span class="tag good">New</span> &ldquo;Stock futures were lower and oil prices were rising Wednesday after Wall Street closed at record highs,&rdquo; as investors await minutes of the Fed&rsquo;s Sept. 15&ndash;16 meeting at 2 PM ET; Reuters reports the minutes are expected to show a much broader debate than the unanimous decision to raise rates suggested. TheStreet, citing CNBC at 8:47 AM, said the benchmark 10-year Treasury yield was up nearly 8 basis points at 5.35% &mdash; its highest level since 2002 &mdash; while the 30-year rose 8.3 basis points to 5.724%, also a 24-year high, and the 2-year rose 2.7 basis points to 4.818%, ahead of today&rsquo;s 10-year note sale. Capital.com&rsquo;s Daniela Hathorn said markets put the probability of a 25 bp hike this month at only around 20%. Separately, Tropical Storm Isaias formed in the Gulf early Wednesday; the National Hurricane Center expects rapid strengthening into the season&rsquo;s first hurricane, with a potential landfall late Friday or early Saturday between eastern Louisiana and the western Florida Panhandle (<a href="{TS}" {A}>TheStreet</a>).</p>\n')
s=rep(s,'<p><b>Pre-market (Reuters, 7:17 AM ET).</b>', newp+'<p><b>Pre-market (Reuters, 7:17 AM ET).</b>')
tape=('Stock futures were lower before Wednesday&rsquo;s open &mdash; Dow E-minis &minus;0.58%, S&amp;P 500 E-minis &minus;0.32% and Nasdaq 100 E-minis &minus;0.70% at 7:17 AM ET (Reuters) &mdash; as the 10-year Treasury yield climbed nearly 8 basis points to 5.35%, its highest since 2002 (CNBC via TheStreet, 8:47 AM), oil rose and investors awaited the Fed&rsquo;s September minutes at 2 PM ET, a day after the S&amp;P 500&rsquo;s first close above 7,800.')
s=re.sub(r'(<div class="tldr"><b>The Tape</b> <span>).*?(</span></div>)', lambda m:m.group(1)+tape+m.group(2), s, count=1, flags=re.S)
# movers
cards=(f'<div class="card"><span class="tag good">+3.81% pre</span><span class="tag good">New</span><h3>Mattel (MAT)</h3><p>Climbed 3.81% before the bell amid intensifying takeover and buyout speculation and growing pressure from activist shareholders (<a href="{TS}" {A}>TheStreet, 8:20 AM</a>).</p></div>\n'
 f'<div class="card"><span class="tag good">+3.33% pre</span><span class="tag good">New</span><h3>Flutter Entertainment (FLUT)</h3><p>Gained 3.33% after Citigroup upgraded the online sports-betting and gaming operator to Buy from Neutral with a $91 price target (<a href="{TS}" {A}>TheStreet, 8:20 AM</a>).</p></div>\n'
 f'<div class="card"><span class="tag bad">&minus;4.58% pre</span><span class="tag good">New</span><h3>Bitmine Immersion Technologies (BMNR)</h3><p>The largest corporate holder of Ethereum sank 4.58% on profit-taking after recent gains and a broader decline in Ethereum prices; chip-materials maker Entegris (ENTG) fell 2.57% (<a href="{TS}" {A}>TheStreet, 8:20 AM</a>).</p></div>\n')
s=rep(s,'<h2 class="sec">Movers &amp; Drivers</h2><div class="cards">\n','<h2 class="sec">Movers &amp; Drivers</h2><div class="cards">\n'+cards)
s=rep(s,'<h3>Constellation Brands (STZ)</h3><p>Fell about 4.5% before the bell despite','<h3>Constellation Brands (STZ)</h3><p>Fell 4.76% before the bell at TheStreet&rsquo;s 8:20 AM read (about 4.5% per Invezz at 7:23 AM) despite')
s=rep(s,'(<a href="https://invezz.com/news/2026/10/07/dow-futures-plunge-305-points-5-things-to-know-before-wall-street-opens-on-oct-7/" style="color:var(--acc2)">Invezz, 7:23 AM</a>).</p></div>\n<div class="card"><span class="tag good">+1.3% pre</span>',
 f'(<a href="https://invezz.com/news/2026/10/07/dow-futures-plunge-305-points-5-things-to-know-before-wall-street-opens-on-oct-7/" style="color:var(--acc2)">Invezz, 7:23 AM</a>). TheStreet had SpaceX down 1.71% at $168.98 at 8:33 AM; the shares debuted at $135 on June 12 and hit a record $225.64 on June 16 (<a href="{TS}" {A}>TheStreet</a>).</p></div>\n<div class="card"><span class="tag good">+1.3% pre</span>')
# rates
s=rep(s,'<td><b>Wed. pre-market:</b> around 5.32% (',f'<td><b>Wed. pre-market:</b> up nearly 8 bp at 5.35%, its highest since 2002 (CNBC via <a href="{TS}" {A}>TheStreet</a>, 8:47 AM); around 5.32% (')
s=rep(s,'<td><b>Wed. pre-market:</b> touched 5.70%, its highest since 2002 (',f'<td><b>Wed. pre-market:</b> +8.3 bp to 5.724%, a 24-year high (CNBC via <a href="{TS}" {A}>TheStreet</a>, 8:47 AM); touched 5.70%, its highest since 2002 (')
s=rep(s,'<td>2-Year Treasury</td><td>4.791% <span class="up">&minus;4.2 bp</span></td><td>3:33 PM ET',f'<td>2-Year Treasury</td><td>4.791% <span class="up">&minus;4.2 bp</span></td><td><b>Wed. pre-market:</b> +2.7 bp to 4.818% (CNBC via TheStreet, 8:47 AM). <b>Tuesday:</b> 3:33 PM ET')
s=rep(s,'<td><b>Wed. pre-market:</b> November futures $90.11',f'<td><b>Wed. pre-market:</b> $90.12 (+0.76%) (<a href="{TS}" {A}>TheStreet, 6:57 AM</a>); November futures $90.11')
s=rep(s,'<td><b>Wed. pre-market:</b> back above $101 (Invezz, 7:23 AM).','<td><b>Wed. pre-market:</b> $102 (+1.40%) (TheStreet, 6:57 AM); back above $101 (Invezz, 7:23 AM).')
s=rep(s,'<td><b>Wed.</b> $4,159.40 (&minus;0.66%) ~4:05 AM ET (Yahoo strip).','<td><b>Wed.</b> futures $4,147.70 (&minus;0.94%) early (TheStreet, 7:24 AM); $4,159.40 (&minus;0.66%) ~4:05 AM ET (Yahoo strip).')
s=rep(s,'<td>Futures, early Tuesday (TheStreet, 7:18 AM)</td>','<td><b>Wed.</b> futures $60.40 (&minus;1.94%) early (TheStreet, 7:27 AM). <b>Tuesday:</b> futures, early (TheStreet, 7:18 AM)</td>')
s=rep(s,'<li><b>Today (Wed. Oct 7):</b>',f'<li><span class="tag good">New</span> <b>Tropical Storm Isaias:</b> upgraded early Wednesday in the Gulf; Florida Gov. Ron DeSantis declared a state of emergency in 25 counties, and the NHC forecasts a potential landfall late Friday or early Saturday between eastern Louisiana and the western Florida Panhandle (<a href="{TS}" {A}>TheStreet, citing WESH</a>).</li>\n<li><b>Today (Wed. Oct 7):</b>')
s=rep(s,'<div class="srcs">Sources: ',f'<div class="srcs">Sources: <a href="{TS}" {A}>TheStreet live blog (Oct 7, updated 8:54 AM ET)</a> &middot; ')
open(f,'w').write(s)
# ---------- CYBER ----------
f='cyber-briefing.html'; s=open(f).read()
s=s.replace('<span class="tag good" style="margin-left:6px">New</span>','')
PW='https://cybersecuritynews.com/32-0-days-pwn2own-2026'
card=(f'<div class="card"><span class="tag warnt">Research</span><span class="tag good" style="margin-left:6px">New</span><h3>Pwn2Own Ireland 2026 day one: 32 unique zero-days, $388,500 paid</h3><p>Researchers reportedly exploited 32 unique zero-days on the contest&rsquo;s opening day (Oct. 6). Three teams broke the Samsung Galaxy S26, Ikotas Labs took $40,000 for an argument-injection flaw in OpenAI Codex, LiteLLM fell to two teams, VinSOC chained five flaws against Oracle Autonomous AI Database and disclosed seven zero-days in the Philips Hue Bridge Pro, and McCaulay Hudson earned $50,000 against the Sonos Era 300; a Google Pixel 10 attempt failed within the time limit. These are contest demonstrations, not attacks on real users (<a href="{PW}" {A}>Cyber Security News</a>).</p></div>')
s=rep(s,'<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">','<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">'+card)
s=rep(s,'<div class="srcs">Sources: ',f'<div class="srcs">Sources: <a href="{PW}" {A}>Cyber Security News (Pwn2Own Ireland 2026 day one)</a> &middot; ')
open(f,'w').write(s)
# ---------- MMA ----------
f='mma-briefing.html'; s=open(f).read()
s=s.replace('<li><span class="tag good">New</span> ','<li>')
UP='https://www.ufc.com/news/ufc-vegas-122-fight-by-fight-preview-allen-vs-duncan'
s=rep(s,'On the main card, Matheus Camilo is &minus;198 against Jai Herbert (+164).</p></div>',
 f'On the main card, Matheus Camilo is &minus;198 against Jai Herbert (+164).</p><p><span class="tag good">New</span> UFC.com&rsquo;s preview: Allen rides a three-fight win streak, most recently a Fight of the Night unanimous decision over Edmen Shahbazyan; Duncan has won five straight, including decisions over Roman Dolidze and Jared Cannonier. The rest of the main card: Loopy Godinez vs. Ketlen Souza, Malcolm Wellmaker vs. Otari Tanzilovi, Julius Walker vs. Gerald Meerschaert and Matheus Camilo vs. Jai Herbert; prelims start at 5 PM ET on Paramount+ (<a href="{UP}" {A}>UFC.com</a>).</p></div>')
s=rep(s,'<div class="srcs">Sources: ',f'<div class="srcs">Sources: <a href="{UP}" {A}>UFC.com (Allen vs. Duncan fight-by-fight preview)</a> &middot; ')
open(f,'w').write(s)
# ---------- INDEX ----------
f='index.html'; s=open(f).read()
s=re.sub(r'(Markets</h3><p>).*?(</p>)', lambda m:m.group(1)+tape+m.group(2), s, count=1, flags=re.S)
open(f,'w').write(s)
print('ok')
