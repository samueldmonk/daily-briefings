#!/usr/bin/env python3
"""Restamp all four pages, mirror each briefing's tldr into its index card, dedupe footers.

The index sync uses the BACKWARDS anchor mandated by CORRECTIONS.md: find the card's own
<a class="go" href=...>, rfind the </p> before it, rfind the <p> before that. A forward
non-greedy match starts at the FIRST <p> in the document and swallows the whole page.
"""
import re, sys, os

D = sys.argv[1] if len(sys.argv) > 1 else "."
STAMP = "5:10 PM"
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
CARD_TARGETS = {
    "cyber-briefing.html": "cyber-briefing.html",
    "wallstreet-briefing.html": "wallstreet-briefing.html",
    "mma-briefing.html": "mma-briefing.html",
}

def rd(p):
    return open(os.path.join(D, p), encoding="utf-8").read()

def wr(p, s):
    open(os.path.join(D, p), "w", encoding="utf-8").write(s)


def extract_tldr(html, label):
    """Return the inner text of the page's .tldr <span>."""
    m = re.search(r'<div class="tldr">.*?<span>(.*?)</span></div>', html, re.S)
    assert m, label + ": tldr span not found"
    inner = m.group(1)
    assert "<p>" not in inner, label + ": tldr contains a nested <p>"
    assert 'class="tldr"' not in inner, label + ": tldr matched past its own close"
    return inner


def card_block(html, href, label):
    """Backwards-anchored extraction of the index card paragraph for `href`."""
    a = html.find('<a class="go" href="%s"' % href)
    assert a != -1, label + ": no go-link for " + href
    pclose = html.rfind("</p>", 0, a)
    assert pclose != -1, label + ": no </p> before the go-link"
    popen = html.rfind("<p>", 0, pclose)
    assert popen != -1, label + ": no <p> before that </p>"
    inner = html[popen + 3:pclose]
    assert "<p>" not in inner, label + ": extracted block has a nested <p> (forward-match bug)"
    return popen + 3, pclose, inner


# ── 1. Sync the three index cards from the briefings' own tldr strips ────────
idx = rd("index.html")
for page, href in CARD_TARGETS.items():
    tldr = extract_tldr(rd(page), page)
    start, end, _old = card_block(idx, href, "index/" + page)
    idx = idx[:start] + tldr + idx[end:]

# The tldr strip itself must NOT appear on the front page.
assert 'class="tldr"' not in idx, "index.html: tldr strip must not appear on the front page"
wr("index.html", idx)

# ── 2. Restamp every page ───────────────────────────────────────────────────
for p in PAGES:
    h = rd(p)
    h = re.sub(r'(<div class="freshline" id="freshline">)Data as of [^<]*?(</div>)',
               r'\g<1>Data as of ' + STAMP +
               ' ET &middot; briefings refresh every 30 minutes, 8 AM&ndash;6 PM ET\g<2>',
               h)
    wr(p, h)

# ── 3. Footer link dedupe (three consecutive runs have introduced duplicates) ─
for p in PAGES:
    h = rd(p)
    seen, out, pos = set(), [], 0
    for m in re.finditer(r'<a\s[^>]*href="https?://[^"]+"[^>]*>.*?</a>(?:<br>)?', h, re.S):
        href = re.search(r'href="([^"]+)"', m.group(0)).group(1)
        if href in seen:
            out.append(h[pos:m.start()])
            pos = m.end()
        else:
            seen.add(href)
    out.append(h[pos:])
    h2 = "".join(out)
    if h2 != h:
        print("%s: deduped %d duplicate link(s)" % (p, h.count('<a ') - h2.count('<a ')))
    wr(p, h2)

print("sync_1710: index synced, all four pages stamped %s, footers deduped" % STAMP)
