#!/usr/bin/env python3
"""Targeted edits onto the 9:40 AM edition -> 10:20 AM edition (Sat Aug 29 2026).

Story of this run:
  MMA    - UFC Shanghai BONUSES ANNOUNCED (sixth check). Four fighters, $100,000 each.
  CYBER  - ATF confirms "major incident"; Qilin claims it. GPUThor Rowhammer defeats ECC.
  MARKET - weekend, no new session; Friday closes re-verified a SIXTH time.

Freshness discipline (per CORRECTIONS.md, 9:49 entry): stamps are NOT blanket-rewritten.
Every carried item is demoted EXPLICITLY before the new ones are stamped.
"""
import io, os, sys, re

D = os.path.dirname(os.path.abspath(__file__))
OLD, NEW = "9:40 AM", "10:20 AM"

def rd(p):
    with io.open(os.path.join(D, p), encoding="utf-8") as f:
        return f.read()

def wr(p, s):
    with io.open(os.path.join(D, p), "w", encoding="utf-8") as f:
        f.write(s)

fails = []
def sub(s, old, new, label, count=1):
    """Replace exactly `count` occurrences; record a failure if the count is wrong."""
    n = s.count(old)
    if n != count:
        fails.append("%s: expected %d occurrence(s), found %d" % (label, count, n))
        return s
    return s.replace(old, new)

# ----------------------------------------------------------------------------
# 1. CYBER
# ----------------------------------------------------------------------------
cy = rd("cyber-briefing.html")

# 1a. DEMOTE the two items that were new/updated at 9:40 -- they are carried now.
cy = sub(cy,
    '<span class="tag new">New &middot; 9:40 AM</span><span class="tag crit">Healthcare</span>',
    '<span class="tag">Carried</span><span class="tag crit">Healthcare</span>',
    "cyber demote CareCloud")
cy = sub(cy,
    '<span class="tag new">Updated &middot; 9:40 AM</span><span class="tag crit">Medical devices</span>',
    '<span class="tag">Carried</span><span class="tag crit">Medical devices</span>',
    "cyber demote Boston Scientific")
# and the prose inside Boston Scientific that says "New this run" -- it was new at 9:40.
cy = sub(cy, "New this run: <b>thousands of employees in Ireland</b>",
             "Added in the 9:40 AM edition: <b>thousands of employees in Ireland</b>",
             "cyber BSX stale-novelty")

# 1b. NEW breach card: ATF / Qilin. Inserted at the head of Breaches & Incidents.
ATF = (
'<div class="card"><div class="tags"><span class="tag new">New &middot; ' + NEW + '</span>'
'<span class="tag crit">Federal</span><span class="tag warn">Claim unattributed</span></div>\n'
'<h4>ATF &mdash; a federal agency confirms a &ldquo;major incident&rdquo;</h4>\n'
'<p>The <b>Bureau of Alcohol, Tobacco, Firearms and Explosives</b> confirmed a cybersecurity <b>&ldquo;major '
'incident&rdquo;</b> in a press release on <b>August 26</b>. The compromised system is <b>standalone</b> and held '
'information tied to <b>ATF investigations</b>; the agency says the system <b>operates separately from the ATF '
'enterprise network</b> and that there is <b>no indication</b> the incident affected the enterprise network, the '
'<b>ATF eForms</b> system, or any other ATF system. &#9888; <b>The attribution is a claim, not a finding, and this '
'page keeps the two apart.</b> The <b>Qilin</b> ransomware group listed ATF on its dark-web leak site on <b>the same '
'day</b>, August 26. But <b>ATF itself has not attributed the incident to Qilin</b>, has not commented on the claim, '
'and has named no attacker; and the group posted <b>no evidence, no file samples, no data-volume figure and no public '
'ransom demand</b>. <b>The confirmation and the claim are both real; the link between them is not established by any '
'source seen this run, and none is asserted here.</b></p></div>\n')
cy = sub(cy, '<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">\n',
             '<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">\n' + ATF,
             "cyber insert ATF card")

