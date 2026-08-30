# -*- coding: utf-8 -*-
# Prose stamps the OBSERVATION (research ran 1:02-1:08 PM); the masthead stamps the PUBLISH.
# Prose must not run ahead of the wall clock.
import io, re, subprocess
def rd(p): return io.open(p,encoding='utf-8').read()
def wr(p,s): io.open(p,'w',encoding='utf-8').write(s)
P=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']

# 1) prose 1:10 PM -> 1:08 PM (observation time), but NOT the masthead/freshline
for p in P:
    s=rd(p)
    cut = s.find('</header>')+9
    head, body = s[:cut], s[cut:]
    body = body.replace('at 1:10 PM','at 1:08 PM').replace('Added at 1:10 PM','Added at 1:08 PM')
    body = body.replace('Completed at 1:10 PM','Completed at 1:08 PM')
    body = body.replace('tenth check of the KEV catalogue at 1:10 PM','tenth check of the KEV catalogue at 1:08 PM')
    body = body.replace('A tenth check at 1:10 PM','A tenth check at 1:08 PM')
    wr(p, head+body)

# 2) masthead + freshline -> actual wall clock now
now = subprocess.check_output(['bash','-lc','TZ=America/New_York date "+%-I:%M %p"']).decode().strip()
for p in P:
    s=rd(p)
    s=re.sub(r'(id="updated">)[^<]*(</span>)', r'\g<1>'+now+' ET'+r'\g<2>', s)
    s=re.sub(r'Data as of [0-9]{1,2}:[0-9]{2} (?:AM|PM) ET', 'Data as of '+now+' ET', s)
    wr(p,s)
print("restamped masthead to", now, "; prose observation time 1:08 PM")
