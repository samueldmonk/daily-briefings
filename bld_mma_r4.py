# -*- coding: utf-8 -*-
import io, common_r4 as C

OUT = "/sessions/youthful-bold-tesla/mnt/outputs/mma-briefing.html"

TLDR = ("Arman Tsarukyan knocked out Mauricio Ruffy in a lightweight title eliminator at UFC 331, but "
        "champion Justin Gaethje says both his hands are still hurt and he will not fight again until 2027.")

CDN = ('<div class="cdn"><span class="lab">Next card</span>'
 '<span class="t" id="ufccdn">&nbsp;</span>'
 '<span class="mut" style="font-size:13.5px">UFC Fight Night: Rosas Jr. vs. Barcelos &middot; Saturday '
 '26 September, 8:00&nbsp;PM ET &middot; Meta APEX, Enterprise, Nevada</span></div>')

CDN_JS = ("<script>(function(){var tgt=new Date('2026-09-26T20:00:00-04:00');function t(){var el=" 
 "document.getElementById('ufccdn');if(!el)return;var d=tgt-new Date();if(d<=0){el.textContent="
 "'Fight week \\u2014 live/completed';return;}var dd=Math.floor(d/864e5),hh=Math.floor(d%864e5/36e5),"
 "mm=Math.floor(d%36e5/6e4);el.textContent=dd+'d '+hh+'h '+mm+'m';}t();setInterval(t,30000);})();</script>")

TOP = ('<div class="lead"><h3>Tsarukyan made himself impossible to deny &mdash; and then the champion said he '
 'cannot punch until 2027</h3>'
 '<p><b>Arman Tsarukyan</b> knocked out <b>Mauricio Ruffy</b> with an elbow at <b>4:56 of round one</b> at '
 '<b>UFC 331</b> on 19 September, in a bout billed as a lightweight title eliminator. He said afterwards that he had '
 'already spoken to Dana White and expects the title shot next.</p>'
 '<p>The obstacle is the champion&rsquo;s hands. <b>Justin Gaethje</b> has said he will not return to the Octagon '
 'until <b>2027</b>, telling Sports Illustrated: <b>&ldquo;I still can&rsquo;t punch anything. Both of my hands are '
 'still hurt from the fight so I&rsquo;m just going to enjoy being the champion for the rest of the year because I '
 'fought two times already in the first six months.&rdquo;</b> The damage dates to his June title win over Ilia '
 'Topuria.</p>'
 '<p>White would not confirm the shot at the UFC 331 post-fight press conference, saying <b>&ldquo;We&rsquo;ll '
 'see&rdquo;</b> and that <b>&ldquo;we don&rsquo;t know what Gaethje is thinking yet. We&rsquo;ll see where his head '
 'is at.&rdquo;</b> He has separately said Tsarukyan <b>&ldquo;completely flipped&rdquo;</b> the script on the title '
 'shot with the knockout. A <b>Gaethje&ndash;Topuria rematch</b> also remains on the table, with White saying he has '
 'not made up his mind. <b>Joe Rogan</b> has publicly backed Tsarukyan for the shot.</p></div>')

CARDS = [
 ("Sat 26 September &middot; Meta APEX, Enterprise, Nevada",
  "UFC Fight Night: Rosas Jr. vs. Barcelos",
  "Bantamweight main event between <b>Raul Rosas Jr.</b> and <b>Raoni Barcelos</b>, also billed as UFC Fight Night "
  "289 / UFC Vegas 121. Twelve bouts, 8:00&nbsp;PM ET, on Paramount+. The bantamweight and women&rsquo;s strawweight "
  "finals of <i>The Ultimate Fighter: Team Cormier vs. Team Bisping</i> are on the card.",
  "Odds: Rosas Jr. &minus;210 / Barcelos +177 (opening line, MMAOddsBreaker)"),
 ("Sat 3 October &middot; Salt Lake City",
  "UFC 332: Silva vs. Wang",
  "The card will crown an <b>undisputed women&rsquo;s flyweight champion</b> after Valentina Shevchenko informed the "
  "promotion she would be unavailable for at least a year. <b>Natalia Silva</b> meets <b>Wang Cong</b> for the "
  "vacant belt.", None),
 ("Sat 24 October &middot; Etihad Arena, Abu Dhabi",
  "UFC 333: Volkanovski vs. Evloev",
  "Featherweight title: reigning two-time champion <b>Alexander Volkanovski</b> against undefeated contender "
  "<b>Movsar Evloev</b>. Co-main is a <b>bantamweight title trilogy bout</b>, reigning two-time champion "
  "<b>Petr Yan</b> vs. former champion <b>Merab Dvalishvili</b>. Two belts on one card.", None),
 ("Sat 14 November &middot; Madison Square Garden, New York",
  "UFC 334: Gane vs. Hokit",
  "<b>Ciryl Gane&rsquo;s first defence of the undisputed heavyweight title</b>, against <b>Josh Hokit</b>. Co-main: "
  "<b>Kayla Harrison vs. Amanda Nunes</b> for the women&rsquo;s bantamweight title, first booked for UFC 324 in "
  "January and delayed eleven months by Harrison&rsquo;s neck injury. UFC 334 is the promotion&rsquo;s 13th visit to "
  "New York City and its first since UFC 322 in November 2025.", None),
]

