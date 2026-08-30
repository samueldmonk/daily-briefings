#!/usr/bin/env python3
import re
D = "/sessions/serene-vigilant-hypatia/mnt/outputs/"
OBS = "3:10 PM"
fails = []

cy = open(D + "cyber-briefing.html", encoding="utf-8").read()
old = "the discrepancy is <b>recorded, not resolved</b>."
new = old + (
 " <b>Corroborated at " + OBS + ":</b> a fresh sweep returned both halves of the pair independently "
 "&mdash; the <b>August 27</b> advisory carrying <b>CVE-2026-18885, CVE-2026-18886 and CVE-2026-74820 at "
 "CVSS v4.0 10.0</b> alongside 6876, with ServiceNow stating it is <b>not aware of malicious exploitation "
 "against ServiceNow instances</b> and urging self-hosted customers to patch or upgrade; and, separately, "
 "<b>CVE-2026-6875</b> at <b>CVSS 9.8</b>, reported to the vendor by <b>Searchlight Cyber on April 1</b>, "
 "fixed on hosted instances from April and on self-hosted instances on <b>July 13</b>, with in-the-wild "
 "exploitation first observed by researchers at <b>Defused</b>. <b>The split status of the two &mdash; 6875 "
 "exploited and old, 6876 new and not exploited &mdash; holds on a second, independent look.</b>"
)
if old in cy:
    cy = cy.replace(old, new, 1)
    open(D + "cyber-briefing.html", "w", encoding="utf-8").write(cy)
else:
    fails.append("cy 6876")

mma = open(D + "mma-briefing.html", encoding="utf-8").read()
old2 = "<b>light favourite</b> to take the belt back."
new2 = old2 + (
 " <b>New at " + OBS + " &mdash; a second book, and it is on the other side of the line.</b> "
 "<b>Bet Online opened Joshua Van at &minus;115 and Alexandre Pantoja at &minus;105</b>, which makes "
 "<b>the reigning champion the light favourite</b>. DraftKings, sourced last run, had it the other way: "
 "<b>Van +100, Pantoja &minus;120</b>. <b>Both are near pick-em and they disagree about who is "
 "favoured</b> &mdash; a 15-point swing on Van across two books, which is what a genuinely even fight "
 "looks like before the money arrives. <b>Neither is adopted</b>; the spread is what this page prints. "
 "&#9888; <b>The co-main now has a price, which it did not last run.</b> <b>Arman Tsarukyan opened at "
 "&minus;400</b> over Mauricio Ruffy &mdash; the previous edition described him as heavily favoured and "
 "printed no number because none was stated; a number is now stated. The card is re-confirmed at "
 "<b>13 fights</b>, Saturday <b>September 19</b>, <b>Crypto.com Arena, Los Angeles</b>. &#9888; <b>One "
 "characterisation returned this run is not adopted:</b> a report describes the UFC 323 original as a "
 "fight &ldquo;that ended in injury.&rdquo; This page carries the result as its own corrections file "
 "records it &mdash; a <b>technical knockout 26 seconds into round one</b>, after an arm injury to "
 "Pantoja &mdash; and does not swap a sourced finish for a looser paraphrase of it."
)
if old2 in mma:
    mma = mma.replace(old2, new2, 1)
    open(D + "mma-briefing.html", "w", encoding="utf-8").write(mma)
else:
    fails.append("mma 331")

print("FIX FAILURES:", fails if fails else "none")
