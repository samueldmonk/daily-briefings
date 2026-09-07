# -*- coding: utf-8 -*-
import io,sys
P='cyber-briefing.html'
s=io.open(P,encoding='utf-8').read()
orig=s
def rep(a,b,n=1):
    global s
    assert s.count(a)>=1, "MISSING: "+a[:120]
    s=s.replace(a,b,n)

# 1) provenance demotion: inherited "this edition" -> "the 1:15 edition"
for a,b in [
 ('the one genuinely new item this edition is not a vulnerability',
  'the one genuinely new item the 1:15 edition was not a vulnerability'),
 ('the underlying vendor research was not fetched first-hand this edition, and this card says so',
  'the underlying vendor research was not fetched first-hand in any edition, and this card says so'),
 ('</b> in any return read this edition',
  '</b> in any return read for this page'),
 ('Sources this edition: search returns citing the 7&nbsp;September analysis',
  'Sources: search returns citing the 7&nbsp;September analysis'),
 ('This edition reads the primary.','The 12:16 edition read the primary.'),
 ('the KEV set below re-confirmed by title this edition','the KEV set below re-confirmed by title the 1:15 edition'),
]:
    rep(a,b)

# 2) Tengu tag New -> Carried
rep('<div class="tags"><span class="t new">New</span><span class="t hot">Linux / IoT</span>',
    '<div class="tags"><span class="t">Carried</span><span class="t hot">Linux / IoT</span>')

# 3) rewrite the novelty ledger note
old_start = s.find('<p class="note" style="margin:-4px 0 12px"><b>One item is tagged New this edition')
old_end   = s.find('</p>', old_start)+4
assert old_start>0 and old_end>old_start
ledger = (u'<p class="note" style="margin:-4px 0 12px"><b>Two items are tagged New this edition and both are on this page: '
 u'the <b>Natural Resources Wales</b> disclosure immediately below, and the <b>Advantech WISE&#8209;6610</b> pair in the '
 u'vulnerability table. The MMA page carries one new item &mdash; the 10&nbsp;October Las Vegas card &mdash; and the Wall Street page carries none.</b> '
 u'<span class="mut">Measured against <code>archive/cyber-2026-09-07-1313.html</code>, <code>archive/wallstreet-2026-09-07-1313.html</code> and '
 u'<code>archive/mma-2026-09-07-1313.html</code>, counting the markup these pages actually emit (<code>class=&quot;t new&quot;</code>) and asserting '
 u'<b>placement per page</b> rather than a bare total. The 1:15 snapshots carried <b>one</b> New tag in total &mdash; the <b>Tengu</b> analysis on this page &mdash; '
 u'and that item is still here and still correct, but it was in the previous archived edition, so its tag now reads <b>Carried</b>. '
 u'Natural Resources Wales, Advantech, and the string <code>79697</code> each return zero matches in all three 1:15 snapshots, which is the test that earns the tag. '
 u'A tag is a statement about the previous snapshot, not about how recently the underlying event happened.</span> '
 u'<b>The markets beat produced no new item this edition</b> &mdash; U.S. exchanges are shut for Labor Day &mdash; '
 u'<span class="mut">and an edition with two new items is reported as two.</span></p>')
s = s[:old_start] + ledger + s[old_end:]

# 4) insert the NRW breach card ahead of the Tengu card
anchor = '<div class="card">\n<div class="tags"><span class="t">Carried</span><span class="t hot">Linux / IoT</span>'
assert anchor in s, 'tengu card anchor missing'
nrw = (u'<div class="card">\n'
 u'<div class="tags"><span class="t new">New</span><span class="t">Public sector</span><span class="t">Human error</span></div>\n'
 u'<h3>Natural Resources Wales published its own staff diversity data to its own website &mdash; and it was not a break-in</h3>\n'
 u'<p><b>Natural Resources Wales has confirmed a personal data breach affecting former and current employees, and the cause it gives is human error rather than intrusion.</b> '
 u'A spreadsheet containing employee information was <b>inadvertently published on the agency&rsquo;s own website</b>, where it was accessible until an internal investigation identified '
 u'the problem and it was taken down. The data relates to people who worked for the agency between <b>April 2013 and March 2018</b>, and the fields at risk are the most sensitive an '
 u'employer holds: <b>diversity monitoring information</b> covering ethnicity, disability status, religion or belief, sexual orientation, Welsh language ability and caring responsibilities. '
 u'NRW says it has <b>found no evidence that the exposed information has been misused</b>, has <b>notified the Information Commissioner&rsquo;s Office</b>, and is examining the controls '
 u'that allowed the file to go out.</p>\n'
 u'<p class="note"><b>Why a desk that spends its day on exploited CVEs is leading a breach card with a spreadsheet.</b> '
 u'<span class="mut">Every other item on this page is someone else&rsquo;s code failing. This one is a publishing workflow, and it produced a disclosure of protected-characteristic data '
 u'that no patch cycle would have prevented and no exploit detection would have caught &mdash; the file was served deliberately, by the victim, over its own web server. '
 u'The affected window closed more than eight years ago, which is the second lesson: retention is an attack surface, and a spreadsheet nobody needed since 2018 is the reason this is a breach '
 u'rather than a near miss. <b>No attacker, no ransom demand, no CVE and no federal deadline attach to this item</b>, and none is printed. '
 u'Sourced from reporting dated 6&ndash;7&nbsp;September (DataBreaches.net, Water Magazine, Cybersecurity News, GBHackers, plus the agency&rsquo;s own statement notice as relayed); '
 u'none of those pages was fetched first-hand. <b>No count of affected individuals was stated in any return, so none is given here.</b></span></p>\n'
 u'</div>\n')
