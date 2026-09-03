# -*- coding: utf-8 -*-
import io, os
O="/sessions/zealous-laughing-euler/mnt/outputs"
def ed(f, pairs):
    p=os.path.join(O,f); s=io.open(p,encoding="utf-8").read()
    for a,b in pairs:
        assert a in s, "ANCHOR MISS in %s: %r" % (f, a[:70])
        s=s.replace(a,b)
    io.open(p,"w",encoding="utf-8").write(s); print("patched",f,len(s))

# ---- DEFECT 1: the summary strip conflated Wednesday's after-hours move with
#      Thursday's pre-market move. They are different windows, not a disagreement.
OLDSUM=("while Snowflake jumps roughly 22&ndash;24% pre-market on a raised full-year forecast.")
NEWSUM=("while Snowflake jumps more than 24% pre-market on a raised full-year forecast.")
for f in ("index.html","wallstreet-briefing.html"):
    ed(f,[(OLDSUM,NEWSUM)])

ed("wallstreet-briefing.html", [
  # ---- DEFECT 1 (cont.): fix the tag and the provenance sentence
  ('<span class="tag a">+22&ndash;24%</span>', '<span class="tag a">+24% pre-market</span>'),
  ('<b>Readings differ:</b> CNBC has the after-hours move at 22%, '
   'Yahoo at 23%, and the Thursday pre-market print at more than 24%. All three are printed; '
   'none is adopted as the number.',
   '<b>Two different windows:</b> the Wednesday after-hours move was reported at 22% by CNBC '
   'and 23% by Yahoo Finance; the figure above is Thursday\'s pre-market print of more than 24%. '
   'These are not competing readings of the same move and are not treated as such.'),
])

ed("mma-briefing.html", [
  # ---- DEFECT 2: "Two September title fights" followed by one name
  ('<li><b>Two September title fights are already on the books</b> &mdash; Van vs. Pantoja 2 at '
   'UFC 331 &mdash; while October\'s pay-per-view is still shopping for a headliner.</li>',
   '<li><b>One September title fight is on the books</b> &mdash; Van vs. Pantoja 2 for the '
   'flyweight belt at UFC 331 &mdash; while October\'s pay-per-view is still shopping for a '
   'headliner.</li>'),
  # ---- DEFECT 3: card depth carried from a prior edition, not sourced this run
  ("the card ran eleven fights deep and this is not the full results table",
   "this is not the full results table, and no card depth is asserted because none was "
   "re-sourced this run"),
  # ---- DEFECT 5: desk jargon in a reader-facing bullet
  ('<li><b>Bilal Hasan\'s bonus is now doubly sourced.</b> He took a $100,000 Performance of the '
   'Night award at Shanghai having earned his contract on Contender Series Week 1 &mdash; a '
   'quick turn from the developmental series to a headline bonus.</li>',
   '<li><b>A fast rise for Bilal Hasan.</b> He earned his UFC contract on Contender Series Week 1 '
   'of this season and has already collected a $100,000 Performance of the Night award at '
   'Shanghai.</li>'),
])

ed("cyber-briefing.html", [
  # ---- DEFECT 4: the Nutex attribution was carried from a prior edition, not re-sourced
  (' and links the activity to the Gentlemen ransomware operation &mdash; the same '
   'crew named as the claimant in the Nutex Health intrusion. The pattern on display is one '
   'intrusion combining access theft, surveillance and defence evasion rather than a '
   'smash-and-grab.',
   ' and links the activity to the Gentlemen ransomware operation. The pattern on display is one '
   'intrusion combining access theft, surveillance and defence evasion rather than a '
   'smash-and-grab.'),
])
