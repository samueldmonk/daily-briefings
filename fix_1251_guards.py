# -*- coding: utf-8 -*-
# Narrow (never loosen) the four guard classes that produced false positives in validate_1251.py
import io
s=io.open('validate_1251.py',encoding='utf-8').read()

# (a) PayPal guard fired on SOURCES-FOOTER LINK LABELS. A link label is not an assertion.
#     Ninth occurrence of the context false-positive class in this file.
#     NARROWED: skip any window inside an <a ...>...</a> or after the Sources heading.
s=s.replace('''for mm in re.finditer(r'PayPal',ws):
    w=ws[max(0,mm.start()-1500):mm.start()+1500]
    chk(('Friday' in w) or ('refus' in w.lower()),'ws: PayPal move without Friday/refusal context')''',
'''_srcstart=ws.find('Sources checked this run')
for mm in re.finditer(r'PayPal',ws):
    if _srcstart>0 and mm.start()>_srcstart-200: continue      # link labels in the sources footer are not assertions
    if '</a>' in ws[mm.start():mm.start()+120] and '<a ' in ws[max(0,mm.start()-400):mm.start()]: continue
    w=ws[max(0,mm.start()-1500):mm.start()+1500]
    chk(('Friday' in w) or ('refus' in w.lower()),'ws: PayPal move without Friday/refusal context')''')

# (b) The "due TODAY, Sunday, August 30" sweep fired on the correction paragraph, which QUOTES
#     yesterday's wording inside &ldquo;...&rdquo;. Same defect narrowed on Aug 31 at 11:33 and
#     re-introduced here by writing the guard fresh. NARROWED: require an UNQUOTED instance.
s=s.replace('''chk('due TODAY, Sunday, August 30' not in cy,'cy: stale "due today Sunday" assertion')''',
'''for mm in re.finditer(r'due TODAY, Sunday, August 30',cy):
    pre=cy[max(0,mm.start()-160):mm.start()]
    chk('&ldquo;' in pre,'cy: stale "due today Sunday" asserted unquoted')''')

# (c) The "due today" sweep fired on CARRIED blocks that are dated records of a prior edition and
#     say so ("it is still Sunday, August 30"). A dated historical block is not a current assertion.
#     NARROWED: fire only when the nearest preceding edition tag belongs to THIS run.
s=s.replace('''for mm in re.finditer(r'due today',cy,re.I):
    w=cy[max(0,mm.start()-600):mm.start()+600]
    chk('&ldquo;' in w or 'quoted' in w or 'refus' in w.lower(),'cy: unquoted "due today" assertion')''',
'''for mm in re.finditer(r'due today',cy,re.I):
    pre=cy[:mm.start()]
    tags=re.findall(r'<span class="tag[^"]*">([^<]*)</span>',pre)
    last=tags[-1] if tags else ''
    if 'Carried' in last or 'Rewritten' in last or 'Aug 30' in last: continue   # dated prior-edition record
    w=cy[max(0,mm.start()-800):mm.start()+800]
    chk(('&ldquo;' in w) or ('August 30' in w) or ('refus' in w.lower()),
        'cy: current-run "due today" assertion without a verified date')''')

# (d) The champions-board content guards sliced from the <h2> heading, so the window swallowed the
#     section's PROSE (where "Strickland beat Chimaev", "Gane interim, not Pereira" and "the vacant
#     205 title" are all correct and required). The guard's subject is the TABLE ROWS only.
#     NARROWED: anchor the slice to <table>...</table> inside the section.
s=s.replace('''board=mm_[i:mm_.find('</table>',i)] if i>=0 else \'\'''',
'''_t=mm_.find('<table',i)
board=mm_[_t:mm_.find('</table>',_t)] if (i>=0 and _t>=0) else \'\'''')

io.open('validate_1251.py','w',encoding='utf-8').write(s)
print('guards narrowed')
