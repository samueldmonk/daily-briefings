# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, "/tmp/db_1788465063")
from shared import page, nav, META, sources
OUT = "/sessions/nifty-sweet-cannon/mnt/outputs"
M = dict(accent="#e84545", accent2="#ff8a5c", bg="#100c0c", panel="#1a1313", line="#322020")
FRESH = '<p class="freshline" id="freshline">&nbsp;</p>'
S_MMA = ("UFC Paris is two days out with Dan Hooker headlining against UFC debutant Salahdine Parnasse, "
         "while UFC 332 is a month away and still without a main event after Valentina Shevchenko withdrew injured.")

b = []
b.append(f'<header class="mast"><h1>The Octagon</h1><p class="tag">Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting</p>{META}</header>')
b.append(f'<div class="tldr"><b>Tale of the Tape</b> <span>{S_MMA}</span></div>')
b.append(FRESH)
b.append(nav("mma", M["accent"]))

b.append('<div class="cdn"><span class="lbl">Next Card</span><span class="clk" id="ufccdn">&nbsp;</span>'
 '<span class="ev">UFC Fight Night: Hooker vs. Parnasse &mdash; Saturday, September 5, Accor Arena, Paris. '
 'Prelims 12 PM ET, main card 3 PM ET on Paramount+.</span></div>')

b.append('<h2 class="sec">Top Story</h2>')
b.append("""<div class="lead">
<h3>UFC 332 is a month out and still has no main event</h3>
<p><strong>Valentina Shevchenko</strong> has withdrawn from the October 3 card at the Delta Center in Salt Lake City
with an undisclosed injury, taking the women&rsquo;s flyweight title fight that was to headline it off the card.</p>
<p>The reported replacement is <strong>Natalia Silva vs. Wang Cong for an interim women&rsquo;s flyweight
championship</strong>. Nothing has been announced; UFC CEO Dana White has said the new main event will be named this
week. Wang Cong is the <strong>No. 6-ranked contender</strong> in the division, and beat Shevchenko in a
<strong>2015 kickboxing bout</strong> &mdash; the two have never met in MMA.</p>
<p>Into that gap stepped <strong>Cris Cyborg</strong>, who publicly offered to headline the card against
<strong>Amanda Nunes</strong>, writing to Nunes on social media: <em>&ldquo;tired of waiting for @KaylaH? Feel like
saving an @ufc event?&rdquo;</em> Nunes knocked Cyborg out at UFC 232 eight years ago to become a two-division
champion. Nunes has not responded.</p>
</div>""")

b.append('<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2><div class="cards">')
b.append("""<div class="card"><div class="tags"><span class="t new">This week</span></div>
<h3>UFC Fight Night: Hooker vs. Parnasse</h3>
<p class="mono" style="color:var(--accent2);margin-bottom:7px">Sat, Sept 5 &middot; Accor Arena, Paris</p>
<p><strong>Dan Hooker vs. Salahdine Parnasse</strong> at lightweight tops a 14-fight card, the UFC&rsquo;s fifth
straight year in the city. Main card support: Fares Ziam vs. Axel Sola; Michael &ldquo;Venom&rdquo; Page vs.
Nursulton Ruziboev; Daniil Donchenko vs. Punahele Soriano; Morgan Charriere vs. Felipe Lima; Losene Keita vs.
Muhammad Naimov. Prelims: Mario Pinto vs. Ryan Spann; Kurtis Campbell vs. Trevor Peek; Oumar Sy vs. Modestas
Bukauskas; Nathaniel Wood vs. TBA.<br><br>
<strong>Odds &mdash; four listings, none adopted:</strong> Parnasse &minus;667 / Hooker +417; Parnasse &minus;600 /
Hooker +440 (DraftKings); opener Parnasse &minus;357 / Hooker +275; implied 81.8% Parnasse / 18.2% Hooker with the
vig removed.</p></div>""")
b.append("""<div class="card"><div class="tags"><span class="t">Prospects</span></div>
<h3>Dana White&rsquo;s Contender Series, season 10 &mdash; week 5</h3>
<p class="mono" style="color:var(--accent2);margin-bottom:7px">Tue, Sept 8 &middot; Meta APEX, Las Vegas</p>
<p>Five fights, headed by an undefeated light heavyweight matchup: <strong>Quentin Pasley (3-0) vs. Arlind Berisha
(5-0)</strong> at 205 lb. Also announced: Isaac Moreno (8-0) vs. Reginaldo Geraldo Jr. (11-1); Martin Kozak (6-0) vs.
Christian Echols (8-4); Apollo Gomes (12-2) vs. Won Il Kwon (14-6); Colton Loud (7-1) vs. Christian Natividad (9-0).
<strong>Frank da Silva Castro lost a second Contender Series shot to a visa issue.</strong> Remaining weeks: Sept 15,
22 and 29.</p></div>""")
b.append("""<div class="card"><div class="tags"><span class="t">Fight Night</span></div>
<h3>Noche UFC</h3>
<p class="mono" style="color:var(--accent2);margin-bottom:7px">Sat, Sept 12 &middot; Glendale, Arizona</p>
<p><strong>Curtis Blaydes vs. Waldo Cortes-Acosta</strong> at heavyweight &mdash; Blaydes&rsquo; first bout under the
new eight-fight deal he signed with the promotion.</p></div>""")
b.append("""<div class="card"><div class="tags"><span class="t">Numbered card</span></div>
<h3>UFC 331</h3>
<p class="mono" style="color:var(--accent2);margin-bottom:7px">Sat, Sept 19 &middot; Crypto.com Arena, Los Angeles</p>
<p>Thirteen fights, main card 9 PM ET / 6 PM PT. Co-main: <strong>Tsarukyan vs. Ruffy</strong>. The card also carries
<strong>Van vs. Pantoja 2</strong>, nine months after a first meeting that lasted just 26 seconds.</p></div>""")
b.append("""<div class="card"><div class="tags"><span class="t warn">Main event TBA</span></div>
<h3>UFC 332</h3>
<p class="mono" style="color:var(--accent2);margin-bottom:7px">Sat, Oct 3 &middot; Delta Center, Salt Lake City</p>
<p>Headliner unannounced after Shevchenko&rsquo;s withdrawal. Silva vs. Wang Cong for an interim women&rsquo;s
flyweight belt is the reported target; White says the announcement comes this week.</p></div>""")
b.append('</div>')

