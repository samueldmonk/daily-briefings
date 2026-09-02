# -*- coding: utf-8 -*-
import shared, io

ACCENT = "#e84545"; ACCENT2 = "#ff8a5c"
SUMMARY = ("UFC 332 has lost its main event a month out after women's flyweight champion Valentina "
           "Shevchenko withdrew injured from a title defence against Natalia Silva, leaving the October 3 "
           "card in Salt Lake City listed as TBD vs. TBD.")

CDN_JS = """<script>(function(){
var target=new Date('2026-09-05T16:00:00Z');
function tick(){var el=document.getElementById('ufccdn');if(!el)return;
var d=target-new Date();
if(d<=0){el.textContent='Fight week \\u2014 live/completed';return;}
var days=Math.floor(d/86400000),h=Math.floor(d%86400000/3600000),m=Math.floor(d%3600000/60000);
el.textContent=days+'d '+h+'h '+m+'m';}
tick();setInterval(tick,30000);})();</script>"""

body = []
A = body.append

A('<header class="mast">')
A('<h1>&#8856; The Octagon</h1>')
A('<p class="tag">Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting</p>')
A(shared.META)
A('</header>')
A(f'<div class="tldr"><b>Tale of the Tape</b> <span>{SUMMARY}</span></div>')
A('<p class="freshline" id="freshline">&nbsp;</p>')
A(shared.nav("mma", ACCENT))

# Countdown
A('<div class="cdn">')
A('<span class="lbl">Next card</span>')
A('<span class="clk" id="ufccdn">&nbsp;</span>')
A('<span class="ev">UFC Fight Night: Hooker vs. Parnasse &mdash; Saturday, September 5, Accor Arena, Paris. '
  'Prelims 12 PM ET, main card 3 PM ET on Paramount+.</span>')
A('</div>')

# Top story
A('<h2 class="sec">Top Story</h2>')
A('<div class="lead">')
A('<h3>UFC 332 has no main event: Valentina Shevchenko pulls out injured, and Salt Lake City is left with '
  'TBD vs. TBD</h3>')
A('<p>The expected UFC 332 headliner &mdash; women\'s flyweight champion <b>Valentina Shevchenko</b> defending '
  'against Brazil\'s <b>Natalia Silva</b>, who is riding a <b>14-fight win streak</b> &mdash; has been '
  'cancelled after Shevchenko suffered an injury and withdrew. The news was first reported by the Brazilian '
  'outlet Ag. Fight on Tuesday afternoon.</p>')
A('<p><b>UFC 332 is set for Saturday, October 3, 2026 at the Delta Center in Salt Lake City, Utah</b>, and with '
  'roughly a month to go it now has <b>neither a main event nor a co-main event</b>. The card is listed on '
  'the UFC\'s own website as <b>TBD vs. TBD</b>.</p>')
A('<p>Bloody Elbow reported today that a replacement main event <b>will be announced this week</b>. Names '
  'floated in the coverage include <b>Josh Hokit</b>, <b>Charles Oliveira</b> and <b>Khamzat Chimaev</b> &mdash; '
  'including the possibility of a <b>Chimaev vs. Strickland 2</b> middleweight title bout. These are reported '
  'as possibilities only; nothing has been announced, and no booking is asserted here.</p>')
A('</div>')

# Upcoming
A('<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>')
A('<div class="cards">')

A('<div class="card"><div class="tags"><span class="t new">This week</span></div>'
  '<p class="mono" style="color:var(--accent2);margin:0 0 6px">SAT SEP 5 &middot; ACCOR ARENA, PARIS</p>'
  '<h3>UFC Fight Night: Hooker vs. Parnasse</h3>'
  '<p>A five-round lightweight main event: <b>Dan Hooker</b> (24-14 professional, 14-10 in the UFC) against '
  '<b>Salahdine Parnasse</b>, who makes his UFC debut in a headliner. Parnasse is a former two-time KSW '
  'featherweight champion and one-time KSW lightweight champion who signed with the UFC in late July 2026 '
  'after previously turning the promotion down &mdash; he did <i>not</i> come through the Contender Series. '
  'Fourteen fights; prelims 12 PM ET, main card 3 PM ET on Paramount+.<br><br>'
  '<b>Odds:</b> Parnasse &minus;667 / Hooker +417 (Rotowire); DraftKings has &minus;600 / +440. The market '
  'range runs &minus;500 to &minus;700 and +360 to +450, and it has moved hard toward the Frenchman since '
  'opening at roughly &minus;400 / +300.<br><br>'
  '<b>Card change (carried from the previous edition):</b> Mairon Santos is out against Nathaniel Wood with '
  'illness, replaced by undefeated newcomer <b>Pavel Andrusca</b>, who has finished seven of his eight wins, '
  'five in the first round. His full won-loss record was not stated in anything fetched, so none is printed.'
  '</p></div>')

