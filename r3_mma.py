# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))
ACC, ACC2 = "#e84545", "#ff8a5c"
EXTRA = """
.cdn{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:11px;
  padding:11px 16px;margin-bottom:16px;display:flex;flex-wrap:wrap;align-items:baseline;gap:12px}
.cdn .lab{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--accent)}
.cdn .ev{font-size:14.5px}
.cdn .clock{font-family:var(--mono);font-size:15px;color:var(--accent2);letter-spacing:.04em}
.dateline{font-family:var(--mono);font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--warn);margin-bottom:7px}
.odds{font-family:var(--mono);font-size:12px;color:var(--muted);margin-top:8px;display:block}
.win{color:var(--up);font-weight:600}
"""
CSS = css(ACC, ACC2, "#100c0c", "#1a1313", "#322020", EXTRA)

SRC = [
 ("Covers - UFC 331 Odds for Sept. 19: Van vs. Pantoja Odds & Fight Card From Los Angeles", "https://www.covers.com/ufc/331-odds-saturday-sept-19-2026"),
 ("Yahoo Sports - UFC 331 full fight card, start time, odds, how to watch and everything to know for Van vs. Pantoja 2", "https://sports.yahoo.com/mma/article/ufc-331-full-fight-card-start-time-odds-where-to-watch-and-everything-to-know-for-van-vs-pantoja-2-200052945.html"),
 ("Forbes - UFC 331 Van Vs. Pantoja 2: Early Full Card Fight Week Betting Odds", "https://www.forbes.com/sites/trentreinsmith/2026/09/15/ufc-331-van-vs-pantoja-2-early-full-card-fight-week-betting-odds/"),
 ("Tapology - UFC 331: Van vs. Pantoja 2", "https://www.tapology.com/fightcenter/events/145652-ufc-331"),
 ("Yahoo Sports - Noche UFC Results, Bonus Winners, Highlights And Reactions", "https://ca.sports.yahoo.com/news/noche-ufc-results-bonus-winners-010055125.html"),
 ("Yahoo Sports - Noche UFC bonuses: Slick Silva sub snags six figures", "https://sports.yahoo.com/articles/noche-ufc-bonuses-slick-silva-013250148.html"),
 ("Forbes - Noche UFC Results, Bonus Winners, Highlights And Reactions", "https://www.forbes.com/sites/brianmazique/2026/09/12/noche-ufc-results-bonus-winners-highlights-and-reactions/"),
 ("UFC.com - Main Card Results | Noche UFC", "https://www.ufc.com/news/noche-ufc-results-silva-vs-delgado"),
 ("UFC.com - Official Scorecards | Noche UFC", "https://www.ufc.com/news/noche-ufc-official-scorecards-silva-vs-delgado"),
 ("LowKick MMA - Noche UFC Bonus Winners Revealed Following Thrilling Finishes", "https://www.lowkickmma.com/noche-ufc-bonus-winners-revealed-following-thrilling-finishes/"),
 ("Wikipedia - UFC 332", "https://en.wikipedia.org/wiki/UFC_332"),
 ("UFC.com - UFC 332: Silva vs Wang", "https://www.ufc.com/event/ufc-332"),
 ("Tapology - Natalia Silva vs. Cong Wang, UFC 332", "https://www.tapology.com/fightcenter/bouts/1176462-ufc-332-natalia-silva-vs-cong-the-joker-wang"),
 ("ESPN - Current and all-time UFC champions", "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
 ("ESPN - 2026 UFC Fightcenter", "https://www.espn.com/mma/fightcenter/_/league/ufc"),
 ("Bloody Elbow - UFC News, Fight Results, Interviews & Throwbacks", "https://bloodyelbow.com/category/ufc-news/"),
 ("Wikipedia - Muhammad Mokaev", "https://en.wikipedia.org/wiki/Muhammad_Mokaev"),
 ("UFC.com - Week 6 Results + Scorecards | Dana White's Contender Series, Season 10", "https://www.ufc.com/news/dana-whites-contender-series-season-10-week-6-results"),
 ("Sports Illustrated - Dana White's Contender Series 2026: Week 6 Live Stream Results & Highlights", "https://www.si.com/fannation/mma/news/dana-white-s-contender-series-2026-week-6-live-stream-results-highlights"),
 ("CBS Sports - Dana White's Contender Series 2026 Week 5 results: Quentin Pasley lands brutal KO to earn UFC contract", "https://www.cbssports.com/ufc/news/dana-whites-contender-series-2026-week-5-results-winners-highlights-contracts/"),
 ("Paramount+ - UFC Schedule 2026: Dates, Start Times For Events", "https://www.paramountplus.com/sneak-peak/ufc-schedule-2026/"),
]

def srcblock():
    return "".join('<div style="margin-bottom:7px">%s &mdash; <a href="%s">%s</a></div>' % (t, u, u) for t, u in SRC)

TLDR = ("It is fight week in Los Angeles: Joshua Van defends the flyweight title against Alexandre Pantoja "
        "on Saturday as a narrow &minus;130 favourite, in a rematch of the bout he won the belt in nine months ago.")

CDN = """<div class="cdn">
<span class="lab">Next Card</span>
<span class="ev"><b>UFC 331: Van vs. Pantoja 2</b> &middot; Saturday 19 September &middot; Crypto.com Arena, Los Angeles</span>
<span class="clock" id="ufccdn">&nbsp;</span>
</div>"""

CDNJS = """<script>(function(){var t=new Date('2026-09-19T21:00:00-04:00');function u(){var el=document.getElementById('ufccdn');if(!el)return;var d=t-new Date();if(d<=0){el.textContent='Fight week \\u2014 live/completed';return;}var dd=Math.floor(d/86400000),hh=Math.floor(d/3600000)%24,mm=Math.floor(d/60000)%60;el.textContent=dd+'d '+hh+'h '+mm+'m';}u();setInterval(u,30000);})();</script>"""

BODY = """@@MAST@@
<div class="tldr"><b>Tale of the Tape</b> <span>@@TLDR@@</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
@@NAV@@

@@CDN@@

<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 9px;font-size:19px">Van defends against the man he took the belt from &mdash; and the line is almost a coin flip</h3>
<p style="margin:0 0 10px">UFC 331 lands Saturday at the <b>Crypto.com Arena</b> in Los Angeles, with <b>Joshua Van</b> putting the flyweight title on the line against <b>Alexandre Pantoja</b>, the champion he beat for it at UFC 323 on 6 December 2025. Covers has Van a <b>&minus;130</b> favourite against Pantoja at <b>+110</b> &mdash; a <b>56%</b> implied probability, which is about as close to even as a title rematch gets.</p>
<p style="margin:0 0 10px">The co-main is the one contenders are watching: <b>Arman Tsarukyan (&minus;290)</b> against <b>Mauricio Ruffy (+235)</b> over five rounds at lightweight, in a division whose belt changed hands in June. <b>Patricio Pitbull</b> also features on the card. The main card starts at <b>9 p.m. ET</b> on Paramount+.</p>
<p style="margin:0" class="note">Michael Chandler has said publicly that he expects a big upset on the card; he does not name the bout in anything fetched this run, so none is attributed to him here.</p>
</div>

<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>
<div class="cards">
<div class="card">
<div class="dateline">Sat 19 Sep &middot; Crypto.com Arena, Los Angeles</div>
<h3>UFC 331: Van vs. Pantoja 2</h3>
<p>Flyweight title rematch headlines, with Tsarukyan vs. Ruffy over five rounds in the co-main and Patricio Pitbull on the card. Main card 9 p.m. ET, Paramount+.</p>
<span class="odds">Odds: Van &minus;130 / Pantoja +110 &middot; Tsarukyan &minus;290 / Ruffy +235 (Covers)</span>
</div>
<div class="card">
<div class="dateline">Sat 3 Oct &middot; Delta Center, Salt Lake City</div>
<h3>UFC 332: Silva vs. Wang</h3>
<p><b>Nat&aacute;lia Silva</b> and <b>Wang Cong</b> contest the <b>vacant</b> women&#39;s flyweight title. The bout was originally to be Shevchenko vs. Silva; Valentina Shevchenko withdrew with a ligament injury to her back and shoulder, and the title was vacated. This is the first numbered-event main card to air on <b>CBS</b>.</p>
<span class="odds">Odds: no source fetched this run states a line for this card.</span>
</div>
<div class="card">
<div class="dateline">Sat 24 Oct</div>
<h3>UFC 333: Volkanovski vs. Evloev</h3>
<p><b>Alexander Volkanovski</b> defends the featherweight title against <b>Movsar Evloev</b>, with a heated trilogy bout between <b>Merab Dvalishvili</b> and <b>Petr Yan</b> for the bantamweight championship in the co-main.</p>
<span class="odds">Odds: no source fetched this run states a line for this card.</span>
</div>
</div>

<h2 class="sec">Last Event &mdash; Noche UFC, 12 September, Desert Diamond Arena, Glendale AZ</h2>
<div class="panel" style="padding:6px 10px">
<table>
<tr><th>Result</th><th>Bout</th><th>Method</th></tr>
<tr><td class="win">Jean Silva</td><td>def. Jose Delgado</td><td>Submission (rear-naked choke), R3 2:57 &mdash; dropped in the first before taking over</td></tr>
<tr><td class="win">Sean King III</td><td>def. Jessie Rosas</td><td>KO, 33 seconds &mdash; by slam, on his UFC debut</td></tr>
<tr><td class="win">Tommy McMillen</td><td>def. Marwan Rahiki</td><td>Unanimous decision (29&ndash;28, 29&ndash;28, 29&ndash;27)</td></tr>
<tr><td class="win">Moreno</td><td>def. Morales</td><td>Split decision (28&ndash;29, 30&ndash;27, 29&ndash;28)</td></tr>
<tr><td class="win">Grasso</td><td>def. Manon Fiorot</td><td>Unanimous decision (29&ndash;28, 29&ndash;28, 29&ndash;28)</td></tr>
<tr><td class="win">Blaydes</td><td>def. Waldo Cortes Acosta</td><td>Unanimous decision (29&ndash;28, 29&ndash;28, 29&ndash;28)</td></tr>
<tr><td class="win">Martinez</td><td>def. Dan Ige</td><td>Unanimous decision (30&ndash;27, 30&ndash;27, 29&ndash;28)</td></tr>
</table>
</div>
<div class="panel" style="margin-top:12px">
<p style="margin:0 0 9px"><b>Bonuses.</b> Four fighters took home an extra <b>$100,000</b>. <b>Performance of the Night</b> went to <b>Jean Silva</b> for the submission and to <b>Sean King III</b> for the 33-second slam knockout on debut. <b>Fight of the Night</b> went to the featherweight prospects <b>Marwan Rahiki</b> and <b>Tommy McMillen</b>, who both banked $100,000 for the war McMillen edged on the cards. Two further finishes that were not bonus winners drew <b>$25,000</b> cheques, which Yahoo&#39;s bonus report attributes to <b>Tommy Gantt</b> and <b>Yousri Belgaroui</b>.</p>
<p style="margin:0" class="note">Two notes on sourcing. First, the first names <b>Marwan</b> Rahiki and <b>Tommy</b> McMillen were dropped from this table in the previous edition because nothing fetched that run stated them; both appear verbatim in the bonus reporting fetched this run, so they are restored. Second, a fighter named Tommy Gantt also appears in this week&#39;s Contender Series coverage below; nothing fetched this run establishes whether that is the same person, so the two are reported separately and not merged.</p>
</div>

<h2 class="sec">Prospect Watch</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t pro">Prospect</span></div>
<h3>Contender Series Week 6 &mdash; four of five winners signed</h3>
<p>Week 6 of <b>Dana White&#39;s Contender Series</b> season 10 ran <b>15 September at the UFC Apex</b>, with ten fighters competing. Four of the five winners earned UFC contracts; one was given a second chance later in the season. Among the signings was <b>Tommy Gantt</b>, a Daniel Cormier protege, who submitted <b>Adam Livingston</b> inside a round.</p>
</div>
<div class="card">
<div class="tags"><span class="t pro">Prospect</span></div>
<h3>Twenty-four contracts through five weeks</h3>
<p>The <b>1 September</b> episode handed out five more contracts, bringing the season to <b>24 UFC contracts through five weeks</b> across <b>18 finishes</b>.</p>
</div>
<div class="card">
<div class="tags"><span class="t pro">Prospect</span></div>
<h3>Quentin Pasley&#39;s Week 5 knockout</h3>
<p><b>Quentin Pasley</b> landed a knockout in Week 5 to earn his UFC contract, per CBS Sports&#39; results write-up for that episode.</p>
</div>
</div>

<h2 class="sec">Around the Sport</h2>
<div class="panel">
<ul class="bul">
<li><b>Mokaev says he was strung along for two years.</b> <b>Muhammad Mokaev</b> told the BBC that UFC executives repeatedly assured him that meeting specific benchmarks would earn him a new contract, and that those promises came to nothing. He was released despite a win over <b>Manel Kape</b> in 2024, and says he is frustrated with how he has been treated since the two sides parted.</li>
<li><b>An Aspinall YouTube update is circulating.</b> Coverage this run notes an update regarding the content of <b>Tom Aspinall</b>&#39;s YouTube channel, following his announcement on 14 September that he had vacated the heavyweight title. Nothing fetched this run states what the update says, so its contents are not characterised here.</li>
<li><b>Steveson gets a main card slot.</b> <b>Gable Steveson</b> has been given his first main card berth, and invoked Mike Tyson vs. Peter McNeeley when asked about his next opponent.</li>
<li><b>The roster keeps shrinking.</b> Bloody Elbow reports the promotion has been on a steady wave of roster removals, clearing room for new signings coming through the Contender Series. Nothing fetched this run names the fighters cut in September, so none is listed.</li>
</ul>
</div>

<h2 class="sec">Rankings &amp; Business</h2>
<div class="panel">
<ul class="bul">
<li><b>Rankings movement.</b> Nothing fetched this run states a specific rankings change, so none is claimed. The most consequential movement on the horizon is at flyweight, where Saturday&#39;s main event decides the belt, and at women&#39;s flyweight, where <b>Nat&aacute;lia Silva</b> and <b>Wang Cong</b> meet for a vacant title on 3 October.</li>
<li><b>Broadcast.</b> UFC 332 will be the <b>first numbered-event main card to air on CBS</b>. UFC 331 airs on Paramount+, main card at 9 p.m. ET.</li>
<li><b>Business figures.</b> No viewership number, gate figure, or TKO Group financial disclosure appears in anything fetched this run, so none is printed. This section carries figures only when a fetched source states them.</li>
</ul>
</div>

<h2 class="sec">Champions Board</h2>
<div class="panel" style="padding:6px 10px">
<table>
<tr><th>Division</th><th>Champion</th><th>Note</th></tr>
<tr><td>Heavyweight</td><td class="mut"><b>VACANT</b></td><td>Tom Aspinall vacated on 14 September over eye complications and a lack of medical clearance; he is not retiring. <b>Ciryl Gane</b> holds the interim title (KO2 Pereira, Freedom 250, 14 June 2026).</td></tr>
<tr><td>Light Heavyweight</td><td class="win">Carlos Ulberg</td><td>KO1 Ji&#345;&iacute; Proch&aacute;zka for the vacant belt, UFC 327, 11 April 2026</td></tr>
<tr><td>Middleweight</td><td class="win">Sean Strickland</td><td>Split decision over Khamzat Chimaev, UFC 328, 9 May 2026; two-time champion</td></tr>
<tr><td>Welterweight</td><td class="win">Islam Makhachev</td><td>UD over Jack Della Maddalena, UFC 322, 15 November 2025; one defence (UD Ian Machado Garry, UFC 330, 15 August 2026)</td></tr>
<tr><td>Lightweight</td><td class="win">Justin Gaethje</td><td>TKO4 Ilia Topuria, Freedom 250, 14 June 2026</td></tr>
<tr><td>Featherweight</td><td class="win">Alexander Volkanovski</td><td>UD over Diego Lopes, UFC 314, 12 April 2025; defends vs. Movsar Evloev at UFC 333 on 24 October</td></tr>
<tr><td>Bantamweight</td><td class="win">Petr Yan</td><td>UD over Merab Dvalishvili, UFC 323, 6 December 2025; trilogy co-main at UFC 333</td></tr>
<tr><td>Flyweight</td><td class="win">Joshua Van</td><td>TKO1 Alexandre Pantoja, UFC 323, 6 December 2025; one defence (TKO5 Tatsuro Taira, UFC 328); defends Saturday</td></tr>
<tr><td>Women&#39;s Flyweight</td><td class="mut"><b>VACANT</b></td><td>Valentina Shevchenko vacated; Silva vs. Wang Cong contest it at UFC 332 on 3 October</td></tr>
<tr><td>Women&#39;s Bantamweight</td><td class="win">Kayla Harrison</td><td>Submission R2 Julianna Pe&ntilde;a, UFC 316, 7 June 2025; no defences</td></tr>
<tr><td>Women&#39;s Strawweight</td><td class="win">Mackenzie Dern</td><td>UD over Virna Jandiroba, UFC 321, 25 October 2025; one defence (UD Gillian Robertson, UFC 330)</td></tr>
</table>
</div>
<p class="note"><b>A source that disagreed with itself, again.</b> The ESPN champions page read this run seats <b>Carlos Ulberg at heavyweight</b> &mdash; a division whose title is vacant &mdash; while simultaneously seating him, correctly, at light heavyweight. That row is refused. Every other belt was re-derived from the most recent title-changing card rather than copied, and ESPN&#39;s read agreed on light heavyweight, middleweight, welterweight, lightweight, featherweight and bantamweight. Eleven belts, two of them vacant.</p>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
@@SRCS@@
</div>
<p class="disc">Compiled automatically from public reporting gathered during this run; nothing was fetched first-hand. Fighter names, methods, scorecards, odds and bonus figures are printed only where a fetched source states them verbatim, and rows are left out rather than filled in from memory. Odds are a single book&#39;s line at a single moment and move constantly. Cards and bouts are subject to change.</p>
"""

BODY = (BODY.replace("@@MAST@@", masthead("The Octagon", "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
            .replace("@@NAV@@", nav("mma"))
            .replace("@@TLDR@@", TLDR)
            .replace("@@CDN@@", CDN)
            .replace("@@SRCS@@", srcblock()))

html = page("The Octagon &mdash; Daily Briefing", CSS, BODY).replace("</body>", CDNJS + "\n</body>")
io.open(os.path.join(OUT, "mma-briefing.html"), "w", encoding="utf-8").write(html)
print("mma ok", len(html))
print("TLDR::" + TLDR)
