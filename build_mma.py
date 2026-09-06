# -*- coding: utf-8 -*-
import shared, io

ACC, ACC2 = "#e84545", "#ff8a5c"
extra = """
.cdn{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);
  border-radius:11px;padding:12px 16px;margin-bottom:16px;display:flex;flex-wrap:wrap;align-items:baseline;gap:12px}
.cdn .lab{font-family:var(--mono);font-size:10.5px;letter-spacing:.17em;text-transform:uppercase;color:var(--accent)}
.cdn .val{font-family:var(--mono);font-size:19px;color:var(--accent2)}
.cdn .who{font-size:13.5px;color:var(--muted)}
.dateline{font-family:var(--mono);font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;color:#e8c766;margin-bottom:7px}
.top{border-left:4px solid var(--accent)}
"""
css = shared.css(ACC, ACC2, "#100c0c", "#1a1313", "#322020", extra)

TLDR = ("Salahdine Parnasse stopped Dan Hooker in the first round of his UFC debut in Paris, took "
        "Performance of the Night and called for Max Holloway — and UFC.com says the win puts him "
        "straight into the lightweight top 15.")

b = io.StringIO(); w = b.write
w(shared.masthead("The Octagon", "Your daily MMA briefing — UFC, prospects &amp; the business of fighting"))
w(f'<div class="tldr"><b>Tale of the Tape</b> <span>{TLDR}</span></div>')
w('<div class="freshline" id="freshline">&nbsp;</div>')
w(shared.nav("mma"))

w('<div class="cdn"><span class="lab">Next card</span><span class="val" id="ufccdn">—</span>'
  '<span class="who">Noche UFC: Silva vs Delgado &middot; Sat, Sept 12 &middot; Desert Diamond Arena, '
  'Glendale, Arizona. <em>Counts down to September 12; no start time is asserted, because none was '
  'sourced this run.</em></span></div>')

w('<h2 class="sec">Top Story</h2>')
w('<div class="panel top">')
w('<h3 style="margin:0 0 9px;font-size:22px">Salahdine Parnasse arrives: a first-round stoppage of Dan '
  'Hooker on debut, in front of a sold-out Paris crowd</h3>')
w('<p>In the UFC Fight Night main event at the Accor Arena, <strong>Salahdine Parnasse (entering 23-2)</strong> '
  'stopped <strong>Dan Hooker (entering 24-14)</strong> by <strong>TKO at 2:35 of round one</strong>. Known '
  'for his grappling, Parnasse instead chose to kickbox with the No. 10-ranked veteran: about halfway '
  'through the opening round he landed a body kick that visibly hurt Hooker, then followed with a flurry '
  'against the fence that put him down.</p>')
w('<p>Parnasse is a <strong>two-division champion outside the UFC</strong> — a two-time KSW featherweight '
  'champion and one-time KSW lightweight champion, 14-2 inside KSW with four defences of the lightweight '
  'belt — who <strong>signed with the UFC in late July 2026</strong> after previously turning the promotion '
  'down, and was handed a five-round main event on debut. <em>He did not come through Dana White’s Contender '
  'Series</em>; this desk has published that error before and will not repeat it.</p>')
w('<p>UFC.com’s own write-up says the win means Parnasse “instantly enters the highly touted lightweight '
  'Top 15.” He took <strong>Performance of the Night</strong>, and afterwards called for a fight with '
  '<strong>Max Holloway</strong>, who reporting places at No. 4 in the lightweight rankings.</p>'
  '<p><strong>The books were on the debutant, and they were right:</strong> UFC.com’s own event page '
  'listed <strong>Parnasse &minus;550, Hooker +400</strong> — Parnasse was the heavy favourite, and he '
  'won inside a round.</p>')
w('</div>')

