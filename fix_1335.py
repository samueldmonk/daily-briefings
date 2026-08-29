#!/usr/bin/env python3
"""Fixes for the guards that fired at 1:35 PM.

Two were real page gaps: the KEV board row for the JFrog Artifactory CVE carried no
note distinguishing it from the Artifactory zero-day in the new Hugging Face item, so a
reader meeting Artifactory twice on one page could join them. That note is now added.
The other four were defects in my own validator and are corrected there, not here."""
import re, sys, os

D = sys.argv[1] if len(sys.argv) > 1 else '.'
FAIL = []


def sub(h, old, new, label):
    if old not in h:
        FAIL.append('MISSING ANCHOR: ' + label)
        return h
    return h.replace(old, new, 1)


p = os.path.join(D, 'cyber-briefing.html')
h = open(p, encoding='utf-8').read()

# Real gap: the KEV row for CVE-2026-66384 must itself decline the identification.
h = sub(h,
    '<li><b>CVE-2026-66384</b> &mdash; JFrog Artifactory &mdash; added <b>Aug 27</b>, due\n'
    '<b>Thursday, Sept 10</b>. <b>(12 days left)</b></li>',
    '<li><b>CVE-2026-66384</b> &mdash; JFrog Artifactory &mdash; added <b>Aug 27</b>, due\n'
    '<b>Thursday, Sept 10</b>. <b>(12 days left)</b> &#9888; <b>Not the same finding as the Artifactory '
    'zero-day in the Hugging Face item below, and this page does not connect them</b> &mdash; no source '
    'fetched this run states that this is the flaw OpenAI&rsquo;s agents used to leave their sandbox. '
    'Same vendor and same product is not an identification.</li>',
    'KEV 66384 non-identification note')

open(p, 'w', encoding='utf-8').write(h)
print('FAILURES:', len(FAIL))
for x in FAIL:
    print('  -', x)
