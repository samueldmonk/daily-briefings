# -*- coding: utf-8 -*-
def rd(f): return open(f, encoding='utf-8').read()
def wr(f,s): open(f,'w',encoding='utf-8').write(s)
def rep(h, old, new, f):
    assert old in h, "MISSING in %s: %r" % (f, old[:110])
    return h.replace(old, new, 1)

# ================= INDEX CARDS =================
f='index.html'; h=rd(f)

# --- security card ---
old = ("The new item is a <b>Cisco IOS XR hardening release bundling seven umbrella CVEs</b>, two rated <b>9.8</b> "
       "&mdash; <b>CVE-2026-20274</b> for memory-safety and resource-lifetime bugs and <b>CVE-2026-20279</b> for "
       "access-control bugs including missing authentication for critical functions &mdash; alongside the "
       "<b>Nexus 9000</b> root-execution flaw <b>CVE-2026-20212</b> the briefing already carried. "
       "Cisco says it is not aware of malicious use as of its 2 September disclosure, neither IOS XR CVE appears in "
       "the 2 or 4 September KEV additions the briefing lists, and no deadline attaches to either.")
new = ("The new item is the pair of numbers that lets an administrator check their own box: returns give the "
       "<b>vulnerable</b> SonicWall SMA1000 builds as <b>12.4.3-03453 and older</b> and <b>12.5.0-02835 and older</b> "
       "under vendor notice <b>SNWLID-2026-0016</b> &mdash; the briefing has carried the <i>fixed</i> hotfixes since midday "
       "but never the vulnerable ones, and that SSRF-to-command-injection chain "
       "(<b>CVE-2026-83548</b> &rarr; <b>CVE-2026-83549</b>) is the most severe entry in the group whose federal deadline "
       "<b>elapsed on 5 September</b>. A conflation is refused alongside it: a summary calls <b>CVE-2026-32475</b> an "
       "Adobe Commerce and Magento flaw, when it is the <b>Elementor Pro</b> WordPress flaw and the Magento story is "
       "<b>StyleSmuggler</b>, which has no CVE at all. The 4:35&nbsp;PM edition&rsquo;s Cisco IOS XR item is carried.")
h = rep(h, old, new, f)

# --- markets card ---
old = ("The new items are the tapes that did close:")
new = ("This edition&rsquo;s sweep returned <b>nothing new</b>, so the briefing carries <b>no New tag</b> &mdash; "
       "the Brent <b>$97.39</b> print, the Hormuz restricted-zone warning and the <b>11 September CPI</b> / "
       "<b>15&ndash;16 September FOMC</b> sequence were all already carried. What changed is the clock: the "
       "<b>1:00 PM ET</b> CME equity-index halt is now about <b>four hours</b> old and the <b>6:00 PM ET</b> reopen is "
       "under an hour away. The 4:35&nbsp;PM edition&rsquo;s new items were the tapes that did close:")
h = rep(h, old, new, f)
h = rep(h, "so no single Brent level is asserted for a thirtieth consecutive edition",
           "so no single Brent level is asserted for a thirty-first consecutive edition", f)

# --- mma card ---
old = ("a reference return says Shevchenko <b>&ldquo;was stripped of the title,&rdquo;</b> the briefing says <b>vacated</b>, and those are different events.")
new = ("a reference return says Shevchenko <b>&ldquo;was stripped of the title,&rdquo;</b> the briefing says <b>vacated</b>, and those are different events. "
       "A second return this edition repeats <b>&ldquo;stripped&rdquo;</b> and adds <b>&ldquo;due to injury&rdquo;</b> &mdash; agreeing on the cause, still disagreeing on the mechanism.")
h = rep(h, old, new, f)
wr(f,h); print("index OK")

