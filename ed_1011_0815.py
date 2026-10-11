import re,sys
D=sys.argv[1]
def rd(f): return open(f'{D}/{f}').read()
def wr(f,t): open(f'{D}/{f}','w').write(t)
def rep(t,a,b,n=1):
    c=t.count(a)
    assert c>=1,('MISSING',a[:120])
    if n==1: assert c==1,('MULTI',c,a[:120])
    return t.replace(a,b)
A='style="color:var(--acc2)"'
# ---------------- MMA ----------------
m=rd('mma-briefing.html')
old_mma_tldr=re.search(r'<div class="tldr"><b>Tale of the Tape</b> <span>(.*?)</span></div>',m).group(1)
new_mma_tldr="Brendan Allen submitted Christian Leroy Duncan with a rear-naked choke at 2:46 of the fifth round to win the UFC Vegas 122 main event and extend his UFC win streak to four, taking one of four $100,000 Performance of the Night bonuses; the UFC heads to Edmonton next Saturday for Buckley vs. Malott."
m=m.replace(old_mma_tldr,new_mma_tldr)
m=rep(m,'<span class="mut">UFC Fight Night: Allen vs. Duncan &middot; Sat Oct 10 &middot; main card 8 PM ET &middot; Meta APEX, Las Vegas</span>',
 '<span class="mut">UFC Fight Night: Buckley vs. Malott &middot; Sat Oct 17 &middot; main card 8 PM ET &middot; Rogers Place, Edmonton</span>')
m=rep(m,"new Date('2026-10-10T20:00:00-04:00')","new Date('2026-10-17T20:00:00-04:00')")
# new top story
Y='https://sports.yahoo.com/mma/article/ufc-vegas-122-results-brendan-allen-stops-christian-leroy-duncan-with-late-choke-calls-out-ex-champ-030151648.html'
LK='https://www.lowkickmma.com/brendan-allen-gets-it-done-late-against-christian-leroy-duncan-at-ufc-vegas-122/'
LKM='https://www.lowkickmma.com/ufc-vegas-122-brendan-allen-vs-christian-leroy-duncan-main-card-results-highlights/'
HV='https://heavy.com/sports/ufc/ufc-vegas-122-bonuses-revealed-following-fun-card/'
UE='https://www.ufc.com/news/pivotal-welterweight-bout-between-joaquin-buckley-and-mike-malott-headlines-ufc-return'
top=f'''<div class="lead" style="border-left-color:var(--acc)"><span class="tag new">New</span><h3>Brendan Allen chokes out Christian Leroy Duncan in the fifth round at UFC Vegas 122</h3>
<p>Brendan Allen beat Christian Leroy Duncan by submission (rear-naked choke) at 2:46 of round five in Saturday&rsquo;s UFC Vegas 122 main event at the Meta APEX, extending his UFC win streak to four straight; Uncrowned lists him at 28-7 (<a href="{Y}" {A}>Uncrowned via Yahoo Sports</a>). LowKick MMA&rsquo;s recap: Duncan stunned Allen with elbows and a spinning attack in a close first round, lost a point for an eye poke early in the second, and was controlled on the mat through the middle rounds before Allen took his back in the fifth and forced the tap (<a href="{LK}" {A}>LowKick MMA</a>). &ldquo;I&rsquo;m steady, defending my spot, doing what I need to do,&rdquo; Allen said afterward. &ldquo;Fight the champion, and if not, where&rsquo;s [Dricus du Plessis]?&rdquo; (<a href="{Y}" {A}>Uncrowned</a>).</p>
<p>The UFC paid four $100,000 Performance of the Night bonuses &mdash; to Allen, Andre Fili (head-kick KO of Kai Kamaka III), Otari Tanzilovi (KO of Malcolm Wellmaker) and Alice Pereira (TKO of Daria Zhelezniakova) &mdash; and no Fight of the Night. $25,000 finish bonuses went to Julius Walker, Francisco Prado, Niko Price and Allen Frye Jr.; Brendson Ribeiro&rsquo;s upset guillotine of Felipe Franco did not qualify because he missed weight. Gerald Meerschaert announced his retirement after losing to Walker, and Price won what Heavy called his retirement fight (<a href="{HV}" {A}>Heavy</a>).</p></div>
'''
i=m.find('<h2 class="sec">Top Story</h2>')
assert i>0
m=m[:i+len('<h2 class="sec">Top Story</h2>\n')]+top+m[i+len('<h2 class="sec">Top Story</h2>\n'):]
# rename old top story heading slightly
m=rep(m,'<h3>Silva wins the vacant women&rsquo;s flyweight title; UFC 332 sets knockout records</h3>','<h3>Last week: Silva wins the vacant women&rsquo;s flyweight title; UFC 332 sets knockout records</h3>')
# remove Oct 10 fight-week card
i=m.find('<h2 class="sec">Fight Week')
s=m.find('<div class="card">',i); e=m.find('<div class="card">',s+20)
assert 'Allen vs. Duncan' in m[s:e] and 'OCT 17' in m[e:e+200]
m=m[:s]+m[e:]
m=rep(m,'<p>Welterweights Joaquin Buckley and Mike Malott headline the UFC&rsquo;s return to Edmonton.</p>',
 f'<p>Welterweights Joaquin Buckley and Mike Malott headline the UFC&rsquo;s return to Edmonton. <span class="tag new">New</span> The UFC lists prelims at 6 PM ET and the main card at 8 PM ET on Sportsnet and TVA Sports (<a href="{UE}" {A}>UFC.com</a>). No sportsbook line for the main event was found this run.</p>')
