# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import css, masthead, nav, page
from common_1635 import S_MMA, tldr, FRESH, srcblock

OUT = os.path.dirname(os.path.abspath(__file__))
ACC, ACC2 = "#e84545", "#ff8a5c"
EXTRA = """
.cdn{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:12px;
  padding:12px 16px;margin-bottom:16px;display:flex;flex-wrap:wrap;align-items:baseline;gap:12px}
.cdn .lab{font-family:var(--mono);font-size:10.5px;letter-spacing:.17em;text-transform:uppercase;color:var(--accent)}
.cdn .clk{font-family:var(--mono);font-size:19px;color:var(--accent2);letter-spacing:-.4px}
.cdn .ev{font-size:14px;color:var(--muted)}
.dv{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;color:var(--warn);text-transform:uppercase;margin-bottom:6px}
"""
CSS = css(ACC, ACC2, "#100c0c", "#1a1313", "#322020", EXTRA)

SRC = [
 ("UFC.com - Official Weigh-In Results | Noche UFC",
  "https://www.ufc.com/news/noche-ufc-silva-delgado-official-weigh-in-results"),
 ("Yahoo Sports - Noche UFC weigh-in results: Jean Silva is ready for Noche UFC redemption",
  "https://sports.yahoo.com/articles/noche-ufc-weigh-results-jean-174628011.html"),
 ("Heavy.com - Jean Silva vs. Jose Delgado Noche UFC Betting Odds Revealed",
  "https://heavy.com/sports/ufc/jean-silva-jose-delgado-odds-revealed/"),
 ("LowKick MMA - UFC Noche: Jean Silva Heavy Favorite As Jose Delgado Takes Late Main Event Call",
  "https://www.lowkickmma.com/ufc-noche-jean-silva-heavy-favorite-as-jose-delgado-takes-late-main-event-call/"),
 ("CBS Sports - Noche UFC predictions: fight card, odds and expert picks for Arizona",
  "https://www.cbssports.com/ufc/news/noche-ufc-fight-card-predictions-jean-silva-jose-delgado-odds/"),
 ("Cageside Press - Noche UFC: Silva vs. Delgado Weigh-In Results",
  "https://cagesidepress.com/2026/09/11/noche-ufc-silva-vs-delgado-weigh-in-results/"),
 ("UFC.com - UFC 332: Silva vs Wang", "https://www.ufc.com/event/ufc-332"),
 ("Tapology - UFC 331: Van vs. Pantoja 2", "https://www.tapology.com/fightcenter/events/145652-ufc-331"),
 ("Tapology - UFC 332: Silva vs. Wang", "https://www.tapology.com/fightcenter/events/146635-ufc-332"),
 ("ESPN - Current and all-time UFC champions",
  "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
 ("Yahoo Sports - No Bets Barred: Jean Silva and Jose Delgado are about to go to war at Noche UFC",
  "https://sports.yahoo.com/articles/no-bets-barred-jean-silva-000000434.html"),
]

CARDS = [
 (['<span class="t hot">tomorrow</span>', '<span class="t">main event</span>'],
  "12 September 2026 &middot; Desert Diamond Arena, Glendale, Arizona",
  "Noche UFC: Silva vs. Delgado",
  "The fourth annual Noche UFC, on Mexican Independence Day weekend and the promotion&rsquo;s first event at this "
  "venue. Featherweight main event over five rounds; <b>all 26 fighters made weight</b>, with Jean Silva on the "
  "championship limit at <b>145</b> and Jose Miguel Delgado at <b>145.5</b>. Prelims <b>2 PM ET</b>, main card "
  "<b>5 PM ET</b>, on Paramount+ at no extra charge.",
  "Odds: Silva &minus;450 / Delgado +350 (Caesars); &minus;440 / +340 (DraftKings); the line moved to &minus;425 / "
  "+355 within hours of opening."),
 (['<span class="t gold">title fight</span>'],
  "19 September 2026 &middot; Crypto.com Arena, Los Angeles",
  "UFC 331: Van vs. Pantoja 2",
  "A flyweight championship rematch between reigning champion <b>Joshua Van</b> and former champion "
  "<b>Alexandre Pantoja</b> headlines a 13-fight card. Co-main: <b>Arman Tsarukyan vs Mauricio Ruffy</b> over five "
  "rounds; <b>Marlon Vera vs Charles Jourdain</b> at bantamweight.",
  "No moneyline for the main event appeared in any source read this run, so none is printed."),
 (['<span class="t new">New</span>', '<span class="t gold">vacant title</span>', '<span class="t">broadcast</span>'],
  "3 October 2026 &middot; Delta Center, Salt Lake City",
  "UFC 332: Silva vs. Wang",
  "<b>Natalia Silva vs Wang Cong</b> for the <b>vacant</b> women&rsquo;s flyweight title tops a 13-fight card, with "
  "<b>Deiveson Figueiredo vs Payton Talbott</b> featured. This will be the <b>first numbered UFC event whose main card "
  "airs on CBS</b>.",
  "No moneyline appeared in any source read this run."),
 (['<span class="t gold">two title fights</span>'],
  "24 October 2026 &middot; Abu Dhabi",
  "UFC 333",
  "Featherweight champion <b>Alexander Volkanovski</b> and bantamweight champion <b>Petr Yan</b> are both booked to "
  "defend on this card.",
  "Bout order and opponents are as previously verified; no odds have been published in a source read this run."),
]


def cards():
    out = ['<div class="cards">']
    for tags, dv, h, p, odds in CARDS:
        out.append('<div class="card"><div class="tags">%s</div><div class="dv">%s</div><h3>%s</h3><p>%s</p>'
                   '<p style="margin-top:8px;color:var(--muted);font-size:13px">%s</p></div>'
                   % ("".join(tags), dv, h, p, odds))
    out.append('</div>')
    return "".join(out)


RESULTS = [
 ("Salahdine Parnasse", "def. Dan Hooker", "TKO, Round 1, 2:25"),
 ("Axel Sola", "def. Far&egrave;s Ziam", "KO, Round 1, 1:40"),
 ("Michael &lsquo;Venom&rsquo; Page", "def. Nursulton Ruziboev", "Unanimous decision, 29-28 x3"),
 ("Daniil Donchenko", "def. Punahele Soriano", "Unanimous decision, 30-27, 30-27, 29-28"),
 ("Kurtis Campbell", "def. Trevor Peek", "Submission, rear-naked choke, Round 3, 3:07"),
 ("Losene Keita", "def. Muhammad Naimov", "KO, Round 1, 2:54"),
]


def resrows():
    return "".join('<tr><td class="up"><b>%s</b></td><td>%s</td><td>%s</td></tr>' % r for r in RESULTS)


PROSPECTS = [
 (['<span class="t pro">prospect</span>', '<span class="t">short notice</span>'],
  "Jose Miguel Delgado (12-2)",
  "Took the Noche UFC main event on <b>twenty-four days&rsquo; notice</b> after Yair Rodriguez withdrew, and has "
  "<b>never faced a ranked opponent</b>. A win over a top-ten featherweight in a five-round headliner would be one of "
  "the larger single-night leaps available on the roster."),
 (['<span class="t pro">prospect</span>', '<span class="t">callout</span>'],
  "Losene Keita",
  "A former Oktagon double champion who knocked out Muhammad Naimov in the first round at UFC Paris and called out "
  "Lerone Murphy afterwards. One of four Performance of the Night winners on that card."),
 (['<span class="t pro">prospect</span>', '<span class="t">first UFC win</span>'],
  "Kurtis Campbell",
  "Submitted Trevor Peek by rear-naked choke in the third round in Paris for his first UFC victory &mdash; and became "
  "the first fighter to finish Peek."),
]


def prospects():
    out = ['<div class="cards">']
    for tags, h, p in PROSPECTS:
        out.append('<div class="card"><div class="tags">%s</div><h3>%s</h3><p>%s</p></div>' % ("".join(tags), h, p))
    out.append('</div>')
    return "".join(out)


CHAMPS = [
 ("Heavyweight", "Tom Aspinall", "Undisputed since 21 June 2025. <b>Interim:</b> Ciryl Gane (KO2 Alex Pereira, Freedom 250, 14 June 2026)."),
 ("Light Heavyweight", "Carlos Ulberg", "Won the vacant title by KO1 over Ji&#345;&iacute; Proch&aacute;zka at UFC 327, 11 April 2026."),
 ("Middleweight", "Sean Strickland", "Split-decision upset of Khamzat Chimaev at UFC 328, 9 May 2026 &mdash; a two-time champion."),
 ("Welterweight", "Islam Makhachev", "UD over Jack Della Maddalena, UFC 322, 15 November 2025. One defence: UD Ian Machado Garry, UFC 330."),
 ("Lightweight", "Justin Gaethje", "TKO4 of Ilia Topuria at UFC Freedom 250, 14 June 2026."),
 ("Featherweight", "Alexander Volkanovski", "UD over Diego Lopes at UFC 314, 12 April 2025; defended at UFC 325. Booked to defend at UFC 333."),
 ("Bantamweight", "Petr Yan", "UD over Merab Dvalishvili at UFC 323, 6 December 2025. Booked to defend at UFC 333."),
 ("Flyweight", "Joshua Van", "TKO1 of Alexandre Pantoja at UFC 323; defended TKO5 over Tatsuro Taira at UFC 328. Rematches Pantoja at UFC 331."),
 ("Women&rsquo;s Bantamweight", "Kayla Harrison", "Submission in round two over Julianna Pe&ntilde;a, UFC 316, 7 June 2025."),
 ("Women&rsquo;s Flyweight", "<span class='mut'>Vacant</span>", "Valentina Shevchenko <b>vacated</b> the title while sidelined by injury. Natalia Silva and Wang Cong contest it at UFC 332 on 3 October."),
 ("Women&rsquo;s Strawweight", "Mackenzie Dern", "UD over Virna Jandiroba, UFC 321, 25 October 2025. One defence: UD Gillian Robertson, UFC 330."),
]


def champrows():
    return "".join('<tr><td class="mut">%s</td><td><b>%s</b></td><td>%s</td></tr>' % c for c in CHAMPS)


COUNTDOWN = """<div class="cdn">
<span class="lab">Next card</span>
<span class="clk" id="ufccdn">&nbsp;</span>
<span class="ev">Noche UFC: Silva vs. Delgado &middot; Desert Diamond Arena, Glendale &middot; main card 5 PM ET Saturday</span>
</div>
<script>(function(){var t=new Date('2026-09-12T17:00:00-04:00');function u(){var d=t-new Date();var e=document.getElementById('ufccdn');if(!e)return;if(d<=0){e.textContent='Fight week \\u2014 live/completed';return;}var m=Math.floor(d/60000),h=Math.floor(m/60),dy=Math.floor(h/24);e.textContent=dy+'d '+(h%24)+'h '+(m%60)+'m';}u();setInterval(u,30000);})();</script>"""

BODY = """@@MAST@@
@@TLDR@@
@@FRESH@@
@@NAV@@

@@CDN@@

<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:3px solid var(--accent)">
<h3 style="margin:0 0 9px;font-size:20px">Noche UFC makes weight in Glendale &mdash; and the market has already made up its mind</h3>
<p style="margin:0 0 11px">All <b>26 fighters</b> across the thirteen-bout card hit their marks at Friday&rsquo;s
official weigh-in. <b>Jean Silva</b> came in at the featherweight championship limit of <b>145</b> pounds and
<b>Jose Miguel Delgado</b> at <b>145.5</b> for a five-round main event at Desert Diamond Arena &mdash; the UFC&rsquo;s
first show at the venue, on Mexican Independence Day weekend, and the fourth annual Noche UFC.</p>
<p style="margin:0 0 11px">The betting line is lopsided. Caesars has Silva at <b>&minus;450</b> and Delgado at
<b>+350</b>; DraftKings opened <b>&minus;440 / +340</b>; within hours of release the number had moved to
<b>&minus;425 / +355</b>. The shape of the matchup explains it &mdash; Delgado is <b>12-2</b>, took the fight on
<b>twenty-four days&rsquo; notice</b> after Yair Rodriguez withdrew, and has never shared the cage with a ranked
opponent, while Silva is the sixth-ranked featherweight.</p>
<p style="margin:0">There is a symmetry to the booking. Silva is the first fighter to headline multiple Noche UFC
events, back to back &mdash; and he lost last year&rsquo;s in San Antonio, to Diego Lopes. Co-main is
<b>Brandon Moreno vs Joseph Morales</b>, with <b>Manon Fiorot vs Alexa Grasso</b> and
<b>Waldo Cortes Acosta vs Curtis Blaydes</b> underneath.</p>
</div>

<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>
@@CARDS@@

<h2 class="sec">Last Event &mdash; UFC Paris, 5 September</h2>
<div class="panel" style="padding:6px 10px">
<table><thead><tr><th>Result</th><th>Bout</th><th>Method</th></tr></thead>
<tbody>@@RESULTS@@</tbody></table>
</div>
<p class="note"><b>Bonuses:</b> UFC.com&rsquo;s bonus coverage records <b>four Performance of the Night awards and no
Fight of the Night</b> &mdash; Parnasse, Sola, Keita and <b>Mario Pinto</b>, who stopped Ryan Spann 55 seconds into
round two. No dollar figure is stated by UFC.com, so none is printed here. Note on Parnasse: he is a former two-time
KSW featherweight and one-time KSW lightweight champion who signed with the UFC in late July 2026 and was given a main
event on debut &mdash; he did not come through the Contender Series.</p>

<h2 class="sec">Prospect Watch</h2>
@@PROSPECTS@@

<h2 class="sec">Around the Sport</h2>
<div class="panel">
<ul class="bul">
<li><b>Saturday is a full day of combat sports.</b> Noche UFC shares the date with Garcia vs Benn, with the UFC prelims
starting at 2 PM ET and the main card at 5 PM ET on Paramount+.</li>
<li><b>Joseph Morales is a TUF season 33 winner</b>, and <b>Alexa Grasso</b> is a former women&rsquo;s flyweight
champion &mdash; two of the more loaded undercard credentials on the Glendale bill.</li>
<li><b>UFC.com&rsquo;s weigh-in page renders &ldquo;Waldo Cortes Acosta&rdquo; without a hyphen</b>, which is the
spelling used here, since it is the primary source for the card.</li>
<li><b>October also carries a Fight Night</b> headlined by <b>Joaquin Buckley vs Mike Malott</b>.</li>
</ul>
</div>

<h2 class="sec">Rankings &amp; Business</h2>
<div class="panel">
<ul class="bul">
<li><b>Rankings movement:</b> Silva enters Saturday ranked <b>sixth</b> at featherweight; at UFC 332, Natalia Silva is
the <b>#1</b> seed and Wang Cong the <b>#8</b> in the vacant-title fight, with <b>#9 Deiveson Figueiredo</b> against
<b>#11 Payton Talbott</b> underneath. Islam Makhachev has been the UFC&rsquo;s <b>#1 pound-for-pound</b> fighter since
8 September.</li>
<li><b>Business &amp; broadcast:</b> UFC Paris produced gross total revenue of <b>$4,365,335</b> from an attendance of
<b>15,687</b> in a sellout &mdash; the <b>highest-grossing event in Accor Arena history</b>. UFC 332 will be the first
numbered event with its main card on <b>CBS</b>; Noche UFC streams on Paramount+ with no extra pay-per-view
charge.</li>
</ul>
</div>

<h2 class="sec">Champions Board</h2>
<div class="panel" style="padding:6px 10px">
<table><thead><tr><th>Division</th><th>Champion</th><th>Note</th></tr></thead>
<tbody>@@CHAMPS@@</tbody></table>
</div>
<p class="note">Verified against the current-champions listing and the most recent completed event this run. One
caution carried forward: aggregated &ldquo;current champions&rdquo; lists still seat Valentina Shevchenko at
125 pounds. She vacated the belt, and UFC.com itself bills the women&rsquo;s flyweight championship as being contested
between Natalia Silva and Wang Cong at UFC 332.</p>

<h2 class="sec">Sources</h2>
<div class="panel"><div class="srcs">@@SRC@@</div></div>

<p class="disc">The Octagon summarises public reporting. Cards and bouts are subject to change &mdash; fighters
withdraw, bouts get rebooked and betting lines move. Odds are quoted with the sportsbook that published them and were
accurate at the time of the read.</p>
"""

body = (BODY.replace("@@MAST@@", masthead("The Octagon", "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
            .replace("@@TLDR@@", tldr("Tale of the Tape", S_MMA))
            .replace("@@FRESH@@", FRESH)
            .replace("@@NAV@@", nav("mma"))
            .replace("@@CDN@@", COUNTDOWN)
            .replace("@@CARDS@@", cards())
            .replace("@@RESULTS@@", resrows())
            .replace("@@PROSPECTS@@", prospects())
            .replace("@@CHAMPS@@", champrows())
            .replace("@@SRC@@", srcblock(SRC)))

html = page("The Octagon &mdash; Daily Briefings", CSS, body)
io.open(os.path.join(OUT, "mma-briefing.html"), "w", encoding="utf-8").write(html)
print("mma ok", len(html))
