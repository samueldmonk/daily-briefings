# -*- coding: utf-8 -*-
import re,sys
O='/sessions/gracious-zealous-maxwell/mnt/outputs/'
P=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']

SHARED=('Ledger across the three briefings: <b>1</b> cyber + <b>0</b> markets + <b>0</b> MMA = <b>1</b>, against <b>3</b> in the '
 '<b>5:38&nbsp;PM</b> snapshots &mdash; a smaller total and a different distribution, which is the self-test. '
 'The one tagged string was proved <b>absent</b> from the <b>2026-09-07-1744</b> snapshots before the tag was applied: <b>51693</b> and <b>TOTOLINK</b> from '
 '<code>archive/cyber-2026-09-07-1744.html</code>. <b>PaperCut</b>, <b>59346</b>, <b>Medusa</b>, <b>83548</b> and <b>32475</b> were proved <b>present</b> in that same snapshot and are deliberately '
 '<i>not</i> what is tagged; on the markets page <b>7,720</b>, <b>29,589</b> and <b>53,292</b> were proved present, which is why the futures prints are now <b>Carried</b> and the only new thing on that page is '
 'the <b>clock</b> &mdash; and a clock is not a tag. On the MMA page every token from the day&rsquo;s sweeps &mdash; <b>Wang Cong</b>, <b>UFC&nbsp;332</b>, <b>3 October</b>, <b>Delta Center</b>, <b>Soldic</b>, '
 '<b>Caesars</b> and the <b>&minus;450 / +350</b> opener &mdash; was proved present in <code>archive/mma-2026-09-07-1744.html</code>, which is why it reports zero for a <b>fourth</b> consecutive edition. '
 '&#9733; <b>The tag that survived this run is the one entry whose own sourcing is weakest, and that is the right outcome: the ledger measures novelty, not confidence, and the page has to carry the confidence separately.</b>')

OLD_START='Ledger across the three briefings:'
OLD_END='a run that finds something after three that did not is.'
n=0
for f in P:
    s=open(O+f,encoding='utf-8').read()
    i=s.find(OLD_START)
    while i>=0:
        j=s.find(OLD_END,i)
        if j<0: break
        s=s[:i]+SHARED+s[j+len(OLD_END):]
        n+=1
        i=s.find(OLD_START, i+len(SHARED))
    open(O+f,'w',encoding='utf-8').write(s)
print('ledger blocks replaced:',n)

def sub(f,a,b,label,req=True):
    s=open(O+f,encoding='utf-8').read()
    if a not in s:
        if req: print('!! MISS',label); sys.exit(1)
        return
    open(O+f,'w',encoding='utf-8').write(s.replace(a,b))
    print('ok',label,s.count(a))

# cyber ledger header
sub('cyber-briefing.html','<b>New-tag ledger &mdash; 2 tags on this page in the 5:38&nbsp;PM ET edition.</b> <span class="mut">The <b>1</b> cyber tag from the 5:05&nbsp;PM edition (the vulnerable SonicWall SMA1000 build thresholds and the vendor notice ID) is stripped to <b>Carried</b>. <b>Two tags are applied here</b>: the <b>VMware Workstation and Fusion</b> guest-to-host escape in the vulnerability table, and the <b>Medusa</b> federal advisory card &mdash; the second of which is tagged for <i>surfacing</i>, not for a number that moved, and the card says so. ',
 '<b>New-tag ledger &mdash; 1 tag on this page in this 6:05&nbsp;PM ET edition, and it is the only tag anywhere on the site.</b> <span class="mut">Both <b>5:38&nbsp;PM</b> cyber tags &mdash; the <b>VMware Workstation and Fusion</b> guest-to-host escape and the <b>Medusa</b> federal advisory &mdash; are stripped to <b>Carried</b>, as is the markets page&rsquo;s futures-prints tag. <b>One tag is applied here</b>: the <b>CVE-2026-51693 / TOTOLINK T6</b> row in the vulnerability table, which is also the thinnest-sourced entry on the page and is labelled as such in its own cell. ',
 'cyber ledger header')

# WS clock-rewrite ordinal + stale edition self-reference
sub('wallstreet-briefing.html','As this <b>5:38&nbsp;PM</b> edition publishes','As this <b>6:05&nbsp;PM</b> edition publishes','ws self-ref')
sub('wallstreet-briefing.html','this <b>5:38&nbsp;PM</b> edition','this <b>6:05&nbsp;PM</b> edition','ws self-ref 2',req=False)
sub('wallstreet-briefing.html','<b>This is the sixth consecutive edition in which a futures-halt sentence has had to be rewritten',
 '<b>This is the eighth consecutive edition in which a futures-halt sentence has had to be rewritten','ws ordinal')

# Brent refusal counter -> thirty-third
for f in ['wallstreet-briefing.html','index.html']:
    sub(f,'thirty-second consecutive edition','thirty-third consecutive edition','brent counter '+f,req=False)

# MMA counters
sub('mma-briefing.html','<b>Nothing is tagged New</b> for a <b>third consecutive edition</b>','<b>Nothing is tagged New</b> for a <b>fourth consecutive edition</b>','mma zero-tag ordinal')
sub('mma-briefing.html','This board has gone nineteen consecutive editions without a champions regression','This board has gone twenty consecutive editions without a champions regression','mma champs streak')