w('<h2 class="sec">Fight Week — Upcoming Cards</h2>')
w('<div class="cards">')
w('<div class="card"><div class="tags"><span class="t gold">Next up</span></div>'
  '<div class="dateline">Sat, Sept 12 &middot; Desert Diamond Arena, Glendale, AZ</div>'
  '<h3>Noche UFC: Silva vs Delgado</h3>'
  '<p>The fourth annual Noche UFC, on Mexican Independence Day weekend. Featherweight <strong>Jean '
  'Silva</strong> meets Arizona’s <strong>Jose Miguel Delgado</strong> — a replacement main event after '
  '<strong>Yair Rodríguez withdrew injured</strong>. Also announced: former flyweight champion '
  '<strong>Brandon Moreno vs Joseph Morales</strong> (the Ultimate Fighter season 33 winner) and '
  '<strong>Manon Fiorot vs Alexa Grasso</strong>. <span class="mut">Odds: not sourced this run, so none are '
  'printed.</span></p></div>')
w('<div class="card"><div class="tags"><span class="t hot">Title fight</span></div>'
  '<div class="dateline">Sat, Sept 19 &middot; Crypto.com Arena, Los Angeles</div>'
  '<h3>UFC 331: Van vs Pantoja 2</h3>'
  '<p>A <strong>flyweight championship rematch</strong>: champion <strong>Joshua Van</strong> defends '
  'against former champion <strong>Alexandre Pantoja</strong>. Van took the belt from Pantoja at UFC 323 in '
  'December 2025 by TKO 26 seconds into round one, the stoppage following an arm injury Pantoja sustained in '
  'the fight. Co-main: <strong>Arman Tsarukyan vs Mauricio Ruffy</strong> at lightweight. '
  '<span class="mut">Odds: not sourced this run.</span></p></div>')
w('<div class="card"><div class="tags"><span class="t">Calendar</span></div>'
  '<div class="dateline">Sat, Sept 26</div>'
  '<h3>An event is on the calendar — headliner not asserted</h3>'
  '<p>A schedule return this run lists a September 26 card, but names it in a way that conflicts with the '
  'September 12 Noche UFC billing above. Rather than resolve a naming conflict this desk cannot verify, the '
  'date is carried and <strong>no headliner is claimed</strong>.</p></div>')
w('<div class="card"><div class="tags"><span class="t">Calendar</span></div>'
  '<div class="dateline">Sat, Oct 17</div>'
  '<h3>Buckley vs Malott</h3>'
  '<p><strong>Joaquin Buckley</strong> and <strong>Mike Malott</strong> are set for a Fight Night main event '
  'on October 17. Venue not sourced this run. Further out, an event is scheduled for <strong>Saturday, '
  'October 24 at the Etihad Arena in Abu Dhabi</strong>.</p></div>')
w('</div>')
w('<div class="note"><strong>Refused this run:</strong> CBS Sports’ “2026 UFC event schedule” page still '
  'lists UFC 324 (Jan 24), UFC 325 (Jan 31) and UFC 326 (March 7) under “Upcoming UFC Schedule.” Those are '
  'months in the past. The page was discarded — a page titled “2026 schedule” is not necessarily a '
  '<em>current</em> schedule.</div>')

