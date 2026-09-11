import io, sys
P = "/sessions/fervent-serene-bohr/mnt/outputs/wallstreet-briefing.html"
s = io.open(P, encoding="utf-8").read()
n = 0
def rep(old, new):
    global s, n
    assert s.count(old) == 1, ("NOT UNIQUE/ABSENT: %r (%d)" % (old[:70], s.count(old)))
    s = s.replace(old, new); n += 1

# 1 — summary strip: the 85.6% point estimate becomes a two-read spread
rep("and CME FedWatch now puts the odds of a Fed hike on Wednesday at 85.6%.",
    "and futures pricing for a Fed hike on Wednesday now spans roughly 71% to 85.6% depending on the read.")

# 2 — lead headline
rep("Dow adds 509 points to end a losing week on a high note as crude cools and rate-hike odds reach 85.6%",
    "Dow adds 509 points to end a losing week on a high note as crude cools and rate-hike bets firm into Wednesday")

# 3 — the hike-probability paragraph, rewritten around two named reads
rep("""<p>The hike probability now has a named source and a precise number: <b>CME FedWatch puts the odds of a hike at Wednesday's meeting at 85.6%</b>. That is the figure this page leads with, because it is attributed to the futures tool itself rather than to a summary of it. The looser reads still in circulation bracket it — one has traders at <b>roughly 90%, up from about 70%</b> before Friday morning's CPI, another puts futures pricing at <b>about 71%</b>, a third at <b>above 65%</b> — and every one of them shares the direction: a hike, not a cut, and firmer after the release.</p>""",
    """<p>The hike probability is printed as a spread, because the two best-attributed reads are fourteen points apart. A <b>CME FedWatch</b> read timed at <b>10:03 a.m. ET</b> gave <b>85.6%</b>; a futures read taken later in the session puts the probability at <b>around 71%</b>, up from earlier in the week. Two looser summaries bracket the same range — one at <b>roughly 90%, from about 70%</b> before Friday morning's CPI, another at <b>above 65%</b>. No single point estimate is asserted as the current number; what every read shares is the direction — a hike, not a cut, and firmer after the release.</p>""")

# 4 — breadth paragraph gains the intraday read
rep("""<p>Breadth backed the rally rather than a handful of megacaps: <b>nine of the eleven S&amp;P 500 sectors finished higher</b>, with technology, industrials and communication services each up more than 1% and only health care and utilities lagging.</p>""",
    """<p>Breadth backed the rally rather than a handful of megacaps: <b>nine of the eleven S&amp;P 500 sectors finished higher</b> on a session review, with technology, industrials and communication services each up more than 1% and only health care and utilities lagging. An intraday read earlier in the day had <b>ten of eleven</b> green, with communication services up <b>1.9%</b> — the session review is the later measurement and is the one this page asserts.</p>""")

# 5 — HPE: three reads now, so the spread is disclosed
rep("""An earlier read this run put the move at +9.08%; the later read gives "up nearly 11%", so it is printed as an approximation.""",
    """Reads of the move disagree: an 11:50 a.m. board gave +9.08%, a session review says "up nearly 11%" and a third read says "over 12%". It is printed as an approximation with the spread stated rather than a false precision.""")

# 6 — Cisco: second read
rep("""<p>The biggest percentage gainer in the Dow Jones Industrial Average — a quieter contribution than the AI-hardware names, but a direct one to the index that carried the session's headline.</p>""",
    """<p>The biggest percentage gainer in the Dow Jones Industrial Average, on a read that also credits strong AI-infrastructure demand and a quantum-networking partnership. A second read gives the move as <b>+3.43%</b>; both are this session, so the card states both rather than picking.</p>""")

# 7 — ACVA after-hours card: deal mechanics
rep("""<p>Copart agreed to acquire the online wholesale auto marketplace for <b>$10.50 a share in cash</b>, a deal reported at roughly <b>$1.9B</b>. The stock also finished the regular session up 44.8%.</p>""",
    """<p>Copart agreed to acquire the online wholesale auto marketplace for <b>$10.50 a share in cash</b>, valuing the equity at roughly <b>$1.9B</b>. Both boards approved unanimously and completion is targeted for <b>the end of 2026</b>, subject to customary conditions including antitrust review. The stock finished the regular session up 44.8%; reads of the day's move span <b>+40% to +45%</b>.</p>""")

# 8 — Chart of the Day note
rep("""The session's single biggest sourced mover: ACV Auctions finished the regular session up 44.8% on Copart's agreed buyout, and held a gain of roughly 44% after hours.""",
    """The session's single biggest sourced mover: ACV Auctions finished the regular session up 44.8% on Copart's agreed buyout — reads of the move span +40% to +45% — and held a gain of roughly 44% after hours.""")

# 9 — On the Radar FOMC bullet
rep("""futures are leaning toward a 25-basis-point hike from the 3.50–3.75% range; CME FedWatch puts the probability at <b>85.6%</b>; looser reads this run run from above 65% to roughly 90%, so the FedWatch figure is the one asserted and the rest are shown as the bracket around it.""",
    """futures are leaning toward a 25-basis-point hike from the 3.50–3.75% range. The probability is published as a spread: a <b>10:03 a.m. ET CME FedWatch</b> read gave <b>85.6%</b> and a later futures read gives <b>around 71%</b>, with looser summaries from above 65% to roughly 90%. No single number is asserted as current.""")

io.open(P, "w", encoding="utf-8").write(s)
print("wallstreet edits applied:", n)
