import sys
P='mma-briefing.html'
h=open(P).read(); n=0
def rep(old,new):
    global h,n
    if old not in h: print("!! NOT FOUND:",old[:120]); sys.exit(1)
    h=h.replace(old,new,1); n+=1
h=h.replace('<span class="tag new">New &middot; 3:15</span>','<span class="tag">Carried &middot; 3:15</span>')

# TLDR
rep('<div class="tldr"><b>Tale of the Tape</b> <span>Saturday\'s Shanghai card at the Oriental Sports Center is headlined by bantamweight contenders Umar Nurmagomedov and Song Yadong, and a fourth line seen at 3:15 has the favourite at −550 / +400, wider than the −500 and −470 this page had been calling stable — and last weekend\'s Sacramento card has finally produced a business figure this page can publish, a 16,867 crowd and a $3,300,000 live gate.</span></div>',
 '<div class="tldr"><b>Tale of the Tape</b> <span>Both winners of last weekend\'s Fight of the Night in Sacramento were handed six-month suspensions after a main-event brawl, the two opponents missing from that card\'s results are now named, and UFC 331 has a date, a building and a flyweight title rematch: Joshua Van vs. Alexandre Pantoja again, September 19 in Los Angeles.</span></div>')

# Top Story replaced with the suspensions story; old top story demoted into Around the Sport is heavy - instead insert new Top Story panel above
rep('Top Story</h2>\n<div class="panel" style="border-left:4px solid var(--acc)">\n<span class="tag">Carried</span><span class="tag acc">Fight week</span><span class="tag">Bantamweight</span>',
 '''Top Story</h2>
<div class="panel" style="border-left:4px solid var(--crit)">
<span class="tag new">New &middot; 4:05</span><span class="tag crit">Suspensions</span><span class="tag">Middleweight</span>
<h3 style="margin:2px 0 9px;font-size:20px">Sacramento&rsquo;s Fight of the Night winners were both suspended six months after a main-event brawl</h3>
<p style="margin:0 0 10px"><b>New at 4:05.</b> <b>Gregory Rodrigues</b> and <b>Anthony Hernandez</b> — the two men who split the <b>$100,000 Fight of the Night</b> award for their five-round main event at UFC Sacramento on <b>August 22</b> — have each been handed <b>six-month suspensions</b> following a <b>brawl</b> connected to that main event (Forbes, August 24).</p>
<p style="margin:0 0 10px">It is an unusual pairing of outcomes on one card: the same bout produced the largest discretionary bonus of the night, the largest disclosed payday (<b>Rodrigues at $340,000</b>, carried on this page since 12:38), <b>and</b> the longest sanction. <span style="color:var(--mut)"><b>What is not stated in the reporting fetched this run, and is therefore not printed:</b> which body issued the suspensions, whether they are medical or disciplinary, whether either man is appealing, when the clock started, and what precisely happened in the brawl. <b>A six-month medical suspension after twenty-five minutes of damage and a six-month disciplinary suspension for fighting outside the bout are very different events, and this page cannot yet tell you which it is.</b> The word used by the source is &ldquo;brawl&rdquo;, and the headline ties it to the main event.</span></p>
</div>

<h2 class="sec">Also Leading — Fight Week</h2>
<div class="panel" style="border-left:4px solid var(--acc)">
<span class="tag">Carried</span><span class="tag acc">Fight week</span><span class="tag">Bantamweight</span>''')

# Results table: fill two blanks
rep('<tr><td class="up"><b>Gregory Rodrigues</b></td><td>def. Anthony Hernandez (main event)</td><td>Unanimous decision (48-47, 49-46, 48-47)</td></tr>\n</tbody></table>',
 '<tr><td class="up"><b>Gregory Rodrigues</b></td><td>def. Anthony Hernandez (main event)</td><td>Unanimous decision (48-47, 49-46, 48-47)</td></tr>\n'
 '<tr><td class="up"><b>MarQuel Mederos</b></td><td>def. Mason Jones (lightweight)</td><td>TKO, round 2 (elbows and punches)</td></tr>\n'
 '<tr><td class="up"><b>Carli Judice</b></td><td>def. Jeisla Chaves (women&rsquo;s flyweight)</td><td>Finish, round 1</td></tr>\n'
 '</tbody></table>')

rep('<div class="note"><b>New at 2:41 — three more finishes are now named, though not their opponents.</b>',
 '<div class="note"><b>New at 4:05 — two of the three blanks are filled, and the table grows for the first time since it was built.</b> Both Performance of the Night winners can now be entered bout-by-bout: <b>MarQuel Mederos stopped Mason Jones by TKO in round two with elbows and punches</b>, and <b>Carli Judice finished Jeisla Chaves in the first round</b>, both at the weights shown. <span style="color:var(--mut)">The exact method of the Judice finish was <b>not</b> stated in the sources fetched this run, so the cell reads &ldquo;Finish, round 1&rdquo; rather than naming a stoppage type. <b>Anthony Wint and Reinier de Ridder remain out of the table</b> — their opponents and methods are still unstated, and a first-round finish is not a result until you can name who it was against. <b>Two of three is not three.</b></span><br><br><b>Carried from 2:41 — three finishes named, not their opponents.</b>')

open(P,'w').write(h); print("mma pass 1:",n)
