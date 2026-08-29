#!/usr/bin/env python3
"""Final read-through fixes: scope the verification claim honestly; add newly sourced Friday
single-stock percentages that sharpen a carried, vaguer figure."""
import io

MISS = []
def ed(t, old, new, label):
    if old not in t:
        MISS.append(label); return t
    return t.replace(old, new, 1)

p = 'wallstreet-briefing.html'
h = io.open(p, encoding='utf-8').read()

# 1) The 12:05 search returned the Dow LEVEL and the S&P/Nasdaq PERCENTS, not all three levels.
#    Say exactly that rather than "the same three figures".
h = ed(h,
 ('its official closes stand unchanged, <b>re-verified a tenth time at 12:05 PM</b> against a fresh\n'
  'search returning the same three figures'),
 ('its official closes stand unchanged, <b>re-verified a tenth time at 12:05 PM</b>. &#9888; <b>What that '
  'tenth check actually returned is narrower than the phrase suggests, so it is stated exactly:</b> a fresh '
  'search this run returned the <b>Dow level (53,560, &minus;9 points, &minus;0.02%)</b> and the '
  '<b>S&amp;P 500 and Nasdaq moves as percentages</b> (&ldquo;slid nearly 0.3%&rdquo;, &ldquo;declined by '
  '0.5%&rdquo;) &mdash; it did <b>not</b> restate the S&amp;P and Nasdaq index levels. Those two levels are '
  '<b>carried</b> from the editions that sourced them and are consistent with every percentage returned since. '
  'The three figures'),
 'ws-lead-scope')

# 2) Nvidia: carried "more than 3%" is now superseded by a sourced precise figure.
h = ed(h,
 ('The shares nonetheless fell more than 3% on Friday after Thursday\'s\n'
  'gain, which is carried from the prior edition\'s sourcing rather than restated this run.</p>'),
 ('The shares nonetheless fell on Friday after Thursday&rsquo;s gain. <b>Sharpened at 12:05 PM:</b> a market '
  'wrap fetched this run puts the Friday decline at <b>&minus;4.45%</b> and names Nvidia the session&rsquo;s '
  '<b>biggest single drag</b>. The carried figure was <b>&ldquo;more than 3%&rdquo;</b>; the two do not '
  'conflict &mdash; the newer one is simply <b>precise where the older one was a floor</b>, and it is the '
  'floor that is retired, not a contradiction that is resolved.</p>'),
 'ws-nvidia-precise')

# 3) New sourced detail on Friday's leaders and laggards — explicitly not a new move.
h = ed(h,
 'Neither is tagged as a mover.</div>',
 ('Neither is tagged as a mover. <b>Added at 12:05 PM &mdash; new precision on an old session, which is not '
  'the same thing as a new move.</b> A wrap fetched this run gives Friday&rsquo;s largest single-stock moves '
  'with figures this page had not carried: decliners <b>Nvidia &minus;4.45%</b>, <b>3M &minus;2.56%</b> and '
  '<b>Honeywell &minus;2.19%</b>; gainers <b>Amazon +4.02%</b>, <b>Salesforce +3.06%</b> and '
  '<b>Nike +3.02%</b>. &#9888; These are <b>Friday, August 28</b> closes. <b>None is tagged New</b>, because '
  'nothing moved &mdash; the tape has been shut throughout. Note that <b>Salesforce appears here as a Friday '
  'gainer</b> while the card below it records a <b>Thursday</b> spread: as with Broadcom and Intel, the two '
  'sit on different days and are <b>not netted</b>.</div>'),
 'ws-friday-movers-detail')

io.open(p, 'w', encoding='utf-8').write(h)
print('MISSES:', MISS if MISS else 'none')
