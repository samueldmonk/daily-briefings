#!/usr/bin/env python3
"""Wall Street page edits for the 10:50 AM Saturday Aug 29 2026 edition."""
import sys, io, os

D = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(D, "wallstreet-briefing.html")
STAMP = "10:50 AM"

h = io.open(P, encoding="utf-8").read()
fails = []


def rep(old, new, n=1):
    global h
    c = h.count(old)
    if c == 0:
        fails.append("NOT FOUND: " + old[:110])
        return
    if c != n:
        fails.append("COUNT %d != %d: %s" % (c, n, old[:110]))
        return
    h = h.replace(old, new)


# ---------------------------------------------------------------- 1. tldr
rep(
    "<div class=\"tldr\"><b>The Tape</b> <span>Markets are closed for the weekend, so Friday&rsquo;s official closes stand &mdash; the S&amp;P 500 slipped 0.25% to 7,711.76 and still finished the week higher &mdash; and the September rate call has turned over since Friday&rsquo;s bell: a prediction market that had put nearly 70% odds on the Fed holding now prices a 48% chance of a quarter-point hike after Warsh&rsquo;s Jackson Hole speech, with Friday&rsquo;s payrolls report the next test.</span></div>",
    "<div class=\"tldr\"><b>The Tape</b> <span>Markets are closed for the weekend, so Friday&rsquo;s official closes stand &mdash; the S&amp;P 500 slipped 0.25% to 7,711.76 and still finished the week higher &mdash; and a third read on the September rate call points the same way as the first two: the odds of a hike were put at about one in three before Warsh spoke at Jackson Hole and above 50/50 after, against a prediction market&rsquo;s 48%, with Friday&rsquo;s payrolls report the next test.</span></div>",
)

# ---------------------------------------------------------------- 2. Lead: seventh re-verification
rep(
    """and its official closes stand unchanged, re-verified a sixth time at 10:20 AM against a fresh
search returning the same three figures""",
    """and its official closes stand unchanged, re-verified a <b>seventh</b> time at """ + STAMP + """ against a fresh
search returning the same three figures""",
)

# ---------------------------------------------------------------- 3. Lead: Warsh substance
rep(
    """own words, that &ldquo;while this summer's PCE and CPI readings were better than expected, they do not tell me
that underlying trends have meaningfully improved.&rdquo;</p>""",
    """own words, that &ldquo;while this summer's PCE and CPI readings were better than expected, they do not tell me
that underlying trends have meaningfully improved.&rdquo;</p>
<p><b>What that speech was, in the reporting fetched at """ + STAMP + """.</b> Coverage of the address is
consistent on the substance and careful about its limits. Warsh said <b>inflation remains higher than the
central bank's longstanding 2% goal</b> and <b>suggested the Fed may need to raise interest rates in the
coming months</b>; one analysis frames the speech as his answer to critics of a <b>muddled July news
conference</b>, delivering the clearer warning that had been missing. Another account, equally sourced,
stresses what he withheld: he <b>gave no indication of where he thinks rates should be</b> and
<b>declined to set out the conditions under which he would advocate a change in policy</b>. Both
characterisations are printed. They are not in conflict &mdash; a warning about inflation and a refusal to
pre-commit to a rate path are different things, and he did both.</p>""",
)

# ---------------------------------------------------------------- 4. movers note
rep(
    """No market figure on this page changed at 10:20 AM; the September rate pricing, which is in <b>On the Radar</b>, turned over in the <b>9:40 AM</b> edition and is carried here.""",
    """<b>No figure on this movers board changed at """ + STAMP + """ either</b>, and none can while the tape is
shut. One number elsewhere on the page did move: the September rate pricing in <b>On the Radar</b> gained a
<b>third, independent read</b> at """ + STAMP + """ &mdash; it is not a stock move and it is not tagged as
one.""",
)

# ---------------------------------------------------------------- 5. rates table pricing row
rep(
    """<td>48% odds of a 25bp hike in September (Kalshi), revised down from ~70% odds of no change; &gt;70% odds of a hike by December</td><td>Sept read this run; Dec read carried</td>""",
    """<td><b>Three reads, all pointing the same way, none adopted.</b> Before the Jackson Hole speech, the odds of
a September hike were put at <b>about one in three</b>; after it, <b>above 50/50</b>. A prediction market
(Kalshi) separately prices <b>48%</b> odds of a 25bp hike in September, revised from ~70% odds of no change.
<b>&gt;70%</b> odds of a hike by December.</td><td>Pre/post-speech pair sourced """ + STAMP + """; Kalshi read 9:40 AM; Dec read carried</td>""",
)

# ---------------------------------------------------------------- 6. On the Radar / FOMC bullet
rep(
    """The above-70% odds of a hike by December is carried from the previous edition and was not restated by any source seen this run.</li>""",
    """The above-70% odds of a hike by December is carried from an earlier edition and was not restated by any source seen at """ + STAMP + """.</p>
<p><b>A third read arrived at """ + STAMP + """, and it reconciles the other two rather than adding a fourth
disagreement.</b> An analysis of the speech reports that <b>before Warsh spoke, investors put the odds of a
September rate hike at about one in three</b>, and that <b>after the speech that likelihood rose above
50/50</b>. Note what that does to the numbers already on this page: <b>about one in three odds of a hike is
the same state as roughly two in three odds of a hold</b>, which is the &ldquo;nearly 70% holding&rdquo;
figure the earlier editions carried &mdash; the same pre-speech moment described from the other side, not a
contradiction of it. The post-speech figures do differ: <b>above 50/50</b> against the prediction market's
<b>48%</b>. They are close, they come from different sources, and this page adopts neither and averages
nothing. The direction is the finding, and it has now survived three independent looks.</li>""",
)

# ---------------------------------------------------------------- 7. sources
rep(
    """<a href="https://www.econoday.com/">Econoday &mdash; 2026 economic calendar</a>""",
    """<a href="https://www.econoday.com/">Econoday &mdash; 2026 economic calendar</a><br><a href="https://www.cnbc.com/2026/08/28/kevin-warsh-jackson-hole-fed-inflation-rate-hike.html">CNBC &mdash; Analysis: Kevin Warsh sharpens inflation warning at Jackson Hole, signaling possible rate hike</a><br><a href="https://www.cnn.com/2026/08/28/business/fed-chairman-kevin-warsh-jackson-hole">CNN Business &mdash; Warsh stays quiet on interest rates but calls inflation &lsquo;concerning&rsquo;</a><br><a href="https://www.npr.org/2026/08/28/nx-s1-5947903/federal-reserve-inflation-jackson-hole-interest-rates">NPR &mdash; Warsh warns inflation is too high, sparking bets rate hikes are coming</a><br><a href="https://www.forbes.com/sites/tylerroush/2026/08/28/fed-chair-kevin-warsh-says-inflation-still-too-high-in-first-jackson-hole-speech/">Forbes &mdash; Warsh says inflation still too high in first Jackson Hole speech</a>""",
)

# ---------------------------------------------------------------- 8. stamps
h = h.replace("10:20 AM ET", STAMP + " ET")

if fails:
    print("FAILURES:")
    for f in fails:
        print("  -", f)
    sys.exit(1)

io.open(P, "w", encoding="utf-8").write(h)
print("ws OK")
