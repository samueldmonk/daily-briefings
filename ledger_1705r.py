# -*- coding: utf-8 -*-
def rd(f): return open(f, encoding='utf-8').read()
def wr(f,s): open(f,'w',encoding='utf-8').write(s)
def rep(h, old, new, f):
    assert old in h, "MISSING in %s: %r" % (f, old[:110])
    return h.replace(old, new, 1)

LED = ('<b>New-tag ledger &mdash; %s on this page in the 5:05&nbsp;PM ET edition.</b> '
       '<span class="mut">%s Ledger across the three briefings: <b>1 cyber + 0 markets + 0 MMA = 1</b>, '
       'against <b>3</b> in the 4:35&nbsp;PM snapshots &mdash; a different total and a different distribution, '
       'which is the self-test. The strings <code>12.4.3-03453</code>, <code>12.5.0-02835</code>, <code>SNWLID</code> and '
       '<code>alternate access path</code> were each proved <b>absent</b> from <code>archive/cyber-2026-09-07-1643.html</code> '
       'before the single tag was applied; <code>6210</code>, <code>8200v</code>, <code>83548</code>, <code>Appliance Work Place</code> and '
       '<code>12.4.3-03526</code> were proved <b>present</b> and are deliberately <b>not</b> what is tagged. On the markets page '
       '<code>97.39</code>, <code>maritime zone</code>, <code>2.38</code>, <code>OPEC</code> and <code>October output</code> were each proved '
       '<b>present</b> in <code>archive/wallstreet-2026-09-07-1643.html</code>, and on the MMA page <code>Moicano</code>, <code>Bahamondes</code>, '
       '<code>Tsarukyan</code>, <code>No. 10</code> and <code>Holloway</code> likewise &mdash; which is why both pages report zero. '
       '&#9733; <b>On the eighteenth run of a holiday the honest ledger is mostly zeros; the one tag that survives is the one that changes what a reader can do.</b></span>')

# ---- CYBER ledger ----
f='cyber-briefing.html'; h=rd(f)
i=h.find('<b>New-tag ledger &mdash; 2 tags on this page in the 3:35&nbsp;PM ET edition.</b>')
assert i>0
j=h.find('</p>', i); assert j>0
body = ('The <b>1</b> cyber tag from the 4:35&nbsp;PM edition (the Cisco IOS XR hardening release) is stripped to <b>Carried</b>, '
        'as are the <b>2</b> markets tags from that edition on their own page. <b>One tag is applied here</b>, on the vulnerable '
        'SonicWall SMA1000 build thresholds and the vendor notice ID. ')
h = h[:i] + (LED % ('1 tag', body)) + h[j:]
wr(f,h)

# ---- WALL STREET ledger ----
f='wallstreet-briefing.html'; h=rd(f)
i=h.find('<b>New-tag ledger &mdash; 1 tag on this page in the 3:35&nbsp;PM ET edition.</b>')
assert i>0
j=h.find('</p>', i); assert j>0
body = ('Both <b>4:35&nbsp;PM</b> tags on this page &mdash; the European and Asian closes, and the two crude prints &mdash; are stripped to '
        '<b>Carried</b>. <b>Nothing is tagged New here</b>: every market and oil return read this run matched something already on the page. ')
h = h[:i] + (LED % ('0 tags', body)) + h[j:]
wr(f,h)

# ---- MMA ledger ----
f='mma-briefing.html'; h=rd(f)
i=h.find('<b>New-tag ledger &mdash; 0 tags on this page in the 3:35&nbsp;PM ET edition.</b>')
assert i>0
j=h.find('</p>', i); assert j>0
body = ('The 4:35&nbsp;PM edition carried <b>0</b> tags here, so there was nothing to strip. <b>Nothing is tagged New</b> for a '
        '<b>second consecutive edition</b>: the sweeps returned the Paris aftermath, the UFC&nbsp;332 build-up and the booked-fights '
        'roundup, all already on the page. ')
h = h[:i] + (LED % ('0 tags', body)) + h[j:]
wr(f,h)
print("ledgers OK")
