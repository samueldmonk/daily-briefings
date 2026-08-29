#!/usr/bin/env python3
"""Third fix pass — the fresh-tag audit caught five more carried items wearing this run's stamp.

The threat-actor spotlight (sourced 8:46) and all four prospect cards (sourced 8:19/8:46)
were tagged as new to the 9:40 edition. None was newly sourced this run. Demoted.
The Bilal Hasan card IS corroborated by the UFC.com page fetched this run, so it is
labelled re-verified rather than merely carried — re-verified is not the same as new.
"""
import io, sys, re

D = sys.argv[1] if len(sys.argv) > 1 else "."

def load(n): return io.open(f"{D}/{n}", encoding="utf-8").read()
def save(n, h): io.open(f"{D}/{n}", "w", encoding="utf-8").write(h)

NEW  = '<span class="tag new">New &middot; 9:40 AM</span>'
CARR = '<span class="tag">Carried</span>'
REV  = '<span class="tag">Carried &middot; re-verified</span>'

# ── CYBER: threat-actor spotlight is carried from 8:46
cy = load("cyber-briefing.html")
if NEW + '<span class="tag crit">Agentic AI</span>' in cy:
    cy = cy.replace(NEW + '<span class="tag crit">Agentic AI</span>',
                    CARR + '<span class="tag crit">Agentic AI</span>', 1)
elif CARR + '<span class="tag crit">Agentic AI</span>' not in cy:
    raise SystemExit("fix3: threat-actor tag not demoted")
cy = cy.replace(
    "Cisco Talos has documented a Chinese-speaking cybercrime group tracked as <b>UAT-10147</b>",
    "First published in the 8:46 edition and carried unchanged. Cisco Talos has documented a "
    "Chinese-speaking cybercrime group tracked as <b>UAT-10147</b>", 1)
save("cyber-briefing.html", cy)

# ── MMA: all four prospect cards are carried from the earlier editions of this card
mm = load("mma-briefing.html")
PROS = '<span class="tag pros">prospect</span>'
n_before = mm.count(PROS + NEW)
if n_before:
    mm = mm.replace(PROS + NEW, PROS + REV, 1)      # Hasan — corroborated by UFC.com this run
    mm = mm.replace(PROS + NEW, PROS + CARR)        # the other three
if mm.count(PROS + NEW) != 0:
    raise SystemExit("fix3: prospect tags not demoted (%d left)" % mm.count(PROS + NEW))

mm = mm.replace(
    "A Dana White's Contender Series season 10 standout",
    "Re-verified against UFC.com's own event page fetched this run, which states each of the following. "
    "A Dana White's Contender Series season 10 standout", 1)

# say plainly why nothing in Prospect Watch is flagged new
anchor = 'Prospect Watch</h2><div class="cards">'
if anchor not in mm:
    raise SystemExit("fix3: prospect watch anchor missing")
mm = mm.replace(anchor,
    'Prospect Watch</h2>'
    '<div class="note" style="margin-bottom:12px"><b>All four cards below are carried, not new to this '
    'edition.</b> They come from the Shanghai card and were first published in the 8:19 and 8:46 editions; '
    'no source seen this run added to them. The Bilal Hasan card is marked re-verified because UFC.com&rsquo;s '
    'own event page, fetched this run, independently states his record, camp and contract timeline &mdash; '
    '<b>re-verifying a claim is not the same as the claim being new</b>, and the tags distinguish the '
    'two.</div><div class="cards">', 1)
save("mma-briefing.html", mm)

print("fix3_0940: OK — 5 carried items demoted from the fresh stamp")
