# -*- coding: utf-8 -*-
import io,re
f='index.html'; s=io.open(f,encoding='utf-8').read()
blocks=list(re.finditer(r'<h3>.*?</p>',s,re.S))
assert len(blocks)==3, len(blocks)

CY=('<h3>The one new cyber item today is a Chrome update that is already older than the one you have installed &mdash; '
'and a print server still owns the only live federal deadline</h3>\n'
'<p><b>Google&rsquo;s 26-fix Chrome release closed two critical use-after-free flaws</b> &mdash; <b>CVE-2026-84353</b> in Shared Tab Groups '
'and <b>CVE-2026-84352</b> in WebGL, both reachable from a crafted page and both escaping the sandbox &mdash; plus a high-severity '
'input-validation flaw, <b>CVE-2026-84325</b>. All three are fixed in <b>152.0.7977.75</b>, and the briefing has carried '
'<b>152.0.7977.82/.83</b> since Friday as the fix for the exploited V8 zero-day <b>CVE-2026-85046</b>: <b>.82 is the later build</b>, so a '
'desk already patched for the zero-day is covered for these. None of the three is exploited or in KEV, and none carries a countdown. '
'<b>PaperCut NG/MF remains the most urgent box</b> &mdash; hands-on human intrusion, and the only federal deadline on the page that has not '
'elapsed, <b>14 September</b>. Tomorrow is Patch Tuesday, with four CVEs pre-published through MSRC and <b>ShieldBreak</b> still unpatched.</p>')

WS=('<h3>Every tape on the page has now stopped &mdash; and Friday&rsquo;s CPI gains an energy problem</h3>\n'
'<p><b>U.S. stock and bond markets are shut all day for Labor Day and reopen at 9:30&nbsp;AM ET Tuesday</b>, and the oil futures that were '
'still trading have all halted since: <b>ICE Brent at about 1:30&nbsp;PM ET</b> and <b>CME crude at about 2:30&nbsp;PM ET</b> on a relayed '
'schedule, after CME&rsquo;s equity-index halt at <b>1:00&nbsp;PM ET</b> &mdash; so every symbol on the briefing&rsquo;s live ticker has been '
'showing a last matched price for more than an hour. <b>The one new item is a component breakdown of the print the week is pointed at:</b> '
'the <b>energy component of CPI rose 14.7% year over year in July</b> and <b>gasoline rose 24.6%</b> &mdash; July readings, not a forecast of '
'Friday&rsquo;s August number &mdash; which is how today&rsquo;s only live market, <b>Brent around $97 and at a six-week high</b>, reaches '
'Friday&rsquo;s only live data point. <b>Two undated settlement prices in the same return are refused</b>, and no single Brent level is '
'asserted as the price.</p>')

MMA=('<h3>No new MMA item today &mdash; and the schedule article promising one is out of date</h3>\n'
'<p><b>Fresh sweeps of the day&rsquo;s UFC news returned only material the briefing already carries</b>, so nothing is tagged New: the full '
'<b>12 September</b> Glendale card, <b>Roberto Soldic&rsquo;s</b> signing and debut against <b>Khaos Williams</b>, the <b>UFC&nbsp;334</b> '
'opener at Madison Square Garden, <b>Brendan Allen vs. Christian Leroy Duncan</b> on 10 October, and Paddy Pimblett&rsquo;s December line. '
'<b>Nat&aacute;lia Silva vs. Wang Cong</b> for Shevchenko&rsquo;s vacated women&rsquo;s flyweight belt still leads the briefing, on a '
'<b>UFC&nbsp;332</b> card now finalised at twelve bouts. <b>One headline is refused:</b> a living event-schedule article advertises '
'&ldquo;Volkanovski vs. Lopes 2&rdquo; as upcoming when that rematch was <b>UFC&nbsp;325 in January</b>, so the Gaethje&ndash;Pimblett booking '
'beside it is not printed either. Saturday&rsquo;s Paris card left <b>Dan Hooker</b> on three straight losses, the longest run of his career.</p>')

for m,new in zip(reversed(blocks),[MMA,WS,CY]):
    s = s[:m.start()] + new + s[m.end():]
io.open(f,'w',encoding='utf-8').write(s)
print("ok")
