#!/usr/bin/env python3
"""Second fix pass — errors caught in the FINAL READ-THROUGH after validate passed.

Findings:
 (1) ws  Rates table asserted the SUPERSEDED Fed pricing as "This run", contradicting On the Radar.
 (2) ws  Lead called PayPal "the one genuinely new item this run" — it led the 8:19 edition.
 (3) ws  Salesforce card said "a fourth read" over a list of six, and "a fresh source this run"
         for a figure no source restated this run.
 (4) ws  Three mover cards tagged "New" were all present in the 9:15 edition.
 (5) cy  "What is new this run" on the watchTowr bypasses — that was new at 9:15.
 (6) cy  "New this run — the exploitation is quantified" on Citrix — that was new at 8:46.
 (7) cy  Two breach cards tagged "New" were present in the 9:15 edition.
 (8) mma "The headliner resolved after the previous edition went out" — it resolved before 9:15.
 (9) mma Two upcoming-card entries tagged "New" were present in the 9:15 edition.
(10) mma Circular phrasing on Nurmagomedov's loss count.
"""
import io, sys

D = sys.argv[1] if len(sys.argv) > 1 else "."

def load(n): return io.open(f"{D}/{n}", encoding="utf-8").read()
def save(n, h): io.open(f"{D}/{n}", "w", encoding="utf-8").write(h)

def sub(h, old, new, tag):
    if old not in h:
        raise SystemExit(f"fix2 ANCHOR MISSING [{tag}]: {old[:100]!r}")
    if h.count(old) != 1:
        raise SystemExit(f"fix2 ANCHOR x{h.count(old)} [{tag}]: {old[:100]!r}")
    return h.replace(old, new)

NEW  = '<span class="tag new">New &middot; 9:40 AM</span>'
UPD  = '<span class="tag new">Updated &middot; 9:40 AM</span>'
CARR = '<span class="tag">Carried</span>'

# ─────────────────────────── WALL STREET ───────────────────────────
ws = load("wallstreet-briefing.html")

# (1) the rates-table row contradicted On the Radar and mislabelled its vintage
ws = sub(ws,
    "<td>Fed policy pricing</td><td>~65% odds of <b>no change</b> in September; &gt;70% odds of a <b>hike</b> by December</td><td>This run</td>",
    "<td>Fed policy pricing</td><td>48% odds of a 25bp <b>hike</b> in September (Kalshi), revised down from "
    "~70% odds of <i>no change</i>; &gt;70% odds of a hike by December</td>"
    "<td>Sept read this run; Dec read carried</td>",
    "ws-rates-row")

# (2) PayPal was the lead of the 8:19 edition, not a fresh item this run
ws = sub(ws,
    "The one genuinely new item this run is corporate, not macro. <b>Stripe and Advent International have\nabandoned",
    "The corporate story of the weekend is unchanged since the 8:19 edition and is repeated here in full "
    "because it is still the largest single-name item on the board &mdash; <b>it is not new to this "
    "edition</b>. <b>What is new to this edition is the rate pricing</b>, which is in On the Radar below. "
    "Stripe and Advent International have\nabandoned",
    "ws-lead-new")

# (3) Salesforce: the count was wrong and the sourcing claim was wrong
ws = sub(ws, "Salesforce &mdash; a fourth read of the same move",
             "Salesforce &mdash; six reads of one session, still unresolved", "ws-crm-h")
ws = sub(ws,
    "A fresh source this run puts CRM at <b>+22.6%</b> on Thursday after beating on both earnings and revenue.\n"
    "That lands near the top of a range this page has been recording all week &mdash; reads of 11.2%, 19%, 22.68%,\n"
    "22.75% and 22.87% have all been offered for the same session. <b>None is asserted, none averaged</b>; the new\n"
    "figure is added to the record, not substituted for it.",
    "Six different percentages have now been published for <b>Thursday's</b> Salesforce move, after the company "
    "beat on both earnings and revenue: <b>11.2%, 19%, 22.6%, 22.68%, 22.75% and 22.87%</b>. <b>No source seen "
    "this run restated any of them</b> &mdash; the most recent addition, +22.6%, arrived in the 8:19 edition, and "
    "the whole set is carried here. <b>None is asserted and none is averaged.</b> Four of the six cluster within "
    "three tenths of a point of each other, which is suggestive; it is not a reason for this page to pick one.",
    "ws-crm-p")

# (4) demote mover cards that were already on the 9:15 page
ws = ws.replace(NEW + '<span class="tag">Premarket</span>', CARR + '<span class="tag">Premarket</span>', 1)
ws = ws.replace(NEW + '<span class="tag">Earnings</span>', CARR + '<span class="tag">Earnings</span>', 1)
ws = ws.replace(NEW + '<span class="tag">Thursday</span>', CARR + '<span class="tag">Thursday</span>', 1)

