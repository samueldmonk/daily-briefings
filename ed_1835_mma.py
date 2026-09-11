import io
P = "/sessions/fervent-serene-bohr/mnt/outputs/mma-briefing.html"
s = io.open(P, encoding="utf-8").read()
n = 0
def rep(old, new):
    global s, n
    assert s.count(old) == 1, ("NOT UNIQUE/ABSENT: %r (%d)" % (old[:70], s.count(old)))
    s = s.replace(old, new); n += 1

# 1 — CORRECTION: a fourth book has Delgado at +310, so "nobody shorter than +340" is false
rep("""<b>Caesars has it Silva −450 / Delgado +350</b>, <b>DraftKings −440 / +340</b>, and a third book read this run has it <b>−425 / +355</b>. The spread across books is the story: nobody has Delgado shorter than +340.</p>""",
    """<b>Caesars has it Silva −450 / Delgado +350</b>, <b>DraftKings −440 / +340</b>, <b>FightOdds.io −425 / +355</b> and <b>MyBookie −441 / +310</b>. The spread across books is the story, and it is wider than it looked earlier: the underdog price runs from <b>+310 to +355</b> depending on where you look, so an earlier framing on this page that nobody had Delgado shorter than +340 is <b>corrected</b> — MyBookie does.</p>""")

# 2 — Delgado's full record and the precise notice
rep("""the unranked Delgado is <b>4-1 in the UFC</b> and took the booking on <b>less than a month's notice</b>.</p>""",
    """the unranked Delgado is <b>12-2</b> overall and <b>4-1 in the UFC</b>, took the booking on <b>twenty-four days' notice</b> and <b>has never faced a ranked opponent</b>. Silva's own record carries <b>twelve knockouts</b> and a single UFC defeat.</p>""")

# 3 — main-card odds line on the Fight Week card
rep("""<div class="odds">Odds: Silva −450 / Delgado +350 (Caesars) · −440 / +340 (DraftKings)</div>""",
    """<div class="odds">Odds: Silva −450 / Delgado +350 (Caesars) · −440 / +340 (DraftKings) · −441 / +310 (MyBookie)</div>""")

# 4 — UFC 331: how Van took the belt in the first meeting
rep("""Flyweight champion <b>Joshua Van</b> defends in a rematch with former champion <b>Alexandre Pantoja</b>.""",
    """Flyweight champion <b>Joshua Van</b> defends in a rematch with former champion <b>Alexandre Pantoja</b> at the <b>Crypto.com Arena in Los Angeles</b>. Van took the belt in the first meeting at <b>UFC 323 in December 2025</b> by technical knockout <b>26 seconds into round one</b>, after Pantoja sustained an arm injury.""")

# 5 — the vacancy now has its stated medical reason
rep("""Valentina Shevchenko vacated the title while sidelined for roughly a year;""",
    """Valentina Shevchenko vacated the title after withdrawing with a <b>ligament injury to her back and shoulder</b>, sidelined for roughly a year;""")

# 6 — summary strip: the odds spread rather than a single book's number
rep("""a −450 favourite over short-notice replacement Jose Miguel Delgado, who is 4-1 in the UFC.""",
    """a favourite at −425 to −450 across four books over short-notice replacement Jose Miguel Delgado, who is 12-2 overall and took the fight on twenty-four days' notice.""")

# 7 — sources read this run
rep("""    <div class="srcline">Yahoo Sports — UFC 331 fight card revealed, Van vs. Pantoja 2 leads loaded lineup — <a href="https://sports.yahoo.com/articles/ufc-331-fight-card-revealed-235537467.html">https://sports.yahoo.com/articles/ufc-331-fight-card-revealed-235537467.html</a></div>""",
    """    <div class="srcline">Yahoo Sports — UFC 331 fight card revealed, Van vs. Pantoja 2 leads loaded lineup — <a href="https://sports.yahoo.com/articles/ufc-331-fight-card-revealed-235537467.html">https://sports.yahoo.com/articles/ufc-331-fight-card-revealed-235537467.html</a></div>
    <div class="srcline">ESPN — Current and all-time UFC champions — <a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions</a></div>
    <div class="srcline">Wikipedia — UFC Fight Night: Silva vs. Delgado — <a href="https://en.wikipedia.org/wiki/UFC_Fight_Night:_Silva_vs._Delgado">https://en.wikipedia.org/wiki/UFC_Fight_Night:_Silva_vs._Delgado</a></div>
    <div class="srcline">Wikipedia — UFC 331 — <a href="https://en.wikipedia.org/wiki/UFC_331">https://en.wikipedia.org/wiki/UFC_331</a></div>
    <div class="srcline">Wikipedia — UFC 332 — <a href="https://en.wikipedia.org/wiki/UFC_332">https://en.wikipedia.org/wiki/UFC_332</a></div>
    <div class="srcline">CBS Sports — Noche UFC predictions: Jean Silva vs. Jose Delgado card, odds and picks — <a href="https://www.cbssports.com/ufc/news/noche-ufc-fight-card-predictions-jean-silva-jose-delgado-odds/">https://www.cbssports.com/ufc/news/noche-ufc-fight-card-predictions-jean-silva-jose-delgado-odds/</a></div>
    <div class="srcline">Fightful — Noche UFC 4: Silva vs. Delgado betting odds (MyBookie) — <a href="https://www.fightful.com/mma/noche-ufc-4-silva-vs-delgado-betting-odds-courtesy-of-mybookie/">https://www.fightful.com/mma/noche-ufc-4-silva-vs-delgado-betting-odds-courtesy-of-mybookie/</a></div>""")

io.open(P, "w", encoding="utf-8").write(s)
print("mma edits applied:", n)
