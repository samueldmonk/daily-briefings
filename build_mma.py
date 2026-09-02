# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp')
from css import BASE, STAMP, nav, meta
OUT="/sessions/amazing-determined-planck/mnt/outputs/"
ROOT=":root{--bg:#100c0c;--panel:#1a1313;--panel2:#221818;--line:#322020;--fg:#f5eae8;--muted:#94736e;--muted2:#cbb3ae;--accent:#e84545;--accent2:#ff8a5c;--up:#3fbf72;--crit:#ff5f5f;--warn:#e0a13a;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}\n"

h=[]
h.append('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Octagon &mdash; Daily MMA Briefing</title><style>'+ROOT+BASE+'</style></head><body><div class="wrap">')
h.append('<div class="masthead"><h1>The Octagon</h1><p class="tag">Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting</p>'+meta()+'</div>')
h.append('<div class="tldr"><b>Tale of the Tape</b> <span>UFC Paris lands Saturday at the Accor Arena with <b>Salahdine Parnasse a &minus;550 favourite on his UFC debut</b> over the No. 10-ranked Dan Hooker at <b>+400</b> &mdash; the shortest main-event price on a fourteen-bout card &mdash; three days after Song Yadong&rsquo;s second-round upset of Umar Nurmagomedov in Shanghai banked a <b>$100,000</b> Performance of the Night bonus.</span></div>')
h.append('<div class="freshline" id="freshline">&nbsp;</div>')
h.append(nav("mma-briefing.html"))

h.append('<div class="cdn"><span class="lab">Next Card</span><span class="val" id="ufccdn">&nbsp;</span><span class="ev">UFC Fight Night: Hooker vs Parnasse &mdash; Sat, Sep 5, Accor Arena, Paris. Prelims 12:00 PM ET, main card 3:00 PM ET, Paramount+. Countdown runs to the main-card start.</span></div>')

h.append('''<h2>Top Story</h2><div class="panel" style="border-left:3px solid var(--accent)">
<h3 style="margin:0 0 9px;font-size:20px;line-height:1.3">A UFC debutant is a &minus;550 favourite in a main event &mdash; over a ranked veteran</h3>
<p>UFC.com&rsquo;s official card for <b>UFC Fight Night: Hooker vs Parnasse</b> prices the main event at <b>Dan Hooker +400 / Salahdine Parnasse &minus;550</b>. <b>Parnasse is making his UFC debut.</b> Hooker is the <b>No. 10-ranked</b> lightweight on the same page &mdash; UFC.com shows a rank badge beside his name and none beside Parnasse&rsquo;s.</p>
<p><b>&minus;550 is the shortest price anywhere on the fourteen-bout card</b>, by comparison with the other thirteen prices listed below &mdash; the next shortest are Kurtis Campbell at &minus;390 and Losene Keita at &minus;360. <b>That ranking is this desk&rsquo;s arithmetic across UFC.com&rsquo;s own table, not a claim any source makes.</b></p>
<p class="note"><b>How the odds were read, because the source is ambiguous row by row.</b> UFC.com renders each bout as a bare pair &mdash; &ldquo;+400 odds &minus;550&rdquo; &mdash; with no stated assignment of price to fighter. Reading the table <b>as a whole</b> resolves it: across the card the <b>first price belongs to the first-named fighter</b> in every row that can be cross-checked against an independently fetched quote, with favourite and underdog matching each time. <b>The ambiguity in one row is resolved by the rest of the table.</b></p>
<p><b>On Parnasse&rsquo;s provenance, which this page has had to correct before:</b> he is a former <b>two-time KSW featherweight champion and one-time KSW lightweight champion</b> who signed with the UFC in <b>late July 2026</b> after previously turning the promotion down, and was handed a main event on debut. <b>He did not come through Dana White&rsquo;s Contender Series</b> &mdash; an earlier claim to that effect was wrong and is not repeated. He is a debutant, not a UFC veteran, contender or ranked fighter.</p>
</div>''')

