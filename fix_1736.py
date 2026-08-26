#!/usr/bin/env python3
"""Fix the real defect the 5:36 harness exposed: the MiniOrange CVEs were ALREADY on
this page (Patch Priority, since the 11:05 edition) WITH numeric CVSS scores from
The Hacker News. The row added at 5:36 duplicated them and, worse, asserted that no
numeric score existed. Remove the duplicate row; fold the new Patchstack/SecurityWeek
corroboration into the existing Patch Priority box instead; correct the tldr."""
import io, os, sys

O = os.path.dirname(os.path.abspath(__file__))
fails = []


def rep(h, old, new, label, count=1):
    n = h.count(old)
    if n != count:
        fails.append('%s: found %d, expected %d' % (label, n, count))
        return h
    return h.replace(old, new)


c = io.open(os.path.join(O, 'cyber-briefing.html'), encoding='utf-8').read()

# --- 1. cut the duplicate MiniOrange table row entirely
i = c.find('<tr><td>CVE-2026-61979 and CVE-2026-15981')
if i < 0:
    fails.append('dup row: not found')
else:
    j = c.find('</tr>', i) + 5
    row = c[i:j]
    if 'Not stated in the coverage fetched this run' not in row:
        fails.append('dup row: wrong row targeted')
    else:
        c = c[:i] + c[j:]

# --- 2. fold ONLY the genuinely new detail into the existing Patch Priority box.
# Everything else SecurityWeek reports (the Patchstack quote, the opportunistic
# characterisation, the DigitalOcean credit) is ALREADY on this page from 11:05.
ANCH = '<b>Fixed in version 17.0.5 (61979) and 17.0.6 (15981) for the Standard edition.</b>'
if c.count(ANCH) != 1:
    fails.append('patch priority: anchor found %d times' % c.count(ANCH))
else:
    ADD = (ANCH + ' <b>&#9679; New &middot; 5:36 &mdash; the FREE edition has a different fix and a different version '
           'number, and that is the trap.</b> <b>SecurityWeek</b>, working from the same DigitalOcean and Patchstack '
           'analysis already summarised here, adds that <b>the free edition is fixed in version 5.4.5</b> &mdash; and '
           'that <b>its advisory lists that fix as a BUGFIX rather than a security patch.</b> '
           '<b>&#9888; THE PAID AND ENTERPRISE EDITIONS WERE NOT NOTIFIED AT ALL</b>, and because they use a '
           '<b>different versioning scheme from the free edition</b>, an administrator <b>cannot tell from a version '
           'number alone whether the site is patched and has to update manually.</b> That is why the two version sets '
           'on this page do not contradict each other: <b>5.4.5 is the free edition, 17.0.5 / 17.0.6 the Standard '
           'edition.</b> The free edition alone runs on <b>more than 10,000 sites</b>; paid-edition install counts are '
           'not published. (SecurityWeek, Aug&nbsp;25.)')
    c = c.replace(ANCH, ADD)

# --- 3. correct the tldr: MiniOrange is corroboration, not the day's new item
old = c[c.find('<div class="tldr"><b>The Wire</b>'):]
old = old[:old.find('</div>') + 6]
if old.count('The Wire') != 1:
    fails.append('tldr: could not isolate')
else:
    new = ('<div class="tldr"><b>The Wire</b> <span>The run&rsquo;s new material is two emptied vendor queues and three '
           'incidents: <b>NVIDIA published four advisories, one covering 18 flaws in its NemoClaw and OpenShell AI-agent '
           'runtime products, two of them critical</b>, and <b>Adobe shipped seven advisories with critical code-execution '
           'fixes in five products</b>; <b>Nutex Health has told the SEC that data was exfiltrated</b> and '
           '<b>ReliaQuest has confirmed a ShinyHunters intrusion that began with one phished employee</b>. '
           'Patch Priority is unchanged &mdash; <b>the miniOrange WordPress login bypass already on this board picks up '
           'one dangerous new detail, that the free edition&rsquo;s fix (version 5.4.5) is published as a bugfix and '
           'paid editions were never notified</b> &mdash; and <b>CISA&rsquo;s KEV catalogue is static for a fifteenth '
           'consecutive edition</b>, '
           'with <b>Oracle CVE-2026-21962 due tomorrow</b>.</span></div>')
    c = rep(c, old, new, 'tldr')

# --- 4. a current-edition KEV status line, so the section is not only "carried"
KA = '<div class="lab">CISA KEV &amp; federal deadlines</div>\n'
if c.count(KA) != 1:
    KA = '<div class="lab">CISA KEV &amp; federal deadlines</div>'
NEWK = (KA + '<p class="note"><b>&#9679; New &middot; 5:36 &mdash; KEV static, fifteenth consecutive edition.</b> '
        'Searches this run again surfaced <b>no CISA alert page later than those already on this board</b>. '
        'The board holds at <b>14 rows</b>, the two nearest deadlines are <b>Oracle CVE-2026-21962 on August&nbsp;27</b> '
        'and <b>Gitea CVE-2026-60004 on August&nbsp;28</b>, and <b>the Adobe and NVIDIA advisories published this week '
        'are NOT in KEV and carry no federal deadline.</b></p>\n')
c = rep(c, KA, NEWK, 'kev status line')

# (write deferred to the end)

# --- 5. index security card: match the corrected cyber lead
x = io.open(os.path.join(O, 'index.html'), encoding='utf-8').read()
x = rep(x,
  '<p><b>NVIDIA shipped four advisories &mdash; one covering 18 flaws in its AI-agent runtime products, two of them '
  'critical &mdash; and Adobe seven</b>, while two <b>critical authentication bypasses in the MiniOrange SAML SSO '
  'plugin</b> are being sprayed at every WordPress site running it. <b>CISA&rsquo;s KEV list is unchanged; Oracle '
  'CVE-2026-21962 is due tomorrow.</b></p>',
  '<p><b>NVIDIA shipped four advisories &mdash; one covering 18 flaws in its AI-agent runtime products, two of them '
  'critical &mdash; and Adobe seven.</b> <b>Nutex Health has told the SEC that data was exfiltrated</b> and '
  '<b>ReliaQuest has confirmed a ShinyHunters intrusion.</b> KEV is unchanged; <b>Oracle CVE-2026-21962 is due '
  'tomorrow.</b></p>', 'index sec p')

if fails:
    print('FAILED:')
    for f in fails:
        print('  -', f)
    sys.exit(1)
io.open(os.path.join(O, 'cyber-briefing.html'), 'w', encoding='utf-8').write(c)
io.open(os.path.join(O, 'index.html'), 'w', encoding='utf-8').write(x)
print('OK - duplicate MiniOrange row removed, corroboration folded into Patch Priority')
