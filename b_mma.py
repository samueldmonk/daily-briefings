# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page

OUT = os.path.dirname(os.path.abspath(__file__))
ACC, ACC2 = "#e84545", "#ff8a5c"
EXTRA = """
.cdn{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px 17px;margin-bottom:16px;
  display:flex;flex-wrap:wrap;align-items:baseline;gap:12px}
.cdn .lbl{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--accent)}
.cdn .v{font-family:var(--mono);font-size:19px;color:var(--txt)}
.cdn .w{font-size:13px;color:var(--muted)}
.dtl{font-family:var(--mono);font-size:11px;letter-spacing:.1em;color:var(--warn);text-transform:uppercase;margin-bottom:6px}
"""
CSS = css(ACC, ACC2, "#100c0c", "#1a1313", "#322020", EXTRA)

SRC = [
 ("Sports Illustrated / FanNation MMA - Michael Page Reportedly Removed From UFC Rankings As Release Looms", "https://www.si.com/fannation/mma/news/michael-page-reportedly-removed-from-ufc-rankings-as-release-looms"),
 ("UFC.com - Main Card Results | UFC Paris", "https://www.ufc.com/news/ufc-paris-results-hooker-vs-parnasse"),
 ("UFC.com - Prelim Results | UFC Paris", "https://www.ufc.com/news/ufc-paris-prelim-results-hooker-vs-parnasse"),
 ("UFC.com - Bonus Coverage | UFC Paris", "https://www.ufc.com/news/bonus-coverage-ufc-fight-night-paris-2026"),
 ("Sherdog - UFC Paris bonuses: Axel Sola, Salahdine Parnasse and more take home $100K", "https://www.sherdog.com/news/news/UFC-Paris-bonuses-Axel-Sola-Salahdine-Parnasse-and-more-take-home-36100K-202674"),
 ("MMA Mania - Official UFC Paris post-fight bonus winners", "https://www.mmamania.com/ufc-bonuses-and-awards/469586/official-ufc-paris-post-fight-bonus-winners-results-paramount-parnasse-hooker-sola-keita"),
 ("ESPN - UFC Fight Night: Hooker vs. Parnasse Fight Results", "https://www.espn.com/mma/fightcenter/_/id/600059993/league/ufc"),
 ("UFC.com - Noche UFC: Silva vs Delgado (September 12, 2026)", "https://www.ufc.com/event/ufc-fight-night-september-12-2026"),
 ("MMA Mania - Latest Noche UFC 4 fight card, Paramount+ start time, date and location", "https://www.mmamania.com/ufc-fight-cards/462438/latest-noche-ufc-4-fight-card-paramount-start-time-date-location-silva-delgado"),
 ("Wikipedia - UFC 331", "https://en.wikipedia.org/wiki/UFC_331"),
 ("Tapology - UFC 331: Van vs. Pantoja 2", "https://www.tapology.com/fightcenter/events/145652-ufc-331"),
 ("boxingnews.com - Van Opens As Slight Favorite Over Pantoja At UFC 331", "https://boxingnews.com/news/van-pantoja-ufc-331-odds"),
 ("UFC.com - Undisputed Flyweight Title Up For Grabs At UFC 332 In Salt Lake City", "https://www.ufc.com/news/undisputed-flyweight-title-grabs-ufc-332-salt-lake-city"),
 ("CBS Sports - UFC 332 fight card: Natalia Silva, Wang Cong to battle for vacant women's flyweight title in Utah", "https://www.cbssports.com/ufc/news/ufc-332-fight-card-natalia-silva-wang-cong-women-flyweight-title/"),
 ("MMA Mania - Silva Vs. Cong Main Events UFC 332 After Shevchenko Stripped Of Title", "https://www.mmamania.com/upcoming-ufc-events/469821/natalia-silva-vs-wang-cong-title-fight-to-main-event-ufc-332-injured-valentina-shevchenko-stripped-of-flyweight-crown"),
 ("Yahoo Sports - When Is The Next UFC? Date, Start Times, Full Schedule", "https://sports.yahoo.com/articles/next-ufc-date-start-times-042627053.html"),
 ("Cageside Press - Dana White's Contender Series Season 10, Week 5 Weigh-In Results", "https://cagesidepress.com/2026/09/07/dana-whites-contender-series-season-10-week-5-weigh-in-results/"),
 ("Tapology - Contender Series 2026: Week 5", "https://www.tapology.com/fightcenter/events/142724-contender-series-2026-week-5"),
 ("ESPN - Current and all-time UFC champions", "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
 ("Variety - 'UFC Freedom 250' Ratings: 8.2 Million Average Viewers", "https://variety.com/2026/tv/news/ufc-freedom-250-ratings-1236785493/"),
 ("TKO Group Holdings - UFC Freedom 250 Delivers 34 Million Total Global Viewers", "https://investor.tkogrp.com/news/news-details/2026/UFC-Freedom-250-Delivers-34-Million-Total-Global-Viewers/default.aspx"),
 ("Variety - UFC 324 Draws 4.96 Million Views in Paramount+ Debut", "https://variety.com/2026/tv/news/ufc-324-ratings-paramountplus-1236641402/"),
 ("ESPN - UFC's first Paramount+ fight card averages nearly 5M views", "https://www.espn.com/espn/story/_/id/47738036/ufc-first-paramount+-fight-card-averages-nearly-5m-views"),
]

def srcblock():
    return "".join('<div style="margin-bottom:7px">%s &mdash; <a href="%s">%s</a></div>' % (t, u, u) for t, u in SRC)

CDN = """<div class="cdn">
<span class="lbl">Next Card</span>
<span class="v" id="ufccdn">&nbsp;</span>
<span class="w">Noche UFC: Silva vs. Delgado &middot; Saturday 12 September &middot; Desert Diamond Arena, Glendale, AZ &middot; prelims 2 PM ET</span>
</div>"""

CDNJS = """<script>(function(){var t=new Date('2026-09-12T14:00:00-04:00');function u(){var e=document.getElementById('ufccdn');if(!e)return;var d=t-new Date();if(d<=0){e.textContent='Fight week \\u2014 live/completed';return;}var dd=Math.floor(d/864e5),hh=Math.floor(d%864e5/36e5),mm=Math.floor(d%36e5/6e4);e.textContent=dd+'d '+hh+'h '+mm+'m';}u();setInterval(u,3e4);})();</script>"""

BODY = """@@MAST@@
<div class="tldr"><b>Tale of the Tape</b> <span>Michael Page has been pulled from the UFC rankings less than two days after winning at UFC Paris with a release reportedly looming, while Valentina Shevchenko has been stripped of the women&#39;s flyweight title after telling the promotion she would be unable to compete for at least a year.</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
@@NAV@@

@@CDN@@

<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 8px;font-size:20px">Michael Page wins on Saturday, is off the rankings by Monday, and a release is reportedly looming</h3>
<p style="margin:0 0 10px">UFC middleweight <b>Michael &ldquo;Venom&rdquo; Page</b> beat <b>Nursulton Ruziboev</b> by unanimous decision at <b>UFC Paris on 5 September</b>. He was initially eligible to be ranked following that win. Then, according to longtime MMA journalist <b>John Morgan</b>, the weekly UFC rankings email sent on <b>Monday 7 September</b> told voters that Page had been <b>removed from the rankings</b> and would not be eligible for this week&#39;s selection.</p>
<p style="margin:0">Page had been <b>No. 15 in the UFC&#39;s media rankings</b> and <b>No. 8 in the recently formed Meta rankings</b>, which the promotion adopted this summer. Reporting this run frames the removal as a strong signal that a <b>release from the promotion is imminent</b>. <span class="mut">The release itself is reported as looming rather than announced, and is described that way here; nothing read this run is a promotion statement, and the ranking removal is the only action actually confirmed to have happened.</span></p>
</div>

<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t">Expanded</span><span class="t gold">Next up</span></div>
<div class="dtl">Sat 12 Sep &middot; Desert Diamond Arena, Glendale, AZ</div>
<h3>Noche UFC: Jean Silva vs. Jose Delgado</h3>
<p>A featherweight (145 lb) main event. New this run: the card carries <b>13 bouts, the fullest lineup on the UFC calendar</b>, with <b>Paramount+ prelims at 2 p.m. ET and the main card at 5 p.m. ET</b>. Also on the card: <b>Brandon Moreno vs. Joseph Morales</b>, <b>Manon Fiorot vs. Alexa Grasso</b>, and &mdash; new this run &mdash; <b>Waldo Cortes-Acosta vs. Curtis Blaydes</b>. <br><span class="mut">Odds: <b>Silva &minus;428 / Delgado +324</b> (UFCalendar, across 20 sportsbooks, 81% implied) and <b>&minus;425 / +355</b> (FightOdds.io), both carried from a prior verified reading; no odds for this card returned in searches run this edition.</span></p>
</div>
<div class="card">
<div class="tags"><span class="t">Expanded</span><span class="t hot">Title</span></div>
<div class="dtl">Sat 19 Sep &middot; Crypto.com Arena, Los Angeles</div>
<h3>UFC 331: Joshua Van vs. Alexandre Pantoja 2</h3>
<p>A flyweight championship rematch headlines a <b>13-fight</b> card. New detail this run: the pair first met at <b>UFC 323 in December 2025</b>, where <b>Van won the belt by technical knockout 26 seconds into the first round</b> after Pantoja sustained an arm injury. Co-main: <b>Arman Tsarukyan vs. Mauricio Ruffy</b> at lightweight.<br>Odds: <b>Van &minus;115 / Pantoja &minus;105</b>, with other books giving <b>Van &minus;105 / Pantoja &minus;115</b> &mdash; near a pick&#39;em either way. <b>Tsarukyan opened as a &minus;400 favourite</b> over Ruffy. <span class="mut">An earlier edition carried Tsarukyan at &minus;380; this run&#39;s read gives &minus;400, and the newer read is used.</span></p>
</div>
<div class="card">
<div class="tags"><span class="t">Expanded</span><span class="t hot">Vacant title</span></div>
<div class="dtl">Sat 3 Oct &middot; Delta Center, Salt Lake City</div>
<h3>UFC 332: Natalia Silva vs. Wang Cong</h3>
<p>For the <b>vacant</b> women&#39;s flyweight title, <b>live on CBS and Paramount+</b> &mdash; the <b>first numbered-event main card to air on CBS</b>. New this run: the belt is vacant because <b>Valentina Shevchenko was stripped of it</b> after telling the UFC she would be unable to compete for <b>at least a year</b>. <b>Natalia Silva</b> enters on a <b>14-fight win streak</b>, with wins over former champions <b>Rose Namajunas, Alexa Grasso and Jessica Andrade</b> in her last three outings. <b>Wang Cong</b> has <b>won four straight in the Octagon</b>, most recently beating <b>Tracy Cortez at UFC 329 in July</b>. <span class="mut">No betting line for this card returned in anything read this run, so none is printed.</span></p>
</div>
<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t">Fight Night</span></div>
<div class="dtl">Sat 17 Oct &middot; venue not returned</div>
<h3>Joaquin Buckley vs. Mike Malott</h3>
<p>A Fight Night main event on 17 October, re-confirmed this run. <span class="mut">Venue and start time were not stated in anything read this run and are not invented here. The UFC has published start times for the next two events only; October, November and December cards do not yet have times released.</span></p>
</div>
<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t gold">Year end</span></div>
<div class="dtl">Sat 12 Dec &middot; Las Vegas</div>
<h3>UFC 335 closes the 2026 calendar</h3>
<p>Twelve UFC events remain in 2026, running from <b>Noche UFC in Glendale on 12 September</b> through <b>UFC 335 in Las Vegas on 12 December</b>. <span class="mut">A search return this run again claimed &ldquo;UFC 335 is scheduled for September 8, 2026, at Meta APEX in Las Vegas&rdquo;. That is refused: it contradicts the 12 December date given in this run&#39;s own schedule reads, and tonight&#39;s UFC-run event is Contender Series Week 5, not a numbered card.</span></p>
</div>
</div>

<h2 class="sec">Last Event &mdash; Results</h2>
<div class="panel">
<p style="margin:0 0 12px"><b>UFC Fight Night: Hooker vs. Parnasse</b> &mdash; Saturday 5 September, <b>Accor Arena, Paris, France</b>. Fourteen fights.</p>
<table>
<tr><th>Result</th><th>Bout</th><th>Method</th></tr>
<tr><td class="up">Salahdine Parnasse</td><td>def. Dan Hooker (main event, lightweight)</td><td>KO, Round 1, 2:35</td></tr>
<tr><td class="up">Axel Sola</td><td>def. Fares Ziam (co-main event)</td><td>KO, Round 1 (100 seconds)</td></tr>
<tr><td class="up">Losene Keita</td><td>def. Muhammad Naimov</td><td>KO, Round 1</td></tr>
<tr><td class="up">Mario Pinto</td><td>def. Ryan Spann</td><td>TKO</td></tr>
<tr><td class="up">Michael Page</td><td>def. Nursulton Ruziboev</td><td>Unanimous decision</td></tr>
</table>
<p class="note"><b>Records:</b> Parnasse improved to <b>24-2</b> on debut; Hooker fell to <b>24-15</b>. <b>Performance bonuses:</b> four <b>$100,000 Performance of the Night</b> awards &mdash; <b>Parnasse, Axel Sola, Mario Pinto and Losene Keita</b> &mdash; plus <b>four $25,000 cheques</b> for finishes that did not win a bonus. No Fight of the Night was awarded. Only bouts whose result and method were both stated in sources read this run are listed; the card ran to fourteen fights and the remainder are not reconstructed here.</p>
</div>

<h2 class="sec">Prospect Watch</h2>
<div class="cards">
<div class="card">
<div class="tags"><span class="t">Expanded</span><span class="t pro">Prospect</span></div>
<h3>Contender Series Week 5 is tonight, and the full names are now confirmed</h3>
<p><b>Dana White&#39;s Contender Series, Season 10 Week 5</b>, takes place <b>tonight, Tuesday 8 September, at 7:00 p.m. ET</b> on <b>Paramount+</b>. Five contract fights. Full names, confirmed from the weigh-in results this run &mdash; earlier editions of this briefing had three of these fighters down only by initial:</p>
</div>
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t pro">Card</span></div>
<h3>The five bouts</h3>
<p><b>Quentin Pasley vs. Arlind Berisha</b> (main event) &middot; <b>Reginaldo Geraldo Jr. vs. Isaac Moreno</b> (welterweight) &middot; <b>Martin Kozak vs. Christian Echols</b> (middleweight) &middot; <b>Apollo Gomes vs. Won Il Kwon</b> (bantamweight) &middot; <b>Christian Natividad vs. Colton Loud</b> (flyweight). <span class="mut">The event has not taken place at the time of this edition, so no results or contract offers are reported.</span></p>
</div>
<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t pro">Signed</span></div>
<h3>Adam Darby, welterweight</h3>
<p>27, <b>Cage Warriors welterweight champion</b>, <b>7-1</b>, on a six-fight streak with six of seven wins inside the distance. Beat <b>Patrick Rivera</b> by <b>third-round TKO (doctor&#39;s stoppage)</b> at <b>DWCS 2026 Week 4</b>, <b>1 September</b>, UFC Apex; five contracts were awarded that week. Signed to welterweight. <span class="mut">A loosely worded round-up gave a different opponent and date for this bout; multiple independent listings give Rivera and 1 September, and that version is what is published.</span></p>
</div>
</div>

<h2 class="sec">Around the Sport</h2>
<div class="panel">
<ul class="bul">
<li><b>Valentina Shevchenko has been stripped of the women&#39;s flyweight title.</b> She told the UFC she would be unable to compete for at least a year, and the belt now goes up for grabs at UFC 332 on 3 October. Independent reporting has again confirmed the division is vacant. This is also the first edition of this briefing in which a source read describes her as <i>stripped</i> rather than as having vacated &mdash; the word does not appear in the previous snapshot.</li>
<li><b>Twelve events remain on the 2026 calendar</b>, from Noche UFC on 12 September through UFC 335 on 12 December. Start times have been published for the next two events only.</li>
<li><b>Salahdine Parnasse won a UFC main event on debut and is now 24-2.</b> He is a former two-time KSW featherweight champion and one-time KSW lightweight champion who signed with the UFC in late July 2026, having previously turned the promotion down; he did not come through the Contender Series.</li>
<li><b>Noche UFC&#39;s 13-bout card is the fullest on the calendar</b>, and it has grown again this run with Waldo Cortes-Acosta vs. Curtis Blaydes appearing among its main fights.</li>
</ul>
</div>

<h2 class="sec">Rankings &amp; Business</h2>
<div class="panel">
<h3 style="margin:0 0 8px;font-size:16px">Rankings movement</h3>
<ul class="bul">
<li><b>Michael Page removed from the rankings</b> on 7 September, having been No. 15 in the media rankings and No. 8 in the Meta rankings. See the Top Story.</li>
<li><b>The Meta rankings are new.</b> The UFC adopted the Meta-branded ranking board this summer; it now runs alongside the long-standing media panel, and Page held a materially higher position on the newer board.</li>
</ul>
<h3 style="margin:18px 0 8px;font-size:16px">Business &amp; broadcast</h3>
<ul class="bul">
<li><b>UFC Freedom 250 averaged 8.2 million viewers</b> across the U.S. and Latin America on Paramount+, the streamer&#39;s biggest live exclusive event ever, and <b>reached 17 million total viewers</b> &mdash; unique people who watched for at least a minute. Including international audiences in Australia, China, India, South Korea, New Zealand and the U.K., TKO puts total global reach at <b>34 million</b>.</li>
<li><b>UFC 324 drew a live average-minute audience of 4.96 million</b> for its main card, the largest exclusive live event on Paramount+ at the time.</li>
<li><b>Paramount is in year one of a seven-year, $7.7 billion media-rights deal</b> with the UFC, which is owned by TKO Group. Paramount says the arrangement is putting UFC events in front of an audience <b>as much as 20 times larger</b> than the pay-per-view average of the previous two years.</li>
<li><b>UFC 332 extends that reach to broadcast television</b>, with the first numbered-event main card to air live and free on CBS.</li>
</ul>
</div>

<h2 class="sec">Champions Board</h2>
<div class="panel">
<table>
<tr><th>Division</th><th>Champion</th><th>Note</th></tr>
<tr><td>Heavyweight</td><td>Tom Aspinall</td><td>Undisputed since 21 June 2025. <b>Interim:</b> Ciryl Gane (KO2 Alex Pereira, Freedom 250, 14 June 2026).</td></tr>
<tr><td>Light Heavyweight</td><td>Carlos Ulberg</td><td>Won the vacant belt by first-round KO over Ji&#345;&iacute; Proch&aacute;zka at UFC 327, 11 April 2026. <span class="mut">This run&#39;s champions list seats Ulberg and dates it 11 April 2026 &mdash; agreeing with this board for a second consecutive edition.</span></td></tr>
<tr><td>Middleweight</td><td>Sean Strickland</td><td>Split-decision win over Khamzat Chimaev at UFC 328, 9 May 2026. Two-time champion.</td></tr>
<tr><td>Welterweight</td><td>Islam Makhachev</td><td>UD over Jack Della Maddalena, UFC 322, 15 November 2025. One defence (UD Ian Machado Garry, UFC 330, 15 August 2026).</td></tr>
<tr><td>Lightweight</td><td>Justin Gaethje</td><td>TKO4 over Ilia Topuria at UFC Freedom 250, 14 June 2026.</td></tr>
<tr><td>Featherweight</td><td>Alexander Volkanovski</td><td>UD over Diego Lopes, UFC 314, 12 April 2025; defended by UD over Lopes at UFC 325, 31 January 2026.</td></tr>
<tr><td>Bantamweight</td><td>Petr Yan</td><td>UD over Merab Dvalishvili, UFC 323, 6 December 2025.</td></tr>
<tr><td>Flyweight</td><td>Joshua Van</td><td>TKO1 over Alexandre Pantoja at UFC 323, 6 December 2025 &mdash; 26 seconds in, after an arm injury to Pantoja. Defended by TKO5 over Tatsuro Taira at UFC 328. <span class="mut">This run&#39;s list again credits him with zero defences, which cannot be reconciled with the UFC 328 result; one defence is carried and the conflict is stated.</span> Rematch with Pantoja at UFC 331 on 19 September.</td></tr>
<tr><td>Women&#39;s Flyweight</td><td class="mut">Vacant</td><td><b>Valentina Shevchenko was stripped of the title</b> after telling the UFC she would be out at least a year. Natalia Silva vs. Wang Cong contest the vacant belt at UFC 332 on 3 October. <span class="mut">This run&#39;s champions list still seats Shevchenko and is refused for a ninth consecutive edition &mdash; a list seating her cannot be current for a card that exists because the belt is vacant.</span></td></tr>
<tr><td>Women&#39;s Bantamweight</td><td>Kayla Harrison</td><td>Sub2 over Julianna Pe&ntilde;a, UFC 316, 7 June 2025. Zero defences.</td></tr>
<tr><td>Women&#39;s Strawweight</td><td>Mackenzie Dern</td><td>UD over Virna Jandiroba, UFC 321, 25 October 2025. One defence (UD Gillian Robertson, UFC 330, 15 August 2026). <span class="mut">This run&#39;s list credits zero defences; one defence is carried from a verified standing correction and the conflict is stated.</span></td></tr>
</table>
<p class="note">Ten of the eleven champions on the list read this run matched this board by name; the women&#39;s flyweight entry is refused above, with the reason given. Two defence counts on that same list conflict with verified results and are also flagged in place. Every belt here was cross-checked against the most recent completed event before publication.</p>
</div>

<h2 class="sec">Sources</h2>
<div class="panel srcs">
@@SRCS@@
</div>
<p class="disc">Compiled automatically from public reporting gathered during this run; nothing was fetched first-hand. Records, odds, bonus amounts, viewership and dollar figures are printed only where a source read this run states them; where a figure was carried from a prior verified reading, it is labelled as carried. Cards and bouts are subject to change &mdash; fighters withdraw, bouts are rebooked and start times move, often within days of an event.</p>
@@CDNJS@@
"""

BODY = (BODY.replace("@@MAST@@", masthead("The Octagon", "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
            .replace("@@NAV@@", nav("mma"))
            .replace("@@CDNJS@@", CDNJS)
            .replace("@@CDN@@", CDN)
            .replace("@@SRCS@@", srcblock()))

html = page("The Octagon &mdash; Daily Briefings", CSS, BODY)
io.open(os.path.join(OUT, "mma-briefing.html"), "w", encoding="utf-8").write(html)
print("mma ok", len(html))
