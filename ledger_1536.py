# -*- coding: utf-8 -*-
import io,re
def swap(f,new):
    s=io.open(f,encoding='utf-8').read()
    m=re.search(r'<p class="note"[^>]*><b>New-tag ledger.*?</p>',s,re.S)
    assert m, f
    s=s[:m.start()]+new+s[m.end():]
    io.open(f,'w',encoding='utf-8').write(s)

CY=('<p class="note" style="margin:-2px 0 10px"><b>New-tag ledger &mdash; 2 tags on this page in the 3:35&nbsp;PM ET edition.</b> '
'<span class="mut">The 3:05 edition carried <b>0</b> tags on this page, so there was nothing to strip here; the <b>1</b> markets tag and the '
'<b>2</b> MMA tags from that edition are stripped to <b>Carried</b> on their own pages. '
'<code>84353</code>, <code>84352</code>, <code>84325</code>, <code>WebGL</code>, <code>DataTransfer</code>, <code>Shared Tab Groups</code>, '
'<code>7977.75</code>, <code>7977.64</code> and all four pre-published Microsoft CVE numbers were each proved <b>absent</b> from '
'<code>archive/cyber-2026-09-07-1518.html</code> before the tags were applied. '
'<b>Only the two Chrome rows are tagged.</b> The Patch Tuesday note beneath them is <b>not</b> tagged, because its subject &mdash; '
'tomorrow&rsquo;s release, and ShieldBreak&rsquo;s place in it &mdash; is already on this page; what is new inside it is four CVE numbers and a '
'refused release time, which is detail on a carried item. Ledger across the three briefings: <b>2 cyber + 1 markets + 0 MMA = 3</b>, '
'against <b>3</b> in the 3:05 snapshots (0 + 1 + 2), so the self-test is non-trivial &mdash; the same total, distributed differently.</span></p>')

WS=('<p class="note" style="margin:-2px 0 10px"><b>New-tag ledger &mdash; 1 tag on this page in the 3:35&nbsp;PM ET edition.</b> '
'<span class="mut">The 3:05 edition&rsquo;s tag (the two reopening-week earnings dates, Kroger and Casey&rsquo;s) is stripped to <b>Carried</b>. '
'<code>14.7</code>, <code>24.6</code> and the phrase <code>energy component</code> were each proved <b>absent</b> from '
'<code>archive/wallstreet-2026-09-07-1518.html</code> before the tag was applied; the nowcast figures <b>3.38</b> and <b>0.36</b> and the '
'<b>Waller</b> hike line were proved <b>present</b>, and are deliberately <b>not</b> what is tagged &mdash; the tag is on the July energy and '
'gasoline components alone. <code>91.30</code> and <code>95.52</code> were also absent, and are <b>not</b> tagged either, because they are '
'<b>refused</b> rather than published. Ledger across the three briefings: <b>2 cyber + 1 markets + 0 MMA = 3</b>, against <b>3</b> in the 3:05 '
'snapshots (0 + 1 + 2).</span></p>')

MMA=('<p class="note" style="margin:-2px 0 10px"><b>New-tag ledger &mdash; 0 tags on this page in the 3:35&nbsp;PM ET edition.</b> '
'<span class="mut">Both 3:05 tags (UFC&nbsp;332&rsquo;s finalised twelve-bout card, and the Silva and Wang Cong records) are stripped to '
'<b>Carried</b>. <b>Nothing is tagged New</b>, because every MMA return read this edition matched something already on the page &mdash; the '
'12 September Glendale card, Soldic, the UFC&nbsp;334 opener, Allen vs. Duncan, Pimblett, and Hooker&rsquo;s post-event numbers. '
'The two strings that <i>were</i> absent from <code>archive/mma-2026-09-07-1518.html</code> &mdash; <code>Lopes 2</code> and '
'<code>Gaethje vs. Pimblett</code> &mdash; appear on this page <b>only inside the refusal that rejects them</b>, and a refusal is not a New item. '
'&#9733; <b>Proving a string absent from the last snapshot is not the same as having something new to say; on a quiet beat the honest ledger '
'reads zero.</b> Ledger across the three briefings: <b>2 cyber + 1 markets + 0 MMA = 3</b>, against <b>3</b> in the 3:05 snapshots '
'(0 + 1 + 2).</span></p>')

swap('cyber-briefing.html',CY); swap('wallstreet-briefing.html',WS); swap('mma-briefing.html',MMA)
print("ok")