w('<h2 class="sec">Last Event — Results</h2>')
w('<div class="panel">')
w('<div class="dateline">UFC Fight Night: Hooker vs Parnasse &middot; Sat, Sept 5, 2026 &middot; Accor Arena, Paris</div>')
w('<table>')
w('<tr><th>Result</th><th>Bout</th><th>Method</th></tr>')
rows = [
 ("Salahdine Parnasse", "def. Dan Hooker — Lightweight (main event)", "TKO, R1 2:35"),
 ("Axel Sola", "def. Far&egrave;s Ziam — Lightweight (co-main)", "KO (left hand), R1 — under two minutes"),
 ("Michael Venom Page", "def. Nursulton Ruziboev — Middleweight", "Unanimous decision (29-28, 29-28, 29-28)"),
 ("Daniil Donchenko", "def. Punahele Soriano — Welterweight", "Unanimous decision (30-27, 30-27, 29-28)"),
 ("Kurtis Campbell", "def. Trevor Peek — Featherweight", "Submission (rear-naked choke), R3 3:07"),
 ("Losene Keita", "def. Muhammad Naimov — Featherweight", "KO (punch), R1 2:54"),
 ("Felipe Lima", "def. Morgan Charri&egrave;re — Featherweight", "Unanimous decision (30-27, 30-27, 29-28)"),
 ("Mario Pinto", "def. Ryan Spann — Heavyweight", "TKO (ground-and-pound), R2 0:55"),
 ("Modestas Bukauskas", "def. Oumar Sy — Light Heavyweight", "TKO"),
 ("Pavel Andrusca", "def. Nathaniel Wood — Featherweight", "Method not returned"),
 ("Fabia Sintes", "def. Michael Aljarouj — Flyweight", "Method not returned"),
 ("Nora Cornolle", "def. Klaudia Sygu&#322;a — Women’s Bantamweight", "Unanimous decision, 30-27 across"),
 ("Matthieu Duclos", "def. Luis Felipe Dias — Middleweight", "TKO (punches), R1 4:35"),
 ("Delphine Benouaich", "def. Sofia Montenegro — Women’s Strawweight", "Submission (rear-naked choke), R2 4:22"),
]
for winner, bout, method in rows:
    w(f'<tr><td class="up"><strong>{winner}</strong></td><td>{bout}</td><td>{method}</td></tr>')
w('</table>')
w('<div class="note">Fourteen bouts, all with a confirmed winner. Two methods are shown as “not '
  'returned” because no source this run stated them — the outcome is published, the method is not '
  'invented. Post-fight records, as given by the reporting source: <strong>Michael Venom Page 26-3 '
  '(5-1 UFC)</strong>; <strong>Nursulton Ruziboev 38-9-2 (5-2 UFC)</strong>. Elsewhere on this page, '
  'records are the ones the promotion published <em>going into</em> the fight. Felipe Lima’s win was '
  'his third inside the Octagon.</div>')
w('</div>')

w('<div class="panel">')
w('<h3 style="margin:0 0 9px;font-size:17px">Bonuses and business</h3>')
w('<ul class="bul">')
w('<li><strong>Four Performance of the Night awards, and no Fight of the Night</strong> — '
  '<strong>Salahdine Parnasse, Axel Sola, Losene Keita</strong> and <strong>Mario Pinto</strong>, per '
  'UFC.com’s own bonus coverage. The UFC page does not state the dollar amount; reporting puts each '
  'Performance of the Night at <strong>$100,000</strong>, and that figure is attributed rather than '
  'asserted.</li>')
w('<li><span class="t new" style="margin-right:7px">New</span><strong>Gross total revenue: '
  '$4,365,335. Attendance: 15,687 — a sellout. Record: the highest-grossing event in Accor Arena '
  'history.</strong> All three figures come straight off UFC.com’s bonus-coverage page.</li>')
w('<li>This was the promotion’s <strong>fifth Accor Arena event since 2022</strong>. The card streamed on '
  '<strong>Paramount+</strong>, prelims at 12 PM ET and main card at 3 PM ET — an unusually early slot '
  'driven by the Paris time zone.</li>')
w('</ul></div>')

w('<h2 class="sec">Prospect Watch</h2>')
w('<div class="cards">')
w('<div class="card"><div class="tags"><span class="t pro">Prospect</span><span class="t new">New</span></div>'
  '<h3>Salahdine Parnasse — debut, main event, bonus</h3>'
  '<p>Entered 23-2 with two KSW belts behind him; his U.S. debut in May 2026, on the Rousey vs Carano main '
  'card, was a first-round stoppage of Kenneth Cross for a fifth straight win. He is still a UFC '
  '<strong>debutant</strong> — not a veteran, contender or previously ranked fighter — but UFC.com now '
  'places him in the lightweight top 15.</p></div>')
