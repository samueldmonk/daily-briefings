#!/usr/bin/env python3
"""Wall Street page — 1:12 PM ET edition, Aug 31 2026. Content edits only."""
import io, sys

P = 'wallstreet-briefing.html'
h = io.open(P, encoding='utf-8').read()
orig = len(h)

# ---------------------------------------------------------------- 1. TLDR
old_tldr_start = h.find('<div class="tldr"><b>The Tape</b>')
assert old_tldr_start > 0
old_tldr_end = h.find('</div>', h.find('</span>', old_tldr_start)) + len('</div>')
NEW_TLDR = (
'<div class="tldr"><b>The Tape</b> <span>'
'<b>The mis-shelved recap has now been refused four times in one session, and on this pass it '
'stopped hedging and called Friday&rsquo;s numbers &ldquo;closing values&rdquo; for a day that is '
'still trading.</b> The same wrap dated <b>August 31</b> again returned <b>S&amp;P 500 7,711.76 '
'&minus;0.3%</b>, <b>Nasdaq Composite 26,402.42 &minus;0.5%</b> and <b>Dow 53,885.10, &minus;464 '
'points, &minus;0.9%</b> &mdash; two of them Friday&rsquo;s verified closes &mdash; presented as '
'a finished session at <b>roughly 1 PM ET</b>. <b>Refused in full for a fourth time.</b> '
'What the live tape shows instead: an <b>eighth rendering</b> of today&rsquo;s move giving the '
'<b>Dow down 315 points, or 0.6%</b>, and the <b>S&amp;P 500 off about half a percent</b>, with '
'<b>energy still the only S&amp;P sector higher</b> on the Strait of Hormuz escalation and '
'<b>utilities the drag</b> &mdash; a split now corroborated by a separate market-close-of-August '
'read headlined on exactly that contrast.'
'</span></div>')
h = h[:old_tldr_start] + NEW_TLDR + h[old_tldr_end:]

# ------------------------------------------------- 2. Demote prior Lead block
h = h.replace(
    '<h2 class="sec">The Lead</h2><div class="note" style="margin-bottom:14px">'
    '<span class="tag new">New &middot; 12:51 PM</span>',
    '<h2 class="sec">The Lead</h2>@@LEADSLOT@@<div class="note" style="margin-bottom:14px">'
    '<span class="tag">Carried &middot; Aug 31, 12:51 PM</span>', 1)
assert '@@LEADSLOT@@' in h

