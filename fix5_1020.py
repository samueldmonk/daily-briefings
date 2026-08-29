# -*- coding: utf-8 -*-
"""Fifth fix pass, 10:20 AM edition -- SIX expired "this run" claims.

Fourth consecutive edition with this exact failure family, so it is now audited
systematically rather than spotted: every POSITIVE novelty form ("sourced this run",
"fetched this run", "corroborated this run", "re-confirmed this run") was enumerated
and each was checked against the edition that actually did the fetching. Negative forms
("no source seen this run states X") were left alone -- they remain true.

Kept as TRUE this run (verified, not rewritten):
  - MMA: UFC.com's event page WAS fetched at 10:20, so Hasan's re-verification stands.
  - MMA: Joshua Van IS corroborated at 10:20 by the UFC 331 listing seen this run.
  - MMA: the "no viewership/gate/purse figure" negative stands.
"""
import io, sys
fails = []
def edit(p, pairs):
    s = io.open(p, encoding='utf-8').read()
    for old, new, label in pairs:
        if s.count(old) != 1:
            fails.append("%s / %s: found %d" % (p, label, s.count(old))); continue
        s = s.replace(old, new)
    io.open(p, 'w', encoding='utf-8').write(s)

edit('cyber-briefing.html', [
    ("Carried from the previous edition's verified sourcing and re-confirmed this run as a\ncurrent item.",
     "Carried from an earlier edition's verified sourcing and last re-confirmed as a current item in the\n"
     "<b>9:40 AM</b> edition.", "TeamPCP"),
    ("The number of signatories is not agreed across the sources fetched this run",
     "The number of signatories is not agreed across the sources fetched for the <b>9:40 AM</b> edition",
     "open-letter signatory sources"),
])

edit('wallstreet-briefing.html', [
    ("Expectations sourced this run:",
     "Expectations, sourced in the <b>8:46 AM</b> edition and carried:", "payrolls expectations"),
    ("The source fetched this run reports that traders on the prediction market Kalshi",
     "The source fetched for the <b>9:40 AM</b> edition reports that traders on the prediction market Kalshi",
     "Kalshi source"),
    ("The source fetched this run frames next week's payrolls release",
     "That same <b>9:40 AM</b> source frames next week's payrolls release", "payrolls framing"),
])

edit('mma-briefing.html', [
    ("the four main-card bouts between the opener and the co-main come from an independent results listing "
     "fetched this run.",
     "the four main-card bouts between the opener and the co-main come from an independent results listing "
     "fetched for the <b>9:15 AM</b> edition.", "main-card listing"),
    ("it comes from post-event search results fetched this run, <b>not</b> from UFC.com",
     "it comes from post-event search results fetched for the <b>8:46 AM</b> edition, <b>not</b> from UFC.com",
     "co-main provenance"),
    ("<li><b>The finishing sequence, sourced this run.</b>",
     "<li><b>The finishing sequence, sourced in the 9:40 AM edition.</b>", "finishing sequence"),
])

if fails:
    print("FIX5 FAILURES:"); [print("  - "+f) for f in fails]; sys.exit(1)
print("fix5_1020.py: applied cleanly.")
