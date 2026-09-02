# -*- coding: utf-8 -*-
import css as C

ACCENT, ACCENT2 = "#e84545", "#ff8a5c"
CSS = C.base_css(ACCENT, ACCENT2, "#100c0c", "#1a1313", "#322020") + """
.cdn{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px 17px;
  margin-bottom:18px;display:flex;flex-wrap:wrap;align-items:baseline;gap:11px}
.cdn .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.cdn .v{font-family:var(--mono);font-size:19px;color:var(--accent2)}
.cdn .e{font-size:14px;color:var(--muted)}
.evdate{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#caa64a;margin-bottom:6px}
.top{border-left:3px solid var(--accent)}
"""

TLDR = ("UFC Paris is three days out with Salahdine Parnasse now a −600 favourite over Dan Hooker on his "
        "promotional debut, a line that has moved roughly 200 points since it opened.")

SOURCES = [
    ("UFC.com — Fight by Fight Preview: UFC Paris, Hooker vs. Parnasse",
     "https://www.ufc.com/news/fight-by-fight-preview-ufc-paris-hooker-vs-parnasse"),
    ("ESPN — UFC Fight Night: Hooker vs. Parnasse fight centre",
     "https://www.espn.com/mma/fightcenter/_/id/600059993/league/ufc"),
    ("Tapology — UFC Fight Night: Hooker vs. Parnasse",
     "https://www.tapology.com/fightcenter/events/144513-ufc-fight-night"),
    ("Rotowire — Hooker vs Parnasse Sep 5, 2026 odds",
     "https://www.rotowire.com/betting/mma/fight/salahdine-parnasse-vs-dan-hooker-odds-2026-09-05-5365"),
    ("MMA Odds Breaker — Opening betting odds for UFC Paris: Hooker vs. Parnasse",
     "https://www.mmaoddsbreaker.com/fight-odds/opening-odds/161246-opening-betting-odds-for-ufc-paris-hooker-vs-parnasse/"),
    ("UFC.com — UFC Shanghai results: Nurmagomedov vs Song",
     "https://www.ufc.com/news/ufc-shanghai-results-nurmagomedov-vs-song"),
    ("ESPN — UFC Fight Night: Nurmagomedov vs. Song results",
     "https://www.espn.com/mma/fightcenter/_/id/600060620/league/ufc"),
    ("Bloody Elbow — Umar Nurmagomedov vs Song Yadong UFC Shanghai result",
     "https://bloodyelbow.com/2026/08/29/umar-nurmagomedov-vs-song-yadong-ufc-shanghai-result-khabibs-cousin-knocked-out-cold/"),
    ("ESPN — Current and all-time UFC champions",
     "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
    ("UFC.com — Welcome to the UFC: DWCS Season 10, Week 4",
     "https://www.ufc.com/news/welcome-ufc-dwcs-season-10-week-4"),
    ("UFC.com — Dana White's Contender Series",
     "https://www.ufc.com/dwcs"),
    ("Tapology — UFC 331: Van vs. Pantoja 2",
     "https://www.tapology.com/fightcenter/events/145652-ufc-331"),
    ("UFCStats — upcoming events",
     "http://www.ufcstats.com/statistics/events/upcoming"),
]

CARDS = [
    ("Sat, Sept 5 · Accor Arena, Paris", "UFC Fight Night: Hooker vs. Parnasse",
     "Salahdine Parnasse makes his UFC debut in a main event, a lightweight bout against Dan Hooker. "
     "Fourteen fights. Co-main is an all-French lightweight meeting between Farès Ziam and Axel Sola; "
     "also booked are Michael Page vs Nursulton Ruziboev, Daniil Donchenko vs Punahele Soriano, "
     "Morgan Charrière vs Felipe Lima and Losene Keita vs Muhammad Naimov. Prelims 12 PM ET / main card "
     "3 PM ET on Paramount+ (start times carried from an earlier fetch, not re-sourced this run).",
     "Odds: Parnasse −600 / Hooker +425; DraftKings −600 / +440. Range across books −500 to −700 and "
     "+360 to +450.", "new"),
    ("Sat, Sept 12 · Glendale, Arizona", "Noche UFC: Silva vs. Delgado",
     "⚠ The billing for this card has now appeared four different ways across editions of this page — "
     "\"Noche UFC 4,\" \"Noche UFC: Silva vs Delgado,\" \"Noche UFC: Rodriguez vs. Silva\" and "
     "\"Noche UFC 4: Silva vs Delgado.\" All are printed; none is adopted. Only \"Silva\" is common to "
     "all four.", "", ""),
    ("Sat, Sept 19 · Crypto.com Arena, Los Angeles", "UFC 331: Van vs. Pantoja 2",
     "Joshua Van defends the flyweight championship against Alexandre Pantoja in a rematch of their "
     "UFC 323 meeting. Thirteen fights. Co-main is Arman Tsarukyan vs Maurício Ruffy at lightweight over "
     "five rounds; also Renato Moicano vs Brian Ortega and Patrício Pitbull vs Doo Ho Choi.", "", ""),
    ("Sat, Sept 26 · Las Vegas", "UFC Fight Night: Rosas Jr. vs. Barcelos",
     "⚠ The name order reverses between listings — one has it Rosas Jr. vs. Barcelos, another Barcelos vs. "
     "Rosas Jr. Both are printed.", "", ""),
    ("Sat, Oct 3 · Salt Lake City, Utah", "UFC 332",
     "No headliner was sourced this run, and none is invented.", "", ""),
    ("Sat, Oct 24 · Abu Dhabi", "UFC 333: Volkanovski vs. Evloev",
     "Alexander Volkanovski against Movsar Evloev at featherweight. ⚠ The schedule listing that supplies "
     "this headliner does <b>not</b> describe it as a title fight; it is understood to be one on the "
     "strength of this desk's standing record that Volkanovski is the reigning featherweight champion and "
     "Evloev the number-one contender, and that is said here rather than left to look like the listing's "
     "claim.", "", ""),
]

RESULTS = [
    ("win", "Song Yadong def. Umar Nurmagomedov", "KO (right uppercut), R2, 1:48"),
    ("win", "Denise Gomes def. Yan Xiaonan", "KO (punch), R1, 4:49"),
]

PROSPECTS = [
    ("Adam Darby", "Signed out of Dana White's Contender Series Season 10, Week 4 on September 1 in "
                   "Las Vegas after what UFC.com described as a masterclass of distance striking."),
    ("Gabriel Lorenço", "Demolished Charlie Cleveland in a heavyweight bout to earn his roster spot; Dana "
                        "White called him \"a new 26-year-old heavyweight beast.\" ⚠ The surname is rendered "
                        "both \"Lorenço\" and \"Lorenco\" across sources."),
    ("Modestino Rodrigues, Silvestre Sanchez, Adam Livingston",
     "The other three Week 4 winners, all signed — the second consecutive week in which all five winners "
     "were awarded contracts. Fifteen athletes had been added through the first three weeks."),
]

AROUND = [
    "<b>Song Yadong is staking a claim at bantamweight.</b> His Shanghai knockout of Umar Nurmagomedov — "
    "as roughly a 4-to-1 underdog — was reported as putting him in line for a title shot. No updated "
    "official ranking positions were sourced this run, so this page states the result and declines to "
    "state the ladder.",
    "<b>A Paris card change:</b> Mairon Santos withdrew with illness from his bout with Nathaniel Wood; "
    "undefeated newcomer Pavel Andrusca, a former Vendetta FN champion, steps in on debut. Carried from an "
    "earlier fetch.",
    "⚠ <b>A widely-surfacing \"Dana White announces\" item was refused.</b> A search return this run "
    "presented a slate pairing Kayla Harrison with Amanda Nunes, Sean O'Malley with Song Yadong and Alexa "
    "Grasso with Rose Namajunas as current news. It is undated and describes \"the first slate of fights "
    "for 2026\" — and this desk's standing record is that the Harrison–Nunes booking for UFC 324 on "
    "January 24 was <b>cancelled</b> after Harrison withdrew for neck surgery. Nothing from it is "
    "published. It is the same defect the cyber page catches weekly: a real announcement, re-served as "
    "today's.",
    "⚠ <b>The Contender Series calendar disagrees with itself.</b> An earlier fetch put Season 10 Week 5 on "
    "<b>September 8</b> at the Meta APEX; this run's fetch puts Week 5 on <b>September 15</b>, with Week 7 "
    "on September 22 and Week 8 on September 29. Both are printed; neither is adopted.",
]

BONUSES = ("Performance of the Night, $100,000 each: <b>Song Yadong</b> and <b>Bilal Hasan</b>. Fight of "
           "the Night, $100,000 each: <b>Levi Rodrigues Jr. vs. Ce Liu</b>. A further $25,000 each went to "
           "Denise Gomes, Kai Asakura, Andre Lima, Rei Tsuruya, Francesco Nuzzi, Hector Santiago and Julia "
           "Polastri. Carried from an earlier run's MMA Mania fetch; not re-sourced this run.")

CHAMPS = [
    ("Heavyweight", "Tom Aspinall", "Undisputed since June 21, 2025."),
    ("Interim Heavyweight", "Ciryl Gane", "KO2 over Alex Pereira at Freedom 250, June 14, 2026."),
    ("Light Heavyweight", "Carlos Ulberg", "Won the vacant belt, KO1 over Jiří Procházka at UFC 327, "
                                           "April 11, 2026; had ACL surgery afterwards."),
    ("Middleweight", "Sean Strickland", "Split-decision upset of Khamzat Chimaev at UFC 328, May 9, 2026 "
                                        "— a two-time champion."),
    ("Welterweight", "Islam Makhachev", "UD over Jack Della Maddalena, UFC 322. One defence — UD over Ian "
                                        "Machado Garry, UFC 330, August 15, 2026, his 17th straight "
                                        "Octagon win."),
    ("Lightweight", "Justin Gaethje", "TKO4 over Ilia Topuria at Freedom 250, June 14, 2026."),
    ("Featherweight", "Alexander Volkanovski", "Defended by UD over Diego Lopes at UFC 325, January 31, "
                                               "2026. Booked against Movsar Evloev at UFC 333."),
    ("Bantamweight", "Petr Yan", "UD over Merab Dvalishvili, UFC 323, December 6, 2025."),
    ("Flyweight", "Joshua Van", "TKO1 over Alexandre Pantoja, UFC 323; defended TKO5 over Tatsuro Taira, "
                                "UFC 328. Rematches Pantoja at UFC 331."),
    ("Women's Flyweight", "Valentina Shevchenko", "—"),
    ("Women's Bantamweight", "Kayla Harrison", "Zero defences — the scheduled UFC 324 defence against "
                                               "Amanda Nunes was cancelled."),
    ("Women's Strawweight", "Mackenzie Dern", "One defence — UD over Gillian Robertson, UFC 330, "
                                              "August 15, 2026."),
    ("Women's Featherweight", "Vacant", "—"),
]

COUNTDOWN_JS = """<script>(function(){var t=new Date('2026-09-05T12:00:00-04:00');function u(){var el=document.getElementById('ufccdn');if(!el)return;var d=t-new Date();if(d<=0){el.textContent='Fight week \\u2014 live/completed';return;}var dd=Math.floor(d/86400000),hh=Math.floor(d%86400000/3600000),mm=Math.floor(d%3600000/60000);el.textContent=dd+'d '+hh+'h '+mm+'m';}u();setInterval(u,30000);})();</script>"""


def build():
    p = []
    p.append(C.head("The Octagon — Daily Briefings", CSS))
    p.append('<div class="masthead"><h1>&#8856; The Octagon</h1>'
             '<p class="tag">Your daily MMA briefing — UFC, prospects &amp; the business of fighting</p>'
             + C.meta_row() + "</div>")
    p.append('<div class="tldr"><b>Tale of the Tape</b> <span>%s</span></div>' % TLDR)
    p.append('<div class="freshline" id="freshline">&nbsp;</div>')
    p.append(C.nav("mma"))

    p.append('<div class="cdn"><span class="k">Next Card</span>'
             '<span class="v" id="ufccdn">&nbsp;</span>'
             '<span class="e">UFC Fight Night: Hooker vs. Parnasse — Saturday, September 5, '
             'Accor Arena, Paris (prelims 12 PM ET)</span></div>')

    # TOP STORY
    p.append('<h2 class="sec">Top Story</h2>')
    p.append('<div class="panel top"><h3>Paris is three days away, and the market has decided the debutant '
             'is the safe bet</h3>'
             '<p>Salahdine Parnasse walks into the Accor Arena on Saturday for his first UFC fight — as a '
             '<b>−600 favourite</b>. Dan Hooker, <b>24-14</b> as a professional and <b>14-10</b> inside the '
             'Octagon, is the <b>+425</b> underdog in his own opponent\'s promotional debut. '
             'The line opened around −400/+300 and has moved roughly 200 points toward the Frenchman since; '
             'DraftKings has it −600/+440 and prices across books run from −500 to −700 and +360 to +450.</p>'
             '<p>That number is not a novelty act. Parnasse is 23-2, a <b>two-time KSW featherweight '
             'champion and one-time KSW lightweight champion</b> who went 14-2 in that promotion with four '
             'defences of the lightweight belt, signed with the UFC in <b>late July 2026</b> having '
             'previously turned the promotion down, and made his U.S. debut in May with a first-round '
             'stoppage of Kenneth Cross for a fifth consecutive win. He is a debutant in this promotion and '
             'nothing more than that — not a UFC veteran, not ranked — but he did not come through the '
             'Contender Series, and this page has corrected that error once and will not repeat it.</p></div>')

    # CARDS
    p.append('<h2 class="sec">Fight Week — Upcoming Cards</h2>')
    cards = []
    for date, name, note, odds, isnew in CARDS:
        t = '<span class="tag new">New</span>' if isnew == "new" else ""
        o = '<p style="margin-top:8px;color:#caa64a">%s</p>' % odds if odds else ""
        cards.append('<div class="card"><div class="evdate">%s</div><h4>%s</h4>%s<p>%s</p>%s</div>'
                     % (date, name, t, note, o))
    p.append('<div class="cards two">' + "".join(cards) + "</div>")
    p.append('<div class="note">Also on the schedule and sourced this run: <b>October 10</b> — Allen vs. '
             'Duncan, Las Vegas; <b>October 17</b> — Buckley vs. Malott, Edmonton; <b>October 31</b> — '
             'Las Vegas, no headliner sourced. Odds are reproduced from source snippets; where a book is '
             'named it is named, and where none was, none is claimed.</div>')

    # RESULTS
    p.append('<h2 class="sec">Last Event — Results</h2>')
    rows = "".join('<tr><td class="%s">Win</td><td>%s</td><td>%s</td></tr>' % r for r in RESULTS)
    p.append('<div class="tblwrap"><table><tr><th>Result</th><th>Bout</th><th>Method</th></tr>'
             + rows + "</table></div>")
    p.append('<div class="note"><b>UFC Fight Night: Nurmagomedov vs. Song</b> — Saturday, August 29, '
             'Oriental Sports Center, Shanghai; 13 fights. Only bouts confirmed by a source fetched this '
             'run are tabled, and no undercard result is guessed. Two method variances are preserved rather '
             'than smoothed over: Song\'s finishing strike reads "right uppercut" in one account and simply '
             '"punch" in another, and the Gomes finish reads "TKO" in one and "KO" in another. Song entered '
             'as roughly a 4-to-1 underdog.<br><br><b>Performance bonuses.</b> %s</div>' % BONUSES)

    # PROSPECTS
    p.append('<h2 class="sec">Prospect Watch</h2>')
    cards = []
    for name, body in PROSPECTS:
        cards.append('<div class="card"><h4>%s</h4><span class="tag new">prospect</span><p>%s</p></div>'
                     % (name, body))
    p.append('<div class="cards two">' + "".join(cards) + "</div>")

    # AROUND
    p.append('<h2 class="sec">Around the Sport</h2>')
    p.append('<div class="panel"><ul class="b">' + "".join("<li>%s</li>" % a for a in AROUND) + "</ul></div>")

    # RANKINGS & BUSINESS
    p.append('<h2 class="sec">Rankings &amp; Business</h2>')
    p.append('<div class="panel">'
             '<p><b>Rankings movement.</b> No updated official ranking positions were sourced after '
             'Shanghai. This page states results and declines to state the ladder.</p>'
             '<p><b>Business &amp; broadcast.</b> Freedom 250 drew <b>34 million total global viewers</b>, '
             '17 million of them across the United States and Latin America, per TKO Group as reported on '
             'June 26, 2026. Paramount is in <b>year one of a seven-year, $7.7 billion deal</b>, and the '
             'Canada expansion beginning in 2027 covers all 13 marquee numbered-event main cards at no '
             'extra cost to Paramount+ subscribers. All three figures are carried from an earlier run\'s '
             'fetch and were not re-sourced today. A separately reported Hollywood Reporter figure of '
             '8 million average viewers for the White House card is an <em>average</em>, not a total, and '
             'is deliberately not combined with or compared against the TKO numbers.</p></div>')

    # CHAMPIONS
    p.append('<h2 class="sec">Champions Board</h2>')
    rows = "".join('<tr><td>%s</td><td class="win">%s</td><td>%s</td></tr>' % c for c in CHAMPS)
    p.append('<div class="tblwrap"><table><tr><th>Division</th><th>Champion</th><th>Note</th></tr>'
             + rows + "</table></div>")
    p.append('<div class="note"><b>The stale champions list returned for a twenty-third time, and it was '
             'wrong in exactly the same single cell.</b> The list fetched this run gives middleweight to '
             'Khamzat Chimaev. The correct answer is <b>Sean Strickland</b>, who took the belt by split '
             'decision at UFC 328 on May 9, 2026. Twelve of the thirteen cells it offered were right — '
             'which is precisely '
             'why the error keeps surviving a casual read. Error counts across the last seventeen fetches: '
             '1, 3, 1, 3, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, <b>1</b>. The board above is the corrected '
             'one. Two cells were independently confirmed by this run\'s fetches: light heavyweight to '
             'Ulberg, and "Women\'s Featherweight: Vacant," which is correct and was offered for the sixth '
             'time.</div>')

    p.append(C.sources(SOURCES))
    p.append('<div class="disc">Cards and bouts are subject to change — fighters withdraw, bouts are '
             'rebooked and betting lines move continuously. Odds shown are point-in-time figures from the '
             'sources listed above, not live prices.</div></footer>')
    p.append(COUNTDOWN_JS)
    p.append(C.STAMP_JS)
    p.append("</div></body></html>")
    return "".join(p)


if __name__ == "__main__":
    open("mma-briefing.html", "w").write(build())
    print("mma ok")
