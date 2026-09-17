# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))

EXTRA = """
.cdbar{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);
  border-radius:10px;padding:11px 15px;margin-bottom:16px;display:flex;flex-wrap:wrap;align-items:baseline;gap:11px}
.cdbar .lab{font-family:var(--mono);font-size:10.5px;letter-spacing:.17em;text-transform:uppercase;color:var(--accent)}
.cdbar .val{font-family:var(--mono);font-size:17px;color:var(--txt)}
.cdbar .ev{font-size:14px;color:#cfcbc6}
.dv{font-family:var(--mono);font-size:11px;letter-spacing:.09em;color:var(--warn);margin-bottom:6px}
"""
CSS = css("#e84545", "#ff8a5c", "#100c0c", "#1a1313", "#322020", EXTRA)

TLDR = ("It is fight week for UFC 331 in Los Angeles, where Joshua Van defends the flyweight title "
        "against Alexandre Pantoja on Saturday &mdash; and, contrary to two aggregator reports, the "
        "champion has not withdrawn.")

CDN = """<script>(function(){var t=new Date('2026-09-19T21:00:00-04:00');function f(){var el=document.getElementById('ufccdn');if(!el)return;var d=t-new Date();if(d<=0){el.textContent='Fight week \\u2014 live/completed';return;}var dd=Math.floor(d/86400000),hh=Math.floor(d/3600000)%24,mm=Math.floor(d/60000)%60;el.textContent=dd+'d '+hh+'h '+mm+'m';}f();setInterval(f,30000);})();</script>"""

