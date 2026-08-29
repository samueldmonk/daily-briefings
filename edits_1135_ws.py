F='wallstreet-briefing.html'
t=open(F).read()
E=[]
def rep(n,o,x): E.append((n,o,x))

rep('tldr',
 'and a third read on the September rate call points the same way as the first two: the odds of a hike were put at about one in three before Warsh spoke at Jackson Hole and above 50/50 after, against a prediction market&rsquo;s 48%, with next Friday&rsquo;s payrolls report the next test &mdash; and that report now carries two differently-sourced forecasts, +58,000 and +90,000, against a July print that went backwards.',
 'and the &ldquo;one in three&rdquo; pre-speech figure on the September rate call now has a date and an origin: reporting from mid-August puts the same reading at roughly 30% odds of a hike against a near-70% chance of a pause, after Goldman Sachs called a September move &ldquo;extremely unlikely&rdquo; &mdash; which also puts this page&rsquo;s carried, undated &ldquo;above 70% by December&rdquo; line in conflict with a dated report that December pricing had already slipped into 2027, so that line is now marked contested rather than repeated.')

rep('updated','Updated <span id="updated">10:50 AM ET</span>','Updated <span id="updated">11:35 AM ET</span>')
rep('freshline','>Data as of 11:05 AM ET','>Data as of 11:35 AM ET')

rep('reverify',
 're-verified a seventh time at 10:50 AM</b> against a fresh\nsearch returning the same three figures',
 're-verified a ninth time at 11:35 AM</b> against a fresh\nsearch returning the same three figures')

rep('movers',
 'No figure on this movers board changed at 11:05 AM either</b>, and none can while the tape is shut.',
 'No figure on this movers board changed at 11:35 AM either</b>, and none can while the tape is shut.')

rep('ratesrow',
 '<b>&gt;70%</b> odds of a hike by December.',
 '&#9888; <b>Contested at 11:35 AM:</b> an earlier edition carried <b>&gt;70% odds of a hike by December</b>, undated; a dated mid-August report says traders had moved a fully-priced December hike out to <b>January 2027</b>. Neither is adopted &mdash; see On the Radar.')

rep('radar',
 'The <b>above-70% odds of a hike by December</b> is <b>carried from an earlier edition</b> and was not restated by any source seen at 10:50 AM.</li>',
 '''The <b>above-70% odds of a hike by December</b> is <b>carried from an earlier edition</b> and was not restated by any source seen at 10:50 AM.
&#9888; <b>At 11:35 AM it acquired a conflict, and it is being marked rather than quietly kept.</b> Reporting
dated <b>mid-August</b> states that traders had <b>fully priced a 25bp hike by December as recently as a week
earlier</b> and that the pricing had since <b>shifted to January 2027</b>. That is not compatible with
&ldquo;above 70% by December&rdquo;. The honest position is that this page cannot order the two: the
above-70% figure is <b>undated</b> and carried, the January-2027 read is <b>dated to mid-August</b>, and
<b>Warsh&rsquo;s August&nbsp;27 speech postdates both</b> and moved September pricing sharply. <b>Neither
number is asserted as current</b>, the December line is marked contested in the table above, and no
December probability is published this run.</li>
<li><b>New at 11:35 AM &mdash; the pre-speech &ldquo;one in three&rdquo; now has a date, an origin and a
second corroborating figure.</b> Three editions have carried &ldquo;about one in three&rdquo; as the
pre-speech odds of a September hike without being able to say when that reading was taken or where it came
from. Reporting fetched this run supplies both. Around <b>mid-August</b>, a rate-probability tool was
showing <b>roughly 30% odds of a 25bp September hike</b> with the chance of a pause <b>rising to almost
70%</b> &mdash; the same pair of numbers this page has been carrying as &ldquo;one in three&rdquo; and
&ldquo;nearly 70% holding&rdquo;, now attached to a period rather than floating. The move down to that level
has a cause attached to it as well: an earlier report describes September-hike odds <b>tumbling after a big
July jobs miss</b>, and <b>Goldman Sachs</b> chief economist <b>Jan Hatzius</b> told clients that recent
<b>declines in retail sales</b> and <b>disappointing employment figures</b> made a September increase
<b>&ldquo;extremely unlikely&rdquo;</b>, with the firm expecting the target range held at <b>3.50%&ndash;3.75%</b>
through the remainder of 2026. &#9888; <b>All of that is pre-Jackson-Hole and is labelled so.</b> It does not
describe where pricing sits now; it explains what the &ldquo;one in three&rdquo; was and how it got there,
which is exactly what the post-speech readings &mdash; <b>above 50/50</b> and the prediction market&rsquo;s
<b>48%</b> &mdash; are measured against. <b>No forecast is offered and no figure is averaged.</b></li>''')

rep('sources',
 'Yahoo Finance &mdash; Jobs report, Broadcom results pose next hurdles</a>',
 '''Yahoo Finance &mdash; Jobs report, Broadcom results pose next hurdles</a><br><a href="https://www.cnbc.com/2026/08/07/odds-the-fed-hikes-in-september-tumble-following-big-july-jobs-miss.html">CNBC &mdash; Odds the Fed hikes in September tumble following big July jobs miss (Aug 7)</a><br><a href="https://finance.yahoo.com/economy/policy/articles/odds-fed-rate-hike-fall-083935313.html">Yahoo Finance &mdash; Odds of a Fed rate hike this year fall as Goldman Sachs warns against hawkish bets</a><br><a href="https://www.bloomberg.com/news/articles/2026-08-17/goldman-says-markets-too-hawkish-on-betting-fed-will-hike-rates">Bloomberg &mdash; Goldman says markets too hawkish on betting the Fed will hike</a><br><a href="https://www.cnn.com/2026/08/11/business/fed-markets-kevin-warsh">CNN Business &mdash; Markets are still trying to figure out the Fed&rsquo;s next move</a>''')

miss=[]
for n,o,x in E:
    if o in t: t=t.replace(o,x,1)
    else: miss.append(n)
open(F,'w').write(t)
print('applied',len(E)-len(miss),'of',len(E),'| MISSED:',miss if miss else 'none')