A('<div class="card">'
  '<p class="mono" style="color:var(--accent2);margin:0 0 6px">SAT SEP 12 &middot; DESERT DIAMOND ARENA, GLENDALE, AZ</p>'
  '<h3>Noche UFC &mdash; UFC Fight Night 288</h3>'
  '<p>Carried from the previous edition: <b>Jean Silva (17-3) vs. Jose Miguel Delgado (12-2)</b> headlines '
  'after Yair Rodr&iacute;guez withdrew injured. Also booked: Moreno vs. Joseph Morales, Fiorot vs. Grasso, '
  'and Blaydes vs. Cortes-Acosta. No odds were sourced for this card this run.</p></div>')

A('<div class="card">'
  '<p class="mono" style="color:var(--accent2);margin:0 0 6px">SAT SEP 19 &middot; CRYPTO.COM ARENA, LOS ANGELES</p>'
  '<h3>UFC 331: Van vs. Pantoja 2</h3>'
  '<p>A <b>flyweight title rematch</b>: champion <b>Joshua Van</b> against <b>Alexandre Pantoja</b>, across '
  'thirteen fights. Prelims 6 PM ET, main card 9 PM ET on Paramount+. Carried from the previous edition: '
  'Pantoja injured an elbow 23 seconds into the first fight at UFC 323; Tsarukyan vs. Ruffy and Moicano vs. '
  'Ortega are also booked at 155. No odds were sourced for this card this run.</p></div>')

A('<div class="card">'
  '<p class="mono" style="color:var(--accent2);margin:0 0 6px">SAT SEP 26 &middot; META APEX, LAS VEGAS</p>'
  '<h3>UFC Fight Night 289</h3>'
  '<p>An aggregator lists the headliner as <b>Rosas Jr. vs. Barcelos</b>; the venue is confirmed as the Meta '
  'Apex in Enterprise, Nevada by a separate schedule source. The billing is attributed rather than adopted, and '
  'no odds were sourced.</p></div>')

A('<div class="card"><div class="tags"><span class="t crit">Main event vacated</span></div>'
  '<p class="mono" style="color:var(--accent2);margin:0 0 6px">SAT OCT 3 &middot; DELTA CENTER, SALT LAKE CITY</p>'
  '<h3>UFC 332 &mdash; TBD vs. TBD</h3>'
  '<p>See today\'s top story: Shevchenko vs. Silva is off, and the card currently has no main event and no '
  'co-main event. A replacement headliner is expected to be announced this week.</p></div>')

A('<div class="card">'
  '<p class="mono" style="color:var(--accent2);margin:0 0 6px">SAT OCT 24 &middot; ETIHAD ARENA, ABU DHABI</p>'
  '<h3>UFC 333 &mdash; two titles</h3>'
  '<p>Carried from the previous edition, where it was sourced for the first time with the title billing '
  'attached: a <b>featherweight championship</b> bout, <b>Alexander Volkanovski vs. Movsar Evloev</b>, with a '
  '<b>bantamweight title</b> co-main, <b>Petr Yan vs. Merab Dvalishvili</b>. Main card 2 PM ET on Paramount+.'
  '</p></div>')
A('</div>')

# Last event
A('<h2 class="sec">Last Event &mdash; UFC Fight Night: Nurmagomedov vs. Song</h2>')
A('<p class="note" style="margin-bottom:10px">Saturday, August 29, 2026 &middot; Oriental Sports Center, '
  'Shanghai &middot; 13 fights</p>')
A('<div class="panel" style="padding:6px 8px"><table>')
A('<tr><th>Result</th><th>Bout</th><th>Method</th></tr>')
A('<tr><td class="up"><b>Song Yadong</b></td><td>def. Umar Nurmagomedov</td>'
  '<td>KO (right uppercut), R2 1:48</td></tr>')
A('</table></div>')
A('<p class="note">Only bouts where the winner, the opponent and the method were all confirmed in sources '
  'fetched this run are tabled. Carried from the previous edition and not re-sourced: Bilal Hasan beat Nilson '
  'Rojas by single-punch knockout, and Song was close to a 5-1 underdog at DraftKings, dropping Nurmagomedov '
  'with a short right hand before the finish.</p>')

A('<div class="panel" style="margin-top:14px">')
A('<p style="margin:0 0 8px"><b>Performance bonuses.</b> The UFC paid <b>$400,000 across the headline awards</b>, '
  'at <b>$100,000 each</b>: <b>Performance of the Night</b> to <b>Song Yadong</b> and <b>Bilal Hasan</b>, and '
  '<b>Fight of the Night</b> to <b>Liu Ce vs. Levi Rodrigues Jr.</b>, with both men paid.</p>')
