#!/usr/bin/env python3
"""GOTCHA #56 — caught by the harness, fixed rather than suppressed.

edits_1806.py added a Vulnerability Watch note and a Breaches card for items that were
ALREADY ON THIS PAGE: Keycloak CVE-2026-18963, Marimo CVE-2026-75149, the Oasis Security
NemoClaw research, Chrome 152, and Mirage2FA were all published in earlier editions today,
several of them in MORE detail than the new copy (the existing NemoClaw item names Elad Luz
and the PSIRT report; the existing Mirage2FA item carries the same ANY.RUN figures).  The
Gitea "patched in late July in 1.27.1" line was likewise already on the board twice.

This is the rule from GOTCHA #55 recurring: BEFORE adding an item, grep the whole page for
it.  Fresh coverage of an old item is corroboration, not a new entry.  The duplicates are
deleted here and only the genuinely new material — Apollo Global and the Taiwan charges —
survives.  Deferred write.
"""
import os, re, sys

D = os.path.dirname(os.path.abspath(__file__))
CY, IDX = 'cyber-briefing.html', 'index.html'
docs = {CY: open(os.path.join(D, CY)).read(), IDX: open(os.path.join(D, IDX)).read()}
fails = []


def cut(name, start_marker, end_marker, label, replacement=''):
    h = docs[name]
    i = h.find(start_marker)
    if i < 0:
        fails.append('CUT START MISSING [%s / %s]' % (name, label))
        return
    j = h.find(end_marker, i)
    if j < 0:
        fails.append('CUT END MISSING [%s / %s]' % (name, label))
        return
    docs[name] = h[:i] + replacement + h[j + len(end_marker):]


def sub(name, old, new, label):
    h = docs[name]
    if h.count(old) != 1:
        fails.append('SUB ANCHOR [%s / %s]: %d occurrences' % (name, label, h.count(old)))
        return
    docs[name] = h.replace(old, new, 1)


# ---- 1. Replace the duplicated Vulnerability Watch note with an honest corroboration note.
corrob = (
 '<p class="note"><b>&#9679; New &middot; 6:06 &mdash; a self-check, and it caught this desk adding items it had '
 'already published.</b> Tonight&rsquo;s sweep of The Hacker News and SecurityWeek returned <b>Keycloak '
 'CVE-2026-18963, Marimo CVE-2026-75149, the Oasis Security NemoClaw research and Chrome&nbsp;152</b> &mdash; '
 '<b>all four are already on this page below, several of them in more detail than the new coverage</b> (the '
 'NemoClaw entry already names Oasis&rsquo;s <b>Elad Luz</b> and the report to NVIDIA&rsquo;s PSIRT; the '
 'Mirage2FA entry already carries the same ANY.RUN figures). <b>The draft rows were written and then deleted '
 'rather than published.</b> Likewise the Gitea line that <b>CVE-2026-60004 was patched in 1.27.1 in late '
 'July</b> &mdash; fresh in SecurityWeek this evening, but on this board since this morning. '
 '<b>RULE (restated): fresh coverage of an old item is corroboration, not a new entry &mdash; grep the page for '
 'the identifier before adding a row.</b> <b>Genuinely new tonight: nothing in this section.</b> '
 '(The Hacker News; SecurityWeek, Aug&nbsp;26.)</p>\n')
cut(CY, '<p class="note"><b>&#9679; New &middot; 6:06 &mdash; three flaws that are not in KEV',
    '(The Hacker News; SecurityWeek.)</p>\n', 'dup vuln note', corrob)

# ---- 2. Delete the duplicated Mirage2FA breach card.
cut(CY, '<div class="card"><div class="tags"><span class="tag new">New &middot; 6:06</span>'
        '<span class="tag warn">Phishing-as-a-service</span>',
    '(The Hacker News, citing ANY.RUN.)</p></div>\n', 'dup Mirage2FA card')

