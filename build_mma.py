# -*- coding: utf-8 -*-
import io, os
from common import head, masthead, nav, STAMP_JS, FOOT

OUT = os.path.dirname(os.path.abspath(__file__))

PAL = """
:root{
  --bg:#100c0c; --panel:#1a1313; --line:#322020;
  --accent:#e84545; --accent2:#ff8a5c;
  --txt:#efe9e6; --muted:#a2948e;
  --up:#22c55e; --down:#ef4444; --warn:#f0b429; --crit:#ef4444;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
.cdn{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:11px 16px;margin-bottom:16px;
  display:flex;flex-wrap:wrap;align-items:baseline;gap:12px}
.cdn .lab{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--accent)}
.cdn .val{font-family:var(--mono);font-size:17px;color:var(--accent2)}
.cdn .ev{font-size:14px;color:var(--muted)}
.dateline{font-family:var(--mono);font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--warn);margin-bottom:6px}
.topstory{border-left:4px solid var(--accent)}
"""

CARDS = [
    ("Sat 19 September 2026 &middot; Crypto.com Arena, Los Angeles",
     "UFC 331: Van vs. Pantoja 2",
     "Joshua Van defends the flyweight title against the man he took it from nine months ago at UFC 323, when "
     "Pantoja suffered an elbow injury 23 seconds in. Pantoja is bidding to become the third fighter to hold the "
     "flyweight belt twice. Co-main: Arman Tsarukyan vs. Mauricio Ruffy at lightweight, five rounds. Early prelims "
     "5:30 p.m., prelims 7 p.m., main card 9 p.m. ET on Paramount+.",
     "Both presentations are printed and neither is converted into the other. Kalshi win probabilities (Covers): "
     "<b>Van 56% / Pantoja 44%</b>, <b>Tsarukyan 72% / Ruffy 28%</b>, <b>Dooho Choi 72% / Patricio Pitbull 28%</b>, "
     "<b>Gable Steveson 91% / Sean Sharaf 9%</b>. American lines for the main event: <b>Van &minus;130 / "
     "Pantoja +110</b>. For the co-main, two readings circulate &mdash; <b>Tsarukyan &minus;290 / Ruffy +235</b> this "
     "run and <b>&minus;305 / +240</b> earlier from Yahoo Sports; both are printed, neither is averaged."),
    ("Sat 3 October 2026 &middot; Delta Center, Salt Lake City",
     "UFC 332: Silva vs. Wang Cong",
     "Nat&aacute;lia Silva and Wang Cong contest the <b>vacant</b> women&rsquo;s flyweight title. The card is billed as "
     "the first numbered UFC main card on CBS; prelims 4 p.m. ET on Paramount+, main card 8 p.m. ET on CBS.",
     "No source fetched this run states a betting line for this card."),
    ("Sat 24 October 2026 &middot; Abu Dhabi",
     "UFC 333",
     "Alexander Volkanovski and Petr Yan are both booked to defend, per this site&rsquo;s standing corrections "
     "ledger. No further matchmaking was confirmed by any source read this run.",
     "No source fetched this run states a betting line for this card."),
]

RESULTS = [
    ("Jean Silva", "def. Jose Miguel Delgado", "Submission (rear-naked choke), 2:57 of Round 3", "win"),
    ("Brandon Moreno", "def. Joseph Morales", "Split decision", "win"),
    ("Tommy McMillen", "def. Marwan Rahiki", "Unanimous decision (29-28, 29-28, 29-27)", "win"),
    ("Alexa Grasso", "def. Manon Fiorot", "Unanimous decision (29-28, 29-28, 29-28)", "win"),
    ("Curtis Blaydes", "def. Waldo Cortes Acosta", "Unanimous decision (29-28, 29-28, 29-28)", "win"),
    ("David Martinez", "def. Dan Ige", "Unanimous decision (30-27, 30-27, 29-28)", "win"),
]