RESULTS = [
 ("Joshua Van (c)", "def. Alexandre Pantoja", "Flyweight title", "Unanimous decision (49&ndash;46, 48&ndash;47, 50&ndash;45)"),
 ("Arman Tsarukyan", "def. Mauricio Ruffy", "Lightweight", "KO (elbow), R1 &mdash; 4:56"),
 ("Patricio Pitbull", "def. Dooho Choi", "Main card", "TKO (punches), R1"),
 ("Sean Sharaf", "def. Gable Steveson", "Main card", "KO"),
 ("Alonzo Menifield", "def. Iwo Baraniewski", "Main card", "Method not stated in sources read this run"),
 ("Marlon &ldquo;Chito&rdquo; Vera", "def. Charles Jourdain", "Main card", "TKO (strikes), R3 &mdash; 2:02 <span class=\"mut\">(carried from the standing ledger)</span>"),
]

PROS = [
 ("Callum Connor vs. Piero Guaylupo", "Lightweight",
  "The headline pairing of <b>week 7 of Dana White&rsquo;s Contender Series season 10</b>, at the Meta APEX on "
  "<b>Tuesday 22 September</b>. The two lightweights arrive with <b>19 consecutive wins between them</b>."),
 ("Five more pairs on Tuesday&rsquo;s card", "Contender Series",
  "Another five sets of fighters make the walk in week 7, hoping to join the <b>28 athletes</b> who have already "
  "earned UFC contracts this season."),
 ("Raul Rosas Jr.", "Main event",
  "The 21-year-old headlines Saturday&rsquo;s APEX card against Raoni Barcelos and has drawn heavy betting support. "
  "See the odds refusal below the cards."),
]

AROUND = [
 "<b>Joe Rogan has backed Arman Tsarukyan for the lightweight title shot</b>, adding a prominent voice to the "
 "pressure on the promotion while the champion sits out.",
 "<b>A Yahoo Sports post-event-facts piece headlines a unique knockdown record for Marlon &ldquo;Chito&rdquo; "
 "Vera</b> at UFC 331. The record itself is not stated in anything read this run, so this desk does not describe it.",
 "<b>UFC 331 was the promotion&rsquo;s 790th event</b>, per the running list of UFC events read this run.",
 "<b>The odds refusal, for a fourth consecutive edition.</b> A second price pairing for Rosas Jr. vs. Barcelos keeps "
 "surfacing in which a heavy favourite sits opposite a modest underdog in the same two-way market. The two numbers "
 "cannot both describe that market, so the pairing is refused and its numerals are not reproduced anywhere on this "
 "page. The MMAOddsBreaker opening line is what is published.",
]

BIZ = [
 "<b>Rankings.</b> Tsarukyan&rsquo;s knockout secured the No.&nbsp;1 contender position at lightweight, and "
 "multiple accounts read this run place him as the clear next challenger &mdash; but Dana White has declined to "
 "confirm the booking, and the champion is out until 2027.",
 "<b>Gate and attendance.</b> UFC 331 drew an <b>announced attendance of 19,357</b> for a <b>live gate of "
 "$8,300,000</b>, per the fighter-purse listing read this run. <span class=\"mut\">An earlier edition of this page "
 "carried a gross-total-revenue figure of $8,228,105; that figure was not restated this run and is dropped rather "
 "than carried.</span>",
 "<b>Performance bonuses.</b> <b>Fight of the Night</b>: Joshua Van and Alexandre Pantoja, <b>$100,000 each</b>. "
 "<b>Performance of the Night</b>: <b>Arman Tsarukyan</b>, $100,000, and <b>Casey O&rsquo;Neill</b>, $100,000, for a "
 "first-round submission of Eduarda Moura. One outlet&rsquo;s headline additionally credits <b>Sean Sharaf</b> with "
 "$100,000 for the Steveson knockout.",
]