b.append('<h2 class="sec">Last Event &mdash; Results</h2>')
b.append('<div class="panel"><p style="margin:0 0 12px;font-size:14.5px;color:#cfc9c2">'
 '<strong>UFC Fight Night: Nurmagomedov vs. Song</strong> &mdash; Saturday, August 29, Oriental Sports Center, '
 'Shanghai. Main card results, from the promotion&rsquo;s official recap.</p><table>'
 '<tr><th>Result</th><th>Bout</th><th>Method</th></tr>'
 '<tr><td class="up">Song Yadong</td><td>def. Umar Nurmagomedov</td><td>KO (right uppercut), R2 1:48</td></tr>'
 '<tr><td class="up">Denise Gomes</td><td>def. Yan Xiaonan</td><td>TKO (strikes), R1 4:49</td></tr>'
 '<tr><td class="up">Kai Asakura</td><td>def. Aoriqileng</td><td>KO (head kick and strikes), R2 0:34</td></tr>'
 '<tr><td class="up">Sumudaerji</td><td>def. Alex Perez</td><td>Unanimous decision (29-28, 29-28, 29-28)</td></tr>'
 '<tr><td class="up">Liu Ce</td><td>def. Levi Rodrigues Jr.</td><td>KO (right hand), R1 4:26</td></tr>'
 '<tr><td class="up">Bilal Hasan</td><td>def. Nilson Rojas</td><td>KO (right hand), R2 2:28</td></tr>'
 '</table>'
 '<div class="note"><strong>Bonuses.</strong> $400,000 across the headline awards, announced by UFC senior vice '
 'president and head of Asia Kevin Chang. Performance of the Night, $100,000 each: <strong>Song Yadong</strong> and '
 '<strong>Bilal Hasan</strong>. Fight of the Night, $100,000 each: <strong>Liu Ce</strong> and <strong>Levi Rodrigues '
 'Jr.</strong> On the $25,000 finishing cheques the reporting splits: one account counts <strong>five</strong>, '
 'another enumerates <strong>seven</strong> names &mdash; Denise Gomes, Kai Asakura, Andre Lima, Rei Tsuruya, '
 'Francesco Nuzzi, Hector Santiago and Julia Polastri. Both are printed; neither is adopted.</div></div>')

