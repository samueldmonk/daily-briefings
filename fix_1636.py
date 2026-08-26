#!/usr/bin/env python3
"""Fixes the one REAL page bug the 1636 harness caught: the Gitea enrichment note was
appended to the WRONG KEV row. edits_1636.py searched the KEV section for the string
'CVE-2026-60004', but the section opens with prose that cross-references that CVE, so
index() landed in the intro and the following '</li>' closed the FIRST row -- Oracle
CVE-2026-21962. Result: Gitea's CVSS, fixed version and Habr provenance were printed
inside an Oracle row. This is the Gitea/Oracle conflation the standing corrections warn
about, produced this time by our own edit script rather than by a search summary.
Fix: cut the note out and re-insert it at the end of the row that actually contains the
Gitea CVE in a <b> tag."""
import io, os, re, sys

D = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(D, 'cyber-briefing.html')
cy = io.open(p, encoding='utf-8').read()

start = cy.index('  <b>&#9679; Updated 4:36:</b> confirmed this run')
end = cy.index('Patch Priority box carries.', start) + len('Patch Priority box carries.')
note = cy[start:end]
cy = cy[:start] + cy[end:]
assert 'Updated 4:36' not in cy, 'note not fully removed'

# Re-target: the row whose CVE *label* is the Gitea one.
m = re.search(r'<li>(?:(?!</li>).)*<b>CVE-2026-60004</b>(?:(?!</li>).)*</li>', cy, re.S)
assert m, 'Gitea KEV row not found'
row = m.group(0)
assert 'Gitea' in row, 'targeted row is not the Gitea row'
assert 'Oracle' not in row, 'targeted row mentions Oracle'
cy = cy[:m.start()] + row[:-len('</li>')] + note + '</li>' + cy[m.end():]

io.open(p, 'w', encoding='utf-8').write(cy)

# Prove it landed correctly.
m2 = re.search(r'<li>(?:(?!</li>).)*Updated 4:36(?:(?!</li>).)*</li>', cy, re.S)
row2 = m2.group(0)
print('note now in row containing CVE-2026-60004:', '<b>CVE-2026-60004</b>' in row2)
print('that row mentions Oracle:', 'Oracle' in row2)
print('Oracle row still clean:', 'Updated 4:36' not in re.search(
    r'<li>(?:(?!</li>).)*CVE-2026-21962(?:(?!</li>).)*</li>', cy, re.S).group(0))
sys.exit(0 if ('<b>CVE-2026-60004</b>' in row2 and 'Oracle' not in row2) else 1)