h.append('''<h2>Fight Week &mdash; Upcoming Cards</h2><div class="note">Dates, venues and start times are UFC.com&rsquo;s unless a card says otherwise. <b>Odds are UFC.com&rsquo;s own listed prices</b>, read first-price-to-first-named-fighter as described above.</div><div class="cards">
<div class="card"><div class="tags"><span class="tag t-a">This Saturday</span><span class="tag t-a">14 bouts</span></div>
<h3>UFC Fight Night: Hooker vs Parnasse</h3><p class="note" style="color:var(--accent2)">SAT, SEP 5 &middot; ACCOR ARENA, PARIS</p><p><b>Dan Hooker (#10) vs Salahdine Parnasse</b> &mdash; lightweight, five rounds. A ranked New Zealand veteran against a French debutant fighting at home. <b>Odds: Hooker +400 / Parnasse &minus;550 (UFC.com).</b> Prelims 12:00 PM ET, main card 3:00 PM ET, both on Paramount+.</p></div>
<div class="card"><div class="tags"><span class="tag t-a">Sep 12</span><span class="tag t-w">Title vs card mismatch</span></div>
<h3>Noche UFC</h3><p class="note" style="color:var(--accent2)">SAT, SEP 12 &middot; DESERT DIAMOND ARENA, GLENDALE, AZ</p><p>Billed as <b>&ldquo;Rodriguez vs Silva,&rdquo;</b> but <b>Yair Rodr&iacute;guez withdrew injured</b> and UFC.com&rsquo;s card has <b>Jean Silva vs Jose Delgado</b>. <b>The event title names a fighter who is not on it</b> &mdash; stated plainly because a reader who trusts the title will get the main event wrong. Thirteen fights; main card <b>5:00 PM ET</b>, prelim start disputed between 1 PM and 2 PM ET across listings and therefore not asserted.</p></div>
<div class="card"><div class="tags"><span class="tag t-a">Sep 19</span><span class="tag t-a">Numbered card</span></div>
<h3>UFC 331: Van vs Pantoja 2</h3><p class="note" style="color:var(--accent2)">SAT, SEP 19 &middot; CRYPTO.COM ARENA, LOS ANGELES</p><p>Flyweight champion <b>Joshua Van</b> rematches <b>Alexandre Pantoja</b>, the man he took the belt from at UFC 323. Thirteen fights; the card also carries <b>Renato Moicano vs Brian Ortega</b> and <b>Patricio Pitbull vs Doo Ho Choi</b>. Main card <b>9:00 PM ET</b>; the prelim tiering differs between listings (early prelims ~5 PM and prelims 7 PM in one, prelims 6 PM in another) and <b>only the 9 PM main card is agreed</b>. <b>No odds for this card were sourced this run.</b></p></div>
<div class="card"><div class="tags"><span class="tag t-a">Sep 26</span></div>
<h3>UFC Vegas 121: Rosas Jr vs Barcelos</h3><p class="note" style="color:var(--accent2)">SAT, SEP 26 &middot; UFC APEX, LAS VEGAS</p><p><b>Raul Rosas Jr. vs Raoni Barcelos</b> headlines. <b>No venue detail beyond the Apex, no start times and no odds were sourced this run</b>, so none are printed.</p></div>
<div class="card"><div class="tags"><span class="tag t-a">Developmental</span></div>
<h3>Dana White&rsquo;s Contender Series &mdash; Weeks 6 and 7</h3><p class="note" style="color:var(--accent2)">TUE, SEP 15 &amp; TUE, SEP 22 &middot; UFC APEX</p><p>Season 10 continues on consecutive Tuesdays. <b>No matchmaking for either week was sourced this run.</b></p></div>
</div>''')