w('<div class="card"><div class="tags"><span class="t pro">Prospect</span><span class="t new">New</span></div>'
  '<h3>Axel Sola — back-to-back finishes</h3>'
  '<p>Entered 12-1-1 and fighting for the third time in 2026. He knocked out fellow Frenchman Farès Ziam '
  'with a single left hand after about 90 seconds of feeling out. It is his second win in Paris in as many '
  'starts and his second straight first-round finish, after opening the year with a Fight of the Night '
  'against Mason Jones.</p></div>')
w('<div class="card"><div class="tags"><span class="t pro">Prospect</span></div>'
  '<h3>Mario Pinto — still undefeated</h3>'
  '<p>Entered 12-0 and stayed there, stopping Ryan Spann 55 seconds into round two after a back-and-forth '
  'first in which both men landed near-fight-ending shots. UFC.com’s own verdict: not the cleanest '
  'performance on the bonus list, but a bonus-worthy one.</p></div>')
w('<div class="card"><div class="tags"><span class="t pro">Prospect</span></div>'
  '<h3>Pavel Andrusca — the short-notice upset</h3>'
  '<p>An 8-0 newcomer from Chișinău, Moldova taken on short notice, Andrusca <strong>beat</strong> Nathaniel '
  'Wood, who had been hunting a fifth straight victory. No method was returned by any source this run, so '
  'none is stated. This desk does not draw a ranking conclusion from it.</p></div>')
w('</div>')

w('<h2 class="sec">Around the Sport</h2>')
w('<div class="panel"><ul class="bul">')
w('<li><strong>Dana White’s Contender Series, Season 10 Week 4:</strong> five contracts awarded '
  '(September 2). A name discrepancy from that card is printed, not resolved — the heavyweight winner '
  'appears as “Gabriel Lourenco” in one set of returns and “Gabriel Lorenço” in this desk’s log. Neither '
  'spelling is asserted over the other.</li>')
w('<li><strong>Parnasse’s callout:</strong> Max Holloway, whom reporting places at No. 4 in the lightweight '
  'rankings. No bout has been announced or booked — this is a post-fight callout, nothing more.</li>')
w('<li><strong>Noche UFC replacement:</strong> Yair Rodríguez withdrew injured from the September 12 main '
  'event and Jose Miguel Delgado stepped in. A previously published Grasso vs Fiorot headliner for that card '
  'is gone; Fiorot vs Grasso is on the card, not on top of it.</li>')
w('<li><strong>No title changed hands.</strong> UFC Paris was a non-title card, as was UFC Shanghai on '
  'August 29. The most recent championship bouts were at UFC 330 on August 15.</li>')
w('</ul></div>')

w('<h2 class="sec">Rankings &amp; Business</h2>')
w('<div class="panel">')
w('<p style="margin-top:0"><strong>Rankings movement.</strong> The only ranking claim this desk will make is '
  'the one UFC.com made itself: the win over Hooker means Parnasse “instantly enters the highly touted '
  'lightweight Top 15.” No other fighter’s ranking movement was stated by a source this run, so none is '
  'inferred — not for Sola, not for Bukauskas, and not for Nathaniel Wood’s division after his loss.</p>')
w('<p><strong>Business &amp; broadcast.</strong> UFC Paris grossed <strong>$4,365,335</strong> in front of a '
  'sold-out <strong>15,687</strong>, the highest-grossing event in Accor Arena history, per UFC.com. The '
  'card aired on Paramount+ in the United States. No viewership figure, and no TKO Group financial figure, '
  'was sourced this run, so neither is printed.</p>')
w('</div>')