# note the demotion so the reader knows why nothing on this board is flagged new
ws = sub(ws,
    "## Movers &amp; Drivers".replace("## ", "") if False else 'Movers &amp; Drivers</h2><div class="cards">',
    'Movers &amp; Drivers</h2>'
    '<div class="note" style="margin-bottom:12px"><b>Nothing on this board is new to the 9:40 edition, and none '
    'of it is tagged as though it were.</b> U.S. equity markets have been closed since Friday&rsquo;s bell, so no '
    'new single-stock move can exist. Every card below is carried from an earlier edition with its original '
    'sourcing intact; the only figure that changed this run is the September rate pricing, which is in '
    '<a href="#radar">On the Radar</a>.</div><div class="cards">',
    "ws-movers-note")

ws = sub(ws, '<h2 class="sec">On the Radar</h2>', '<h2 class="sec" id="radar">On the Radar</h2>', "ws-radar-id")
save("wallstreet-briefing.html", ws)

# ─────────────────────────── CYBER ───────────────────────────
cy = load("cyber-briefing.html")

# (5) the watchTowr bypass finding was new at 9:15
cy = sub(cy,
    "<b>What is new this run, and it is not good.</b> watchTowr reports it found",
    "<b>The worst of it, first published in the 9:15 edition and re-verified against two independent reports "
    "this run.</b> watchTowr reports it found",
    "cy-newthisrun-1")

# (6) the Citrix telemetry was new at 8:46
cy = sub(cy,
    "<b>New this run &mdash; the exploitation is quantified.</b> Telemetry cited by CISA-tracking researchers",
    "<b>The exploitation is quantified &mdash; carried from the 8:46 edition, where it was first sourced.</b> "
    "Telemetry cited by CISA-tracking researchers",
    "cy-newthisrun-2")

# (7) breach cards: MAG unchanged, Boston Scientific materially updated
cy = cy.replace(NEW + '<span class="tag">Aviation</span>', CARR + '<span class="tag">Aviation</span>', 1)
cy = cy.replace(NEW + '<span class="tag crit">Medical devices</span>',
                UPD + '<span class="tag crit">Medical devices</span>', 1)
save("cyber-briefing.html", cy)

# ─────────────────────────── MMA ───────────────────────────
mm = load("mma-briefing.html")

# (8) stale temporal claim — the main event resolved before the 9:15 edition, not after this one
mm = sub(mm,
    "The headliner resolved after the previous edition went out, and it went the home fighter's way.",
    "The headliner went the home fighter's way. It resolved during the 9:15 edition, not this one, and is "
    "repeated here with the finishing sequence now filled in.",
    "mma-stale-temporal")

# (10) circular loss-count phrasing replaced with the explicit derivation
mm = sub(mm,
    "It is the second loss of Nurmagomedov's career by this page's own record of his 20-1 mark.",
    "UFC.com's pre-fight copy listed Nurmagomedov at <b>20-1</b>, so this is the <b>second defeat of his "
    "career</b> &mdash; a derivation from the pre-fight record, not a figure any source stated after the fight.",
    "mma-losscount")

# (9) upcoming-card tags: only Noche UFC changed this run
mm = sub(mm,
    NEW + '</div>\n<div class="dateline">Sat, Sept 19',
    CARR + '</div>\n<div class="dateline">Sat, Sept 19', "mma-tag-331")
mm = sub(mm,
    NEW + '</div>\n<div class="dateline">Sat, Sept 5',
    CARR + '</div>\n<div class="dateline">Sat, Sept 5', "mma-tag-paris")
mm = sub(mm,
    NEW + '</div>\n<div class="dateline">Sat, Sept 12',
    UPD + '</div>\n<div class="dateline">Sat, Sept 12', "mma-tag-noche")
mm = sub(mm, '<span class="tag">Completed &middot; 9:40 AM</span>',
             '<span class="tag">Completed</span>', "mma-tag-completed")
save("mma-briefing.html", mm)

# ─────────────────────────── INDEX (re-sync cards) ───────────────────────────
import re
ix = load("index.html")
for page, kick in (("cyber-briefing.html", "c-cy"),
                   ("wallstreet-briefing.html", "c-ws"),
                   ("mma-briefing.html", "c-mm")):
    t = re.search(r'<div class="tldr"><b>[^<]*</b>\s*<span>(.*?)</span></div>', load(page), re.S).group(1)
    pat = re.compile(r'(<div class="bigcard ' + kick + r'">.*?<p>)(.*?)(</p>)', re.S)
    ix = pat.sub(lambda m: m.group(1) + t + m.group(3), ix, count=1)
save("index.html", ix)

print("fix2_0940: OK — 10 read-through corrections applied")
