# -*- coding: utf-8 -*-
import io
f='wallstreet-briefing.html'; s=io.open(f,encoding='utf-8').read()
old=('as the 2:15 edition publishes at about <b>2:15&nbsp;PM ET</b>, the 1:00&nbsp;PM ET halt is '
     '<b>about an hour and a quarter in the past</b>, so the equity-index quotes in the tape above are '
     '<b>the last matched prices of a shortened holiday session, not a live market</b> &mdash; a quiet screen, '
     'which is not the same thing as a flat one.')
assert old in s, 'anchor missing'
new=('that sentence was true when it was written and false ninety minutes later. As this <b>3:35&nbsp;PM</b> edition publishes, '
     'the 1:00&nbsp;PM ET halt is <b>about two and a half hours in the past</b> &mdash; and it is no longer even the most recent of the '
     'day&rsquo;s three halts, ICE Brent having stopped at about <b>1:30&nbsp;PM ET</b> and CME crude at about <b>2:30&nbsp;PM ET</b>. '
     'The equity-index quotes in the tape above are <b>the last matched prices of a shortened holiday session, not a live market</b>, '
     'and by now every other symbol on that tape is too &mdash; a quiet screen, which is not the same thing as a flat one. '
     '<b>This is the fourth consecutive edition in which a futures-halt sentence has had to be rewritten against the clock rather than '
     'against its source</b>, which is why the elapsed figure is now restated every run instead of inherited.')
s=s.replace(old,new,1)
io.open(f,'w',encoding='utf-8').write(s)
print('ok')
