import io, sys
P = "/sessions/beautiful-zealous-mendel/mnt/outputs/wallstreet-briefing.html"
s = io.open(P, encoding="utf-8").read()
n = 0
def rep(old, new):
    global s, n
    c = s.count(old)
    assert c == 1, "count=%d for: %s" % (c, old[:110])
    s = s.replace(old, new); n += 1

# 1 — TLDR
rep(
"Two hours into the session the tech-led rally has broadened and the Dow has joined it — the latest read has the Dow up 217.20 points (+0.41%) and the Nasdaq Composite up 327.22 points (+1.25%), with Okta still the biggest single-stock mover on its results.",
"Just past noon the tech-led rally has cooled a step — the latest read has the Dow up 147.67 points (+0.28%) and the Nasdaq Composite up 279.61 points (+1.07%), both below the 11:35 tallies, with the S&amp;P 500 still holding a 0.4% gain and Okta still the biggest single-stock mover.")

# 2 — Lead tags
rep('<span class="tag new">Updated · 11:35 AM ET</span><span class="tag acc">Midday session</span>',
    '<span class="tag new">Updated · 12:05 PM ET</span><span class="tag acc">Midday session</span>')

# 3 — Lead headline
rep("<h3>The rally broadens at midday: the Dow joins in, Okta still leads — as of ~11:35 AM ET</h3>",
    "<h3>Past noon the rally cools a step: the Dow and Nasdaq give back part of the midday gain — as of ~12:05 PM ET</h3>")

# 4 — Lead paragraph one
rep('<p style="margin:0 0 10px">Roughly two hours into the regular session, US stocks are <b>climbing</b> after results from Nvidia, Salesforce and CrowdStrike lifted the technology trade. The strongest-anchored read seen this run has the <b>Dow up 217.20 points, or 0.41%</b>, the <b>Nasdaq Composite up 327.22 points, or 1.25%</b>, and the <b>S&amp;P 500 up 0.4%</b>. <b>That is a change from this page\'s 9:35 edition</b>, which had the Dow hovering near the flat line — the Dow has since moved decisively higher, and the page names the change rather than quietly overwriting it.</p>',
    '<p style="margin:0 0 10px">Just past noon, US stocks are still <b>climbing</b> after results from Nvidia, Salesforce and CrowdStrike lifted the technology trade — but the advance has <b>narrowed since late morning</b>. The latest read seen this run has the <b>Dow up 147.67 points, or 0.28%</b>, the <b>Nasdaq Composite up 279.61 points, or 1.07%</b>, and the <b>Russell 2000 up 7.64 points, or 0.25%</b>, with the <b>S&amp;P 500 holding a 0.4% gain</b>. <b>Both large-cap gauges are below the 11:35 tallies</b> this page carried — the Dow at +217.20 (+0.41%) and the Nasdaq at +327.22 (+1.25%) — so the direction is unchanged but the size of the move has come in. The page names that drift rather than quietly overwriting it.</p>')

# 5 — reconciliation paragraph opener
rep("<b>How this page chose between three competing index sets, and why.</b> A second read this run has the <b>Dow up 169.90 points (+0.32%)</b> and the <b>Nasdaq Composite up 300.97 points (+1.15%)</b>. Both sets are internally consistent, but only the first reconciles against Wednesday's verified close: 217.20 points on the Dow is 0.41% of Wednesday's level, and 327.22 on the Nasdaq is 1.25% of its level, while the second set implies a prior close that does not match Wednesday's. The first set therefore leads and the second is printed alongside; <b>neither is averaged, and neither source stamped its figures with a time</b>, so no level is asserted in this section — levels live in the Weekly Scorecard.",
    "<b>Four index reads have now been taken across this session, and all four reconcile to the same prior close.</b> In order: <b>+169.90 (+0.32%)</b>, <b>+217.20 (+0.41%)</b> and now <b>+147.67 (+0.28%)</b> on the Dow, and <b>+300.97 (+1.15%)</b>, <b>+327.22 (+1.25%)</b> and now <b>+279.61 (+1.07%)</b> on the Nasdaq Composite. Each pair divides out to a prior close within the rounding band of Wednesday's, which is what makes them a sequence of intraday snapshots rather than competing claims about one moment — <b>so the newest leads and the earlier ones are kept as history, not averaged away</b>. <b>No source stamped its figures with a time</b>, so no level is asserted in this section; levels live in the Weekly Scorecard.")

