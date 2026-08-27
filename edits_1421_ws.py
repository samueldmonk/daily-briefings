# -*- coding: utf-8 -*-
P='/tmp/db_1787854887/wallstreet-briefing.html'
s=open(P,encoding='utf-8').read()
def rep(old,new,n=1):
    global s
    c=s.count(old); assert c==n, "count %d want %d :: %s"%(c,n,old[:100]); s=s.replace(old,new)

rep('<span class="tag new">Updated &middot; 12:38 PM ET</span>','<span class="tag">Carried &middot; 12:38 PM ET</span>') if '<span class="tag new">Updated &middot; 12:38 PM ET</span>' in s else None
s=s.replace('<span class="tag new">Updated · 12:38 PM ET</span>','<span class="tag">Carried · 12:38 PM ET</span>')
s=s.replace('<span class="tag new">Updated · 12:38</span>','<span class="tag">Carried · 12:38</span>')
s=s.replace('<span class="tag new">New · 12:38</span>','<span class="tag">Carried · 12:38</span>')

rep("The tech-led rally has re-accelerated into the afternoon &mdash; the latest read has the Nasdaq Composite up 400.29 points (+1.53%) and the Dow up 208.48 points (+0.39%), both above the 12:05 tallies, with the S&amp;P 500 still holding a 0.4% gain and Okta still the biggest single-stock mover."
 if "The tech-led rally has re-accelerated into the afternoon &mdash;" in s else
 "The tech-led rally has re-accelerated into the afternoon — the latest read has the Nasdaq Composite up 400.29 points (+1.53%) and the Dow up 208.48 points (+0.39%), both above the 12:05 tallies, with the S&amp;P 500 still holding a 0.4% gain and Okta still the biggest single-stock mover.",
 "The S&amp;P 500's gain has doubled to 0.8% on the afternoon read and Bloomberg has technology as the only sector advancing as of 1:25 PM ET — the first time-stamped figure any source has given this page today — with the Nasdaq Composite up about 1.5% and the Dow up about 0.4%.")

rep("<h3>The rally re-accelerates after lunch: the Nasdaq Composite adds more than 400 points — as of ~12:38 PM ET</h3>",
    "<span class=\"tag new\">Updated · 2:21 PM ET</span>\n<h3>Technology is carrying the tape by itself, and the S&amp;P 500's gain has doubled to 0.8% — as of ~2:21 PM ET</h3>")

anchor='<p style="margin:0 0 10px">Into the early afternoon, US stocks are <b>climbing again</b>'
newp=('<p style="margin:0 0 10px"><b>New at 2:21 — a fifth index read of the session, and it is percentage-only.</b> '
 'Yahoo Finance and TheStreet\'s August 27 coverage both have the <b>Dow up 0.4%</b>, the <b>S&amp;P 500 up 0.8%</b> and the '
 '<b>Nasdaq Composite up 1.5%</b>. The Nasdaq and Dow figures sit inside the rounding band of the 12:38 reads (+1.53% and +0.39%), '
 'so the large-cap tape is broadly where it was after lunch. <b>The S&amp;P 500 line is the one that has moved:</b> it was quoted '
 'at 0.4% in every read this page carried from the open through 12:38, and is now quoted at double that. '
 '<span style="color:var(--mut)">Neither source published point changes alongside these percentages, so no point figures are printed for this read.</span> '
 '<b>And for the first time this session a source has stamped a time on its number:</b> Bloomberg reports the S&amp;P 500 <b>up 0.8% at 1:25 p.m. in New York</b>, '
 'which both corroborates the higher read and dates it. <span style="color:var(--mut)">A separate Bloomberg item carrying "S&amp;P 500 and Nasdaq 100 gained 0.4% and 0.7%, the Dow inched lower" '
 'is <b>futures</b> coverage published before the bell, and is not published here as a current read.</span></p>\n')
rep(anchor, newp+anchor)

rep("<b>No source stamped its figures with a time</b>, so no level is asserted in this section; levels live in the Weekly Scorecard.",
    "<b>None of those four sources stamped its figures with a time</b>, so no level is asserted in this section; levels live in the Weekly Scorecard. "
    "<span style=\"color:var(--mut)\"><b>Struck at 2:21:</b> this page said flatly that <i>no</i> source had stamped a time on its figures. That is no longer true — "
    "Bloomberg's 1:25 p.m. read, above, is stamped. The claim is narrowed to the four sources it was actually about.</span>")

rep("<b>Four index reads have now been taken across this session, and all four reconcile to the same prior close.</b>",
    "<b>Four point-and-percent index reads have been taken across this session, and all four reconcile to the same prior close.</b> "
    "<span style=\"color:var(--mut)\">(The 2:21 read above is percentage-only, so it is not part of this ladder.)</span>")

