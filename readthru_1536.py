# -*- coding: utf-8 -*-
import io
# (a) cyber tldr omitted the Android qualifier the table row carries
f='cyber-briefing.html'; s=io.open(f,encoding='utf-8').read()
old=('<b>CVE-2026-84352</b> in WebGL, both reachable from a crafted page and both escaping the sandbox')
assert old in s, 'A'
new=('<b>CVE-2026-84352</b> in WebGL, both reachable from a crafted page and both escaping the sandbox '
     '(the write-up for <b>84353 specifies Chrome on Android</b>, and that qualifier travels with it)')
s=s.replace(old,new,1); io.open(f,'w',encoding='utf-8').write(s)

# (b) same omission on the index card
f='index.html'; s=io.open(f,encoding='utf-8').read()
old=('<b>CVE-2026-84352</b> in WebGL, both reachable from a crafted page and both escaping the sandbox')
assert old in s, 'B'
new=('<b>CVE-2026-84352</b> in WebGL, both reachable from a crafted page and both escaping the sandbox '
     '(84353 is specified on <b>Android</b>)')
s=s.replace(old,new,1); io.open(f,'w',encoding='utf-8').write(s)
print('ok')