BODY = """@@MAST@@
<div class="tldr"><b>Tale of the Tape</b> <span>@@TLDR@@</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
@@NAV@@

<div class="cdbar">
<span class="lab">Next Card</span>
<span class="val" id="ufccdn">&nbsp;</span>
<span class="ev">UFC 331 &middot; Van vs. Pantoja 2 &middot; Crypto.com Arena, Los Angeles &middot; Sat 19 Sep, main card 9:00 p.m. ET</span>
</div>

<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 9px;font-size:21px">Fight week in Los Angeles: Van defends against Pantoja, nine months after 23 seconds</h3>
<p style="margin:0 0 10px"><strong>UFC 331</strong> lands on <strong>Saturday 19 September</strong> at <strong>Crypto.com Arena</strong> in Los Angeles, headlined by a <strong>flyweight title rematch</strong> between champion <strong>Joshua Van</strong> and <strong>Alexandre Pantoja</strong>. Their first meeting, at <strong>UFC 323</strong>, ended after <strong>23 seconds</strong> when Pantoja succumbed to an elbow injury &mdash; which is why this one is being sold as unfinished business rather than a repeat. Van is out to prove he is the legitimate champion; Pantoja is trying to become the third fighter to hold the flyweight title twice.</p>
<p style="margin:0 0 10px">The market has it close. Kalshi's win probabilities, as carried by Covers, put <strong>Van at 56%</strong> and <strong>Pantoja at 44%</strong>; in conventional American lines Yahoo Sports has <strong>Van &minus;130</strong> and <strong>Pantoja +110</strong>. Underneath, <strong>Arman Tsarukyan</strong> (72% / &minus;305) meets <strong>Mauricio Ruffy</strong> (28% / +240) in a lightweight co-main, and <strong>Dooho Choi</strong> (72% / &minus;270) faces <strong>Patricio Pitbull</strong> (28% / +220). Covers spells the Korean featherweight <strong>&ldquo;Dooho Choi&rdquo;</strong>; other outlets write <strong>&ldquo;Doo Ho Choi&rdquo;</strong> &mdash; the variant is noted here rather than silently chosen.</p>
<p style="margin:0" class="note"><strong>Standing correction, carried forward: the flyweight champion has not pulled out of UFC 331.</strong> Two aggregators have circulated a claim that Joshua Van withdrew late in fight week. Three primary reads refute it: UFC.com's own <em>Updates To Crypto.com UFC 331</em> page lists exactly one change &mdash; Brian Ortega out with injury &mdash; the same page's event module still renders the Van&ndash;Pantoja title bout for Saturday, and Wikipedia's UFC 331 entry, which documents the Oliveira, Harrison&ndash;Nunes and Blaydes withdrawals in detail, records no Van withdrawal at all. Two aggregators agreeing is one source; a card change is real when the promotion's own announcement page says so.</p>
</div>

<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>
<div class="cards">
<div class="card">
<div class="dv">Sat 19 Sep &middot; Crypto.com Arena, Los Angeles</div>
<div class="tags"><span class="t hot">Title fight</span><span class="t">UFC 331</span></div>
<h3>Joshua Van vs. Alexandre Pantoja 2</h3>
<p>Flyweight championship rematch. Early prelims 5:30 p.m. ET, prelims 7 p.m. ET, main card 9 p.m. ET on Paramount+. <strong>Odds: Van 56% / Pantoja 44% (Kalshi, via Covers, updated 16 Sep 9:51 a.m. ET); Van &minus;130 / Pantoja +110 (Yahoo Sports).</strong></p>
</div>
<div class="card">
<div class="dv">Sat 3 Oct &middot; Delta Center, Salt Lake City</div>
<div class="tags"><span class="t gold">Vacant title</span><span class="t">UFC 332</span></div>
<h3>Nat&aacute;lia Silva vs. Wang Cong</h3>
<p>For the <strong>vacant women's flyweight title</strong>, after Valentina Shevchenko vacated with a ligament injury to her back and shoulder expected to sideline her for a year. This is the first numbered-event main card to air on <strong>CBS</strong>: prelims 4 p.m. ET on Paramount+, main card 8 p.m. ET. Also booked: Payton Talbott vs. D. Figueiredo, Roman Kopylov vs. Ateba Gautier, Khaos Williams vs. Roberto Soldi&#263;, Mick Parkin vs. Johnny Walker. <em>No source fetched this run states a betting line for this card.</em></p>
</div>
<div class="card">
<div class="dv">Sat 24 Oct &middot; Abu Dhabi</div>
<div class="tags"><span class="t">Two title fights</span><span class="t">UFC 333</span></div>
<h3>Volkanovski and Yan both defend</h3>
<p>Featherweight champion <strong>Alexander Volkanovski</strong> and bantamweight champion <strong>Petr Yan</strong> are both booked to defend. <em>No source fetched this run states a betting line for this card.</em></p>
</div>
</div>

<h2 class="sec">Last Event &mdash; Noche UFC, Glendale, 12 September</h2>
<div class="panel" style="padding:4px 0">
<table>
<tr><th>Result</th><th>Bout</th><th>Method</th></tr>
<tr><td class="up">Jean Silva</td><td>def. Jose Miguel Delgado</td><td>Submission (rear-naked choke), 2:57 R3</td></tr>
<tr><td class="up">Brandon Moreno</td><td>def. Morales</td><td>Split decision</td></tr>
<tr><td class="up">Tommy McMillen</td><td>def. Marwan Rahiki</td><td>Unanimous decision (29-28, 29-28, 29-27)</td></tr>
<tr><td class="up">Alexa Grasso</td><td>def. Manon Fiorot</td><td>Unanimous decision (29-28 &times;3)</td></tr>
<tr><td class="up">Curtis Blaydes</td><td>def. Waldo Cortes-Acosta</td><td>Unanimous decision (29-28 &times;3)</td></tr>
<tr><td class="up">Martinez</td><td>def. Dan Ige</td><td>Unanimous decision (30-27, 30-27, 29-28)</td></tr>
<tr><td class="up">Sean King III</td><td>def. Jessie Rosas</td><td>KO (slam), 0:36 R1 &mdash; UFC debut</td></tr>
</table>
</div>
<p class="note"><strong>Bonuses:</strong> Performance of the Night and <strong>$100,000</strong> each to <strong>Jean Silva</strong> and <strong>Sean King III</strong>; <strong>Fight of the Night</strong> to <strong>Tommy McMillen vs. Marwan Rahiki</strong>. Delgado took the main event on short notice after Yair Rodriguez was forced out with injury. No scores are printed for Moreno&ndash;Morales: UFC's own copy renders that scoreline inconsistently, so only the decision type is carried. Two competitors appear by surname alone &mdash; Morales and Martinez &mdash; because that is how the source copy gives them; no first name is guessed. UFC's bonus page and its own video title both give King's finishing time as <strong>0:36</strong>.</p>

<h2 class="sec">Prospect Watch</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t pro">Prospect</span><span class="t">Featherweight</span></div>
<h3>Tommy McMillen &mdash; 12-0</h3>
<p>Took his record to <strong>12-0</strong> with a unanimous decision over fellow undefeated featherweight <strong>Marwan Rahiki</strong> at Noche UFC, in a three-round slugfest that earned <strong>Fight of the Night</strong>. Two unbeaten prospects were matched against each other and the division got a genuine answer out of it.</p>
</div>
<div class="card">
<div class="tags"><span class="t pro">Prospect</span><span class="t">Debut</span></div>
<h3>Sean King III &mdash; 7-0</h3>
<p>A <strong>0:36 slam knockout</strong> of Jessie Rosas on his UFC debut, worth a <strong>$100,000</strong> Performance of the Night bonus and a record of <strong>7-0</strong>. Debuts do not announce themselves much louder than that.</p>
</div>
<div class="card">
<div class="tags"><span class="t pro">Prospect</span><span class="t">Heavyweight</span></div>
<h3>Gable Steveson gets the main card</h3>
<p>The Olympic wrestling gold medallist receives his <strong>first main-card slot</strong> since arriving in the UFC, facing <strong>Sean Sharaf</strong> on Saturday. The market treats it as a formality: <strong>91% / 9%</strong> on Kalshi, <strong>&minus;1600 / +900</strong> in American lines &mdash; the widest gap on the card. Steveson himself invoked Mike Tyson vs. Peter McNeeley when asked about the matchmaking.</p>
</div>
</div>

<h2 class="sec">Around the Sport</h2>
<div class="panel">
<ul class="bul">
<li><strong>The heavyweight belt is still vacant.</strong> <strong>Tom Aspinall</strong> vacated the undisputed title on <strong>14 September</strong> &mdash; &ldquo;I'm absolutely gutted&rdquo; &mdash; saying ongoing complications with his eyes mean he cannot be medically cleared to fight. The trouble traces back to the double eye-poke in his <strong>no-contest with Ciryl Gane at UFC 321</strong>. He is not retiring. Reporting notes an <em>expectation</em> that interim champion <strong>Ciryl Gane</strong> will be elevated to undisputed, but no promotion has been announced, so the board below still reads vacant with Gane interim.</li>
<li><strong>Muhammad Mokaev still wants back in.</strong> The flyweight, released by the UFC in <strong>July 2024</strong> after beating Manuel Kape at UFC 304 despite a <strong>7-0</strong> promotional record, told interviewers this week that the promotion &ldquo;wasted two years of my life&rdquo; and that he intends to return. He has fought eight times since leaving and won the BRAVE CF belt.</li>
<li><strong>Michael Chandler is calling an upset</strong> at UFC 331 on Saturday.</li>
<li><strong>Bonus context on the last card:</strong> Noche UFC ran at the <strong>Desert Diamond Arena</strong> in Glendale, Arizona, on 12 September &mdash; a week before the pay-per-view returns to Los Angeles.</li>
</ul>
</div>

<h2 class="sec">Rankings &amp; Business</h2>
<div class="panel">
<p style="margin:0 0 9px"><strong>Rankings movement.</strong> Welterweight champion <strong>Islam Makhachev</strong> holds the record for consecutive Octagon victories at <strong>17 straight</strong>, set with his unanimous-decision defence over Ian Machado Garry at UFC 330 on 15 August. At featherweight, <strong>Movsar Evloev</strong> remains the number-one contender after beating Lerone Murphy at UFC London in March.</p>
<p style="margin:0" class="note"><strong>Business &amp; broadcast.</strong> UFC 332 on 3 October will be the first numbered-event main card carried on <strong>CBS</strong>, with prelims on Paramount+ &mdash; the clearest marker yet of the Paramount broadcast arrangement reshaping how numbered cards reach viewers. <em>No viewership, gate or TKO Group financial figure is published this run: no source fetched this run stated one.</em></p>
</div>

<h2 class="sec">Champions Board</h2>
<div class="panel" style="padding:4px 0">
<table>
<tr><th>Division</th><th>Champion</th><th>Note</th></tr>
<tr><td>Heavyweight</td><td class="mut">VACANT</td><td>Aspinall vacated 14 Sep 2026. <strong>Ciryl Gane</strong> holds the interim title (KO2 Pereira, Freedom 250, 14 Jun 2026).</td></tr>
<tr><td>Light Heavyweight</td><td>Carlos Ulberg</td><td>KO1 Ji&#345;&iacute; Proch&aacute;zka, UFC 327, 11 Apr 2026 &mdash; won the vacant belt.</td></tr>
<tr><td>Middleweight</td><td>Sean Strickland</td><td>Split decision over Khamzat Chimaev, UFC 328, 9 May 2026. Two-time champion.</td></tr>
<tr><td>Welterweight</td><td>Islam Makhachev</td><td>UD Jack Della Maddalena, UFC 322, 15 Nov 2025. One defence &mdash; UD Ian Machado Garry, UFC 330, 15 Aug 2026.</td></tr>
<tr><td>Lightweight</td><td>Justin Gaethje</td><td>TKO4 Ilia Topuria, Freedom 250, 14 Jun 2026.</td></tr>
<tr><td>Featherweight</td><td>Alexander Volkanovski</td><td>UD Diego Lopes, UFC 314, 12 Apr 2025. One defence. Booked to defend at UFC 333.</td></tr>
<tr><td>Bantamweight</td><td>Petr Yan</td><td>UD Merab Dvalishvili, UFC 323, 6 Dec 2025. Booked to defend at UFC 333.</td></tr>
<tr><td>Flyweight</td><td>Joshua Van</td><td>TKO1 Alexandre Pantoja, UFC 323, 6 Dec 2025; defended TKO5 Tatsuro Taira, UFC 328. Defends Saturday.</td></tr>
<tr><td>Women's Flyweight</td><td class="mut">VACANT</td><td>Shevchenko vacated with injury. Nat&aacute;lia Silva vs. Wang Cong contest it at UFC 332, 3 Oct.</td></tr>
<tr><td>Women's Bantamweight</td><td>Kayla Harrison</td><td>Sub2 Julianna Pe&ntilde;a, UFC 316, 7 Jun 2025. No defences.</td></tr>
<tr><td>Women's Strawweight</td><td>Mackenzie Dern</td><td>Reigning; ESPN's champions page agrees on this row.</td></tr>
</table>
</div>
<p class="note"><strong>Eleven belts, exactly two vacant.</strong> Refused this run: ESPN's &ldquo;Current and all-time UFC champions&rdquo; page has regressed again and is once more seating <strong>Tom Aspinall</strong> at heavyweight with a 21 June 2025 title date &mdash; an entry that predates his vacating the belt on 14 September 2026. That row is not carried. ESPN's remaining rows agree with the board above. Pereira, Chimaev, Shevchenko, Topuria, Pantoja and Aspinall appear in no champion cell on this page.</p>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
<a href="https://www.covers.com/ufc/331-odds-saturday-sept-19-2026">Covers &mdash; UFC 331 odds (Kalshi probabilities), updated 16 Sep 9:51 a.m. ET</a> &middot;
<a href="https://sports.yahoo.com/mma/article/ufc-331-full-fight-card-start-time-odds-where-to-watch-and-everything-to-know-for-van-vs-pantoja-2-200052945.html">Yahoo Sports &mdash; UFC 331 full card, times and American lines</a> &middot;
<a href="https://www.ufc.com/event/ufc-332">UFC.com &mdash; UFC 332: Silva vs Wang</a> &middot;
<a href="https://www.cbssports.com/ufc/news/ufc-332-fight-card-natalia-silva-wang-cong-women-flyweight-title/">CBS Sports &mdash; UFC 332 vacant-title main event</a> &middot;
<a href="https://en.wikipedia.org/wiki/UFC_332">Wikipedia &mdash; UFC 332</a> &middot;
<a href="https://www.ufc.com/news/noche-ufc-results-silva-vs-delgado">UFC.com &mdash; Noche UFC main card results</a> &middot;
<a href="https://www.ufc.com/news/bonus-coverage-noche-ufc-glendale-2026">UFC.com &mdash; Noche UFC bonus coverage</a> &middot;
<a href="https://sports.yahoo.com/articles/noche-ufc-results-bonus-winners-010055125.html">Yahoo Sports &mdash; Noche UFC results and bonus winners</a> &middot;
<a href="https://www.forbes.com/sites/brianmazique/2026/09/12/noche-ufc-results-bonus-winners-highlights-and-reactions/">Forbes &mdash; Noche UFC bonuses</a> &middot;
<a href="https://www.cbssports.com/ufc/news/tom-aspinall-ufc-heavyweight-championship-vacate/">CBS Sports &mdash; Aspinall vacates the heavyweight title</a> &middot;
<a href="https://www.mmaweekly.com/news/tom-aspinall-vacates-ufc-heavyweight-title">MMA Weekly &mdash; Aspinall vacates</a> &middot;
<a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">ESPN &mdash; current and all-time UFC champions (heavyweight row refused, see note)</a> &middot;
<a href="https://www.sportbible.com/ufc/muhammad-mokaev-ufc-dana-white-return-pfl-career-decision-564777-20260916">SportBible &mdash; Mokaev on a UFC return, 16 Sep</a> &middot;
<a href="https://www.mmamania.com/ufc-news/472789/muhammad-mokaev-upset-with-ufc-offer-they-wasted-two-years-of-my-life">MMA Mania &mdash; Mokaev</a>
</div>

<div class="disc">Cards and bouts are subject to change. Odds move constantly and are shown with the book and the time the source stated them; where two presentations existed (win probabilities and American lines) both are given rather than converted. Records, methods and finishing times are taken from the promotion's own pages where available. This is a news summary, not betting advice.</div>
@@CDN@@
"""

BODY = (BODY.replace("@@MAST@@", masthead("The Octagon", "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
            .replace("@@NAV@@", nav("mma"))
            .replace("@@TLDR@@", TLDR)
            .replace("@@CDN@@", CDN))

html = page("The Octagon &mdash; Daily MMA Briefing", CSS, BODY)
io.open(os.path.join(OUT, "mma-briefing.html"), "w", encoding="utf-8").write(html)
print("mma ok", len(html))