PROSPECTS = [
    ("Tommy McMillen", "12-0",
     "A first-year featherweight and a Dana White&rsquo;s Contender Series Class of &rsquo;25 graduate. He was "
     "battered and nearly finished in the second round against Marwan Rahiki, survived, and took the third "
     "outright; UFC.com calls him &ldquo;already one of the most entertaining all-action talents on the roster.&rdquo; "
     "He has asked for a fourth fight this year in Las Vegas and promised another bonus."),
    ("Sean King III", "7-0",
     "Caught Jessie Rosas on a takedown attempt 36 seconds into his UFC debut, lifted him and slammed him for an "
     "instant knockout. Performance of the Night on debut."),
    ("David Martinez", "4-0 in the UFC",
     "The Mexican bantamweight swept the cards against Dan Ige to extend his overall winning streak to eleven. "
     "UFC.com&rsquo;s read: nothing flashy, but quick, well-rounded and &ldquo;clearly a step ahead of the veteran "
     "set in the 135-pound ranks.&rdquo;"),
]

AROUND = [
    "<b>The heavyweight belt is vacant.</b> Tom Aspinall vacated the undisputed title on <b>14 September</b> over "
    "eye complications tracing back to the eye pokes in his no-contest with Ciryl Gane at UFC 321. He is not "
    "retiring. <b>Ciryl Gane holds the interim title.</b> Reporting describes an <i>expectation</i> that Gane is "
    "elevated to undisputed &mdash; an expectation, not an announcement, so the board below still reads vacant.",
    "<b>ESPN&rsquo;s champions page is still seating Aspinall at heavyweight</b>, on a 21 June 2025 title win, three "
    "days after he gave the belt up. That is the sixth consecutive run with this regression; the row is refused "
    "again. The same page agreed with every other men&rsquo;s division read this run.",
    "<b>Brian Ortega is off UFC 331.</b> He had been scheduled to face Renato Moicano on Saturday.",
    "<b>Michael Chandler is predicting a major upset</b> at UFC 331, and <b>Gable Steveson</b> &mdash; who gets his "
    "first main-card slot since arriving in the UFC &mdash; invoked Mike Tyson vs. Peter McNeeley when asked about "
    "his opponent.",
    "<b>Muhammad Mokaev</b> is publicly frustrated with how the UFC has treated him since the two sides parted "
    "ways. For the record: he was <b>released in July 2024</b> after beating Manel Kape at UFC 304 despite a 7-0 "
    "promotional record. The current news is his comments on 16 September vowing a return, not a fresh release.",
    "<b>Brandon Moreno snapped a two-fight skid</b> in his first Noche UFC appearance, and <b>Alexa Grasso</b> took "
    "her second straight win &mdash; UFC.com describes her as the clubhouse leader for the next flyweight title shot.",
]

CHAMPS = [
    ("Heavyweight", "<b>VACANT</b>", "Aspinall vacated 14 Sep 2026. <b>Interim: Ciryl Gane</b> (KO2 Pereira, Freedom 250, 14 Jun 2026)"),
    ("Light Heavyweight", "Carlos Ulberg", "KO1 Ji&#345;&iacute; Proch&aacute;zka for the vacant title, UFC 327, 11 Apr 2026"),
    ("Middleweight", "Sean Strickland", "Split decision over Khamzat Chimaev, UFC 328, 9 May 2026 &mdash; two-time champion"),
    ("Welterweight", "Islam Makhachev", "UD Jack Della Maddalena, UFC 322, 15 Nov 2025. 1 defence (UD Ian Machado Garry, UFC 330)"),
    ("Lightweight", "Justin Gaethje", "TKO4 Ilia Topuria, Freedom 250, 14 Jun 2026"),
    ("Featherweight", "Alexander Volkanovski", "UD Diego Lopes, UFC 314, 12 Apr 2025. Defended at UFC 325, 31 Jan 2026"),
    ("Bantamweight", "Petr Yan", "UD Merab Dvalishvili, UFC 323, 6 Dec 2025"),
    ("Flyweight", "Joshua Van", "TKO1 Alexandre Pantoja, UFC 323, 6 Dec 2025. 1 defence (TKO5 Tatsuro Taira, UFC 328). <b>Defends Saturday</b>"),
    ("Women&rsquo;s Flyweight", "<b>VACANT</b>", "Valentina Shevchenko vacated. Nat&aacute;lia Silva vs. Wang Cong contest it at UFC 332, 3 Oct 2026"),
    ("Women&rsquo;s Bantamweight", "Kayla Harrison", "Sub2 Julianna Pe&ntilde;a, UFC 316, 7 Jun 2025. 0 defences"),
    ("Women&rsquo;s Strawweight", "Mackenzie Dern", "UD Virna Jandiroba, UFC 321, 25 Oct 2025. 1 defence (UD Gillian Robertson, UFC 330)"),
]

