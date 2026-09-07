# -*- coding: utf-8 -*-
import io
D='/tmp/db_1788782763/'
def load(f): return io.open(D+f,encoding='utf-8').read()
def save(f,h): io.open(D+f,'w',encoding='utf-8').write(h)
N=[0]
def rep(h,old,new,cnt=1):
    assert h.count(old)==cnt, ("COUNT %d!=%d for: %r"%(h.count(old),cnt,old[:110]))
    N[0]+=1; return h.replace(old,new)

m=load('mma-briefing.html')

# 1) Stoppage refusal: honest about THIS run's provenance
old_start=m.find('<p style="margin:0"><b>One number this desk will not assert: the stoppage time.</b>')
old_end=m.find('</p>',old_start)+4
old=m[old_start:old_end]
new=('<p style="margin:0"><b>One number this desk will not assert: the stoppage time.</b> <b>And this run the test could not be run the same way, which is worth stating plainly rather than papering over.</b> '
 'UFC.com&rsquo;s results page has been fetched directly in each of the last seven editions and its main-event heading has read <b>&ldquo;TKO, Round 1, 2:25&rdquo;</b> every time, with '
 '<span style="font-family:var(--mono);font-size:12.5px">article:modified_time</span> frozen at <b>2026-09-05T18:40:35&minus;0400</b>. <b>This run that page could not be retrieved at all</b> &mdash; the fetch was refused '
 'before it reached the site &mdash; so no fresh reading of UFC.com is claimed here. What was fetched instead was Wikipedia&rsquo;s event page, and its results table <b>did not render</b>: the Method, Round and Time '
 'columns came back empty. A search return this run again summarised the finish at <b>2:35</b>, the fifth consecutive edition in which an aggregator has done so. So the position is unchanged and is now unchanged for the '
 '<b>twelfth consecutive edition</b>, but for a different reason: last night there was a direct reading that disagreed with the aggregators; this morning there is no direct reading at all. Either way the case for '
 'overwriting the promotion&rsquo;s own page on a count of aggregators has not improved, and the table below still records the result as TKO, Round 1, with no stamp. <span class="mut">Everything else about the card was '
 're-verified from Wikipedia&rsquo;s prose and citations this run and matched &mdash; the bonuses, the absence of a Fight of the Night award, and Parnasse&rsquo;s KSW titles.</span></p>')
m=rep(m,old,new)

# 2) Bonus structure + Paris streak + the Santos withdrawal
m=rep(m,'Gross total revenue <b>$4,365,335</b>; attendance <b>15,687 (sold out)</b>; the promotion records it as the <b>highest-grossing event in Accor Arena history</b>.</p>',
 'Gross total revenue <b>$4,365,335</b>; attendance <b>15,687 (sold out)</b>; the promotion records it as the <b>highest-grossing event in Accor Arena history</b>. '
 '<b>The bonus structure itself is newly sourced this morning</b>, from Wikipedia&rsquo;s event page citing Heavy&rsquo;s bonus report: the four Performance of the Night awards were worth '
 '<b>$100,000</b> each, and <b>the other finishes on the card received an additional $25,000</b> apiece &mdash; which is why a card with no Fight of the Night award still paid out broadly. '
 'Two further details from the same page: this was the promotion&rsquo;s <b>fifth consecutive annual visit to Paris</b> and its first since <b>UFC Fight Night: Imavov vs. Borralho in September 2025</b>; '
 'and the featherweight bout originally booked for <b>Nathaniel Wood vs. Mairon Santos</b> changed hands late &mdash; Santos withdrew with an unspecified health issue and was replaced by promotional '
 'newcomer <b>Pavel Andrusca</b>.</p>')

save('mma-briefing.html',m)
print("mma1:",N[0])
