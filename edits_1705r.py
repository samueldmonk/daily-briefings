# -*- coding: utf-8 -*-
import re, sys

ED = "5:05&nbsp;PM ET"
PREV = "4:35&nbsp;PM"

def rd(f): return open(f, encoding='utf-8').read()
def wr(f,s): open(f,'w',encoding='utf-8').write(s)

def rep(h, old, new, f, must=1):
    n = h.count(old)
    assert n >= must, "MISSING in %s: %r (found %d)" % (f, old[:90], n)
    return h.replace(old, new)

# ---------------- 1. DEMOTE inherited "this run"/"this edition" ----------------
demotions = {
 'cyber-briefing.html': [
   ("<b>The new item this edition is a networking vendor shipping a pile of critical fixes as one release:</b>",
    "<b>The new item in the 4:35&nbsp;PM edition was a networking vendor shipping a pile of critical fixes as one release:</b>"),
   ("returns read this run describe a <b>Cisco IOS XR hardening release",
    "returns read then described a <b>Cisco IOS XR hardening release"),
   ("Nothing was fetched first-hand this run.</span></span></div>",
    "Nothing was fetched first-hand in the 4:35&nbsp;PM edition or this one.</span></span></div>"),
   ("Returns read this run put <b>seven umbrella CVEs</b>",
    "Returns read in the 4:35&nbsp;PM edition put <b>seven umbrella CVEs</b>"),
 ],
 'wallstreet-briefing.html': [
   ("<b>The new items this edition are the only tapes that actually closed today, and they are not American:</b>",
    "<b>The new items in the 4:35&nbsp;PM edition were the only tapes that actually closed today, and they are not American:</b>"),
   ("Nothing was fetched first-hand this run.</span></span></div>",
    "Nothing was fetched first-hand in the 4:35&nbsp;PM edition or this one.</span></span></div>"),
   ("Returns read this run give the <b>pan-European Stoxx&nbsp;600</b>",
    "Returns read in the 4:35&nbsp;PM edition gave the <b>pan-European Stoxx&nbsp;600</b>"),
 ],
 'mma-briefing.html': [
   ("<b>There is no new development this edition &mdash; the sweep returned only material this page already carries</b>",
    "<b>There is no new development in this edition either &mdash; a second consecutive sweep returned only material this page already carries</b>"),
   ("Nothing was fetched first-hand this run.</span></span></div>",
    "Nothing was fetched first-hand in the 4:35&nbsp;PM edition or this one.</span></span></div>"),
   ("<b>this page carries zero New tags this edition</b>",
    "<b>this page carried zero New tags in the 4:35&nbsp;PM edition</b>"),
   ("<b>no return read this run reconciles them</b>",
    "<b>no return read in the 4:35&nbsp;PM edition reconciled them</b>"),
   ("&#9733; <b>A one-word difference in how a title came open is a factual claim about who did what, not a style choice.</b> Nothing was fetched first-hand this run.",
    "&#9733; <b>A one-word difference in how a title came open is a factual claim about who did what, not a style choice.</b> Nothing was fetched first-hand in the 4:35&nbsp;PM edition or this one."),
 ],
 'index.html': [
   ("This edition&rsquo;s sweep returned nothing new, so the briefing carries <b>no New tag</b>",
    "A second consecutive sweep returned nothing new, so the briefing carries <b>no New tag</b>"),
 ],
}
for f, pairs in demotions.items():
    h = rd(f)
    for a,b in pairs: h = rep(h,a,b,f)
    wr(f,h)
print("demote OK")

# ---------------- 2. STRIP previous edition's New tags to Carried ----------------
for f in ['cyber-briefing.html','wallstreet-briefing.html']:
    h = rd(f)
    n = h.count('<span class="t new" style="margin-right:6px">New</span>')
    h = h.replace('<span class="t new" style="margin-right:6px">New</span>',
                  '<span class="t" style="margin-right:6px">Carried</span>')
    h = h.replace('<span class="t new" style="margin-right:6px">New</span> CVE-2026-20274',
                  '<span class="t" style="margin-right:6px">Carried</span> CVE-2026-20274')
    wr(f,h); print("stripped %d New tags in %s" % (n,f))

# cyber table row tag (different markup)
h = rd('cyber-briefing.html')
h = h.replace('<td><span class="t new" style="margin-right:6px">New</span> CVE-2026-20274',
              '<td><span class="t" style="margin-right:6px">Carried</span> CVE-2026-20274')
wr('cyber-briefing.html',h)
print("strip OK")
