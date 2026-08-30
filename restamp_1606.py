# -*- coding: utf-8 -*-
"""Write the masthead stamp statically (date / time / edition / freshline) on all pages."""
import re, sys, io, os, datetime
from zoneinfo import ZoneInfo
D=sys.argv[1]
now=datetime.datetime.now(ZoneInfo('America/New_York'))
date_s=now.strftime('%A, %B %-d, %Y')
time_s=now.strftime('%-I:%M %p')+' ET'
h=now.hour
ed='Morning Edition' if h<11 else ('Midday Edition' if h<15 else 'Afternoon Edition')
fresh='Data as of %s &middot; briefings refresh every 30 minutes, 8 AM&ndash;6 PM ET'%time_s
files=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']
for f in files:
    p=os.path.join(D,f)
    if not os.path.exists(p): continue
    s=io.open(p,encoding='utf-8').read()
    for _id,val in [('datestamp',date_s),('updated',time_s),('edition',ed)]:
        s=re.sub(r'(<span id="%s"[^>]*>).*?(</span>)'%_id, lambda m: m.group(1)+val+m.group(2), s, flags=re.S)
    s=re.sub(r'(<div class="freshline" id="freshline"[^>]*>).*?(</div>)', lambda m: m.group(1)+fresh+m.group(2), s, flags=re.S)
    s=re.sub(r'(<div id="freshline"[^>]*class="freshline"[^>]*>).*?(</div>)', lambda m: m.group(1)+fresh+m.group(2), s, flags=re.S)
    io.open(p,'w',encoding='utf-8').write(s)
print('STAMP:', date_s, '|', time_s, '|', ed)