b.append('<h2 class="sec">Prospect Watch</h2><div class="cards">')
b.append("""<div class="card"><div class="tags"><span class="t ok">Prospect</span><span class="t new">New</span></div>
<h3>Bilal Hasan, 25 &mdash; unbeaten on debut</h3><p>Won his UFC deal on Dana White&rsquo;s Contender Series and
opened the Shanghai main card by knocking out Nilson Rojas with a right hand in the second, having been put on the
deck himself moments earlier. Took home a <strong>$100,000</strong> Performance of the Night bonus and called out
Andre Lima.</p></div>""")
b.append("""<div class="card"><div class="tags"><span class="t ok">Prospect</span><span class="t new">New</span></div>
<h3>Liu Ce &mdash; a debut KO at light heavyweight</h3><p>The Chinese kickboxer went toe-to-toe with Levi Rodrigues
Jr. from the opening bell and finished him with a right hand late in the first round of his promotional debut,
splitting a Fight of the Night bonus with the man he beat.</p></div>""")
b.append("""<div class="card"><div class="tags"><span class="t ok">Prospect</span><span class="t new">New</span></div>
<h3>Five contracts from Contender Series week 4</h3><p>Dana White announced UFC contract offers for all five week-4
winners: <strong>Adam Darby, Modestino Rodrigues, Silvestre Sanchez, Gabriel Loren&ccedil;o and Adam
Livingston</strong>.</p></div>""")
b.append('</div>')

b.append('<h2 class="sec">Around the Sport</h2><div class="panel"><ul class="bul">'
 '<li><strong>Song Yadong</strong>, 28, may have fought his way into the No. 1 contender position at bantamweight. He '
 'took the fight on with a bad cut under his right eyebrow from an accidental clash of heads, and had choked out '
 'Deiveson Figueiredo in Macau in his previous outing.</li>'
 '<li><strong>Denise Gomes</strong> has now won five straight. Yan Xiaonan had lost only to champions and contenders '
 'before Shanghai.</li>'
 '<li><strong>Sumudaerji</strong> edged Alex Perez in a rematch decided in the clinch in the final round; he is 6-2 '
 'with one no contest over his last nine flyweight appearances and should climb into the rankings.</li>'
 '<li><strong>Kai Asakura</strong> is 2-0 with two highlight-reel finishes since moving to 135 pounds.</li>'
 '<li><strong>Jason Jackson</strong>, the former Bellator welterweight champion, says he is a free agent waiting for '
 'the UFC&rsquo;s call. <strong>Jailton Almeida</strong> was among this year&rsquo;s heavyweight releases.</li>'
 '<li><strong>On Salahdine Parnasse:</strong> he signed with the UFC in <strong>late July 2026</strong>, having '
 'previously turned the promotion down, and headlines on debut. He is a former <strong>two-time KSW featherweight '
 'and one-time KSW lightweight champion</strong> &mdash; not a Contender Series signee &mdash; and he is a UFC '
 'debutant, not a ranked fighter or contender.</li>'
 '</ul></div>')

b.append('<h2 class="sec">Rankings &amp; Business</h2><div class="panel"><ul class="bul">'
 '<li><strong>Rankings movement:</strong> Wang Cong is published as the <strong>No. 6-ranked</strong> women&rsquo;s '
 'flyweight contender. Song Yadong and Sumudaerji are both described as in line to climb; no updated ranking number '
 'is stated for either, so none is printed.</li>'
 '<li><strong>Business &amp; broadcast:</strong> no viewership figure, gate or rights number was confirmed for this '
 'edition, so none is published. UFC Paris and Contender Series week 5 both stream on Paramount+.</li>'
 '</ul></div>')

