#!/usr/bin/env python3
"""Restamp ONLY. The index<-tldr sync lives in fix_1636.py; running a sync
twice is what mangled index.html this run, so this file no longer contains one."""
import io, re, sys, datetime, zoneinfo
O = "/sessions/relaxed-dreamy-einstein/mnt/outputs/"
PAGES = ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]
def rd(p):
    with io.open(O+p, encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(O+p, "w", encoding="utf-8") as f: f.write(s)
fails = []
# ── restamp ──
now = datetime.datetime.now(zoneinfo.ZoneInfo("America/New_York"))
datestamp = now.strftime("%A, %B %-d, %Y")
tm = now.strftime("%-I:%M %p")
h = now.hour
edition = "Morning Edition" if h < 11 else ("Midday Edition" if h < 15 else "Afternoon Edition")
fresh = "Data as of %s ET &middot; briefings refresh every 30 minutes, 8 AM&ndash;6 PM ET" % tm

def setid(s, idname, val):
    # widened: id may not be the first attribute
    pat = re.compile(r'(<span[^>]*id="%s"[^>]*>)(.*?)(</span>)' % idname, flags=re.S)
    if not pat.search(s): return s, False
    return pat.sub(lambda m: m.group(1) + val + m.group(3), s, count=1), True

for p in PAGES:
    s = rd(p)
    for idname, val in (("datestamp", datestamp), ("updated", tm + " ET"), ("edition", edition)):
        s, ok = setid(s, idname, val)
        if not ok: fails.append("%s: id=%s not rewritten" % (p, idname))
    pat = re.compile(r'(<div class="freshline" id="freshline">)(.*?)(</div>)', flags=re.S)
    if pat.search(s):
        s = pat.sub(lambda m: m.group(1) + fresh + m.group(3), s, count=1)
    else:
        fails.append("%s: freshline not rewritten" % p)
    wr(p, s)

print("STAMP: %s | %s | %s" % (edition, datestamp, tm))
print("SYNC/RESTAMP FAILURES:", fails if fails else "none")
sys.exit(1 if fails else 0)
