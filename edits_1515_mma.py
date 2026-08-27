# -*- coding: utf-8 -*-
p='mma-briefing.html'
s=open(p,encoding='utf-8').read()
def rep(old,new,label):
    global s
    assert old in s, "NOT FOUND: "+label
    assert s.count(old)==1, "NOT UNIQUE: "+label
    s=s.replace(old,new,1); print("ok:",label)

# M1 tldr
rep("Saturday's Shanghai card at the Oriental Sports Center is headlined by bantamweight contenders Umar Nurmagomedov and Song Yadong, with Nurmagomedov at −500 on two of the three lines seen today and −470 on the third",
"Saturday's Shanghai card at the Oriental Sports Center is headlined by bantamweight contenders Umar Nurmagomedov and Song Yadong, and a fourth line seen at 3:15 has moved the favourite out to −550 / +400, wider than the −500 and −470 this page had been calling stable",
'M1 tldr')

# M2 odds paragraph rebuild
rep("<b>Odds:</b> Nurmagomedov <b>−500</b> / Song <b>+380</b> consensus (roughly 80% / 20% implied); <b>MMAOddsBreaker's opening line was −500 / +385</b>; DraftKings opened the fight at <b>−470 / +360</b>. <span style=\"color:var(--mut)\">All three reads are printed and none averaged; the favourite's price is stable across them, and the spread sits on the underdog side.</span>",
"<b>Odds:</b> Nurmagomedov <b>−500</b> / Song <b>+380</b> consensus (roughly 80% / 20% implied); <b>MMAOddsBreaker's opening line was −500 / +385</b>; DraftKings opened the fight at <b>−470 / +360</b>. <b>New at 3:15 — a fourth line, and it breaks the claim this card was carrying.</b> RotoWire lists the fight at <b>Nurmagomedov −550 / Song +400</b>. <span style=\"color:var(--mut)\"><b>Until this read, this card said the favourite's price was &ldquo;stable across&rdquo; the lines. It is not, and the sentence is replaced rather than left standing.</b> The four reads now run −470, −500, −500 and −550, a range of eighty cents on the favourite, and the underdog has moved with it from +360 to +400. What can still be said accurately is narrower and worth saying: <b>every line seen has Nurmagomedov a heavy favourite</b>, from roughly 82% to 85% implied before the vig, and the spread is widening rather than converging as the card approaches. <b>All four are printed, none is averaged, and no book is named as the market.</b></span>",
'M2 odds')

# M3 rest of card
rep("<b>Alex Perez vs. Su Mudaerji</b>, a rematch — their first meeting in <b>May</b> ended prematurely after a low blow.",
"<b>Alex Perez vs. Su Mudaerji</b>, a rematch — their first meeting in <b>May</b> ended prematurely after a low blow. <b>New at 3:15 — the rest of the card is now listed, and one blank from 2:21 is filled.</b> Also on the main card: <b>Liu Ce vs. Levi Rodrigues Jr.</b> and <b>Bilal Hasan vs. Nilson Rojas</b> — Hasan is the Contender Series week-one signing this page noted at 2:21 as making his debut here <i>with no opponent named</i>; Rojas is that opponent. On the preliminary card: <b>Namsrai Batbayar vs. Andre Lima</b>, <b>Rei Tsuruya vs. Kevin Borjas</b> and <b>Jack Jenkins vs. Sean Woodson</b>. <span style=\"color:var(--mut)\"><b>Two spelling splits are recorded, not resolved.</b> This card carries <b>Qileng Aori</b> and <b>Su Mudaerji</b> from earlier listings; the listing fetched at 3:15 renders them <b>Aoriqileng</b> and <b>Sumudaerji</b>. Both forms are printed and neither is adopted, on the same footing as the Balleto / Balletto split further down this page. Chinese names appear in Anglicised listings in more than one order and this page will not guess which is the fighter&rsquo;s own preference.</span>",
'M3 rest of card')

# M4 sources
rep('<footer><b style="color:var(--ink)">Sources</b><ul class="bul"><li><b>Fetched 2:41 PM ET</b>',
'<footer><b style="color:var(--ink)">Sources</b><ul class="bul">'
'<li><b>Fetched 3:15 PM ET</b> — RotoWire, <a href="https://www.rotowire.com/betting/mma/fight/yadong-song-vs-umar-nurmagomedov-odds-2026-08-29-5429">Nurmagomedov vs Song Aug 29, 2026 Odds</a> — Nurmagomedov −550, Song +400.</li>'
'<li><b>Fetched 3:15 PM ET</b> — Yahoo Sports, <a href="https://sports.yahoo.com/articles/ufc-shanghai-best-betting-props-031100716.html">UFC Shanghai best betting props, parlays and picks</a> — full main card and prelims, including Bilal Hasan vs. Nilson Rojas; main card 6:00 a.m. ET, stream from 3 a.m. ET on Paramount+.</li>'
'<li><b>Fetched 3:15 PM ET</b> — UFC.com, <a href="https://www.ufc.com/event/ufc-fight-night-august-29-2026">UFC Fight Night: Nurmagomedov vs Song</a> — Aug 29, 2026, Shanghai Oriental Sports Center.</li>'
'<li><b>Fetched 3:15 PM ET</b> — ESPN, <a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">Current and all-time UFC champions</a> — Aspinall, Ulberg, Strickland, Makhachev, Gaethje and Volkanovski confirmed against the source this run.</li>'
'<li><b>Fetched 2:41 PM ET</b>',
'M4 sources')

open(p,'w',encoding='utf-8').write(s)
print("WROTE",p,len(s))
