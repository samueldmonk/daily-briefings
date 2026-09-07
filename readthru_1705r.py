# -*- coding: utf-8 -*-
def rd(f): return open(f, encoding='utf-8').read()
def wr(f,s): open(f,'w',encoding='utf-8').write(s)
def rep(h,old,new,f):
    assert old in h, "MISSING in %s: %r"%(f,old[:110])
    return h.replace(old,new,1)

# (a) "most severe entry" overclaims uniqueness — CVE-2026-49869 (Kestra OSS) shares the 10.0.
f='cyber-briefing.html'; h=rd(f)
h = rep(h,
 "and that chain (CVE-2026-83548 &rarr; CVE-2026-83549) is the most severe entry in the group whose federal deadline <b>elapsed on 5 September</b>.",
 "and that chain (CVE-2026-83548 &rarr; CVE-2026-83549) sits at the top of the group whose federal deadline <b>elapsed on 5 September</b> &mdash; <b>tied on CVSS 10.0 with CVE-2026-49869 in Kestra OSS</b>, not alone at the top.", f)

# (b) provenance of the fixed builds: the ledger proves 10:46, not 12:16.
h = rep(h,
 "the page has named the fixed builds since the 12:16 edition but never the <i>vulnerable</i> ones",
 "the page has named the fixed builds since the <b>10:46</b> edition &mdash; checked against the archived snapshots, which carry them from <code>cyber-2026-09-07-1046.html</code> onward and not before &mdash; but never the <i>vulnerable</i> ones", f)
h = rep(h,
 "this page has carried the <i>fixed</i> hotfixes since the 12:16 edition but never the vulnerable ones",
 "this page has carried the <i>fixed</i> hotfixes since the <b>10:46</b> edition but never the vulnerable ones", f)
wr(f,h)

# (c) same two corrections on the index card
f='index.html'; h=rd(f)
h = rep(h,
 "the briefing has carried the <i>fixed</i> hotfixes since midday but never the vulnerable ones, and that SSRF-to-command-injection chain "
 "(<b>CVE-2026-83548</b> &rarr; <b>CVE-2026-83549</b>) is the most severe entry in the group whose federal deadline <b>elapsed on 5 September</b>.",
 "the briefing has carried the <i>fixed</i> hotfixes since its <b>10:46</b> edition but never the vulnerable ones, and that SSRF-to-command-injection chain "
 "(<b>CVE-2026-83548</b> &rarr; <b>CVE-2026-83549</b>) sits at the top of the group whose federal deadline <b>elapsed on 5 September</b>, "
 "<b>tied on CVSS 10.0</b> with Kestra OSS rather than alone.", f)
wr(f,h)
print("read-through corrections OK")
