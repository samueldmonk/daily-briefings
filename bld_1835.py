import re, sys
fails=[]
def rep(h, old, new, label, count=1):
    if h.count(old)!=count:
        fails.append("MISS %s (found %d)"%(label,h.count(old))); return h
    return h.replace(old,new,count)

# ---------------- CYBER ----------------
c=open('cyber-briefing.html').read()
# 1. strip inherited New tag
c=rep(c,'<div class="tags"><span class="tag new">New</span><span class="tag warn">Identity</span></div>',
        '<div class="tags"><span class="tag warn">Identity</span></div>','cyber strip New')
# 2. resolve the PaperCut deadline anomaly
old=('Note the window: 31 August to 14 September is <b>two weeks</b>, not the three weeks BOD 22-01 '
     'normally allows. Coverage read this run states the 14 September date plainly; the shorter clock is '
     'not explained in anything read, and is flagged here rather than smoothed over. This page had not '
     'carried the PaperCut entries at all until this edition.')
new=('Note the window: 31 August to 14 September is <b>two weeks</b>. '
     '<span class="tag new">New</span> Earlier editions flagged that as unexplained against the three-week clock of '
     '<b>BOD 22-01</b> and declined to reconcile it. It is not an anomaly. <b>BOD 26-04</b>, issued '
     '<b>10 June 2026</b>, supersedes BOD 22-01 and replaces its one-size-fits-all remediation timeline with '
     'risk-based due dates keyed to four criteria &mdash; asset exposure, KEV status, exploit automatability and '
     'post-exploitation technical impact. The top tier is <b>three calendar days</b>, with mandatory forensic '
     'triage, for a publicly exposed asset where the technical impact is total and the flaw is automatable; the '
     'bottom tier defers to the next system upgrade. Reads this run disagree on the outer bound &mdash; one puts '
     'the longest fixed window at <b>14 days</b>, another at <b>60</b> &mdash; so no single range is asserted here, '
     'but a fourteen-day PaperCut clock is the directive working as written rather than a discrepancy. '
     'This page had not carried the PaperCut entries at all until the previous edition.')
c=rep(c,old,new,'cyber BOD 26-04 resolution')
# 3. sources
c=rep(c,'<h2 class="sec">Sources &mdash; fetched this run</h2>',
        '<h2 class="sec">Sources &mdash; fetched this run</h2>','cyber sources hdr')
old_s='The Hacker News &mdash; PaperCut replaces emergency patches for two actively exploited flaws'
if old_s in c:
    c=c.replace(old_s, old_s, 1)
open('cyber-briefing.html','w').write(c)

# ---------------- MARKETS ----------------
w=open('wallstreet-briefing.html').read()
w=rep(w,'<div class="tags"><span class="tag new">New</span><span class="tag warn">Energy</span></div>',
        '<div class="tags"><span class="tag warn">Energy</span></div>','ws strip New')
old=('and Goldman Sachs switched its call from no change to a hike after the print.')
new=('and Goldman Sachs switched its call from no change to a hike after the print. Goldman chief economist '
     '<b>David Mericle</b> put the reasoning in market terms rather than macro ones: pricing for a hike had '
     'reached <b>nearly 90%</b>, high enough that the FOMC would likely want to avoid the reaction that holding '
     'would provoke.')
w=rep(w,old,new,'ws Mericle')
open('wallstreet-briefing.html','w').write(w)

# ---------------- MMA ----------------
m=open('mma-briefing.html').read()
anchor='<div class="card"><div class="datel">Sat 24 Oct &middot; Etihad Arena, Abu Dhabi</div>'
card=('<div class="card"><div class="datel">Sat 17 Oct &middot; Rogers Place, Edmonton</div>'
      '<h3>UFC Fight Night: Buckley vs. Malott</h3><p>A welterweight main event between '
      '<b>Joaquin Buckley</b> and <b>Mike Malott</b> in Malott&rsquo;s home country, with '
      '<b>Erin Blanchfield vs. Jasmine Jasudavicius</b> at women&rsquo;s flyweight as the co-main. '
      'The card is listed as <b>UFC Fight Night 291</b>. The event name was disputed in earlier editions today and is '
      'settled: UFC.com, ESPN, Tapology and the Rogers Place event listing all carry <b>Buckley vs. Malott</b>. '
      '<i>Burns vs. Malott</i> is a different, already-completed card &mdash; Winnipeg, 18 April 2026, where Malott '
      'took a Performance of the Night bonus for stopping Gilbert Burns in round three. No betting line for the '
      'headliner appears in anything read this run, so none is given.</p></div>')
m=rep(m,anchor,card+anchor,'mma insert 17 Oct card')
open('mma-briefing.html','w').write(m)

if fails:
    print("FAILED:"); [print(" ",f) for f in fails]; sys.exit(1)
print("BUILD-1835 OK")
