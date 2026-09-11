# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page
from build_1530 import S_MMA, tldr, FRESH, srcblock

OUT = os.path.dirname(os.path.abspath(__file__))
ACC, ACC2 = "#e84545", "#ff8a5c"
EXTRA = """
.cdn{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:11px;
  padding:12px 16px;margin-bottom:16px;display:flex;flex-wrap:wrap;align-items:baseline;gap:12px}
.cdn .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.cdn .v{font-family:var(--mono);font-size:18px;color:var(--txt);letter-spacing:-.3px}
.cdn .w{font-size:13.5px;color:var(--muted)}
.dtv{font-family:var(--mono);font-size:11px;letter-spacing:.11em;text-transform:uppercase;color:var(--warn);margin-bottom:6px}
"""
CSS = css(ACC, ACC2, "#100c0c", "#1a1313", "#322020", EXTRA)

SRC = [
 ("UFC.com - Official Weigh-In Results | Noche UFC (Sept. 11, 2026)",
  "https://www.ufc.com/news/noche-ufc-silva-delgado-official-weigh-in-results"),
 ("UFC.com - Main Card Results | UFC Paris (Hooker vs Parnasse)",
  "https://www.ufc.com/news/ufc-paris-results-hooker-vs-parnasse"),
 ("UFC.com - Bonus Coverage | UFC Paris",
  "https://www.ufc.com/news/bonus-coverage-ufc-fight-night-paris-2026"),
 ("UFC.com - Women's Flyweight Championship Leads Showcase Of Rising Stars In UFC Return To Salt Lake City",
  "https://www.ufc.com/news/womens-flyweight-championship-leads-showcase-rising-stars-ufc-return-salt-lake-city"),
 ("UFC.com - Fighters On The Rise | Noche UFC (McMillen, Rongzhu, Tarin)",
  "https://www.ufc.com/news/fighters-on-the-rise-noche-ufc-mcmillen-rongzhu-tarin"),
 ("UFC.com - UFC Fight Night: Silva vs Delgado event page",
  "https://www.ufc.com/event/ufc-fight-night-september-12-2026"),
 ("Wikipedia - UFC Fight Night: Silva vs. Delgado",
  "https://en.wikipedia.org/wiki/UFC_Fight_Night:_Silva_vs._Delgado"),
 ("Wikipedia - UFC 331", "https://en.wikipedia.org/wiki/UFC_331"),
 ("Yahoo Sports - UFC 331 fight card revealed, Van vs. Pantoja 2 leads loaded lineup",
  "https://sports.yahoo.com/articles/ufc-331-fight-card-revealed-235537467.html"),
 ("Yahoo Sports - Noche UFC preview and predictions: Can Jose Delgado actually upset Jean Silva?",
  "https://ca.sports.yahoo.com/news/noche-ufc-preview-and-predictions-can-jose-delgado-actually-upset-jean-silva-173056798.html"),
 ("Yahoo Sports - Noche UFC video: Jean Silva, Jose Delgado make weight in Arizona",
  "https://ca.sports.yahoo.com/news/noche-ufc-video-jean-silva-162920602.html"),
 ("CBS Sports - Noche UFC predictions: Jean Silva vs. Jose Delgado fight card, odds and expert picks",
  "https://www.cbssports.com/ufc/news/noche-ufc-fight-card-predictions-jean-silva-jose-delgado-odds/"),
 ("RotoWire - Silva vs Delgado Sep 12, 2026 Odds",
  "https://www.rotowire.com/betting/mma/fight/jose-delgado-vs-jean-silva-odds-2026-09-12-5614"),
 ("ESPN - Current and all-time UFC champions",
  "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
]

CDN = """<div class="cdn">
<span class="k">Next card</span>
<span class="v" id="ufccdn">&nbsp;</span>
<span class="w">Noche UFC: Silva vs Delgado &mdash; Sat 12 Sept, Desert Diamond Arena, Glendale, AZ. Prelims 2 PM ET, main card 5 PM ET, Paramount+.</span>
</div>
<script>(function(){var t=new Date('2026-09-12T14:00:00-04:00');function u(){var e=document.getElementById('ufccdn');if(!e)return;var d=t-new Date();if(d<=0){e.textContent='Fight week \\u2014 live/completed';return;}var dd=Math.floor(d/864e5),hh=Math.floor(d%864e5/36e5),mm=Math.floor(d%36e5/6e4);e.textContent=dd+'d '+hh+'h '+mm+'m';}u();setInterval(u,3e4);})();</script>"""

BODY = """@@MAST@@
@@TLDR@@
@@FRESH@@
@@NAV@@

@@CDN@@

<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<div class="tags"><span class="t new">New</span><span class="t hot">Fight week</span><span class="t gold">Noche UFC</span></div>
<h3 style="font-size:20px;margin:0 0 9px">The Whole Card Made Weight in Glendale &mdash; Thirteen Bouts, No Misses, and a Headliner Who Took the Fight on Under a Month&rsquo;s Notice</h3>
<p>UFC.com published the official weights on Friday morning for <b>NOCHE UFC: SILVA vs DELGADO</b>, Saturday 12 September at the <b>Desert Diamond Arena in Glendale, Arizona</b> &mdash; the promotion&rsquo;s <b>first event at that venue</b> and its fourth annual Mexican Independence Day card. <b>All thirteen bouts made weight.</b> The main event is scheduled for five rounds; every other bout is three.</p>
<p>At the top, <b>Jean Silva</b> weighed in at <b>145</b> and <b>Jose Miguel Delgado</b> at <b>145.5</b>. Silva (<b>17-3 MMA, 6-1 UFC</b>) was originally booked opposite <b>Yair Rodriguez</b>, who withdrew injured; Delgado (<b>12-2 MMA, 4-1 UFC</b>) stepped in on <b>less than a month&rsquo;s notice</b>. Two things make the matchup unusual. Silva becomes the <b>first fighter to headline multiple Noche UFC events</b>, and he does it in <b>back-to-back appearances</b> &mdash; last year&rsquo;s went against him, a loss to <b>Diego Lopes</b> in San Antonio. And Delgado is <b>Arizona&rsquo;s own</b> and <b>unranked</b>, getting the biggest fight of his career in his home state against a top-ten featherweight.</p>
<p style="margin-bottom:0">Prelims air at <b>2 PM ET / 11 AM PT</b> and the main card at <b>5 PM ET / 2 PM PT</b>, with every bout streaming on <b>Paramount+</b> &mdash; a special earlier slot than the usual Fight Night window. The card is stacked with Mexican and Latin American talent, including former champions in <b>Brandon Moreno</b> and <b>Alexa Grasso</b>. Immediately after the card, UFC turns over to Zuffa Boxing for <b>Garcia vs Benn</b>, with <b>Jai Opetaia vs Noel Mikaelian</b> in the co-main.</p>
</div>

<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>
<div class="cards">

<div class="card">
<div class="tags"><span class="t hot">Tomorrow</span></div>
<div class="dtv">Sat 12 Sept &middot; Desert Diamond Arena, Glendale, AZ</div>
<h4>Noche UFC: Silva vs Delgado (Fight Night 288)</h4>
<p><b>Jean Silva (145) vs Jose Miguel Delgado (145.5)</b>, featherweight, five rounds. Yair Rodriguez withdrew injured and Delgado replaced him on short notice. Co-main: <b>Brandon Moreno (125.5) vs Joseph Morales (125.5)</b>.</p>
<p style="margin:9px 0 0"><b>Odds:</b> Silva <b>&minus;440</b> / Delgado <b>+340</b> (DraftKings, per a RotoWire listing read this run). Method props have Silva by KO/TKO at <b>&minus;145</b> and by decision at <b>+460</b>; Delgado&rsquo;s best path is KO/TKO at <b>+700</b>. <span class="mut">The line has moved across books through the week &mdash; earlier reads this week showed &minus;425/+330 and &minus;441/+310 &mdash; so the book is named rather than a single price presented as the market.</span> Co-main: <b>Moreno &minus;102 / Morales &minus;125</b>.</p>
</div>

<div class="card">
<div class="tags"><span class="t">Next week</span><span class="t gold">Title fight</span></div>
<div class="dtv">Sat 19 Sept &middot; Crypto.com Arena, Los Angeles, CA</div>
<h4>UFC 331: Van vs Pantoja 2</h4>
<p>A <b>flyweight championship rematch</b> headlines: reigning champion <b>Joshua Van</b> against former champion <b>Alexandre Pantoja</b>. The co-main is a five-rounder with title implications &mdash; <b>No. 2-ranked lightweight Arman Tsarukyan vs Mauricio Ruffy</b>. Also booked: <b>Marlon Vera vs Charles Jourdain</b> at bantamweight.</p>
<p style="margin:9px 0 0"><span class="mut">No main-event moneyline is printed &mdash; no source read this run states one for Van vs Pantoja 2.</span></p>
</div>

<div class="card">
<div class="tags"><span class="t gold">Vacant title</span></div>
<div class="dtv">Sat 3 Oct &middot; Salt Lake City, UT</div>
<h4>UFC 332: Silva vs Wang</h4>
<p>The <b>vacant women&rsquo;s flyweight championship</b> headlines UFC&rsquo;s return to Salt Lake City: <b>(#1) Natalia Silva vs (#8) Wang Cong</b>. Valentina Shevchenko vacated the belt while injured and is guaranteed a title shot when cleared. Also featured on UFC&rsquo;s own billing: <b>(#9) Deiveson Figueiredo vs (#11) Payton Talbott</b>.</p>
<p style="margin:9px 0 0"><span class="mut">The winner&rsquo;s first challenger may already be on tomorrow&rsquo;s card &mdash; preview coverage describes the Fiorot&ndash;Grasso winner as next in line for whoever is crowned.</span></p>
</div>

<div class="card">
<div class="tags"><span class="t gold">Two title fights</span></div>
<div class="dtv">Sat 24 Oct &middot; Abu Dhabi</div>
<h4>UFC 333</h4>
<p>Two champions are booked to defend on the same card: featherweight champion <b>Alexander Volkanovski</b> and bantamweight champion <b>Petr Yan</b>. <span class="mut">Carried from this desk&rsquo;s standing verified record rather than from a source read this run; no bout order, odds or full lineup is asserted.</span></p>
</div>

</div>

<h2 class="sec">Tomorrow&rsquo;s Card &mdash; Official Weights</h2>
<div class="panel">
<table>
<tr><th>Bout</th><th>Weights</th><th>Slot</th></tr>
<tr><td><b>Jean Silva vs Jose Miguel Delgado</b> &mdash; featherweight</td><td>145 / 145.5</td><td>Main event (5 rds)</td></tr>
<tr><td><b>Brandon Moreno vs Joseph Morales</b> &mdash; flyweight</td><td>125.5 / 125.5</td><td>Co-main</td></tr>
<tr><td>Tommy McMillen vs Marwan Rahiki &mdash; featherweight</td><td>145 / 145.5</td><td>Main card</td></tr>
<tr><td>Manon Fiorot vs Alexa Grasso &mdash; women&rsquo;s flyweight</td><td>125 / 125</td><td>Main card</td></tr>
<tr><td>Waldo Cortes Acosta vs Curtis Blaydes &mdash; heavyweight</td><td>262 / 260</td><td>Main card</td></tr>
<tr><td>David Martinez vs Dan Ige &mdash; bantamweight</td><td>135 / 135.5</td><td>Main card</td></tr>
<tr><td>Tim Elliott vs Edgar Chairez &mdash; catchweight (130 lbs)</td><td>130 / 130</td><td>Prelims</td></tr>
<tr><td>Ignacio Bahamondes vs Muslim Salikhov &mdash; welterweight</td><td>170 / 170.5</td><td>Prelims</td></tr>
<tr><td>Yousri Belgaroui vs Djorden Santos &mdash; middleweight</td><td>185.5 / 185</td><td>Prelims</td></tr>
<tr><td>Drakkar Klose vs Tommy Gantt &mdash; lightweight</td><td>155.5 / 155.5</td><td>Prelims</td></tr>
<tr><td>Rafa Garcia vs Rongzhu &mdash; lightweight</td><td>155 / 155</td><td>Prelims</td></tr>
<tr><td>Sean King III vs Jessie Rosas &mdash; featherweight</td><td>145.5 / 145.5</td><td>Prelims</td></tr>
<tr><td>JJ Aldrich vs Regina Tarin &mdash; women&rsquo;s flyweight</td><td>125 / 125</td><td>Prelims</td></tr>
</table>
<p class="note">Weights as published by UFC.com on 11 September 2026. Names and spellings are reproduced exactly as UFC.com renders them on the official weigh-in results page. No fighter missed weight.</p>
</div>

<h2 class="sec">Last Event &mdash; Results</h2>
<div class="panel">
<p style="margin:0 0 12px"><b>UFC Fight Night: Hooker vs Parnasse (UFC Paris)</b> &mdash; Saturday 5 September 2026, Accor Arena, Paris, France. Main card results as published by UFC.com:</p>
<table>
<tr><th>Result</th><th>Bout</th><th>Method</th></tr>
<tr><td class="up">Parnasse</td><td><b>Salahdine Parnasse</b> def. Dan Hooker &mdash; main event</td><td>TKO, Round 1, 2:25</td></tr>
<tr><td class="up">Sola</td><td><b>Axel Sola</b> def. Far&egrave;s Ziam &mdash; co-main</td><td>KO, Round 1, 1:40</td></tr>
<tr><td class="up">Page</td><td><b>Michael &ldquo;Venom&rdquo; Page</b> def. Nursulton Ruziboev</td><td>Unanimous decision (29-28, 29-28, 29-28)</td></tr>
<tr><td class="up">Donchenko</td><td><b>Daniil Donchenko</b> def. Punahele Soriano</td><td>Unanimous decision (30-27, 30-27, 29-28)</td></tr>
<tr><td class="up">Campbell</td><td><b>Kurtis Campbell</b> def. Trevor Peek</td><td>Submission, rear-naked choke, Round 3, 3:07</td></tr>
<tr><td class="up">Keita</td><td><b>Losene Keita</b> def. Muhammad Naimov</td><td>KO, Round 1, 2:54</td></tr>
</table>
<p class="note"><b>Bonuses (UFC.com):</b> four <b>Performance of the Night</b> awards and no Fight of the Night &mdash; <b>Salahdine Parnasse</b>, <b>Axel Sola</b>, <b>Losene Keita</b> and <b>Mario Pinto</b>, the last for a second-round stoppage of Ryan Spann <b>55 seconds into Round 2</b> that kept him undefeated. <span class="mut">UFC.com does not state a dollar figure for the bonuses, so none is printed.</span></p>
<p class="note"><b>Around the results:</b> Parnasse &mdash; a former <b>two-division champion outside the UFC</b>, 28 years old and debuting in a five-round main event on home soil &mdash; hurt Hooker with a body kick midway through the round and finished against the fence. He has now <b>won six straight, all by stoppage</b>, and UFC.com says he &ldquo;instantly enters the highly touted lightweight Top 15.&rdquo; Michael Venom Page has now <b>won four straight</b> and all three of his middleweight appearances. Donchenko, a <b>TUF winner</b>, extended his streak to <b>eight</b> with a third consecutive UFC win and called for Daniel Rodriguez. Campbell earned his <b>first UFC win</b> and became the first to finish Trevor Peek. Keita, a former <b>Oktagon MMA double champion</b>, took his first UFC win and called out Lerone Murphy.</p>
</div>

<h2 class="sec">Prospect Watch</h2>
<div class="cards">

<div class="card">
<div class="tags"><span class="t new">New</span><span class="t pro">Prospect</span></div>
<h4>Tommy McMillen, Rongzhu and Regina Tarin</h4>
<p>UFC.com&rsquo;s &ldquo;Fighters On The Rise&rdquo; feature for Noche UFC names three names to watch on tomorrow&rsquo;s card: <b>Tommy McMillen</b>, who meets Marwan Rahiki on the main card; <b>Rongzhu</b>, opposite Rafa Garcia at lightweight; and <b>Regina Tarin</b>, facing JJ Aldrich at women&rsquo;s flyweight. All three made weight Friday morning.</p>
</div>

<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t pro">Prospect</span></div>
<h4>Quentin Pasley (4-0)</h4>
<p>Won a UFC contract on <b>Dana White&rsquo;s Contender Series season 10, week 5</b> on <b>Tuesday 8 September</b> at the Meta Apex, stopping <b>Arlind Berisha</b> with elbows at <b>4:41 of round one</b>.</p>
</div>

<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t pro">Prospect</span></div>
<h4>Christian Natividad (10-0)</h4>
<p>Also signed out of DWCS week 5, with a <b>first-round body-punch knockout of Colton Loud at 1:10</b>. Alongside him, <b>Mart&iacute;n Koz&aacute;k</b> (TKO, punches, round two, 1:32 over Christian Echols) and <b>Isaac Moreno</b> (unanimous decision, 29-28 across the board, over Reginaldo Geraldo Jr.) also earned contracts. <b>Apollo Gomes</b> beat Kwon Won-il by unanimous decision but was <b>not</b> signed.</p>
</div>

</div>

<h2 class="sec">Around the Sport</h2>
<div class="panel">
<ul class="bul">
<li><b>Zuffa Boxing follows Noche UFC on the same night.</b> UFC&rsquo;s own coverage points viewers straight from the Glendale card to <b>Garcia vs Benn</b> &mdash; Ryan Garcia against Conor Benn &mdash; with <b>Jai Opetaia vs Noel Mikaelian</b> as the co-main. Both are billed by UFC.com as title fights.</li>
<li><b>Alexa Grasso returns.</b> UFC.com frames the former women&rsquo;s flyweight champion&rsquo;s bout with <b>Manon Fiorot</b> as being &ldquo;back on the hunt for gold&rdquo; &mdash; with the division&rsquo;s belt vacant and being contested at UFC 332, the winner has an obvious claim.</li>
<li><b>Brandon Moreno is approaching a decade in the UFC.</b> The former two-time flyweight champion faces TUF 33 winner <b>Joseph Morales</b> in the co-main; Moreno enters on a two-fight skid.</li>
<li><b>Dan Ige has moved to bantamweight.</b> The veteran meets <b>David Martinez</b> on the main card in his first outing at 135; UFC.com&rsquo;s interview with him is headlined &ldquo;A Change Can Do You Good.&rdquo;</li>
<li><b>DWCS season 10 continues Tuesday.</b> Week 6 is <b>Tuesday 15 September</b>; the series airs Tuesdays from the Meta Apex in Las Vegas.</li>
</ul>
</div>

<h2 class="sec">Rankings &amp; Business</h2>
<div class="panel">
<ul class="bul">
<li><b>Rankings movement:</b> UFC.com seeds the UFC 332 headliner as <b>(#1) Natalia Silva vs (#8) Wang Cong</b> and its co-feature as <b>(#9) Deiveson Figueiredo vs (#11) Payton Talbott</b>. <b>Arman Tsarukyan</b> is listed at <b>No. 2 at lightweight</b> going into UFC 331. UFC.com says Salahdine Parnasse <b>&ldquo;instantly enters the highly touted lightweight Top 15&rdquo;</b> after Paris; Jean Silva sits at <b>No. 6 at featherweight</b> in the MMA Fighting Global Rankings, and <b>Jose Miguel Delgado is unranked</b>.</li>
<li><b>UFC Paris set a venue record.</b> UFC.com reports <b>gross total revenue of $4,365,335</b> and <b>attendance of 15,687 (sold out)</b> &mdash; the <b>highest-grossing event in Accor Arena history</b>.</li>
<li><b>No viewership or TKO Group figure is published this edition.</b> No source read this run states one, and none is inferred.</li>
</ul>
</div>

<h2 class="sec">Champions Board</h2>
<div class="panel">
<table>
<tr><th>Division</th><th>Champion</th><th>Note</th></tr>
<tr><td>Heavyweight</td><td><b>Tom Aspinall</b></td><td>Undisputed. <b>Interim:</b> Ciryl Gane (KO2 Pereira, Freedom 250, 14 Jun 2026).</td></tr>
<tr><td>Light Heavyweight</td><td><b>Carlos Ulberg</b></td><td>Won the vacant belt KO1 over Ji&#345;&iacute; Proch&aacute;zka at UFC 327 (11 Apr 2026); tore an ACL in the win and is out until 2027.</td></tr>
<tr><td>Middleweight</td><td><b>Sean Strickland</b></td><td>Split-decision upset of Khamzat Chimaev at UFC 328 (9 May 2026); two-time champion.</td></tr>
<tr><td>Welterweight</td><td><b>Islam Makhachev</b></td><td>1 defence &mdash; UD over Ian Machado Garry, UFC 330 (15 Aug 2026); 17th straight UFC win, a record.</td></tr>
<tr><td>Lightweight</td><td><b>Justin Gaethje</b></td><td>TKO4 of Ilia Topuria, Freedom 250 (14 Jun 2026).</td></tr>
<tr><td>Featherweight</td><td><b>Alexander Volkanovski</b></td><td>Defended UD over Diego Lopes, UFC 325 (31 Jan 2026); ties Jos&eacute; Aldo at 8 featherweight title defences. Booked to defend at UFC 333.</td></tr>
<tr><td>Bantamweight</td><td><b>Petr Yan</b></td><td>UD over Merab Dvalishvili, UFC 323 (6 Dec 2025). Booked to defend at UFC 333.</td></tr>
<tr><td>Flyweight</td><td><b>Joshua Van</b></td><td>1 defence &mdash; TKO5 Tatsuro Taira, UFC 328 (9 May 2026). Faces Alexandre Pantoja in a rematch at UFC 331 on 19 September.</td></tr>
<tr><td>Women&rsquo;s Flyweight</td><td class="nc"><b>VACANT</b></td><td>Valentina Shevchenko <b>vacated</b> while injured. <b>Natalia Silva vs Wang Cong contest the vacant title at UFC 332, Salt Lake City, 3 October 2026.</b> Shevchenko is guaranteed a title shot when cleared.</td></tr>
<tr><td>Women&rsquo;s Bantamweight</td><td><b>Kayla Harrison</b></td><td>Sub2 Julianna Pe&ntilde;a, UFC 316 (7 Jun 2025); <b>0 defences</b> &mdash; the UFC 324 defence vs Amanda Nunes was cancelled after Harrison withdrew for neck surgery.</td></tr>
<tr><td>Women&rsquo;s Strawweight</td><td><b>Mackenzie Dern</b></td><td>1 defence &mdash; UD over Gillian Robertson, UFC 330 (15 Aug 2026).</td></tr>
</table>
<p class="note">Every row is checked against the latest completed event before publication. The women&rsquo;s flyweight row is independently corroborated by a source read this run: UFC.com&rsquo;s own UFC 332 billing headlines the card with the <b>women&rsquo;s flyweight championship</b> between Natalia Silva and Wang Cong &mdash; a title fight that only exists because the belt is vacant. Any &ldquo;current champions&rdquo; listing that still seats Shevchenko at 125 lb, Alex Pereira at light heavyweight or Khamzat Chimaev at middleweight predates the events that changed those belts and is refused on sight.</p>
</div>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
@@SRCS@@
</div>
<p class="disc">Compiled automatically from public reporting gathered during this run. Cards and bouts are subject to change &mdash; fighters withdraw, bouts are rebooked and betting lines move, sometimes within hours of publication. Records, methods, odds and financial figures appear only where a source read this run states them; where a figure was absent, this page says so rather than supplying one.</p>
"""

BODY = (BODY.replace("@@MAST@@", masthead("The Octagon", "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
            .replace("@@TLDR@@", tldr("Tale of the Tape", S_MMA))
            .replace("@@FRESH@@", FRESH)
            .replace("@@NAV@@", nav("mma"))
            .replace("@@CDN@@", CDN)
            .replace("@@SRCS@@", srcblock(SRC)))

io.open(os.path.join(OUT, "mma-briefing.html"), "w", encoding="utf-8").write(
    page("The Octagon &mdash; Daily Briefings", CSS, BODY))
print("mma ok")