# last event
s=m.find('<h2 class="sec">Last Event'); e=m.find('<h2 class="sec">Prospect Watch')
rows=[('Allen def. Duncan','Middleweight (main event)','SUB (rear-naked choke), 2:46 R5'),
('Disputed: Camilo / Herbert','Lightweight (co-main)','UD (29-28 x3) &mdash; winner disputed, see note'),
('Godínez def. Souza','117-lb catchweight','UD (29-28 x3)'),
('Fili def. Kamaka III','Featherweight','KO (head kick), 0:22 R2'),
('Tanzilovi def. Wellmaker','Bantamweight','KO (head kick and punches), 2:39 R2'),
('Walker def. Meerschaert','Light heavyweight','TKO (punches), 3:35 R2'),
('Prado def. Bonfim','163.5-lb catchweight','TKO (punches), 4:23 R1'),
('Price def. Shahbazyan','Welterweight','TKO (punch and knee), 1:58 R1'),
('Ribeiro def. Franco','208.5-lb catchweight','SUB (mounted guillotine), 1:49 R1'),
('Frye def. Harris','Heavyweight','KO (punches), 2:59 R1'),
('Pereira def. Zhelezniakova','Women&rsquo;s bantamweight','TKO (doctor stoppage), 5:00 R1'),
('Draw: Gatto vs. Kareckaite','Women&rsquo;s flyweight','Majority draw (29-27, 28-28, 28-28)')]
tr=''
for r,b,mm in rows:
    cls='up' if ' def. ' in r else 'warn'
    tr+=f'<tr><td class="{cls}">{r.replace("Godínez","God&iacute;nez")}</td><td>{b}</td><td>{mm}</td></tr>\n'