mv='<h2 class="sec">Movers &amp; Drivers</h2>\n<div class="cards">\n'
card=('<div class="card"><span class="tag new">New · 2:21</span><span class="tag acc">Movers board</span>\n'
 '<h3>The afternoon movers board is a <i>lower</i> set than the one that arrived at 12:38 — and both are printed</h3>'
 '<p><b>New at 2:21:</b> a fresh movers roundup for August 27 puts <b>Okta up 17.4%</b> after a second-quarter beat and an upward revision to full-year guidance, '
 '<b>Salesforce up 10.4%</b> on its beat and an expanded partnership with AI lab Anthropic, <b>Nvidia up 9%</b> after saying revenue will grow about 70% next fiscal year, '
 'and <b>CrowdStrike up 9%</b>. The same coverage notes an <b>ETF tracking software firms climbed 6.5%</b> on Salesforce\'s forecast. '
 '<b>All four sit below the reads this page carried at 12:38</b> — Okta 26.17%, Salesforce 21.04%, Nvidia 9.48%, CrowdStrike 17.93% — '
 'and the gap runs to nearly nine points on CrowdStrike. <span style="color:var(--mut)">This page does not treat the newer set as a correction of the older one and does not average them: '
 'both are single-source snapshots of a fast tape, the full ladders are on the individual cards below, and nothing has been overwritten. '
 'Bloomberg\'s 1:25 p.m. coverage adds a third Nvidia read — <b>up 7%</b> — alongside <b>Micron, Marvell, Sandisk, Palo Alto and GE Vernova adding between 6% and 3%</b> '
 'on the read-through from Nvidia\'s outlook.</span></p></div>\n\n')
rep(mv, mv+card)

rep("<h3>Okta (OKTA) — up 26.17%, still the session's biggest mover</h3>",
    "<h3>Okta (OKTA) — quoted at 26.17%, 19% and now 17.4%, and the newest read is the smallest</h3>")
rep("<span style=\"color:var(--mut)\">The 9:05 edition printed no percentage for Okta because none had been stated; two have now been, and they disagree.</span>",
    "<span style=\"color:var(--mut)\">The 9:05 edition printed no percentage for Okta because none had been stated; three have now been, and they disagree. "
    "<b>New at 2:21:</b> a fresh roundup quotes <b>Okta up 17.4%</b> — below both earlier figures — attributing the move to a second-quarter beat and an upward revision to full-year guidance. "
    "The three reads span nearly nine percentage points and this page adopts none of them.</span>")

rep("<b>Updated at 12:38:</b> Salesforce has closed much of the gap on a fresh read of <b>+21.04%</b>, which sits between Okta's two figures; the chart symbol is left on Okta because no read seen this run puts another name above 26.17%.",
    "<b>Updated at 12:38:</b> Salesforce closed much of the gap on a fresh read of <b>+21.04%</b>, which sits between Okta's two figures. "
    "<b>Updated at 2:21, and the reasoning has narrowed:</b> the newest roundup puts <b>Okta at 17.4%</b> — <i>below</i> Salesforce's 21.04% — "
    "so it is no longer true that Okta leads on every pairing of reads this page holds. What is still true, and is the basis for keeping the symbol here: "
    "<b>Okta is first within each internally consistent single-source set</b> (it leads Salesforce 17.4% to 10.4% on this run's roundup), and "
    "<b>no name has been quoted above Okta's 26.17% high at any point today</b>.")

rep("— a direction, not a number.</span>",
    "— a direction, not a number.</span> <b>New at 2:21 — a sector statement with a time on it, and it is published.</b> "
    "Bloomberg reports that <b>technology was the only sector to advance in the S&amp;P 500</b>, which was <b>up 0.8% at 1:25 p.m. in New York</b>, with "
    "<b>Micron, Marvell, Sandisk, Palo Alto and GE Vernova adding between 6% and 3%</b> on the read-through from Nvidia's outlook. "
    "That is the first sector claim this page has been able to publish today with a timestamp attached — which is precisely what the rejected tables lacked. "
    "<span style=\"color:var(--mut)\"><b>And a third rejection:</b> a table offering \"Energy declined 1.82%\" was fetched again this run with no session date beyond \"the day\" — "
    "the same figure, from the same shape of source, that this page withheld at 12:05. It is withheld again. <b>A number does not become sourced by being offered three times.</b></span>")

rep("$81.36–$81.63</td>","$81.36–$82.86</td>")
rep("Two reads this run, both for Aug 27 and both printed:", "<b>Three reads for August 27, all printed and none averaged:</b>")
rep("in the early New York session (Benzinga).", "in the early New York session (Benzinga); and, <b>new at 2:21</b>, <b>$82.86, down 0.08%</b> (ConvexTrade).")
rep("Investing.com showed a WTI futures range of $81.44–$82.15.", "Investing.com showed a WTI futures range of $81.44–$82.15. <b>Brent</b> is quoted at <b>$87.65</b> for August 27 (Eastern Herald) — the first Brent read this page has carried today. <span style=\"color:var(--mut)\">The three WTI reads disagree on level by about a dollar and a half; all three are lower on the day.</span>")

rep("<li><b>HP (HPQ)</b> joins Nvidia, Salesforce and CrowdStrike on this week's earnings watchlist.</li>",
    "<li><b>New at 2:21 — July PCE, and it ran hot.</b> The PCE price index rose <b>0.2% on the month</b> against expectations of <b>0.1%</b>, "
    "with annual inflation at <b>3.7%</b> versus a <b>3.6%</b> forecast (Trading Economics). That is the backdrop to the September pricing below, which is priced for a <i>hike</i>.</li>\n"
    "<li><b>HP (HPQ)</b> joins Nvidia, Salesforce and CrowdStrike on this week's earnings watchlist.</li>")

rep("The item is restored, and the standing corrections file has been amended so the mistake is not repeated.</span></li>",
    "The item is restored, and the standing corrections file has been amended so the mistake is not repeated. "
    "<b>Corroborated at 2:21:</b> Yahoo Finance and TheStreet both frame Thursday's session as investors <i>awaiting</i> the Fed's Jackson Hole gathering — "
    "which places the symposium ahead of this tape, not behind it.</span></li>")

open(P,'w',encoding='utf-8').write(s); print("WS OK",len(s))