A('<p style="margin:0">Additional <b>$25,000</b> stoppage bonuses are reported for <b>Denise Gomes, Kai '
  'Asakura, Andre Lima, Rei Tsuruya, Francesco Nuzzi, Hector Santiago and Julia Polastri</b>. '
  '<b>No count is asserted:</b> the source names seven fighters in one sentence and says "five more fighters '
  'collected" in the next, so the two cannot both be right.</p>')
A('</div>')

# Prospect watch
A('<h2 class="sec">Prospect Watch</h2>')
A('<div class="cards">')
A('<div class="card"><div class="tags"><span class="t ok">Prospect</span><span class="t">Debut</span></div>'
  '<h3>Pavel Andrusca &mdash; undefeated, short notice, Paris</h3>'
  '<p>Steps in against Nathaniel Wood on Saturday after Mairon Santos withdrew ill. Undefeated, with '
  '<b>seven of eight wins by finish and five in the first round</b>. His full record has not been stated in any '
  'source fetched, so none is printed. Carried from the previous edition.</p></div>')
A('<div class="card"><div class="tags"><span class="t ok">Prospect</span><span class="t">Debut</span></div>'
  '<h3>Salahdine Parnasse &mdash; a main event on debut</h3>'
  '<p>23-2, and a former <b>two-time KSW featherweight champion and one-time KSW lightweight champion</b> '
  '&mdash; 14-2 inside KSW with four defences of the lightweight belt. He signed with the UFC in late July 2026 '
  'having previously turned the promotion down, and made his U.S. debut in May 2026 on the Rousey vs. Carano '
  'main card with a first-round stoppage of Kenneth Cross for a fifth straight win. He is a UFC debutant, not a '
  'ranked contender, and he did not come through the Contender Series.</p></div>')
A('</div>')

# Around the sport
A('<h2 class="sec">Around the Sport</h2>')
A('<div class="panel"><ul class="bul">')
A('<li><b>Shanghai\'s post-fight scene is still unresolved.</b> Carried from the previous edition: '
  '<b>Usman Nurmagomedov</b>, the PFL lightweight champion, leapt the fence after the knockout, shoved a '
  'celebrating Song and appeared to nearly elbow him. No disciplinary outcome has been sourced, so none is '
  'stated &mdash; and no family relationship between the two Nurmagomedovs is asserted, because no source '
  'fetched states one.</li>')
A('<li><b>Contender Series dates return a third way, and are refused again.</b> This run\'s search places '
  'Dana White\'s Contender Series on <b>September 15 and September 22</b>; earlier runs returned September 8, '
  'and before that September 15 for the same week. All are printed, none adopted, and no card or results are '
  'carried from it &mdash; a previous run surfaced a contract-winners list whose names did not correspond to '
  'any fighter on the card returned by the same search.</li>')
A('<li><b>UFC 332\'s replacement headliner is the week\'s live question.</b> With the card a month out and '
  'listed as TBD vs. TBD, the promotion has an unusually short runway to sell a pay-per-view; watch for the '
  'announcement Bloody Elbow says is coming this week.</li>')
A('</ul></div>')

# Rankings & business
A('<h2 class="sec">Rankings &amp; Business</h2>')
A('<div class="panel">')
A('<p style="margin:0 0 10px"><b>Rankings movement.</b> Carried from the previous edition, where it was sourced: '
  'ESPN wrote that Song Yadong\'s knockout of Umar Nurmagomedov "immediately puts him in the thick of the title '
  'conversation at 135 pounds" and called it the biggest win of his career. <b>No ranking number is asserted</b>, '
  'because none has been stated in any source fetched.</p>')
A('<p style="margin:0"><b>Business &amp; broadcast.</b> <b>No figures are printed.</b> No viewership number, '
  'gate, attendance or TKO Group financial figure was stated in anything fetched this run. The only broadcast '
  'facts carried are distribution: Paris, Noche UFC and UFC 331 all stream on Paramount+, and UFC 333\'s main '
  'card is set for 2 PM ET with no pay-per-view.</p>')
A('</div>')