le=f'''<h2 class="sec">Last Event &mdash; Results</h2>
<div class="panel"><div class="mono" style="color:var(--acc2);font-size:12px;margin-bottom:8px">UFC VEGAS 122: ALLEN VS. DUNCAN &middot; OCT 10 &middot; META APEX, LAS VEGAS</div> <span class="tag new">New</span>
<table><tr><th>Result</th><th>Bout</th><th>Method</th></tr>
{tr}</table>
<p class="note"><b>Bonuses:</b> no Fight of the Night; $100,000 Performance of the Night to Brendan Allen, Andre Fili, Otari Tanzilovi and Alice Pereira; $25,000 finish bonuses to Julius Walker, Francisco Prado, Niko Price and Allen Frye Jr. (<a href="{HV}" {A}>Heavy</a>). Results and times: <a href="{Y}" {A}>Uncrowned via Yahoo Sports</a>; main event confirmed by the UFC&rsquo;s official result as quoted by <a href="{LK}" {A}>LowKick MMA</a>. <b>Co-main conflict:</b> Uncrowned lists &ldquo;Matheus Camilo def. Jai Herbert via unanimous decision (29&ndash;28, 29&ndash;28, 29&ndash;28)&rdquo;; LowKick MMA&rsquo;s main-card results list &ldquo;Jai Herbert defeated Matheus Camilo by unanimous decision (29-28 x 3)&rdquo; (<a href="{LKM}" {A}>LowKick MMA</a>). This desk could not break the tie this run, so no winner is printed. Spellings follow Uncrowned (&ldquo;Daria Zhelezniakova&rdquo;, &ldquo;Loopy God&iacute;nez&rdquo;).</p></div>

'''
m=m[:s]+le+m[e:]
# champions note
m=rep(m,'Re-checked this edition (Sat Oct 10, ~8:35 AM ET): no UFC event since UFC 332 &mdash; tonight&rsquo;s UFC Vegas 122 is a non-title card;',
 'Re-checked this edition (Sun Oct 11, ~8:15 AM ET): UFC Vegas 122 (Oct 10) was a non-title card, so no belt changed hands; ESPN&rsquo;s champions page again returned no content to this desk&rsquo;s fetch, so the board stands on the standing corrections record. Earlier (Sat Oct 10, ~8:35 AM ET): no UFC event since UFC 332;')
# sources
m=rep(m,'<div class="srcs">Sources: ',f'<div class="srcs">Sources: <a href="{Y}">Uncrowned via Yahoo Sports (UFC Vegas 122 results, Oct 11)</a> &middot; <a href="{LK}">LowKick MMA (Allen vs. Duncan recap)</a> &middot; <a href="{LKM}">LowKick MMA (main-card results)</a> &middot; <a href="{HV}">Heavy (UFC Vegas 122 bonuses)</a> &middot; <a href="{UE}">UFC.com (Buckley vs. Malott)</a> &middot; ')
wr('mma-briefing.html',m)

# ---------------- CYBER ----------------
c=rd('cyber-briefing.html')
old_c_tldr=re.search(r'<div class="tldr"><b>The Wire</b> <span>(.*?)</span></div>',c).group(1)
new_c_tldr="Today, Sunday, Oct. 11, is CISA&rsquo;s deadline for federal agencies to patch five older flaws &mdash; in ProFTPD, ONLYOFFICE Docs, Strapi, Apache Struts and ISC BIND &mdash; exploited by China-linked Flax Typhoon, while exploited NetScaler CVE-2026-88779 is now four days past its Oct. 7 deadline and attackers keep probing unpatched Atlassian Data Center instances."
c=c.replace(old_c_tldr,new_c_tldr)
c=rep(c,'is three days past its Oct. 7 federal deadline','is four days past its Oct. 7 federal deadline, the five Flax Typhoon KEV entries fall due today,')
c=rep(c,'<div class="n">3 days</div><div class="l">Overdue:','<div class="n">4 days</div><div class="l">Overdue:')
c=rep(c,'federal deadline <b>Wednesday, October 7, 2026</b> <b class="critc">(3 days overdue)</b>','federal deadline <b>Wednesday, October 7, 2026</b> <b class="critc">(4 days overdue)</b>')
c=rep(c,'<b>Due Sunday:</b> the five','<b>Due TODAY (Sun. Oct 11):</b> the five')
c=c.replace('<b class="warnc">(1 day left &mdash; due tomorrow)</b>','<b class="critc">(0 days left &mdash; due today)</b>')
c=rep(c,'due Oct 5 <b class="critc">(5 days overdue)</b>','due Oct 5 <b class="critc">(6 days overdue)</b>')
c=rep(c,'due Oct 4 <b class="critc">(6 days overdue)</b>','due Oct 4 <b class="critc">(7 days overdue)</b>')
c=rep(c,'(Oct 3, <b class="critc">6 days overdue</b>)','(due Oct 3, <b class="critc">8 days overdue</b>)')
c=rep(c,'(Oct 2, <b class="critc">7 days overdue</b>)','(due Oct 2, <b class="critc">9 days overdue</b>)')
c=rep(c,'(Sept 30, <b class="critc">9 days overdue</b>','(due Sept 30, <b class="critc">11 days overdue</b>')
c=rep(c,'due <b>Oct 4, 2026</b> <b class="critc">(6 days overdue)</b>','due <b>Oct 4, 2026</b> <b class="critc">(7 days overdue)</b>')
c=rep(c,'due <b>Oct 5, 2026</b> <b class="critc">(5 days overdue)</b>','due <b>Oct 5, 2026</b> <b class="critc">(6 days overdue)</b>')
c=rep(c,'due <b>Oct 7, 2026</b> <b class="critc">(3 days overdue)</b>','due <b>Oct 7, 2026</b> <b class="critc">(4 days overdue)</b>')
c=rep(c,'due <b>Oct 3, 2026</b> <b class="critc">(7 days overdue)</b>','due <b>Oct 3, 2026</b> <b class="critc">(8 days overdue)</b>')
c=rep(c,'due <b>Oct 2, 2026</b> <b class="critc">(8 days overdue)</b>','due <b>Oct 2, 2026</b> <b class="critc">(9 days overdue)</b>')
c=rep(c,'due <b>Sept 30, 2026</b> <b class="critc">(10 days overdue)</b>','due <b>Sept 30, 2026</b> <b class="critc">(11 days overdue)</b>')
wr('cyber-briefing.html',c)

