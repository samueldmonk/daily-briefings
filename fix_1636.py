#!/usr/bin/env python3
"""Fix pass:
   (a) index.html was mangled by a non-greedy <p>...</p> sync that swallowed
       everything between the first <p> in the document and each card's
       closing </p>.  Restore from repo and re-sync anchored BACKWARDS from
       each 'Read the briefing' link to its own immediately-preceding <p>.
   (b) dedupe footer source links this run's edits duplicated."""
import io, re, sys, shutil

O = "/sessions/relaxed-dreamy-einstein/mnt/outputs/"
REPO = "/tmp/db_1788122176/"
fails = []

# ── (a) restore + correct sync ──
shutil.copy(REPO+"index.html", O+"index.html")
idx = io.open(O+"index.html", encoding="utf-8").read()

def tldr_of(page, label):
    s = io.open(O+page, encoding="utf-8").read()
    m = re.search(r'<div class="tldr"><b>%s</b> <span>(.*?)</span></div>' % re.escape(label), s, re.S)
    if not m: fails.append("tldr missing on %s" % page)
    return m.group(1) if m else None

for page, label, href in [("cyber-briefing.html","The Wire","cyber-briefing.html"),
                          ("wallstreet-briefing.html","The Tape","wallstreet-briefing.html"),
                          ("mma-briefing.html","Tale of the Tape","mma-briefing.html")]:
    body = tldr_of(page, label)
    if body is None: continue
    anchor = '<a class="go" href="%s">' % href
    ai = idx.find(anchor)
    if ai < 0: fails.append("index: anchor %s not found" % href); continue
    ce = idx.rfind("</p>", 0, ai)                 # this card's closing </p>
    cs = idx.rfind("<p>", 0, ce)                  # its OWN opening <p>
    if ce < 0 or cs < 0: fails.append("index: <p> block for %s not found" % href); continue
    seg = idx[cs+3:ce]
    if "<p>" in seg or "</p>" in seg or "class=\"go\"" in seg:
        fails.append("index: card block for %s is not a single flat <p>" % href); continue
    idx = idx[:cs+3] + body + idx[ce:]

io.open(O+"index.html","w",encoding="utf-8").write(idx)

# ── (b) dedupe footer hrefs, keeping the FIRST occurrence ──
# widened per the standing rule: links may carry target/rel attributes and may
# sit after </footer>, so match any <a ...href="http...">...</a>.
LINK = re.compile(r'<a\s[^>]*href="(https?://[^"]+)"[^>]*>.*?</a>(?:<br>)?', re.S)
for p in ["cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]:
    s = io.open(O+p, encoding="utf-8").read()
    seen = set(); out = []; last = 0; removed = 0
    for m in LINK.finditer(s):
        url = m.group(1)
        if url in seen:
            out.append(s[last:m.start()]); last = m.end(); removed += 1
        else:
            seen.add(url)
    out.append(s[last:])
    s = "".join(out)
    io.open(O+p,"w",encoding="utf-8").write(s)
    print("%s: removed %d duplicate links" % (p, removed))

print("FIX FAILURES:", fails if fails else "none")
sys.exit(1 if fails else 0)