CHAMPS = [
 ("Heavyweight", "Ciryl Gane", "19 September 2026",
  "Undisputed. Elevated from interim after Tom Aspinall vacated on 14 September; first defence vs. Josh Hokit at UFC 334."),
 ("Light Heavyweight", "Carlos Ulberg", "11 April 2026", "KO1 over Ji&#345;&iacute; Proch&aacute;zka at UFC 327 for the vacant belt."),
 ("Middleweight", "Sean Strickland", "9 May 2026", "Split decision over Khamzat Chimaev at UFC 328; two-time champion."),
 ("Welterweight", "Islam Makhachev", "15 November 2025", "UD over Jack Della Maddalena at UFC 322; two-division champion, 1 defence."),
 ("Lightweight", "Justin Gaethje", "14 June 2026", "TKO4 over Ilia Topuria at UFC Freedom 250. Out until 2027 with hand injuries."),
 ("Featherweight", "Alexander Volkanovski", "12 April 2025", "UD over Diego Lopes at UFC 314; 1 defence. Defends vs. Movsar Evloev at UFC 333."),
 ("Bantamweight", "Petr Yan", "6 December 2025", "UD over Merab Dvalishvili at UFC 323; two-time champion. Trilogy defence vs. Dvalishvili at UFC 333."),
 ("Flyweight", "Joshua Van", "6 December 2025", "TKO1 over Alexandre Pantoja at UFC 323; <b>2 defences</b>, most recently UD over Pantoja at UFC 331 on 19 September."),
 ("Women&rsquo;s Bantamweight", "Kayla Harrison", "7 June 2025", "Defends against Amanda Nunes at UFC 334."),
 ("Women&rsquo;s Flyweight", "VACANT", "&mdash;", "Shevchenko told the promotion she would be unavailable for at least a year; Silva vs. Wang Cong contest the vacant belt at UFC 332 on 3 October."),
 ("Women&rsquo;s Strawweight", "Mackenzie Dern", "25 October 2025", "1 defence."),
]

VERIFY = ('<p class="note">How this board was verified this run. A published current-champions listing read '
 '<b>this run</b> gives <b>Ciryl Gane at heavyweight with a title date of 19 September 2026</b> and independently '
 'matches this board at <b>light heavyweight, middleweight, welterweight, lightweight and featherweight</b> &mdash; '
 'the third consecutive run in which a listing of that kind has corroborated the heavyweight row. Every other belt '
 'was re-derived from the most recent event that could have changed it, and the UFC 331 result, the UFC 332 '
 'vacant-title booking and the UFC 333 and UFC 334 title bookings were each restated in sources read this run. '
 '<b>Alex Pereira is not the light-heavyweight champion, Khamzat Chimaev is not the middleweight champion, '
 'featherweight is not vacant, and Tom Aspinall is no longer the heavyweight champion.</b> Any current-champions '
 'listing that predates UFC 331 will be wrong at flyweight and heavyweight.</p>')

SRC = [
 ("https://www.ufc.com/news/cryptocom-ufc-331-van-vs-pantoja-2-results", "UFC.com &mdash; UFC 331 main card results"),
 ("https://www.cbssports.com/ufc/news/ufc-331-fight-card-joshua-van-alexandre-pantoja-results-winners/",
  "CBS Sports &mdash; UFC 331 card, results and winners"),
 ("https://bloodyelbow.com/2026/09/20/dana-white-answers-arman-tsarukyans-request-to-challenge-justin-gaethje-after-ufc-331/",
  "Bloody Elbow &mdash; Dana White answers Tsarukyan&rsquo;s request"),
 ("https://ca.sports.yahoo.com/news/ufc-champ-justin-gaethje-isnt-fighting-for-the-rest-of-2026-where-does-that-leave-lightweight-191027281.html",
  "Yahoo Sports &mdash; Gaethje is not fighting for the rest of 2026"),
 ("https://www.bjpenn.com/mma-news/ufc/justin-gaethje-remains-sidelined-until-2027-amid-injury-update-both-of-my-hands-are-still-hurt/",
  "BJPenn.com &mdash; Gaethje sidelined until 2027, &ldquo;both of my hands are still hurt&rdquo;"),
 ("https://www.ufc.com/event/ufc-fight-night-september-26-2026", "UFC.com &mdash; UFC Fight Night: Rosas Jr. vs Barcelos"),
 ("https://www.mmaoddsbreaker.com/fight-odds/opening-odds/161297-opening-betting-odds-for-ufc-vegas-121-rosas-jr-vs-barcelos/",
  "MMAOddsBreaker &mdash; opening odds for UFC Vegas 121"),
 ("https://en.wikipedia.org/wiki/UFC_333", "Wikipedia &mdash; UFC 333: Volkanovski vs. Evloev"),
 ("https://www.fightmatrix.com/2026/09/18/four-ufc-fights-that-give-fall-2026-a-real-championship-shape/",
  "Fight Matrix &mdash; four matchups confirmed for fall 2026"),
 ("https://www.ufc.com/news/week-7-preview-dana-whites-contender-series-season-10",
  "UFC.com &mdash; Contender Series season 10, week 7 preview"),
 ("https://moneymma.substack.com/p/ufc-331-fighter-purses-incentive", "MoneyMMA &mdash; UFC 331 purses, attendance and gate"),
 ("https://www.mmamania.com/ufc-331-fight-card-start-time-date-location-van-vs-pantoja-2/473405/official-post-fight-bonus-winners-ufc-331-results-paramount-proper-chaos-van-pantoja-sharaf-o-neill-tsarukyan",
  "MMA Mania &mdash; official UFC 331 post-fight bonus winners"),
 ("https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions", "ESPN &mdash; Current and all-time UFC champions"),
 ("https://en.wikipedia.org/wiki/List_of_UFC_events", "Wikipedia &mdash; List of UFC events"),
]

