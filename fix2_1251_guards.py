# -*- coding: utf-8 -*-
import io
s=io.open('validate_1251.py',encoding='utf-8').read()

# (c) NARROWED AGAIN: the carried-tag allowlist ('Carried'/'Rewritten'/'Aug 30') did not include the
#     'Refused &middot; 3:10 PM' tag form, so three dated prior-edition blocks read as current.
#     The correct test is not "is this tag carried" but "is this block NEW THIS RUN" -- invert it.
s=s.replace("""    if 'Carried' in last or 'Rewritten' in last or 'Aug 30' in last: continue   # dated prior-edition record""",
"""    if 'New &middot; 12:51 PM' not in last: continue   # only a block published THIS RUN can assert a current deadline""")

# (d) NARROWED: the forbidden-name sweep matched the Note column, where "KO2 Pereira",
#     "split decision over Khamzat Chimaev" and "for the vacant title" are all CORRECT and
#     load-bearing -- they name who a champion BEAT and how a belt was won. The June regression
#     this guard exists for was Pereira/Chimaev listed AS the champion. Test the champion cells,
#     and separately that no belt is described as CURRENTLY vacant.
s=s.replace("""chk('Pereira' not in board,'mma: Pereira must not appear in the champions table')
chk('Chimaev' not in board,'mma: Chimaev must not appear in the champions table')
chk('acant' not in board,'mma: no vacant belt should be listed')""",
"""_rows=re.findall(r'<tr>(.*?)</tr>',board,re.S)
_champcells=[]
for _r in _rows:
    _c=re.findall(r'<td>(.*?)</td>',_r,re.S)
    if len(_c)>=2: _champcells.append(re.sub(r'<[^>]+>','',_c[1]))
chk(len(_champcells)>=8,'mma: fewer than 8 champion rows')
for _bad in ['Pereira','Chimaev']:
    chk(not any(_bad in _c for _c in _champcells),'mma: %s listed AS a champion'%_bad)
for _c in _champcells:
    chk('acant' not in _c and _c.strip()!='','mma: a champion cell is vacant or empty')
chk(re.search(r'(currently|now) vacant',board,re.I) is None,'mma: a belt is described as currently vacant')
chk('Interim: Ciryl Gane' in board,'mma: Gane interim note missing from the board')
chk('Tom Aspinall' in _champcells[0] if _champcells else False,'mma: heavyweight champion cell wrong')""")

io.open('validate_1251.py','w',encoding='utf-8').write(s)
print('guards narrowed (round 2)')