w('<h2 class="sec">Champions Board</h2>')
w('<div class="panel"><table>')
w('<tr><th>Division</th><th>Champion</th><th>Note</th></tr>')
champs = [
 ("Heavyweight", "Tom Aspinall", "Undisputed; inherited the title June 21, 2025. 0 title defences. <em>Re-verified this run.</em>"),
 ("Heavyweight (interim)", "Ciryl Gane", "KO2 over Alex Pereira, Freedom 250, June 14 2026. <em>Carried from this desk’s standing file; not in this run’s returns.</em>"),
 ("Light Heavyweight", "Carlos Ulberg", "Won the vacant belt KO1 over Ji&#345;í Procházka at UFC 327, April 11 2026. Pereira is <strong>not</strong> the champion. <em>Re-verified this run.</em>"),
 ("Middleweight", "Sean Strickland", "Split-decision upset of Khamzat Chimaev at UFC 328, May 9 2026; two-time champion. Chimaev is <strong>not</strong> the champion. <em>Re-verified this run.</em>"),
 ("Welterweight", "Islam Makhachev", "UD over Jack Della Maddalena, UFC 322, Nov 15 2025. One defence — UD over Ian Machado Garry, UFC 330, Aug 15 2026, his 17th straight UFC win. <em>Re-verified this run.</em>"),
 ("Lightweight", "Justin Gaethje", "TKO4 over Ilia Topuria, Freedom 250, June 14 2026. <em>Re-verified this run.</em>"),
 ("Featherweight", "Alexander Volkanovski", "<strong>Not vacant.</strong> UD over Diego Lopes, UFC 314, April 12 2025; defended UD over Lopes at UFC 325, Jan 31 2026. <em>Re-verified this run.</em>"),
 ("Bantamweight", "Petr Yan", "UD over Merab Dvalishvili, UFC 323, Dec 6 2025. <em>Re-verified this run.</em>"),
 ("Flyweight", "Joshua Van", "TKO1 over Alexandre Pantoja, UFC 323, Dec 6 2025; defended TKO5 over Tatsuro Taira, UFC 328, May 9 2026. Faces Pantoja again Sept 19. <em>Re-verified this run.</em>"),
 ("Women’s Flyweight", "Valentina Shevchenko", "<em>Carried from this desk’s standing file.</em>"),
 ("Women’s Bantamweight", "Kayla Harrison", "Sub2 over Julianna Peña, UFC 316, June 7 2025. <strong>0 defences</strong> — the UFC 324 defence vs Amanda Nunes was cancelled after Harrison withdrew for neck surgery. <em>Carried from this desk’s standing file.</em>"),
 ("Women’s Strawweight", "Mackenzie Dern", "UD over Virna Jandiroba, UFC 321, Oct 25 2025; one defence — UD over Gillian Robertson, UFC 330, Aug 15 2026. <em>Carried; again absent from this run’s champions return.</em>"),
]
for d, c, n in champs:
    w(f'<tr><td class="mut">{d}</td><td><strong>{c}</strong></td><td>{n}</td></tr>')
w('</table>')
w('<div class="note">Eight of the twelve rows were re-verified this run against an ESPN-sourced '
  'current-champions return. The remaining four are carried from this desk’s standing corrections file and '
  'are labelled as such rather than presented as freshly confirmed. <strong>The middleweight and light '
  'heavyweight regressions did not fire for a fourth consecutive run.</strong> Neither UFC Shanghai '
  '(Aug 29) nor UFC Paris (today) was a title card, so no belt can have changed since UFC 330 on '
  'August 15.</div>')
w('</div>')

