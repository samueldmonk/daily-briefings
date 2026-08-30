# -*- coding: utf-8 -*-
import sys, io, os
D = sys.argv[1]
def rd(f): return io.open(os.path.join(D,f), encoding='utf-8').read()
def wr(f,s): io.open(os.path.join(D,f),'w',encoding='utf-8').write(s)
fails=[]
def sub(s, old, new, label):
    if s.count(old)!=1:
        fails.append('%s: count=%d' % (label, s.count(old))); return s
    return s.replace(old,new)

w = rd('wallstreet-briefing.html')
anchor = '<h2 class="sec">The Lead</h2>\n<p><span class="tag new">New &middot; 3:36 PM</span> <b>A twenty-third verification, and this run the interesting number is not a price but a date.</b>'
newblock = ('<h2 class="sec">The Lead</h2>\n'
 '<p><span class="tag new">New &middot; 4:06 PM</span> <b>The hawkish read finally arrives in Warsh&rsquo;s own sentences &mdash; and a fourth Friday index number is recorded without being promoted.</b> '
 'Every edition since Friday has described the Jackson Hole address as hawkish on the strength of what coverage said about it. A report fetched this run quotes the Chair directly on both halves of the argument: he reaffirmed that the Fed&rsquo;s 2% inflation goal is <b>&ldquo;a firm, fixed target&rdquo;</b>, and he placed <b>&ldquo;responsibility for 65 months of sustained, elevated inflation&hellip; squarely with the central bank&rdquo;</b>. '
 'Read together those are an argument about <b>credibility</b> rather than about any single data print &mdash; a different claim from &ldquo;inflation is running hot&rdquo;, and one that helps explain why the pricing moved as far as it did on a speech containing no new data. This page already carried one Warsh sentence, on the summer PCE and CPI readings; <b>these are additional, not a replacement for it</b>.</p>\n'
 '<p>&#9888; <b>A fourth Friday index figure arrived, and it is not a fourth reading of the three this page publishes.</b> The same sweep returned the <b>Nasdaq 100</b> closing Friday at <b>29,433.43, down 0.70%</b>. '
 'The Weekly Scorecard below tracks the <b>Nasdaq Composite</b>, which closed <b>26,402.42, &minus;0.52%</b> &mdash; a different index with a different membership, so the two figures do not compete and <b>neither corrects the other</b>. It is recorded here precisely because a 0.70% decline sitting beside a 0.52% one invites the substitution this page keeps refusing to make: <b>the 100 is not promoted into the Composite row</b>, and no line below has been changed by it. Re-confirmed in the same sweep, with one figure sharpened: <b>WTI $83.44, &minus;0.11%</b> alongside <b>Brent $88.29, &minus;0.26%</b>.</p>\n'
 '<p><b>One forward-looking read is printed as attribution and not as a forecast.</b> An analyst reading of the same speech, fetched this run, holds that a hike <b>probably will not come in September but will arrive by October or December</b>. That is one interpretation of a question two venues already answer differently on this page &mdash; CME at 57/43 for a hike, Polymarket and Kalshi both at 52% for a hold &mdash; and it is <b>attributed rather than adopted</b>, for an eleventh consecutive read. <b>The FOMC date is unchanged and not in dispute: September 16.</b></p>\n'
 '<p><span class="tag new">New &middot; 3:36 PM</span> <b>A twenty-third verification, and this run the interesting number is not a price but a date.</b>')
w = sub(w, anchor, newblock, 'ws lead')
wr('wallstreet-briefing.html', w)

m = rd('mma-briefing.html')
old331 = '<b>13 fights</b> total; prelims 6 PM ET, main card 9 PM ET, Paramount+. <b>No betting line for this card was\nstated by any source seen this run, so none is printed.</b>'
new331 = ('<b>13 fights</b> total; prelims 6 PM ET, main card 9 PM ET, Paramount+. '
 '&#9888; <b>A start-time conflict is recorded at 4:06 PM and not resolved.</b> A schedule aggregator fetched this run puts the UFC 331 main card at <b>5 PM ET</b>, where this page carries <b>9 PM ET</b> from its earlier sourcing. '
 '<b>Neither is adopted over the other</b> &mdash; an aggregator listing a month of events at once is not the promotion&rsquo;s own page, and a Los Angeles card can plausibly be listed either way depending on whether the schedule is quoting local or Eastern time. <b>The date, venue and card are unaffected by the disagreement</b>, and only the start time is in question. '
 '<b>No betting line for this card was stated by any source seen this run, so none is printed.</b>')
m = sub(m, old331, new331, 'mma 331')
wr('mma-briefing.html', m)
print('FAILS:', fails if fails else 'none')