h.append('''<h2>Last Event &mdash; Results</h2><div class="note"><b>UFC Fight Night: Nurmagomedov vs. Song</b> &mdash; Saturday, August 29, 2026, Shanghai Oriental Sports Center, Shanghai. Only bouts for which a winner, opponent and method were all sourced this run appear below.</div><table>
<tr><th>Result</th><th>Bout</th><th>Method</th></tr>
<tr><td class="up">Song Yadong</td><td>def. Umar Nurmagomedov</td><td>KO/TKO, R2, 1:48</td></tr>
<tr><td class="up">Denise Gomes</td><td>def. Yan Xiaonan</td><td>KO/TKO (elbow), R1, 4:49</td></tr>
<tr><td class="up">Kai Asakura</td><td>def. Aoriqileng</td><td>KO/TKO (punches), R2, 0:34</td></tr>
<tr><td class="up">Levi Rodrigues Jr.</td><td>def. Liu Ce</td><td>KO/TKO (punch), R1, 4:26</td></tr>
<tr><td class="up">Bilal Hasan</td><td>def. Nilson Rojas</td><td>KO/TKO (punch), R2, 2:28</td></tr>
<tr><td class="up">Francesco Nuzzi</td><td>def. Xiao Long</td><td>KO/TKO (punches), R1, 1:00</td></tr>
</table>
<div class="callout" style="border-left-color:var(--accent)"><h3>Performance bonuses &mdash; Shanghai</h3><p><b>Performance of the Night ($100,000 each): Song Yadong</b>, for the main-event upset, and <b>Bilal Hasan</b>, for a second-round knockout of fellow debutant Nilson Rojas. <b>Fight of the Night ($100,000 each): Liu Ce vs Levi Rodrigues Jr.</b> Separately, the card&rsquo;s remaining finishers &mdash; Denise Gomes, Kai Asakura, Andre Lima, Rei Tsuruya, Francesco Nuzzi, Hector Santiago and Julia Polastri &mdash; each earned an additional <b>$25,000</b> for their stoppages. <b>Every figure here is stated by the sources; none is inferred.</b></p></div>''')

h.append('''<h2>Prospect Watch</h2><div class="cards">
<div class="card"><div class="tags"><span class="tag t-new">New this run</span><span class="tag t-new">Contracts</span></div>
<h3>Five UFC contracts out of DWCS Week 4</h3><p>Dana White&rsquo;s Contender Series Season 10, Week 4 ran <b>Tuesday, September 1</b> at the UFC Apex, and <b>all five winners were offered UFC contracts</b>: <b>Adam Darby</b>, <b>Modestino Rodrigues</b>, <b>Silvestre Sanchez</b>, <b>Adam Livingston</b> and a fifth heavyweight winner whose surname is rendered two different ways across the reports fetched this run &mdash; <b>so his name is not printed here.</b> A misspelt fighter is a worse error than an incomplete list.</p></div>
<div class="card"><div class="tags"><span class="tag t-new">New this run</span><span class="tag t-new">Prospect</span></div>
<h3>Adam Darby</h3><p>Beat <b>Patrick Rivera</b> in the Week 4 main event by <b>doctor&rsquo;s stoppage in the third round</b>, earning a UFC contract.</p></div>
<div class="card"><div class="tags"><span class="tag t-new">New this run</span><span class="tag t-new">Prospect</span></div>
<h3>Silvestre Sanchez</h3><p>Found momentum in the second round of a lightweight barnburner with <b>Liam McCracken</b> and <b>knocked him out cold in the final round</b>. Contract awarded.</p></div>
<div class="card"><div class="tags"><span class="tag t-new">New this run</span><span class="tag t-new">Prospect</span></div>
<h3>Adam Livingston</h3><p>Edged a <b>split decision</b> over <b>Hunter Smith</b> at lightweight, earning a contract <b>in his second Contender Series appearance</b> after a failed attempt last year.</p></div>
<div class="card"><div class="tags"><span class="tag t-a">Debut Saturday</span><span class="tag t-new">Prospect</span></div>
<h3>Salahdine Parnasse</h3><p>Former <b>two-time KSW featherweight champion</b> and <b>one-time KSW lightweight champion</b>, <b>14-2 inside KSW</b> with four defences of the lightweight belt. Signed with the UFC in late July 2026 having previously turned it down; his U.S. debut in May 2026 was a <b>first-round stoppage of Kenneth Cross</b> for a fifth straight win. <b>Not a Contender Series signee.</b></p></div>
</div>''')

