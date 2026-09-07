# -*- coding: utf-8 -*-
import re,sys
O='/sessions/gracious-zealous-maxwell/mnt/outputs/'
def rd(f): return open(O+f,encoding='utf-8').read()
def wr(f,s): open(O+f,'w',encoding='utf-8').write(s)
def sub1(s,a,b,label,count=1):
    n=s.count(a)
    if n<count:
        print('!! MISS',label,'expected>=%d got %d'%(count,n)); sys.exit(1)
    return s.replace(a,b)

# ---------------- 1. DEMOTIONS (all pages) ----------------
for f in ['cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    s=rd(f)
    s=s.replace('this 5:38&nbsp;PM edition','the 5:38&nbsp;PM edition')
    s=s.replace('this 5:38 PM edition','the 5:38 PM edition')
    s=s.replace('this run','the 5:38&nbsp;PM edition')
    s=s.replace('from this edition','from the 5:38&nbsp;PM edition')
    wr(f,s)
    print('demoted',f)

# ---------------- 2. WALL STREET ----------------
w=rd('wallstreet-briefing.html')

# 2a. body clock paragraph -- the reopen has now HAPPENED
old=('s, the 1:00&nbsp;PM ET halt is <b>about four and a half hours in the past</b>, it is the oldest of the day&rsquo;s three '
     '&mdash; ICE Brent stopped at about <b>1:30&nbsp;PM ET</b> and CME crude at about <b>2:30&nbsp;PM ET</b> &mdash; and the reopen is now '
     '<b>the nearest event of the day in either direction</b>: <b>5:00 p.m. CT is 6:00 PM ET</b>, roughly <b>twenty minutes</b> from the 5:38&nbsp;PM edition '
     'and inside the half-hour, at which point the static tape at the top of this page starts moving again on <b>Tuesday</b>&rsquo;s trade date.')
new=('s, the 1:00&nbsp;PM ET halt is <b>about five hours in the past</b>, and for the first time today it is <b>no longer the event this page is counting from</b>. '
     '<b>The reopen has happened.</b> <b>5:00 p.m. CT is 6:00 PM ET</b>, and this edition publishes <b>minutes after it</b> &mdash; so the static tape at the top of this page '
     '<b>has started moving again, on <b>Tuesday</b>&rsquo;s trade date</b>, and the halt that shaped every edition since lunchtime is now a closed interval rather than an open one: '
     '<b>1:00&nbsp;PM to 6:00 PM ET, five hours</b>. <span class="mut">The two commodity halts sat inside it &mdash; ICE Brent stopped at about <b>1:30&nbsp;PM ET</b> and CME crude at about '
     '<b>2:30&nbsp;PM ET</b> &mdash; and this page makes <b>no claim about what the reopened tape is printing</b>: the reopen time was verified in an earlier edition, the elapsed arithmetic is this desk&rsquo;s, '
     'and <b>no return read at this desk gives a post-reopen level for any symbol</b>. A tape that has started moving is not a tape anyone here has read. &#9733; <b>The moment a countdown reaches zero is the moment to stop '
     'quoting the countdown and start saying what you do and do not know about the other side of it.</b></span>')
w=sub1(w,old,new,'WS body clock')

# 2b. tldr clock sentence
old2=('The clock moved too: the <b>1:00 PM ET</b> CME equity-index halt is now <b>about four and a half hours old</b> and the <b>6:00 PM ET</b> reopen is roughly '
      '<b>twenty minutes</b> away &mdash; the nearest event of the day in either direction.')
new2=('<b>The one thing that is new in this 6:05&nbsp;PM edition is the clock, and it has crossed over:</b> the <b>6:00 PM ET</b> CME reopen '
      '<b>has now happened</b>, minutes before this edition publishes, so the <b>1:00 PM ET</b> equity-index halt is a <b>closed five-hour interval</b> rather than a running one and the tape above '
      '<b>has started moving again on Tuesday&rsquo;s trade date</b>. <b>No level is asserted for the reopened tape</b> &mdash; no return read at this desk gives one.')
w=sub1(w,old2,new2,'WS tldr clock')

# 2c. demote the futures item in the tldr opener
w=sub1(w,'<b>One item is new in the 5:38&nbsp;PM edition, and it fills a gap this page has carried since the halt:</b>',
        '<b>The 5:38&nbsp;PM edition&rsquo;s item filled a gap this page had carried since the halt:</b>','WS tldr demote')

# 2d. strip the markets New tag -> Carried (0 new tags on markets this edition)
w=w.replace('<span class="t new" style="margin-right:6px">New</span>','<span class="t" style="margin-right:6px">Carried</span>')
w=w.replace('<span class="t new">New</span>','<span class="t">Carried</span>')
wr('wallstreet-briefing.html',w)
print('WS done; new tags now',w.count('class="t new"'))
