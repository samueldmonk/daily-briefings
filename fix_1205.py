#!/usr/bin/env python3
"""Post-edit fixes for the 12:05 edition: inherited markup defect, provenance, CPI self-contradiction."""
import io, os, re, sys
OUT="/sessions/vibrant-gracious-wright/mnt/outputs"
fails=[]
def L(n): return io.open(os.path.join(OUT,n),encoding="utf-8").read()
def S(n,h): io.open(os.path.join(OUT,n),"w",encoding="utf-8").write(h)
def rep(h,o,n,label,count=1):
    if o not in h: fails.append("MISSING: "+label); return h
    if h.count(o)!=count: fails.append("COUNT %d!=%d: %s"%(h.count(o),count,label))
    return h.replace(o,n,count)

# ---------------- CYBER ----------------
c=L("cyber-briefing.html")

# (1) INHERITED MARKUP DEFECT: a doubled </div> after the last Breaches card closed
#     <div class="wrap"> ~41KB early, pushing everything from Vulnerability Watch down
#     outside the page's max-width/padding container.
c = rep(c,
  'What is now a matter of record is the filing, not the breach.</span></p>\n</div>\n</div>\n<h2 class="sec">Vulnerability Watch</h2>',
  'What is now a matter of record is the filing, not the breach.</span></p>\n</div>\n<h2 class="sec">Vulnerability Watch</h2>',
  "cyber: remove stray </div> that closed .wrap early")

# (2) PROVENANCE: an inherited first-hand claim my demoter's patterns missed
c = rep(c, "Two first-hand fetches this run supply all three.",
           "Two first-hand fetches in the 11:46 edition supplied all three.",
           "cyber: demote 'Two first-hand fetches this run'")

# (3) note the markup repair on the page
c = rep(c, '<h2 class="sec">Vulnerability Watch</h2>',
  '<h2 class="sec">Vulnerability Watch</h2>\n<p class="note" style="margin:-4px 0 12px"><b>A markup defect that predates this edition was repaired here, and it is worth recording because no content check could ever have found it.</b> <span class="mut">A doubled <code>&lt;/div&gt;</code> after the last card in Breaches &amp; Incidents closed the page&rsquo;s <code>.wrap</code> container roughly 41,000 characters early &mdash; so everything from this heading down, about a third of the page, was rendering outside the wrapper that supplies the max-width and the padding. The page&rsquo;s <code>&lt;div&gt;</code> opens and closes were off by exactly one, and had been for some time; the other three pages balance exactly. &#9733; <b>A page that reads correctly can still be built wrong, and only a structural check finds it &mdash; balance the tags, and check that the container closing last is the container that opened first.</b> Both assertions now run every edition, on all four pages.</span></p>',
  "cyber: log markup repair")

S("cyber-briefing.html", c)

# ---------------- WALL STREET ----------------
w=L("wallstreet-briefing.html")

# (4) SELF-CONTRADICTION: the draft CPI paragraph asserted a "new" contradiction and a
#     blanket withholding, while the page already carries a fuller, correctly-attributed
#     treatment of the same forecasts further down. Replaced with one paragraph that
#     defers to the established treatment instead of competing with it.
old_start = '<p><b>No CPI consensus figure is published here, and the reason is a direct contradiction between two returns this run.</b>'
i = w.find(old_start)
if i < 0: fails.append("MISSING: ws CPI paragraph")
else:
    j = w.find('</p>', i)+4
    NEWP = '''<p><b>This run&rsquo;s week-ahead return repeated the same CPI forecasts this page already carries, and it changes nothing &mdash; which is the point of checking.</b> It gave headline <b>3.4%</b> year on year and core <b>2.4%</b>. The headline figure lands inside the ~3.4% cluster set out under the CPI consensus below; the core figure inverts the core-versus-headline relationship in exactly the way the 4 September nowcast does, and against Morningstar&rsquo;s survey, which has core <em>above</em> headline. <span class="mut">So the spread this page refuses to collapse into a single consensus number is unchanged, and the refusal stands where it already stood &mdash; restated here rather than re-argued, because the fuller treatment is below and two accounts of the same disagreement on one page is how a page starts contradicting itself.</span> <b>The same return also described the August payrolls consensus as 55,000.</b> That is the collision this desk has already resolved: the consensus is <b>53,000</b>, and 55,000 is the two-month upward revision to June and July. <span class="mut">An aggregator repeating a number this page has already traced to the wrong line is a reason to re-state the finding, not to reopen it.</span></p>'''
    w = w[:i] + NEWP + w[j:]

# (5) the Apple/Oracle paragraph should not restate the CPI date as if it were new
w = rep(w, '<b>Friday 11 September</b> &mdash; <b>August CPI at 8:30&nbsp;AM ET</b>, the print Fed governor Christopher Waller said on 3 September would largely determine his vote.',
           '<b>Friday 11 September</b> &mdash; <b>August CPI at 8:30&nbsp;AM ET</b>, already the fixed point of this page and the print Fed governor Christopher Waller said on 3 September would largely determine his vote; the FOMC decision follows on 16 September.',
           "ws: CPI line defers to existing treatment")

S("wallstreet-briefing.html", w)

print("FIXES APPLIED" if not fails else "FAILURES:")
for f in fails: print("  -",f)
sys.exit(1 if fails else 0)