# Champions
A('<h2 class="sec">Champions Board</h2>')
A('<div class="panel" style="padding:6px 8px"><table>')
A('<tr><th>Division</th><th>Champion</th><th>Note</th></tr>')
champs = [
 ("Heavyweight", "Tom Aspinall", "Undisputed. <b>Interim:</b> Ciryl Gane (KO2 Pereira, Freedom 250, June 14, 2026)."),
 ("Light Heavyweight", "Carlos Ulberg", "Won the vacant belt by first-round knockout of Ji&#345;&iacute; Proch&aacute;zka at UFC 327, April 11, 2026."),
 ("Middleweight", "Sean Strickland", "<b>Two-time champion.</b> Split decision over Khamzat Chimaev at UFC 328, Prudential Center, Newark &mdash; two judges 48-47 Strickland, one 48-47 Chimaev."),
 ("Welterweight", "Islam Makhachev", "Two-division champion; vacated lightweight. One defence &mdash; decision over Ian Machado Garry, UFC 330, August 15, 2026."),
 ("Lightweight", "Justin Gaethje", "TKO4 of Ilia Topuria at Freedom 250, June 14, 2026."),
 ("Featherweight", "Alexander Volkanovski", "Defends against Movsar Evloev at UFC 333, October 24."),
 ("Bantamweight", "Petr Yan", "Defends against Merab Dvalishvili at UFC 333, October 24."),
 ("Flyweight", "Joshua Van", "One defence. Rematches Alexandre Pantoja at UFC 331, September 19."),
 ("Women's Bantamweight", "Kayla Harrison", "Zero defences; the scheduled UFC 324 defence against Amanda Nunes was cancelled after Harrison withdrew for neck surgery."),
 ("Women's Flyweight", "Valentina Shevchenko", "<b>Injured</b> &mdash; withdrew from the planned UFC 332 defence against Natalia Silva."),
 ("Women's Strawweight", "Mackenzie Dern", "One defence &mdash; decision over Gillian Robertson, UFC 330, August 15, 2026."),
 ("Women's Featherweight", "Vacant", "&mdash;"),
]
for d, c, n in champs:
    A(f'<tr><td><b>{d}</b></td><td>{c}</td><td>{n}</td></tr>')
A('</table></div>')
A('<p class="note"><b>Middleweight is the cell that keeps coming back wrong.</b> The aggregated "current UFC '
  'champions" list returned by search named <b>Khamzat Chimaev</b> at 185 again this run &mdash; the twenty-sixth '
  'consecutive time. Chimaev lost the belt to <b>Sean Strickland</b> at UFC 328, re-verified on a fresh fetch '
  'this run against ESPN, CBS Sports, Sky Sports and UFC.com. The same aggregated list got the other eleven '
  'cells right. Some outlets date UFC 328 to May 10, 2026; this desk publishes May 9, 2026 per its standing '
  'record of the event.</p>')

A(shared.sources([
 ("Bloody Elbow &mdash; UFC 332 update: new main event will be announced this week after title fight collapsed due to injury",
  "https://bloodyelbow.com/2026/09/02/ufc-332-update-new-main-event-will-be-announced-this-week-after-title-fight-collapsed-due-to-injury/"),
 ("MMA Mania &mdash; Valentina Shevchenko pulls out of UFC 332, leaving Salt Lake City without a championship fight",
  "https://www.mmamania.com/ufc-news/469092/valentina-shevchenko-pulls-out-of-ufc-332-leaving-salt-lake-city-without-a-championship-fight"),
 ("UFC.com &mdash; UFC 332", "https://www.ufc.com/event/ufc-332"),
 ("UFC.com &mdash; UFC Fight Night: Hooker vs Parnasse (September 5, 2026)",
  "https://www.ufc.com/event/ufc-fight-night-september-05-2026"),
 ("Rotowire &mdash; Hooker vs Parnasse, Sep 5 2026 odds",
  "https://www.rotowire.com/betting/mma/fight/salahdine-parnasse-vs-dan-hooker-odds-2026-09-05-5365"),
 ("UFC.com &mdash; UFC Fight Night Shanghai bonus coverage",
  "https://www.ufc.com/news/ufc-fight-night-shanghai-2026-bonus-coverage"),
 ("UFC.com &mdash; UFC Shanghai official scorecards: Nurmagomedov vs Song",
  "https://www.ufc.com/news/ufc-shanghai-official-scorecards-nurmagomedov-vs-song"),
 ("ESPN &mdash; Strickland stuns rival Chimaev for UFC middleweight title",
  "https://www.espn.com/mma/ufc/story/_/id/48728368/strickland-stuns-chimaev-ufc-middleweight-title"),
 ("ESPN &mdash; Current and all-time UFC champions",
  "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
 ("Tapology &mdash; UFC 331: Van vs. Pantoja 2",
  "https://www.tapology.com/fightcenter/events/145652-ufc-331"),
 ("UFCalendar &mdash; UFC schedule", "https://www.ufcalendar.com/ufc/schedule"),
]))
A('<p class="disc">Cards and bouts are subject to change. Odds move constantly and are shown as of the time '
  'they were fetched; this briefing is for information only and is not betting advice.</p>')
A('</footer>')

html = shared.page("The Octagon &mdash; Daily Briefings", ACCENT, ACCENT2,
                   "#100c0c", "#1a1313", "#322020", "\n".join(body), "", CDN_JS)
io.open("mma-briefing.html", "w", encoding="utf-8").write(html)
print("mma ok", len(html))