# 1c. NEW Vulnerability Watch row: GPUThor. No CVE was stated by any source this run,
#     so no identifier is invented -- the cell says so.
GPU = (
'<tr><td><b>GPUThor</b><br><span class="mono" style="font-size:11px">no CVE stated</span></td>'
'<td>Not stated</td><td>NVIDIA Ampere workstation GPUs with GDDR6 &mdash; RTX A4000, A4500, A5000, A6000; '
'server-class A100 for privilege escalation</td>\n'
'<td><b>New &middot; ' + NEW + '.</b> A Rowhammer attack from University of Toronto researchers that '
'<b>defeats error-correcting code</b> on the affected cards, giving <b>denial of service and root-level privilege '
'escalation on the host</b>. Reported to produce <b>up to 23,500&times; more bit flips</b> than the first GPU '
'Rowhammer attack and to complete <b>end-to-end privilege escalation on an A6000 in 1.1 minutes</b>, against '
'<b>21.9 hours</b> for the previous best technique. Privilege escalation still works on the <b>A100</b> because it '
'relies on SECDED-level ECC. <b>Precondition:</b> the attacker must be able to launch an <b>unprivileged CUDA '
'kernel</b> on the target GPU &mdash; as a co-tenant on a shared card, or as untrusted code on a single-tenant '
'machine. Disclosed to NVIDIA <b>April 29</b>; NVIDIA published guidance on <b>August 21</b>. '
'<b>No CVE identifier and no CVSS score was stated by any source seen this run, so neither is printed</b>, and this '
'is <b>not</b> a KEV item &mdash; it does not belong in the deadline list below.</td></tr>\n')
cy = sub(cy, '<tr><td><b>CVE-2026-8452</b></td>', GPU + '<tr><td><b>CVE-2026-8452</b></td>',
             "cyber insert GPUThor row")

# 1d. KEV re-verification note for this run (direct CISA fetch returned an empty body).
cy = sub(cy,
    '<div class="note">These windows are assigned per-CVE under <b>BOD 26-04</b>,',
    '<div class="note"><b>Re-verified at ' + NEW + ', on weaker provenance than a direct read, and the page says '
    'so.</b> A <b>direct fetch of CISA&rsquo;s own August 26 alert page returned an empty body</b> this run. The '
    'batch was therefore confirmed from <b>search results that enumerate all six CVEs of that batch by identifier</b> '
    '&mdash; CVE-2015-3246, CVE-2015-5287, CVE-2019-1068, CVE-2021-23758, CVE-2022-0995 and CVE-2026-8452 &mdash; '
    'matching the standing record exactly, with <b>no new KEV batch added since August 26</b>. A snippet-mediated read '
    'of a primary source is not the same as reading it, and the difference is printed rather than smoothed over. '
    'These windows are assigned per-CVE under <b>BOD 26-04</b>,',
    "cyber KEV provenance note")

# 1e. TLDR -- swap the trailing CareCloud clause for the new ATF item.
CY_TLDR_OLD = ('Two federal remediation deadlines expire today &mdash; the exploited Citrix NetScaler flaw and a '
 '2019 SQL Server bug &mdash; PaperCut&rsquo;s researchers say new bypasses affect even the latest fully patched '
 'build, and CareCloud&rsquo;s March intrusion has now been filed with regulators at 3,756,469 people, among the '
 'largest healthcare breaches of the year.')
CY_TLDR_NEW = ('Two federal remediation deadlines expire today &mdash; the exploited Citrix NetScaler flaw and a '
 '2019 SQL Server bug &mdash; PaperCut&rsquo;s researchers say new bypasses affect even the latest fully patched '
 'build, and the ATF has confirmed a cybersecurity &ldquo;major incident&rdquo; on a standalone system holding '
 'investigation records, which the Qilin group has claimed without evidence and the agency has not attributed to '
 'anyone.')
cy = sub(cy, CY_TLDR_OLD, CY_TLDR_NEW, "cyber tldr")

# 1f. Stamps.
cy = cy.replace(OLD, NEW)
wr("cyber-briefing.html", cy)

# ----------------------------------------------------------------------------
# 2. MMA
# ----------------------------------------------------------------------------
mm = rd("mma-briefing.html")