# ---- 3. KEV note: drop the "new detail" claim, keep the static streak + the re-confirmation.
sub(CY,
 '<b>&#9679; New detail on the '
 'Gitea row:</b> SecurityWeek reports the flaw was <b>patched by Gitea&rsquo;s developers in late July with the '
 'release of version 1.27.1</b> &mdash; the same fixed version already on this board &mdash; which means <b>a fix '
 'existed for roughly a month before CISA listed the bug as exploited.</b> <b>&#9888; The federal deadline is '
 'unaffected by that; the patch gap is a defender&rsquo;s framing, not a change to the due date.</b> '
 '(SecurityWeek, Aug&nbsp;26.)</p>\n',
 '<b>&#9888; NOT A NEW DETAIL, THOUGH IT ARRIVED AS ONE:</b> '
 'SecurityWeek&rsquo;s Gitea write-up this evening states the flaw was <b>patched in version 1.27.1 in late '
 'July</b> &mdash; which is <b>already on this board, twice, and has been since this morning.</b> It is recorded '
 'here as <b>independent corroboration of the fixed version</b>, not as an addition. The only framing worth '
 'drawing from it is the <b>patch gap</b>: a fix existed for roughly a month before CISA listed the bug as '
 'exploited. <b>&#9888; That changes nothing about the August&nbsp;28 federal deadline.</b> '
 '(SecurityWeek, Aug&nbsp;26.)</p>\n',
 'kev note')

# ---- 4. Cyber tldr: lead on what is actually new.
m = re.search(r'<div class="tldr"><b>The Wire</b> <span>.*?</span></div>', docs[CY], re.S)
if not m:
    fails.append('cyber tldr not found')
else:
    docs[CY] = docs[CY][:m.start()] + (
        '<div class="tldr"><b>The Wire</b> <span>Two genuinely new items, and the rest of tonight&rsquo;s sweep '
        'turned out to be corroboration of what this page already carried. <b>Apollo Global Management has '
        'confirmed that a social-engineering intrusion reached its cloud platforms between July&nbsp;6 and '
        'July&nbsp;10 and exposed names, dates of birth, addresses, contact details and Social Security '
        'numbers</b> &mdash; no victim count disclosed, no client funds taken, and part of a wave of help-desk-'
        'impersonation calls against private equity and financial firms; and <b>Taiwanese prosecutors have '
        'charged nine people, including Nvidia and Super Micro employees, over illegal AI server exports to '
        'China.</b> <b>Everything else returned tonight &mdash; Keycloak, Marimo, NemoClaw, Chrome&nbsp;152, '
        'Mirage2FA, the Gitea patch date &mdash; was already published here and was deliberately not re-added.</b> '
        '<b>Patch Priority is unchanged, Oracle CVE-2026-21962 is due tomorrow, and KEV is static for a sixteenth '
        'consecutive edition.</b></span></div>') + docs[CY][m.end():]

# ---- 5. Index cyber card must match the rewritten lead.
sub(IDX,
 '<p><b>Apollo Global Management says a social-engineering intrusion reached its cloud platforms between '
 'July&nbsp;6 and July&nbsp;10 and exposed names, dates of birth, addresses and Social Security numbers</b> '
 '&mdash; no count disclosed, no client funds taken. <b>A CVSS 9.1 Keycloak password-reset takeover</b> and an '
 '<b>NVIDIA NemoClaw model-poisoning flaw with no CVE and no Windows fix</b> join the board; KEV is static and '
 '<b>Oracle CVE-2026-21962 is due tomorrow.</b></p>',
 '<p><b>Apollo Global Management says a social-engineering intrusion reached its cloud platforms between '
 'July&nbsp;6 and July&nbsp;10 and exposed names, dates of birth, addresses and Social Security numbers</b> '
 '&mdash; no count disclosed, no client funds taken. <b>Taiwan has charged nine people, Nvidia and Super Micro '
 'staff among them, over illegal AI server exports to China.</b> The rest of tonight&rsquo;s sweep was '
 'corroboration of items already on the board; KEV is static and <b>Oracle CVE-2026-21962 is due tomorrow.</b></p>',
 'index cyber card')

if fails:
    print('FAILED — NOTHING WRITTEN')
    for f in fails:
        print('  ' + f)
    sys.exit(1)
for n, h in docs.items():
    open(os.path.join(D, n), 'w').write(h)
print('OK — duplicates removed from cyber-briefing.html, index.html resynced')