b = []
b.append(C.head("The Octagon &mdash; Daily MMA Briefing", "mma"))
b.append(C.masthead("The Octagon", "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
b.append(C.META)
b.append(C.tldr("Tale of the Tape", TLDR))
b.append(C.nav("mma"))
b.append(CDN)
b.append(C.sec("Top Story"))
b.append(TOP)
b.append(C.sec("Fight Week &mdash; Upcoming Cards"))
b.append('<div class="cards">')
for when, name, note, odds in CARDS:
    o = ('<p class="mut" style="margin-top:9px;font-size:13.5px">%s</p>' % odds) if odds else ''
    b.append('<div class="card"><div class="mono" style="font-size:11px;letter-spacing:.12em;'
             'text-transform:uppercase;color:#e8c766;margin-bottom:7px">%s</div><h3>%s</h3><p>%s</p>%s</div>'
             % (when, name, note, o))
b.append('</div>')
b.append(C.sec("Last Event &mdash; UFC 331: Van vs. Pantoja 2, Saturday 19 September"))
b.append('<div class="panel"><p class="note" style="margin:0 0 12px">Crypto.com Arena, Los Angeles.</p>'
         '<table><tr><th>Result</th><th>Bout</th><th>Method</th></tr>')
for w, o, div, m in RESULTS:
    b.append('<tr><td class="up">%s</td><td>%s <span class="mut">&middot; %s</span></td><td class="mut">%s</td></tr>'
             % (w, o, div, m))
b.append('</table></div>')
b.append('<div class="panel"><ul class="bul">')
for x in BIZ[2:]:
    b.append('<li>%s</li>' % x)
b.append('</ul></div>')
b.append(C.sec("Prospect Watch"))
b.append('<div class="cards">')
for name, tag, txt in PROS:
    b.append('<div class="card"><span class="tag good">Prospect</span><span class="tag">%s</span><h3>%s</h3>'
             '<p>%s</p></div>' % (tag, name, txt))
b.append('</div>')
b.append(C.sec("Around the Sport"))
b.append('<div class="panel"><ul class="bul">')
for a in AROUND:
    b.append('<li>%s</li>' % a)
b.append('</ul></div>')
b.append(C.sec("Rankings &amp; Business"))
b.append('<div class="panel"><ul class="bul">')
for x in BIZ[:2]:
    b.append('<li>%s</li>' % x)
b.append('</ul></div>')
b.append(C.sec("Champions Board"))
b.append('<div class="panel"><table><tr><th>Division</th><th>Champion</th><th>Won</th><th>Note</th></tr>')
for d, ch, won, note in CHAMPS:
    cls = ' class="warnc"' if ch == "VACANT" else ''
    b.append('<tr><td>%s</td><td%s><b>%s</b></td><td class="mono mut">%s</td><td class="mut">%s</td></tr>'
             % (d, cls, ch, won, note))
b.append('</table>' + VERIFY + '</div>')
b.append(C.srcs(SRC))
b.append(C.footer("Cards and bouts are subject to change. Odds move; the line above is an opening price and is "
                  "named as such. Records, purses, gates and bonus awards appear here only where a source read in "
                  "this run states the figure."))
b.append(CDN_JS)
b.append(C.TAIL)

io.open(OUT, "w", encoding="utf-8").write("".join(b))
print("wrote", OUT)
