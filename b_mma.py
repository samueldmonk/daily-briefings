# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))
ACC, ACC2 = "#e84545", "#ff8a5c"
EXTRA = """
.cdn{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:10px;
  padding:11px 15px;margin-bottom:16px;display:flex;flex-wrap:wrap;align-items:baseline;gap:12px}
.cdn .lab{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.cdn .val{font-family:var(--mono);font-size:16px;color:var(--txt)}
.cdn .ev{font-size:14px;color:var(--muted)}
.dateline{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--warn);margin-bottom:7px}
"""
CSS = css(ACC, ACC2, "#100c0c", "#1a1313", "#322020", EXTRA)

SRC = [
 ("ESPN — Current and all-time UFC champions", "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
 ("UFC.com — official home of Ultimate Fighting Championship", "https://www.ufc.com/"),
 ("UFC.com — Updates to UFC Fight Night Paris 2026", "https://www.ufc.com/news/updates-ufc-fight-night-paris-2026"),
 ("UFC.com — The 10: spotlighting September's most exciting matchups", "https://www.ufc.com/news/10-spotlighting-septembers-most-exciting-matchups"),
 ("UFC.com — Crypto.com UFC 331", "https://www.ufc.com/event/cryptocom-ufc-331"),
 ("Yahoo Sports — Noche UFC: Jean Silva vs. Jose Delgado odds, what to know", "https://sports.yahoo.com/articles/noche-ufc-jean-silva-vs-125016123.html"),
 ("Yahoo Sports — Jean Silva vs. Jose Delgado Noche UFC betting odds revealed", "https://sports.yahoo.com/articles/jean-silva-vs-jose-delgado-055714314.html"),
 ("MMA Mania — Noche UFC 4 odds: betting line opens for Silva vs. Delgado", "https://www.mmamania.com/ufc-odds/466248/noche-ufc-4-odds-betting-line-opens-jean-silva-vs-jose-delgado-main-event-its-not-close"),
 ("Yahoo Sports — UFC 331 odds revealed: Joshua Van an underdog, Gable Steveson -1500", "https://sports.yahoo.com/articles/ufc-331-odds-revealed-joshua-060205602.html"),
 ("MMA Mania — UFC 331 opening odds: tight race for Van-Pantoja 2", "https://www.mmamania.com/ufc-odds/462743/ufc-331-opening-odds-tight-race-van-pantoja-2-arman-gable-steveson-huge-betting-favorites"),
 ("Tapology — UFC 331: Van vs. Pantoja 2", "https://www.tapology.com/fightcenter/events/145652-ufc-331"),
 ("Athlon Sports — When is the next UFC? Date, start times, full schedule", "https://athlonsports.com/mma/ufc-schedule-2026-dates-start-times-full-fight-cards"),
 ("Yahoo Sports — When is the next UFC? Date, start times, full schedule", "https://sports.yahoo.com/articles/next-ufc-date-start-times-042627053.html"),
 ("CBS Sports — Dana White's Contender Series 2026 Week 4 results: Adam Darby leads five winners to earn contracts", "https://www.cbssports.com/ufc/news/dana-whites-contender-series-2026-week-4-results-winners-contracts-highlights/"),
 ("Cage Warriors — Adam Darby secures UFC contract in DWCS headliner", "https://cagewarriors.com/adam-darby-secures-ufc-contract-in-dwcs-headliner/"),
 ("Tapology — Adam Darby vs. Patrick Rivera, Contender Series 2026", "https://www.tapology.com/fightcenter/bouts/1161411-contender-series-2026-adam-the-plank-darby-vs-patrick-rivera"),
 ("TKO Group Holdings — UFC Freedom 250 delivers 34 million total global viewers", "https://investor.tkogrp.com/news/news-details/2026/UFC-Freedom-250-Delivers-34-Million-Total-Global-Viewers/default.aspx"),
 ("Investing.com — TKO Group stock surges after UFC Freedom 250 viewership report", "https://www.investing.com/news/stock-market-news/tko-group-stock-surges-after-ufc-freedom-250-viewership-report-93CH-4763190"),
 ("Paramount+ — UFC schedule 2026: dates, start times", "https://www.paramountplus.com/sneak-peak/ufc-schedule-2026/"),
]

def srcblock():
    return "".join('<div style="margin-bottom:7px">%s &mdash; <a href="%s">%s</a></div>' % (t, u, u) for t, u in SRC)

CDN_JS = """<script>(function(){var el=document.getElementById('ufccdn');if(!el)return;
var target=new Date('2026-09-12T17:00:00-04:00').getTime();
function tick(){var d=target-Date.now();
if(d<=0){el.textContent='Fight week \\u2014 live/completed';return;}
var days=Math.floor(d/86400000),h=Math.floor(d%86400000/3600000),m=Math.floor(d%3600000/60000);
el.textContent=days+'d '+h+'h '+m+'m';}
tick();setInterval(tick,30000);})();</script>"""

BODY = """
%s
<div class="tldr"><b>Tale of the Tape</b> <span>UFC 332 on 3 October will put its entire main card live and free on CBS for the first time ever, headlined by Nat&aacute;lia Silva against Wang Cong for the vacant women&#39;s flyweight title.</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
%s

<div class="cdn">
<span class="lab">Next Card</span>
<span class="val" id="ufccdn">&nbsp;</span>
<span class="ev">Noche UFC: Silva vs. Delgado &middot; Sat 12 September &middot; Desert Diamond Arena, Glendale, AZ &middot; main card 5 PM ET, Paramount+</span>
</div>

<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 8px;font-size:19px">A numbered-card UFC main event is going out free on network television</h3>
<p style="margin:0 0 10px">Nat&aacute;lia Silva vs. Wang Cong is official as the <b>UFC 332</b> main event, taking place <b>3 October at 8 PM ET on CBS and Paramount+</b>. The line that matters: <b>for the first time ever, the entire UFC 332 main card will be broadcast live and free on CBS.</b></p>
<p style="margin:0 0 10px">The bout itself is for the <b>vacant women&#39;s flyweight title</b> &mdash; the division has no champion, which is the reason this fight exists and the reason the champions board below reads Vacant at 125 pounds. Silva and Wang meet at the <b>Delta Center in Salt Lake City</b>.</p>
<p style="margin:0"><span class="mut">No betting line for the UFC 332 main event appeared in any return read this run, so none is printed for that card below.</span></p>
</div>

<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t">Expanded</span><span class="t gold">Next up</span></div>
<div class="dateline">Sat 12 Sep &middot; Desert Diamond Arena, Glendale, AZ</div>
<h3>Noche UFC: Jean Silva vs. Jose Delgado</h3>
<p>A five-round featherweight main event. Delgado stepped in after Yair Rodr&iacute;guez pulled out with a training-camp injury, and gets the first chance in his UFC career to headline a card. Prelims 1 PM ET, main card 5 PM ET on Paramount+.<br><br>
<b>Odds:</b> Silva <b>&minus;428</b> / Delgado <b>+324</b> (UFCalendar, tracked across 20 sportsbooks, an 81%% implied win probability for Silva); Silva <b>&minus;425</b> / Delgado <b>+355</b> (FightOdds.io); Silva <b>&minus;450</b> / Delgado <b>+350</b> (Caesars opener).<br><br>
<span class="mut">One source read this run renders the venue &ldquo;Diamond Desert Arena&rdquo;; the name verified here and in prior editions is Desert Diamond Arena, and that is what is printed.</span></p>
</div>
<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t hot">Title fight</span></div>
<div class="dateline">Sat 19 Sep &middot; Crypto.com Arena, Los Angeles</div>
<h3>UFC 331: Joshua Van vs. Alexandre Pantoja 2</h3>
<p>A 13-fight card, with a flyweight championship rematch on top &mdash; a return to the UFC 323 title fight that ended in injury.<br><br>
<b>Odds:</b> Van <b>+100</b> / Pantoja <b>&minus;120</b> (DraftKings opener); Van <b>&minus;105</b> / Pantoja <b>&minus;115</b> (BetOnline). Near pick-em at both, with the reigning champion the marginal underdog at one and the marginal favourite at the other.<br><br>
<b>Undercard lines:</b> co-main Arman Tsarukyan <b>&minus;380</b> vs. Mauricio Ruffy <b>+305</b>; Olympic gold medallist Gable Steveson carries the heaviest line on the card at <b>&minus;1500</b> against Sean Sharaf at <b>+600</b>.</p>
</div>
<div class="card">
<div class="tags"><span class="t">Expanded</span><span class="t hot">Vacant title</span></div>
<div class="dateline">Sat 3 Oct &middot; Delta Center, Salt Lake City</div>
<h3>UFC 332: Nat&aacute;lia Silva vs. Wang Cong</h3>
<p>For the vacant women&#39;s flyweight title, 8 PM ET. The entire main card airs live and free on CBS, alongside Paramount+ &mdash; a first for the promotion.<br><br>
<span class="mut">Odds: none returned this run for this card.</span></p>
</div>
<div class="card">
<div class="tags"><span class="t new">New</span></div>
<div class="dateline">Sat 17 Oct &middot; Venue not stated in returns read this run</div>
<h3>UFC Fight Night: Joaquin Buckley vs. Mike Malott</h3>
<p>Buckley and Malott meet on 17 October in a Fight Night main event.<br><br>
<span class="mut">Start times for October, November and December cards have not been released &mdash; the UFC has published times for the next two events only. No odds returned. Fight cards change constantly; nothing is final until fight week.</span></p>
</div>
<div class="card">
<div class="tags"><span class="t new">New</span></div>
<div class="dateline">Late Sep &middot; Date and venue not stated in returns read this run</div>
<h3>Raul Rosas Jr. vs. Raoni Barcelos</h3>
<p>Rosas Jr. headlines a UFC event for the first time, in the final bout of September, facing the Brazilian veteran Barcelos a couple of weeks before turning 22.</p>
</div>
</div>

<h2 class="sec">Last Event &mdash; Results</h2>
<div class="panel">
<p style="margin:0 0 12px"><b>UFC Fight Night, Paris &mdash; Accor Arena, 5 September.</b> No title fight took place, so no belt changed hands at the most recent event.</p>
<table>
<tr><th>Result</th><th>Bout</th><th>Method</th></tr>
<tr><td class="up">Salahdine Parnasse</td><td>def. Dan Hooker (main event, lightweight)</td><td>TKO, round 1, 2:35 &mdash; body kick, then a flurry on the fence</td></tr>
<tr><td class="up">Axel Sola</td><td>def. Fares Ziam</td><td>KO, 100 seconds</td></tr>
<tr><td class="up">Mario Pinto</td><td>def. Ryan Spann</td><td>TKO</td></tr>
</table>
<p class="note">Only bouts with both a sourced winner and a sourced method are tabled; the rest of the card is omitted rather than reconstructed.</p>
<p style="margin:12px 0 0"><b>Performance bonuses.</b> Four <b>$100,000</b> Performance of the Night awards &mdash; <b>Parnasse, Sola, Losene Keita and Pinto</b> &mdash; plus <b>$25,000</b> awards to <b>Delphine Benouaich, Matthieu Duclos, Modestas Bukauskas and Kurtis Campbell</b>. Post-fight, Parnasse called for <b>Max Holloway</b> (&ldquo;My dream fight is Max Holloway&rdquo;); that is a call-out, <b>not a booking</b>. Parnasse&#39;s record after the win is <b>24-2</b>. He did not come through Dana White&#39;s Contender Series &mdash; he signed an exclusive UFC deal this summer as a former two-division KSW champion.</p>
</div>

<h2 class="sec">Prospect Watch</h2>
<p class="note" style="margin:0 0 12px">The section title is this desk&#39;s framing. Each tag below repeats only what a source read this run actually says about the fighter.</p>
<div class="cards">
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t pro">Signed a UFC contract</span></div>
<h3>Adam Darby</h3>
<p>The 27-year-old <b>Cage Warriors welterweight champion</b> earned a UFC contract headlining <b>Dana White&#39;s Contender Series 2026 Week 4</b>, stopping <b>Patrick Rivera</b> in the <b>third round by TKO (doctor&#39;s stoppage)</b> at the UFC Apex in Las Vegas on <b>1 September 2026</b>. He entered on a six-fight winning streak at <b>7-1</b>, six of the seven wins inside the distance, and was signed to the welterweight division. Five contracts were awarded that week.<br><br>
<span class="mut">A loosely worded round-up read this run gives the opponent as &ldquo;Kerry Hatley&rdquo; and the date as 2 September. Multiple independent listings give Patrick Rivera and 1 September; the round-up version is refused and is used nowhere on this page.</span></p>
</div>
<div class="card">
<div class="tags"><span class="t pro">Two stoppage wins each</span></div>
<h3>Tommy McMillen and Marwan Rahiki</h3>
<p>Both have been among the top rookies of 2026, each earning a pair of stoppage wins to begin their UFC journeys. They meet each other on the Noche UFC card on 12 September.</p>
</div>
<div class="card">
<div class="tags"><span class="t">First headliner</span></div>
<h3>Raul Rosas Jr.</h3>
<p>Headlining his first UFC event in the final bout of September against Raoni Barcelos, a couple of weeks before he turns 22.</p>
</div>
</div>

<h2 class="sec">Around the Sport</h2>
<div class="panel">
<ul class="bul">
<li><b>The UFC 332 main card on free network television</b> is the structural story of the month &mdash; the first time the promotion has put an entire main card live and free on CBS.</li>
<li><b>Jose Delgado&#39;s first headline slot came by attrition</b>: Yair Rodr&iacute;guez withdrew injured from the Noche UFC main event during camp, and Delgado stepped in for a five-round fight against a heavy favourite.</li>
<li><b>The flyweight rematch is a rerun of an anticlimax.</b> Van and Pantoja&#39;s first meeting at UFC 323 ended in injury; the sportsbooks have priced the rematch as close to a coin flip.</li>
<li><b>Nothing is final until fight week.</b> Only announced or booked fights are listed above; cards change constantly, and start times for October onward have not been published.</li>
</ul>
</div>

<h2 class="sec">Rankings &amp; Business</h2>
<div class="panel">
<p style="margin:0 0 10px"><b>Rankings movement.</b> Dan Hooker entered the Paris main event ranked <b>#10</b> at lightweight and was stopped in the first round; Alexa Grasso meets <b>#2</b> Manon Fiorot on the Noche UFC card. <span class="mut">No return read this run published a post-Paris rankings update, so no other movement is asserted.</span></p>
<p style="margin:0"><b>Business &amp; broadcast.</b> The most recent audience figure this desk has verified remains <b>UFC Freedom 250</b> from <b>14 June</b> at the White House: <b>34 million total global viewers</b>, having initially reported 17 million on Paramount+ across the U.S. and Latin America before data from Australia, China, India, South Korea, New Zealand and the U.K. doubled it. The U.S. averaged <b>7.0 million viewers</b>, the most-watched UFC event domestically; <b>TKO Group Holdings (NYSE:TKO) shares rose 6.2%%</b> on the report. <span class="mut">No viewership, gate or TKO figure for UFC Paris or for any September card appeared in any return read this run, so none is printed.</span></p>
</div>

<h2 class="sec">Champions Board</h2>
<div class="panel">
<table>
<tr><th>Division</th><th>Champion</th><th>Note</th></tr>
<tr><td>Heavyweight</td><td>Tom Aspinall</td><td class="mut">Corroborated by an ESPN-attributed list read this run.</td></tr>
<tr><td>Light Heavyweight</td><td>Carlos Ulberg</td><td>Won the belt at <b>UFC 327</b> in <b>Miami, April 2026</b>, by first-round KO over Ji&#345;&iacute; Proch&aacute;zka. <b>The ESPN-attributed list read this run seats Alex Pereira here; that is refused</b> &mdash; a list that predates UFC 327 cannot be current.</td></tr>
<tr><td>Middleweight</td><td>Sean Strickland</td><td class="mut">Won the title 9 May 2026 by split decision over Khamzat Chimaev. Corroborated this run.</td></tr>
<tr><td>Welterweight</td><td>Islam Makhachev</td><td class="mut">Won 15 Nov 2025 by unanimous decision over Jack Della Maddalena. Corroborated this run.</td></tr>
<tr><td>Lightweight</td><td>Justin Gaethje</td><td class="mut">Won 14 June 2026, TKO round 4 over Ilia Topuria. Corroborated this run.</td></tr>
<tr><td>Featherweight</td><td>Alexander Volkanovski</td><td class="mut">Won 12 April 2025 by unanimous decision over Diego Lopes; one defence. Corroborated this run.</td></tr>
<tr><td>Bantamweight</td><td>Petr Yan</td><td class="mut">Won 6 Dec 2025 by unanimous decision over Merab Dvalishvili. Corroborated this run.</td></tr>
<tr><td>Flyweight</td><td>Joshua Van</td><td>Won the title at <b>UFC 323</b> in <b>26 seconds</b> after a Pantoja arm injury; <b>17-2</b> overall, <b>10-1</b> in the UFC. Defends against Pantoja on 19 September. <span class="mut">Conflict: the list read this run credits Van with zero defences, which cannot be squared with the TKO5 of Tatsuro Taira at UFC 328 that the same sweep reports. One defence is carried and the conflict printed.</span></td></tr>
<tr><td>Women&#39;s Bantamweight</td><td>Kayla Harrison</td><td class="mut">Won 7 June 2025 by round-two submission over Julianna Pe&ntilde;a. Corroborated this run.</td></tr>
<tr><td>Women&#39;s Flyweight</td><td class="mut">Vacant</td><td><b>The ESPN-attributed list read this run seats Valentina Shevchenko here; that is refused.</b> A list seating a champion at 125 pounds cannot be current for UFC 332, a card that exists precisely because the belt is vacant &mdash; and this run independently confirmed Silva vs. Wang Cong as a fight for the vacant title.</td></tr>
<tr><td>Women&#39;s Strawweight</td><td>Mackenzie Dern</td><td class="mut">Won 25 Oct 2025 by unanimous decision over Virna Jandiroba. Corroborated this run.</td></tr>
</table>
<p class="note">Nine of the eleven champions on the list read this run matched this board by name; two are refused above. The two refusals are recorded above with the reason for each; the board is cross-checked against the most recent completed event before publication, and no title changed hands at UFC Paris on 5 September.</p>
</div>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
%s
</div>
<p class="disc">Compiled automatically from public reporting gathered during this run; nothing was fetched first-hand. Every name, record, method, bonus and betting line above traces to a source listed here or to a standing sourced correction, and anything unconfirmed was omitted rather than guessed. Cards and bouts are subject to change; odds move constantly and are shown with the book that quoted them.</p>
%s
""" % (masthead("The Octagon", "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"), nav("mma"), srcblock(), CDN_JS)

html = page("The Octagon &mdash; Daily Briefings", CSS, BODY)
io.open(os.path.join(OUT, "mma-briefing.html"), "w", encoding="utf-8").write(html)
print("mma ok", len(html))