w('<h2 class="sec">Sources</h2>')
w('<div class="panel srcs">')
w('Fetched or returned this run: '
  '<a href="https://www.ufc.com/news/bonus-coverage-ufc-fight-night-paris-2026">UFC.com — Bonus Coverage, UFC Paris</a> (primary: bonuses, gate, attendance, Accor Arena record) · '
  '<a href="https://www.ufc.com/news/ufc-paris-results-hooker-vs-parnasse">UFC.com — Main Card Results</a> · '
  '<a href="https://www.ufc.com/news/ufc-paris-prelim-results-hooker-vs-parnasse">UFC.com — Prelim Results</a> · '
  '<a href="https://www.ufc.com/event/ufc-fight-night-september-05-2026">UFC.com — UFC Fight Night: Hooker vs Parnasse event page</a> · '
  '<a href="https://www.espn.com/mma/story/_/id/49840367/salahdine-parnasse-knocks-dan-hooker-ufc-debut">ESPN — Parnasse knocks out Hooker in UFC debut</a> · '
  '<a href="https://sports.yahoo.com/articles/ufc-paris-results-salahdine-parnasse-220612694.html">Yahoo Sports — Parnasse sparks Hooker, ready for Max Holloway</a> · '
  '<a href="https://ca.sports.yahoo.com/news/ufc-paris-results-michael-page-212307652.html">Yahoo Sports — Michael Page wins decision</a> · '
  '<a href="https://cagesidepress.com/2026/09/05/no-fight-of-the-night-foursome-collects-performance-bonuses-at-ufc-paris/">Cageside Press — No Fight of the Night, foursome collects bonuses</a> · '
  '<a href="https://www.mmamania.com/ufc-bonuses-and-awards/469586/official-ufc-paris-post-fight-bonus-winners-results-paramount-parnasse-hooker-sola-keita">MMA Mania — bonus winners</a> · '
  '<a href="https://www.fightbookmma.com/ufc-paris-hooker-vs-parnasse-results-fight-card-live-updates/">FightBook MMA — live results</a> · '
  '<a href="https://en.wikipedia.org/wiki/UFC_Fight_Night:_Hooker_vs._Parnasse">Wikipedia — UFC Fight Night: Hooker vs. Parnasse</a> · '
  '<a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">ESPN — Current and all-time UFC champions</a> · '
  '<a href="https://www.ufc.com/news/noche-ufc-take-place-september-12-ufc-returns-glendale-arizona">UFC.com — Noche UFC returns to Glendale, Sept 12</a> · '
  '<a href="https://www.ufc.com/event/ufc-fight-night-september-12-2026">UFC.com — Noche UFC: Silva vs Delgado</a> · '
  '<a href="https://en.wikipedia.org/wiki/UFC_331">Wikipedia — UFC 331</a> · '
  '<a href="https://www.aljazeera.com/sports/2026/8/6/ufc-331-van-pantoja-rematch-tsarukyan-returns-and-full-fight-card">Al Jazeera — UFC 331 preview</a> · '
  '<a href="https://combatpress.com/2026/09/contender-series-season-10-week-4-results-five-awarded-contracts/">Combat Press — DWCS S10 W4, five contracts</a>.')
w('</div>')

w('<div class="disc"><strong>Cards and bouts are subject to change.</strong> Every result, method, round and '
  'time above traces to a source fetched this run; where a method was not stated by any source, the cell '
  'says so rather than guessing. Records are the ones the promotion published going into the fight, '
  'except where a post-fight record is explicitly labelled as such. Betting figures are printed only where a source stated them.</div>')

w("""<script>(function(){try{
var target=new Date('2026-09-12T00:00:00-04:00');
function tick(){var el=document.getElementById('ufccdn');if(!el)return;
var d=target-new Date();
if(d<=0){el.textContent='Fight week — live/completed';return;}
var days=Math.floor(d/86400000),h=Math.floor(d%86400000/3600000),m=Math.floor(d%3600000/60000);
el.textContent=days+'d '+h+'h '+m+'m';}
tick();setInterval(tick,30000);}catch(e){}})();</script>""")

html = shared.page("The Octagon — Daily MMA Briefing", css, b.getvalue())
open("/tmp/build_1788656196/out/mma-briefing.html","w",encoding="utf-8").write(html)
print("mma bytes", len(html))