SOURCES = [
    ("UFC.com &mdash; Main Card Results, Noche UFC: Silva vs Delgado",
     "https://www.ufc.com/news/noche-ufc-results-silva-vs-delgado"),
    ("UFC.com &mdash; Bonus Coverage, Noche UFC",
     "https://www.ufc.com/news/bonus-coverage-noche-ufc-glendale-2026"),
    ("Covers &mdash; UFC 331 odds for Sept. 19: Van vs. Pantoja",
     "https://www.covers.com/ufc/331-odds-saturday-sept-19-2026"),
    ("Yahoo Sports &mdash; UFC 331 full fight card, start time, odds and how to watch",
     "https://sports.yahoo.com/mma/article/ufc-331-full-fight-card-start-time-odds-where-to-watch-and-everything-to-know-for-van-vs-pantoja-2-200052945.html"),
    ("Forbes &mdash; UFC 331: early full-card fight-week betting odds",
     "https://www.forbes.com/sites/trentreinsmith/2026/09/15/ufc-331-van-vs-pantoja-2-early-full-card-fight-week-betting-odds/"),
    ("ESPN &mdash; Current and all-time UFC champions (cross-check; heavyweight row refused)",
     "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
    ("Tapology &mdash; UFC 331: Van vs. Pantoja 2",
     "https://www.tapology.com/fightcenter/events/145652-ufc-331"),
    ("BJPenn.com &mdash; Mauricio Ruffy on his UFC 331 matchup with Arman Tsarukyan",
     "https://www.bjpenn.com/mma-news/ufc/mauricio-ruffy-claims-hes-evolved-into-champion-mentality-ahead-of-arman-tsarukyan-fight-at-ufc-331/"),
    ("Bloody Elbow &mdash; UFC news", "https://bloodyelbow.com/category/ufc-news/"),
]

COUNTDOWN_JS = """<script>(function(){var t=new Date('2026-09-19T21:00:00-04:00');function u(){var e=document.getElementById('ufccdn');if(!e)return;var d=t-new Date();if(d<=0){e.textContent='Fight week \\u2014 live/completed';return;}var dd=Math.floor(d/864e5),hh=Math.floor(d%864e5/36e5),mm=Math.floor(d%36e5/6e4);e.textContent=dd+'d '+hh+'h '+mm+'m';}u();setInterval(u,30000);})();</script>"""


def build():
    o = io.StringIO()
    o.write(head("The Octagon &mdash; Daily MMA Briefing", PAL))
    o.write(masthead("The Octagon",
                     "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
    o.write('<div class="tldr"><b>Tale of the Tape</b> <span>UFC 331 lands Saturday in Los Angeles with Joshua Van '
            'defending the flyweight title against Alexandre Pantoja in a rematch, while the heavyweight belt sits '
            'vacant after Tom Aspinall gave it up on 14 September.</span></div>\n')
    o.write('<div class="freshline" id="freshline">&nbsp;</div>\n')
    o.write(nav("mma"))

    o.write('<div class="cdn"><span class="lab">Next card</span>'
            '<span class="val" id="ufccdn">&nbsp;</span>'
            '<span class="ev">UFC 331: Van vs. Pantoja 2 &middot; Sat 19 Sep, main card 9:00 PM ET &middot; '
            'Crypto.com Arena, Los Angeles</span></div>\n')

    # Top story
    o.write('<h2 class="sec">Top Story</h2>\n')
    o.write('<div class="panel topstory">'
            '<div class="tags"><span class="t gold">Fight week</span><span class="t">Flyweight title</span></div>'
            '<h3 style="margin:0 0 9px;font-size:20px">Joshua Van finally gets to settle it with Alexandre Pantoja</h3>'
            '<p style="margin:0 0 10px">Van took the flyweight belt from Pantoja at UFC 323 in December in the least '
            'satisfying way available: Pantoja suffered an elbow injury <b>23 seconds</b> into the fight and it was '
            'waved off. Nine months on, Van has one defence to his name &mdash; a fifth-round TKO of Tatsuro Taira at '
            'UFC 328 &mdash; and the rematch is the main event of <b>UFC 331 on Saturday 19 September at '
            'Crypto.com Arena in Los Angeles</b>. Pantoja is trying to become the third fighter to hold the flyweight '
            'title twice.</p>'
            '<p style="margin:0 0 10px">The betting market makes it close, which is unusual for a champion&rsquo;s '
            'first real defence of a title won that way: Kalshi has it <b>Van 56% / Pantoja 44%</b>, and the American '
            'line is <b>Van &minus;130 / Pantoja +110</b>. The co-main is a genuine lightweight crossroads &mdash; '
            '<b>Arman Tsarukyan</b>, 10-2 and on five straight since beating Dan Hooker last November, against '
            '<b>Mauricio Ruffy</b>, who has wins over Michael Chandler and Rafael Fiziev and says he has grown into a '
            '&ldquo;champion mentality.&rdquo;</p>'
            '<p style="margin:0" class="mut">One card change to note: <b>Brian Ortega is off the event</b>, having '
            'been scheduled against Renato Moicano.</p>'
            "</div>\n")

    # Upcoming cards
    o.write('<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>\n<div class="cards">')
    for dateline, title, body, odds in CARDS:
        o.write('<div class="card"><div class="dateline">%s</div><h3>%s</h3>'
                '<p>%s</p><p style="margin-top:9px"><b>Odds.</b> %s</p></div>' % (dateline, title, body, odds))
    o.write("</div>\n")
    o.write('<p class="note">The Covers board read this run also carries bouts this site has never listed before, '
            'among them <b>Michael Aswell vs. JooSang Yoo</b> (Kalshi 30% / 70%). Two spelling notes: Covers renders '
            'the featherweight as &ldquo;Dooho Choi&rdquo; where other outlets use &ldquo;Doo Ho Choi&rdquo;, and the '
            'same page gives Tai Tuivasa&rsquo;s opponent as both &ldquo;Robelis Despaigne&rdquo; and &ldquo;Robelois '
            'Despaigne&rdquo; in two tables, at 84% and 85% respectively. Neither is silently picked.</p>\n')

    # Last event
    o.write('<h2 class="sec">Last Event &mdash; Noche UFC, Sat 12 September, Desert Diamond Arena, Glendale AZ</h2>\n'
            '<div class="panel" style="padding:6px 10px"><table>'
            "<tr><th>Result</th><th>Bout</th><th>Method</th></tr>")
    for winner, opp, method, _ in RESULTS:
        o.write('<tr><td class="up"><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (winner, opp, method))
    o.write("</table></div>\n")
    o.write('<div class="panel"><b>Performance bonuses.</b> UFC.com awarded <b>Performance of the Night</b> to '
            '<b>Jean Silva</b> and to <b>Sean King III</b>, whose debut slam knockout is timed by UFC&rsquo;s own '
            'headline at <b>0:36</b>. <b>Fight of the Night</b> went to <b>Tommy McMillen vs. Marwan Rahiki</b>. '
            'UFC&rsquo;s bonus page prints no dollar amounts; Yahoo Sports and Forbes both state <b>$100,000</b> for '
            'the two Performance awards, and that figure is carried with their attribution. <b>No amount is stated '
            'anywhere for Fight of the Night</b>, so none is printed.</div>\n')

    # Prospects
    o.write('<h2 class="sec">Prospect Watch</h2>\n<div class="cards">')
    for name, rec, body in PROSPECTS:
        o.write('<div class="card"><div class="tags"><span class="t pro">Prospect</span>'
                '<span class="t">%s</span></div><h3>%s</h3><p>%s</p></div>' % (rec, name, body))
    o.write("</div>\n")

    # Around the sport
    o.write('<h2 class="sec">Around the Sport</h2>\n<div class="panel"><ul class="bul">')
    for a in AROUND:
        o.write("<li>%s</li>" % a)
    o.write("</ul></div>\n")

    # Rankings & business
    o.write('<h2 class="sec">Rankings &amp; Business</h2>\n<div class="panel">'
            '<p style="margin:0 0 10px"><b>Rankings movement.</b> UFC.com has Alexa Grasso as the clubhouse leader for '
            'the next women&rsquo;s flyweight title shot after beating Manon Fiorot, and expects Curtis Blaydes to '
            're-claim a place in the heavyweight top five after out-pointing Waldo Cortes Acosta &mdash; while warning '
            'that the win &ldquo;left a lot to be desired.&rdquo; Tommy McMillen is 12-0 and David Martinez is 4-0 in '
            'the Octagon on an eleven-fight overall streak.</p>'
            '<p style="margin:0"><b>Business &amp; broadcast.</b> UFC 331 streams on Paramount+ (early prelims '
            '5:30 p.m., prelims 7 p.m., main card 9 p.m. ET). UFC 332 on 3 October is billed as the first numbered '
            'main card on CBS, with prelims on Paramount+ at 4 p.m. and the main card at 8 p.m. ET. '
            '<b>No viewership, gate or TKO Group figure is stated by any source fetched this run</b>, so none is '
            'printed.</p></div>\n')

    # Champions
    o.write('<h2 class="sec">Champions Board</h2>\n<div class="panel" style="padding:6px 10px"><table>'
            "<tr><th>Division</th><th>Champion</th><th>Won / defences</th></tr>")
    for div, champ, note in CHAMPS:
        o.write("<tr><td><b>%s</b></td><td>%s</td><td class=\"mut\">%s</td></tr>" % (div, champ, note))
    o.write("</table></div>\n")
    o.write('<p class="note">Eleven belts, two of them vacant. Every row is re-derived from the most recent '
            'title-changing card rather than copied from any standings page. ESPN&rsquo;s champions article is used as '
            'a cross-check only: this run it again seated <b>Tom Aspinall</b> at heavyweight three days after he '
            'vacated, and that row is refused. Alex Pereira, Khamzat Chimaev, Valentina Shevchenko, Ilia Topuria, '
            'Magomed Ankalaev and Alexandre Pantoja do not hold belts and are absent from every champion cell above.</p>\n')

    # Sources
    o.write('<h2 class="sec">Sources</h2>\n<div class="panel srcs">')
    o.write("<br>".join('<a href="%s">%s</a>' % (u, t) for t, u in SOURCES))
    o.write("</div>\n")

    o.write('<p class="disc">The Octagon is compiled from public reporting at the time of publication. Cards and '
            'bouts are subject to change. Betting lines are quoted as stated by the book or market named and are not '
            'a recommendation.</p>\n')

    o.write(FOOT % (STAMP_JS + "\n" + COUNTDOWN_JS))
    return o.getvalue()


if __name__ == "__main__":
    html = build()
    with open(os.path.join(OUT, "mma-briefing.html"), "w") as f:
        f.write(html)
    print("mma ok", len(html))
