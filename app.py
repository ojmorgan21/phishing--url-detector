from flask import Flask, request, render_template_string
import train
app = Flask(__name__)
HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PhishGuard</title>
<style>
*{box-sizing:border-box;font-family:system-ui,sans-serif}
body{margin:0;background:#070b14;color:#eef2ff;min-height:100vh}
.top{max-width:900px;margin:0 auto;padding:24px 18px 0;display:flex;justify-content:space-between;align-items:center}
.logo{font-weight:800;font-size:20px}
.logo span{color:#22c55e}
.badge{font-size:12px;background:#111c33;border:1px solid #26345c;padding:6px 10px;border-radius:999px;color:#a5b4fc}
.hero{max-width:900px;margin:0 auto;padding:28px 18px;text-align:center}
.hero h1{font-size:38px;line-height:1.05;margin:10px 0}
.hero h1 i{color:#38bdf8;font-style:normal}
.hero p{color:#94a3b8;font-size:16px;line-height:1.6;max-width:600px;margin:0 auto}
.card{max-width:720px;margin:22px auto;background:#0f172a;border:1px solid #1e293b;border-radius:20px;padding:18px}
.form{display:flex;gap:10px}
input{flex:1;background:#020617;border:1px solid #334155;color:white;padding:15px 16px;border-radius:12px;font-size:15px;outline:none}
button{background:#22c55e;color:#04120a;border:0;padding:0 22px;border-radius:12px;font-weight:800;font-size:15px;cursor:pointer}
.examples{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin-top:14px}
.examples button{background:#1e293b;color:#cbd5e1;font-weight:500;padding:7px 12px;font-size:13px}
PYEOFcat >> app.py << 'PYEOF'
.result{margin-top:16px;border-radius:14px;padding:18px;text-align:left}
.safe{background:#052e16;border:1px solid #16a34a}
.danger{background:#450a0a;border:1px solid #ef4444}
.result h2{margin:0;font-size:22px}
.meter{height:8px;background:rgba(255,255,255,.2);border-radius:999px;margin-top:12px;overflow:hidden}
.fill{height:100%;background:white;border-radius:999px}
.grid{max-width:900px;margin:10px auto 30px;padding:0 18px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.box{background:#0f172a;border:1px solid #1e293b;border-radius:16px;padding:16px}
.box b{display:block;margin-bottom:6px}
.box span{color:#94a3b8;font-size:13px;line-height:1.5;display:block}
.footer{text-align:center;color:#64748b;font-size:12px;padding-bottom:30px}
@media(max-width:650px){.hero h1{font-size:30px}.form{flex-direction:column}.grid{grid-template-columns:1fr}}
</style>
</head>
<body>
<div class="top"><div class="logo">🛡️ Phish<span>Guard</span></div><div class="badge">● LIVE PROTECTION</div></div>
<div class="hero">
<h1>Is this link <i>safe</i><br>or a trap?</h1>
<p>Paste any suspicious link before you click it. PhishGuard checks for fake logins, typosquatting, IP tricks and other phishing patterns.</p>
</div>
<div class="card">
<form method="POST" class="form">
<input name="url" placeholder="Paste URL here - e.g. https://paypal-secure-login.com" value="{{ url }}" required>
<button>Check →</button>
</form>
<div class="examples">
<button onclick="fill('https://google.com')">Try: google.com</button>
<button onclick="fill('http://paypal-secure-login-verify.com')">Try: fake PayPal</button>
<button onclick="fill('http://192.168.1.1/login')">Try: IP login</button>
</div>
{% if result %}
<div class="result {{ 'danger' if is_phishing else 'safe' }}">
<h2>{{ '🚨 PHISHING - DANGER' if is_phishing else '✅ SAFE - Looks Legit' }}</h2>
<p><b>{{ url }}</b><br>{{ 'Do NOT enter passwords or M-Pesa PIN on this site.' if is_phishing else 'No major phishing signals found. Still be careful.' }}</p>
<div class="meter"><div class="fill" style="width:{{ score * 10 }}%"></div></div>
<p style="font-size:13px">Risk Score: {{ score }} / 10</p>
</div>
{% endif %}
</div>
<div class="grid">
<div class="box"><b>🔍 Smart Checks</b><span>Checks length, @ symbols, IP addresses, suspicious words, HTTPS and more.</span></div>
<div class="box"><b>⚡ Instant</b><span>No signup. No download. Paste and get a verdict in under a second.</span></div>
<div class="box"><b>🔒 Private</b><span>We dont store your URLs. Check and go.</span></div>
</div>
<div class="footer">Built by Morgan • Phishing URL Detector • Stay safe online</div>
<script>function fill(v){document.querySelector('input[name=url]').value=v}</script>
</body>
</html>
"""
@app.route('/', methods=['GET','POST'])
def home():
    result = None
    score = 0
    url = ""
    is_phishing = False
    if request.method == 'POST':
        url = request.form['url'].strip()
        if url:
            score = train.score(url)
            is_phishing = score >= 5
            result = "PHISHING - DANGER" if is_phishing else "SAFE - Legit"
    return render_template_string(HTML, result=result, score=score, url=url, is_phishing=is_phishing)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