s = s.replace(anchor, nrw + anchor, 1)

# 5) Advantech row into the Vulnerability Watch table, right after the header row
hdr = '<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>\n'
assert hdr in s
adv = (u'<tr><td><span class="t new">New</span> CVE-2026-79697<br><span class="mut">with CVE-2026-79698</span></td>'
 u'<td class="down"><b>9.9 (Critical)</b><br><span class="mut">VulDB</span></td>'
 u'<td>Advantech <b>WISE-6610</b> series LoRaWAN gateways, firmware <b>1.2.1_20251110</b></td>'
 u'<td><b>Unauthenticated command injection in the Basic Station certificate-deletion handler.</b> '
 u'The <code>basicstation_apply</code> routine passes its <code>act</code> argument through to a shell, and <b>no authentication is required</b> to reach it &mdash; '
 u'network access to the gateway is the whole prerequisite. <b>CVE-2026-79698</b> is the same defect in a different handler, <code>nodered_lib_apply</code> in the Node-RED library component; '
 u'VulDB records it against the identical firmware build, and <b>no separate score is asserted for it here</b> because only the daily CVE brief supplied one. '
 u'The affected list runs across the <b>NB, EB, TB, JB, CB and EL variants plus the P-series</b> (WISE-6610P-DEA, -DNA, -DTA). '
 u'<b>Fixed in firmware 1.2.4_20260821</b>, hosted at advantech.com; VulDB records that the vendor was contacted early and shipped the fix. '
 u'<b>Disclosed, not exploited: no proof-of-concept, no in-the-wild claim, and NOT in the CISA KEV catalog</b> &mdash; the 2 and 4 September KEV additions listed below do not include it, '
 u'so <b>no federal deadline and no countdown attach to this row.</b> '
 u'<span class="mut">Two routes to the record: the VulDB entries for both CVEs, and a 7&nbsp;September daily CVE brief that lists the pair at 9.9; a third write-up describes the Basic Station '
 u'flaw as critical RCE without printing a score. Neither Advantech&rsquo;s bulletin nor NVD was fetched first-hand, and the score is attributed to VulDB rather than to the vendor.</span></td></tr>\n')
s = s.replace(hdr, hdr + adv, 1)

# 6) tldr: append the new-item clause
old_tl = u'and the one genuinely new item the 1:15 edition was not a vulnerability at all but a piece of malware, the <b>Tengu</b> Linux bot, freshly analysed today and built to reboot the machine when defenders kill it.'
new_tl = (u'and the two genuinely new items this edition sit either side of the usual security story: '
 u'a <b>Natural Resources Wales</b> disclosure caused by publishing a staff spreadsheet to its own website rather than by any intruder, '
 u'and an unauthenticated command-injection pair in <b>Advantech WISE-6610</b> LoRaWAN gateways, scored 9.9 by VulDB, already fixed in firmware and not exploited.')
rep(old_tl,new_tl)

# 7) sources
src_anchor = u'<h2 class="sec">Sources</h2>'
assert src_anchor in s
add = (u'<h2 class="sec">Sources</h2><p class="note" style="margin:-2px 0 10px"><b>Added the 1:45 PM ET edition, and none of these was fetched first-hand:</b> '
 u'<span class="mut">search returns for Natural Resources Wales (DataBreaches.net, 6&nbsp;Sep; Water Magazine, 7&nbsp;Sep; Cybersecurity News; GBHackers; Cyberpress; the agency statement notice as relayed) '
 u'and for the Advantech WISE-6610 pair (VulDB entries for CVE-2026-79697 and CVE-2026-79698; a 7&nbsp;September daily CVE brief; TheHackerWire).</span></p>')
s = s.replace(src_anchor, add, 1)

assert s!=orig
io.open(P,'w',encoding='utf-8').write(s)
print("cyber OK", len(s))
