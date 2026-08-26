import io, os, sys
O=os.path.dirname(os.path.abspath(__file__)); fails=[]
def rep(h,o,n,l,cnt=1):
    if h.count(o)!=cnt: fails.append('%s: found %d'%(l,h.count(o))); return h
    return h.replace(o,n)
w=io.open(os.path.join(O,'wallstreet-briefing.html'),encoding='utf-8').read()
# the Okta card's tag strip still reads "+14%", which is Salesforce's number, not Okta's
w=rep(w,'<div class="tags"><span class="tag">4:36</span><span class="tag up">+14%</span><span class="tag">Sourced move</span></div>',
      '<div class="tags"><span class="tag">5:36</span><span class="tag up">Okta &plus;15% / &plus;17%</span>'
      '<span class="tag up">CRM &plus;14% / &plus;12%</span><span class="tag up">CRWD &plus;12% / &plus;10%</span>'
      '<span class="tag down">HPQ &minus;11%</span><span class="tag down">SNPS &minus;6%</span>'
      '<span class="tag down">NVDA &minus;1%</span><span class="tag up">NTNX &plus;5%</span>'
      '<span class="tag">Two reads each, neither merged</span></div>','okta tags')
# grammar: the flag sentence ran into the sentence it interrupts
w=rep(w,'EPS.</b> The figures below are unchanged on revenue of',
      'EPS.</b> <b>The figures this page does publish are unchanged:</b> revenue of',
      'crm grammar')
# the "older framing" note asserts NVDA has no magnitude; true at 5:06, false now
w=rep(w,'and the one that does not is the largest company on the list.',
      'and the one that does not is the largest company on the list. <b>&#9888; That last clause is no longer true '
      'as of 5:36 &mdash; Nvidia now has two sourced after-hours magnitudes; the sentence is kept only as the record of '
      'what this page said at 5:06.</b>','older framing')
io.open(os.path.join(O,'wallstreet-briefing.html'),'w',encoding='utf-8').write(w)
if fails: print('FAILED',fails); sys.exit(1)
print('polish OK')
