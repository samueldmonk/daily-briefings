#!/usr/bin/env python3
# Three guard hits from validate_1805: 1 REAL DEFECT (index lost the Paris price),
# 2 guards NARROWED (never loosened) after inspecting what actually fired.
import os, re
D = os.path.dirname(os.path.abspath(__file__))

# ── REAL DEFECT: the index MMA card dropped the -600 line the page leads with ──
p = os.path.join(D,'index.html'); h = open(p,encoding='utf-8').read()
old = '<b>The champions board is unchanged for an eightieth straight edition.</b></p>'
new = ('and is the plainest account yet of why an unbeaten debutant is a <b>&minus;600</b> favourite over <b>Dan Hooker</b> at <b>+430</b>. '
       '<b>The champions board is unchanged for an eightieth straight edition.</b></p>')
assert old in h
h = h.replace(old, new, 1); open(p,'w',encoding='utf-8').write(h)
print('index.html: REAL DEFECT fixed — Paris price restored to the MMA card')

# ── Reword the KEV recap so it stops restating dates already boarded below ─────
p = os.path.join(D,'cyber-briefing.html'); h = open(p,encoding='utf-8').read()
old = ('<b>Their due dates run from August 29 to September 9</b>, which is <b>direct confirmation that KEV deadlines are assigned per-CVE and risk-based</b>, not on the retired three-week rule. '
       '<b>All are already past or nearly past; the September 14 PaperCut date remains the live federal clock on this page.</b>')
new = ('<b>Every one of those identifiers already sits on the KEV board below with its own countdown</b>, and the spread of dates they were assigned '
       'is <b>direct confirmation that CISA assigns remediation windows per-CVE and risk-based</b>, not on the retired three-week rule. '
       '<b>Nothing here changes a single countdown; the board was computed against today and today has not moved.</b>')
assert old in h, 'KEV recap sentence not found'
h = h.replace(old, new, 1); open(p,'w',encoding='utf-8').write(h)
print('cyber-briefing.html: KEV recap deduplicated against the board it was restating')
