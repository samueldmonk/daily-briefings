#!/usr/bin/env python3
"""Wall Street content edits, 1:41 PM ET edition, Aug 31 2026."""
import io, re
p = 'wallstreet-briefing.html'
h = io.open(p, encoding='utf-8').read()

# demote previous New tags on this page
h = h.replace('<span class="tag new">New &middot; 1:12 PM</span>',
              '<span class="tag">Carried &middot; Aug 31, 1:12 PM</span>')

LEAD = (
'<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 1:41 PM</span> '
'<b>The first live reading of the day that carries its own clock, and it changes which index is worst.</b> '
'A market read fetched this run states that <b>as of around 1:31 PM EDT the Dow Jones Industrial Average '
'slipped 0.5%, the S&amp;P 500 declined 0.4% and the Nasdaq Composite fell 0.3%</b>. '
'&#9888; <b>This is the first intraday set all session to state its own as-of time to the minute</b>, which is '
'the single property this page has been asking of every figure it refused. It is published as a timestamped '
'snapshot rather than as the session&rsquo;s move.<br><br>'
'&#9888; <b>It also inverts the running order.</b> Every earlier rendering today put the Nasdaq at or below the '
'S&amp;P; this one has the <b>Nasdaq shallowest at &minus;0.3%</b> and the <b>Dow deepest at &minus;0.5%</b>. '
'<b>That is not a contradiction of the earlier reads &mdash; it is a later moment in an open session</b>, and the '
'direction of travel it implies is a tech bid firming into the afternoon while the Dow&rsquo;s decline holds. '
'<b>The S&amp;P family now reads &minus;0.4% / &minus;0.43% / &minus;0.45% / &minus;0.47% / &minus;0.5% / &minus;0.55% '
'across the session; the Dow reads &minus;0.5% / &minus;0.6% / &minus;0.60% / &minus;0.64%.</b> '
'<b>All printed, none adopted, and no index level is published for the live session.</b><br><br>'
'&#9888; <b>The refused wrap returned a fifth and a sixth time, and it is now riding inside otherwise-good returns.</b> '
'The same figures &mdash; <b>S&amp;P 500 7,711.76 &minus;0.3%</b>, <b>Nasdaq 26,402.42 &minus;0.5%</b>, '
'<b>Dow 53,885.10, &minus;464 points, &minus;0.9%</b> ending a <b>five-day winning streak</b>, with '
'<b>PayPal &minus;12.7%</b> as the major loser &mdash; came back once on its own and once <b>appended to the very '
'return that carried the good 1:31 PM snapshot</b>, as a trailing sentence beginning <b>&ldquo;by market close for '
'the day&rdquo;</b>. <b>Refused again, both times.</b> '
'<b>The lesson of the sixth refusal is narrower than the first five: a return is not clean or dirty as a whole. '
'The timestamped sentence and the mis-shelved one arrived together, and each had to be judged on its own.</b><br><br>'
'<b>The cause is unchanged and better sourced.</b> Reporting fetched this run attributes the decline to '
'<b>U.S. forces striking Iranian rocket launchers on the Strait of Hormuz on Sunday</b> &mdash; described as the first '
'U.S. military action against Iran in about a month &mdash; with <b>both sides far apart on a ceasefire that would '
'fully reopen the strait</b>, lifting energy prices and <b>rate-hike expectations for September</b>. '
'&#9888; <b>One variant recorded, not adopted:</b> a separate wire describes the target as <b>an Iranian island in '
'the Strait of Hormuz</b> rather than rocket launchers on it. <b>Both renderings are printed; neither is used to '
'correct the other</b>, because nothing fetched this run reconciles them.</div>'
)
anchor = '<h2 class="sec">The Lead</h2>'
assert anchor in h
h = h.replace(anchor, anchor + LEAD, 1)