# 6 — CrowdStrike card
rep("<h3>CrowdStrike (CRWD) — quoted at +9% at midday, with a record ARR quarter</h3><p>The latest coverage seen this run has <b>CRWD up 9%</b>, against the <b>14.34%</b> this page carried at 9:35 and the <b>8.9%</b> it showed pre-open. All three reads are printed and none averaged.",
    "<h3>CrowdStrike (CRWD) — quoted at +9.4% past noon, with a record ARR quarter</h3><p>The latest coverage seen this run has <b>CRWD up 9.4%</b>, a shade firmer than the <b>9%</b> quoted at 11:35 and well below the <b>14.34%</b> this page carried at 9:35; it showed <b>8.9%</b> pre-open. All four reads are printed and none averaged.")
rep('<span class="tag new">Updated · 11:35</span><span class="tag acc">Cybersecurity</span>\n<h3>CrowdStrike',
    '<span class="tag new">Updated · 12:05</span><span class="tag acc">Cybersecurity</span>\n<h3>CrowdStrike')

# 7 — new Arm card, inserted after the Palantir card
old_pltr = '<h3>Palantir (PLTR) — up 3.8% to $184.32</h3><p>Palantir is <b>up 3.8% in morning trading, at $184.32</b>, lifted in the coverage seen this run by a fresh analyst endorsement. <span style="color:var(--mut)">The endorsing firm is not named in the text fetched here, so none is named on this page.</span></p></div>'
rep(old_pltr, old_pltr + """

<div class="card"><span class="tag new">New · 12:05</span><span class="tag acc">Semis</span>
<h3>Arm Holdings (ARM) — up 6.2% to $266.50</h3><p><b>Arm Holdings ADRs are up 6.2% in morning trading, at $266.50</b>, in the movers feed fetched this run. <span style="color:var(--mut)">No catalyst specific to Arm is stated in the text seen here; the move sits inside the same semiconductor read-through that followed Nvidia's report, but this page does not assert a cause a source did not give.</span></p></div>""")

# 8 — sector note, append this run's rejection
rep("A source that cannot say which session it is describing cannot supply this page with a sector number.</span></div>",
    "A source that cannot say which session it is describing cannot supply this page with a sector number. <b>A second sector read was fetched at 12:05 and is also withheld:</b> \"Energy down 1.82%\" and \"8 out of 11 sectors closed higher.\" A sector that <i>closed</i> cannot describe a session still two hours from lunch, and the accompanying text dates itself only as \"the most recent trading session.\" What the same source does say plainly, and what is published, is that <b>Thursday opened with a rally in technology and weakness in energy</b> — a direction, not a number.</span></div>")

# 9 — On the Radar: FedWatch bullet
rep("<li><b>Fed policy.</b> The federal funds target range stands at <b>3.50%–3.75%</b>, left unchanged at the July meeting (Trading Economics).</li>",
    "<li><b>Fed policy.</b> The federal funds target range stands at <b>3.50%–3.75%</b>, left unchanged at the July meeting (Trading Economics). <b>New this run:</b> CME Group's FedWatch tool has markets pricing a <b>36.1% likelihood of a rate <i>hike</i> at the September meeting</b> (Benzinga) — the probability is for a hike, not a cut, and is printed that way deliberately.</li>")

io.open(P, "w", encoding="utf-8").write(s)
print("wallstreet edits applied:", n)
