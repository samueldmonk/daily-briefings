import io, re
D = "/sessions/lucid-funny-planck/mnt/outputs/"

def tldr(f):
    s = io.open(D + f, encoding="utf-8").read()
    m = re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', s, re.S)
    assert m, f
    return m.group(1)

cy, ws, mm = tldr("cyber-briefing.html"), tldr("wallstreet-briefing.html"), tldr("mma-briefing.html")

F = D + "index.html"
s = io.open(F, encoding="utf-8").read()
n = 0
def sub(cls, txt):
    global s, n
    pat = re.compile(r'(<div class="bcard ' + cls + r'">.*?<p>)(.*?)(</p>)', re.S)
    assert len(pat.findall(s)) == 1, cls
    s = pat.sub(lambda m: m.group(1) + txt + m.group(3), s, count=1); n += 1

sub("c1", cy); sub("c2", ws); sub("c3", mm)
io.open(F, "w", encoding="utf-8").write(s)

# verify byte-identical
s2 = io.open(F, encoding="utf-8").read()
for cls, t in (("c1", cy), ("c2", ws), ("c3", mm)):
    assert t in s2, cls
print("index cards synced:", n)
