# -*- coding: utf-8 -*-
"""Read-through fixes, applied at source level so nothing regresses."""
import io, sys

P = "/sessions/inspiring-practical-pasteur/build_0905.py"
s = io.open(P, encoding="utf-8").read()
n = 0

def rep(old, new, label):
    global s, n
    if old not in s:
        print("MISS:", label); sys.exit(1)
    if s.count(old) != 1:
        print("AMBIG(%d):" % s.count(old), label); sys.exit(1)
    s = s.replace(old, new); n += 1
    print("ok:", label)

# ---- C1: banner wording (a flaw is not a server; "disclosed this week" was loose)
rep("""             'Five actively exploited flaws &mdash; two scored CVSS 10.0, one a supply-chain server that '
             'holds an organisation\\'s build artifacts &mdash; carry a federal remediation deadline two '
             'days out, a second federal deadline lands eleven days out, and two healthcare data '
             'incidents disclosed this week run into the millions of records.</div>')""",
    """             'Five actively exploited flaws &mdash; two scored CVSS 10.0, and one in the server that '
             'holds an organisation\\'s build artifacts &mdash; carry a federal remediation deadline two '
             'days out, a second federal deadline lands eleven days out, and two healthcare incidents in '
             'the news this week involve millions of records between them.</div>')""",
    "C1 banner")

# ---- C2: drop the unverifiable outlet attribution on the "second-largest" ranking
rep("""'affected. HIPAA Journal calls it the second-largest confirmed healthcare data breach of the '""",
    """'affected. It is reported as the second-largest confirmed healthcare data breach of the '""",
    "C2 aesto attribution")

# ---- C3: desk jargon out of the threat-actor card
rep("""             'smash-and-grab. The reporting was restated in a search return dated today, so the item is '
             'carried on a fresh fetch rather than from the earlier edition.</p></div></div>')""",
    """             'smash-and-grab. The reporting carries today\\'s date.</p></div></div>')""",
    "C3 actor jargon")

# ---- C4: do not reprint the refused Penn AG figure
rep("""             '(1) A search return again surfaced the INC Ransom attack on the Pennsylvania Attorney '
             'General\\'s Office alongside September 2026 material, this time with a 5.7 terabyte claim. '
             'The underlying coverage is dated September 2025; not published as current news, for the '
             'second consecutive edition. '""",
    """             '(1) A search return again surfaced the INC Ransom attack on the Pennsylvania Attorney '
             'General\\'s Office alongside September 2026 material, this time carrying a claimed volume '
             'of stolen data. The underlying coverage is dated September 2025; the item is not published '
             'as current news for the second consecutive edition, and the claimed figure is not '
             'reprinted. '""",
    "C4 penn ag figure")

# ---- C5: PaperCut restoration line was stale by one edition; add this run's re-fetch detail
rep("""             '<div class="note">The PaperCut pair was dropped from the earlier edition this morning '
             'because nothing in that run\\'s searches restated its deadline. It is restored here on a '
             'fresh fetch that gives the August 31 add and the September 14 due date. Countdowns above '
             'are computed from today, September 3, 2026.</div></div>')""",
    """             '<div class="note">The PaperCut pair was dropped from the 8:16 AM edition for want of a '
             'restated deadline, restored at 8:49 AM, and re-verified again for this edition: CISA added '
             'both CVEs on Monday, August 31 with a September 14 remediation date, and the vendor scores '
             'them CVE-2026-81578 at CVSS 8.8 and CVE-2026-82078 at 9.4. Coverage this week describes '
             'the attacks escalating from reconnaissance to hands-on-keyboard activity. Countdowns above '
             'are computed from today, September 3, 2026.</div></div>')""",
    "C5 papercut note")

# ---- W1: Snowflake percentage consistency across summary, tag and body
rep("""             'and are not treated as such.</p></div>')""",
    """             'and are not treated as such. This run\\'s fetch gives the pre-market move as 24%; the '
             '8:49 AM fetch gave more than 24%.</p></div>')""",
    "W1 snowflake pct")

# ---- W2: the "last trading day before September 2" claim is false (Sept 1 was a session)
rep("""             'is energy up 1.3% on <b>August 31</b> &mdash; the last trading day before September 2, and '
             'so not Wednesday\\'s session at all. Year-to-date readings are the firm ones: energy leads, '""",
    """             'is energy up 1.3% on <b>August 31</b>, which is not Wednesday\\'s session. The return '
             'describes August 31 as the last trading day before September 2; September 1 was itself a '
             'trading day, so that framing is not adopted either. Year-to-date readings are the firm '
             'ones: energy leads, '""",
    "W2 sector aug31")

# ---- W3: trade balance bullet must reflect that the release has happened
rep("""             '<li><b>Also this morning &mdash; July international trade in goods and services.</b> '
             'Expected &minus;$71.2 billion against a prior &minus;$73.26 billion.</li>'""",
    """             '<li><b>Also released at 8:30 AM ET &mdash; July international trade in goods and '
             'services.</b> No actual print appeared in anything fetched for this edition, so none is '
             'published. The consensus was &minus;$71.2 billion against a prior &minus;$73.26 '
             'billion.</li>'""",
    "W3 trade balance")

# ---- M1: desk jargon out of the top story
rep("""             'October 3. Coverage fetched for this edition puts it plainly: the event is a month away and '
             'has <b>neither a main event nor a co-main event</b>. Reporting this week says the UFC is '""",
    """             'October 3. The event is a month away and has <b>neither a main event nor a co-main '
             'event</b>. Reporting this week says the UFC is '""",
    "M1 mma jargon")

# ---- M2: the results-table note overstated what this run re-sourced
rep("""    b.append('<div class="note">Only the bouts re-sourced in this run\\'s searches are listed; '
             'this is not the full results table, and no card depth is asserted because '
             'none was re-sourced this run. Nurmagomedov entered a '""",
    """    b.append('<div class="note">This run\\'s results fetch restated the main event and the bonus '
             'awards; the co-main and the Asakura bout are carried from this desk\\'s verified record of '
             'the card. It is not the full results table, and no card depth is asserted because none has '
             'been re-sourced. Nurmagomedov entered a '""",
    "M2 results note")

# ---- M3: drop the P4P bullet from the same aggregated source that got two champion cells wrong
rep("""             '<li>Islam Makhachev sits at No. 1 on the men\\'s pound-for-pound board in aggregated '
             'rankings dated September 1; Merab Dvalishvili and Sean O\\'Malley are the top two ranked '
             'bantamweights behind the champion.</li>'""",
    """             '<li>No pound-for-pound or divisional ranking is asserted this edition. The aggregated '
             'rankings source that supplied them in earlier editions is the same one that returned two '
             'wrong champions for this build, so its unverified positions are not carried forward.</li>'""",
    "M3 rankings drop")

# ---- M4: UFC 327 date discrepancy printed rather than silently asserted
rep("""             '<tr><td><b>Light Heavyweight</b></td><td>Carlos Ulberg</td><td>Champion since April 11, 2026.</td></tr>'""",
    """             '<tr><td><b>Light Heavyweight</b></td><td>Carlos Ulberg</td>'
             '<td>Won the vacant belt at UFC 327 by first-round knockout of Ji&#345;&iacute; '
             'Proch&aacute;zka. This desk\\'s standing record dates the card April 11, 2026; Al Jazeera '
             'files its report under April 12. The discrepancy is printed, not resolved.</td></tr>'""",
    "M4 ufc327 date")

io.open(P, "w", encoding="utf-8").write(s)
print("FIXES COMPLETE:", n)