# 2a. DEMOTE the Noche UFC 4 card -- it was updated at 9:40, not now.
mm = sub(mm, '<div class="card"><div class="tags"><span class="tag new">Updated &middot; 9:40 AM</span></div>\n'
             '<div class="dateline">Sat, Sept 12',
             '<div class="card"><div class="tags"><span class="tag">Carried</span></div>\n'
             '<div class="dateline">Sat, Sept 12',
             "mma demote Noche UFC 4")
mm = sub(mm, "The 9:15 edition could verify only the date and the event name. <b>Both the venue and the "
             "headliner are sourced this run</b>",
             "The 9:15 edition could verify only the date and the event name. <b>The venue and the headliner "
             "were sourced in the 9:40 AM edition</b>",
             "mma Noche stale-novelty")

# 2b. THE LEAD OF THIS RUN -- bonuses. Replace the results-table note.
BON_OLD = ('<b>Performance bonuses: still none announced in any source seen this run</b> &mdash; and the main event '
 'is now <b>resolved</b>, so the earlier explanation for the silence no longer applies. This is the <b>fifth</b> '
 'consecutive check with nothing announced. <b>Three fighters missed weight</b>')
BON_NEW = ('<b>Performance bonuses: ANNOUNCED, at the sixth check, and printed here for the first time.</b> '
 '<b>Four fighters take home $100,000 each</b>, announced after the card by <b>Kevin Chang</b>, UFC senior vice '
 'president and head of Asia. <b>Fight of the Night: Liu Ce vs. Levi Rodrigues Jr.</b> &mdash; both men paid. '
 '<b>Performance of the Night: Song Yadong</b> and <b>Bilal Hasan</b>. The same report puts the card at '
 '<b>ten finishes</b>, which is the count this page has carried, and calls it the promotion&rsquo;s '
 '<b>third visit to the venue</b>. <b>Three fighters missed weight</b>')
mm = sub(mm, BON_OLD, BON_NEW, "mma bonuses (results note)")

# 2c. Around the Sport -- replace the "still no bonuses" bullet.
ATS_OLD_START = '<li><b>Still no bonuses, on a fifth check &mdash; and one name is already ruled out.</b>'
i = mm.find(ATS_OLD_START)
j = mm.find('</li>', i)
if i < 0 or j < 0:
    fails.append("mma: could not locate the 'still no bonuses' bullet")
else:
    ATS_NEW = ('<li><b>The bonuses landed, and the two fighters this page had already ruled out stayed ruled out.</b> '
     'UFC senior vice president and head of Asia <b>Kevin Chang</b> announced <b>one Fight of the Night and two '
     'Performance of the Night awards</b> after the card, <b>$100,000</b> apiece to <b>four fighters</b>: '
     '<b>Liu Ce</b> and <b>Levi Rodrigues Jr.</b> for the light-heavyweight Fight of the Night, and <b>Song Yadong</b> '
     'and <b>Bilal Hasan</b> for Performance of the Night. Neither <b>Julia Polastri</b> nor <b>Andre Lima</b> is on '
     'the list &mdash; both missed weight, and both were recorded here as ineligible before the awards were known. '
     'The live blog&rsquo;s assessment that Polastri <i>would have</i> won one for her head-kick knockout had she made '
     'weight is left standing as what it was: <b>a reporter&rsquo;s assessment, now overtaken by the actual '
     'announcement</b>. Five consecutive editions of this page said no bonuses had been announced and declined to '
     'guess at them; this is the edition that could print them.</li>')
    mm = mm[:i] + ATS_NEW + mm[j+5:]

# 2d. Top Story -- the finishing-sequence bullet now has a second, differing description.
SEQ_OLD = ('One outlet describes him as knocked out cold. The official method is recorded as <b>knockout '
 '(punch)</b>.</li>')
SEQ_NEW = ('One outlet describes him as knocked out cold. The official method is recorded as <b>knockout '
 '(punch)</b>. &#9888; <b>A second account sourced at ' + NEW + ' describes the same punch differently</b>, and '
 'both are printed rather than reconciled: the bonus report calls it a <b>right uppercut landed behind the ear</b>, '
 'followed by <b>punches and hammerfists</b> on the ground, and frames round one as Song <i>seemingly losing</i> it. '
 'The first account calls the finishing blow a <b>hook thrown as Nurmagomedov shot for a takedown</b>. <b>Winner, '
 'method category, round and the 1:48 mark agree across every source; the punch itself does not, and no version is '
 'adopted.</b> The same report notes Song trains as a <b>Team Alpha Male</b> associate.</li>')
