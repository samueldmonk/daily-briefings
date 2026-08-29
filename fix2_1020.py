# -*- coding: utf-8 -*-
"""Second fix pass, 10:20 AM edition -- five errors caught in the FINAL READ-THROUGH
after validate_1020.py passed with 553 checks and 0 failures.

  1. ws   - the sixth-re-verification insert left a REDUNDANT second sentence saying
            the same thing ("Those figures were re-confirmed against a fresh search
            this morning"). A page must not say a thing twice in two sentences.
  2. mma  - "the promotion's third visit to the venue" was attributed to the bonus
            report, but the 2025 UFC Shanghai card was at the Shanghai Indoor Stadium
            and this one at the Oriental Sports Center, so "venue" is doubtful. It adds
            nothing and is DROPPED rather than printed with a caveat.
  3. mma  - "both were recorded here as ineligible" overstated the Polastri case: this
            page recorded a REPORTER's assessment about her, and asserted ineligibility
            only for Lima. Rewritten to the true split.
  4. mma  - Bilal Hasan's prospect card gained a real new fact (a $100,000 Performance
            of the Night award) and is therefore promoted to Updated with this run's
            stamp; the note above the cards, which said all four were carried, is
            corrected to match.
  5. cyber- subject-verb agreement on the GPUThor row.
"""
import io, sys

fails = []
def edit(p, pairs):
    s = io.open(p, encoding='utf-8').read()
    for old, new, label in pairs:
        if s.count(old) != 1:
            fails.append("%s / %s: found %d" % (p, label, s.count(old)))
            continue
        s = s.replace(old, new)
    io.open(p, 'w', encoding='utf-8').write(s)

edit('wallstreet-briefing.html', [(
    " Those figures were re-confirmed against a fresh search this morning rather than carried on trust.",
    "", "redundant re-confirmation sentence")])

edit('mma-briefing.html', [
    (" The same report puts the card at\n<b>ten finishes</b>, which is the count this page has carried, and calls "
     "it the promotion&rsquo;s\n<b>third visit to the venue</b>.",
     " The same report independently puts the card at <b>ten finishes</b>, which is the count this page has "
     "carried.", "third-visit claim dropped"),

    ("Neither <b>Julia Polastri</b> nor <b>Andre Lima</b> is on "
     "the list &mdash; both missed weight, and both were recorded here as ineligible before the awards were known.",
     "Neither <b>Julia Polastri</b> nor <b>Andre Lima</b> is on the list, and both missed weight. This page had "
     "recorded the two cases differently and the distinction survives the announcement: <b>Lima was stated to be "
     "ineligible</b>, on his second weight miss in the promotion; <b>Polastri was not</b> &mdash; what was recorded "
     "about her was a reporter&rsquo;s view of what she would have won.",
     "ineligibility overreach"),

    ('<div class="card"><div class="tags"><span class="tag pros">prospect</span>'
     '<span class="tag">Carried &middot; re-verified</span></div>\n<h4>Bilal Hasan</h4>',
     '<div class="card"><div class="tags"><span class="tag pros">prospect</span>'
     '<span class="tag new">Updated &middot; 10:20 AM</span></div>\n<h4>Bilal Hasan</h4>',
     "Hasan card promoted"),

    ("after Rojas had briefly turned the fight with power\npunches moments before.</p></div>",
     "after Rojas had briefly turned the fight with power\npunches moments before. <b>New at 10:20 AM:</b> that "
     "finish took a <b>$100,000 Performance of the Night</b> award &mdash; a debut win and a six-figure bonus on "
     "the same night, less than three weeks after he signed.</p></div>",
     "Hasan bonus added"),

    ("<b>All four cards below are carried, not new to this edition.</b> They come from the Shanghai card and were "
     "first published in the 8:19 and 8:46 editions; no source seen this run added to them. The Bilal Hasan card "
     "is marked re-verified because UFC.com&rsquo;s own event page, fetched this run, independently states his "
     "record, camp and contract timeline &mdash; <b>re-verifying a claim is not the same as the claim being "
     "new</b>, and the tags distinguish the two.",
     "<b>Three of the four cards below are carried, not new to this edition.</b> They come from the Shanghai card "
     "and were first published in the 8:19 and 8:46 editions; no source seen this run added to them. <b>The Bilal "
     "Hasan card is the exception and is tagged Updated</b>: his <b>$100,000 Performance of the Night</b> award "
     "was announced and sourced at 10:20 AM. The rest of that card is unchanged and was re-verified against "
     "UFC.com&rsquo;s own event page, fetched this run, which independently states his record, camp and contract "
     "timeline &mdash; <b>re-verifying a claim is not the same as the claim being new</b>, and the tags "
     "distinguish the two.",
     "prospect note corrected"),
])

edit('cyber-briefing.html', [(
    "<b>No CVE identifier and no CVSS score was stated by any source seen this run, so neither is printed</b>",
    "<b>No CVE identifier and no CVSS score were stated by any source seen this run, so neither is printed</b>",
    "GPUThor agreement")])

if fails:
    print("FIX2 FAILURES (%d):" % len(fails))
    for f in fails:
        print("  - " + f)
    sys.exit(1)
print("fix2_1020.py: all fixes applied cleanly.")
