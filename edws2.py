# -*- coding: utf-8 -*-
import io
D='/tmp/db_1788782763/'
def load(f): return io.open(D+f,encoding='utf-8').read()
def save(f,h): io.open(D+f,'w',encoding='utf-8').write(h)
N=[0]
def rep(h,old,new,cnt=1):
    assert h.count(old)==cnt, ("COUNT %d!=%d for: %r"%(h.count(old),cnt,old[:110]))
    N[0]+=1; return h.replace(old,new)

w=load('wallstreet-briefing.html')

# tldr rewritten for Labor Day + the widened odds spread
w=rep(w,'<span>U.S. markets are closed for the weekend and shut again Monday for Labor Day, leaving Friday&rsquo;s lower close as the last word: August payrolls came in at 162,000 against a 53,000 consensus, but the case for a Fed hike at the 15&ndash;16 September meeting has since softened, with governor Christopher Waller saying he would be inclined to hold if next Friday&rsquo;s CPI cools &mdash; though the payrolls print then pushed CME FedWatch hike odds back above even, from 49.4% the day before to somewhere in the high 50s or low 60s depending on which return you read.</span>',
 '<span>U.S. stock and bond markets are shut all day for Labor Day and reopen Tuesday, leaving Friday&rsquo;s lower close as the last word: August payrolls came in at 162,000 against a 53,000 consensus &mdash; the strongest month since March, with June and July revised up by 55,000 between them &mdash; and hike odds for the 15&ndash;16 September meeting are now above even but unsettled, running from 58% to about 63% across three sources against 49.4% before the jobs number, with Friday&rsquo;s CPI still the input that decides it.</span>')

# hike odds: widen printed range to include the 63% return
w=rep(w,'to somewhere in the high 50s or low 60s depending on which return you read','to somewhere in the high 50s or low 60s depending on which return you read',0) if False else w

save('wallstreet-briefing.html',w)
print("ws tldr:",N[0])