h.append('''<h2>Around the Sport</h2><ul class="bul">
<li><b>The Paris card runs fourteen bouts across two tiers</b> &mdash; six on the main card, eight on the prelims &mdash; with <b>no early-prelim section listed on UFC.com</b>.</li>
<li><b>Three fighters carry rank badges on the Paris card:</b> Dan Hooker at <b>#10</b>, Michael &ldquo;Venom&rdquo; Page at <b>#15</b> and Nora Cornolle at <b>#13</b>. <b>No other bout on the card shows a rank beside either name</b>, including Nathaniel Wood vs Pavel Andrusca.</li>
<li><b>The card is heavily French.</b> Ziam, Sola, Charriere, Sy, Aljarouj, Cornolle, Duclos and Benouaich all carry the French flag on UFC.com, as does Parnasse &mdash; nine of twenty-eight fighters.</li>
<li><b>Yan Xiaonan was stopped by an elbow in the first round</b> in Shanghai, one of nine finishes on a card where every result sourced this run ended inside the distance.</li>
<li><b>A previously reported Paris booking of Kelvin Gastelum vs. Belgaroui was refused again this run</b> &mdash; UFC.com&rsquo;s card does not contain it, and neither man appears on the fourteen-bout listing.</li>
</ul>''')

h.append('''<h2>Rankings &amp; Business</h2><div class="cards">
<div class="card"><div class="tags"><span class="tag t-a">Rankings</span></div>
<h3>Rankings movement</h3><p><b>No ranking change was sourced this run</b>, so none is reported. The only rank figures on this page are the badges UFC.com displays on the Paris card &mdash; Hooker #10, Page #15, Cornolle #13.</p></div>
<div class="card"><div class="tags"><span class="tag t-a">Business</span></div>
<h3>Business &amp; broadcast</h3><p>Both the Paris prelims and main card stream on <b>Paramount+</b>. <b>No viewership figure, gate, television rating or TKO Group financial number was sourced this run, and none is published.</b> The only dollar figures on this page are the Shanghai bonus amounts, which the sources state.</p></div>
</div>''')

