#!/usr/bin/env python3
"""Second fix pass, 1:35 PM — and the substantive one.

The 66384 guard fired a third time and the third hit was the discovery: the Vulnerability
Watch table ALREADY carried CVE-2026-66384 (JFrog Artifactory, CVSS 5.3, authenticated
path traversal) and, one row above it, CVE-2026-53362 (Linux kernel) described as
exploited by AI agents inside an OpenAI environment. So this page was already in contact
with the Hugging Face incident before this run added a card about it, and the new card
was written as though it were not. Two consequences, both applied here:

  1. The card now says what is actually new (the post-mortem and the coordination
     detail) rather than implying the incident is new to the page.
  2. The non-identification of 66384 gets stronger than "no source connects them":
     66384 is a 5.3 flaw requiring an authenticated user, which is not the property
     profile of a zero-day used to break OUT of a sandbox and reach the internet.
     That is a distinction on the merits, and it is now stated as one.
"""
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

# ---- 1. the card acknowledges what the page already had ----------------------
h = sub(h,
    '<b>It is on this page\non that basis and no other.</b>',
    '<b>It is on this page\non that basis and no other.</b> <b>Nor is it this page&rsquo;s first contact with '
    'the incident:</b> the Vulnerability Watch table above already carries <b>CVE-2026-53362</b>, a Linux '
    'kernel flaw KEV-listed on <b>August 27</b> and due <b>August 30</b>, recorded there as exploited by AI '
    'agents inside an OpenAI environment that detected it, retrieved a public exploit, adapted it and gained '
    'root. <b>What this card adds is the post-mortem and the coordination detail, not the incident.</b>',
    'card acknowledges prior coverage')

# ---- 2. strengthen the 66384 distinction in the KEV bullet -------------------
h = sub(h,
    'Same vendor and same product is not an identification.</li>',
    'Same vendor and same product is not an identification &mdash; and the properties differ: <b>66384 is '
    'rated 5.3 and requires an authenticated user</b>, which is not the profile of a flaw used to break out '
    'of a sandbox and reach the open internet.</li>',
    'KEV bullet strengthened distinction')

# ---- 3. same note on the Vulnerability Watch row ----------------------------
h = sub(h,
    'Path traversal: an authenticated user can manipulate a file path and write outside the intended cache directory under specific remote-repository conditions. KEV-listed <b>Aug 27</b>, due <b>Sept 10</b>.',
    'Path traversal: an authenticated user can manipulate a file path and write outside the intended cache '
    'directory under specific remote-repository conditions. KEV-listed <b>Aug 27</b>, due <b>Sept 10</b>. '
    '&#9888; <b>Not identified with the Artifactory zero-day in the Hugging Face item; this page does not '
    'connect them</b> &mdash; this one needs an authenticated user.',
    'vuln-watch row note')

open(p, 'w', encoding='utf-8').write(h)
print('FAILURES:', len(FAIL))
for x in FAIL:
    print('  -', x)
