# Pure Python Phishing Detector - no sklearn needed
import json, re
from urllib.parse import urlparse

LEGIT = ['google.com','safaricom.co.ke','kra.go.ke','equitybank.co.ke','kcb.co.ke','facebook.com','youtube.com','wikipedia.org','jumia.co.ke','nation.co.ke','airtelkenya.com','mpesa.co.ke','co-operativebank.co.ke']

def score(url):
    s = 0
    u = url.lower()
    if not u.startswith('http'):
        u = 'https://' + u
    dom = urlparse(u).netloc
    if dom in LEGIT:
        return 0
    if dom.startswith('www.'):
        dom = dom[4:]
    if dom in LEGIT:
        return 0
    if len(u) > 60: s += 2
    if u.count('-') >= 2: s += 2
    if u.count('.') >= 4: s += 2
    if '@' in u: s += 3
    if re.search(r'\d+\.\d+\.\d+\.\d+', u): s += 4
    if u.startswith('http://'): s += 1
    for w in ['free','verify','login','secure','update','confirm','bonus','gift','win','safaricom-','mpesa-','kra-','equity-','kcb-','airtel-']:
        if w in u and dom not in LEGIT:
            s += 2
    for t in ['.xyz','.top','.tk','.ml','.ga','.cf','.ru']:
        if dom.endswith(t): s += 3
    return s

# test
for t in ['google.com','safaricom.co.ke','safaricom-free.xyz','mpesa-verify.top']:
    print(t, score(t))

json.dump({'legit': LEGIT}, open('model.json','w'))
print("Saved model.json")
##