h.append('''<h2>UFC Paris &mdash; full card and prices</h2><table>
<tr><th>Bout</th><th>Weight</th><th>Odds (UFC.com)</th></tr>
<tr><td><b>Dan Hooker (#10) vs Salahdine Parnasse</b></td><td>Lightweight</td><td>+400 / &minus;550</td></tr>
<tr><td>Far&egrave;s Ziam vs Axel Sola</td><td>Lightweight</td><td>&minus;145 / +125</td></tr>
<tr><td>Michael Venom Page (#15) vs Nursulton Ruziboev</td><td>Middleweight</td><td>&minus;175 / +145</td></tr>
<tr><td>Daniil Donchenko vs Punahele Soriano</td><td>Welterweight</td><td>&minus;245 / +200</td></tr>
<tr><td>Kurtis Campbell vs Trevor Peek</td><td>Featherweight</td><td>&minus;390 / +310</td></tr>
<tr><td>Losene Keita vs Muhammad Naimov</td><td>Featherweight</td><td>&minus;360 / +280</td></tr>
<tr><td colspan="3" style="background:var(--panel2);font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)">Prelims &mdash; 12:00 PM ET</td></tr>
<tr><td>Morgan Charriere vs Felipe Lima</td><td>Featherweight</td><td>+155 / &minus;185</td></tr>
<tr><td>Mario Pinto vs Ryan Spann</td><td>Heavyweight</td><td>&minus;275 / +225</td></tr>
<tr><td>Oumar Sy vs Modestas Bukauskas</td><td>Light Heavyweight</td><td>&minus;210 / +175</td></tr>
<tr><td>Nathaniel Wood vs Pavel Andrusca</td><td>Featherweight</td><td>+110 / &minus;130</td></tr>
<tr><td>Michael Aljarouj vs Fabia Sintes</td><td>Flyweight</td><td>&minus;130 / +110</td></tr>
<tr><td>Nora Cornolle (#13) vs Klaudia Sygula</td><td>Women&rsquo;s Bantamweight</td><td>&minus;125 / +105</td></tr>
<tr><td>Matthieu Duclos vs Luis Felipe Dias</td><td>Middleweight</td><td>&minus;115 / &minus;105</td></tr>
<tr><td>Delphine Benouaich vs Sofia Montenegro</td><td>Women&rsquo;s Strawweight</td><td>&minus;150 / +125</td></tr>
</table><div class="note"><b>The first six bouts are the main card (3:00 PM ET); the eight below the divider are the prelims (12:00 PM ET).</b> A secondhand listing fetched this run placed <b>Charriere&ndash;Lima on the main card and Campbell&ndash;Peek on the prelims</b>; <b>UFC.com &mdash; last modified Sept 1 at 3:54 PM ET &mdash; has them the other way round, and UFC.com is what is published.</b> Names are spelled as UFC.com spells them.</div>''')

h.append('''<h2>Champions Board</h2><div class="note"><b>Re-verified against the most recent completed event before publishing.</b> A search result this run again returned <b>middleweight as Khamzat Chimaev</b> &mdash; that is wrong, and it is the eighteenth consecutive edition in which a stale champions list has had to be corrected in that one cell. Sean Strickland took the belt by split decision at UFC 328 on May 9, 2026; two judges scored it 48-47 Strickland, one 48-47 Chimaev.</div><table>
<tr><th>Division</th><th>Champion</th><th>Note</th></tr>
<tr><td>Heavyweight</td><td>Tom Aspinall</td><td>Undisputed since June 21, 2025</td></tr>
<tr><td>Interim Heavyweight</td><td>Ciryl Gane</td><td>KO2 over Alex Pereira, Freedom 250, June 14, 2026</td></tr>
<tr><td>Light Heavyweight</td><td>Carlos Ulberg</td><td>Won the vacant belt, KO1 over Ji&#345;&iacute; Proch&aacute;zka, UFC 327, April 11, 2026</td></tr>
<tr><td>Middleweight</td><td>Sean Strickland</td><td><b>Split decision over Khamzat Chimaev, UFC 328, May 9, 2026</b> &mdash; two-time champion; first man to beat Chimaev</td></tr>
<tr><td>Welterweight</td><td>Islam Makhachev</td><td>UFC 322, Nov 15, 2025; two-division champion. One defence &mdash; decision over Ian Machado Garry, UFC 330, Aug 15, 2026</td></tr>
<tr><td>Lightweight</td><td>Justin Gaethje</td><td>TKO4 over Ilia Topuria, Freedom 250, June 14, 2026</td></tr>
<tr><td>Featherweight</td><td>Alexander Volkanovski</td><td>Reclaimed April 12, 2025; defended over Diego Lopes, UFC 325, Jan 31, 2026. <b>Not vacant</b></td></tr>
<tr><td>Bantamweight</td><td>Petr Yan</td><td>Decision over Merab Dvalishvili, UFC 323, Dec 6, 2025</td></tr>
<tr><td>Flyweight</td><td>Joshua Van</td><td>TKO1 over Alexandre Pantoja, UFC 323, Dec 6, 2025; one defence. <b>Rematches Pantoja at UFC 331</b></td></tr>
<tr><td>Women&rsquo;s Bantamweight</td><td>Kayla Harrison</td><td>Sub2 over Julianna Pe&ntilde;a, UFC 316, June 7, 2025; <b>0 defences</b></td></tr>
<tr><td>Women&rsquo;s Flyweight</td><td>Valentina Shevchenko</td><td>&mdash;</td></tr>
<tr><td>Women&rsquo;s Strawweight</td><td>Mackenzie Dern</td><td>UFC 321, Oct 25, 2025. One defence &mdash; decision over Gillian Robertson, UFC 330, Aug 15, 2026</td></tr>
</table>''')

