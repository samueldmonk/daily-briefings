# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page
from common_1605 import S_MMA, tldr, FRESH, srcblock

OUT = os.path.dirname(os.path.abspath(__file__))
ACC, ACC2 = "#e84545", "#ff8a5c"
EXTRA = """
.cdn{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:10px;
  padding:11px 15px;margin-bottom:16px;display:flex;flex-wrap:wrap;align-items:baseline;gap:11px}
.cdn .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.cdn .v{font-family:var(--mono);font-size:19px;color:var(--txt);letter-spacing:-.5px}
.cdn .w{font-size:13.5px;color:var(--muted)}
.dateline{font-family:var(--mono);font-size:10.5px;letter-spacing:.11em;text-transform:uppercase;color:var(--warn);margin-bottom:6px}
"""
CSS = css(ACC, ACC2, "#100c0c", "#1a1313", "#322020", EXTRA)

SRC = [
 ("UFC - Noche UFC (2026) official event hub", "https://www.ufc.com/noche-ufc-2026"),
 ("UFC - Noche UFC: Silva vs Delgado (event page)", "https://www.ufc.com/event/ufc-fight-night-september-12-2026"),
 ("UFC - A Full Day Of Combat Sports On September 12 Between Noche UFC And Garcia vs Benn",
  "https://www.ufc.com/news/full-day-combat-sports-september-12-between-noche-ufc-and-garcia-vs-benn"),
 ("Yahoo Sports - Noche UFC 4: How to watch, start time, live stream & full fight card",
  "https://sports.yahoo.com/articles/noche-ufc-4-watch-start-034634939.html"),
 ("Yahoo Sports - Noche UFC 4: Jean Silva vs. Jose Delgado Betting Odds",
  "https://sports.yahoo.com/articles/noche-ufc-4-jean-silva-053210529.html"),
 ("Yahoo Sports - Noche UFC preview and predictions: Can Jose Delgado actually upset Jean Silva?",
  "https://ca.sports.yahoo.com/news/noche-ufc-preview-and-predictions-can-jose-delgado-actually-upset-jean-silva-173056798.html"),
 ("CBS Sports - Noche UFC predictions: fight card, odds and expert picks for Arizona",
  "https://www.cbssports.com/ufc/news/noche-ufc-fight-card-predictions-jean-silva-jose-delgado-odds/"),
 ("ESPN - Noche UFC: Silva vs. Delgado live fight coverage",
  "https://www.espn.com/mma/fightcenter/_/id/600060772/league/ufc"),
 ("Wikipedia - UFC Fight Night: Silva vs. Delgado",
  "https://en.wikipedia.org/wiki/UFC_Fight_Night:_Silva_vs._Delgado"),
 ("ESPN - Current and all-time UFC champions",
  "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
 ("UFCalendar - UFC rankings 2026: every division, champions and top 15",
  "https://www.ufcalendar.com/rankings"),
 ("Desert Diamond Arena - Noche UFC", "https://www.desertdiamondarena.com/event/noche-ufc/106/"),
]

CDN = """<div class="cdn">
<span class="k">Next card</span>
<span class="v" id="ufccdn">&nbsp;</span>
<span class="w">Noche UFC: Silva vs Delgado &mdash; Sat 12 Sept, Desert Diamond Arena, Glendale, AZ. Prelims 2 PM ET, main card 5 PM ET, on Paramount+ with no extra pay-per-view charge.</span>
</div>
<script>(function(){var t=new Date('2026-09-12T14:00:00-04:00');function u(){var e=document.getElementById('ufccdn');if(!e)return;var d=t-new Date();if(d<=0){e.textContent='Fight week \\u2014 live/completed';return;}var dd=Math.floor(d/864e5),hh=Math.floor(d%864e5/36e5),mm=Math.floor(d%36e5/6e4);e.textContent=dd+'d '+hh+'h '+mm+'m';}u();setInterval(u,3e4);})();</script>"""

UPCOMING = [
 (['<span class="t new">New</span>', '<span class="t gold">odds</span>', '<span class="t">main event</span>'],
  "Sat 12 September &middot; Desert Diamond Arena, Glendale, AZ",
  "Noche UFC: Jean Silva vs Jose Miguel Delgado",
  "Five rounds at featherweight, on Paramount+. Silva, <b>17-3</b> with twelve knockouts and one UFC defeat, is ranked "
  "sixth; Delgado, <b>12-2</b> and an Arizona native, took the fight on <b>twenty-four days&rsquo; notice</b> after Yair "
  "Rodriguez withdrew, and has never faced a ranked opponent. Also on the card: former flyweight champion "
  "<b>Brandon Moreno</b> vs <b>Joseph Morales</b>, the winner of The Ultimate Fighter season 33, and "
  "<b>Manon Fiorot</b> vs former women&rsquo;s 125-pound champion <b>Alexa Grasso</b>.",
  "Odds: Silva &minus;430 / Delgado +320 (FanDuel)"),
 (['<span class="t hot">title fight</span>'],
  "Sat 19 September &middot; Crypto.com Arena, Los Angeles",
  "UFC 331: Joshua Van vs Alexandre Pantoja",
  "A flyweight title rematch &mdash; champion Van against the former champion he took the belt from. Co-main: "
  "<b>(#2 lightweight) Arman Tsarukyan vs Mauricio Ruffy</b> over five rounds. Also booked: <b>Marlon Vera vs "
  "Charles Jourdain</b> at bantamweight.",
  ""),
 (['<span class="t hot">vacant title</span>'],
  "Sat 3 October &middot; Salt Lake City",
  "UFC 332: Natalia Silva vs Wang Cong for the vacant women&rsquo;s flyweight title",
  "UFC.com bills the <b>(#1) Silva vs (#8) Wang Cong</b> bout as the women&rsquo;s flyweight championship, contested "
  "vacant after Valentina Shevchenko vacated the belt while sidelined by injury. Featured bout: <b>(#9) Deiveson "
  "Figueiredo vs (#11) Payton Talbott</b>.",
  ""),
 (['<span class="t hot">two title fights</span>'],
  "Sat 24 October &middot; Abu Dhabi",
  "UFC 333: Volkanovski and Yan both defend",
  "Featherweight champion <b>Alexander Volkanovski</b> and bantamweight champion <b>Petr Yan</b> are both booked to "
  "defend on the same card.",
  ""),
]


def upcoming():
    out = ['<div class="cards">']
    for tags, dl, h, p, odds in UPCOMING:
        oddline = ('<p style="margin:9px 0 0;font-family:var(--mono);font-size:12px;color:var(--warn)">%s</p>' % odds) if odds else ""
        out.append('<div class="card"><div class="tags">%s</div><div class="dateline">%s</div><h3>%s</h3><p>%s</p>%s</div>'
                   % ("".join(tags), dl, h, p, oddline))
    out.append('</div>')
    return "".join(out)


RESULTS = [
 ("Salahdine Parnasse", "def. Dan Hooker", "TKO, Round 1, 2:25"),
 ("Axel Sola", "def. Far&egrave;s Ziam", "KO, Round 1, 1:40"),
 ("Michael &ldquo;Venom&rdquo; Page", "def. Nursulton Ruziboev", "Unanimous decision, 29-28 &times;3"),
 ("Daniil Donchenko", "def. Punahele Soriano", "Unanimous decision, 30-27, 30-27, 29-28"),
 ("Kurtis Campbell", "def. Trevor Peek", "Submission, rear-naked choke, Round 3, 3:07"),
 ("Losene Keita", "def. Muhammad Naimov", "KO, Round 1, 2:54"),
]


def results():
    out = []
    for w, b, m in RESULTS:
        out.append('<tr><td class="up"><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (w, b, m))
    return "".join(out)


WEIGHIN = [
 ("Jean Silva (145) vs Jose Miguel Delgado (145.5)", "Main event, five rounds"),
 ("Brandon Moreno (125.5) vs Joseph Morales (125.5)", "Co-main event"),
 ("McMillen (145) vs Rahiki (145.5)", "Main card"),
 ("Manon Fiorot (125) vs Alexa Grasso (125)", "Main card"),
 ("Waldo Cortes Acosta (262) vs Curtis Blaydes (260)", "Main card"),
 ("Martinez (135) vs Ige (135.5)", "Main card"),
 ("Elliott vs Chairez", "Prelims &mdash; catchweight, 130"),
 ("Bahamondes (170) vs Salikhov (170.5)", "Prelims"),
 ("Belgaroui (185.5) vs Santos (185)", "Prelims"),
 ("Klose vs Gantt (155.5)", "Prelims"),
 ("Rafa Garcia vs Rongzhu (155)", "Prelims"),
 ("Sean King III vs Jessie Rosas (145.5)", "Prelims"),
 ("JJ Aldrich vs Regina Tarin (125)", "Prelims"),
]

PROSPECTS = [
 (['<span class="t pro">prospect</span>', '<span class="t new">New</span>'],
  "Jose Miguel Delgado &mdash; 12-2, and a main event on 24 days&rsquo; notice",
  "The Phoenix native gets the biggest possible platform in his own state: a five-round featherweight main event against "
  "a top-ten opponent, taken on <b>twenty-four days&rsquo; notice</b> after Yair Rodriguez withdrew. He has never faced "
  "a ranked opponent, which is exactly what makes Saturday a real test of the projection."),
 (['<span class="t pro">prospect</span>'],
  "Joseph Morales &mdash; TUF 33 winner, five straight",
  "The Ultimate Fighter season 33 winner extended his run to five with a first-round submission of veteran Matt Schnell "
  "at flyweight. He draws the hardest possible name next: former champion Brandon Moreno, in the co-main."),
 (['<span class="t pro">prospect</span>'],
  "Quillan Salkilld &mdash; 6-0 in the UFC",
  "The Australian lightweight submitted #8-ranked Mateusz Gamrot by rear-naked choke in the first round of his first "
  "UFC main event at the Meta Apex on 8 August, earning a Performance of the Night bonus &mdash; his <b>third $100,000 "
  "bonus of 2026</b>."),
]


def prospects():
    out = ['<div class="cards">']
    for tags, h, p in PROSPECTS:
        out.append('<div class="card"><div class="tags">%s</div><h3>%s</h3><p>%s</p></div>' % ("".join(tags), h, p))
    out.append('</div>')
    return "".join(out)


CHAMPS = [
 ("Heavyweight", "Tom Aspinall", "Undisputed; inherited the belt 21 June 2025. <b>Interim heavyweight:</b> Ciryl Gane, KO2 of Alex Pereira at UFC Freedom 250, 14 June 2026."),
 ("Light Heavyweight", "Carlos Ulberg", "Won the vacant title, KO1 of Ji&#345;&iacute; Proch&aacute;zka at UFC 327, 11 April 2026. Had ACL surgery afterwards."),
 ("Middleweight", "Sean Strickland", "Split-decision upset of Khamzat Chimaev at UFC 328, 9 May 2026 &mdash; a two-time champion."),
 ("Welterweight", "Islam Makhachev", "UD over Jack Della Maddalena at UFC 322, 15 Nov 2025. One defence: UD over Ian Machado Garry at UFC 330, 15 Aug 2026, a 17th straight Octagon win. <b>#1 in the men&rsquo;s pound-for-pound rankings</b> as of 8 September."),
 ("Lightweight", "Justin Gaethje", "TKO4 of Ilia Topuria at UFC Freedom 250, 14 June 2026."),
 ("Featherweight", "Alexander Volkanovski", "UD over Diego Lopes at UFC 314, 12 April 2025; one defence, UD over Lopes at UFC 325, 31 Jan 2026. Booked to defend at UFC 333."),
 ("Bantamweight", "Petr Yan", "UD over Merab Dvalishvili at UFC 323, 6 Dec 2025. Booked to defend at UFC 333."),
 ("Flyweight", "Joshua Van", "TKO1 of Alexandre Pantoja at UFC 323, 6 Dec 2025; one defence, TKO5 of Tatsuro Taira at UFC 328. Rematches Pantoja at UFC 331."),
 ("Women&rsquo;s Flyweight", '<span style="color:var(--warn)">Vacant</span>', "Valentina Shevchenko vacated the title while sidelined by injury for roughly a year. Natalia Silva vs Wang Cong contest the vacant belt at UFC 332 on 3 October; the UFC says Shevchenko is guaranteed a title shot when cleared."),
 ("Women&rsquo;s Bantamweight", "Kayla Harrison", "Submission (round 2) of Julianna Pe&ntilde;a at UFC 316, 7 June 2025. Zero defences &mdash; the UFC 324 defence against Amanda Nunes was cancelled after Harrison withdrew for neck surgery."),
 ("Women&rsquo;s Strawweight", "Mackenzie Dern", "UD over Virna Jandiroba at UFC 321, 25 Oct 2025. One defence: UD over Gillian Robertson at UFC 330, 15 Aug 2026."),
]


def champs():
    out = []
    for div, name, note in CHAMPS:
        out.append('<tr><td><b>%s</b></td><td>%s</td><td class="mut">%s</td></tr>' % (div, name, note))
    return "".join(out)


BODY = """@@MAST@@
@@TLDR@@
@@FRESH@@
@@NAV@@

@@CDN@@

<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--accent)">
<h3 style="margin:0 0 9px;font-size:19px">Silva is a &minus;430 favourite for Noche UFC, and the man across from him took the fight three and a half weeks ago</h3>
<p style="margin:0 0 11px">The fourth annual Noche UFC lands at Desert Diamond Arena in Glendale on Saturday, on Mexican
Independence Day weekend, and the market has made up its mind about the main event. FanDuel has <b>Jean Silva at
&minus;430</b> and <b>Jose Miguel Delgado at +320</b>; a $20 wager on Silva returns a total payout of $24.65, against
$84 for Delgado.</p>
<p style="margin:0 0 11px">The gap is a function of how this bout came together. Silva was matched with Yair Rodriguez;
after that withdrawal, Delgado &mdash; <b>12-2</b>, from Phoenix, and without a ranked opponent anywhere on his record
&mdash; accepted a five-round main event on <b>twenty-four days&rsquo; notice</b>. Silva is <b>17-3</b> with twelve
knockouts, ranked sixth at featherweight and carrying one UFC defeat: last year&rsquo;s Noche main event in San Antonio,
against Diego Lopes. That makes him the first fighter to headline multiple Noche UFC events, and he does it
back-to-back.</p>
<p style="margin:0">Every fighter on the thirteen-bout card made weight, and this is the UFC&rsquo;s first event at the
venue. The whole card streams on <b>Paramount+</b> in the United States with no additional pay-per-view charge &mdash;
prelims at 2 PM ET, main card at 5 PM ET &mdash; on a day that also carries Garcia vs Benn in boxing.</p>
</div>

<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>
@@UPCOMING@@

<h2 class="sec">Official Weigh-In &mdash; all thirteen bouts, nobody missed</h2>
<div class="panel" style="padding:6px 10px">
<table><thead><tr><th>Bout (weights in pounds)</th><th>Position</th></tr></thead>
<tbody>@@WEIGHIN@@</tbody></table>
</div>
<p class="note">Weights are from the UFC&rsquo;s official weigh-in results page for the event. Name rendering follows
that page, which writes <b>Waldo Cortes Acosta</b> without a hyphen.</p>

<h2 class="sec">Last Event &mdash; UFC Paris, Sat 5 September, Accor Arena</h2>
<div class="panel" style="padding:6px 10px">
<table><thead><tr><th>Result</th><th>Bout</th><th>Method</th></tr></thead>
<tbody>@@RESULTS@@</tbody></table>
</div>
<p class="note"><b>Bonuses:</b> UFC.com&rsquo;s bonus coverage records <b>four Performance of the Night awards and no
Fight of the Night</b> &mdash; Parnasse, Sola, Keita and <b>Mario Pinto</b>, who stopped Ryan Spann 55 seconds into
round two. No dollar figure is stated by UFC.com, so none is printed here.</p>

<h2 class="sec">Prospect Watch</h2>
@@PROSPECTS@@

<h2 class="sec">Around the Sport</h2>
<div class="panel">
<ul class="bul">
<li><b>Parnasse arrived exactly as advertised.</b> Salahdine Parnasse stopped Dan Hooker in the first round of the UFC
Paris main event on his promotional debut. He is 28, a former two-time KSW featherweight champion and one-time KSW
lightweight champion who signed with the UFC in late July 2026 having previously turned the promotion down, and he now
has <b>six straight wins, all by stoppage</b>. UFC.com says he &ldquo;instantly enters the highly touted lightweight
Top 15&rdquo;.</li>
<li><b>The women&rsquo;s flyweight belt is genuinely vacant</b>, and UFC.com&rsquo;s own billing for UFC 332 confirms it
&mdash; the Silva vs Wang Cong bout is labelled the women&rsquo;s flyweight championship. Any &ldquo;current
champions&rdquo; list still seating Valentina Shevchenko at 125 pounds is out of date.</li>
<li><b>Contender Series week five produced four contracts</b> on Tuesday 8 September at the Meta Apex: Quentin Pasley
(KO by elbows, R1 4:41), Isaac Moreno (UD 29-28 &times;3), Martin Koz&aacute;k (TKO, R2 1:32) and Christian Natividad
(KO by body punch, R1 1:10). Apollo Gomes won by unanimous decision but was not signed. Week six is Tuesday
15 September.</li>
<li><b>October also has a Fight Night</b> headlined by Joaquin Buckley vs Mike Malott.</li>
</ul>
</div>

<h2 class="sec">Rankings &amp; Business</h2>
<div class="panel">
<p style="margin:0 0 11px"><b>Rankings movement.</b> Islam Makhachev holds the <b>#1 spot in the men&rsquo;s
pound-for-pound rankings</b> as of 8 September 2026. Jean Silva enters Saturday ranked <b>sixth at featherweight</b>;
UFC 332&rsquo;s featured bouts carry the seeds <b>(#1) Natalia Silva</b>, <b>(#8) Wang Cong</b>, <b>(#9) Deiveson
Figueiredo</b> and <b>(#11) Payton Talbott</b>. Movsar Evloev remains the featherweight #1 contender after beating
Lerone Murphy at UFC London in March.</p>
<p style="margin:0"><b>Business and broadcast.</b> UFC Paris grossed <b>$4,365,335</b> on an attendance of
<b>15,687</b> &mdash; a sell-out, and the <b>highest-grossing event in Accor Arena history</b>. Saturday&rsquo;s Noche
UFC streams on Paramount+ in the U.S. with no extra pay-per-view charge, the model the promotion has now used for
several cards running. No viewership or gate figure has been published for Noche UFC, so none is printed.</p>
</div>

<h2 class="sec">Champions Board</h2>
<div class="panel" style="padding:6px 10px">
<table><thead><tr><th>Division</th><th>Champion</th><th>How and when</th></tr></thead>
<tbody>@@CHAMPS@@</tbody></table>
</div>
<p class="note">Cross-checked against ESPN&rsquo;s &ldquo;Current and all-time UFC champions&rdquo; for this edition and
reconciled against the most recent completed card. Pereira does not hold the light-heavyweight title, Chimaev does not
hold the middleweight title, and featherweight is not vacant.</p>

<h2 class="sec">Sources</h2>
<div class="panel"><div class="srcs">@@SRC@@</div></div>

<p class="disc">Cards and bouts are subject to change &mdash; withdrawals, replacements and reshuffles are routine, and
Saturday&rsquo;s main event is itself the product of one. Betting lines move; the odds shown carry the book that quoted
them at the time of the read.</p>
"""


def weighin():
    return "".join('<tr><td><b>%s</b></td><td class="mut">%s</td></tr>' % (b, d) for b, d in WEIGHIN)


body = (BODY.replace("@@MAST@@", masthead("The Octagon", "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
            .replace("@@TLDR@@", tldr("Tale of the Tape", S_MMA))
            .replace("@@FRESH@@", FRESH)
            .replace("@@NAV@@", nav("mma"))
            .replace("@@CDN@@", CDN)
            .replace("@@UPCOMING@@", upcoming())
            .replace("@@WEIGHIN@@", weighin())
            .replace("@@RESULTS@@", results())
            .replace("@@PROSPECTS@@", prospects())
            .replace("@@CHAMPS@@", champs())
            .replace("@@SRC@@", srcblock(SRC)))

html = page("The Octagon &mdash; Daily Briefings", CSS, body)
io.open(os.path.join(OUT, "mma-briefing.html"), "w", encoding="utf-8").write(html)
print("mma ok", len(html))
