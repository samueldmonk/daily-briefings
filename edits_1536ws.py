# -*- coding: utf-8 -*-
import io
f='wallstreet-briefing.html'
s=io.open(f,encoding='utf-8').read()
FAIL=[]
anchor='<h2 class="sec">On the Radar</h2>'
assert anchor in s

BLOCK = ('<p><span class="t new" style="margin-right:6px">New</span>'
'<b>Friday&rsquo;s CPI now has an energy problem attached to it, and the two figures are the only new numbers this desk found today.</b> '
'A commentary piece dated <b>today, 7 September</b>, breaks the inflation print the whole week is pointed at into components, and the energy side is '
'where the pressure is: the <b>energy component of CPI rose 14.7% year over year in July</b>, and <b>gasoline specifically rose 24.6% year over year</b>. '
'<span class="mut">Both are <b>July</b> readings and are printed as July readings &mdash; they are <b>not</b> a forecast of Friday&rsquo;s August number and are not presented as one. '
'They sit against the nowcast this page already carries, <b>3.38% headline year over year and 0.36% month over month as of 4 September</b>, which is unchanged and is <b>not</b> re-tagged; '
'the same piece restates <b>Fed Governor Christopher Waller</b>&rsquo;s line that the September decision could hinge on this print and that a <b>hike</b> is on the table if it runs hot, '
'which this page has carried since the morning. The energy components are the whole of what is new. '
'Given the oil story this page is already leading with &mdash; Brent around $97 and a six-week high &mdash; a 14.7% energy contribution is the mechanism by which today&rsquo;s only live market '
'reaches Friday&rsquo;s only live data point, which is why it is worth a tag on a day the exchanges were shut.</span></p>\n'
'<p class="note"><b>Two settlement prices in that same return are refused.</b> <span class="mut">It gives <b>WTI settling at $91.30</b> and <b>Brent at $95.52</b> with <b>no date attached to either</b>. '
'This page holds <b>Brent&rsquo;s Friday settlement at $96.28</b>, sourced and carried all day &mdash; <b>$95.52 is 76 cents below it</b> &mdash; and today produced no settlement at all, because '
'<b>ICE and CME publish no Monday settlement for a U.S. holiday session</b>, which this page also already says. An undated settlement that matches neither Friday nor today is a reading from some '
'other session, and it is <b>not printed as either</b>. &#9733; <b>A price with no date is not a price. The refusal is printed here rather than left silent, because the next edition will meet the '
'same two numbers and should not have to re-derive the reason.</b></span></p>\n')

s = s.replace(anchor, anchor + BLOCK, 1)
io.open(f,'w',encoding='utf-8').write(s)
print("ok")