b.append('<h2 class="sec">Champions Board</h2><div class="panel"><table>'
 '<tr><th>Division</th><th>Champion</th><th>Won / notes</th></tr>'
 '<tr><td>Heavyweight</td><td>Tom Aspinall</td><td>Undisputed since June 21, 2025</td></tr>'
 '<tr><td>Heavyweight (interim)</td><td>Ciryl Gane</td><td>KO2 Alex Pereira, Freedom 250, June 14, 2026</td></tr>'
 '<tr><td>Light Heavyweight</td><td>Carlos Ulberg</td><td>KO1 Ji&#345;&iacute; Proch&aacute;zka for the vacant belt, UFC 327, April 11, 2026</td></tr>'
 '<tr><td>Middleweight</td><td>Sean Strickland</td><td>Split decision over Khamzat Chimaev, UFC 328, May 9, 2026 &mdash; two-time champion</td></tr>'
 '<tr><td>Welterweight</td><td>Islam Makhachev</td><td>UD Jack Della Maddalena, UFC 322, Nov 15, 2025. 1 defence &mdash; UD Ian Machado Garry, UFC 330, Aug 15, 2026</td></tr>'
 '<tr><td>Lightweight</td><td>Justin Gaethje</td><td>TKO4 Ilia Topuria, Freedom 250, June 14, 2026</td></tr>'
 '<tr><td>Featherweight</td><td>Alexander Volkanovski</td><td>UD Diego Lopes, UFC 314, April 12, 2025; defended UD Lopes, UFC 325, Jan 31, 2026</td></tr>'
 '<tr><td>Bantamweight</td><td>Petr Yan</td><td>UD Merab Dvalishvili, UFC 323, Dec 6, 2025</td></tr>'
 '<tr><td>Flyweight</td><td>Joshua Van</td><td>TKO1 Alexandre Pantoja, UFC 323, Dec 6, 2025; defended TKO5 Tatsuro Taira, UFC 328, May 9, 2026</td></tr>'
 '<tr><td>Women&rsquo;s Flyweight</td><td>Valentina Shevchenko</td><td>Out of UFC 332 with an undisclosed injury; an interim title bout is reported</td></tr>'
 '<tr><td>Women&rsquo;s Bantamweight</td><td>Kayla Harrison</td><td>Sub2 Julianna Pe&ntilde;a, UFC 316, June 7, 2025 &mdash; 0 defenses</td></tr>'
 '<tr><td>Women&rsquo;s Strawweight</td><td>Mackenzie Dern</td><td>UD Virna Jandiroba, UFC 321, Oct 25, 2025. 1 defence &mdash; UD Gillian Robertson, UFC 330, Aug 15, 2026</td></tr>'
 '</table><div class="note"><strong>A caution for readers checking elsewhere.</strong> A widely syndicated '
 '&ldquo;current champions&rdquo; listing still shows Alex Pereira at light heavyweight, Khamzat Chimaev at '
 'middleweight and Ilia Topuria at lightweight. All three were superseded by results at UFC 327 (April 11, 2026), '
 'UFC 328 (May 9, 2026) and Freedom 250 (June 14, 2026) respectively, and the board above reflects those results.'
 '</div></div>')

b.append(sources([
 ("UFC.com &mdash; Main Card Results, UFC Shanghai: Nurmagomedov vs Song", "https://www.ufc.com/news/ufc-shanghai-results-nurmagomedov-vs-song"),
 ("UFC.com &mdash; UFC Fight Night: Hooker vs Parnasse (Sept 5, 2026)", "https://www.ufc.com/event/ufc-fight-night-september-05-2026"),
 ("UFC.com &mdash; Fight by fight preview, UFC Paris", "https://www.ufc.com/news/fight-by-fight-preview-ufc-paris-hooker-vs-parnasse"),
 ("UFC.com &mdash; Bonus Coverage, UFC Shanghai", "https://www.ufc.com/news/ufc-fight-night-shanghai-2026-bonus-coverage"),
 ("Bloody Elbow &mdash; UFC 332 update: new main event will be announced this week", "https://bloodyelbow.com/2026/09/02/ufc-332-update-new-main-event-will-be-announced-this-week-after-title-fight-collapsed-due-to-injury/"),
 ("Athlon Sports &mdash; Shevchenko out of UFC 332, Wang Cong&ndash;Silva reportedly targeted", "https://athlonsports.com/mma/ufc-332-wang-cong-natalia-silva-shevchenko-rematch"),
 ("Rotowire &mdash; Hooker vs Parnasse odds, Sept 5, 2026", "https://www.rotowire.com/betting/mma/fight/salahdine-parnasse-vs-dan-hooker-odds-2026-09-05-5365"),
 ("Sherdog &mdash; Dana White&rsquo;s Contender Series 2026: Week 5", "https://www.sherdog.com/events/Dana-Whites-Contender-Series-Contender-Series-2026-Week-5-112631"),
 ("Yahoo Sports &mdash; Dana White signs 5 new UFC fighters after DWCS week 4", "https://sports.yahoo.com/articles/dana-white-signs-5-ufc-042710022.html"),
 ("ESPN &mdash; Current and all-time UFC champions", "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
]))
b.append('<p class="disc">The Octagon is an automated summary of published MMA reporting. Cards and bouts are subject '
 'to change. Betting lines are quoted as listed and move constantly.</p></footer>')

CDN = """<script>(function(){var t=new Date('2026-09-05T15:00:00-04:00');var el=document.getElementById('ufccdn');
function tick(){if(!el)return;var d=t-new Date();if(d<=0){el.textContent='Fight week \\u2014 live/completed';return;}
var dd=Math.floor(d/86400000),hh=Math.floor(d%86400000/3600000),mm=Math.floor(d%3600000/60000);
el.textContent=dd+'d '+hh+'h '+mm+'m';}tick();setInterval(tick,30000);})();</script>"""

H = page("The Octagon &mdash; Daily Briefings", M["accent"], M["accent2"], M["bg"], M["panel"], M["line"], "\n".join(b), extra_js=CDN)
open(os.path.join(OUT, "mma-briefing.html"), "w").write(H)
print("mma ok", len(H))