mm = sub(mm, SEQ_OLD, SEQ_NEW, "mma finishing-sequence discrepancy")

# 2e. UFC.com lag is now on a SIXTH fetch (fetched again this run; modified_time unmoved).
mm = sub(mm, '&#9888; <b>UFC.com is still behind, on a fifth consecutive fetch.</b>',
             '&#9888; <b>UFC.com is still behind, on a sixth consecutive fetch.</b>',
             "mma UFC.com lag count (top story)")
mm = sub(mm, 'The promotion&rsquo;s own main-card results page was fetched again during this run and is '
             '<b>still carrying the pre-event preview</b>',
             'The promotion&rsquo;s own main-card results page was fetched directly again at ' + NEW + ' and is '
             '<b>still carrying the pre-event preview</b>',
             "mma UFC.com lag wording")

# 2f. The completed-event card gains the bonus line -- a genuine update, so it is stamped.
mm = sub(mm, '<div class="card"><div class="tags"><span class="tag">Completed</span></div>\n'
             '<div class="dateline">Sat, Aug 29 &middot; Oriental Sports Center, Shanghai</div>',
             '<div class="card"><div class="tags"><span class="tag new">Updated &middot; ' + NEW + '</span>'
             '<span class="tag">Completed</span></div>\n'
             '<div class="dateline">Sat, Aug 29 &middot; Oriental Sports Center, Shanghai</div>',
             "mma stamp completed card")

# 2g. TLDR -- add the bonuses.
MM_TLDR_OLD = ('Song Yadong knocked out Umar Nurmagomedov in the second round of the UFC Shanghai main event, ending '
 'the No. 3 bantamweight&rsquo;s title-shot claim in front of a home crowd, on a card where ten of thirteen bouts '
 'finished inside the distance and Denise Gomes stopped a fighter ten places above her in the co-main.')
MM_TLDR_NEW = ('Song Yadong knocked out Umar Nurmagomedov in the second round of the UFC Shanghai main event, ending '
 'the No. 3 bantamweight&rsquo;s title-shot claim in front of a home crowd, on a card where ten of thirteen bouts '
 'finished inside the distance &mdash; and the promotion has now announced the bonuses, $100,000 each to Song and '
 'Bilal Hasan for Performance of the Night and to Liu Ce and Levi Rodrigues Jr. for Fight of the Night.')
mm = sub(mm, MM_TLDR_OLD, MM_TLDR_NEW, "mma tldr")

mm = mm.replace(OLD, NEW)
wr("mma-briefing.html", mm)

# ----------------------------------------------------------------------------
# 3. MARKETS -- weekend, no new session. Stamps + a sixth re-verification note.
# ----------------------------------------------------------------------------
ws = rd("wallstreet-briefing.html")
ws = sub(ws, "Friday closes re-verified a fifth time", "Friday closes re-verified a sixth time",
             "markets re-verify count", count=ws.count("Friday closes re-verified a fifth time"))
ws = ws.replace(OLD, NEW)
wr("wallstreet-briefing.html", ws)

# ----------------------------------------------------------------------------
# 4. INDEX -- cards must stay byte-identical to each page's tldr.
# ----------------------------------------------------------------------------
ix = rd("index.html")
ix = sub(ix, CY_TLDR_OLD, CY_TLDR_NEW, "index cyber card")
ix = sub(ix, MM_TLDR_OLD, MM_TLDR_NEW, "index mma card")
ix = sub(ix, "and a main event published from corroborated secondary reporting while the promotion's own page "
             "still lagged on a fifth fetch",
             "a main event published from corroborated secondary reporting while the promotion's own page still "
             "lagged on a sixth fetch, a federal breach confirmation kept apart from the leak-site claim attached "
             "to it, and a GPU attack printed with no CVE because none was stated",
             "index sources note")
ix = ix.replace(OLD, NEW)
wr("index.html", ix)

# ----------------------------------------------------------------------------
if fails:
    print("EDIT FAILURES (%d):" % len(fails))
    for f in fails:
        print("  - " + f)
    sys.exit(1)
print("edits_1020.py: all edits applied cleanly.")