# ------------------------------------------------------------------ MOVERS
MOV = (
'<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 1:41 PM</span> '
'<b>A second wildfire-liability name arrives with a percentage, and it makes the utilities line a pair rather than '
'an outlier.</b> A sector read fetched this run names <b>PG&amp;E Corporation (NYSE:PCG) down 20.0%</b> alongside '
'<b>Edison International down 21.0%</b>, both <b>following regulatory updates regarding wildfire liabilities</b>, and '
'states that <b>PG&amp;E dragged down the Utilities Select Sector SPDR (XLU) after new California legislation left a '
'lot of uncertainty about utilities&rsquo; exposure to wildfire liabilities</b>. '
'&#9888; <b>PCG at &minus;20.0% is a new figure; this page has carried PG&amp;E at &minus;16.7% since midday.</b><br><br>'
'&#9888; <b>Two figures for each name, and this page treats the pair differently from the Elastic case.</b> '
'<b>EIX reads &minus;22.3% earlier and &minus;21.0% now; PCG reads &minus;16.7% earlier and &minus;20.0% now.</b> '
'Neither pair rounds together, which under this page&rsquo;s own rule would make them competing claims. '
'<b>The rule does not apply here, and the reason is the clock:</b> Elastic&rsquo;s two figures described a '
'<b>finished close</b>, which has exactly one correct value, while these describe an <b>open session</b>, where a '
'percentage is entitled to move between two reads. <b>Both moments are printed with their moment attached, and the '
'earlier figures are not withdrawn.</b> <b>What the two pairs agree on is the shape: EIX fell further than PCG, and '
'they moved together.</b><br><br>'
'<b>Breadth, for the first time today.</b> The same read states that <b>nearly 65% of issues in U.S. markets are '
'declining</b>, with <b>energy the clear winner among sectors</b> &mdash; still the <b>only S&amp;P 500 sector in '
'positive territory</b>, <b>up about 2%</b> on the session and <b>more than 6% for the month</b>, lifting '
'<b>Chevron and Exxon</b>; <b>utilities down 1.6%</b> as one of the two biggest laggards. '
'&#9888; <b>Chart of the Day stays on Edison International</b> &mdash; PG&amp;E is the corroborating name here, not '
'the larger move.</div>'
)
a2 = '>Movers &amp; Drivers</h2>'
assert a2 in h
h = h.replace(a2, a2 + MOV, 1)

# ------------------------------------------------------------------ RATES
RATES = (
'<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 1:41 PM</span> '
'<b>A live curve reading finally clears the bar, and it clears it on the strength of the number it cites as its '
'baseline.</b> A read fetched this run states that <b>the yield on the two-year Treasury, which closely tracks '
'expectations about Fed moves, rose to 4.35% from 4.34% late Friday</b>, and that <b>the yield on the 10-year '
'Treasury rose to 4.76% from 4.73% late Friday</b>. '
'&#9888; <b>Both stated baselines match this table to the basis point</b> &mdash; the table carries Friday&rsquo;s '
'<b>4.34%</b> two-year and <b>4.73%</b> ten-year from dated sources. <b>A live figure that names the prior close this '
'page already holds is anchored to the right session</b>, which is precisely what the <b>undated 4.72%</b> refused '
'seven times could never do, and what the rounded <b>&ldquo;around 4.7%&rdquo;</b> could only do approximately. '
'<b>This is the first live yield reading this page has been able to place on its timeline.</b><br><br>'
'&#9888; <b>It is printed here and the table is still not overwritten</b>, because the table&rsquo;s rows are '
'<b>official closes</b> and the session is open; <b>the 4.76% and 4.35% are today&rsquo;s live levels, the 4.73% and '
'4.34% remain Friday&rsquo;s closes, and the three-basis-point move in the ten-year is the news.</b> '
'<b>It also confirms the direction the &ldquo;around 4.7% after three consecutive sessions of gains&rdquo; reading '
'established: up.</b><br><br>'
'<b>Crude, and a refusal that now resolves in favour of the figure already carried.</b> The same run gives '
'<b>Brent crude just over $92 a barrel</b> and <b>West Texas Intermediate near $86</b>, after a '
'<b>3% jump as the U.S. and Iran resumed military attacks</b>; a separate return has <b>global benchmark crude '
'gaining 2% at the open</b>. &#9888; <b>The &ldquo;near $86&rdquo; WTI figure is now stated by a second source this '
'run, which settles the $80 reading refused at 12:51 against it</b> &mdash; <b>the $80 is not printed as a level and '
'the $86 stands as the corroborated one.</b> <b>Brent just over $92 is new to this page.</b></div>'
)
a3 = 'Rates, Bonds &amp; Commodities</h2>'
assert a3 in h
h = h.replace(a3, a3 + RATES, 1)

# ------------------------------------------------------------------ TLDR
new_tldr = (
'<div class="tldr"><b>The Tape</b> <span>The first live reading of the day to state its own clock &mdash; '
'the Dow off 0.5%, the S&amp;P 500 off 0.4% and the Nasdaq off 0.3% as of about 1:31 PM ET &mdash; arrived in the '
'same return as the mis-shelved recap this page has now refused six times, and a live two-year and ten-year yield '
'cleared the bar for the first time by naming Friday&rsquo;s closes as their baseline.</span></div>'
)
h = re.sub(r'<div class="tldr">.*?</div>', new_tldr, h, count=1, flags=re.S)

io.open(p, 'w', encoding='utf-8').write(h)
print('ws edits applied,', len(h), 'bytes')
