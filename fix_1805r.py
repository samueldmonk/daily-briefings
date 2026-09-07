# -*- coding: utf-8 -*-
import sys
O='/sessions/gracious-zealous-maxwell/mnt/outputs/'
def sub1(f,a,b,label):
    s=open(O+f,encoding='utf-8').read()
    if a not in s: print('!! MISS',label); sys.exit(1)
    open(O+f,'w',encoding='utf-8').write(s.replace(a,b,1))

# 1. MMA: restore the missing opening <p> before the champions refusal note
sub1('mma-briefing.html','Champions Board</h2>\n<b>The stale-champions trap',
     'Champions Board</h2>\n<p class="note" style="margin:-4px 0 12px"><b>The stale-champions trap','mma p open')

# 2. demote the two inherited source-footer headers
sub1('cyber-briefing.html','<b>Added in this 5:38&nbsp;PM ET edition, none fetched first-hand:</b>',
     '<b>Added in the 5:38&nbsp;PM ET edition, none fetched first-hand:</b>','cy src demote')
sub1('wallstreet-briefing.html','<b>Added in this 5:38&nbsp;PM ET edition, not fetched first-hand:</b>',
     '<b>Added in the 5:38&nbsp;PM ET edition, not fetched first-hand:</b>','ws src demote')

# 3. index: the stale clock sentence on the markets card
sub1('index.html','The clock moved too: the <b>1:00 PM ET</b> halt is now about <b>four and a half hours</b> old and the <b>6:00 PM ET</b> reopen is roughly <b>twenty minutes</b> away.',
     'The clock has since crossed over: the <b>6:00 PM ET</b> reopen <b>has happened</b>, and the <b>1:00 PM ET</b> halt is now a closed <b>five-hour</b> interval.','ix clock')
print('fixes applied')