NEW_LEAD = (
'<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 1:12 PM</span> '
'<b>The refusal that has run all session went from mis-shelved to explicitly mislabelled, and the '
'label is the new evidence.</b> Asked plainly for today&rsquo;s index levels at <b>around 1 PM ET</b>, '
'the same wrap dated <b>August 31</b> returned its figures under the heading '
'<b>&ldquo;closing values for August 31, 2026&rdquo;</b>, with the explanatory note that '
'<b>&ldquo;the market had already closed for the day&rdquo;</b>: <b>S&amp;P 500 7,711.76, down 0.3%</b>; '
'<b>Nasdaq Composite 26,402.42, slipping 0.5% on weak performance by AI stocks</b>; '
'<b>Dow Jones Industrial Average 53,885.10, down 464 points or 0.9%</b>, described as ending a '
'<b>five-day winning streak</b>. <b>The New York session does not close until 4 PM ET.</b> '
'<b>Two of the three levels are Friday&rsquo;s verified closes, which this page carries verbatim</b>, '
'and the third matches neither Friday&rsquo;s verified <b>53,559.99</b> nor anything else this page '
'has seen. <b>Refused in full for a fourth time.</b><br><br>'
'&#9888; <b>What the fourth pass adds is that the claim is now falsifiable without any arithmetic '
'at all.</b> The first refusal (11:50) needed Friday&rsquo;s closes in hand to spot two levels '
'repeating; the third (12:51) needed only the return&rsquo;s own contradictory sector directions. '
'<b>This one asserts a completed session at a timestamp when the exchange is open</b>, which any '
'clock settles. <b>Three independent tests have now condemned the same source, and the cheapest of '
'them is the calendar.</b> Expect it to keep returning under every query shape until 4 PM ET.<br><br>'
'<b>The live session, from sources that date themselves.</b> A read fetched this run gives the '
'<b>S&amp;P 500 slipping 0.5%</b> with the <b>Dow down 315 points, or 0.6%</b>. &#9888; <b>That points '
'figure is new and it does reconcile</b> &mdash; <b>315 against Friday&rsquo;s verified 53,559.99 close '
'is 0.588%, which rounds to the stated 0.6%</b> &mdash; but <b>no level is stated alongside it and none '
'is derived</b>, so the page&rsquo;s standing rule holds and <b>still no index level is published for '
'the live session</b>. &#9888; <b>It is also the second distinct Dow points figure of the day</b>, '
'against the <b>~&minus;400 points</b> fetched at 11:50, and a <b>third Dow percentage</b> alongside '
'<b>&minus;0.60%</b> and <b>&minus;0.64%</b>; <b>all printed, none adopted.</b> Today&rsquo;s S&amp;P '
'family is unchanged at <b>&minus;0.43% / &minus;0.45% / &minus;0.47% / &minus;0.5% / &minus;0.55%</b>.'
'<br><br>'
'<b>The sector split gained its own headline, which is corroboration rather than news.</b> A market '
'read published this run is headlined on <b>energy stocks leading in a subdued final trading day of '
'August with utilities under pressure</b> &mdash; the same two-sided story this page has carried since '
'11:31, now stated as the day&rsquo;s organising fact by a source that reached it independently. '
'<b>Energy remains the only S&amp;P sector higher</b>, up about <b>2%</b> on the session and more than '
'<b>6%</b> for the month; <b>utilities are down 1.6%</b> on the two California wildfire-liability names. '
'&#9888; <b>No new figure is taken from that headline</b> &mdash; it corroborates a direction this page '
'already had, and a corroboration is recorded as one rather than promoted into a finding.</div>')
h = h.replace('@@LEADSLOT@@', NEW_LEAD, 1)

# ---------------------------------------------------- 3. Movers note (prepend)
anchor = '<h2 class="sec">Movers &amp; Drivers</h2>'
assert anchor in h
MOVERS_NOTE = (
'<div class="note" style="margin-bottom:14px"><span class="tag new">New &middot; 1:12 PM</span> '
'<b>No new mover cleared the bar this run, and saying so is the finding.</b> A movers sweep fetched '
'at <b>1 PM ET</b> returned the same four names this page already carries with the same figures &mdash; '
'<b>Edison International &minus;22.3%</b> on California&rsquo;s legislature failing to pass wildfire '
'liability reform, <b>SAIC +4.6%</b> in early trading on better-than-expected second-quarter results, '
'<b>CrowdStrike +3.9%</b> as <b>Fal.Con 2026</b> opened in Las Vegas, and <b>Tesla +3.7%</b> on Optimus '
'entering the production phase at Fremont. <b>Every one is a re-confirmation, not an addition.</b> '
'&#9888; <b>The same return carried the refused wrap&rsquo;s premarket set</b> &mdash; '
'<b>S&amp;P 500 &minus;0.27%, Nasdaq 100 &minus;0.20%, Dow &minus;0.25%, Russell 2000 &minus;0.19%</b>, '
'explicitly labelled <b>premarket</b> &mdash; <b>recorded and not published as the live session</b>, '
'because a premarket percentage is a different measurement from a midday one and this page spent the '
'8:10 AM edition learning that. <b>Chart of the Day stays on Edison International</b>: nothing fetched '
'this run moves further with an identified cause.</div>')
h = h.replace(anchor, anchor + MOVERS_NOTE, 1)

assert len(h) > orig
io.open(P, 'w', encoding='utf-8').write(h)
print('wallstreet-briefing.html %d -> %d bytes' % (orig, len(h)))