# ---------------- WALL STREET ----------------
w=rd('wallstreet-briefing.html')
old_w_tldr=re.search(r'<div class="tldr"><b>The Tape</b> <span>(.*?)</span></div>',w).group(1)
new_w_tldr="Markets are closed for the weekend after stocks closed higher Friday &mdash; the Dow up 0.83%, the Nasdaq 0.64% and the S&amp;P 500 0.59% &mdash; to cap a winning week; JPMorgan, Goldman Sachs, Citigroup and Wells Fargo open bank earnings Tuesday, with September CPI due Wednesday."
w=w.replace(old_w_tldr,new_w_tldr)
K='https://www.kitco.com/news/off-the-wire/2026-10-09/wall-st-week-ahead-bank-earnings-cpi-headline-busy-markets-week-sp-500'
w=rep(w,'<p><b>Weekend (Sat. Oct 10, ~8 AM ET; re-checked ~6:35 PM).</b>',
 f'<p><span class="tag new">New</span> <b>Week ahead (Sun. Oct 11, ~8:15 AM ET).</b> JPMorgan, Goldman Sachs, Citigroup and Wells Fargo report Tuesday, and Morgan Stanley and Bank of America on Wednesday, &ldquo;rounding out reports from the six largest lenders,&rdquo; Reuters wrote Friday; Johnson &amp; Johnson, UnitedHealth and BlackRock also report. S&amp;P 500 third-quarter earnings are expected to have jumped by more than 30%, per LSEG IBES, while the S&amp;P 500 banks index is down 9% over the past month amid rising Treasury yields. Wednesday&rsquo;s September CPI is expected to show a 3.6% annual rise (core 2.5%) in a Reuters poll &mdash; among the last key releases before the Fed&rsquo;s Oct. 27&ndash;28 meeting, after it &ldquo;hiked rates last month for the first time since 2023.&rdquo; Reuters put the 10-year yield &ldquo;last around 5.23%, after recently reaching its highest level in 24 years&rdquo; (<a href="{K}" {A}>Reuters via Kitco, Oct. 9</a>).</p>\n<p><b>Weekend (Sat. Oct 10, ~8 AM ET; re-checked Sun. ~8:15 AM).</b>')
wr('wallstreet-briefing.html',w)
# sources footer for ws
w=rd('wallstreet-briefing.html')
i=w.find('Sources:',w.rfind('<footer'))
assert i>0
w=w[:i+len('Sources: ')]+f'<a href="{K}">Reuters via Kitco (Wall St Week Ahead, Oct 9)</a> &middot; '+w[i+len('Sources: '):]
wr('wallstreet-briefing.html',w)

# ---------------- INDEX ----------------
x=rd('index.html')
x=rep(x,old_c_tldr,new_c_tldr); x=rep(x,old_w_tldr,new_w_tldr); x=rep(x,old_mma_tldr,new_mma_tldr)
wr('index.html',x)
print('ok')
