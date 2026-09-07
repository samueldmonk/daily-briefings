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

# Rankings movement — today is the Monday after the card
m=rep(m,'<span class="mut">No other ranking changes were sourced this run. The most recent rankings return seen this run was dated <b>2 September</b> &mdash; before the Paris card &mdash; so no official post-event movement is reflected anywhere yet, and none is asserted here.</span></p>',
 '<span class="mut">No other ranking changes were sourced this run. The most recent rankings return seen this run is still dated <b>2 September</b> &mdash; before the Paris card &mdash; so no official post-event movement is reflected anywhere yet, and none is asserted here.</span> '
 '<b>Today is the day that should change, and the mechanism is newly sourced this run.</b> The UFC replaced its media panel with algorithmic rankings built with Meta in <b>June 2026</b>, computed from '
 'fight results, opponent quality and recency, and &mdash; per that same description &mdash; <b>updated the Monday after every UFC event</b>. UFC Paris was Saturday, which makes today the scheduled '
 'update. <span class="mut">Nothing about the post-Paris board is asserted here in advance of it: the mechanism is sourced, the outcome is not, and this desk will read the refreshed board before printing any movement from it.</span></p>')

# Prospect Watch: roster additions
m=rep(m,'<h2 class="sec">Around the Sport</h2>',
 '<div class="panel" style="margin-top:14px"><p style="margin:0"><b>Roster additions.</b> Five fighters were listed as added to the UFC roster on <b>1 September 2026</b>: '
 '<b>Adam Livingston</b> (lightweight), <b>Gabriel Loren&ccedil;o</b> (heavyweight), <b>Silvestre Sanchez</b> (lightweight), <b>Modestino Rodrigues</b> (middleweight) and <b>Adam Darby</b> (welterweight). '
 '<span class="mut">Names and divisions only. No records, debut dates or signing routes are published &mdash; none were stated in the return that carried the list, and this desk will not infer a Contender Series '
 'route or a debut booking that no source named.</span></p></div>\n<h2 class="sec">Around the Sport</h2>')

save('mma-briefing.html',m)
print("mma2:",N[0])
