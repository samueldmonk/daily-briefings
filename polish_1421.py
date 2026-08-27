# -*- coding: utf-8 -*-
D='/tmp/db_1787854887/'
def go(f,pairs):
    s=open(D+f,encoding='utf-8').read()
    for old,new in pairs:
        assert s.count(old)>=1,"MISSING %s :: %s"%(f,old[:90]); s=s.replace(old,new)
    open(D+f,'w',encoding='utf-8').write(s)

go('wallstreet-briefing.html',[
 # (i) freshest tag should lead the Lead panel
 ('<span class="tag">Carried · 12:38 PM ET</span><span class="tag acc">Midday session</span>\n<span class="tag new">Updated · 2:21 PM ET</span>',
  '<span class="tag new">Updated · 2:21 PM ET</span><span class="tag acc">Midday session</span><span class="tag">Carried · 12:38 PM ET</span>'),
 # (ii) narrow an unverifiable "every read" claim to what the page itself demonstrably holds
 ("it was quoted at 0.4% in every read this page carried from the open through 12:38, and is now quoted at double that.",
  "0.4% is the only S&amp;P 500 figure this page has carried at any point today until now, and the index is now quoted at double that."),
 # (iii) make explicit that the new Bloomberg line adds no numeric SECTOR figure
 ("That is the first sector claim this page has been able to publish today with a timestamp attached — which is precisely what the rejected tables lacked.",
  "That is the first sector claim this page has been able to publish today with a timestamp attached — which is precisely what the rejected tables lacked. "
  "<span style=\"color:var(--mut)\">Note what it is not: Bloomberg gives a <i>direction</i> for sectors (technology alone advancing) plus an index figure and five single-stock figures. "
  "It supplies no numeric sector return, so the two semiconductor ETF proxies above remain the only sector <i>numbers</i> on this page.</span>"),
])

go('cyber-briefing.html',[
 ("expires today with the working day more than half gone",
  "expires today, with under three hours of the East Coast business day left"),
])
print("polish ok")
