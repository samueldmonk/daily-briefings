# -*- coding: utf-8 -*-
def rd(f): return open(f, encoding='utf-8').read()
def wr(f,s): open(f,'w',encoding='utf-8').write(s)
def rep(h, old, new, f):
    assert old in h, "MISSING in %s: %r" % (f, old[:100])
    return h.replace(old, new, 1)

# ============ CYBER: new item — the vulnerable build thresholds ============
f='cyber-briefing.html'; h=rd(f)
old = ("Affected models are the <b>SMA1000 6210, 7210 and 8200v</b>; the fixes are hotfixes "
       "<b>12.4.3-03526</b> and <b>12.5.0-02952</b> and later.")
new = ("Affected models are the <b>SMA1000 6210, 7210 and 8200v</b>; the fixes are hotfixes "
       "<b>12.4.3-03526</b> and <b>12.5.0-02952</b> and later. "
       "<b><span class=\"t new\" style=\"margin-right:6px\">New</span>Returns read this run close the one gap this entry has carried all day: the page has named the fixed builds since the 12:16 edition but never the <i>vulnerable</i> ones, so an administrator could not check an appliance against it.</b> "
       "The vulnerable builds are <b>12.4.3-03453 and older</b> and <b>12.5.0-02835 and older</b>, and the vendor notice is <b>SNWLID-2026-0016</b>. "
       "The same returns give the mechanism on 83548 as an <b>unintended alternate access path</b> in the Appliance Work Place interface, reachable over the network at <b>low attack complexity</b> with <b>no prior privileges and no user interaction</b> &mdash; which is the shape of the 10.0. "
       "<span class=\"mut\">Between the two pairs of numbers there is a build gap on each train (03453 &rarr; 03526, 02835 &rarr; 02952) that <b>no return this desk has read accounts for</b>; nothing is asserted about builds that fall inside it, and an appliance sitting there should be treated as unfixed until the vendor notice says otherwise. The build strings and the notice ID come from search returns citing the SonicWall product notice, <b>Rapid7</b> and <b>Sophos</b>; the notice itself was <b>not fetched first-hand</b>.</span>")
h = rep(h, old, new, f)

# Cyber: refusal — aggregator conflated the Elementor CVE with Magento
old2 = ("Neither StyleSmuggler nor CVE-2026-32475 in Elementor Pro is KEV-listed, and neither carries a federal deadline")
new2 = ("<b>A conflation is refused this run, and it is one that would have merged the two biggest items on this page.</b> "
        "A search summary read this run states that <b>CVE-2026-32475</b> is &ldquo;an arbitrary file upload issue in <b>Adobe Commerce and Magento</b> form submission functions.&rdquo; "
        "<b>It is not.</b> CVE-2026-32475 is the <b>Elementor Pro plugin for WordPress</b> flaw described above, fixed in <b>4.2.2</b>; the Adobe Commerce and Magento story on this page is <b>StyleSmuggler</b>, which has <b>no CVE at all</b> and <b>no vendor patch</b>. "
        "The summary appears to have fused the two because both are file-handling flaws in e-commerce software reported in the same week. "
        "The two remain separate entries here, with separate vendors, separate fix states and separate remediation. "
        "&#9733; <b>An aggregator that gives one CVE two different products has told you it merged two stories; the fixed-version number is what pulls them apart.</b><br><br>"
        "Neither StyleSmuggler nor CVE-2026-32475 in Elementor Pro is KEV-listed, and neither carries a federal deadline")
h = rep(h, old2, new2, f)

# Cyber: the Defiant count — phrasing difference, not a new number
old3 = ("the firm has <b>blocked over 190,000 exploit attempts</b> to date")
new3 = ("the firm has <b>blocked over 190,000 exploit attempts</b> to date "
        "<span class=\"mut\">(a return read this run renders the same count as &ldquo;almost 200,000&rdquo;; that is the same figure rounded up a decade, not a fresh reading, so the sourced <b>190,000+</b> is what stays on the page and in the stat strip)</span>")
h = rep(h, old3, new3, f)
wr(f,h); print("cyber content OK")

# ============ WALL STREET: recompute the halt elapsed figure ============
f='wallstreet-briefing.html'; h=rd(f)
old = ("As this <b>3:35&nbsp;PM</b> edition publishes, the 1:00&nbsp;PM ET halt is <b>about two and a half hours in the past</b> &mdash; and it is no longer even the most recent of the day&rsquo;s three halts, ICE Brent having stopped at about <b>1:30&nbsp;PM ET</b> and CME crude at about <b>2:30&nbsp;PM ET</b>.")
new = ("As this <b>5:05&nbsp;PM</b> edition publishes, the 1:00&nbsp;PM ET halt is <b>about four hours in the past</b>, it is the oldest of the day&rsquo;s three &mdash; ICE Brent stopped at about <b>1:30&nbsp;PM ET</b> and CME crude at about <b>2:30&nbsp;PM ET</b> &mdash; and for the first time today the <b>reopen is the nearer event</b>: <b>5:00 p.m. CT is 6:00 PM ET</b>, under an hour from this edition, at which point the static tape at the top of this page starts moving again on <b>Tuesday</b>&rsquo;s trade date.")
h = rep(h, old, new, f)

old = ("<b>This is the fourth consecutive edition in which a futures-halt sentence has had to be rewritten against the clock rather than against its source</b>")
new = ("<b>This is the sixth consecutive edition in which a futures-halt sentence has had to be rewritten against the clock rather than against its source</b>")
h = rep(h, old, new, f)

# Brent refusal counter advances
h = h.replace("for the thirtieth consecutive edition", "for the thirty-first consecutive edition")
wr(f,h); print("ws content OK")
