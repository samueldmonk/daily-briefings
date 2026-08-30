import re, subprocess
NEW = subprocess.check_output(['bash','-c','TZ=America/New_York date +"%-I:%M %p"']).decode().strip()
OLD = "8:31 PM"
files = ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']
log = []

def sub(s, old, new, fname, req=1):
    n = s.count(old)
    assert n == req, f"{fname}: expected {req} of {old[:60]!r}, found {n}"
    log.append(f"{fname}: {n}x {old[:55]!r}")
    return s.replace(old, new)

for f in files:
    s = open(f).read()
    n = s.count(OLD)
    assert n >= 2, f"{f}: only {n} stamp occurrences"
    s = s.replace(OLD, NEW)
    log.append(f"{f}: stamp {n}x -> {NEW}")
    open(f,'w').write(s)

# --- Wall Street: advance the verification counter ---
f='wallstreet-briefing.html'; s=open(f).read()
s = sub(s, "re-verified a <b>fourteenth</b> time this run",
           "re-verified a <b>fifteenth</b> time this run", f)
s = sub(s, "the <b>fourth consecutive</b> check of that breadth",
           "the <b>fifth consecutive</b> check of that breadth", f)
s = sub(s, "re-verified a fourteenth time at 6:20 PM, and an eleventh time at 12:35 PM",
           "re-verified a fifteenth time at " + NEW + ", a fourteenth at 6:20 PM, and an eleventh time at 12:35 PM", f)
open(f,'w').write(s)

# --- index card must mirror the Wall Street tldr ---
f='index.html'; s=open(f).read()
if "re-verified a <b>fourteenth</b> time this run" in s:
    s = sub(s, "re-verified a <b>fourteenth</b> time this run",
               "re-verified a <b>fifteenth</b> time this run", f)
if "the <b>fourth consecutive</b> check of that breadth" in s:
    s = sub(s, "the <b>fourth consecutive</b> check of that breadth",
               "the <b>fifth consecutive</b> check of that breadth", f)
open(f,'w').write(s)

# --- Cyber: record the sixth KEV check ---
f='cyber-briefing.html'; s=open(f).read()
anchor = "<b><b>A fifth check at 6:20 PM returned CISA&rsquo;s own August 27 alert page for the first time.</b>"
add = anchor + " <b>A sixth check at " + NEW + " returned no CISA alert dated later than August 27</b>, so every id and all four countdowns on this board stand unchanged."
s = sub(s, anchor, add, f)
open(f,'w').write(s)

print("NEW STAMP:", NEW)
print("\n".join(log))
