# -*- coding: utf-8 -*-
import io, common

TLDR = ("Joshua Van kept the flyweight belt with a unanimous decision over Alexandre Pantoja at UFC 331 "
        "in Los Angeles, a card that drew 19,357 fans and an $8.3 million gate and paid Van and Pantoja "
        "$100,000 apiece for Fight of the Night.")

p = []
p.append(common.head("The Octagon &mdash; Daily Briefing", "mma"))
p.append(common.masthead("The Octagon",
         "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
p.append(common.META)
p.append(common.tldr("Tale of the Tape", TLDR))
p.append(common.nav("mma"))

# Countdown bar
p.append('<div class="cdn"><span class="lab">Next card</span>'
         '<span class="t" id="ufccdn">&nbsp;</span>'
         '<span class="mut" style="font-size:13.5px">UFC Fight Night: Rosas Jr. vs. Barcelos &mdash; '
         'Saturday 26 September, Meta Apex, Enterprise, Nevada</span></div>')

# Top story
p.append(common.sec("Top story"))
p.append('<div class="lead"><h3>Van keeps the belt, and UFC 331 turns out to have been a $8.3 million '
         'night</h3>'
         '<p><b>Joshua Van defeated Alexandre Pantoja by unanimous decision</b> &mdash; scorecards '
         '<b>49&ndash;46, 48&ndash;47 and 50&ndash;45</b> &mdash; to retain the flyweight championship in '
         'the main event of <b>UFC 331</b> on <b>Saturday 19 September</b> at <b>Crypto.com Arena, Los '
         'Angeles</b>. The 50&ndash;45 card resolves a scoring discrepancy this desk had left open in '
         'earlier editions: one judge did give Van every round.</p>'
         '<p><b>The business of it.</b> The card drew an announced attendance of <b>19,357</b> for a live '
         'gate of <b>$8,300,000</b>. <b>Pantoja earned $782,000</b> &mdash; $650,000 to show, $32,000 in '
         'fight-week incentive pay and a $100,000 Fight of the Night bonus. <b>Van earned $642,000</b> '
         '&mdash; $500,000 to show, $42,000 incentive pay and the matching $100,000 bonus. The UFC&rsquo;s '
         'promotional guidelines compliance payout for the event totalled <b>$270,500</b>.</p>'
         '<p>The champion has now made <b>one verified defence</b> of the belt he took from Pantoja at '
         '<b>UFC 323 in December 2025</b>, by technical knockout 26 seconds into round one after Pantoja '
         'injured his arm. A further defence over Tatsuro Taira at UFC 328 is carried from earlier '
         'editions and was not restated in sources read this run.</p></div>')

# Fight week
p.append(common.sec("Fight week &mdash; upcoming cards"))
p.append('<div class="cards">')
p.append('<div class="card"><div class="dv">Sat 26 Sep &middot; Meta Apex, Enterprise, Nevada</div>'
         '<h3>UFC Fight Night: Rosas Jr. vs. Barcelos</h3>'
         '<p>A bantamweight main event between <b>Raul Rosas Jr.</b> and <b>Raoni Barcelos</b>. '
         '<b>Odds: Rosas Jr. &minus;1011 / Barcelos +133</b> (market consensus; no single book is named '
         'in the source) &mdash; a gap that reads as the market siding hard with youth and recent wins '
         'over veteran form. Also on the card: the <b>bantamweight and women&rsquo;s strawweight finals '
         'of The Ultimate Fighter: Team Cormier vs. Team Bisping</b>, and <b>Rinya Nakamura vs. Brady '
         'Hiestand</b> at bantamweight.</p></div>')
p.append('<div class="card"><div class="dv">Sat 3 Oct &middot; Delta Center, Salt Lake City</div>'
         '<h3>UFC 332: Silva vs. Wang</h3>'
         '<p><b>Nat&aacute;lia Silva vs. Wang Cong</b> for the <b>vacant women&rsquo;s flyweight '
         'championship</b>. The belt is vacant because <b>Valentina Shevchenko withdrew with a ligament '
         'injury to her back and shoulder</b> that will sideline her for a year, and was stripped. '
         'This is the <b>first numbered event main card to air on CBS</b>: prelims at <b>4 PM ET on '
         'Paramount+</b>, main card at <b>8 PM ET on CBS</b>.</p></div>')
p.append('<div class="card"><span class="tag new">New</span>'
         '<div class="dv">Sat 10 Oct &middot; Meta Apex, Enterprise, Nevada</div>'
         '<h3>UFC Fight Night: Allen vs. Duncan</h3>'
         '<p>A middleweight headliner between <b>Brendan Allen</b>, the former LFA middleweight champion, '
         'and <b>Christian Leroy Duncan</b>. Also billed as UFC Fight Night 290 and UFC Vegas 122; '
         '<b>12 fights</b> on the card. The venue is newly sourced this run &mdash; earlier editions '
         'carried this card without one.</p></div>')
p.append('<div class="card"><span class="tag new">New</span>'
         '<div class="dv">Sat 17 Oct &middot; Rogers Place, Edmonton, Alberta</div>'
         '<h3>UFC Fight Night: Buckley vs. Malott</h3>'
         '<p>A welterweight main event between <b>Joaquin Buckley</b> and <b>Mike Malott</b>, billed as '
         'UFC Fight Night 291 &mdash; and a home card for Malott. The Edmonton venue is newly sourced '
         'this run.</p></div>')
p.append('<div class="card"><div class="dv">Sat 24 Oct &middot; Etihad Arena, Abu Dhabi</div>'
         '<h3>UFC 333: Volkanovski vs. Evloev</h3>'
         '<p>Two title fights in one night. <b>Alexander Volkanovski</b>, the reigning two-time '
         'featherweight champion, defends against the undefeated <b>Movsar Evloev</b>; in the co-main, '
         '<b>Petr Yan</b>, the reigning two-time bantamweight champion, meets former champion '
         '<b>Merab Dvalishvili</b> in a <b>trilogy bout</b>. It is the promotion&rsquo;s <b>24th visit to '
         'Abu Dhabi</b> and the <b>eleventh numbered event</b> in the city, the first since UFC Fight '
         'Night: Ankalaev vs. Guskov in July 2026.</p></div>')
p.append('<div class="card"><div class="dv">Sat 31 Oct &middot; venue not sourced</div>'
         '<h3>Moicano vs. Nolan</h3>'
         '<p>Carried from earlier editions and not restated in sources read this run. '
         '<b>UFC 334 (Sat 14 Nov) at Madison Square Garden</b> is likewise carried rather than '
         're-verified this run.</p></div>')
p.append('</div>')

# Results
p.append(common.sec("Last event &mdash; UFC 331 results, Sat 19 September"))
p.append('<div class="panel" style="padding:8px 10px"><table><thead><tr><th>Result</th><th>Bout</th>'
         '<th>Method</th></tr></thead><tbody>'
         '<tr><td class="up">Joshua Van</td><td>def. Alexandre Pantoja</td>'
         '<td>Unanimous decision (49&ndash;46, 48&ndash;47, 50&ndash;45) &mdash; flyweight title</td></tr>'
         '<tr><td class="up">Arman Tsarukyan</td><td>def. Mauricio Ruffy</td>'
         '<td>KO by elbow, round 1</td></tr>'
         '<tr><td class="up">Patricio Pitbull</td><td>def. Dooho Choi</td>'
         '<td>TKO (punches), round 1</td></tr>'
         '<tr><td class="up">Sean Sharaf</td><td>def. Gable Steveson</td>'
         '<td>KO (punch), round 1</td></tr>'
         '<tr><td class="up">Casey O&rsquo;Neill</td><td>def. Eduarda Moura</td>'
         '<td>Submission (armbar), round 1</td></tr>'
         '<tr><td class="up">Alonzo Menifield</td><td>def. Iwo Baraniewski</td>'
         '<td>Split decision (29&ndash;28, 28&ndash;29, 29&ndash;28)</td></tr>'
         '</tbody></table></div>')
p.append('<p class="note">All six rows are restated in sources read this run. The Menifield method is '
         '<b>upgraded this run</b> from an inferred result to a sourced <b>split decision with '
         'scorecards</b>, and the Van scorecards close the scoring discrepancy earlier editions carried.</p>')

p.append(common.sec("UFC 331 &mdash; bonuses"))
p.append('<div class="panel"><ul class="bul">'
         '<li><b>Fight of the Night:</b> <b>Joshua Van</b> and <b>Alexandre Pantoja</b>, '
         '<b>$100,000 each</b>.</li>'
         '<li><b>Performance of the Night:</b> <b>Arman Tsarukyan</b> and <b>Casey O&rsquo;Neill</b>, '
         '<b>$100,000 each</b>.</li>'
         '<li><b>Four fighters earned $25,000 finish bonuses.</b></li>'
         '<li><b>Sean Sharaf</b> earned a <b>$100,000 bonus</b> for the 12-second knockout of Gable '
         'Steveson &mdash; <b>$50,000 from the UFC and $50,000 for the &ldquo;Chaos Bonus&rdquo;</b>, as '
         'this run&rsquo;s source renders it. <b>Steveson earned $160,000</b> for the loss. An itemisation '
         'totalling $185,000 for Sharaf, carried from earlier editions, is not restated this run and is '
         'not adopted.</li>'
         '</ul></div>')

# Prospect watch
p.append(common.sec("Prospect watch"))
p.append('<div class="cards">')
p.append('<div class="card"><span class="tag good">Prospect</span>'
         '<h3>Raul Rosas Jr.</h3>'
         '<p>Headlines his own Fight Night on 26 September as a <b>&minus;1011 favourite</b> over Raoni '
         'Barcelos &mdash; a price that puts a former youngest-fighter-on-the-roster curiosity squarely '
         'in main-event company on recent form.</p></div>')
p.append('<div class="card"><span class="tag good">Prospect</span>'
         '<h3>Rinya Nakamura</h3>'
         '<p>The <b>Road to UFC season one bantamweight winner</b> faces <b>Brady Hiestand</b> on the '
         '26 September card.</p></div>')
p.append('<div class="card"><span class="tag good">Prospect</span>'
         '<h3>The Ultimate Fighter finalists</h3>'
         '<p>The <b>bantamweight and women&rsquo;s strawweight finals</b> of <b>The Ultimate Fighter: '
         'Team Cormier vs. Team Bisping</b> are scheduled for 26 September &mdash; two roster spots and '
         'two contracts decided on one night.</p></div>')
p.append('</div>')

# Around the sport
p.append(common.sec("Around the sport"))
p.append('<div class="panel"><ul class="bul">'
         '<li>Yahoo Sports&rsquo; UFC 331 post-event facts report that <b>&ldquo;Chito&rdquo; Vera set a '
         'unique knockdown record</b> on the card.</li>'
         '<li><b>Curtis Blaydes</b> signed a <b>new eight-fight deal</b>, reported in August, against a '
         'run of surprise roster removals &mdash; the promotion has let a number of notable names go '
         'rather than renew.</li>'
         '<li><b>Valentina Shevchenko</b> is out for <b>a year</b> with a ligament injury to her back and '
         'shoulder, which is why the women&rsquo;s flyweight title is vacant and contested on 3 October.</li>'
         '</ul></div>')

# Rankings & business
p.append(common.sec("Rankings &amp; business"))
p.append('<div class="panel"><ul class="bul">'
         '<li><b>Rankings movement.</b> The only belt to change hands recently did so <b>without a '
         'fight</b>: <b>Ciryl Gane</b> was elevated from interim to undisputed heavyweight champion on '
         '<b>19 September</b> after <b>Tom Aspinall vacated</b>. UFC 331 had no heavyweight title bout.</li>'
         '<li><b>Gate and attendance.</b> UFC 331 &mdash; <b>19,357</b> announced attendance, '
         '<b>$8,300,000</b> live gate.</li>'
         '<li><b>Payroll.</b> Disclosed purses include <b>Pantoja $782,000</b> and <b>Van $642,000</b> '
         'in totals, with <b>$270,500</b> in promotional guidelines compliance pay across the card.</li>'
         '<li><b>Broadcast.</b> <b>UFC 332 is the first numbered event main card to air on CBS</b>, with '
         'prelims on Paramount+ &mdash; the clearest signal yet of what the Paramount deal looks like in '
         'practice.</li>'
         '<li><b>International.</b> UFC 333 is the promotion&rsquo;s <b>24th visit to Abu Dhabi</b> and '
         'the <b>eleventh numbered event</b> held there.</li>'
         '</ul></div>')

# Champions board
p.append(common.sec("Champions board"))
p.append('<div class="panel" style="padding:8px 10px"><table><thead><tr><th>Division</th><th>Champion</th>'
         '<th>Note</th></tr></thead><tbody>'
         '<tr><td>Heavyweight</td><td class="accc">Ciryl Gane</td>'
         '<td>Announced <b>19 September 2026</b>, elevated from interim after Tom Aspinall vacated. '
         'ESPN lists 19 Sep as the title date; he did not compete for it, so this page does not render '
         'it as a fight result.</td></tr>'
         '<tr><td>Light heavyweight</td><td class="accc">Carlos Ulberg</td>'
         '<td>Won <b>11 April 2026</b>, KO round 1 over Ji&#345;&iacute; Proch&aacute;zka at UFC 327.</td></tr>'
         '<tr><td>Middleweight</td><td class="accc">Sean Strickland</td>'
         '<td>Won <b>9 May 2026</b>, split decision over Khamzat Chimaev at UFC 328.</td></tr>'
         '<tr><td>Welterweight</td><td class="accc">Islam Makhachev</td>'
         '<td>Won <b>15 November 2025</b>, unanimous decision over Jack Della Maddalena at UFC 322.</td></tr>'
         '<tr><td>Lightweight</td><td class="accc">Justin Gaethje</td>'
         '<td>Won <b>14 June 2026</b>, TKO round 4 over Ilia Topuria at UFC Freedom 250.</td></tr>'
         '<tr><td>Featherweight</td><td class="accc">Alexander Volkanovski</td>'
         '<td>Won <b>12 April 2025</b>, unanimous decision over Diego Lopes at UFC 314. Defends against '
         'Movsar Evloev on 24 October.</td></tr>'
         '<tr><td>Bantamweight</td><td class="accc">Petr Yan</td>'
         '<td>Reigning two-time champion. Faces Merab Dvalishvili in a trilogy bout on 24 October.</td></tr>'
         '<tr><td>Flyweight</td><td class="accc">Joshua Van</td>'
         '<td>Won at <b>UFC 323, December 2025</b> (TKO, 26 seconds into round 1). Defended at UFC 331 '
         'on 19 September 2026.</td></tr>'
         '<tr><td>Women&rsquo;s bantamweight</td><td class="accc">Kayla Harrison</td>'
         '<td>Carried from this desk&rsquo;s standing record; not restated in sources read this run.</td></tr>'
         '<tr><td>Women&rsquo;s flyweight</td><td class="warnc">VACANT</td>'
         '<td>Valentina Shevchenko was stripped after withdrawing with a ligament injury to her back and '
         'shoulder. Nat&aacute;lia Silva vs. Wang Cong contest it at UFC 332 on 3 October.</td></tr>'
         '<tr><td>Women&rsquo;s strawweight</td><td class="accc">Mackenzie Dern</td>'
         '<td>Carried from this desk&rsquo;s standing record; not restated in sources read this run.</td></tr>'
         '</tbody></table></div>')
p.append('<p class="note">Eleven rows, one vacant. Cross-checked this run against ESPN&rsquo;s current '
         'champions listing and the UFC 331 and UFC 333 event pages. Six rows carry a newly sourced '
         'title-win date and method this run; the two labelled as carried are exactly that.</p>')

p.append(common.srcs([
    ("https://www.ufc.com/news/cryptocom-ufc-331-van-vs-pantoja-2-results",
     "UFC.com &mdash; UFC 331: Van vs. Pantoja 2 main card results"),
    ("https://www.cbssports.com/ufc/news/ufc-331-fight-results-joshua-van-alexandre-pantoja-card-live-updates/live/",
     "CBS Sports &mdash; UFC 331 results and highlights"),
    ("https://en.wikipedia.org/wiki/UFC_331", "Wikipedia &mdash; UFC 331"),
    ("https://bleacherreport.com/articles/25501053-ufc-331-prize-money-payouts-revealed-van-pantoja-steveson-sharaf-and-all-fighters",
     "Bleacher Report &mdash; UFC 331 prize money payouts revealed"),
    ("https://moneymma.substack.com/p/ufc-331-fighter-purses-incentive",
     "Money MMA &mdash; UFC 331 fighter purses, incentive pay, attendance &amp; gate"),
    ("https://sports.yahoo.com/articles/ufc-331-payouts-revealed-pantoja-050712716.html",
     "Yahoo Sports &mdash; UFC 331 payouts revealed"),
    ("https://sports.yahoo.com/articles/ufc-331-post-event-facts-201532141.html",
     "Yahoo Sports &mdash; UFC 331 post-event facts"),
    ("https://en.wikipedia.org/wiki/UFC_Fight_Night:_Rosas_Jr._vs._Barcelos",
     "Wikipedia &mdash; UFC Fight Night: Rosas Jr. vs. Barcelos"),
    ("https://www.lowkickmma.com/raul-rosas-jr-vs-raoni-barcelos-odds-heavy-money-lands-on-rosas-for-ufc-fight-night-main-event/",
     "LowKick MMA &mdash; Rosas Jr. vs. Barcelos odds"),
    ("https://en.wikipedia.org/wiki/UFC_332", "Wikipedia &mdash; UFC 332"),
    ("https://www.mmamania.com/upcoming-ufc-events/469821/natalia-silva-vs-wang-cong-title-fight-to-main-event-ufc-332-injured-valentina-shevchenko-stripped-of-flyweight-crown",
     "MMA Mania &mdash; Silva vs. Cong to main event UFC 332 after Shevchenko stripped"),
    ("https://en.wikipedia.org/wiki/UFC_Fight_Night:_Allen_vs._Duncan",
     "Wikipedia &mdash; UFC Fight Night: Allen vs. Duncan"),
    ("https://en.wikipedia.org/wiki/UFC_Fight_Night:_Buckley_vs._Malott",
     "Wikipedia &mdash; UFC Fight Night: Buckley vs. Malott"),
    ("https://en.wikipedia.org/wiki/UFC_333", "Wikipedia &mdash; UFC 333"),
    ("https://www.thenationalnews.com/sport/combat-sports/2026/09/18/ufc-333-countdown-one-night-two-title-fights-and-a-trilogy-to-be-decided-in-abu-dhabi/",
     "The National &mdash; UFC 333 countdown: two title fights and a trilogy in Abu Dhabi"),
    ("https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions",
     "ESPN &mdash; current and all-time UFC champions"),
    ("https://bloodyelbow.com/2026/08/21/ex-ufc-title-challenger-survives-trend-of-surprise-roster-removals-by-signing-new-8-fight-deal/",
     "Bloody Elbow &mdash; new eight-fight deal amid surprise roster removals"),
]))

p.append(common.footer(
    "Cards and bouts are subject to change. Results, methods, scorecards, purses and odds are as stated "
    "by the named sources at the time of reading; betting lines move and the figures here are a snapshot, "
    "not an offer. Rows labelled as carried are drawn from this desk&rsquo;s standing record rather than "
    "from a source read this run."))

# Countdown script
p.append('<script>(function(){var t=new Date("2026-09-26T19:00:00-04:00").getTime();'
         'var el=document.getElementById("ufccdn");if(!el)return;'
         'function tick(){var d=t-Date.now();'
         'if(d<=0){el.textContent="Fight week \\u2014 live/completed";return;}'
         'var dd=Math.floor(d/86400000),hh=Math.floor(d%86400000/3600000),'
         'mm=Math.floor(d%3600000/60000);'
         'el.textContent=dd+"d "+hh+"h "+mm+"m";}'
         'tick();setInterval(tick,30000);})();</script>')
p.append(common.TAIL)

html = "".join(p)
io.open("mma-briefing.html", "w", encoding="utf-8").write(html)
print("mma ok", len(html))
