# -*- coding: utf-8 -*-
import io, os, sys
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))

# weekdays computed, never written by hand
D331 = date(2026, 9, 19); D332 = date(2026, 10, 3); D333 = date(2026, 10, 24)
W331, W332, W333 = (d.strftime('%A') for d in (D331, D332, D333))

EXTRA = """
.cdn{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px 17px;margin-bottom:16px;
  display:flex;flex-wrap:wrap;align-items:baseline;gap:12px}
.cdn .lab{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--accent)}
.cdn .val{font-family:var(--mono);font-size:19px;color:var(--warn)}
.cdn .who{font-size:14px;color:#cfcbc6}
.evd{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--warn);margin-bottom:7px}
.odds{font-family:var(--mono);font-size:11.5px;color:var(--muted);margin-top:9px;display:block}
"""
CSS = css("#e84545", "#ff8a5c", "#100c0c", "#1a1313", "#322020", EXTRA)

TLDR = ("UFC 331 headlines Saturday in Los Angeles with Van&ndash;Pantoja 2 priced close to even at "
        "56/44, and the card's only late change is Brian Ortega's injury withdrawal &mdash; not, as "
        "several aggregators reported this morning, the champion's.")

BODY = """@@MAST@@
<div class="tldr"><b>Tale of the Tape</b> <span>@@TLDR@@</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
@@NAV@@

<div class="cdn">
<span class="lab">Next Card</span>
<span class="val" id="ufccdn">&nbsp;</span>
<span class="who">UFC 331 &middot; Van vs. Pantoja 2 &middot; Crypto.com Arena, Los Angeles &middot; main card 9 p.m. ET on Paramount+</span>
</div>

<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 9px;font-size:20px">No, the flyweight champion has not pulled out of UFC 331</h3>
<p style="margin:0 0 10px">Several aggregator headlines circulating this morning &mdash; carried by Yardbarker and boxingnews.com among others &mdash; report that <strong>Joshua Van withdrew</strong> from Saturday's main event, leaving Alexandre Pantoja without an opponent and UFC 331 with &ldquo;a reshuffled main card.&rdquo; <strong>Nothing primary supports it, and three primary reads contradict it.</strong></p>
<p style="margin:0 0 10px">UFC.com's own announcement page for the card, published <strong>14 September</strong>, lists exactly one change: <strong>Brian Ortega is out with an injury</strong>, and his lightweight bout with <strong>Renato Moicano</strong> has been removed. Moicano instead headlines a Fight Night on <strong>31 October at Meta APEX in Las Vegas</strong> against No. 11-ranked <strong>Tom Nolan</strong>, who arrives on a five-fight win streak. That same UFC.com page still lists the <strong>Flyweight Title Bout, Van vs. Pantoja 2, Sat 19 Sep, 9:00 p.m. EDT</strong>, and UFC.com has published fight-week features on the rematch since. Wikipedia's UFC 331 entry, which documents every withdrawal from this card in detail &mdash; Oliveira's, Harrison&ndash;Nunes's, Blaydes's &mdash; records no Van withdrawal at all.</p>
<p style="margin:0 0 10px">The likeliest explanation is a garbled retelling of the <em>first</em> fight: at UFC 323 in December 2025, it was <strong>Pantoja</strong> who was hurt, losing the belt to a first-round stoppage after an arm injury. The one genuine fight-week loss, reported by Bloody Elbow on 15 September as &ldquo;UFC 331 loses main card matchup,&rdquo; is Ortega&ndash;Moicano.</p>
<p style="margin:0" class="note">Published as a correction rather than as news: the withdrawal claim is recorded here because it is circulating, not because it is established. If UFC.com or the promotion says otherwise before Saturday, the next edition will lead with that.</p>
</div>

<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>
<div class="cards">
<div class="card">
<div class="evd">@@W331@@ 19 September &middot; Crypto.com Arena, Los Angeles</div>
<h3>UFC 331 &mdash; Joshua Van vs. Alexandre Pantoja 2</h3>
<p>The flyweight title rematch, nine months after Van took the belt at UFC 323 when Pantoja was stopped in the first round with an arm injury. Arman Tsarukyan vs. Maur&iacute;cio Ruffy is a rare five-round non-title co-main, widely read as a lightweight title eliminator; Patricio Pitbull faces Dooho Choi on the main card &mdash; spelled that way by Covers, and &ldquo;Doo Ho Choi&rdquo; elsewhere. Early prelims 5 p.m. ET, prelims 7 p.m., main card 9 p.m. ET on Paramount+.</p>
<span class="odds">Odds &mdash; Covers (Kalshi probabilities, updated 16 Sep 9:51 a.m. ET): Van 56% / Pantoja 44% &middot; Tsarukyan 72% / Ruffy 28% &middot; Choi 72% / Pitbull 28%</span>
</div>
<div class="card">
<div class="evd">@@W332@@ 3 October &middot; Delta Center, Salt Lake City</div>
<h3>UFC 332 &mdash; Natalia Silva vs. Wang Cong, for the vacant title</h3>
<p>The women's flyweight belt is on the line after Valentina Shevchenko was forced out having told the UFC she would be unable to compete for at least a year. Silva arrives on a <strong>14-fight win streak</strong>, with wins over former champions Rose Namajunas, Alexa Grasso and Jessica Andrade in her last three. Wang has won four straight in the Octagon, most recently beating Tracy Cortez at UFC 329 in July. It is the <strong>first numbered main card to air on CBS</strong>.</p>
<span class="odds">Odds &mdash; no source fetched this run states a line for this card.</span>
</div>
<div class="card">
<div class="evd">@@W333@@ 24 October &middot; Etihad Arena, Abu Dhabi</div>
<h3>UFC 333 &mdash; Volkanovski vs. Evloev, Yan vs. Dvalishvili 3</h3>
<p>Two title fights: featherweight champion <strong>Alexander Volkanovski</strong> defends against undefeated No. 1 contender <strong>Movsar Evloev</strong>, and bantamweight champion <strong>Petr Yan</strong> meets former champion <strong>Merab Dvalishvili</strong> in a trilogy co-main. Also booked: Alexander Volkov vs. Rizvan Kuniev at heavyweight, plus Arnold Allen, Aaron Pico, Dominick Reyes and Azamat Murzakanov. The promotion's 24th visit to Abu Dhabi.</p>
<span class="odds">Odds &mdash; no source fetched this run states a line for this card.</span>
</div>
</div>

<h2 class="sec">Last Event &mdash; Noche UFC, 12 September, Desert Diamond Arena, Glendale</h2>
<div class="panel" style="padding:4px 0">
<table>
<tr><th>Result</th><th>Bout</th><th>Method</th></tr>
<tr><td class="up">Jean Silva</td><td>def. Jose Miguel Delgado &middot; featherweight, main event</td><td>Submission (rear-naked choke), 2:57 of R3</td></tr>
<tr><td class="up">Brandon Moreno</td><td>def. Joseph Morales &middot; co-main event</td><td>Split decision</td></tr>
<tr><td class="up">Tommy McMillen</td><td>def. Marwan Rahiki &middot; featherweight</td><td>Unanimous decision (29-28, 29-28, 29-27)</td></tr>
<tr><td class="up">Alexa Grasso</td><td>def. Manon Fiorot &middot; flyweight</td><td>Unanimous decision (29-28, 29-28, 29-28)</td></tr>
<tr><td class="up">Curtis Blaydes</td><td>def. Waldo Cortes-Acosta &middot; heavyweight</td><td>Unanimous decision (29-28, 29-28, 29-28)</td></tr>
<tr><td class="up">David Martinez</td><td>def. Dan Ige &middot; bantamweight</td><td>Unanimous decision (30-27, 30-27, 29-28)</td></tr>
<tr><td class="up">Sean King III</td><td>def. Jessie Rosas &middot; prelims, UFC debut</td><td>KO by slam, 0:36 of R1</td></tr>
</table>
</div>
<div class="panel">
<p style="margin:0 0 8px"><strong>Bonuses.</strong> Performance of the Night to <strong>Jean Silva</strong> and to <strong>Sean King III</strong>, who caught Rosas on a takedown attempt 36 seconds into his debut, lifted him and slammed him for an instant knockout, moving to 7-0. Fight of the Night to <strong>Tommy McMillen vs. Marwan Rahiki</strong>, a scrappy fifteen minutes in which Rahiki nearly finished McMillen in the second before McMillen took the third; McMillen is now <strong>12-0</strong> and has asked for a fourth fight this year in Las Vegas.</p>
<p style="margin:0" class="note">No dollar amounts are printed for these bonuses. UFC's own bonus page does not state them, and nothing else fetched this run does either. Silva's win was his second straight, taking him to 7-1 in the Octagon with six finishes; Martinez is 4-0 in the UFC on an eleven-fight winning streak overall.</p>
</div>

<h2 class="sec">Prospect Watch &mdash; Contender Series, Season 10, Week 6</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t pro">Signed</span><span class="t">Welterweight</span></div>
<h3>Mayton Perea (9-3)</h3>
<p>Knocked out Zevan Hunt (7-1) with punches at <strong>0:45 of round one</strong> in the 15 September main event at Meta APEX, and took a contract.</p>
</div>
<div class="card">
<div class="tags"><span class="t pro">Signed</span><span class="t">Lightweight</span></div>
<h3>Akbar Abdullaev (14-0)</h3>
<p>The fastest finish of the night: a <strong>19-second knockout</strong> of Ednilson Santos (14-8-1), and still unbeaten through fourteen.</p>
</div>
<div class="card">
<div class="tags"><span class="t pro">Signed</span><span class="t">Middleweight</span></div>
<h3>Igor Cavalcanti (14-2) &amp; Luis Hernandez (8-0)</h3>
<p>Cavalcanti stopped Oscar Ravello (13-4-1) with elbows and punches at <strong>1:38 of round one</strong>; Hernandez submitted Hugo Guillon (7-2) by rear-naked choke at <strong>1:01 of round two</strong>. Both earned deals, taking the night's total to four.</p>
</div>
<div class="card">
<div class="tags"><span class="t">No contract</span><span class="t">Featherweight</span></div>
<h3>Tyshawn Williams (9-0)</h3>
<p>Beat Antonio Monteiro (18-6-1) by unanimous decision but did not get a deal on the night &mdash; Dana White instead offered him another Contender Series appearance this season.</p>
</div>
</div>

<h2 class="sec">Around the Sport</h2>
<div class="panel">
<ul class="bul">
<li><strong>Ortega out, Moicano rebooked.</strong> Brian Ortega's injury removes the Moicano rematch from UFC 331; Moicano now headlines 31 October at Meta APEX against Tom Nolan, his fourth UFC main event.</li>
<li><strong>Chandler expects an upset.</strong> Michael Chandler is publicly predicting a significant upset on Saturday's card in Los Angeles.</li>
<li><strong>The heavyweight vacuum.</strong> With the undisputed title vacated on 14 September, speculation has turned to whether <strong>Jon Jones</strong> returns &mdash; driven by concern that Tom Aspinall may not be able to fight again rather than by anything Jones has announced.</li>
<li><strong>Grasso is the clubhouse leader.</strong> Her win over Manon Fiorot was a second straight and, per UFC's own recap, sets her up as the front-runner for the next women's flyweight championship opportunity &mdash; a belt being contested as vacant at UFC 332.</li>
</ul>
</div>

<h2 class="sec">Rankings &amp; Business</h2>
<div class="cards">
<div class="card">
<h3>Rankings movement</h3>
<p>Curtis Blaydes's decision over Waldo Cortes-Acosta is expected to <strong>reclaim him a place in the heavyweight top five</strong>. Movsar Evloev remains the undefeated No. 1 featherweight contender ahead of UFC 333, and Merab Dvalishvili the No. 1 bantamweight contender. Tom Nolan is <strong>No. 11</strong> at lightweight.</p>
</div>
<div class="card">
<h3>Business &amp; broadcast</h3>
<p>Paramount holds UFC rights under a <strong>seven-year, $7.7 billion</strong> agreement with TKO Group &mdash; an average of about <strong>$1.1 billion a year</strong> &mdash; replacing the pay-per-view model. <strong>UFC Freedom 250</strong> averaged <strong>8.2 million viewers</strong> across the US and Latin America on Paramount+, reached a record <strong>17 million</strong> total on the platform in those markets, and an estimated <strong>34 million</strong> total global viewers once Australia, China, India, South Korea, New Zealand and the UK are included. <strong>UFC 324</strong> drew a live average-minute audience of <strong>4.96 million</strong>. UFC 332 on 3 October will be the first numbered main card on CBS.</p>
</div>
</div>

<h2 class="sec">Champions Board</h2>
<div class="panel" style="padding:4px 0">
<table>
<tr><th>Division</th><th>Champion</th><th>Note</th></tr>
<tr><td>Heavyweight</td><td class="down"><strong>VACANT</strong></td><td>Tom Aspinall vacated on 14 September over eye complications; he is not retiring. <strong>Interim: Ciryl Gane</strong> (KO2 Pereira, Freedom 250, 14 Jun 2026).</td></tr>
<tr><td>Light Heavyweight</td><td class="up">Carlos Ulberg</td><td>KO1 Ji&#345;&iacute; Proch&aacute;zka for the vacant belt, UFC 327, 11 Apr 2026.</td></tr>
<tr><td>Middleweight</td><td class="up">Sean Strickland</td><td>Split decision over Khamzat Chimaev, UFC 328, 9 May 2026. Two-time champion.</td></tr>
<tr><td>Welterweight</td><td class="up">Islam Makhachev</td><td>UD over Jack Della Maddalena, UFC 322, 15 Nov 2025. One defence: UD Ian Machado Garry, UFC 330.</td></tr>
<tr><td>Lightweight</td><td class="up">Justin Gaethje</td><td>TKO4 Ilia Topuria, Freedom 250, 14 Jun 2026.</td></tr>
<tr><td>Featherweight</td><td class="up">Alexander Volkanovski</td><td>Defends against Movsar Evloev at UFC 333, 24 Oct 2026.</td></tr>
<tr><td>Bantamweight</td><td class="up">Petr Yan</td><td>UD over Merab Dvalishvili, UFC 323, 6 Dec 2025. Trilogy bout at UFC 333.</td></tr>
<tr><td>Flyweight</td><td class="up">Joshua Van</td><td>Defends against Alexandre Pantoja at UFC 331, 19 Sep 2026. One defence: TKO5 Tatsuro Taira, UFC 328.</td></tr>
<tr><td>Women's Flyweight</td><td class="down"><strong>VACANT</strong></td><td>Valentina Shevchenko vacated; Natalia Silva vs. Wang Cong contest it at UFC 332, 3 Oct 2026.</td></tr>
<tr><td>Women's Bantamweight</td><td class="up">Kayla Harrison</td><td>Sub2 Julianna Pe&ntilde;a, UFC 316, 7 Jun 2025. The Nunes bout planned for UFC 331 is postponed.</td></tr>
<tr><td>Women's Strawweight</td><td class="up">Mackenzie Dern</td><td>One defence: UD Gillian Robertson, UFC 330, 15 Aug 2026.</td></tr>
</table>
</div>
<p class="note"><strong>Source regression logged.</strong> ESPN's current-champions page, read this run, seats <strong>Tom Aspinall at heavyweight on a 21 June 2025 title win</strong> &mdash; an entry that predates his vacating the belt on 14 September. That row is refused. ESPN agreed with this board on light heavyweight (Ulberg), middleweight (Strickland), welterweight (Makhachev), lightweight (Gaethje), featherweight (Volkanovski), bantamweight (Yan), flyweight (Van) and women's strawweight (Dern). Every belt is re-derived from the most recent title-changing event rather than copied from any single list.</p>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
<a href="https://www.ufc.com/news/updates-cryptocom-ufc-331-van-vs-pantoja-2">UFC.com &mdash; Updates to UFC 331</a> &middot;
<a href="https://www.ufc.com/event/cryptocom-ufc-331">UFC.com &mdash; UFC 331 event page</a> &middot;
<a href="https://www.ufc.com/news/noche-ufc-results-silva-vs-delgado">UFC.com &mdash; Noche UFC main card results</a> &middot;
<a href="https://www.ufc.com/news/bonus-coverage-noche-ufc-glendale-2026">UFC.com &mdash; Noche UFC bonuses</a> &middot;
<a href="https://www.ufc.com/news/dana-whites-contender-series-season-10-week-6-results">UFC.com &mdash; Contender Series, Week 6</a> &middot;
<a href="https://www.ufc.com/news/undisputed-flyweight-title-grabs-ufc-332-salt-lake-city">UFC.com &mdash; UFC 332 title announcement</a> &middot;
<a href="https://www.covers.com/ufc/331-odds-saturday-sept-19-2026">Covers &mdash; UFC 331 odds</a> &middot;
<a href="https://en.wikipedia.org/wiki/UFC_331">Wikipedia &mdash; UFC 331</a> &middot;
<a href="https://en.wikipedia.org/wiki/UFC_333">Wikipedia &mdash; UFC 333</a> &middot;
<a href="https://bloodyelbow.com/2026/09/15/ufc-331-loses-main-card-matchup-on-fight-week-as-star-releases-statement-this-one-hurts/">Bloody Elbow &mdash; UFC 331 loses a main-card matchup</a> &middot;
<a href="https://www.cbssports.com/ufc/news/ufc-332-fight-card-natalia-silva-wang-cong-women-flyweight-title/">CBS Sports &mdash; UFC 332</a> &middot;
<a href="https://combatpress.com/2026/09/contender-series-season-10-week-6-results-four-contracts-awarded/">Combat Press &mdash; Contender Series Week 6</a> &middot;
<a href="https://investor.tkogrp.com/news/news-details/2026/UFC-Freedom-250-Delivers-34-Million-Total-Global-Viewers/default.aspx">TKO Group &mdash; Freedom 250 viewership</a> &middot;
<a href="https://variety.com/2026/tv/news/ufc-freedom-250-ratings-1236785493/">Variety &mdash; Freedom 250 ratings</a> &middot;
<a href="https://www.espn.com/espn/story/_/id/47738036/ufc-first-paramount+-fight-card-averages-nearly-5m-views">ESPN &mdash; UFC 324 on Paramount+</a> &middot;
<a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">ESPN &mdash; current UFC champions (cross-check)</a>
</div>

<div class="disc">Cards and bouts are subject to change. Records, methods, scorecards and bonus designations are taken from UFC's own event coverage where available; betting figures are quoted with their book and their timestamp, and where no source fetched this run stated a line, the card says so rather than supplying one.</div>

<script>(function(){try{var t=new Date('2026-09-19T21:00:00-04:00');function tick(){var e=document.getElementById('ufccdn');if(!e)return;var d=t-new Date();if(d<=0){e.textContent='Fight week \\u2014 live/completed';return;}var dd=Math.floor(d/86400000),hh=Math.floor(d%86400000/3600000),mm=Math.floor(d%3600000/60000);e.textContent=dd+'d '+hh+'h '+mm+'m';}tick();setInterval(tick,30000);}catch(e){}})();</script>
"""

BODY = (BODY.replace("@@MAST@@", masthead("The Octagon", "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
            .replace("@@NAV@@", nav("mma"))
            .replace("@@TLDR@@", TLDR)
            .replace("@@W331@@", W331).replace("@@W332@@", W332).replace("@@W333@@", W333))

html = page("The Octagon &mdash; Daily MMA Briefing", CSS, BODY)
io.open(os.path.join(OUT, "mma-briefing.html"), "w", encoding="utf-8").write(html)
print("mma ok", len(html), "|", W331, W332, W333)