# ================= SOURCES FOOTERS =================
f='cyber-briefing.html'; h=rd(f)
old = '<h2 class="sec">Sources</h2><p class="note" style="margin:-2px 0 10px"><b>Added in the 4:35&nbsp;PM ET edition:</b>'
new = ('<h2 class="sec">Sources</h2><p class="note" style="margin:-2px 0 10px"><b>Added in the 5:05&nbsp;PM ET edition '
       '(search returns, none fetched first-hand):</b> '
       '<a href="https://www.sonicwall.com/support/notices/product-notice-sma-1000-series-affected-by-multiple-vulnerabilities-snwlid-2026-0016/kA1VN000002AXmQ0AW">SonicWall product notice SNWLID-2026-0016 &mdash; SMA 1000 Series multiple vulnerabilities</a> &nbsp;&middot;&nbsp; '
       '<a href="https://www.rapid7.com/blog/post/etr-critical-sonicwall-sma1000-vulnerabilities-cve-2026-83548-cve-2026-83549-exploited-in-the-wild/">Rapid7 &mdash; SMA1000 CVE-2026-83548 / CVE-2026-83549 exploited in the wild</a> &nbsp;&middot;&nbsp; '
       '<a href="https://www.sophos.com/en-us/blog/sonicwall-83548-83549">Sophos &mdash; SMA1000 vulnerabilities in active exploitation</a> &nbsp;&middot;&nbsp; '
       '<a href="https://www.wordfence.com/blog/2026/09/attackers-actively-exploiting-critical-vulnerability-in-elementor-pro-plugin/">Wordfence / Defiant &mdash; Elementor Pro CVE-2026-32475 (the &ldquo;almost 200,000&rdquo; phrasing of the blocked-attempt count)</a> &nbsp;&middot;&nbsp; '
       '<a href="https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog">CISA alert &mdash; 2 September KEV additions (re-confirmed this run)</a>. '
       '<span class="mut"><b>Refused this run and named here:</b> a search summary attributing <b>CVE-2026-32475</b> to <b>Adobe Commerce and Magento</b> &mdash; it is the Elementor Pro WordPress flaw, and the Magento item on this page is StyleSmuggler, which has no CVE.</span></p>'
       '<p class="note" style="margin:-2px 0 10px"><b>Added in the 4:35&nbsp;PM ET edition:</b>')
h = rep(h, old, new, f); wr(f,h)

f='wallstreet-briefing.html'; h=rd(f)
i=h.find('<h2 class="sec">Sources</h2>')
assert i>0
add = ('<h2 class="sec">Sources</h2><p class="note" style="margin:-2px 0 10px"><b>Re-checked in the 5:05&nbsp;PM ET edition, '
       'none fetched first-hand and none new:</b> <span class="mut">a Labor Day market-hours return re-confirming NYSE and Nasdaq shut all day '
       'with the normal session resuming <b>Tuesday 8 September</b>; a commodity data page giving <b>Brent 97.39, up 1.15%</b> on 7 September '
       '&mdash; below the <b>$97.93</b> touch and therefore corroboration, not a new high; an oil-market summary restating the weekend tanker strikes, '
       'the <b>restricted maritime zone</b> Tehran says it will impose beyond Hormuz, Hormuz traffic at its lowest since May, and <b>OPEC+ leaving October '
       'output policy unchanged</b>; and a week-ahead return restating <b>Waller</b> leaning to hold, the <b>15&ndash;16 September FOMC</b>, '
       '<b>CPI on Friday 11 September</b> and the <b>3.38% / 0.36%</b> headline and <b>2.38% / 0.20%</b> core nowcasts as of 4 September. '
       '<b>Every one of these was proved already present on the page before it was read as new.</b></span></p>')
h = h[:i] + add + h[i+len('<h2 class="sec">Sources</h2>'):]
wr(f,h)

f='mma-briefing.html'; h=rd(f)
i=h.find('<h2 class="sec">Sources</h2>')
assert i>0
add = ('<h2 class="sec">Sources</h2><p class="note" style="margin:-2px 0 10px"><b>Re-checked in the 5:05&nbsp;PM ET edition, '
       'none fetched first-hand and none new:</b> <span class="mut">UFC&nbsp;332 odds coverage restating <b>Silva &minus;210 (opened &minus;250)</b> '
       'and <b>Wang Cong +180 (opened +210)</b> per BetOnline.ag and <b>Talbott &minus;550 / Figueiredo +415</b> in the co-main &mdash; and using '
       '<b>&ldquo;stripped &hellip; due to injury&rdquo;</b> for the vacated belt, the wording conflict noted above; UFC Paris aftermath coverage '
       'restating <b>Parnasse TKO1 Hooker at 2:35</b>, the expectation that he takes Hooker&rsquo;s <b>No. 10</b> lightweight ranking, and Hooker&rsquo;s '
       'losses to <b>Arman Tsarukyan</b> and <b>Benoit Saint Denis</b>; and a booked-fights roundup restating <b>Moicano vs. Ortega</b> at UFC&nbsp;331 and '
       '<b>Bahamondes vs. Salikhov</b> at Noche UFC. <b>All were proved already present on the page.</b></span></p>')
h = h[:i] + add + h[i+len('<h2 class="sec">Sources</h2>'):]
wr(f,h)
print("sources OK")