h.append('''<h2>Sources</h2><div class="panel srcs">
<a href="https://www.ufc.com/event/ufc-fight-night-september-05-2026">UFC.com &mdash; UFC Fight Night: Hooker vs Parnasse, official card, odds and start times (last modified Sept 1, 2026, 3:54 PM ET)</a><br>
<a href="https://www.espn.com/mma/fightcenter/_/id/600060620/league/ufc">ESPN &mdash; UFC Fight Night: Nurmagomedov vs. Song fight results</a><br>
<a href="https://www.ufc.com/news/ufc-fight-night-shanghai-2026-bonus-coverage">UFC.com &mdash; UFC Shanghai bonus coverage</a><br>
<a href="https://www.sherdog.com/news/news/UFC-Shanghai-bonuses-Yadong-Song-3-others-earn-36100000-202571">Sherdog &mdash; UFC Shanghai bonuses: Yadong Song, 3 others earn $100,000</a><br>
<a href="https://www.espn.com/mma/ufc/story/_/id/48728368/strickland-stuns-chimaev-ufc-middleweight-title">ESPN &mdash; Strickland stuns rival Chimaev for UFC middleweight title</a><br>
<a href="https://www.skysports.com/mma/news/19828/13542189/sean-strickland-defeats-khamzat-chimaev-in-ufc-328-to-regain-middleweight-title-after-split-decision">Sky Sports &mdash; Strickland defeats Chimaev at UFC 328 to regain the middleweight title</a><br>
<a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">ESPN &mdash; Current and all-time UFC champions</a><br>
<a href="https://www.si.com/fannation/mma/news/dana-white-s-contender-series-2026-week-4-live-stream-results-highlights">Sports Illustrated &mdash; Dana White&rsquo;s Contender Series 2026 Week 4 results</a><br>
<a href="https://www.tapology.com/fightcenter/events/142723-contender-series-2026-week-4">Tapology &mdash; Contender Series 2026: Week 4</a><br>
<a href="https://www.ufc.com/news/10-spotlighting-septembers-most-exciting-matchups">UFC.com &mdash; The 10: Spotlighting September&rsquo;s most exciting matchups</a>
</div>
<div class="disc"><b>Cards and bouts are subject to change.</b> Odds are the prices UFC.com listed at the time of the fetch above and move constantly; they are not a recommendation and no wagering advice is offered. Where a name, time or figure was rendered inconsistently across sources, this page says so rather than choosing silently.</div>''')

CDN = """<script>(function(){var el=document.getElementById('ufccdn');if(!el)return;function t(){var n=new Date();var e=new Date('2026-09-05T15:00:00-04:00');var s=Math.floor((e-n)/1000);if(s<=0){el.textContent='Fight week \\u2014 live/completed';return;}var d=Math.floor(s/86400),hh=Math.floor(s%86400/3600),mm=Math.floor(s%3600/60);el.textContent=d+'d '+hh+'h '+mm+'m';}t();setInterval(t,30000);})();</script>"""
h.append('</div>'+CDN+STAMP+'</body></html>')
open(OUT+"mma-briefing.html","w").write("".join(h))
print("mma ok", sum(len(x) for x in h))
