# -*- coding: utf-8 -*-
def rd(f): return open(f, encoding='utf-8').read()
def wr(f,s): open(f,'w',encoding='utf-8').write(s)
def rep(h, old, new, f):
    assert old in h, "MISSING in %s: %r" % (f, old[:100])
    return h.replace(old, new, 1)

# ---- CYBER tldr: lead with this edition's new item ----
f='cyber-briefing.html'; h=rd(f)
old = ("<b>The new item in the 4:35&nbsp;PM edition was a networking vendor shipping a pile of critical fixes as one release:</b>")
new = ("<b>The new item this edition is the pair of numbers that lets an administrator check their own appliance:</b> "
       "returns read this run give the <b>vulnerable</b> SonicWall SMA1000 builds as <b>12.4.3-03453 and older</b> and <b>12.5.0-02835 and older</b>, "
       "under vendor notice <b>SNWLID-2026-0016</b> &mdash; this page has carried the <i>fixed</i> hotfixes since the 12:16 edition but never the vulnerable ones, "
       "and that chain (CVE-2026-83548 &rarr; CVE-2026-83549) is the most severe entry in the group whose federal deadline <b>elapsed on 5 September</b>. "
       "A conflation is refused alongside it: a summary read this run calls <b>CVE-2026-32475</b> an Adobe Commerce and Magento flaw &mdash; it is the <b>Elementor Pro</b> WordPress flaw, "
       "and the Magento story here is <b>StyleSmuggler</b>, which has no CVE at all. "
       "<b>The new item in the 4:35&nbsp;PM edition was a networking vendor shipping a pile of critical fixes as one release:</b>")
h = rep(h, old, new, f); wr(f,h)

# ---- WALL STREET tldr ----
f='wallstreet-briefing.html'; h=rd(f)
old = ("<b>The new items in the 4:35&nbsp;PM edition were the only tapes that actually closed today, and they are not American:</b>")
new = ("<b>This edition&rsquo;s sweep returned nothing new, so nothing on this page is tagged New</b> &mdash; every market, oil and week-ahead return matched something already carried, "
       "down to the <b>Brent $97.39</b> print, the Hormuz restricted-zone warning and the <b>11 September CPI</b> / <b>15&ndash;16 September FOMC</b> sequence. "
       "The only thing that changed is the clock: the <b>1:00 PM ET</b> CME equity-index halt is now <b>about four hours old</b> and the <b>6:00 PM ET</b> reopen is under an hour away. "
       "<b>The new items in the 4:35&nbsp;PM edition were the only tapes that actually closed today, and they are not American:</b>")
h = rep(h, old, new, f); wr(f,h)

# ---- MMA tldr: second consecutive quiet sweep already reflected; add the stripped/vacated reason ----
f='mma-briefing.html'; h=rd(f)
old = ("A reference return says Shevchenko <b>&ldquo;was stripped of the title&rdquo;</b>; this page has said <b>vacated</b> since the <b>5 September</b> announcement, and <b>those are different events</b> &mdash; the page keeps <b>vacated</b> and says the conflict exists.")
new = ("A reference return says Shevchenko <b>&ldquo;was stripped of the title&rdquo;</b>; this page has said <b>vacated</b> since the <b>5 September</b> announcement, and <b>those are different events</b> &mdash; the page keeps <b>vacated</b> and says the conflict exists. "
       "A second return read this run repeats <b>&ldquo;stripped&rdquo;</b> and adds a reason &mdash; <b>&ldquo;due to injury&rdquo;</b> &mdash; which <b>agrees with this page on the cause and still disagrees on the mechanism</b>, so the conflict is now two returns deep and is still not resolved here.")
h = rep(h, old, new, f); wr(f,h)
print("tldrs OK")
