import io
P='/sessions/optimistic-youthful-curie/mnt/outputs/mma-briefing.html'
s=io.open(P,encoding='utf-8').read()
n=0
def R(old,new):
    global s,n
    c=s.count(old); assert c==1,('COUNT %d for: %s'%(c,old[:110]))
    s=s.replace(old,new); n+=1

# 1 — the rankings disagreement gains a THIRD variant this run
R('<p style="margin:0;color:var(--mut);font-size:13.6px"><b>Rankings, unresolved:</b> UFC.com\'s own preview headline bills the fight as "#3 Umar Nurmagomedov and #5 Song Yadong," while a summary of the same coverage describes them as ranked No. 2 and No. 6 at 135 pounds. Both readings are printed; neither is adopted, and no numeric rank is asserted here for either man.</p>',
  '<p style="margin:0;color:var(--mut);font-size:13.6px"><b>Rankings, unresolved — and now three-way.</b> UFC.com\'s own preview headline bills the fight as <b>"#3 Umar Nurmagomedov and #5 Song Yadong,"</b> and that wording was re-confirmed verbatim again this run. A summary of the same coverage has described them as <b>No. 2 and No. 6</b>. A third read fetched this run gives <b>#3 and #6</b>. All three are printed; none is adopted, and <b>no numeric rank is asserted here for either man</b>. <b>Context, without a causal claim:</b> UFC began transitioning its official rankings away from the traditional media panel toward the data-determined <b>Meta UFC Rankings</b> on <b>June 22, 2026</b> (UFC.com). This page records that alongside the disagreement; no source seen this run connects the two, and none is asserted to.</p>')

# 2 — Rankings & Business block
R('<p style="margin:0 0 9px"><b>Rankings movement.</b> The only ranking dispute live this run is the Shanghai main event itself: UFC.com bills the fighters as <b>#3 and #5</b> at bantamweight, while a summary of the same coverage puts them at <b>No. 2 and No. 6</b>. Both are recorded; neither is adopted.</p>',
  '<p style="margin:0 0 9px"><b>Rankings movement.</b> The only ranking dispute live this run is the Shanghai main event itself, and it has widened from two readings to three: UFC.com\'s headline says <b>#3 and #5</b>, a summary of the same coverage says <b>No. 2 and No. 6</b>, and a third read this run says <b>#3 and #6</b>. All are recorded; none is adopted.</p>\n<p style="margin:0 0 9px"><b>The ranking system itself is mid-transition.</b> On <b>June 22, 2026</b>, UFC and its official fan technology partner <b>Meta</b> announced the <b>Meta UFC Rankings</b>, and UFC began moving its official rankings from the traditional media panel to a system "determined entirely by fight data" (UFC.com). <span style="color:var(--mut)">Recorded as a sourced fact about the sport. This page does <b>not</b> assert that the transition explains the conflicting rank numbers above — no source seen this run makes that link.</span></p>')

# 3 — Prospect Watch week 3: full card with methods, now verified
R('<h3>Week 3 — five fights, five contracts, and a record upset</h3><p>All five winners on <b>August 25</b> left with UFC deals. In the featured bout, bantamweight <b>Alex Apodaca</b> beat <b>Bella Mir</b> — daughter of former UFC heavyweight champion Frank Mir — by unanimous decision, <b>29-28 on all three cards</b>. Mir had been a <b>−6000</b> favourite and Apodaca a <b>+1200</b> underdog, described as the <b>biggest upset in Contender Series history</b>. Joining her on the roster: <b>Ronald Humphrey</b> (first-round submission of Alexis Miranda), <b>Sean Clancy Jr.</b>, <b>Nick Galanti</b> and <b>Guilherme Uriel</b>, the quartet all winning by finish.</p></div>',
  '<h3>Week 3 — five fights, five contracts, and a record upset (now with every method verified)</h3><p>All five winners on <b>August 25</b> at the UFC Apex left with contracts, and the full card is now sourced with methods and times: <b>Alex Apodaca def. Bella Mir</b> by unanimous decision, <b>29-28 on all three cards</b>; <b>Guilherme Uriel def. Mario Piazzon</b> by submission (guillotine choke), <b>R1, 0:50</b>; <b>Sean Clancy Jr. def. Gary Balleto</b> by TKO, <b>R2, 3:54</b>; <b>Ronald Humphrey def. Alexis Miranda</b> by submission (rear-naked choke), <b>R1, 4:03</b>; and <b>Nick Galanti def. Carlos Petruzzella</b> by KO, <b>R1, 0:35</b>. Mir — daughter of former UFC heavyweight champion Frank Mir — had been a <b>−6000</b> favourite and Apodaca a <b>+1200</b> underdog, reported as the <b>biggest upset in Contender Series history</b>. <span style="color:var(--mut)">The prior edition named the five winners but could source a method for only two of them; the other three, and all five opponents, are added here. Ten fighters competed across the five bouts. (Sports Illustrated)</span></p></div>')

# 4 — Top story tag / freshness stamp
R('<div class="tldr"><b>Tale of the Tape</b> <span>It is fight week in Shanghai: bantamweight contenders Umar Nurmagomedov and Song Yadong headline Saturday\'s card at the Oriental Sports Center, with Nurmagomedov roughly a −500 favourite.</span></div>',
  '<div class="tldr"><b>Tale of the Tape</b> <span>It is fight week in Shanghai: bantamweight contenders Umar Nurmagomedov and Song Yadong headline Saturday\'s card at the Oriental Sports Center, with Nurmagomedov roughly a −500 favourite and official weigh-ins due Friday.</span></div>')

io.open(P,'w',encoding='utf-8').write(s)
print('mma edits applied:',n)
